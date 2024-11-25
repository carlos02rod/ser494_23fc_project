#### SER494: Machine Learning Evaluation
#### (Inflation: its effects on consumer confidence)
#### (Carlos Rodriguez)
#### (11/24/24)


## Evaluation Metrics
### Metric 1
**Name:** (MSE)

**Choice Justification:** When analyzing our linear regression models we want
to limit larger error cases and have a better collective understanding of what our average
looks like.

**Interpretation:** The lower the number is the better are predictions are actually predicting.
larger numbers basically tell us that we are far off what the actual value should be.

### Metric 2
**Name:** (MAE)

**Choice Justification:** Since we are using linear regression within our models,
it would contain the representation of the average magnitude of the errors within our 
prediction. where it differs from MSE is how it treats error cases, its almost binary.

**Interpretation:** again, the lower, the better. Since its now looking for absolute our data
leaves out some outliers and just shows us how close our predictions actually are.

### Metric 3
**Name:** (MedAE)

**Choice Justification:** Instead of looking at just the mean of the data MedAE lets us
look into the median of the data so the data can be more focused on the median predictions.

## Alternative Models
### Alternative Ridge Regression
**Construction:** Ridge estimates coefficients of different regression
models if a correlation exists with the independent variables. This will be using L2.
**Evaluation:** This model didn't do as good as the linear counterparts, and its having
trouble finding any significant patterns within the training.

### Alternative Lasso
**Construction:**  by preventing overfitting we can have more specific predictions compared
to linear regression
**Evaluation:** This model performed worse than Ridge model, and it can be attributed to something
having to do with the datasets. a fix to this cn be fine-tuning the alpha variable to find the best one.

## Best Model
**Model:** all_vs_confidence 