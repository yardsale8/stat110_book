
Example 6.6: Time Perception 
+++++++++++++++++++++++++++++

Recall the study conducted by researchers at Pennsylvania State University which
investigated whether time perception, a simple indication of a person’s ability
to concentrate, is impaired during nicotine withdrawal. This study was discussed
in Chapter 5. Twenty smokers were randomly assigned to a 24-hour smoking
abstinence and were asked to estimate how much time had passed during a
45-second period. Another 20 smokers were randomly assigned to a group which was
*not* forced to abstain from nicotine; they were also asked to estimate how much
time had passed during a 45-second period. Suppose the resulting data on
perceived elapsed time (in seconds) were analyzed as shown below (these results
are artificial but are similar to the actual findings). The data can be found in
the file **Nicotine\_all.JMP**.

.. admonition:: Research Question: 

    Do those smokers suffering from nicotine withdrawal tend to believe that
    more time has elapsed than do those not suffering from nicotine withdrawal?

.. admonition:: Questions:

    1. What is the response variable in this study?

    2. What is the predictor variable in this study?

The data can be summarized using JMP by selecting **Analyze > Fit Y by
X** and placing the predictor (i.e., explanatory) variable in the **X,
Factor** box and the response in the **Y, Response** box. Then, use the
**Display Options** menu from the red drop-down arrow to add the
boxplots and mean diamonds.

    |image6111|

It is clear that the SAMPLE of smokers suffering from nicotine
withdrawal has a larger mean perceived elapsed time than those not
suffering from withdrawal. However, to determine whether there is a
difference in the POPULATION means, we will carry out a hypothesis test.


**Step 0:** Check the assumptions behind the test to be sure that the test is valid.

            1. Are the two groups independent?

            2. Are both sample sizes sufficiently large? If not, is it reasonable to assume that both populations are normally distributed?

            |image6112|

**Step 1:** Convert the research question into H\ :sub:`0` and H\ :sub:`a`

            H\ :sub:`0`

            H\ :sub:`a`

**Step 2:** Calculate a *test statistic* from your data.

            |image6113|

            Verify the value of the test statistic from JMP:
            |image6114|

            .. math::

                SE_{\bar{x}_1-\bar{x}_2} = \sqrt{\frac{s_1^2}{n_1}+ \frac{s_2^2}{n_2}}= \\
                t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{SE_{\bar{x}_1-\bar{x}_2}}=

            Recall that this test statistic comes from a t-distribution w

            .. math::

                df = \frac{\left(\frac{s_1^2}{n_1}+ \frac{s_2^2}{n_2}\right)^2}
                          {\frac{\left(\frac{s_1^2}{n_1}\right)^2}{n_1 - 1}+ 
                          \frac{\left(\frac{s_2^2}{n_2}\right)^2}{n_2 - 1}}=37.9

**Step 3:** Determine the *p-value*

            |image6115|

            p-value = 

**Step 5:** Write a conclusion in terms of the original research question.

            “The study provides evidence that the average perceived elapsed time is higher for those smokers suffering from nicotine withdrawal than for those not suffering from nicotine withdrawal (p-value = .0042)


Finally, construct a 95% confidence interval for the difference in
means:

|image6116|

Lower Endpoint =

Upper Endpoint =

Again, we often write this confidence interval as:

Interpret the meaning of this confidence interval:

