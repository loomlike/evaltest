# LLM-as-Judge
Towards Robust and Impartial LLM Judgments.

## Components

### Judge Prompt Generator

* Interface to define the judge identity
* Interface to define the metrics definition
* Interface to define the scoring guideline
* Interface to add few shot judging examples

### Judge Functional Test

* Test utility functions

### Judge Bias Test

* Positional
* Verbosity
* Self-enhancement

To test these, set up an experiment as follows and run a Chi-square test.

- **Data**: 
- **Generation models**:
- **Judge models**:

You may repeat *n* times to ensure the results are consistent.

First, build a contingency table based on the judge scores, counting how many cases were won by generation models for each judge model.

| winner        | generation-model-x | generation-model-y | tie |
|---------------|---------------|-------------|-----|
| judge-model-a | 8             | 21          | 163 |
| judge-model-b | 11            | 18          | 163 |

Using this data, run the Chi-square test with the null hypothesis that *"the outcomes (generation-model-x win, generation-model-y win, or tie) are independent of the judges"*. If the p-value is less than the common significance level of 0.05, you can reject the null hypothesis and conclude that the results are dependent on the judges.

### Meta Evaluation

* Evaluation study UI
* Evaluation analysis utility functions
* Evaluation result dashboard 