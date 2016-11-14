Statistical Inference: Conducting a Simulation Study with Playing Cards
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The above *descriptive analysis* tells us what we have learned about
the 50 subjects in the study. Our next goal is to make *inferences*
beyond what happened in the study (i.e., we want to make general
statements about the population). Does the higher proportion of
yawners in the seeded group provide convincing evidence that being
seeded with a yawn actually makes a person more likely to yawn? Note
that it is possible that random chance alone could have led to this
large of a difference. That is, while it is *possible* that the yawn
seeding had no effect and the MythBusters happened to observe more
yawners in the seeded group just by chance, the key question is
whether it is *probable*.

We will answer this question by replicating the experiment over and
over again, but in a situation where we know that yawn seeding has no
effect (the null model). We’ll start with 14 yawners and 36
non-yawners, and we’ll randomly assign 34 of these 50 subjects to the
seeded group and the remaining 16 to the non-seeded group.

Note that we could use playing cards to replicate this experiment:
let 14 red cards represent the yawners, and let 36 black cards
represent the non-yawners. Shuffle the cards well, and randomly deal
out 34 to be the seeded group. This is the first run of our
simulation study. Construct the contingency table to show the number
of yawners and non-yawners in each group from the first run of our
simulation study.

|image3044|

Next, note that if you know the number of yawners in the Seeded group,
then you can fill in the rest of the cells in the contingency table. So,
for the rest of the simulated runs, **we need only keep track of the
number of yawners in the Seeded group**. Record the number of yawners in
the Seeded group from your first simulated experiment in the table
below. Then, repeat this randomization process nine more times,
recording your results in the table.

|image3045|

Next, create a dotplot of the results:

|image3046|

Number of Yawners Randomly Assigned to the Seeded Group

.. admonition:: Questions:

    1. How many randomizations were performed by the class as a whole? What
       proportion gave results *at least as extreme* as the actual study (10
       or more yawners in the seeded group)?

    2. Note that the random process used in the simulation study models the
       situation where the yawn seeding has no effect on whether the subject
       actually yawns—we simply assume there are 14 people who will yawn no
       matter what group they are in, and they are assigned to the two
       groups at random . Based on this simulation study, does it appear
       that random assignment of yawners to groups will result in 10 or more
       yawners in the seeded group just by chance? Explain.

    3. Recall that the MythBusters obtained 10 yawners in the Seeded group.
       Given your answer to Question 2, would you say that the data provide
       convincing statistical evidence to support the research question?
       Explain.
