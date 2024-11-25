#### SER494: Experimentation
#### (inflation: its effects on consumer confidence)
#### (Carlos Rodriguez)
#### (11/24/24)


## Explainable Records
### Record 1
**Raw Data:**

Inflation Rate: 2.5%
Gasoline Price: $2.887 per gallon
Electricity per KWH: $0.136
Chicken cost: $1.444 per pound

Output:
Consumer Confidence Index (CCI): 100.49929948778527

**Prediction Explanation:**
The CCI value of 100.4993 indicates that the provided data shows that the
consumer confidence is somewhat optimistic and shows people arent too confident
but are willing to spend on day-to-day supplies without issue.
Not very bullish but it's a stable level.

### Record 2
**Raw Data:**
Inflation Rate: 7.9%
Gasoline Price: $3.592 per gallon
Electricity per KWH: $0.148
Chicken cost: $1.632 per pound

Output:
Consumer Confidence Index (CCI): 98.41365678614002

**Prediction Explanation:**
The CCI value of 98.41365678614002 indicates that the provided data shows that the
consumer confidence is below normal levels. FYI, anything at 100 or above is what we are looking for,
anything below shows that confidence levels are not so good and might reduce consumer spending, stalling
the economic engine. 98 is pushing it and may lead to continued downturn and every day americans
feelings the effects of a recession.


## Interesting Features
### Feature A
**Feature:** 
Inflation Rate

**Justification:**
Inflation is directly responsible for impacting cost of goods across all sectors,
your average citizen sees this change in everyday products and features that we used to build our model.
You can see its importance by how accurate and low the error threshold is representing that this is a
major factor for consumer confidence and price of goods.

### Feature B
**Feature:** 
Consumer Confidence Index (CCI)

**Justification:**
CCI is responsible for putting current economic conditions on a scale we can understand. Its influence on the model
can show us its effects on mentalities of customers and spending. This is great to know because it can give us sentiment 
of a large group of people and in our case those who spend and live in the US.


## Experiments 
### Varying A: 
Inflation Rate

**Prediction Trend Seen:**
As inflation rates increased from 1% to 7%, economic strain is shown in our CCI indicator
leading to the CCI falling below 98 which is negative sentiment.

### Varying B:
Consumer Confidence Index

**Prediction Trend Seen:** 
Increasing CCI values corresponded to a lowering of inflation between 0 and 3 percent,
and household goods falling to average or below levels.

### Varying A and B together
**Prediction Trend Seen:**
With an increase in inflation and a decrease in CCI we can predict prices of goods to go up and
a slippery slope effect on our 2 features

### Varying A and B inversely
**Prediction Trend Seen:** With a decrease in inflation and increase in CCI we see consumers very confident
and are likely to splurge on items that arent necessarily needed.

### Varying A and B
**Prediction Trend Seen:** if we increase inflation but also increase CCI we see a weird effect where things are
getting more expensive but the consumer is still confident in the system and is still spending
this can probably be because most americans are getting paid more or some sort of incentive to spend
more is existing and hasn't been taken into account.
