Confidence Interval for a Single Population Mean
------------------------------------------------

In Example 5.1, we found evidence that the mean perceived elapsed time
for smokers suffering from nicotine withdrawal significantly differed
from the actual 45 seconds of time that had elapsed. Our next question
is obvious: HOW MUCH does it differ? To answer this question, we must
construct a *confidence interval*.

Recall our discussion of confidence intervals from earlier in the
semester:

This procedure does NOT require any hypotheses concerning our population
parameter of interest (the mean, in this case). We will use both our
sample data (in particular, the observed mean) and what we know about
the distribution of sample means to obtain a range of likely values for
our population mean.

.. admonition:: Comments

    1. A confidence interval allows us to estimate the population parameter
           of interest (recall that the hypothesis test does NOT allow us to
           do this). Therefore, when available, a confidence interval should
           always accompany the hypothesis test.

    2. The confidence interval does not require any hypothesized value for
           the population parameter. Instead, we center the confidence
           interval on the sample mean. Consider the following example.

**Example 5.4:** Our goal is to construct a 95% confidence interval for
the mean perceived elapsed time for smokers suffering from nicotine
withdrawal. To do this, we will center our distribution of sample means
on the observed mean. Then, we will find the lower and upper endpoints
that separate the middle 95% of the distribution from the rest (since we
are constructing a 95% confidence interval).

    |image5033|

The formula for calculating the endpoints of this confidence interval is
given as follows:

.. math::

    \bar{x} \pm t_{quantile}\frac{s}{\sqrt{n}}

The appropriate t-quantile can be found using JMP. To find this value,
you need the following information:

-  confidence level =

-  df =

Open a new JMP data table and choose **Probability > t Quantile** from
the Formula editor. Enter the following:

|image5034|

Here is an animated GIF of the process.

|image515|

For this example, JMP returns the following t-quantile:

|image5035|

Also, recall from Example 5.1 that the mean and standard deviation are
as follows:

|image5036|

Use this information to find the endpoints of the confidence interval:

Lower endpoint: :math:`\bar{x}-t_{quantile}\left(s/\sqrt{n}\right) = 55.05 - 2.093*\frac{9.327}{\sqrt{20}} = 50.68`

Upper endpoint: :math:`\bar{x}+t_{quantile}\left(s/\sqrt{n}\right) = 55.05 + 2.093*\frac{9.327}{\sqrt{20}} = 59.42`

Confidence Intervals for the Mean in JMP
++++++++++++++++++++++++++++++++++++++++

Note that JMP automatically provides the endpoints of the 95% confidence
interval for this mean when you analyze the distribution of the variable
of interest.

|image5037|

.. admonition:: Questions:

    1. Interpret the meaning of this interval. What does this interval tell
       us about the true mean perceived elapsed time for *all* smokers that
       are suffering from nicotine withdrawal?

    2. Does this interval agree with what you learned from the hypothesis
       test? Explain.

    3. How would your calculations change if you wanted to obtain a 90%
       confidence interval, instead?


Confidence Intervals for the Population Standard Deviation
----------------------------------------------------------

If the original population is bell-shaped, then there is also a formula for the
population standard deviation.  This is due to the fact that, for normal data,
the distribution of the standard deviation squared (also known as the variance)
has a chi-square distribution.

|image513|

While it is certainly possible to compute a confidence interval using the
formula, it is more convenient to compute these intervals using the built-in JMP
functions.  We can generate a confidence interval for both the population mean
and standard deviation as follows.

.. admonition:: Constructing Confidence Intervals for the Mean and Standard Deviation in JMP

    1. Enter the sample data in a new data table.
    2. Perform ANALYZE > DISTRIBUTION on the column of interest.
    3. Click on the triangle above the distribution and select confidence intervals. 

|image514|

.. caution::

    We need to make sure that the original data is fairly normal before relying
    on the formula for the confidence interval for a standard deviation.  If
    there is any doubt about this normality, we would be better off using the
    bootstrap interval instead.

Picking the Correct Procedure
-----------------------------

Now that we have a choice between using the bootstrap and using the JMP
intervals, we need some rules on which procedure is the right procedure for a
given data set.  The advantage of JMP is the ease of use, but the JMP procedures
require normality in some form (either normality of the original data or
normality through a large sample in the case of estimating :math:`\mu`).

.. admonition:: Using JMP is viable when

    - Estimating :math:`\mu`:

        Using JMP to construct a confidence interval for :math:`\mu` is viable when

        1. The original data is normal, or
        2. The sample size is large (:math:`n \ge 40`)

    - Estimating :math:`\sigma`:

        Using JMP to construct a confidence interval for :math:`\sigma` is viable
        when the original data is normal.

Luckily, the bootstrap confidence intervals don't require any assumptions about
normality and can be used when the JMP intervals are not viable.  The following
flow chart illustrates the decision process involved in deciding which procedure
is correct for a given data set.

|image517|

Recall that we use a normal probability plot to decide if the original data is
normal.  Consequently, we will perform the following steps when constructing a
confidence interval.

.. admonition:: Main Steps in Constructing a Confidence Interval for :math:`\mu` or :math:`\sigma` 

    1. Use JMP to construct a normal quantile plot and check the normality of the
       original data.
    2. Determine the correct procedure based on normality and the sample size.
    3. Construct your confidence interval.
    4. Write a sentence summarizing your interval in the context of the problem.



.. mchoice:: mc_picking_correct_1
    :answer_a: JMP interval
    :answer_b: Bootstrap interval
    :correct: a
    :feedback_a: Since the original data is normal, it is safe to use JMP.
    :feedback_b: Since the original data is normal, it is safe to use JMP.  We might as well pick the procedure that requires less work.

    Suppose that we are estimating the population mean, the original data is normal, and the sample size is 10.  Which type of interval should we use?

.. mchoice:: mc_picking_correct_2
    :answer_a: JMP interval
    :answer_b: Bootstrap interval
    :correct: a
    :feedback_a: Since the original data is normal, it is safe to use JMP.
    :feedback_b: Since the original data is normal, it is safe to use JMP.  We might as well pick the procedure that requires less work.

    Suppose that we are estimating the population standard deviation, the original data is normal, and the sample size is 10.  Which type of interval should we use?


.. mchoice:: mc_picking_correct_3
    :answer_a: JMP interval
    :answer_b: Bootstrap interval
    :correct: b
    :feedback_a: Since the original data is not normal and the sample size is small, it is safer to use the bootstrap intervals.
    :feedback_b: Since the original data is not normal and the sample size is small, it is safer to use the bootstrap intervals.

    Suppose that we are estimating the population mean, the sample size is 10, but the original data is NOT normal.  Which type of interval should we use?
