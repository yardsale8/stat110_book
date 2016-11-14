
**Example 6.3: Systolic Blood Pressure and Captopril, Revisited**

As we saw in Example 6.2, patients with moderate essential hypertension saw a
decrease in systolic blood pressure. Note that we could also investigate the
following question.

.. admonition:: Research Question: 

    Does the systolic blood pressure decrease by more than 10 mmHg?

**Check the assumptions behind the test**

-  Is the number of pairs sufficiently large?

-  If not, is it reasonable to assume the differences in systolic and
   diastolic blood pressures are normally distributed?

+-------------+-------------+
| |image6014|   | |image6015|   |
+=============+=============+
+-------------+-------------+

**Step 1: Set up the null and alternative hypotheses**

H\ :sub:`0`:

H\ :sub:`a`:

**Step 2: Find the test statistic and the p-value**

+------------------------------+------------------------------------------------------------------------+
| |image6016|                    | .. math::                                                              |
|                              |                                                                        |
|                              |    SE_{difference} = \frac{s_{difference}}{\sqrt{n}}\\                 |
|                              |    t = \frac{\bar{x}_{difference} - \mu_{difference}}{SE_{difference}} |
+==============================+========================================================================+
+------------------------------+------------------------------------------------------------------------+


**Using JMP:**

+-------------+----+
| |image6017|   |    |
|             |    |
| |image6018|   |    |
|             |    |
| p-value:    |    |
+=============+====+
+-------------+----+

**Step 3: Write a conclusion in the context of the problem**

Recall the 95% confidence interval for the average difference in
systolic blood pressure means:

|image6019|

Does this interval agree with the results of the hypothesis test?
Explain.
