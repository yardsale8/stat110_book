Chapter 6 Part 2
================

***COMPARING TWO POPULATION MEANS: INDEPENDENT SAMPLES***

In Chapter 5, we considered inference for a single population mean.
Then, in the first part of Chapter 6 we extended these ideas so that
comparisons could be made between two groups. Such comparisons were made
using differences because the observations in the two groups were
related, or *dependent*.

In this section, we will consider making comparisons between two groups
when the observations in one group are *independent* of the observations
in the other group. The methodologies considered here are a bit more
involved because it no longer makes sense to simply work with
differences. Consider the following example.

**Example 6.5:** A study was conducted in which the relationship between
smoking and birth weights of babies was considered. The data can be
found in the file **LowBirth.JMP**, a portion of which is shown below.

|image0|

*Comment*: The first observation for a nonsmoker is in NO WAY related to
the first observation for a smoker. Therefore, these groups are
*independent*.

Next, let’s examine birth weight across the two groups: smokers and
nonsmokers.

|image1|\ |image2|

In JMP, we can compare the distributions by selecting **Analyze > Fit Y
by X.** Place the categorical variable (**Smoke**) in the **X, Factor**
box, and place the numerical variable of interest (**Actual\_Weight**)
in the **Y, Response** box. Select the “Display Options” menu from the
red drop-down arrow to display the boxplots and mean diamonds.

|image3|

|image4|\ *
*

*
Questions*:

1. Identify the following sample statistics from the JMP output:

+----------------------+---------------------+-----------------+
|                      | Sample Statistics   |
+======================+=====================+=================+
|                      | Group 1             | Group 2         |
|                      |                     |                 |
|                      | (Smokers)           | (Nonsmokers)    |
+----------------------+---------------------+-----------------+
| Mean                 |                     |                 |
+----------------------+---------------------+-----------------+
| Standard Deviation   | s\ :sub:`1` =       | s\ :sub:`2` =   |
+----------------------+---------------------+-----------------+
| # of Observations    | n\ :sub:`1` =       | n\ :sub:`2` =   |
+----------------------+---------------------+-----------------+

1. We are interested in the true difference between these two population
   means, . Based on the data, what is your best guess for this
   difference, and what does it indicate about birth weights for smokers
   compared to nonsmokers?

2. If you were to take another sample, is your “best guess” from the
   previous question likely to change? Explain.

*
*

| Since the difference will change from sample to sample, in order to
  make valid inferences about the true population difference, we must
  first understand *how* the difference in sample means is expected to
  change from sample to sample. That is, we must determine what
  differences in means are likely to happen by chance when taking random
  samples from populations with the same mean. The following
  illustration in Tinkerplots gives us some insight into this.
| |image5|

***Characteristics of the Sampling Distribution for the Difference in
Means ***

The illustration in Tinkerplots helps us understand the intuition behind
inference for a difference in means, but we don’t really need
Tinkerplots to determine the characteristics of a distribution of
differences in means. Instead, we can use what statisticians discovered
long ago: as long as the samples are independent, the sampling
distribution for the *difference in means* can be described as follows.

1. The sampling distribution is centered around μ\ :sub:`1` –
   μ\ :sub:`2`.

2. The standard deviation of our sampling distribution (i.e., standard
   error) is given as follows:

3. The shape of the sampling distribution is approximately normal if (1)
   both sample sizes are “sufficiently large” OR (2) if both original
   populations are normally distributed.

Given these characteristics, the test statistic we will use when testing
for differences in two population means for INDEPENDENT samples is as
follows:

This test statistic follows a t-distribution with the following degrees
of freedom:

Therefore, as long as it is reasonable to assume the shape of the
distribution of differences in means is approximately normal (see #3
above), we can use the t-distribution to find our p-value. This
procedure is typically referred to as the **two-sample t-test**.\ ***
***

***Testing for a Difference in Two Population Means (Assuming
Independent Samples)***

**Back to Example 6.5:** Carry out the hypothesis test associated with
the following research question: Is the average birth weight lower when
mothers are classified as smokers?

+---------------+-----------------------------------------------------------------------------------------------------------------------------------+
| **Step 0:**   | Check the assumptions behind the test to be sure that the t-test is valid.                                                        |
|               |                                                                                                                                   |
|               | 1. Are the two groups independent? Explain.                                                                                       |
|               |                                                                                                                                   |
|               | 2. Are both sample sizes sufficiently large? If not, is it reasonable to assume that both populations are normally distributed?   |
|               |                                                                                                                                   |
|               | |image6|                                                                                                                          |
+===============+===================================================================================================================================+
| **Step 1:**   | Convert the research question into H\ :sub:`0` and H\ :sub:`a`.                                                                   |
|               |                                                                                                                                   |
|               | H\ :sub:`0`:                                                                                                                      |
|               |                                                                                                                                   |
|               | H\ :sub:`a`:                                                                                                                      |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------+
| **Step 2:**   | Calculate a *test statistic* from your data.                                                                                      |
|               |                                                                                                                                   |
|               | To do this in JMP, click on the red drop-down arrow next to “Oneway Analysis…” and select **t-test**.                             |
|               |                                                                                                                                   |
|               | JMP returns the following:                                                                                                        |
|               |                                                                                                                                   |
|               | |image7|                                                                                                                          |
|               |                                                                                                                                   |
|               | Verify the value of the test statistic from JMP:                                                                                  |
|               |                                                                                                                                   |
|               | |image8|                                                                                                                          |
|               |                                                                                                                                   |
|               |     Recall that this test statistic comes from a t-distribution with                                                              |
|               |                                                                                                                                   |
|               |     168.419                                                                                                                       |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------+
| **Step 3:**   | Determine the *p-value*.                                                                                                          |
|               |                                                                                                                                   |
|               | |image9|                                                                                                                          |
|               |                                                                                                                                   |
|               | *p-value*:                                                                                                                        |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------+
| **Step 4:**   | Write a conclusion in terms of the original research question.                                                                    |
|               |                                                                                                                                   |
|               | “We have evidence that the average birth weight is lower when mothers are classified as smokers (p-value = .0038).”               |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------+

***
***

***Constructing a Confidence Interval for the Difference in Means
***

|image10|

Lower Endpoint =

Upper Endpoint =

| We often write this confidence interval as:
| Interpret the meaning of this 95% confidence interval:

**
**

**
**

**
**

**Example 6.6:** Recall the study conducted by researchers at
Pennsylvania State University which investigated whether time
perception, a simple indication of a person’s ability to concentrate, is
impaired during nicotine withdrawal. This study was discussed in Chapter
5. Twenty smokers were randomly assigned to a 24-hour smoking abstinence
and were asked to estimate how much time had passed during a 45-second
period. Another 20 smokers were randomly assigned to a group which was
*not* forced to abstain from nicotine; they were also asked to estimate
how much time had passed during a 45-second period. Suppose the
resulting data on perceived elapsed time (in seconds) were analyzed as
shown below (these results are artificial but are similar to the actual
findings). The data can be found in the file **Nicotine\_all.JMP**.

*Research Question*: Do those smokers suffering from nicotine withdrawal
tend to believe that more time has elapsed than do those not suffering
from nicotine withdrawal?

*Questions*:

1. What is the response variable in this study?

2. What is the predictor variable in this study?

The data can be summarized using JMP by selecting **Analyze > Fit Y by
X** and placing the predictor (i.e., explanatory) variable in the **X,
Factor** box and the response in the **Y, Response** box. Then, use the
**Display Options** menu from the red drop-down arrow to add the
boxplots and mean diamonds.

    |image11|

It is clear that the SAMPLE of smokers suffering from nicotine
withdrawal has a larger mean perceived elapsed time than those not
suffering from withdrawal. However, to determine whether there is a
difference in the POPULATION means, we will carry out a hypothesis test.

+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Step 0:**   | Check the assumptions behind the test to be sure that the test is valid.                                                                                                                                        |
|               |                                                                                                                                                                                                                 |
|               | 1. Are the two groups independent?                                                                                                                                                                              |
|               |                                                                                                                                                                                                                 |
|               | 2. Are both sample sizes sufficiently large? If not, is it reasonable to assume that both populations are normally distributed?                                                                                 |
|               |                                                                                                                                                                                                                 |
|               | |image12|                                                                                                                                                                                                       |
+===============+=================================================================================================================================================================================================================+
| **Step 1:**   | Convert the research question into H\ :sub:`0` and H\ :sub:`a`.                                                                                                                                                 |
|               |                                                                                                                                                                                                                 |
|               | H\ :sub:`0`:                                                                                                                                                                                                    |
|               |                                                                                                                                                                                                                 |
|               | H\ :sub:`a`:                                                                                                                                                                                                    |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Step 2:**   | Calculate a *test statistic* from your data.                                                                                                                                                                    |
|               |                                                                                                                                                                                                                 |
|               | |image13|                                                                                                                                                                                                       |
|               |                                                                                                                                                                                                                 |
|               | | Verify the value of the test statistic from JMP:                                                                                                                                                              |
|               | | |image14|                                                                                                                                                                                                     |
|               |                                                                                                                                                                                                                 |
|               |     Recall that this test statistic comes from a t-distribution with                                                                                                                                            |
|               |                                                                                                                                                                                                                 |
|               |     37.9998                                                                                                                                                                                                     |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Step 3:**   | Determine the *p-value*.                                                                                                                                                                                        |
|               |                                                                                                                                                                                                                 |
|               | |image15|                                                                                                                                                                                                       |
|               |                                                                                                                                                                                                                 |
|               | *p-value*:                                                                                                                                                                                                      |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Step 5:**   | Write a conclusion in terms of the original research question.                                                                                                                                                  |
|               |                                                                                                                                                                                                                 |
|               | “The study provides evidence that the average perceived elapsed time is higher for those smokers suffering from nicotine withdrawal than for those not suffering from nicotine withdrawal (p-value = .0042).”   |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Finally, construct a 95% confidence interval for the difference in
means:

|image16|

Lower Endpoint =

Upper Endpoint =

Again, we often write this confidence interval as:

Interpret the meaning of this confidence interval:

**
**

**Example 6.7:** Consider the data found in the file **NYC\_Trees.JMP**.
Suppose you want to compare the canopy area of the two types of trees.
Is the average canopy area of a Honey Locust different from the average
canopy area of a Norway Maple? The data are summarized as follows:

    |image17|

It is clear that the SAMPLE of Norway Maple trees has a higher mean
canopy area than the SAMPLE of Honey Locust trees. However, to determine
whether the POPULATION mean canopy areas differ between the two groups,
we will carry out a hypothesis test.

+---------------+-----------------------------------------------------------------------------------------------------------------------------------+
| **Step 0:**   | Check the assumptions behind the test to be sure that the test is valid.                                                          |
|               |                                                                                                                                   |
|               | 1. Are the two groups independent?                                                                                                |
|               |                                                                                                                                   |
|               | 2. Are both sample sizes sufficiently large? If not, is it reasonable to assume that both populations are normally distributed?   |
|               |                                                                                                                                   |
|               | |image18|                                                                                                                         |
+===============+===================================================================================================================================+
| **Step 1:**   | Convert the research question into H\ :sub:`0` and H\ :sub:`a`.                                                                   |
|               |                                                                                                                                   |
|               | H\ :sub:`0`:                                                                                                                      |
|               |                                                                                                                                   |
|               | H\ :sub:`a`:                                                                                                                      |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------+
| **Step 2:**   | Calculate a *test statistic* from your data.                                                                                      |
|               |                                                                                                                                   |
|               | |image19|                                                                                                                         |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------+
| **Step 3:**   | Determine the *p-value*.                                                                                                          |
|               |                                                                                                                                   |
|               | *p-value*:                                                                                                                        |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------+
| **Step 4:**   | Write a conclusion in terms of the original research question.                                                                    |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------+

Finally, we can construct a confidence interval for the difference in
means:

|image20|

Lower Endpoint =

Upper Endpoint =

This confidence interval can also be written as:

Interpret the meaning of this 95% confidence interval:

***
Nonparametric Tests***

These tests are an alternative to the two-sample t-test for comparing
the “average” value of two populations where the samples from each
population are taken independently. This test is appropriate when the
assumption of normality is violated (as it may have been in the previous
example). To obtain the output for these tests, simply select
**Nonparametric >** from the drop-down menu in the upper left-hand
corner of the boxplots.

|image21|

JMP returns the following output when the Wilcoxon Test is selected:

|image22|

The decision based on Wilcoxon’s test is the same decision that we
arrived at using the standard two-sample t-test above. Often, these
procedures will agree each other because the above t-test is robust to
(i.e. not greatly affected by) departures from normality.

**
**

***The t-Test for Independent Samples Assuming Equal Variances
***

The two-sample t-test that we discussed in the previous section uses the
following test statistic:

| Many statisticians use this version of the t-test only when they feel
  that the variances of the two populations of interest are
  significantly different from one another (hence it is often called the
  two-sample t-test assuming unequal variances).
| If, however, it is reasonable to assume that the amount of variability
  in the two populations is about the same, then statisticians often use
  a slightly different version of the t-test. Assuming the two variances
  are equal, we can obtain a common estimate of this equal variance
  (this is called a *pooled* estimate).

Then, the test statistic for the t-test is calculated as follows:

    | Assuming the two variances are equal, this test statistic comes
      from a t-distribution with
    | df = (n:sub:`1` – 1) + (n:sub:`2` – 1).
    | In practice, the two-sample t-test that was introduced earlier and
      used throughout the previous section works well, even if the two
      distributions being compared have the same amount of variability.
      Therefore, it’s my opinion that instead of worrying about which
      one to use, just go with the test assuming unequal variances.

.. |image0| image:: img/media/image1.png
   :width: 5.85600in
   :height: 0.65942in
.. |image1| image:: img/media/image2.png
   :width: 5.14400in
   :height: 1.72401in
.. |image2| image:: img/media/image3.png
   :width: 5.07200in
   :height: 1.69988in
.. |image3| image:: img/media/image4.png
   :width: 3.53879in
   :height: 2.60417in
.. |image4| image:: img/media/image5.png
   :width: 3.75000in
   :height: 0.87500in
.. |image5| image:: img/media/image9.png
   :width: 6.79456in
   :height: 3.60417in
.. |image6| image:: img/media/image13.png
   :width: 4.76834in
   :height: 1.97917in
.. |image7| image:: img/media/image15.png
   :width: 4.81317in
   :height: 1.58355in
.. |image8| image:: img/media/image5.png
   :width: 4.37561in
   :height: 1.02098in
.. |image9| image:: img/media/image15.png
   :width: 4.81317in
   :height: 1.58355in
.. |image10| image:: img/media/image15.png
   :width: 4.41667in
   :height: 1.45310in
.. |image11| image:: img/media/image18.png
   :width: 3.45833in
   :height: 2.15022in
.. |image12| image:: img/media/image19.png
   :width: 4.08000in
   :height: 1.57228in
.. |image13| image:: img/media/image20.png
   :width: 4.20800in
   :height: 1.37295in
.. |image14| image:: img/media/image21.png
   :width: 4.65833in
   :height: 0.92004in
.. |image15| image:: img/media/image20.png
   :width: 4.44792in
   :height: 1.45123in
.. |image16| image:: img/media/image20.png
   :width: 4.91667in
   :height: 1.60417in
.. |image17| image:: img/media/image23.png
   :width: 3.67404in
   :height: 3.22917in
.. |image18| image:: img/media/image24.png
   :width: 3.80208in
   :height: 1.52530in
.. |image19| image:: img/media/image25.png
   :width: 4.81317in
   :height: 1.58355in
.. |image20| image:: img/media/image25.png
   :width: 4.81317in
   :height: 1.58355in
.. |image21| image:: img/media/image26.png
   :width: 4.46611in
   :height: 2.59375in
.. |image22| image:: img/media/image27.png
   :width: 4.92777in
   :height: 2.33366in
