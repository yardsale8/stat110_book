
Example 6.5: Smoking and Birth Weight 
++++++++++++++++++++++++++++++++++++++

A study was conducted in which the relationship between smoking and birth
weights of babies was considered. The data can be found in the file
**LowBirth.JMP**, a portion of which is shown below.

|image610|

.. note::

    The first observation for a nonsmoker is in NO WAY related to the first
    observation for a smoker. Therefore, these groups are *independent*.

Next, let’s examine birth weight across the two groups: smokers and
nonsmokers.

========== ==========
|image611| |image612|
========== ==========

In JMP, we can compare the distributions by selecting **Analyze > Fit Y
by X.** Place the categorical variable (**Smoke**) in the **X, Factor**
box, and place the numerical variable of interest (**Actual\_Weight**)
in the **Y, Response** box. Select the “Display Options” menu from the
red drop-down arrow to display the boxplots and mean diamonds.

|image613|

|image614|

.. admonition:: Questions:

    1. Identify the following sample statistics from the JMP output:

    |image6123|

    2. We are interested in the true difference between these two population
       means, . Based on the data, what is your best guess for this
       difference, and what does it indicate about birth weights for smokers
       compared to nonsmokers?

    3. If you were to take another sample, is your “best guess” from the
       previous question likely to change? Explain.


Since the difference will change from sample to sample, in order to make valid
inferences about the true population difference, we must first understand *how*
the difference in sample means is expected to change from sample to sample. That
is, we must determine what differences in means are likely to happen by chance
when taking random samples from populations with the same mean. The following
illustration in Tinkerplots gives us some insight into this.

|image615|
