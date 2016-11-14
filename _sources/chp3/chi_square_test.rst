
Chi-Square Test (Alternative to Fisher’s Exact Test)
----------------------------------------------------

Fisher’s exact test from the previous section can be used for either
upper-tailed, lower-tailed, or two-tailed hypothesis tests for differences in
two proportions. The *Chi-square test* is another procedure we can use to test
for differences between two proportions.  However, this procedure can be used
for **ONLY TWO-SIDED TESTS**!  Consider the data from Example 4.4.

    | H\ :sub:`0`: The proportion of families afflicted by alcoholism is
      the same regardless of whether or
    | not the female in the family suffers from primary unipolar
      depression.

    | H\ :sub:`a`: The proportion of families afflicted by alcoholism
      *differs* depending on whether or not
    | the female in the family suffers from primary unipolar depression.

With the chi-square test, the evidence from our sample will consist of a
*test statistic*, which for this test is given as follows:

.. math::

   \mathrm{Test\,Statistic} = \sum \frac{\left(\mathrm{Observed} - \mathrm{Expected}\right)^2}{\mathrm{Expected}}

.. admonition:: Question: 

    Where do we get the expected counts?

    |image3053|

We can also use JMP to calculate the expected counts, deviances, and
cell contributions to find the test statistic:

|image3022|

.. math::

   \mathrm{Test\,Statistic} = \sum \frac{\left(\mathrm{Observed} - \mathrm{Expected}\right)^2}{\mathrm{Expected}}=

.. admonition:: Questions:

    1. What does it mean when the test statistic is “large”?

    2. At what point does the test statistic provide evidence to support our
       research question?

Find the p-value:
+++++++++++++++++

Recall that the Chi-Square test uses a distribution known as the
chi-square (χ:sup:`2`) distribution. The chi-square distribution
takes on only positive numbers and is a continuous distribution. In
addition, this distribution is indexed by its degrees of freedom (or
df). For this test, this is given by df = (r - 1)(c - 1). When the
null hypothesis is true, the test-statistic follows the chi-square
distribution with df = (r - 1)(c - 1). .

The following graph shows the chi-square distribution with df = 1.
The p-value is found by plotting the chi-square test statistic on
the x-axis and calculating the area under the curve above the test
statistic.

+-------------+----+
| |image3023|   |    |
+=============+====+
+-------------+----+

Note that the output for the chi-square test automatically appears when
you select **Analyze > Fit Y by X.**

|image3054|

.. admonition:: Assumptions behind the Chi-Square Test:

    The chi-square test for independence may be inappropriate for tables with
    very small expected cell frequencies. One rule of thumb suggests that most
    of the expected cell frequencies in the table should be 5 or more;
    otherwise, the chi-square approximation may not be reliable. JMP and most
    other statistical software packages will warn you when the results of the
    chi-square test are suspect.

    Also, each observation in the study can be classified into only one cell
    of the contingency table, and the observations must be independent.
