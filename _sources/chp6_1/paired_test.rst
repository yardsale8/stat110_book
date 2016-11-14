
Comparing Two Population Means: Dependent Samples
-------------------------------------------------

The hypothesis testing procedures presented in this section should be
used when the observations from the two groups being compared are
*dependent*. Whether or not the observations are dependent is determined
by how the data are collected. To see this, consider the following
example.

Example 6.1: Thanksgiving Holiday Weight Gain
+++++++++++++++++++++++++++++++++++++++++++++

In a 2006 study published in *Nutrition Journal*, researchers were
interested in assessing potential changes that occur in body weight
during the Thanksgiving holiday break in college students. This
paper’s abstract indicates that “a total of 94 college students
reported to the human body composition laboratory at the University of
Oklahoma following a 6-hour fast with testing occurring prior to, and
immediately following the Thanksgiving holiday break. Body weight was
assessed using a balance beam scale while participants were dressed in
minimal clothing.”

.. admonition:: Source: 

    Hull et al. The Effects of the Thanksgiving Holiday on Weight Gain. Nutrition Journal 2006, **5**:29; doi:10.1186/1475-2891-5-29.

.. admonition:: Research Question: 

    On average, does body weight of college students increase over the Thanksgiving holiday break?

.. admonition:: Questions:

    1. What is the response variable of interest?

    2. What is the predictor variable of interest?

The raw data from this study were not available; however, the data in
the file **ThanksgivingWeightData.jmp** are similar to the actual
results obtained by the researchers. A portion of these data is shown
below:

|image600|

.. admonition:: Questions:

    1. What can be said about the weight of Subject #1 as compared to
       Subject #7, for example, regardless of whether the data were
       collected before or after Thanksgiving?

.. note::

    For these data, the first pre-weight is related to the first
    post-weight (the two measurements were made on the same person). Thus,
    these two samples are **dependent**.

In other words, some of the variability in the responses might be due to
differences between time periods (before vs. after), but much of the variability
in the observations is likely due to differences between people! So, to control
for this variability in weights from person to person (which will help us
isolate the effect of Thanksgiving break), we will work with the *DIFFERENCES*
on each subject, instead. This will remove the structure of dependence between
the pre- and post-Thanksgiving groups and will control for the fact that some
people, in general, tend to weigh more (or less) than others. In the end, this
helps us to isolate the effect of Thanksgiving break (i.e., before vs.  after).
