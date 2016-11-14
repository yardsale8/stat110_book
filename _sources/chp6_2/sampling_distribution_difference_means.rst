
Characteristics of the Sampling Distribution for the Difference in Means 
-------------------------------------------------------------------------

The illustration in Tinkerplots helps us understand the intuition behind
inference for a difference in means, but we don’t really need Tinkerplots to
determine the characteristics of a distribution of differences in means.
Instead, we can use what statisticians discovered long ago: as long as the
samples are independent, the sampling distribution for the *difference in means*
can be described as follows.

1. The sampling distribution is centered around :math:`\mu_1 - \mu_2`.

2. The standard deviation of our sampling distribution (i.e., standard
   error) is given as follows:

.. math::

    SE_{\bar{x}_1-\bar{x}_2} = \sqrt{\frac{s_1^2}{n_1}+ \frac{s_2^2}{n_2}}

3. The shape of the sampling distribution is approximately normal if (1) both
   sample sizes are “sufficiently large” OR (2) if both original populations are
   normally distributed.

Given these characteristics, the test statistic we will use when testing for
differences in two population means for INDEPENDENT samples is as follows:

.. math::

    t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{SE_{\bar{x}_1-\bar{x}_2}}

This test statistic follows a t-distribution with the following degrees of
freedom:

.. math::

    df = \frac{\left(\frac{s_1^2}{n_1}+ \frac{s_2^2}{n_2}\right)^2}
              {\frac{\left(\frac{s_1^2}{n_1}\right)^2}{n_1 - 1}+ 
              \frac{\left(\frac{s_2^2}{n_2}\right)^2}{n_2 - 1}}

Therefore, as long as it is reasonable to assume the shape of the distribution
of differences in means is approximately normal (see #3 above), we can use the
t-distribution to find our p-value. This procedure is typically referred to as
the **two-sample t-test**.
