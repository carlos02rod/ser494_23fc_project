#### SER494: Project Exploration
#### Inflation: its effects on consumer goods and confidence
#### Carlos Rodriguez
#### 10-08-2024

#### Dataset 1(Chicken-Report.xlsx): 
MD5 Hash: 68c0fe589bbb6913416fca464816b503
Site: https://www.bls.gov/data/home.htm#prices (Average price data - chicken)
Author: U.S. BUREAU OF LABOR STATISTICS
Constructed: 10/04/24
- Contains monthly figures on the average price of a pound of
chicken from 2014 to 2024(not seasonally adjusted).
- Contains over 120 unique figures to analyze
- They are categorized into per month figures, within each month is a integer number that takes the avg price 
combining all figures in the country.

#### Dataset 2(Electricity-Report.xlsx):
MD5 Hash: ec1dc075950fe49fc71388b05e9c513b
Site: https://www.bls.gov/data/home.htm#prices (Average price data - electricity)
Author: U.S. BUREAU OF LABOR STATISTICS
Constructed: 10/04/24
- Contains monthly figures on the average price of 1 KWK from 2014 to 2024(not seasonally adjusted).
- Contains over 120 unique figures to analyze
- They are categorized into per month figures, within each month is a integer number that takes the avg price 
combining all figures in the country.

#### Dataset 3(Gasoline-Report.xlsx): 
MD5 Hash: 7823fc56a57da1251b2d6b63e05aea31
Site: https://www.bls.gov/data/home.htm#prices (Average price data - gasoline)
Author: U.S. BUREAU OF LABOR STATISTICS
Constructed: 10/04/24
- Contains monthly figures on the average price of a gallon of gasoline from 2014 to 2024(not seasonally adjusted).
- Contains over 120 unique integer figures to analyze
- They are categorized into per month figures, within each month is a integer number that takes the avg price 
combining all figures in the country.

#### Dataset 4(Inflation-Report.xlsx): 
MD5 Hash: 854522bd809acfb5b34c1845ea72b008
Site: https://www.bls.gov/data/home.htm#prices ((All urban consumers) 12-month average CPI of all items)
Author: U.S. BUREAU OF LABOR STATISTICS
Constructed: 10/04/24
- Contains monthly figures of 12-month US inflation rate from 2014 to 2024(not seasonally adjusted).
- Contains over 120 unique integer figures to analyze
- They are categorized into per month figures, within each month is a integer number that takes the avg rate 
combining all figures in the country.

#### Dataset 5(Confidence-Report.csv): 
MD5 Hash: 9447485211a567adde4acfbad696c74f
Site: https://www.oecd.org/en/data/indicators/consumer-confidence-index-cci.html?oecdcontrol-b2a0dbca4d-var3=2014-10&oecdcontrol-b2a0dbca4d-var4=2024-06 (consumer confidence based off an index)
Author: Organisation for Economic Co-operation and Development
Constructed: 10/04/24
- Contains monthly figures of the Consumer-confidence index from 2014 to 2024(not seasonally adjusted).
- Contains over 120 unique integer figures to analyze. over 100 index means the consumer is confident, under means otherwise.
- They are categorized into per month figures, within each month is a integer number that takes into account the confidence of 
the people. 100 being the benchmark to go above or below (provides indication of future development).
- the 100 is an amplitude index allowing the long-term average to be 100

#### ---------------------------------------------------------------------------------------------------------

Each of these record contain a row of only 1 attribute since the data is split up amongst
multiple datasets/tables, it will be combined in processing.

#### Interpretable Record 1:
Chicken Price
Date: August 2021
Average Price: 1.472 per lbs.

Explanation: This value represents the average price in the U.S.
for a pound of chicken. Collected by a government agency this data
lets us track the price month-to-month to detect any significant changes.
Since chicken is usually a household item it was added as a indicator that 
consumers can relate to and better understand these trends.

#### Interpretable Record 2:
Inflation Rate
Date: August 2021
12-Month Inflation Rate: 5.3

Explanation: This value represents the 12-month average for the inflation rate in the
U.S. signifying an increase in price across the board in consumer goods. This indicator 
takes into account all aspects of consumers. From gas, toiletry's, bills, cars, etc. 5.3 is above 
average as for things go, and we can see an uptick in costs possibly signifying a decrease in consumer
confidence.


## Background Domain Knowledge
Inflation is a general economic indicator into how the economy is handling price of goods and overall stability.
For a while it has been seen as healthy for an economy to have a minor but steady inflation growth about 1-4 percent a year.
Some example where this is not a good thing is the Covid-19 pandemic. The virus not only hurt lives, 
but also decimated financial markets all over the world because of lack of supply of most goods. this in-turn plummeted consumer-confidence
and left in its wake a clear road into a recession. When inflation is high, people and governments spend less which eventually
leads to increase costs on essential goods and this leads into a slippery slope of issues.
For a while governments use interest rates to keep the inflation rate at bay and that is something we will be looking into
when performing our data evaluations. Some commodities like gasoline and chicken saw an increase in price during these times
because they are heavily dependent on economic conditions. These are 2 commodities that households within the country consistently 
purchase so consumers feel the effects of them the most. The datasets for this project, which include those described above and electricity,
as well as inflation rates and consumer confidence from 2014 to 2024, provide insights into the interplay between these factors
during a decade marked by significant economic change. The data collected by U.S. Bureau of Labor Statistics(BLS) reports on all these factors by a 
CPI index that aggregates all consumer data. Often times inflation doesn't affect all commodities the same, so comparing things like food to
gas will be an interesting analysis to visualize to see how the country is lacking in some aspects more than others. This allows us to see
weaknesses in supply chain and even demand. Going back to the federal interest rate talked about a bit ago, The Federal Reserve Bank(FRED) lowers rates
across the board to give companies incentive to spend and borrow money. the more money invested into projects are theoretically going back into the economy
and increasing commerce, giving the economy a boost and keeping inflation and confidence at good levels. Sometimes this isnt the case and causes more pain for the governments than how
it was before. We will be able to analyze this by referencing the Organisation for Economic Co-operation and Development(OECD) index where we can visually see
the overall anxiety of consumers across the country. An example where it fails is if the Federal reserve is already at a rate of .5 percent points. if they continue
lowering interest rates, and it reaches 0, it will decimate confidence because the only tool keeping inflation at bay has been lost, losing all leverage they had in recovering, leaving a scare in the market,
massive sale offs, layoffs and a stall in commercial spending. this of course is worst case scenario... but entirely possible...


U.S. Bureau of Labor Statistics. (2024). "Average price data - chicken." Retrieved from https://www.bls.gov/data/home.htm#prices

Organisation for Economic Co-operation and Development. (2024). "Consumer Confidence Index." Retrieved from https://www.oecd.org

Federal Reserve Bank of St. Louis. "Effective Federal Funds Rate (FEDFUNDS)." FRED, Federal Reserve Bank of St. Louis, n.d.,
https://fred.stlouisfed.org/series/FEDFUNDS.



## Dataset Generality
Datasets provided allow users of all paths an understanding into the complicated nature of economic stability in the U.S. A pound of chicken, Price per KwH, Gallon of gas,
are all things people from the U.S. understand far too well. We live off of these things and without them our world would cease to exist and the wheels of capitalism would soon follow.
They were chosen because of this generality so the visualization would provide a sobering thought to those who continue reading through this analysis.
The Consumer Confidence Index dataset allows the user to understand economic conditions at there respective times and shows how they felt toward spending toward these times. For Example,
if  the index was at 95, this would mean confidence was low/scared. people spent less, saved more, and were scared of what the future held, a sort of gloominess in the air. The user may
have not realized it, but they felt it deep down as well. Finally, the final dataset being our conclusion dataset that ultimately is what affects the rest of the datasets is Inflation. When people say
10 dollars 5 years ago is now worth 6 you can blame inflation. dollar amount left in the bank will naturally depreciate because of this and the price of goods like apples and bananas are just 2 products in a boatload
that get affected by it.


## Data Transformations
### Transformation N
**Description:** TODO
**Soundness Justification:** TODO
(duplicate above as many times as needed; remove this line when done)
## Visualizations
### Visual N
**Analysis:** TODO
(duplicate above as many times as needed; remove this line when done)