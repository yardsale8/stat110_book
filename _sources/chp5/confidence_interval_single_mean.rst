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

For this example, JMP returns the following t-quantile:

|image5035|

Also, recall from Example 5.1 that the mean and standard deviation are
as follows:

|image5036|

Use this information to find the endpoints of the confidence interval:

Lower endpoint (:math:`\bar{x}-t_{quantile}\left(s/\sqrt{n}\right)`): =

Upper endpoint (:math:`\bar{x}-t_{quantile}\left(s/\sqrt{n}\right)`): =

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


Confidence Intervals in JMP
---------------------------

While it is certainly possible to compute a confidence interval using the
formula and the t-quantiles, it is more convenient to compute these intervals
using the built-in JMP functions.  We can generate a confidence interval for the
population mean and standard deviation as follows.

.. admonition:: Constructing Confidence Intervals for the Mean and Standard Deviation in JMP

    1. Enter the sample data in a new data table.
    2. Perform ANALYZE > DISTRIBUTION on the column of interest.
    3. 
