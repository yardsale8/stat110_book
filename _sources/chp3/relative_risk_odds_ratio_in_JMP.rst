
Relative Risk and Odds Ratios in JMP
------------------------------------

To discuss the calculation of the relative risk and the odds ratio in
JMP, let’s once again consider the Adoption and Suicide Attempt
example. The data should be entered in JMP as follows.

|image3025|

In JMP, select **Analyze > Fit Y by X** and enter the following:

|image3026|

Click OK. On the output that appears, click on the red drop-down arrow
next to **Contingency Analysis…** and select **Relative Risk**.

|image3027|

Enter the following and click OK.

|image3028|

JMP returns the following:

|image3029|

If you also ask for the **Odds Ratio** from this red drop-down arrow,
JMP returns this quantity:

|image3030|

Note that JMP is by default computing the odds of NOT attempting suicide
since this column appears first in the contingency table. It is then
computing the odds ratio with the Adopted Group in the numerator, since
this row appears first in the table.

|image3031|

After re-ordering the columns for the *Suicide Attempt?* variable we
obtain the following:

|image3032|

|image3033|

.. admonition:: Questions:

    1. Verify that the relative risk and odds ratio shown match our
       calculations.

    2. Note that JMP gives a confidence interval for both the relative risk
       and the odds ratio. What would it imply if either of these confidence
       intervals was to include the value one? Explain.
