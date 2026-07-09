# PPP conversion factor for private consumption - Data package

This data package contains the data that powers the chart ["PPP conversion factor for private consumption"](https://ourworldindata.org/grapher/ppp-conversion-factor-for-private-consumption?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website. It was downloaded on June 19, 2026.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For most countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The final column is the data column, which is the time series that powers the chart. If the CSV data is downloaded using the "full data" option, then the column corresponds to the time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data column is transformed depending on the chart type and thus the association with the time series might not be as straightforward.


## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

## Detailed information about the data


## PPP conversion factor, private consumption (LCU per international $)
Last updated: February 27, 2026  
Next update: February 2027  
Date range: 1990–2024  
Unit: LCU per international $  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
ICP, Eurostat PPP Programme, and OECD PPP Programme, via World Bank (2026) – processed by Our World in Data

#### Full citation
ICP, Eurostat PPP Programme, and OECD PPP Programme, via World Bank (2026) – processed by Our World in Data. “PPP conversion factor, private consumption (LCU per international $)” [dataset]. ICP, Eurostat PPP Programme, and OECD PPP Programme, via World Bank, “World Development Indicators 125” [original data].
Source: ICP, Eurostat PPP Programme, and OECD PPP Programme, via World Bank (2026) – processed by Our World In Data

### How is this data described by its producer - ICP, Eurostat PPP Programme, and OECD PPP Programme, via World Bank (2026)?
The purchasing power parity (PPP) conversion factor is a currency conversion factor and a spatial price deflator. They convert different currencies to a common currency and, in the process of conversion, equalize their purchasing power by eliminating the differences in price levels between countries, thereby allowing volume or output comparisons of gross domestic product (GDP) and its expenditure components. This conversion factor is for household final consumption expenditure and the base currency is the US dollar.

### Aggregation method:
No aggregation provided for this indicator.

### Statistical concept and methodology:
Methodology: The International Comparison Program (ICP) estimates PPPs for the world’s countries. The ICP is conducted as a global partnership of countries, multilateral agencies, and academia. The 2021 ICP comparison covered 176 countries, including 49 Eurostat-OECD countries. For countries that have not participated in ICP comparisons, the PPP are imputed based on a regression model.

ICP-estimated PPPs cover years from 2011 to 2021. WDI extrapolates 2011 PPPs for years earlier years, and 2021 PPPs for later years. Description of WDI extrapolation approach is available here: https://datahelpdesk.worldbank.org/knowledgebase/articles/665452-how-do-you-extrapolate-the-ppp-conversion-factors

For the member countries of Eurostat-OECD PPP Programme, PPP conversion factors are periodically updated based on the organizations’ databases. For Eurostat-OECD PPP Programme, please refer to the following websites.
(http://www.oecd.org/sdd/prices-ppp/)
(https://ec.europa.eu/eurostat/web/purchasing-power-parities/overview)

For more information on the ICP and PPPs, please refer to the ICP website at https://www.worldbank.org/en/programs/icp.
Statistical concept(s): PPPs are primarily used to convert the national accounts data of economies, such as GDP and its expenditure components, into a common currency. In the process of conversion, they control for differences in the price levels of economies, and thus equalize purchasing power. PPP-based comparisons of economic output differ from market exchange rate-based comparisons as the latter do not distinguish between the relative price levels of different items in economies. Overall price levels are normally higher in higher-income economies than they are in lower-income economies (Balassa-Samuelson effect), mostly because of the large differences in price levels for non-traded products. If no account is taken of the larger price level differences for non-traded products when converting GDP to a common currency, the size of higher-income economies with high price levels will be overstated and the size of lower-income economies with low price levels will be understated. No distinction is made between traded products and non-traded products when market exchange rates are used to convert GDP to a common currency: the rate is the same for all products. PPP-converted GDP does not have this bias because PPPs account for the different price levels of traded products and non-traded products. Thus, PPPs are more appropriate for comparing the output of economies and the average material well-being of their inhabitants and are also less impacted by the potential volatility of market exchange rates.

PPPs are calculated by the International Comparison Program (ICP) based on the prices of goods and services within an economy and national accounts expenditures. See https://www.worldbank.org/en/programs/icp/methodology.

### Development relevance:
PPPs are used to convert national accounts data from different countries, such as GDP and its expenditure components, into a common currency, while also eliminating the effect of price level differences between countries. PPPs are also used to derive price level indexes (PLIs), the ratio of a country’s PPP to its market exchange rate, to directly compare price levels across countries.
PPPs, PLIs, and the PPP-based expenditures to which they give rise are primarily used to make spatial comparisons of volume and per capita consumption or levels of GDP and its expenditure components across countries. PPP-based indicators are used for national, regional, and global policy making and analysis across the socioeconomic spectrum from poverty and inequality, to health and education, to energy and climate, through to economic growth, labor, productivity, trade, competitiveness, and infrastructure. A number of Sustainable Development Goals use PPP-based indicators to measure development progress.
- Recommended uses of PPPs include: to make spatial comparisons of GDP and its expenditure components; to make spatial comparisons of price levels; and to group countries by their per capita volume indexes and price level indexes.
- Recommended uses of PPPs with limitations include: to analyze changes over time in relative GDP per capita and relative prices; to analyze price convergence; to make spatial comparisons of the cost of living; and to use PPPs calculated for GDP and its expenditure components as deflators for other values.

### Limitations and exceptions:
Global PPP estimates provided by ICP are produced by the ICP Global Office and regional implementing agencies, based on data supplied by the national implementing agencies in the participating economies, and in accordance with the methodology recommended by the ICP Technical Advisory Group and approved by the ICP Governing Board. As such, these results are not produced by participating economies as part of their national official statistics.

PPPs are not recommended to be used as: a precise measure to establish strict rankings of countries; a means of constructing national growth rates; a measure to generate output and productivity comparisons by industry; an indicator of the undervaluation or overvaluation of currencies; and as an equilibrium exchange rate.

### Source

#### ICP, Eurostat PPP Programme, and OECD PPP Programme, via World Bank – World Development Indicators
Retrieved on: 2026-02-27  
Retrieved from: https://data.worldbank.org/indicator/PA.NUS.PRVT.PP  


    