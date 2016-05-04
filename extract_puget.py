#!/usr/bin/env python

import pandas as pd
import numpy as np
import scipy.stats
import sys
import pylab

REGIONCODE = '4503' # puget sound lowlands
PRECIPNCODE = '01' # precipitation
TEMPCODE = '02'
NULLVALUE = -9.99
MINYEAR = 1895
MAXYEAR = 2015

def read_precip(infile, outcsv, varcode):
    years = []
    monthlist = []
    with open(infile) as f:
        for line in f.readlines():

            # extract region from [0:4]
            if line[:4] == REGIONCODE:

                # [4:6] should equal VARIABLECODE

                # extract year from [6:10]
                year = int(line[6:10])
                if year >= MINYEAR and year <= MAXYEAR:
                    years.append(year)
                    months = np.empty(12)

                    # extract monthly values
                    for i in range(12):
                        begin = 10 + i*7
                        end = 17 + i*7
                        val = float(line[begin:end].strip())
                        if val==NULLVALUE: val = np.nan
                        months[i] = val

                    monthlist.append(months)

    # assemble table
    df = pd.DataFrame(monthlist, columns=np.arange(12), index=years)
    df.index.name = 'year'

    # compute annual means
    df['annual'] = np.mean(df,1)

    # compute 1950-1999 baseline
    df['baseline'] = np.mean(df['annual'])

    if varcode == '01':
        #convert feet to inches
        df = df*12.0
    elif varcode == '02':
        pass

    # compute slope
    s,i,r,p,sd = scipy.stats.linregress(df.index, df['annual'])
    print "P-value: {}".format(p)

    df['trendline'] = df.index*s + i

    pylab.plot(df.index, df['annual'], '-')
    pylab.plot(df.index, df['trendline'], '-')
    pylab.plot(df.index, df['baseline'], '-')
    pylab.show()

    # dump to csv
    df.to_csv(outcsv)

if __name__ == "__main__":
    read_precip(*sys.argv[1:])
