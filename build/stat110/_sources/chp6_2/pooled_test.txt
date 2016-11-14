
The t-Test for Independent Samples Assuming Equal Variances
-----------------------------------------------------------

The two-sample t-test that we discussed in the previous section uses the
following test statistic:

.. math::

    SE_{\bar{x}_1-\bar{x}_2} = \sqrt{\frac{s_1^2}{n_1}+ \frac{s_2^2}{n_2}}\\
    t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{SE_{\bar{x}_1-\bar{x}_2}}

Many statisticians use this version of the t-test only when they feel that the
variances of the two populations of interest are significantly different from
one another (hence it is often called the two-sample t-test assuming unequal
variances).

If, however, it is reasonable to assume that the amount of variability in the
two populations is about the same, then statisticians often use a slightly
different version of the t-test. Assuming the two variances are equal, we can
obtain a common estimate of this equal variance (this is called a *pooled*
estimate).

.. math::

    SE_{pooled} = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{(n_1 - 1) + (n_2 - 1)}}

Then, the test statistic for the t-test is calculated as follows:

.. math::

    t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{SE_{pooled}}

Assuming the two variances are equal, this test statistic comes from a
t-distribution with :math:`df = (n_1 – 1) + (n_2 – 1)`.  In practice, the
two-sample t-test that was introduced earlier and used throughout the previous
section works well, even if the two distributions being compared have the same
amount of variability.  Therefore, it’s my opinion that instead of worrying
about which one to use, just go with the test assuming unequal variances.
