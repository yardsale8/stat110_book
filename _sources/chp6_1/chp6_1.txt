Chapter 6 Part 1
================

| ***
  ***\ In this chapter, we will consider methods that allow us to make
  comparisons on numerical variables between two different groups. In
  general, these methods should be used to address research questions
  involving a categorical predictor variable (with two categories) and a
  numerical response variable.
| Two different cases will be considered: (1) When the samples are
  *dependent* (also called *matched* or *paired*), and (2) when the
  samples are independent.
| ***
  COMPARING TWO POPULATION MEANS: DEPENDENT SAMPLES***

The hypothesis testing procedures presented in this section should be
used when the observations from the two groups being compared are
*dependent*. Whether or not the observations are dependent is determined
by how the data are collected. To see this, consider the following
example.

| ***
  Example 6.1: Thanksgiving Holiday Weight Gain
  ***
| In a 2006 study published in *Nutrition Journal*, researchers were
  interested in assessing potential changes that occur in body weight
  during the Thanksgiving holiday break in college students. This
  paper’s abstract indicates that “a total of 94 college students
  reported to the human body composition laboratory at the University of
  Oklahoma following a 6-hour fast with testing occurring prior to, and
  immediately following the Thanksgiving holiday break. Body weight was
  assessed using a balance beam scale while participants were dressed in
  minimal clothing.”
| *Source: Hull et al. The Effects of the Thanksgiving Holiday on Weight
  Gain. Nutrition Journal 2006, **5**:29; doi:10.1186/1475-2891-5-29.*

*Research Question*: On average, does body weight of college students
increase over the Thanksgiving holiday break?

*
Questions*:

1. What is the response variable of interest?

2. What is the predictor variable of interest?

| The raw data from this study were not available; however, the data in
  the file **ThanksgivingWeightData.jmp** are similar to the actual
  results obtained by the researchers. A portion of these data is shown
  below:
| |image0|

*Questions*:

1. What can be said about the weight of Subject #1 as compared to
   Subject #7, for example, regardless of whether the data were
   collected before or after Thanksgiving?

*Comment*: For these data, the first pre-weight is related to the first
post-weight (the two measurements were made on the same person). Thus,
these two samples are **dependent**.

In other words, some of the variability in the responses might be due to
differences between time periods (before vs. after), but much of the
variability in the observations is likely due to differences between
people! So, to control for this variability in weights from person to
person (which will help us isolate the effect of Thanksgiving break), we
will work with the *DIFFERENCES* on each subject, instead. This will
remove the structure of dependence between the pre- and
post-Thanksgiving groups and will control for the fact that some people,
in general, tend to weigh more (or less) than others. In the end, this
helps us to isolate the effect of Thanksgiving break (i.e., before vs.
after).

***
Calculating the Difference in JMP***

| First, open the file called **ThanksgivingWeightData.**. To calculate
  the difference, create an additional column (double click on empty
  column next to “‘Post Weight”) and title it “Difference.” Right-click
  on the new column header and select **Formula**.
| |image1|

In the edit window, tell JMP to calculate the difference as follows:

|image2|

Click **Apply** and then **OK**, and JMP returns the following (only the
results for the first 10 subjects are shown below):

|image3|

*Questions*:

1. What does a positive difference of 3.9 indicate?

2. What does a difference of -1.9 indicate?

| To determine what the average difference is, we can analyze the
  distribution of the differences using the descriptive methods
  discussed in Chapter 4:
| |image4|

*Questions*:

1. What is the average difference of the 94 subjects? Interpret this
   value.

2. If Thanksgiving break had no effect on body weight, what would you
   expect these differences to be, on average?\ *
   *

3. If the research hypothesis is correct (body weights of college
   students increase over Thanksgiving break), what would you expect
   these differences to be, on average?

*
Comment*: Note that these differences are represented by a single column
of data. *So, instead of viewing this as a problem involving a
categorical predictor and a numerical response, you could view this as a
problem involving a single numerical variable – the differences!*
Therefore, the hypothesis testing procedure is *exactly* the same as the
procedure for testing a single population mean we discussed in Chapter
5.

That is, the parameter of interest is the true population average of the
differences which we will represent by μ\ :sub:`difference`.

-  Our best estimate for this parameter is the *sample mean* of the
   observed differences. We’ll call this quantity.

-  The sample standard deviation of the differences will be denoted by
   s\ :sub:`difference`.

We can carry out the hypothesis test as follows to determine whether
body weights of college students tend to increase over Thanksgiving
break.

***Checking the Normality Assumption*:**

Recall that for the t-test to be valid, at least one of the following
conditions must be met:

-  Either the sample size is sufficiently large (greater than 30 or so),
   or

-  The distribution of the observed data is approximately normal (which
   would indicate that the population is normally distributed so that
   the Central Limit Theorem would apply even with a small sample size)

*Question*: Does the t-test appear to be a valid approach for testing
this research question? Justify your reasoning.

***Step 1: Set up the null and alternative hypotheses***

H\ :sub:`o`:

H\ :sub:`a`:

***Step 2: Find the t-statistic and the p-value***

=

| To calculate this test statistic and its associated p-value in JMP,
  use the methods discussed in Chapter 5:
| |image5|

p-value =

***
Step 3: Write a conclusion in the context of the problem***

***
Interpreting the 95% confidence interval for the mean difference***

***
***

| *Comment*: Suppose that when calculating the difference, you switched
  the order of the categories:
| |image6|

What effect would this have had on the analysis?

H\ :sub:`o`:

H\ :sub:`a`:

=

|image7|

p-value =

Conclusion:

95% confidence interval for the mean difference:

***
***

***Example 6.2: Systolic Blood Pressure and Captopril*
**\ The data in the file **Captopril.jmp** give the systolic and
diastolic blood pressures for 15 patients with moderate essential
hypertension, immediately before and two hours after taking a drug,
captopril. Our interest is in investigating the response to the drug
treatment.

*Research Question*: Is there a change in systolic blood pressure after
taking captopril?

*Question*: Are these samples dependent or independent? Explain.

***Check the assumptions behind the test
***

-  Is the number of pairs sufficiently large?

-  If not, is it reasonable to assume the differences in systolic and
   diastolic blood pressures are normally distributed?

+------------+------------+
| |image8|   | |image9|   |
+============+============+
+------------+------------+

***Step 1: Set up the null and alternative hypotheses***

H\ :sub:`0`:

H\ :sub:`a`:

***Step 2: Find the test statistic and the p-value
***

+-------------+-----+
| |image10|   | =   |
+=============+=====+
+-------------+-----+

Using JMP:

+-------------+-------------+
| |image11|   | |image12|   |
|             |             |
| p-value:    |             |
+=============+=============+
+-------------+-------------+

***Step 3: Write a conclusion in the context of the problem***

*
*

*
*

Finally, construct a 95% confidence interval for the average difference
in systolic blood pressure means.

|image13|

*Questions*:

1. Interpret this confidence interval.

2. Does this interval agree with the results of the hypothesis test?
   Explain.

***Example 6.3: Systolic Blood Pressure and Captopril, Revisited*
**\ As we saw in Example 6.2, patients with moderate essential
hypertension saw a decrease in systolic blood pressure. Note that we
could also investigate the following question.

*Research Question*: Does the systolic blood pressure decrease by more
than 10 mmHg?

*Check the assumptions behind the test
*

-  Is the number of pairs sufficiently large?

-  If not, is it reasonable to assume the differences in systolic and
   diastolic blood pressures are normally distributed?

+-------------+-------------+
| |image14|   | |image15|   |
+=============+=============+
+-------------+-------------+

***Step 1: Set up the null and alternative hypotheses***

H\ :sub:`0`:

H\ :sub:`a`:

***Step 2: Find the test statistic and the p-value
***

+-------------+-----+
| |image16|   | =   |
+=============+=====+
+-------------+-----+

*
*\ Using JMP:

+-------------+----+
| |image17|   |    |
|             |    |
| |image18|   |    |
|             |    |
| p-value:    |    |
+=============+====+
+-------------+----+

***Step 3: Write a conclusion in the context of the problem***

*
*

Recall the 95% confidence interval for the average difference in
systolic blood pressure means:

|image19|

Does this interval agree with the results of the hypothesis test?
Explain.

***
***

***
Example 6.4: Diastolic Blood Pressure and Captopril*
**\ Finally, we will use the Captopril data to investigate the following
question.

*Research Question*: Does the diastolic blood pressure decrease by more
than 5 mmHg?

*
Step 0: Check the assumptions behind the test
*

-  Is the number of pairs sufficiently large?

-  If not, is it reasonable to assume the differences in systolic and
   diastolic blood pressures are normally distributed?

+-------------+-------------+
| |image20|   | |image21|   |
+=============+=============+
+-------------+-------------+

*
*

***Step 1: Set up the null and alternative hypotheses***

H\ :sub:`0`:

H\ :sub:`a`:

***Step 2: Find the test statistic and the p-value
***

+-------------+-----+
| |image22|   | =   |
+=============+=====+
+-------------+-----+

Using JMP:

+-------------+-------------+
| |image23|   | |image24|   |
|             |             |
| p-value:    |             |
+=============+=============+
+-------------+-------------+

***Step 3: Write a conclusion in the context of the problem***

*
*

Find the 95% confidence interval for the average difference in systolic
blood pressure means:

|image25|

Does this interval agree with the results of the hypothesis test?
Explain.

.. |image0| image:: img/media/image1.png
   :width: 2.17612in
   :height: 3.17241in
.. |image1| image:: img/media/image2.png
   :width: 2.93750in
   :height: 1.31304in
.. |image2| image:: img/media/image3.png
   :width: 1.95833in
   :height: 0.37500in
.. |image3| image:: img/media/image4.png
   :width: 2.93750in
   :height: 1.96546in
.. |image4| image:: img/media/image5.png
   :width: 3.82443in
   :height: 1.69133in
.. |image5| image:: img/media/image8.png
   :width: 4.49080in
   :height: 1.81695in
.. |image6| image:: img/media/image9.png
   :width: 2.00000in
   :height: 0.43750in
.. |image7| image:: img/media/image10.png
   :width: 6.50000in
   :height: 2.66736in
.. |image8| image:: img/media/image11.png
   :width: 1.67485in
   :height: 1.23861in
.. |image9| image:: img/media/image12.png
   :width: 1.44785in
   :height: 1.14507in
.. |image10| image:: img/media/image13.png
   :width: 1.33129in
   :height: 0.94782in
.. |image11| image:: img/media/image14.png
   :width: 3.09375in
   :height: 1.35265in
.. |image12| image:: img/media/image15.png
   :width: 1.47239in
   :height: 2.13978in
.. |image13| image:: img/media/image13.png
   :width: 1.58015in
   :height: 1.12500in
.. |image14| image:: img/media/image11.png
   :width: 1.45977in
   :height: 1.07955in
.. |image15| image:: img/media/image12.png
   :width: 1.31609in
   :height: 1.04086in
.. |image16| image:: img/media/image13.png
   :width: 1.29885in
   :height: 0.92473in
.. |image17| image:: img/media/image16.png
   :width: 2.63793in
   :height: 1.16139in
.. |image18| image:: img/media/image17.png
   :width: 1.61069in
   :height: 2.35583in
.. |image19| image:: img/media/image13.png
   :width: 1.58015in
   :height: 1.12500in
.. |image20| image:: img/media/image18.png
   :width: 2.01042in
   :height: 1.41372in
.. |image21| image:: img/media/image19.png
   :width: 1.82292in
   :height: 1.48638in
.. |image22| image:: img/media/image20.png
   :width: 1.75000in
   :height: 1.28397in
.. |image23| image:: img/media/image21.png
   :width: 3.26415in
   :height: 1.46349in
.. |image24| image:: img/media/image22.png
   :width: 1.64151in
   :height: 2.20063in
.. |image25| image:: img/media/image20.png
   :width: 1.75000in
   :height: 1.28397in
