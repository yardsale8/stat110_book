
Confidence Interval for the Difference in Proportions
-----------------------------------------------------

Recall our conclusion from Example 3.4 after conducting a hypothesis
test: “We have evidence the proportion of families afflicted by
alcoholism differs depending on whether or not the female in the family
had primary unipolar depression.” The next natural question is as
follows: how large is the difference in these proportions?

We can start by finding the difference in these proportions obtained
from the sample:

-  :math:`\hat{\pi}_{\mathrm{Alcoholism|Depression}}` =

-  :math:`\hat{\pi}_{\mathrm{Alcoholism|Control}}` =

-  :math:`\hat{\pi}_{\mathrm{Alcoholism|Depression}}` - :math:`\hat{\pi}_{\mathrm{Alcoholism|Control}}` =

.. admonition:: Task

    Interpret this difference in the sample proportions:

Next, note that when discussing the results of the Alcoholism and
Depression example, we want to make conclusions that allow us to compare
the alcoholism rate in the POPULATION of families of all females
affected by depression versus those who are not. The difference we just
calculated describes the size of the difference in the proportions
obtained in our SAMPLE. To generalize these results to the population,
we must calculate a confidence interval for the risk difference.

To find the confidence interval of interest for the previous example, we
need the following.

Let :math:`\hat{\pi}_1 = \hat{\pi}_{\mathrm{Alcoholism\,Depression}}` 
and :math:`\hat{\pi}_2 = \hat{\pi}_{\mathrm{Alcoholism\|Control}}` .

1. An **ESTIMATE** of the difference in the two proportions (i.e., the risk
   difference): 

   .. math:: \hat{\pi}_1 - \hat{\pi}_2

2. An appropriate **QUANTILE**:

    This confidence interval requires quantiles from the standard normal
    distribution which will vary depending on the level of confidence.

    +-----------------------+---------+--------+--------+
    | Level of Confidence   | 90%     | 95%    | 99%    |
    +=======================+=========+========+========+
    | z-Quantile            | 1.645   | 1.96   | 2.58   |
    +-----------------------+---------+--------+--------+

    For a 95% confidence interval, z-Quantile =

3. The **STANDARD DEVIATION OF THE ESTIMATE** (i.e., the standard error):

    The standard deviation of the difference between two proportions
    is calculated as follows.
    
    .. math::

        \sqrt{\frac{\hat{\pi}_1(1-\hat{\pi}_1)}{n_1} +\frac{\hat{\pi}_2(1-\hat{\pi}_2)}{n_2}} 

The 95% confidence interval for the risk difference is then calculated
as follows:
   .. math:: \hat{\pi}_1 - \hat{\pi}_2 \pm 1.96\sqrt{\frac{\hat{\pi}_1(1-\hat{\pi}_1)}{n_1} +\frac{\hat{\pi}_2(1-\hat{\pi}_2)}{n_2}} 

Note that we could have also reversed the order of the proportions
when finding the difference:
   .. math:: \hat{\pi}_2 - \hat{\pi}_1 = \hat{\pi}_{\mathrm{Alcoholism|Control}} - \hat{\pi}_{\mathrm{Alcoholism|Depression}} 

The 95% confidence interval for the risk difference is then calculated
as follows:
   .. math:: \hat{\pi}_2 - \hat{\pi}_1 \pm 1.96\sqrt{\frac{\hat{\pi}_1(1-\hat{\pi}_1)}{n_1} +\frac{\hat{\pi}_2(1-\hat{\pi}_2)}{n_2}} 

.. admonition:: Guidelines for Interpreting a Confidence Interval for a Difference in Proportions:

    1. Check whether zero falls in the interval or not. If it does, it is
       *plausible* (but not proof!) that the two proportions are equal.

    2. If all values in a 95% confidence interval for :math:`\pi_1 - \pi_2`
       are positive, then you can infer that :math:`\pi_1 > \pi_2`
       interval tells you how much bigger (with 95% certainty) :math:`\pi_1`
       is.  Similarly, if all values in a confidence interval for :math:`\pi_1 - \pi_2`
       are negative, then you can infer that :math:`\pi_1 < \pi_2`.
       The interval tells you how much bigger :math:`\pi_2` is.

    |image3055|

.. admonition:: Questions:

    1. Interpret the 95% confidence interval for the difference in
       proportions in this problem.

    2. Does this confidence interval agree with the results of the
       hypothesis test? Explain.
