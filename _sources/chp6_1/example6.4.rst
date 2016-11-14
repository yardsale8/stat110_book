
**Example 6.4: Diastolic Blood Pressure and Captopril**

Finally, we will use the Captopril data to investigate the following
question.

.. admonition:: Research Question: 

    Does the diastolic blood pressure decrease by more than 5 mmHg?

**Step 0: Check the assumptions behind the test**

-  Is the number of pairs sufficiently large?

-  If not, is it reasonable to assume the differences in systolic and
   diastolic blood pressures are normally distributed?

+-------------+-------------+
| |image6020|   | |image6021|   |
+=============+=============+
+-------------+-------------+


**Step 1: Set up the null and alternative hypotheses**

H\ :sub:`0`:

H\ :sub:`a`:

**Step 2: Find the test statistic and the p-value**

+------------------------------+------------------------------------------------------------------------+
| |image6022|                    | .. math::                                                              |
|                              |                                                                        |
|                              |    SE_{difference} = \frac{s_{difference}}{\sqrt{n}}\\                 |
|                              |    t = \frac{\bar{x}_{difference} - \mu_{difference}}{SE_{difference}} |
+==============================+========================================================================+
+------------------------------+------------------------------------------------------------------------+

Using JMP:

+-------------+-------------+
| |image6023|   | |image6024|   |
|             |             |
| p-value:    |             |
+=============+=============+
+-------------+-------------+

**Step 3: Write a conclusion in the context of the problem**

Find the 95% confidence interval for the average difference in systolic
blood pressure means:

|image6025|

Does this interval agree with the results of the hypothesis test?
Explain.
