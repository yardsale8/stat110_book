
Example 3.12: Opinions on Disciplining Children across Regions of U.S.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

On September 16-17, 2014, an NBC News/Marist Poll surveyed a random
sample of 606 adults nationwide. Respondents were asked the following
question: “Do you think it is right or wrong for parents to discipline
their children by striking them - either with a paddle, switch, or
belt?”

The results were separated according to the Region of the U.S. in
which the respondent lived (Northeast, Midwest, South, or West). The
data are summarized in the following table.

+-------------+---------+---------+----------+------------+
|             | Right   | Wrong   | Unsure   | *Totals*   |
+=============+=========+=========+==========+============+
| Northeast   | 22      | 80      | 7        | 109        |
+-------------+---------+---------+----------+------------+
| Midwest     | 33      | 90      | 10       | 133        |
+-------------+---------+---------+----------+------------+
| South       | 114     | 96      | 14       | 224        |
+-------------+---------+---------+----------+------------+
| West        | 38      | 97      | 5        | 140        |
+-------------+---------+---------+----------+------------+
| *Totals*    | 207     | 363     | 36       | 606        |
+-------------+---------+---------+----------+------------+

.. admonition:: Research Question: 

    Is there a statistically significant association between *Region* and
    *Opinion on this Discipline Issue*?

First, since we don’t have access to the raw data, we can enter the data
from the contingency table into JMP as follows (see the file
**Discipline.jmp** posted on the course website).

|image3038|

We can then use the **Analyze > Fit Y by X** menu to obtain the desired
output:

|image3039|

**Step 1**: Convert the research question into :math:`H_0` and :math:`H_a`:

H\ :sub:`o`:

H\ :sub:`a`:

**Step 2**: Find the test statistic and p-value from the data.

|image3040|

.. note:: 

    The chi-square distribution with df = 6 is shown below. Do you see why the
    p-value is so small? 

|image3041|

**Step 3**: Write a conclusion in the context of the problem.

Finally, note that if we determine a significant relationship exists
between the two variables of interest, we should take the time to
describe this relationship.

|image3042|

Also, we can look at each cell’s contribution to the test statistic to
informally determine what is driving the significance of this
relationship:

|image3043|
