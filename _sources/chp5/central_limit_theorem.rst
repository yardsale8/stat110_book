
The Central Limit Theorem
-------------------------

Note that a statistician would not necessarily carry out a simulation study such
as this to answer a research question. Instead, one could use “short-cuts”
known as a t-test or confidence interval to investigate a research question
concerning a single population mean. These short-cuts are results of something
known as the *central limit theorem*, which states the following:

.. admonition:: The Central Limit Theorem for the Mean

    Consider a random sample of n observations from ANY population with mean µ and
    standard deviation σ. The distribution of sample means will have a *mean* of
    :math:`\mu` and a *standard deviation* of :math:`\sigma/\sqrt{n}`. When
    :math:`n` (the number of subjects in the sample) is sufficiently large, this
    distribution will be approximately *NORMAL*; moreover, this approximation gets
    better as the sample size (:math:`n`) increases.

We can see the Central Limit Theorem applied to the sample means
calculated from our hypothetical population from Example 5.2 as follows:

|image5010|

-  We see that this normal distribution is centered at the true
   population *mean*, :math:`\mu = 45`.

-  The standard deviation of all observations in our hypothetical
   population is :math:`\sigma = 9.4` seconds. According to the central limit
   theorem, then, the *standard deviation* of the distribution of sample
   means is given by :math:`\sigma/\sqrt{n} = 9.4/\sqrt{20}=2.1`

-  We see that the distribution of sample means is approximately
   *normal*.

Finally, recall from the previous chapter that given the mean and
standard deviation of a distribution, we can determine whether a given
observation is an outlier or not based on its position on this
distribution. This will help us decide whether the sample mean actually
observed in the research study is an outlier on the distribution that
assumes the null hypothesis is true.

The only question that remains is this: How large does n (the number of
subjects in a study) have to be in order for us to use the short-cut
provided by the Central Limit Theorem?


How large does n have to be?
++++++++++++++++++++++++++++

We have seen that the distribution of the sample mean will not always be
bell-shaped and often retains from of the features of the original population,
such as a skewed shape.  Next, we give some guidance on when it is reasonable to
assume that the distribution of sample means will be normal.

.. admonition:: Normal Population

   If the original population is normally distributed, then the sampling
   distribution of the mean will also be normally distributed even
   if the sample size n is very small 
   
(verify this using Tinkerplots as shown in class).

+-----------------------------------+--------------------------------------------+
| Distribution of the Population:   | Distribution of Sample Means when n = 2:   |
|                                   |                                            |
| |image5011|                         | |image5012|                                  |
+===================================+============================================+
+-----------------------------------+--------------------------------------------+

.. admonition:: Skewed Population

   The more skewed the distribution, the larger the sample size must be
   before the normal approximation fits the distribution of sample
   means well.

+-----------------------------------+---------------------------------------------+
| Distribution of the Population:   | Distribution of Sample Means when n = 2:    |
|                                   |                                             |
| |image5013|                         | |image5014|                                   |
+===================================+=============================================+
| Distribution of the Population:   | Distribution of Sample Means when n = 10:   |
|                                   |                                             |
|                                   | |image5015|                                   |
+-----------------------------------+---------------------------------------------+
| Distribution of the Population:   | Distribution of Sample Means when n = 20:   |
|                                   |                                             |
|                                   | |image5016|                                   |
+-----------------------------------+---------------------------------------------+
| Distribution of the Population:   | Distribution of Sample Means when n = 30:   |
|                                   |                                             |
|                                   | |image5017|                                   |
+-----------------------------------+---------------------------------------------+

.. admonition:: General Rule

   For almost all populations, samples of size n ≥ 30 or 40 subjects
   will be sufficient to say that the distribution of sample means
   is approximately normal. However, if the distribution is very
   skewed, the sample size may have to be much larger than 30 in
   order for the central limit theorem to apply.

In summary, we can use the Central Limit Theorem to help us create procedures
for answering questions about the population mean, be it comparing the mean to
some hypothesized value or estimating the value of the population mean with an
interval.

This works because:

1. We know the distribution of sample means will be approximately normal
   if either (i) the original population is normally distributed, or
   (ii) our sample size is sufficiently large.

2. We know the distribution of sample means will be centered at the true
   population mean 
..    (which we can set to some hypothesized value in the null hypothesis).

3. We know that the variability in the distribution of sample means is
   given by :math:`\sigma/\sqrt{n}` (i.e., the variability decreases as the sample size gets
   larger, which we can see in the above examples).

In the next section, we put all of the pieces together to create what is
a t-confidence interval.
.. known as the **t-test**.
