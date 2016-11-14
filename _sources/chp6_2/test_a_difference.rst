
Testing for a Difference in Two Population Means (Assuming Independent Samples)
-------------------------------------------------------------------------------

**Back to Example 6.5:** Carry out the hypothesis test associated with
the following research question: Is the average birth weight lower when
mothers are classified as smokers?

**Step 0:** Check the assumptions behind the test to be sure that the t-test is valid.

1. Are the two groups independent? Explain.

2. Are both sample sizes sufficiently large? If not, is it reasonable to assume that both populations are normally distributed?

|image616|

**Step 1:** Convert the research question into H\ :sub:`0` and H\ :sub:`a`.

H\ :sub:`0`:

H\ :sub:`a`:

**Step 2:** Calculate the *test statsitic* from your data.

To do this in JMP, click on the red drop-down arrow next to "Oneway Analysis..."
and select **t-test**.

|image6124|

JMP returns the following:

|image6110|

Verify the value of the test statistic in JMP:


|image618|

.. math::

    SE_{\bar{x}_1-\bar{x}_2} = \sqrt{\frac{s_1^2}{n_1}+ \frac{s_2^2}{n_2}}\\
    t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{SE_{\bar{x}_1-\bar{x}_2}}


**Step 3:** Determine the *p-value*.

|image619|

*p-value*:

**Step 4:** Write a conclusion in terms of the original research question.

    "We have evidence that the average birth weight is lower when mothers are classified as smokers (p-value = .0038)."

