Example 1.2 Helper vs. Hinderer?
--------------------------------

In a study reported in a November 2007 issue of *Nature*, researchers
investigated whether infants take into account an individual’s actions
towards others in evaluating that individual as appealing or aversive,
perhaps laying the foundation for social interaction (Hamlin, Wynn,
and Bloom, 2007). In one component of the study, sixteen 10-month-old
infants were shown a “climber” character (a piece of wood with
“google” eyes glued onto it) that could not make it up a hill in two
tries. Then they were shown two scenarios for the climber’s next try,
one where the climber was pushed to the top of the hill by another
character (“helper”) and one where the climber was pushed back down
the hill by another character (“hinderer”). The infant was alternately
shown these two scenarios several times. Then the child was presented
with both pieces of wood (the helper and the hinderer) and asked to
pick one to play with. The color and shape and order (left/right) of
the toys were varied and balanced out among the 16 infants.

.. admonition:: References

    Hamlin, J. Kiley, Karen Wynn, and Paul Bloom. “Social evaluation by preverbal infants.” November 22, 2007. Nature, Volume 150. 

    Introducing Concepts of Statistical Inference. Rossman, Chance, Cobb, and Holcomb. NSF/DUE/CCLI # 0633349.

.. admonition:: Research Question 
    Do 10-month-old infants show a preference for the helper toy over the hinderer toy?

.. admonition:: Questions

    1. Why was it important for the researchers to balance out the color,
       shape, and order of the toys across the study? For example, how would
       the study results have been affected if the researchers always made
       the helper toy a blue circle and the hinderer a yellow triangle?

    2. Identify the following in the context of this example:

       -  Population of interest:

       -  Sample:

       -  Variable of interest:

       -  Data type:

    3. Recall that this study involves 16 infants. If the population of all
       10-month-old infants has no real preference for one toy over the
       other, how many infants do you *expect* to choose the helper toy?
       Explain.

    4. Suppose that 10 out of 16 infants choose the helper toy (62.5%).
       Since this value is higher than 50%, a researcher argues that these
       data show that the majority of *all* 10-month-old infants would
       choose the helper toy. What is wrong with their reasoning?

Once again, the key question is how to determine whether the study’s
result is surprising under the assumption that there is no real
preference for one toy over the other in the population of all
10-month-old infants. To answer this, we will *simulate* the process of
16 infants simply choosing a toy at random, over and over again. Each
time we simulate the process, we’ll keep track of how many infants out
of the 16 chose the ***helper toy*** (note that you could also keep
track of the number that chose the hinderer toy). Once we’ve repeated
this process a large number of times, we’ll have a pretty good sense for
what outcomes would be very surprising, somewhat surprising, or not so
surprising if the population of all 10-month-old infants has no real
preference.

.. admonition:: Simulation

    Carry out the Tinkerplots simulation. Note that you should consider the
    following questions when designing your simulation study:

    -  What are the two possible outcomes on each of the trials? Change the
       values on your spinner accordingly.

    -  What is the probability that each outcome occurs under the assumption
       that the population of all 10-month-old infants has no real
       preference for either toy? Change your spinner accordingly.

    -  Be sure to change the **Draw** value to 1 since only one infant is
       choosing a toy at a time.

    -  How many infants were used in this study? Keep this value in mind
       when setting the **Repeat** value.

    Carry out the simulation study 1000 times overall, keeping track of the
    number of infants that choose the helper toy in each of the simulated
    experiments. 

Sketch in your results below:

+------------+
| |image2|   |
+============+
| |image8|   |
+------------+

.. admonition:: *Questions*

    1. What does each dot on this plot represent?

    2. Suppose that in the actual study 10 out of 16 infants chose the
       helper toy. Would this convince you that the majority of the
       population of all 10-month-old infants had a preference for the
       helper toy? Why or why not?

    3. **The actual study results are as follows: 14 out of 16 infants chose
       the helper toy**. Mark this on the axis above the results of your
       simulations study. Based on this statistical investigation, what
       should the researchers conclude? Recall that their research question
       was stated as follows: Do 10-month-old infants tend to prefer the
       helper toy over the hinderer toy?
