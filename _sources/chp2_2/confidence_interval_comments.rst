
.. admonition:: General Comments Concerning the Confidence Interval for a Single Proportion*:

    1. A confidence interval allows us to estimate the population parameter of interest (note that the hypothesis test does NOT allow us to do this). Therefore, when available, a confidence interval should always accompany the hypothesis test.

    2. Several methods exist for constructing a confidence interval for a binomial proportion. We have considered a method known as the “Wald” interval. **Note that this method does not typically perform well for very small sample sizes or when the point estimate is very close to either zero or one.**  This is because the normal curve does *not* approximate the binomial distribution very well in these situations. For example, consider the binomial distribution with π = .10 and n = 20:

       |image2214|

       If our point estimate had been and the sample size had been n = 20, then the Wald method would not have provided us with a very reliable interval estimate of the true population proportion. Other alternatives (such as adjusted Wald intervals, binomial exact intervals, or score intervals) will be more appropriate in these case.  One rule of thumb is that as long as and , the Wald interval should work reasonably well. If these conditions aren’t met, you shouldn’t use the Wald method.
