Another Example
---------------

Example 7.2 
++++++++++++

Consider the data found in the file **FEV.jmp**. This
data is from an investigation which concerns measuring the subjects'
respiratory function, as well as whether the subjects themselves smoke.
In this problem, the measured outcome of interest is forced expiratory
volume (FEV), which is, essentially, the amount of air an individual can
exhale in the first second of a forceful breath. The file includes
measurements on the following variables:

-  FEV (liters)

-  Age (years)

-  Height (inches)

-  Gender (M/F)

-  Smoking Status (Y/N)

One primary question of interest is how pulmonary function differs
between smokers and nonsmokers. To investigate this question, we will
begin by utilizing some descriptive methods and inferential methods
discussed earlier in the semester.

|image7014|

.. admonition:: Questions

    1. What do these summaries indicate concerning the relationship between
       smoking and lung function?

    2. Do you really believe that this is the case? If not, can you think of
       any potential problems with either the study itself or our
       descriptive methods which might cause the data to display this
       relationship?

Next, let’s consider another variable in the study, Age. We can use a
scatterplot to describe how FEV changes across Age:

|image7015|

Let’s calculate the correlation coefficient and the regression line in
JMP:

|image7016|
|image7017|

.. admonition:: Questions

    1. Interpret the intercept of the regression line in the context of the
       problem.

    2. Interpret the slope of the regression line in the context of the
       problem.

    3. What can you say about the relationship between Age and lung
       function? How does this affect the summaries we observed at the
       beginning of this example?

Finally, let’s examine the relationship between Smoking Status and FEV
after accounting for Age. From the red drop-down arrow next to
“Bivariate Fit of FEV by Age” select Group by… Smoking Status. From the
same drop-down menu, select Fit Line. This requests that JMP fit a
regression line for both smokers and nonsmokers. Your scatterplot should
appear as follows.

|image7018|

|image7019|

|image7020|

.. admonition:: Questions

    1. Does it appear that the rate at which a nonsmoker’s FEV increases
       with Age differs from the rate at which a smoker’s FEV increases with
       Age? Explain.

    2. Based on this information, do you think it is fair to examine the
       relationship between FEV and Smoking Status without accounting for
       Age? Explain.
