
**Example 6.2: Systolic Blood Pressure and Captopril**

The data in the file **Captopril.jmp** give the systolic and
diastolic blood pressures for 15 patients with moderate essential
hypertension, immediately before and two hours after taking a drug,
captopril. Our interest is in investigating the response to the drug
treatment.

.. admonition:: Research Question: 

    Is there a change in systolic blood pressure after taking captopril?

.. admonition:: Question: 

    Are these samples dependent or independent? Explain.

**Check the assumptions behind the test**

-  Is the number of pairs sufficiently large?

-  If not, is it reasonable to assume the differences in systolic and
   diastolic blood pressures are normally distributed?

+------------+------------+
| |image608|   | |image609|   |
+============+============+
+------------+------------+

**Step 1: Set up the null and alternative hypotheses**

H\ :sub:`0`:

H\ :sub:`a`:

**Step 2: Find the test statistic and the p-value**

+------------------------------+------------------------------------------------------------------------+
| |image6010|                    | .. math::                                                              |
|                              |                                                                        |
|                              |    SE_{difference} = \frac{s_{difference}}{\sqrt{n}}\\                 |
|                              |    t = \frac{\bar{x}_{difference} - \mu_{difference}}{SE_{difference}} |
+==============================+========================================================================+
+------------------------------+------------------------------------------------------------------------+

Using JMP:

+-------------+-------------+
| |image6011|   | |image6012|   |
|             |             |
| p-value:    |             |
+=============+=============+
+-------------+-------------+

**Step 3: Write a conclusion in the context of the problem**


Finally, construct a 95% confidence interval for the average difference
in systolic blood pressure means.

|image6013|

.. admonition:: Questions:

    1. Interpret this confidence interval.

    2. Does this interval agree with the results of the hypothesis test?
       Explain.
