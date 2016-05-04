#!/usr/bin/make

URL = ftp://ftp.ncdc.noaa.gov/pub/data/cirs/climdiv/
DATEFILE = procdate.txt
PRECIP = climdiv-pcpndv-v1.0.0-
TEMP = climdiv-tmpcdv-v1.0.0-
DATESTAMP := $(shell curl $(URL)$(DATEFILE))

PRECIP_CSV = observed_precip.csv
TEMP_CSV = observed_temp.csv

all: $(PRECIP_CSV) $(TEMP_CSV)

$(PRECIP_CSV): $(PRECIP)$(DATESTAMP) extract_puget.py
	python extract_puget.py $< $@ 01

$(TEMP_CSV): $(TEMP)$(DATESTAMP) extract_puget.py
	python extract_puget.py $< $@ 02

$(PRECIP)$(DATESTAMP):
	curl -O $(URL)$@

$(TEMP)$(DATESTAMP):
	curl -O $(URL)$@

.SECONDARY: *

.PHONY: clean

clean:
	rm -f $(PRECIP_CSV) $(TEMP_CSV)
