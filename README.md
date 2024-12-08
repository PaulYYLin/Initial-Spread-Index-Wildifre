# Description
Global Fire Weather Indices - ISI using overwintered DC start-up
Dataset: initial_spread_index_1979-2018.nc

Description:
This dataset was developed by Natural Resources Canada using the European Centre for Medium-range Weather Forecasts (ECMWF) ERA5-HRS Reanalysis product (C3S, 2017) as inputs to the Canadian Forest Fire Danger Rating System R Package (Wang et al. 2017).
ISI index is a numerical rating of the expected rate of firespread. It combines the effects of wind and FFMC on rate of spread without the influence of variable quantities of fuel.

Citation:
Megan McElhinny, Piyush Jain, Justin F. Beckers, Chelene Hanes, & Mike Flannigan. (2019). Global Fire Weather Indices - ISI using overwintered DC start-up (1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.3540920

# Data Processing
Using selfdefine nc_operation to manipulate the nc datatype (Geogrpraphic Data) to Clean, Group and Extract data with required condition.

# Insight Mining

<img width="1129" alt="image" src="https://github.com/user-attachments/assets/79b5c2de-86ac-4e2f-afb4-ed044ce4a296">

High-Risk Areas:
• The western and central regions of Alberta, show consistently high ISI values (red zones) across several years. These areas align with dense wildfire occurrences, indicating significant fire spread potential.

Low-Risk Areas:
• The eastern plains and southern regions exhibit consistently lower ISI values (yellow to light orange zones) across all years. Wildfires are sparse or absent in these regions, marking them as safer zones for citizens during fire-prone months.

Temporal Variability:
Fire-prone areas shift slightly year-to-year due to varying climate conditions. Years like 2011, 2015, and 2018 show widespread high ISI regions, while 2014 and 2016 exhibit subdued ISI values and fewer fire occurrences.

Correlations Between ISI and Wildfire Locations:
Most wildfires occur in regions with medium to high ISI values, underscoring the importance of ISI as an effective indicator of fire spread risk. However, occasional wildfires in low ISI areas suggest that other factors, such as ignition sources or wind, also contribute to fire risk.
