
The Wald Interval
-----------------

The previous discussion involving Tinkerplots helps us understand the
intuition behind a confidence interval. Note that a statistician would
not necessarily compute a confidence interval in this way. Instead, to
calculate a confidence interval for a proportion, a statistician often
makes use of the **normal distribution** (i.e., the bell-shaped
curve). Note that the normal curve approximates the distribution of
sample proportions obtained from Tinkerplots quite well:

|image2210|

If we can reasonably assume that this will be the case (later, we’ll
discuss certain conditions under which the normal approximation may not
be reasonable), then we don’t even need the “dots” from Tinkerplots to
find the middle 95%. We can use mathematical theory and a procedure
known as the **Wald interval**, instead.

|image2211|

To find the endpoints for a 95% confidence interval, we need only find
the values on the x-axis of the above graph that separate the middle
95% from the rest.

.. admonition:: The Wald Method

    We can use Wald’s method to do this with the following steps:

    1. Start with the **point estimate,** :math:`\hat{\pi}`:

    2. Calculate the **standard error** associated with this point
       estimate:

    .. math::

        \sqrt{\frac{\hat{\pi}\left(1 - \hat{\pi}\right)}{n}}

    3. Calculate the **margin of error**: This is defined as 1.96 standard
       errors for a 95% confidence interval.


       .. math::

           1.96\sqrt{\frac{\hat{\pi}\left(1 - \hat{\pi}\right)}{n}}=

       Comment: See the following excerpt from the Star Tribune article.

       |image2212|

    4. Find the **endpoints** of the confidence interval:

    .. math::

       \mathrm{Lower\,endpoint} = \hat{\pi} - 1.96\sqrt{\frac{\hat{\pi}\left(1 - \hat{\pi}\right)}{n}}=

       \mathrm{Upper\,endpoint} = \hat{\pi} + 1.96\sqrt{\frac{\hat{\pi}\left(1 - \hat{\pi}\right)}{n}}=


Note that if you desired to construct a 90% or a 99% confidence
interval, instead, the formula would change slightly. These formulas are
shown in the table below.

.. admonition:: Formulas for 90%, 95%, and 99% Confidence Intervals for a Proportion

    - For a 90% confidence interval, the margin of error is defined as 1.645 standard errors.
      The 90% confidence interval is then given by
      :math:`\hat{\pi} \pm 1.645\sqrt{\frac{\hat{\pi}\left(1 - \hat{\pi}\right)}{n}}`.

    - For a 95% confidence interval, the margin of error is defined as 1.96 standard errors.
      The 95% confidence interval is then given by
      :math:`\hat{\pi} \pm 1.96\sqrt{\frac{\hat{\pi}\left(1 - \hat{\pi}\right)}{n}}`

    - For a 99% confidence interval, the margin of error is defined as 2.575 standard errors.
      The 99% confidence interval is then given by
      :math:`\hat{\pi} \pm 2.575\sqrt{\frac{\hat{\pi}\left(1 - \hat{\pi}\right)}{n}}`.

.. admonition:: Questions::

    1. What happens to the margin of error when the confidence level
       decreases? For example, what will happen if we were to construct a
       90% confidence level instead of 95%?

    2. What will happen to the margin of error and the confidence interval
       if we increase the level of confidence?

    3. What will happen to the margin of error if the sample size increases?
       Explain.

    4. Recall the headline used by the Star Tribune and one of the first
       sentences of their article.
       |image2213|
       Carry out the binomial exact test to determine whether the poll
       provides evidence that this is really the case.

    +--------------------------------+----------------+
    | Null Hypothesis                | H\ :sub:`o`:   |
    +--------------------------------+----------------+
    | Alterative Hypothesis          | H\ :sub:`a`:   |
    +================================+================+
    | p-value                        |                |
    +--------------------------------+----------------+
    | Conclusion                     |                |
    +--------------------------------+----------------+

    5. Does the confidence interval agree with the decision at which you
       arrived using the hypothesis test? Explain.
