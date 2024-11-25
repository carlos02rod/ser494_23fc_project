#### SER494: Project Proposal
#### Inflation: its effects on consumer goods and confidence
#### Carlos Rodriguez
#### 10-22-2024


#### Keywords: 
consumer-confidence, inflation, economic-stability


#### Description: 
This project will analyze the effects of inflation on key consumer goods categories such as fuel, groceries, 
and household bills, assessing how these rising costs affect consumer behavior.
The analysis will focus on identifying general patterns in how prices in these categories have changed with 
inflation and seeing if we can predict these changes. In addition, the project will compare these results with
consumer confidence indexes to understand whether consumer spending behavior aligns with economic outlook,
especially during times of duress and uncertainty. To further increase the usefulness of our analysis we will be
implementing regression to predict economic strain on the everyday consumer and whether they reach a tipping point.


#### Research Questions: 
RO1: To describe the trends between inflation rate data to price of essential consumer goods like Gas, electricity,etc.
Focusing on how over time these trends align with shifting consumer confidence.

RO2(Regression): To predict the confidence/economic strain value on consumers by considering inflation rates, gas, 
and previous confidence levels.

RO3: To defend our regression implementation used in RO2 we will do cross-validation with existing consumer confidence values and
analyze compared to other related datasets to ensure the reliability of our regression.

RO4: to defend our regression of economic strain, we evaluate the relationships between inflation rates and consumer spending behavior 
performing the prediction in RO2 which allows us to analyze regressions performance.


#### Intellectual Merit: 
This comparison will help us identify whether there is a discrepancy between rising costs and 
consumer spending, giving us insights into consumer resilience or strain under pressure. Uncovering 
potential patterns into how consumers reach can help us in developing a key(line of resistance) in which we 
can create a threshold where things might go south and be able to predict outcomes or tipping points in each
of our 3 categories. With this insight we are able to see thresholds where things appear to be "over-extended",
"stable", and "dire". After discovering patterns we can create a regression model that can gauge how much consumers are strapped for cash
and whether this is an insight that involves consumer-confidence levels.


#### Data Sourcing: 
Alot of this data is available publicly by the US 
government, one of those being the Federal Reserve which will be one of our main data retrieval points because of 
its influence on the economy and industries. Sticking to data provided to this will help us
keep data consistent and faultless.

Consumer Expenditure Survey: 
gives us official data from the government within many categories, some of those being Income before taxes, 
Consumer price data, employment data, etc.
https://www.bls.gov/data/
 
Federal Reserve Economic Data: 
gives us official inflation data, along with interest rates and consumer data
https://www.federalreserve.gov/releases/g19/default.htm

Bureau of Economic Analysis: 
Provides official data on consumption/price data on sectors pertaining to consumers (gas, groceries, bills)
https://www.bea.gov/data/industries

The data above was previously used within a time-series setting but can be easily transformed to remove the time element
and strictly keep the aggregated/average data.


#### Background Knowledge:
How should we measure Consumer Confidence - Jeff Domini, insight into how confidence is measured and the things
we must take into account to develop a clear understanding.
https://www.aeaweb.org/articles?id=10.1257/0895330041371303

Relationship between inflation and economic growth - V Gokal, analyzing the partnership or similar patterns 
between inflation and economic indicators.
https://www.academia.edu/download/55760736/2004_04_wp.pdf
https://catalogue.nla.gov.au/catalog/3548174

Why Is Food Still So Expensive? - Taryn Phaneuf, others factors attribute to increased prices and this article
outlines some of those and even those attributes have reasons of their own, but they all have a root problem and
I hope it has to do with inflation.
https://www.nerdwallet.com/article/finance/price-of-food


#### Related Work:
Curtin, R. Consumer Confidence in the 21st Century. Survey Research Center (2021). 
https://data.sca.isr.umich.edu/fetchdoc.php?docid=26457

Eggoh, J. C. Nonlinear relationship between inflation and economic growth.(2014).
https://www.sciencedirect.com/science/article/pii/S1090944314000027

European Commission. Insights from the Commission’s consumer survey. (2023).
https://ec.europa.eu/economy_finance/forecasts/2023/summer/Box_1_1%20Insights%20from%20the%20Commissions%20consumer%20survey%20how%20inflation%20is%20shaping%20consumer.pdf

Journal of Family Psychology. Economic strain and quality of life among families with emerging adult children. (2023). 
https://onlinelibrary.wiley.com/doi/full/10.1111/famp.12884

Deloitte. United States Economic Forecast.(2023).
https://www2.deloitte.com/us/en/insights/economy/us-economic-forecast/united-states-outlook-analysis.html

Antor, S. A. K. Relationship between inflation and economic growth.(2018).
https://www.academia.edu/35881031/RELATIONSHIP_BETWEEN_INFLATION_AND_ECONOMIC_GROWTH