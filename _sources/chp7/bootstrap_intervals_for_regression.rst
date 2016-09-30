Inference for Regression
---------------------------------------------

Recall that statistical inference it the process of making guesses about
population parameters using a random sample.  We can apply the same ideas we
used earlier in the book to linear regression, estimating the values of
the population correlation coefficient and/or the slope of the regression line
fit to the entire population.  In this section, we will apply the bootstrap
process to regression to obtain confidence intervals for these quantities.

Notation for Regression
-----------------------

The following figure gives the common symbols used for the sample and population
correlation coefficients and slopes.  Once again, greek letters are used for the
parameters, in this case :math:`\rho` and :math:`\beta` for the correlation
coefficient and slope, respectively.  The sample correlation coefficient and
sample slope are respectively denoted by :math:`r` and :math:`b`.

|image7022|

Bootstrap Intervals for Regression
----------------------------------

Our goal is to use the sample values of :math:`r` and :math:`b` to estimate 
:math:`\rho` and :math:`\beta`.  We can again estimate the sampling variability
in these statistics by using the bootstrap.  Let's review the process of
generating the bootstrap distribution of a statistic.

.. admonition:: Generating the bootstrap distribution of a statistic

    1. Generate many samples of the sample (at least 1000) by taking samples
       that 
           a. use the same size as the original sample
           b. use sampling with replacement

    2. For each sample, compute the value of the bootstrap statistic.

    3. Collect all of these bootstrap statistics into the bootstrap
       distribution. We can construct C% confidence intervals using
       the middle C% of this distribution.

Once again, we will use the StatKey Website, this time in the section titled
`Confidence Interval for a Slope, Correlation <http://www.lock5stat.com/StatKey/bootstrap_2_quant/bootstrap_2_quant.html>`_

|image7023|
