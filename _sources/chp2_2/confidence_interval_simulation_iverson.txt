
When carrying out hypothesis tests, we are testing claims about
population parameters. Sometimes, however, our goal is to *estimate* a
parameter of interest. Statisticians typically do this with a
**confidence interval,** which is simply a range of likely values for
the parameter of interest. The big difference between *hypothesis
testing* and *confidence intervals* is as follows: the construction of a
confidence interval does NOT require any hypotheses concerning our
population parameter of interest.

Example 2.5: Star Tribune Poll Regarding Legalization of Medical Marijuana
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

In February of 2014, a Star Tribune Minnesota poll asked a random
sample of adults in Minnesota, “Do you support or oppose legalizing
marijuana for medical purposes in Minnesota?” Of the 800 adults
surveyed, 408 (51%) answered that they would support this.

|image227|

Source: http://www.startribune.com/politics/statelocal/245910931.html


.. admonition:: Questions:

    Ultimately, the Star Tribune conducted this poll because they wanted to
    estimate the proportion of adults in Minnesota that felt (at the time of
    the survey) that medical marijuana should be legalized. Keep this in
    mind as you answer the following questions.

    1. What is the population of interest?

    2. What is the parameter of interest?

    3. What is the sample?

    4. What is the sample statistic of interest?

Based on the results of this poll, our best guess for the proportion
of all Minnesotans that feel medical marijuana should be legalized is
= 408/800 = 51%. This is called a **point estimate**.

In `StatKey's Confidence Interval for a Single Proportion
<http://www.lock5stat.com/StatKey/bootstrap_1_cat/bootstrap_1_cat.html>`_ , 
we need to enter the statistic by clicking **Edit Data** and entering the
statistic, as shown below.

|image2250|

We know, however, that if a different sample of 800 Minnesotan adults had been
polled, this point estimate would likely change. So, instead of using only this
point estimate, we’ll also use statistical methods to estimate the parameter of
interest with a *range* of likely values (this range is called the **confidence
interval**).  To get this range of likely values, we’ll start with our point
estimate (i.e., the sample statistic, = 51%). This is our best guess so far.
Then, we can use StatKey to get an idea of how much we expect this statistic
to change from one random sample to the next because of natural sampling
variation. The distribution of sample proportions obtained by repeated sampling
is shown below.  

|image2251|

To get a 95% confidence interval for the parameter of interest, we find
both the *lower endpoint* and the *upper endpoint* that separate the
“middle” 95% of this distribution from the outer 5%. As before, this is
accomplished by clicking **two-tail** and setting the confidence level to the
desired value.

.. note::

    As before, you should **always** report your confidence interval in a
    well-formed sentence that describes the parameter of interest in the context
    of the problem.  For example, for the intervals shown above, we would write 

        *We are 95% confidence that the population proportion of all
        Minnesotans that feel medical marijuana should be legalized is between
        0.475 and 0.546* 

    Note that we are trying to estimate the value for the whole population,
    **not** the sample.

.. admonition:: Questions:

    5. Find the lower and upper endpoints for a confidence interval for the
       parameter of interest, π = the proportion of all Minnesotan adults
       that felt medical marijuana should be legalized.

    6. Interpret this confidence interval.
