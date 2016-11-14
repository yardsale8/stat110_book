
Example 3.2: Vested Interest and Task Performance
+++++++++++++++++++++++++++++++++++++++++++++++++

This example is from Investigating Statistical Concepts, Applications,
and Methods by Beth Chance and Allan Rossman. 2006.
Thomson-Brooks/Cole.*

    “A study published in the *Journal of Personality and Social Psychology*
    (Butler and Baumeister, 1998) investigated a conjecture that having an
    observer with a vested interest would decrease subjects’ performance on
    a skill-based task. Subjects were given time to practice playing a video
    game that required them to navigate an obstacle course as quickly as
    possible. They were then told to play the game one final time with an
    observer present. Subjects were randomly assigned to one of two groups.
    One group (A) was told that the participant and observer would each win
    $3 if the participant beat a certain threshold time, and the other group
    (B) was told only that the participant would win the prize if the
    threshold were beaten. The threshold was chosen to be a time that they
    beat in 30% of their practice turns. The following results are very
    similar to those found in the experiment: 3 of the 12 subjects in group
    A beat the threshold, and 8 of 12 subjects in group B achieved success.”

|image3048|

.. admonition:: Research Hypothesis: 

    Having an observer with a vested interest decreases performance on a skill-based task.

.. admonition:: Questions:

    1. What variables must be measured in order to address the research
       question? Are they categorical or numerical?

    2. Which is the response variable? Which is the explanatory variable?

The data can be entered into JMP as follows:

|image3010|

To create the contingency table and the mosaic plot in JMP, select
**Analyze > Fit Y by X**. As always, place the response variable in
the **Y, Response** box and the explanatory variable in the **X,
Factor** box.

|image3011|

Click OK, and JMP returns the following:

|image3049|

.. admonition:: Questions:

    3. What is the proportion of successes (beating the threshold) for each
       group?

    4. What is the difference in the proportion of successes between these
       two groups? Do these proportions differ in the direction conjectured
       by the researchers?

    5. Even if the observer’s interest had absolutely no effect on subjects’
       performance, is it *possible* to have obtained a difference such as
       this by random chance alone? Explain.

    6. Next, let’s think about some outcomes that might occur by chance even
       if having an observer with a vested interest has no real effect on
       the success rate. We will assume that 11 of the 24 subjects are going
       to succeed, no matter what group they’re in. Then, we’ll randomly
       assign them to the two groups of size 12 and see how many of the
       successes end up in each group purely by chance. Note that this
       implies that the row and column totals are fixed. What would the
       counts for the “most extreme” table look like in this case? That is,
       what possible outcome would give us the most convincing evidence in
       support of the research hypothesis?

    |image3012|

    7. Give a few more examples of tables that are *more extreme* than the
       observed data but not *as extreme* as the “most extreme” table shown
       above.

    +-------------+-------------+-------------+
    | |image3013|   | |image3014|   | |image3015|   |
    +=============+=============+=============+
    +-------------+-------------+-------------+

Keep in mind that a p-value is always the probability of seeing
results at least as extreme as the observed data. So, JMP uses what is
known as the hypergeometric distribution to find the probability of
seeing the observed data table and EACH table that is more extreme,
assuming that there is no difference in the two groups being compared.
The sum of these probabilities is the p-value from Fisher’s exact
test.

Fisher’s Exact Test to Obtain Exact p-values
____________________________________________

|image3050|
