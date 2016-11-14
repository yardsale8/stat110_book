Statistical Inference: Conducting a Simulation Study with Tinkerplots
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Note that we could use technology to simulate this process much more
efficiently. This will enable us to easily obtain many more simulated
results so that we can be more confident in our answer to Question 3
above.

Open the file **YawnExperiment.tp** from the course website. Note that
each mixer contains 50 “subjects.” The first mixer contains 14 yawners
and 36 non-yawners; the second mixer contains 34 subjects in the Seeded
group and 16 in the Non-seeded group.

Make sure the **Repeat** value is set to 50 (the number of subjects in
the study), and set BOTH mixers to sample **Without Replacement** (as
shown below).

|image304|

Click Run, and you will see the results of the first simulated trial:

|image305|

To plot these results, drag a new **Plot** to the workspace. Drag the
predictor variable (Group) to the x-axis and the response variable
(Yawn) to the y-axis, as shown below.

|image306|

Click on **n** to count the number in each cell, and you can also
vertically stack the dots using the **Stack** tool.

Note that we are interested in recording the number of yawners in the
Seeded group. Place your cursor over this number (circled in red on the
below graph), right-click, and choose **Collect Statistic.** Set the
**Collect** value to 99 in order to obtain a total of 100 simulated
results, and click **Collect**.

|image307|

Finally, to graph these outcomes, highlight the
“count\_Yawn\_yes\_Group\_Seeded” column and drag a new plot into the
workspace. Drag a point all the way to the right to organize the dots,
and use the **Stack** tool to vertically stack the dots. Finally,
right-click on either endpoint on the x-axis and set “Bin Width” to 1,
and use the count tool (**n**) to count the dots in each bin.

You should see something similar to the following:

|image308|

.. admonition:: Questions:

    1. What does each dot on the above plot represent?

    2. What value(s) occurred most often by chance under the null model?
       Explain why this makes sense.

    3. How often did we see results at least as extreme as the observed data
       (10 or more yawners in the seeded group) under the null model?
       Calculate the proportion of simulated results in which we observed 10
       or more yawners in the seeded group. Note that this is an approximate
       p-value!

    4. The MythBusters reported the following results: 25% yawned of those
       not given a yawn seed, and 29% yawned of those given a yawn seed.
       Then, they cited the "large sample size" and the 4% difference in the
       proportion that yawned between the seeded and non-seeded group to
       confidently conclude that yawn seed had a significant effect on the
       subjects. Therefore, they concluded that the yawn is decisively
       contagious. Do you agree or disagree with their answer? Justify your
       reasoning.
