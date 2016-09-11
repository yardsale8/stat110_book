
CONFIDENCE INTERVAL FOR A SINGLE POPULATION MEAN
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

    |image33|

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

|image34|

For this example, JMP returns the following t-quantile:

|image35|

Also, recall from Example 5.1 that the mean and standard deviation are
as follows:

|image36|

Use this information to find the endpoints of the confidence interval:

Lower endpoint (:math:`\bar{x}-t_{quantile}\left(s/\sqrt{n}\right)`): =

Upper endpoint (:math:`\bar{x}-t_{quantile}\left(s/\sqrt{n}\right)`): =

Note that JMP automatically provides the endpoints of the 95% confidence
interval for this mean when you analyze the distribution of the variable
of interest.

|image37|

.. admonition:: Questions:

    1. Interpret the meaning of this interval. What does this interval tell
       us about the true mean perceived elapsed time for *all* smokers that
       are suffering from nicotine withdrawal?

    2. Does this interval agree with what you learned from the hypothesis
       test? Explain.

    3. How would your calculations change if you wanted to obtain a 90%
       confidence interval, instead?


More on the Interpretation of Confidence Intervals
--------------------------------------------------

The 95% refers to the process of constructing the confidence interval.
This means that if we were to take many samples of size 20 from the
population, constructing a confidence interval each time, we would
expect 95% of them to capture the true population mean. Consider the
following example:

Example 5.5:
++++++++++++

Our goal is to take samples from a population in order to
estimate the true population mean. Shown below are 10 random samples of
size n = 5. Construct a confidence interval for each of the samples.

+-------------+--------------------+---------------------+---------------------------+
| Sample ID   | Data from Sample   | Sample Statistics   | 90% Confidence Interval   |
+=============+====================+=====================+===========================+
| 1           | 12.49983           | Mean 9.65898        |                           |
|             |                    |                     |                           |
|             | 11.4342            | Std Dev 2.19771     |                           |
|             |                    |                     |                           |
|             | 8.210933           |                     |                           |
|             |                    |                     |                           |
|             | 7.373925           |                     |                           |
|             |                    |                     |                           |
|             | 8.776002           |                     |                           |
+-------------+--------------------+---------------------+---------------------------+
| 2           | 5.655407           | Mean 8.78778        |                           |
|             |                    |                     |                           |
|             | 8.903349           | Std Dev 3.01349     |                           |
|             |                    |                     |                           |
|             | 12.98215           |                     |                           |
|             |                    |                     |                           |
|             | 10.22548           |                     |                           |
|             |                    |                     |                           |
|             | 6.172528           |                     |                           |
+-------------+--------------------+---------------------+---------------------------+
| 3           | 8.181802           | Mean 7.56466        |                           |
|             |                    |                     |                           |
|             | 12.08606           | Std Dev 2.73035     |                           |
|             |                    |                     |                           |
|             | 6.176875           |                     |                           |
|             |                    |                     |                           |
|             | 5.556382           |                     |                           |
|             |                    |                     |                           |
|             | 5.822172           |                     |                           |
+-------------+--------------------+---------------------+---------------------------+
| 4           | 13.19405           | Mean 6.91243        |                           |
|             |                    |                     |                           |
|             | 5.122735           | Std Dev 3.96465     |                           |
|             |                    |                     |                           |
|             | 2.469639           |                     |                           |
|             |                    |                     |                           |
|             | 7.373925           |                     |                           |
|             |                    |                     |                           |
|             | 6.401793           |                     |                           |
+-------------+--------------------+---------------------+---------------------------+
| 5           | 9.293009           | Mean 9.00462        |                           |
|             |                    |                     |                           |
|             | 10.52984           | Std Dev 1.59555     |                           |
|             |                    |                     |                           |
|             | 7.260893           |                     |                           |
|             |                    |                     |                           |
|             | 10.50763           |                     |                           |
|             |                    |                     |                           |
|             | 7.431728           |                     |                           |
+-------------+--------------------+---------------------+---------------------------+
| 6           | 9.303573           | Mean 9.59799        |                           |
|             |                    |                     |                           |
|             | 2.354969           | Std Dev 5.23552     |                           |
|             |                    |                     |                           |
|             | 8.811873           |                     |                           |
|             |                    |                     |                           |
|             | 17.06401           |                     |                           |
|             |                    |                     |                           |
|             | 10.45554           |                     |                           |
+-------------+--------------------+---------------------+---------------------------+
| 7           | 10.91127           | Mean 10.02919       |                           |
|             |                    |                     |                           |
|             | 8.023941           | Std Dev 2.57711     |                           |
|             |                    |                     |                           |
|             | 8.432168           |                     |                           |
|             |                    |                     |                           |
|             | 14.17466           |                     |                           |
|             |                    |                     |                           |
|             | 8.603912           |                     |                           |
+-------------+--------------------+---------------------+---------------------------+
| 8           | 11.53353           | Mean 7.53778        |                           |
|             |                    |                     |                           |
|             | 5.782364           | Std Dev 5.67659     |                           |
|             |                    |                     |                           |
|             | 11.44628           |                     |                           |
|             |                    |                     |                           |
|             | 10.61424           |                     |                           |
|             |                    |                     |                           |
|             | -1.68752           |                     |                           |
+-------------+--------------------+---------------------+---------------------------+
| 9           | 8.197059           | Mean 7.89132        |                           |
|             |                    |                     |                           |
|             | 6.193274           | Std Dev 1.59424     |                           |
|             |                    |                     |                           |
|             | 9.114461           |                     |                           |
|             |                    |                     |                           |
|             | 6.290799           |                     |                           |
|             |                    |                     |                           |
|             | 9.661013           |                     |                           |
+-------------+--------------------+---------------------+---------------------------+
| 10          | 6.53196            | Mean 9.61584        |                           |
|             |                    |                     |                           |
|             | 12.08221           | Std Dev 3.09866     |                           |
|             |                    |                     |                           |
|             | 6.81856            |                     |                           |
|             |                    |                     |                           |
|             | 13.46314           |                     |                           |
|             |                    |                     |                           |
|             | 9.183324           |                     |                           |
+-------------+--------------------+---------------------+---------------------------+

A graphical representation of the intervals is presented below:

|image38|

.. admonition:: Questions:

    1. Why are some of the 90% confidence intervals wider than others?

    2. In truth, these 10 random samples were generated from a population
       with a mean of 10. How many of the confidence intervals captured this
       true mean? What does it mean to say that we are 90% confident?
