
Inference for a Categorical Variable with More than Two Categories
------------------------------------------------------------------

The analyses we have completed up to this point in the semester were
for a single categorical variable with only *two* outcomes. For
example, in the helper/hinderer study, the babies were choosing either
one toy or the other. In the gender discrimination example, each
employee selected for management was either male or female. Next,
we’ll consider problems involving a single categorical variable which
has more than two categories.

Example 2.7: Minnesota Crime Data
+++++++++++++++++++++++++++++++++

The Minneapolis Police Department posts regular updates on crime statistics on
their website. A colleague of mine has collected this data for the past few
years on all neighborhoods in Minneapolis. A portion of the data set and the
precinct map are shown below.

|image2219|

Source: http://www.minneapolismn.gov/police/crime-statistics/

Suppose the police chief for Precinct #2 has received a complaint from a
permanent resident who lives in a neighborhood near the University of
Minnesota. This resident has asked for additional patrol to take place
in his neighborhood as he believes that crime rates vary over the course
of the year.

.. admonition:: Research Question:

    Is there evidence to suggest that crime patterns in the University of Minnesota neighborhood differ over the four seasons of the year?

Crime rates are reported by month, so we will use the following
definitions for the Seasons:

-  Fall: September, October, and November

-  Winter: December, January, and February

-  Spring: March, April, and May

-  Summer: June, July, and August

Crimes classified as Murder, Rape, Robbery, Aggravated Assault,
Burglary, Larceny, Auto Theft, and Arson are used in reporting the
**Total**.

The Minneapolis Police Department reported that a total of 103 crimes
occurred in the University of Minnesota neighborhood last year.

|image2220|

The approach we take here to address the research question is very
similar to what we have done previously. We will *assume* the crime
patterns are occurring equally across the four seasons (i.e., that the
null hypothesis is true) and then get a good idea of what outcomes we
would expect to see if this were really the case. Then, we will check to
see if the observed outcomes given in the data are consistent (or
inconsistent) with what we expected to see under the null hypothesis. If
the observed data are inconsistent with the outcomes expected under the
null, then we have sufficient statistical evidence to say crime rates
vary across the four seasons.

.. admonition:: Questions:

    1. Find the expected number of total crimes for each season under the
       assumption that crimes are occurring equally over the four seasons.
       How did you obtain these values?

    |image2241|

Note that we must allow for some slight variations in the crime patterns
over the four seasons because we do not anticipate the numbers to come
out exactly at the expected number for each season. Over repeated
samples, slight variations will occur in the crime patterns. We could
use Tinkerplots to give us an idea of how much deviation from the
expected counts we should anticipate.

    |image2221|

.. admonition:: Questions

    2. Why is the spinner set up with 25% for each season? Explain.

    3. Why is the repeat value set to 103? Explain.

Suppose that after running the first trial of the simulation, you
obtained the following results:

|image2222|

To keep track of the count for the number of crimes in each season
over repeated trials of this simulation, we can right-click on *each*
season’s count and select **Collect Statistic**. Note that this needs
to be repeated for each season. Tinkerplots then creates a table as
follows:

|image2223|

Note that I have placed 99 in the Collect box so that we end up with a
total of 100 simulated trials.

|image2224|

The following plot shows what outcomes our simulation study suggests we
would anticipate for each season, assuming that crimes are equally
likely to occur in any of the four seasons.

|image2225|

Next, consider the actual crime statistics for the University of
Minnesota neighborhood for the past year.

|image2242|

Plot these observed outcomes on the above graph. What do you think?
Recall that our goal is to determine whether this observed result is
consistent or not with what our simulation tells us we should see if
there is really no difference in the crime rate across seasons.

.. admonition:: Questions:

    4. Why is it more difficult to determine whether or not our data is
       considered an outlier in this situation than in the problems we dealt
       with previously?

Measuring Distance between Observed and Expected with Several Categories
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

One way to address this problem is to consider the overall distance
between the Observed and Expected counts for all four seasons
combined. This is shown below.

|image2226|

Compute the distance from the Observed to the Expected for the Spring
and Summer seasons.

|image2243|

.. admonition:: Questions:

    5. Find the sum of the Distance for all four seasons. What is this total
       distance? Does this value make sense for total distance? How might we
       overcome this issue?

So that the negative distances do not cancel out the positive ones,
we will square each distance before adding them up. *Note that the
absolute value could have been used, as well, but the statistical
hypothesis testing procedure we will soon be discussing uses the
squared distances, so that’s what we’re considering here.*

|image2244|

The total squared distances summed up across all four seasons is about
137. Note that we cannot determine whether or not this 137 is an outlier
using our previous graphs because the previous graphs considered each
season individually. Our new measure is the squared distance between the
Observed and Expected counts summed over four seasons, so we now need a
new graph that shows this value for all of our 100 simulated results in
Tinkerplots to determine whether or not 137 is an outlier.

|image2227|

.. admonition:: Questions:

    6.  What would a value of 0 imply on the above number line? Explain why a
        value less than 0 is not possible when the distances are squared and
        summed across the categories.

    7.  What would a large value imply? Is this evidence for or against the
        original research question? Explain.

    8. When squared distances are computed and summed across all categories,
        the appropriate test is an upper-tailed test. Explain why this is the
        case.

In Tinkerplots, a formula can be used in the History table to compute
the squared distance between the simulated outcome for a single trial
and the expected count for each season. These squared distance values
are then summed across the four seasons.

The outcomes from the first 5 trials are shown here.

|image2228|

A graph of the total squared distances from all 100 trials in
Tinkerplots is given below. The p-value is determined using the
proportion of dots greater than or equal to 137, the “observed outcome”
from the study.

|image2229|

.. admonition:: Questions:

    9. What is the approximate p-value from the above graph? What is the
       appropriate statistical decision for our research question?
