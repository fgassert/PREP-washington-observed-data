
Scripts for preparing data to recreate these graphs based on data from Vose et al. (2014)

![graph]()

### Output files:

- [observed_temp.csv]()
- [observed_precip.csv]()

### Column names

Year: ```year```
Annual average: ```annual```
Trendline: ```trendline```
Baseline: ```baseline```

There are month columns as well but these can be ignored
The trendline shouldn't be shown on the precip graph as it is not significant

### Units

- observed_temp.csv: Degrees F
- observed_precip.csv: Inches of precip

### Build

Requires: curl, scipy, numpy, pandas, pylab

```
make clean; make
```
