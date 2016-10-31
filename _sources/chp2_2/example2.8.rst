
Example 2.8: The Minnesota Student Survey 
++++++++++++++++++++++++++++++++++++++++++

The Minnesota Student Survey (MSS) is a survey administered every three years to
6\ :sup:`th`, 9\ :sup:`th`, and 12\ :sup:`th` grade students. It is also offered
to students in area learning centers and to youth in juvenile correctional
facilities. This survey is an important vehicle for youth voice, as school
districts, local public health agencies, and social services agencies use the
survey results in planning and evaluation for school and community initiatives
and prevention programming.

Questions are related to both the home and school life of students.
Topics include family relationships, feelings about school, substance
use, wellness activities, and more. Participation in the survey is
voluntary, confidential, and anonymous.

For this analysis, we will consider Question # 105 from this survey.
Data has been collected for Fillmore County, which is in Southeastern
Minnesota. Fillmore County (population = 20,866) consists of several
small rural communities.

+-----------------------------------------+--------------------------+
| Question #105 from MN Students Survey   | Fillmore County is in    |
|                                         |                          |
| |image2230|                               | Southeastern Minnesota   |
|                                         |                          |
|                                         | |image2231|                |
+=========================================+==========================+
+-----------------------------------------+--------------------------+

The following data was obtained from the Minnesota Department of
Education website.

|image2232|

.. admonition:: Source: 

    Minnesota Department of Education,
    http://education.state.mn.us/MDE/Learning_Support/Safe_and_Healthy_Learners/Minnesota_Student_Survey/index.html

Information regarding the historical patterns for Grade 6 students from
across the state of Minnesota is given here and will be used for
comparisons.

Historical Patterns for Grade 6 Students Across the Entire State of
Minnesota:

-  About 3 out of 4 students in Grade 6 respond to the third part of
   this question (i.e., “smoking marijuana once or twice a week” ) with
   “Great Risk”

-  A very small percentage, only about 1%, respond to the third part of
   this question with “No Risk”

-  The remaining students typically divide themselves between “Slight
   Risk” and “Moderate Risk” when responding to the third part of this
   question.

|image2245|

Consider the following table. The first row of this table contains the
Observed Outcomes for Grade 6 students from Fillmore County (male and
female tallies were combined). The second row contains the Expected
Outcome (under the null hypothesis) for each of the possible survey
responses.

|image2246|

.. admonition:: Questions:

    10. The value in the first row and second column is 9 (i.e. *Observed*
        count in the Slight Risk category). Explain where this number came
        from. What does this value represent?

    11. What does the Total value for the Observed row represent?

    12. The value in the second row and second column is 21.72 (i.e.
        *Expected* count in the Slight Risk category). Explain where this
        number came from. How was it computed? What does this value
        represent?

    13. Why is the *Expected* count for the Great Risk category so much
        higher than the others?

    14. Suppose your friend computes the following percentages: No Risk:
        9/181 ≈ 5%; Slight Risk: 9/181 ≈ 5%; Moderate Risk: 20/181 ≈ 11%; and
        Great Risk: 143/181≈ 79%. Your friend then makes the following
        statement: “There is enough evidence for the research question
        because these percentages are different from the historical
        percentages (i.e., No Risk = 1%, Slight Risk = 12%, Moderate Risk =
        12%, and Great Risk = 75%).” Why is this statement statistically
        incorrect? Explain.

Once again, in an effort to understand the amount of acceptable
deviation from the expected, we can consider the distance between the
Observed and the Expected outcome for each of the possible choices for
this question.

|image2247|

We discussed earlier the fact that we need to square the differences
(i.e., distances) before summing because otherwise the positive and
negative values cancel each other out. Upon careful inspection of these
differences, there is another problem that also needs to be addressed.

In particular, notice that the difference in the Great Risk category is
7.25, and the difference in the No Risk category is slightly smaller at
7.19. However, these distances alone fail to take into consideration the
*scale* of the expected values. The following **Test Statistic**
accounts for the scale of the expected counts:

.. math:: \mathrm{Test\,Statistic} = \sum\frac{\left( \text{Observed} - \text{Expected} \right)^{2}}{\text{Expected}}

|image2248|

The **Test Statistic** for this analysis would be:

.. math:: 

    \mathrm{Test\,Statistic} = \sum\frac{\left( \text{Observed} - \text{Expected} \right)^{2}}{\text{Expected}} = 28.56 + 7.45 + 0.14 + 0.39 = 36.54

Similar to what we have done in the past, now we must determine whether
or not the Test Statistic from the observed data would be considered an
outlier under the null hypothesis. Tinkerplots can be used to compute
the Test Statistic over repeated samples under the null hypothesis. The
outcomes from the first 10 trials are shown here (see the far right
column in table below).

|image2233|

The following graph shows the test statistic computed for each of the
100 simulations carried out under the null hypothesis in Tinkerplots:

|image2234|

.. admonition:: Questions:


    1. The Test Statistic for the observed data from our sample of Grade 6
       students in Fillmore County is 36.54. Is this value consistent with
       results we would expect to see if Grade 6 students in Fillmore County
       do not deviate from historical state-wide patterns for the marijuana
       portion of this question? Explain.

    2. Consider the formula for the test statistic. What would a value near
       0 imply? What would a large value imply? Explain.

       .. math:: \mathrm{Test\,Statistic} = \sum\frac{\left( \text{Observed} - \text{Expected} \right)^{2}}{\text{Expected}}

    3. Compute the p-value, make a decision, and write a final conclusion
       for the original research question.

       |image2249|

.. note:: 

    It can be shown that this test statistic actually follows
    what is known as the **Chi-Square Distribution**. This is different from
    the Binomial distribution presented earlier.

    -  Unlike the binomial distribution, the chi-square distribution is not
       based on counts and is often skewed to the right.

       |image2235|

    -  The number of categories is taken into consideration through a
       quantity called the degrees-of-freedom, typically referred to as the
       **df**.

       *df* = # of Categories – 1

    This hypothesis testing procedure is often called the **Chi-square
    Goodness of Fit Test** and can easily be carried out using most
    statistical software packages.
