
Scripts for preparing data to recreate these graphs based on data from Vose et al. (2014)

![graph](https://raw.githubusercontent.com/fgassert/PREP-washington-observed-data/master/Screen%20Shot%202016-05-03%20at%209.32.53%20PM.png)

Note: the caption contains a typo. Baselines reflect the entire period of 1895-2014, not 1950-1999

### Output files:

- [observed_temp.csv](https://raw.githubusercontent.com/fgassert/PREP-washington-observed-data/master/observed_temp.csv)
- [observed_precip.csv](https://raw.githubusercontent.com/fgassert/PREP-washington-observed-data/master/observed_precip.csv)

### Column names

Year: ```year```
Annual average: ```annual```
Trendline: ```trendline```
Baseline: ```baseline```

There are month columns as well but these can be ignored
The trendline shouldn't be shown on the precip graph as it is not significant

### Units

- observed_temp.csv: Degrees F
- observed_precip.csv: Inches of precipitation

### Build

Requires: curl, scipy, numpy, pandas, pylab

```
make clean; make
```
