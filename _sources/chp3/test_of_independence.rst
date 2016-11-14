
Carrying out the chi-square test of independence:
+++++++++++++++++++++++++++++++++++++++++++++++++

.. admonition:: Assumptions behind the Chi-square Test:

    The chi-square test of independence may be inappropriate for tables with
    very small expected cell frequencies. One rule of thumb suggests that most
    of the expected cell frequencies in the table should be 5 or more;
    otherwise, the chi-square approximation may not be reliable. Also, all
    observations that are counted in the contingency table should be independent
    of each other.

**Step 1**: Convert the research question into :math:`H_0` and :math:`H_a`:

H\ :sub:`o`:

H\ :sub:`a`:

**Step 2**: Calculate a test statistic and p-value from the data.

.. math::

   \mathrm{Test\,Statistic} = \sum \frac{\left(\mathrm{Observed} - \mathrm{Expected}\right)^2}{\mathrm{Expected}}=

Observed counts:

|image3057|

Finding the expected counts:

|image3058|

Once we have the expected counts, we can calculate the test statistic as
follows:

.. math::

   \mathrm{Test\,Statistic} = \sum \frac{\left(\mathrm{Observed} - \mathrm{Expected}\right)^2}{\mathrm{Expected}}=

.. admonition:: Questions:

    1. What does it mean when the test statistic is “large”?

    2. At what point does the test statistic provide evidence to support our
       research question?

Finding the p-value:
++++++++++++++++++++

The Chi-Square test uses a distribution known as the chi-square :math:`\chi^2`
distribution.  The chi-square distribution takes on only positive numbers and is
a *continuous* distribution. In addition, this distribution is indexed by its
degrees of freedom (or df).  For this test, this is given by 

.. math:: df = (r - 1)(c - 1).

You can use the following function in EXCEL to find the p-value:
**=CHIDIST(test statistic, df).**

The following graph shows the chi-square distribution with df = 2.
The p-value is found by plotting the chi-square test statistic on
the x-axis and calculating the area under the curve above the test
statistic.

|image3036|

The output for the chi-square test is also given in the JMP output:

|image3059|

**Step 3**: Write a conclusion in the context of the problem

Finally, since we have determined that there is a significant
association between support for the Iraq war and political
affiliation, we can describe this relationship based on the patterns
displayed in the mosaic plot.

|image3037|
