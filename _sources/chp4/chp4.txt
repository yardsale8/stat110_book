Chapter 4
=========

In this chapter, we will consider descriptive methods appropriate for
summarizing numerical variables.

| ***Example 4.1: Summarizing Household Income Levels in Minnesota
  Counties
  ***\ The data in the file **USQuickFacts.jmp** was recorded by the
  U.S. Census Bureau (*Source: http://quickfacts.census.gov)*. This file
  includes information on several demographic variables for all counties
  in the U.S. In this example, we will consider only the counties of
  Minnesota.
| To subset the Minnesota counties in JMP, we first must select Analyze
  > Distribution and enter the following:
| |image0|\ ***
  ***

| Next, on the resulting bar chart, double-click on the bar for
  Minnesota.
| |image1|

A new data table should open in JMP which contains only the 87 counties
in Minnesota. This is the data file we will consider in this example. We
will begin by examining the distribution of *Median Household Income,
2007-2011.*

| To do this, once again select Analyze > Distribution. Place the
  variable of interest, *Median Household Income, 2007-2011,* in the Y,
  Columns box as shown below.
| |image2|

JMP returns the following output by default:

|image3|

Next, we’ll discuss some of the summary statistics provided in each
piece of the output.

+-----------------------------------------------------------------------+----------------------------------------------------------------+
| **Summary Statistics Representing a “Typical Value” in a Data Set**   |
+=======================================================================+================================================================+
|                                                                       | ***Mean***: The arithmetic average of all of the values in a   |
|                                                                       | data set.                                                      |
+-----------------------------------------------------------------------+----------------------------------------------------------------+
|                                                                       | ***Median***: The middle term of a data set (after the         |
|                                                                       | numerical values have been ordered). If the data set           |
|                                                                       | contains an even number of observations, then the              |
|                                                                       | median is the average of the middle two observations.          |
+-----------------------------------------------------------------------+----------------------------------------------------------------+

*Questions*:

1. Is it necessary that the median be an actual measurement from the
   data set? Explain.

2. Is it necessary that the mean be an actual measurement from the data
   set? Explain.

3. Suppose the maximum value in this data set was changed from $83,415
   to $100,000. What impact would this have on the mean? What impact
   would this have on the median?

+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Other Summary Statistics for Describing the “Location” of a Data Set**   |
+============================================================================+============================================================================================================================================================================================================================================================+
|                                                                            | *P\ **ercentiles*** (JMP calls these Quantiles) give us insight into the entire spectrum of our data set. The p\ :sup:`th` percentile of a set of measurements is defined to be the point in the data set where p% of the measurements fall at or below.   |
+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                            | | ***Quartiles*** are special cases of percentiles.                                                                                                                                                                                                        |
|                                                                            | | Q\ :sub:`1` – The median of the lower half of the data                                                                                                                                                                                                   |
|                                                                            | | (i.e., the 25\ :sup:`th` percentile)                                                                                                                                                                                                                     |
|                                                                            |                                                                                                                                                                                                                                                            |
|                                                                            | Q\ :sub:`2` – The median (i.e., the 50\ :sup:`th` percentile)                                                                                                                                                                                              |
|                                                                            |                                                                                                                                                                                                                                                            |
|                                                                            | | Q\ :sub:`3` – The median of the upper half of the data                                                                                                                                                                                                   |
|                                                                            | | (i.e., the 75\ :sup:`th` percentile)                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*Questions*:

1. What percent of counties in Minnesota have a median household income
   of $44,791 or less?

   *
   *\ |image4|\ *
   *

2. What percent of counties in Minnesota have a median household income
   of $52,713 or less?

3. What percent of counties in Minnesota have a median household income
   above $52,713?

   *
   *

4. The 2.5\ :sup:`th` percentile is about \_\_\_\_\_\_\_\_\_\_\_\_\_\_
   and the 97.5\ :sup:`th` percentile is \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.
   What proportion of Minnesota counties has a median household income
   between these two values?

***MEASURES OF LOCATION
***

| The summary statistics discussed above are often all referred to as
  measures of location. These summaries give us an idea of where a data
  distribution lies. In particular, the mean and median give us an idea
  of the *center* (or middle) of the distribution (this summarizes the
  data set with a single value representing a “typical” value in the
  data set).
| The percentiles (called quantiles in JMP) give us an idea of what
  percent of the data distribution lies at or below a particular value.
| What summary (or summaries) we choose to describe the entire data set
  depends on our objective. If the goal is to describe a typical value
  in the data set, then the mean or median may be an appropriate summary
  statistic. However, if interest lies in what value is exceeded by only
  5% of the data distribution, for example, then we would use the
  95\ :sup:`th` percentile.

***MEASURES OF VARIABILITY***

Sometimes a measure of “center” does not adequately tell a data set’s
story. For example, consider the median household income across counties
for three different states (Minnesota, Wisconsin, and Virginia):

|image5|

The following picture shows the average for each state.

|image6|

*Questions*:

1. What differences exist in the *Typical Household Income* values
   across these three states? Discuss.

2. Suppose that your friend tries to summarize the differences across
   these three states using only the mean (i.e., average) from each
   state. Do you think that this single summary (the mean) tells the
   whole story well? Why or why not?

To adequately describe a data set, we must also describe the amount of
variability present in that data set. Some of these measures are
described below. Also, some of these summary statistics don’t appear by
default in JMP. To see them, click on the red drop-down arrow next to
“Summary Statistics” and choose “Customize Summary Statistics” as shown
below.

|image7|

To get the following output, I requested that JMP display both the
**Range** and the **Interquartile Range**.

+-------------------------------------------------------------------------+-------------------------------------------------------------+
| **Summary Statistics for Describing the “Variability” of a Data Set**   |
+=========================================================================+=============================================================+
| |image8|                                                                | | ***Range***: The difference between the largest           |
|                                                                         | | value and the smallest value in a data set.               |
|                                                                         |                                                             |
|                                                                         |     Range = Maximum – Minimum                               |
|                                                                         |                                                             |
|                                                                         | **                                                          |
|                                                                         | **                                                          |
+-------------------------------------------------------------------------+-------------------------------------------------------------+
|                                                                         | | ***Interquartile Range (IQR)***: The IQR is computed as   |
|                                                                         | | the difference between the first and third quartiles.     |
|                                                                         |                                                             |
|                                                                         |     IQR = Q\ :sub:`3` – Q\ :sub:`1`                         |
+-------------------------------------------------------------------------+-------------------------------------------------------------+

*
*

*Questions*:

1. How many observations from the data set are used in the computation
       of the range?

2. Outliers (which we will discuss later) are extreme observations which
       need to be handled with care in an analysis. How will outliers
       affect the range?

3. What is the smallest possible value for the range? What does it mean
       if the range is at this value?

4. What percent of the data lies between Q\ :sub:`1` and Q\ :sub:`3`?

5. Which is more affected by outliers: the range or the IQR? Explain.

Some statisticians advocate that one of the most intuitive ways to
measure variability is to consider what’s called the **Mean Absolute
Deviation**.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Definition**                                                                                                                                                                                        |
+=======================================================================================================================================================================================================+
| ***                                                                                                                                                                                                   |
| Mean Absolute Deviation***: For each measurement, calculate how far away that measurement is from the mean of the data set. The mean absolute deviation is the average of these absolute distances.   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

To see how this is calculated, first consider the mean for Minnesota:

|image9|

| Then, consider the distance between each measurement and the mean:
| |image10|

Next, we consider the length of each of these distances (i.e., the
absolute value of each of the distances) on the following plot. The
average of these lengths is the **mean absolute deviation**.

|image11|

| *
  Question*: Why is it important that we take the absolute value of the
  distances before finding their average?
| JMP doesn’t compute this measure of variability, which tells you how
  often it’s used in practice. This concept is worth considering,
  however, because it helps you understand how both the **variance** and
  the **standard deviation** are computed (these measures are commonly
  used to describe the amount of variability in a data set).
| For example, like the mean absolute deviation, the variance also
  measures how far a “typical” observation is from the mean.
| |image12|
| Instead of working with the **absolute value** of these distances,
  however, the variance works with the **squared** distances (note that
  this still prevents positive distances from cancelling out negative
  distances).

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Definition**                                                                                                                                                                        |
+=======================================================================================================================================================================================+
| ***                                                                                                                                                                                   |
| Variance***: For each data point, calculate how far away that value is from the mean of the data set. Then, square each of these distances and add them up. Finally, divide by n-1.   |
|                                                                                                                                                                                       |
| | Variance:                                                                                                                                                                           |
| | *                                                                                                                                                                                   |
|   Note: We divide by n –1 because dividing by n tends to underestimate the true population variance.                                                                                  |
|   So, our estimate of the variance is better when we divide by n-1.                                                                                                                   |
|   *                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Finally, because the original distances were squared, the variance is in
terms of squared units. To get back into the original scale of our data
set, we take the square root of the variance.

+-----------------------------------------------------------+
| **Definition**                                            |
+===========================================================+
| ***                                                       |
| Standard Deviation***: The square root of the variance.   |
|                                                           |
| Standard deviation:                                       |
+-----------------------------------------------------------+

The following output shows both the variance and the standard deviation.

+-------------------------------------------------------------------------+-----------------------------+
| **Summary Statistics for Describing the “Variability” of a Data Set**   |
+=========================================================================+=============================+
|                                                                         | ***Variance***:**           |
|                                                                         | **                          |
+-------------------------------------------------------------------------+-----------------------------+
|                                                                         | ***Standard deviation***:   |
+-------------------------------------------------------------------------+-----------------------------+

Next, reconsider the following three states.

|image13|

JMP was used to obtained summary statistics for all three:

+-----------------+-------------+
| **Virginia**    | |image14|   |
+=================+=============+
| **Wisconsin**   | |image15|   |
+-----------------+-------------+
| **Minnesota**   | |image16|   |
+-----------------+-------------+

*Questions*:

1. Compare each of the aforementioned statistics appropriate for
   summarizing variability across the three states.

2. Which state has the *most* variability in its county-level median
   household incomes? The *least*? How did you decide this?

***
***

| ***Example 4.2: Comparing Household Income Levels Across States
  ***
| Next, suppose we want to determine which states tend to have the
  highest household income levels. To do this, we will go back to our
  original data set, **QuickFacts.jmp**. Recall that the data were
  collected at the county level, so we will begin by summarizing the
  household incomes for each state.
| For example, we could use JMP to find the mean of *Median household
  income* for each state as follows. Select Tables > Summary and enter
  the following:

|image17|

JMP will then open a new data table of which a portion is shown below:

|image18|

This will allow us to make comparisons across states. Note that you can
select Tables > Sort to sort the results in numerical order. After
sorting, we see that the five states with the lowest household incomes
as measured by the mean are shown below:

|image19|

The top five states are shown here:

|image20|

Instead of sorting the data, you could also use Graph Builder to create
graphs such as the following. This makes a visual comparison of
household incomes across states much easier.

| |image21|
| Note that you could create similar maps with other summary statistics
  such as the median or percentiles of the household income data, as
  well.

*
*

*
*

Next, suppose that instead of identifying the highest-earning states,
you were more interested in which states have the most problems with
*income inequality*.

*Questions*:

1. The map from the previous page will *not* help you investigate this
   question. Why not?

2. What summary statistics *will* help you investigate income inequality
   within each state? Explain your reasoning.

3. Use the following map to identify a few states that appear to have
   the most problems with income inequality and a few states that appear
   to have the least problems with income inequality.

    |image22|

Another look at the household income levels by county in a few
individual states:

+----------+------------+
| Hawaii   | Virginia   |
+==========+============+
+----------+------------+

*
Questions*:

1. Suppose a researcher claims there will obviously be less variability
   in incomes in Hawaii than in Virginia simply because Hawaii has only
   5 counties versus Virginia’s 134 counties. In other words, he or she
   is arguing that the measures of variability are smaller for Hawaii
   simply because we have a smaller sample size in that state. Why is
   this reasoning *incorrect*? What is the real reason there is less
   variability in Hawaii?

2. | Note that when I used JMP to compute the standard deviation for
     each state to create the map on page 124, JMP did not report this
     summary statistic for the District of Columbia.
   | |image23|
   | Why did this happen?

***GRAPHICAL SUMMARIES OF NUMERICAL DATA
***

In this section, we will discuss common methods for graphing numerical
data. Graphs conveniently allow us to examine both the location and the
variability in a data set. Moreover, we gain insight into the *shape* of
a data distribution.

***Example 4.3: Graphing Household Income Levels in Minnesota
Counties***

In this example, we will once again consider summarizing the median
household incomes of all 87 counties in Minnesota. Recall that we’ve
already seen a dotplot of these data:\ ***
***

JMP does not create dotplots, but JMP can be used to create the
following graphics.

| ***Histogram***
| A histogram is created by dividing the range of the data distribution
  into class intervals and then counting the number of observations that
  fall in each interval. A rectangular column is plotted in each
  interval, and the height of the column is proportional to the
  frequency of observations within the interval. The y-axis can be
  labeled with either the count or the percentage of the observations
  that fall in each interval.

To see this, note that we could start with our dotplot and divide the
data distribution into the following classes. Then, we can count the
number of data points in each interval.

|image24|

| When you use the Analyze > Distribution platform, JMP provides the
  histogram by default. You can select “Histogram Options > Show counts”
  to display the counts for each interval.
| |image25|

***Density Smoother***

You can use JMP to overlay a density smoother on the histogram. To do
this, select “Continuous Fit > Smooth Curve” from the red drop-down
arrow next to the variable name. You can control the amount of smoothing
with the slider bar.

|image26|

This curve ignores some of the minor irregularities that may appear in
the histogram and provides us with a smooth estimate of the real trends
in the data.

***Boxplot***

The procedure for constructing a boxplot is as follows:

1. Draw horizontal lines at Q\ :sub:`1`, Q\ :sub:`2`, and Q\ :sub:`3`.
       Enclose these horizontal lines in a box.

2. Find the lower and upper whiskers:

    | - The endpoint of the lower whisker is the larger of the minimum
      and
    | (Q:sub:`1` – 1.5\*IQR).

    | - The endpoint of the upper whisker is the smaller of the maximum
      and
    | (Q:sub:`3` + 1.5\*IQR).

*Comment*: Any measurement beyond the endpoint of either whisker is
classified as a potential outlier (an extreme observation).

When you use the Analyze > Distribution platform in JMP, the boxplot
appears by default. You can open and close the boxplot by clicking on
the red drop-down menu next to the variable name and selecting “Outlier
Box Plot.”

|image27|

*
Questions*:

1. Are there any counties in Minnesota in which the median household
   income is unusually low? If so, which ones?

2. Are there any counties in Minnesota in which the median household
   income is unusually high? If so, which ones?

***CDF Plot***

To create a plot of the cumulative distribution function (i.e., a CDF
plot) in JMP, select this option from the red drop-down arrow next to
the variable name.

|image28|

This plot allows you to easily determine the percentage of the data that
falls at or below a given value on the x-axis. To see this, consider
both a histogram of the data and the percentiles which were discussed
earlier.

+----+-------------+
|    | |image29|   |
+====+=============+
+----+-------------+

*Questions*:

1. | What percentage of counties in Minnesota has a median household
     income level below
   | $50,000?

2. | What percentage of counties in Minnesota has a median household
     income level above
   | $60,000?

***A DISCUSSION OF SKEWNESS***

A data distribution is said to be symmetric if it has the same shape on
both sides of the center. **Skewness** measures the amount of asymmetry
in a data distribution.

The distribution is said to be *positively skewed* or *skewed to the
right* if the measurements tend to trail off to the right. Similarly, a
distribution is *negatively skewed* or *skewed to the left* if the
measurements trail off to the left.

JMP provides a numerical measure of skewness, as well. This measure
takes on the value zero when the data distribution is perfectly
symmetric; skewness measures greater than zero indicate the data are
positively skewed, and skewness measures less than zero indicate the
data are negatively skewed. This skewness measure can be displayed by
customizing the Summary Statistics section of the output.

We have already summarized the median household income for counties in
Minnesota. Next, let’s also consider summaries from two other states,
Nevada and Maryland.

| |image30|
| |image31|

|image32|

*Questions*:

1. How would you describe the shape of the distribution of median
   household incomes in Nevada counties?

2. How would you describe the shape of the distribution of median
   household incomes in Maryland counties?

***Z-SCORES
***

A *Z-score*, often called a standardized value, measures the number of
standard deviations an observation is away from the mean of the data
distribution. The z-score can be used to transform observations to a
dimensionless scale; in addition, it can be used to measure the position
of an observation. Z-scores are calculated as shown below:

*Interpretation of Z-Scores*:

-  As mentioned, the standardized values transform the data so that the
       data is placed on a standard, dimensionless scale that has a mean
       of 0 and a standard deviation of 1.

-  If a Z-Score is negative, then the observation is that many standard
       deviations below the mean.

-  If the Z-Score is positive, then the observation is that many
       standard deviations above the mean.

-  If the Z-Score is 0, then the data value is the same as the mean.

-  If the Standard Deviation is 0, then the Z-Score is not defined and
       thus cannot be computed.

| To obtain Z-scores for the median household incomes of Minnesota
  counties in JMP, select
| **Save > Standardized** from the red drop-down arrow next to the
  variable name once you’re in the Analyze > Distribution platform.

| The Z-scores will be displayed in the last column of the original data
  set.
| |image33|

*Questions*:

1. Show how the Z-score for Winona County was calculated:

    |image34|

1. What does this tell you about the relative position of Winona County
       in the data set?

***THE IDENTIFICATION OF OUTLIERS***

We have already discussed using boxplots to identify outliers. In
addition, we can use Z-scores.

-  Any data value whose Z-Score is **below −2 or above 2** is considered
   a potential outlier.

-  Any data value whose Z-Score is **below -3 or above 3** is considered
   an outlier and warrants further investigation.

These guidelines come from the following theories.

1. ***Empirical Rule***: If the probability distribution is bell-shaped
       and symmetric, then the Empirical Rule applies. This rule says
       that APPROXIMATELY…

-  68% of the values fall within one standard deviation of the mean.

-  95% of the values fall within two standard deviations of the mean.

-  99.7% of the values fall within three standard deviations of the
   mean.

    |image35|

    *Image Source: http://threes.com
    *

1. ***Chebyshev’s Rule***: For ANY probability distribution, Chebyshev’s
       Rule tells us that AT LEAST…

-  75% of the values fall within two standard deviations of the mean.

-  89% of the values fall within three standard deviations of the mean.

-  1 - 1/k\ :sup:`2` of the values fall within k standard deviation of
   the mean.

.. |image0| image:: img/media/image1.png
   :width: 4.92708in
   :height: 1.81555in
.. |image1| image:: img/media/image2.png
   :width: 6.41667in
   :height: 2.47917in
.. |image2| image:: img/media/image3.png
   :width: 4.50000in
   :height: 1.50240in
.. |image3| image:: img/media/image4.png
   :width: 4.61321in
   :height: 2.07632in
.. |image4| image:: img/media/image14.png
   :width: 4.14066in
   :height: 1.62264in
.. |image5| image:: img/media/image15.png
   :width: 4.11321in
   :height: 2.46107in
.. |image6| image:: img/media/image16.png
   :width: 3.11983in
   :height: 1.36792in
.. |image7| image:: img/media/image17.png
   :width: 4.67925in
   :height: 1.38164in
.. |image8| image:: img/media/image19.png
   :width: 1.89664in
   :height: 1.78302in
.. |image9| image:: img/media/image23.png
   :width: 2.78302in
   :height: 1.18881in
.. |image10| image:: img/media/image24.png
   :width: 2.83962in
   :height: 0.90555in
.. |image11| image:: img/media/image25.png
   :width: 5.68868in
   :height: 1.22647in
.. |image12| image:: img/media/image24.png
   :width: 2.59434in
   :height: 0.82733in
.. |image13| image:: img/media/image15.png
   :width: 3.18868in
   :height: 1.90789in
.. |image14| image:: img/media/image32.png
   :width: 3.13208in
   :height: 1.56604in
.. |image15| image:: img/media/image33.png
   :width: 3.14151in
   :height: 1.51738in
.. |image16| image:: img/media/image34.png
   :width: 3.03774in
   :height: 1.51887in
.. |image17| image:: img/media/image35.png
   :width: 4.10417in
   :height: 2.18543in
.. |image18| image:: img/media/image36.png
   :width: 3.28125in
   :height: 1.26202in
.. |image19| image:: img/media/image37.png
   :width: 3.43750in
   :height: 1.30587in
.. |image20| image:: img/media/image38.png
   :width: 3.09375in
   :height: 1.42708in
.. |image21| image:: img/media/image39.png
   :width: 6.50000in
   :height: 4.03472in
.. |image22| image:: img/media/image40.png
   :width: 5.83333in
   :height: 3.56232in
.. |image23| image:: img/media/image43.png
   :width: 4.77083in
   :height: 1.80170in
.. |image24| image:: img/media/image45.png
   :width: 5.43750in
   :height: 1.93750in
.. |image25| image:: img/media/image46.png
   :width: 3.59375in
   :height: 2.32593in
.. |image26| image:: img/media/image47.png
   :width: 5.69792in
   :height: 2.72255in
.. |image27| image:: img/media/image48.png
   :width: 5.00000in
   :height: 1.55208in
.. |image28| image:: img/media/image49.png
   :width: 3.06250in
   :height: 2.42173in
.. |image29| image:: img/media/image51.png
   :width: 1.40407in
   :height: 1.67708in
.. |image30| image:: img/media/image52.png
   :width: 6.48958in
   :height: 2.33333in
.. |image31| image:: img/media/image53.png
   :width: 6.48958in
   :height: 2.32292in
.. |image32| image:: img/media/image54.png
   :width: 6.48958in
   :height: 2.31250in
.. |image33| image:: img/media/image56.png
   :width: 4.85833in
   :height: 1.76389in
.. |image34| image:: img/media/image57.png
   :width: 1.93777in
   :height: 1.35436in
.. |image35| image:: img/media/image58.png
   :width: 3.39583in
   :height: 2.11458in
