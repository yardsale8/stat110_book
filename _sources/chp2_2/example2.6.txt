
Example 2.6: Helper vs. Hinderer, Revisited
+++++++++++++++++++++++++++++++++++++++++++

Recall that in this study, 14 of the 16 ten-month-old infants chose the helper
toy. Suppose that the researcher wants to estimate the parameter of interest, π
= the proportion of all ten-month-olds that would choose the helper (you could
also think of this as π = the probability that a randomly selected ten-month-old
would choose the helper toy).

First, check the conditions to determine whether the Wald method is
appropriate.

For illustrative purposes only, use Wald’s method to obtain a 95%
confidence interval for π.

1. Start with the **point estimate,** :math:`\hat{\pi} = \frac{14}{16}=0.875`:

2. Calculate the **standard error** associated with this point
   estimate:

.. math::

    \sqrt{\frac{\hat{\pi}\left(1 - \hat{\pi}\right)}{n}}=\sqrt{\frac{0.875\left(1 - 0.875\right)}{16}}\approx0.083


3. Calculate the **margin of error**: This is defined as 1.96 standard
   errors for a 95% confidence interval.


   .. math::

       1.96\sqrt{\frac{\hat{\pi}\left(1 - \hat{\pi}\right)}{n}}\approx1.96*0.083=0.162

   Comment: See the following excerpt from the Star Tribune article.

   |image2212|

4. Find the **endpoints** of the confidence interval:

.. math::

   \mathrm{Lower\,endpoint} = \hat{\pi} - 1.96\sqrt{\frac{\hat{\pi}\left(1 - \hat{\pi}\right)}{n}}=0.875-0.162=0.713

   \mathrm{Upper\,endpoint} = \hat{\pi} + 1.96\sqrt{\frac{\hat{\pi}\left(1 - \hat{\pi}\right)}{n}}=0.875+0.162=1.04
