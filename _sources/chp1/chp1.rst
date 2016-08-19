Chapter 1
=========

.. admonition:: Lab

    Our first task will be to investigate whether or not we can confidently claim 
    that a claim of hearing loss was based on a lie.  Please complete 
    `Lab 1 - Evaluating a Claim of Hearing Loss <./lab1.html>`_.

In the *“Evaluating a Claim of Hearing Loss”* activity, we encountered
several basic examples that required us to think statistically in order
to investigate a question of interest. Before we move on to slightly
more complex examples, we will discuss some basic definitions that will
be used throughout the semester.

SOME BASIC DEFINITIONS
----------------------

.. glossary:: 

    Statistics

    Categorical (or qualitative) data 
        Measurements that are classified into one of a group of categories.

    Numerical (or quantitative) data 
        Measurements that are recorded on a naturally occurring numerical scale.

    Data set
        Most of what we’ll be doing in this course centers on trying to understand a set of information. This set of information is from a . . .

    Population 
        The complete collection of ALL elements that are of interest for a given problem. The population is often so big that obtaining all information about its elements is either difficult or impossible. So, we work with a more manageable set of data that we obtain from a . . .

    Sample 
        A subcollection of elements drawn from a population

    Observation 
        The collection of measurements from a particular unit in a sample.

    Variable 
        Any measurable characteristic of an observation.


Example 1.1: Alleged Hearing Loss
---------------------------------

Consider once again the example presented in an article by
Pankratz, Fausti, and Peed titled “A Forced-Choice Technique to
Evaluate Deafness in the Hysterical or Malingering Patient.”

Recall that the subject was correct on 36 out of 100 trials when he
was asked to identify whether the tone played with either the red or
the blue lightbulb.

.. admonition:: Source

    Journal of Consulting and Clinical Psychology, 1975, Vol. 43, pg. 421-422.

Match each description to the correct statistics concept:

.. dragndrop:: question1.1_1
    :feedback: At least one of your items is matched incorrectly.  Please try again.
    :match_1:  All trials of the experiment for a hearing impaired individual|||Population of interest
    :match_2:  The 100 trials of a hearing impaired person that were observed|||Sample
    :match_3:  Whether or not the hearing impaired person answered correctly|||Variable of interest
    :match_4:  Categorical|||Data type

Recall that we carried out a simulation study to determine whether this
patient who was suspected of malingering had obtained too few correct
answers. The results of the simulation study indicate what outcomes we
expect from a guessing subject:

+------------+
| |image1|   |
+------------+


.. mchoice:: mc1.1_1
    :answer_a: One set of 100 trials
    :answer_b: One correct guess
    :answer_c: One trial
    :answer_d: The number of correct guesses in 100 trials
    :correct: d
    :feedback_a: HINT: Last class we recorded the number of correct guesses in 12 trials, but now we are doing 100 trials.  What should we record?
    :feedback_b: HINT: Last class we recorded the number of correct guesses in 12 trials, but now we are doing 100 trials.  What should we record?
    :feedback_c: HINT: Last class we recorded the number of correct guesses in 12 trials, but now we are doing 100 trials.  What should we record?
    :feedback_d: Each dot represents to the number of correct guesses in 100 trials

    What does each dot/star represent?

.. mchoice:: mc1.1_2
    :answer_a: Answering incorrectly on purpose
    :answer_b: Consistent with guessing
    :correct: a
    :feedback_a: This answer would not be consistent with guessing, as the number of times that a hearing impaired person would guess 36 or fewer correct is very low.
    :feedback_b: Guessing 36 correct is not a typical result.  Notice that it is very rare to guess 36 or fewer correct. If someone is guessing, it would be much more likely to between 40 and 60 answers correct.

    Based on the results of this simulation study, do you
    believe the patient’s outcome of 36 correct out of 100 was consistent
    with guessing, or do these results indicate that he may have been
    answering incorrectly on purpose in order to mislead the researchers
    into believing he was hearing impaired?

.. mchoice:: mc1.1_3
    :answer_a: Yes
    :answer_b: No
    :correct: b
    :feedback_a: To <i>confidently</i> establish that the person was answering incorrectly on purpose, we would need the person to get an <i>unusually</i> small number of correct answers.  In this case, 48 correct would **not** be unusual as it happened fairly frequently in the simultion.
    :feedback_b: While the person may have been answering incorrectly on purpose, their results were not unusual when compaired to someone that was guessing.  Therefore we cannot <i>confidently</i> conclude that this person was making mistakes on purpose.

    Now suppose that another person was tested in the same way, and this person
    answered 48 out of the 100 trials correctly.  Can we **confidently** conclude
    that this person was purposefully answering the questions
    incorrectly?

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

Example 1.3: Are Women Passed Over for Managerial Training?
-----------------------------------------------------------

This example involves possible discrimination against female
employees. Suppose a large supermarket chain occasionally selects
employees to receive management training. A group of female employees
has claimed that they are less likely than male employees of similar
qualifications to be chosen for this training.
The large employee pool that can be tapped for management training is
60% female and 40% male; however, since the management program began,
9 of the 20 employees chosen for management training were female (only
45%). Do the female employees have a valid statistical argument that
they are being discriminated against?

.. admonition:: Research Question 
    Is there statistical evidence for gender discrimination against females?

.. admonition:: *Questions*

    1. Identify the following in the context of this example:

       -  Population of interest:

       -  Sample:

       -  Variable of interest:

       -  Data type:

    2. If the selection process was unbiased, how many of the 20 employees
       selected for management do you *expect* to be women? Explain.

Once again, the key question is how to determine whether the result is
surprising under the assumption that the selection process is unbiased.
To answer this, we will *simulate* the process of an unbiased selection
process, over and over again. Each time we simulate the process, we’ll
keep track of how many of the 20 employees selected for management were
female. Once we’ve repeated this process a large number of times, we’ll
have a pretty good sense for what outcomes would be very surprising,
somewhat surprising, or not so surprising if there was no discrimination
in the selection process.

.. admonition:: Simulation

    Carry out the Tinkerplots simulation. Note that you should consider the
    following questions when designing your simulation study:

    -  What are the two possible outcomes on each of the trials? Change the
       values on your spinner accordingly.

    -  What is the probability that each outcome occurs under the assumption
       that there is no gender discrimination in the selection process?
       Change your spinner accordingly.

    -  Be sure to change the **Draw** value to 1 since only one employee was
       chosen at a time.

    -  How many subjects were there in this study? Keep this value in mind
       when setting the **Repeat** value.

    Carry out the simulation study 1000 times overall, keeping track of the
    number of the employees chosen for management that were female on each
    of the simulated experiments. 

Sketch in your results below:

+------------+
| |image4|   |
+============+
| |image9|   |
+------------+

.. admonition:: *Questions*

    3. What does each dot on this plot represent?

    4. Recall that since the management program began, only 9 of the 20
       employees chosen for management training were female. Does this
       outcome convince you that the selection process is biased against
       women? Why or why not?

Example 1.4: Font Preferences
-----------------------------

Researchers carried out a marketing field study in order to study
preferences of potential consumers in the U.S. They used silver
cardboard boxes to contain chocolate truffles in a forced choice task.
All of the box tops were decorated in the same way, and a white label
was attached to each bearing the name “\ *Indulgence*\ ” in either
Signet font or Salem font. The text on each label was approximately
equal-sized. For each of the 40 subjects in the study, one box labeled
with the Signet font and another box labeled with the Salem font were
placed on a tray, and the subject was simply asked to choose a truffle
from one of the two boxes that were on the tray in front of them.

=========
|image15|
=========
|image16|
=========

The researchers aren’t sure which font is more appropriate for the
label and simply want to know whether the majority of all consumers
will choose the truffles with one font more than the other. In the
sample of 40 subjects, 30 chose to take a truffle from the box that
had Signet font.

.. admonition:: Research Question 
    Do the majority of consumers have a preference for one font over the other?

.. admonition:: *Questions*

    1. Identify the following in the context of this example:

       -  Population of interest:

       -  Sample:

       -  Variable of interest:

       -  Data type:

    2. If there was no preference in the population, how many of the 40
       consumers do you *expect* to choose Signet font? Explain.

To gain an understanding of what outcomes we expect to see if there is
no real preference in the population of all consumers, we will
*simulate* this experiment under the condition that there is no
preference for one font over the other. 

.. admonition:: Simulation

    Carry out the Tinkerplots
    simulation. Note that you should consider the following questions when
    designing your simulation study:

    -  What are the two possible outcomes on each of the trials? Change the
       values on your spinner accordingly.

    -  What is the probability that each outcome occurs under the assumption
       that there is no preference in the population? Change your spinner
       accordingly.

    -  Be sure to change the **Draw** value to 1.

    -  How many subjects were there in this study? Keep this value in mind
       when setting the **Repeat** value.

    Carry out the simulation study 1000 times overall, keeping track of the
    number that choose Signet on each of the simulated experiments. 

Sketch in your results below:

+------------+
| |image7|   |
+============+
| |image14|  |
+------------+

.. admonition:: *Questions*

    3. What does each dot on this plot represent?

    4. **In the actual study, 30 of the 40 selected the Signet font. Does**
       this outcome convince you that there is a preference for one font
       over the other? Why or why not?

.. |image0| image:: img/media/image1.png
   :width: 1005
   :height: 390
   :scale: 47 %
.. |image1| image:: img/media/image1.png
   :width: 6.49136in
   :height: 4.70755in
.. |image2| image:: img/media/image2.png
   :width: 6.50000in
   :height: 0.27153in
.. |image3| image:: img/media/image3.png
   :width: 6.50000in
   :height: 0.36319in
.. |image4| image:: img/media/image5.png
   :width: 6.50000in
   :height: 0.45908in
.. |image5| image:: img/media/image7.png
   :width: 1.12500in
   :height: 0.31601in
.. |image6| image:: img/media/image8.png
   :width: 1.11458in
   :height: 0.33922in
.. |image7| image:: img/media/image11.png
   :width: 6.50000in
   :height: 0.47153in
.. |image8| image:: img/media/image21.png
   :width: 6.50000in
   :height: 1.90in
.. |image9| image:: img/media/image20.png
   :width: 6.50000in
   :height: 1.90in
.. |image10| image:: img/media/image22.png
.. |image11| image:: img/media/image23.png
.. |image12| image:: img/media/image24.png
.. |image13| image:: img/media/image25.png
.. |image14| image:: img/media/image27.png
   :width: 6.50000in
   :height: 1.90in
.. |image15| image:: img/media/image28.png
.. |image16| image:: img/media/image29.png
