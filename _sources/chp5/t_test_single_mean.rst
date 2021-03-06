THE T-TEST FOR A SINGLE POPULATION MEAN
---------------------------------------

Back to Example 5.1:
++++++++++++++++++++

Recall that the researchers wanted to show that
the mean perceived elapsed time for smokers suffering from nicotine
withdrawal was greater than the actual 45 seconds that had elapsed. The
data collected in the study were summarized as follows:

|image18|

**Step 1:** Set up the null and alternative hypotheses

H\ :sub:`o`:

H\ :sub:`a`:

**Step 2:** Find the t-statistic and the p-value

To determine whether or not the distance between µ (the hypothesized
population mean) and (the mean from our observed sample) is larger than
what we would expect by random chance, we will use the following
statistic:

.. math::

    t = \frac{\bar{x} - \mu}{s/\sqrt{n}}

Why use this statistic? Because this quantity measures the position of
our observed sample mean on the null model, just like the Z-score
discussed in the previous chapter.

|image39|

Note that this is very much like the Z-score, with one minor exception.
We don’t know the true population standard deviation, σ, so we estimate
it with the standard deviation calculated from the 20 observed subjects
in the study (this estimate is commonly denoted by s).

This t-statistic comes from what is called a t-distribution. The amount
of variability in a t-distribution depends on the sample size n (the
greater the sample size, the smaller the standard deviation of the
distribution of sample means). Therefore, this distribution is indexed
by its *degrees of freedom* (df).

.. note:: 

    For inference on a single mean,

    .. math::
        
        df = n - 1.


To find the p-value associated with this test statistic, we must
remember that this is an upper-tailed test (we are trying to find
evidence that the mean is *greater* than 45 seconds). So, the p-value
will be the probability we would observe a sample mean (or a
t-statistic) *greater* than that obtained in the actual study by chance
alone, assuming the null hypothesis is true:

|image19|

|image20|

To obtain this p-value from JMP, go to the output displaying the
distribution of perceived elapsed time, click on the red drop-down arrow
next to the variable name, and select **Test Mean.**

Enter the value from the null hypothesis as shown:

|image21|

JMP returns the following:

|image22|

**Step 3:** Write a conclusion in the context of the problem

Checking the Normality Assumption:
++++++++++++++++++++++++++++++++++

For the t-test to be valid, at least one of the following conditions
must be met:

-  Either the sample size is sufficiently large (greater than 30 or so),
   or

-  The distribution of the observed data is approximately normal (which
   would indicate that the population is normally distributed so that
   the Central Limit Theorem would apply even with a small sample size)

For Example 5.1, we have a sample size of 20 subjects, which is not
sufficiently large. So we must check whether the data seem to come
from a normal distribution. The histogram seems to indicate that this
is a reasonable assumption:

|image23|

We can also use JMP to create a **normal quantile plot**. To do this,
select this option from the red drop-down arrow next to the variable
name.


|image24|


Example 5.3:
++++++++++++

For the data given in Example 5.1, we found evidence that
the mean perceived elapsed was in fact greater than the actual 45
seconds that had elapsed. This study alone, however, doesn’t really
prove that the nicotine withdrawal was what impaired one’s perception of
time. Why not?

Suppose that the researchers also studied 20 subjects who were smokers
that did NOT abstain from smoking prior to the data collection (so,
they were not suffering from nicotine withdrawal). Data on their
perceived elapsed times are given in the file **Nicotine2.JMP**.

|image25|

.. admonition:: Research Question: 

    Is there evidence the mean perceived elapsed time
    for all smokers *not* suffering from nicotine withdrawal is
    significantly greater than the actual 45 seconds?

Carry out the formal t-test to address this research question.

**Step 1:** Set up the null and alternative hypotheses

H\ :sub:`o`:

H\ :sub:`a`:

**Step 2:** Find the t-statistic and the p-value

Finding the p-value:

|image26|

|image27|

|image28|

**Step 3:** Write a conclusion in the context of the problem


.. include:: normality_assumption.rst
