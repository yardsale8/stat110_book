Chapter 1 Malone
================

.. role:: math(raw)
   :format: html latex
..

Chapter 1: Introduction to Statistical Thinking

Section 1.1: Evaluating a Claim of Hearing Loss

*Example 1.1*: Insurance Fraud - Deafness

+------------+------------+
| |image0|   |
+============+============+
| |image1|   | :          |
|            |            |
|            | :          |
|            |            |
|            | :          |
|            |            |
|            | |image2|   |
+------------+------------+

*Source: http://www.independent.co.uk*

Consider the following case study centered on potential insurance fraud
regarding deafness. This case study was presented in an article by
Pankratz, Fausti, and Peed titled “A Forced-Choice Technique to Evaluate
Deafness in the Hysterical or Malingering Patient.” *Source: Journal of
Consulting and Clinical Psychology, 1975, Vol. 43, pg. 421-422.* The
following is an excerpt from the article:

    *The patient was a 27-year-old male with a history of multiple
    hospitalizations for idiopathic convulsive disorder, functional
    disabilities, accidents, and personality problems. His hospital
    records indicated that he was manipulative, exaggerated his symptoms
    to his advantage, and that he was a generally disruptive patient. He
    made repeated attempts to obtain compensation for his disabilities.
    During his present hospitalization he complained of bilateral
    hearing loss, left-sided weakness, left-sided numbness, intermittent
    speech difficulty, and memory deficit. There were few consistent or
    objective findings for these complaints. All of his symptoms
    disappeared quickly with the exception of the alleged hearing loss.
    *

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+
| To assess his alleged hearing loss, testing was conducted through earphones with the subject seated in a sound-treated audiology testing chamber. Visual stimuli utilized during the investigation were produced by a red and a blue light bulb, which were mounted behind a one-way mirror so that the subject could see the bulbs only when they were illuminated by the examiner. The subject was presented several trials on each of which the red and then the blue light were turned on consecutively for 2 seconds each. On each trial, a 1,000-Hz tone was randomly paired with the illumination of either the blue or red light bulb, and the subject was instructed to indicate with which light bulb the tone was paired. Because the researchers were implementing a “forced-choice” technique, the subject was forced to answer each time with either “red” or “blue.”   | |image3|   |
+=======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+============+
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+

**Understanding Outcomes**

| Suppose an individual was asked to participate in the hearing
  evaluation experiment presented above.
| A total of 20 trials of the experiment were conducted.

+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Situation A   | +-------------------------------------------------------------------------------------------------------------+----------+   |
|               | | Outcome                                                                                                     | Number   |   |
|               | +=============================================================================================================+==========+   |
|               | | Number of times an individual was able to **correctly** associate the light with the playing of the sound   | 20       |   |
|               | +-------------------------------------------------------------------------------------------------------------+----------+   |
|               | | Number **incorrect**                                                                                        | 0        |   |
|               | +-------------------------------------------------------------------------------------------------------------+----------+   |
|               | | Total                                                                                                       | 20       |   |
|               | +-------------------------------------------------------------------------------------------------------------+----------+   |
+===============+==============================================================================================================================+
| Situation B   | +-------------------------------------------------------------------------------------------------------------+----------+   |
|               | | Outcome                                                                                                     | Number   |   |
|               | +=============================================================================================================+==========+   |
|               | | Number of times an individual was able to **correctly** associate the light with the playing of the sound   | 10       |   |
|               | +-------------------------------------------------------------------------------------------------------------+----------+   |
|               | | Number **incorrect**                                                                                        | 10       |   |
|               | +-------------------------------------------------------------------------------------------------------------+----------+   |
|               | | Total                                                                                                       | 20       |   |
|               | +-------------------------------------------------------------------------------------------------------------+----------+   |
+---------------+------------------------------------------------------------------------------------------------------------------------------+

*Questions*:

1. What can be said about an individual whose outcomes are similar to
   Situation A? Discuss.

2. What can be said about an individual whose outcomes are similar to
   Situation B? Discuss.

|image4|

Consider one final set of outcomes.

+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Situation C   | +-------------------------------------------------------------------------------------------------------------+----------+   |
|               | | Outcome                                                                                                     | Number   |   |
|               | +=============================================================================================================+==========+   |
|               | | Number of times an individual was able to **correctly** associate the light with the playing of the sound   | 0        |   |
|               | +-------------------------------------------------------------------------------------------------------------+----------+   |
|               | | Number **incorrect**                                                                                        | 20       |   |
|               | +-------------------------------------------------------------------------------------------------------------+----------+   |
|               | | Total                                                                                                       | 20       |   |
|               | +-------------------------------------------------------------------------------------------------------------+----------+   |
+===============+==============================================================================================================================+
+---------------+------------------------------------------------------------------------------------------------------------------------------+

*Question*:

1. What can be said about this individual in terms of their ability to
   hear? Discuss.

Statistical methods can be used to help fight against insurance fraud.
In this situation, it is necessary to determine whether or not the
subject in this investigation is intentionally giving the wrong answers.
In order to make a determination of this nature, we must first gain an
understanding of *likely* versus *unlikely* outcomes. A simulation model
can be used to identify likely outcomes given a particular situation.

**Modeling Deaf Outcomes**

A simulation model will be constructed to mimic the outcomes of a deaf
person. This model requires the identification of two pieces of
information.

-  Number of completed trials

-  The likelihood or chance of obtaining a correct response

For our example, the number of completed trials is 20, and the chance of
obtaining a correct response for a deaf person is 1 out of 2, or 50%.

+---------------------------------------------------------------+-----------------------------------------+
| Necessary information for building a model                    | Deaf Example                            |
+===============================================================+=========================================+
| -  Number of completed trials                                 | 20                                      |
+---------------------------------------------------------------+-----------------------------------------+
| -  The likelihood or chance of obtaining a correct response   | 1 out of 2; i.e., :math:`\frac{1}{2}`   |
+---------------------------------------------------------------+-----------------------------------------+

+-----------------------------------------------------------------------------------------------+
| Definition                                                                                    |
+===============================================================================================+
| The ***expected*** outcome is the outcome which is identified as the *most* likely outcome.   |
+-----------------------------------------------------------------------------------------------+

The expected outcome for the number of correct responses for 20 trials
with each trial having a :math:`\frac{1}{2}` chance of being correct is
10.

.. math::

   \begin{matrix}
   \text{Expected} & = & 20*\frac{1}{2} \\
    & & 10 \\
   \end{matrix}

The expected value for a model with a :math:`\frac{1}{2}` chance of
being correct will be in the middle; i.e., halfway across the number
line representing the number correct.

|image5|

The most important element that a statistical approach provides to
solving a problem of this nature is an understanding of the inherent
variation that exists in the outcomes from the simulation model. In
particular, there is inherent variation (i.e., randomness) present in
the number of correct responses over repeated trials. The amount of
inherent variation depends on the model being used. In this situation,
the number of trials and the likelihood of a correct response determine
the amount of inherent variation.

+---------------------------------+------------+
| Amount of Inherent Variation    |
+=================================+============+
| *Not much inherent variation*   | |image6|   |
+---------------------------------+------------+
| *A lot of                       |            |
| inherent variation*             |            |
+---------------------------------+------------+

The amount of inherent variation can be discovered using an
appropriately selected random device. A variety of software technologies
have been developed to construct simulation models, and some type of
random device is a necessary part of their development. For this simple
type of experiment, however, a fair coin is sufficient for determining
the amount of inherent variation in the outcomes of interest.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| (Optional) Constructing the simulation model via fair coins                                                                                                                                                                                                                                                                                                                                                                                                                          |
+======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+   |
| | A fair coin can be used to simulate the outcomes from a deaf person. In particular, in this forced choice scenario, a deaf person would simply have to guess which light is associated with the sound on each of the 20 trials. Each trial results in one of two possible outcomes: the subject answering *correctly* or *incorrectly*. Since the subject is guessing between two lights, the chance of obtaining a correct response is 1 out of 2, or :math:`\frac{1}{2}` .   |   |
| |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |   |
| | +------------+-------------------------------------+                                                                                                                                                                                                                                                                                                                                                                                                                           |   |
| | | |image7|   | Deaf person guesses *correctly*     |                                                                                                                                                                                                                                                                                                                                                                                                                           |   |
| | +============+=====================================+                                                                                                                                                                                                                                                                                                                                                                                                                           |   |
| | | |image8|   | Deaf person guesses *incorrectly*   |                                                                                                                                                                                                                                                                                                                                                                                                                           |   |
| | +------------+-------------------------------------+                                                                                                                                                                                                                                                                                                                                                                                                                           |   |
| |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |   |
| | +------------------------------------------------------+----------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                                            |   |
| | | **Coin Model**                                       | **Simulation Model**                                     |                                                                                                                                                                                                                                                                                                                                                            |   |
| | +======================================================+==========================================================+                                                                                                                                                                                                                                                                                                                                                            |   |
| | | 1a) If you toss a coin 20 times, how many coins      | 1b) If a deaf person completes 20 trials of this         |                                                                                                                                                                                                                                                                                                                                                            |   |
| | | would you expect to land on heads?                   | experiment, how many responses would you                 |                                                                                                                                                                                                                                                                                                                                                            |   |
| | |                                                      | expect them to get correct?                              |                                                                                                                                                                                                                                                                                                                                                            |   |
| | +------------------------------------------------------+----------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                                            |   |
| | | 2a) A classmate tosses a coin 20 times and gets 9    | 2b) A deaf person got 9 out of the 20 correct. The       |                                                                                                                                                                                                                                                                                                                                                            |   |
| | | heads. He claims the coin is not fair and must       | investigators claim this deaf person incorrectly on      |                                                                                                                                                                                                                                                                                                                                                            |   |
| | | have been tampered with. What is wrong with          | purpose. What is wrong with their reasoning?             |                                                                                                                                                                                                                                                                                                                                                            |   |
| | | his reasoning?                                       |                                                          |                                                                                                                                                                                                                                                                                                                                                            |   |
| | +------------------------------------------------------+----------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                                            |   |
| | | 3a) A classmate tosses a coin that appears to have   | 3b) A suspect gets 0 out 20 correct. The investigators   |                                                                                                                                                                                                                                                                                                                                                            |   |
| | | been tampered with a total of 20 times. She          | claim that the suspect must be answering                 |                                                                                                                                                                                                                                                                                                                                                            |   |
| | | gets 0 heads. She claims her coin is not fair.       | incorrectly on purpose. Do you agree with their          |                                                                                                                                                                                                                                                                                                                                                            |   |
| | | Do you agree with her reasoning?                     | reasoning?                                               |                                                                                                                                                                                                                                                                                                                                                            |   |
| | +------------------------------------------------------+----------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                                            |   |
| | |                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                       |   |
| | +------------------------------------------------------+----------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                                            |   |
| +================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+   |
| +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

As an alternative to repeatedly flipping a fair coin, an applet has been
constructed so that you can conduct your own repeated trials of this
hearing experiment.

Applet Link: http://course1.winona.edu/cmalone/afc_hearing/

Recall that the goal is to mimic the outcomes of a deaf person.
Therefore, when conducting this experiment, you should mute the speakers
on your computer.

*Task*: Conduct 20 repeated trials of the hearing experiment. Record the
number of correct results below.

+-------------------------------------------------------+-------------+-------------+----+---------+-------------+-------------+
| Trial                                                 | Choice      | Correct?    |    | Trial   | Choice      | Correct?    |
+=======================================================+=============+=============+====+=========+=============+=============+
| 1                                                     | |image9|    | |image10|   |    | 11      | |image11|   | |image12|   |
+-------------------------------------------------------+-------------+-------------+----+---------+-------------+-------------+
| 2                                                     | |image13|   | |image14|   |    | 12      | |image15|   | |image16|   |
+-------------------------------------------------------+-------------+-------------+----+---------+-------------+-------------+
| 3                                                     | |image17|   | |image18|   |    | 13      | |image19|   | |image20|   |
+-------------------------------------------------------+-------------+-------------+----+---------+-------------+-------------+
| 4                                                     | |image21|   | |image22|   |    | 14      | |image23|   | |image24|   |
+-------------------------------------------------------+-------------+-------------+----+---------+-------------+-------------+
| 5                                                     | |image25|   | |image26|   |    | 15      | |image27|   | |image28|   |
+-------------------------------------------------------+-------------+-------------+----+---------+-------------+-------------+
| 6                                                     | |image29|   | |image30|   |    | 16      | |image31|   | |image32|   |
+-------------------------------------------------------+-------------+-------------+----+---------+-------------+-------------+
| 7                                                     | |image33|   | |image34|   |    | 17      | |image35|   | |image36|   |
+-------------------------------------------------------+-------------+-------------+----+---------+-------------+-------------+
| 8                                                     | |image37|   | |image38|   |    | 18      | |image39|   | |image40|   |
+-------------------------------------------------------+-------------+-------------+----+---------+-------------+-------------+
| 9                                                     | |image41|   | |image42|   |    | 19      | |image43|   | |image44|   |
+-------------------------------------------------------+-------------+-------------+----+---------+-------------+-------------+
| 10                                                    | |image45|   | |image46|   |    | 20      | |image47|   | |image48|   |
+-------------------------------------------------------+-------------+-------------+----+---------+-------------+-------------+
| Total Number of Correct Results: \_\_\_\_\_\_\_\_\_   |
+-------------------------------------------------------+-------------+-------------+----+---------+-------------+-------------+

Collect the simulation outcomes from everybody in the class. Place a dot
for each outcome on the following number line.

|image49|

+---------------------+
| *Example dotplot*   |
|                     |
| |image50|           |
+=====================+
+---------------------+

*Questions*:

1. Circle your dot on the plot above. Answer the following regarding
   your dot.

   a. How many correct did you get? How many could you have gotten
      correct?

   b. Is your dot (i.e., outcome) similar to the others in your class?
      Discuss.

2. Which of the following is true about these dots?

   a. These dots are meant to mimic the outcomes of deaf people.

   b. These dots are meant to mimic the outcomes of people who are
      thought to be lying about their ability to hear.

3. Given the simulation results on the above dotplot, what would you
   think about a subject’s claim that he suffers hearing loss if he
   answered

   a. 7 correctly?

   b. 0 or 1 correctly?

   c. 3 or 4 correctly?

**Evaluating Evidence**

In the actual study, the subject was asked to complete 100 trials
(instead of 20 trials as was done above). The graphic below was obtained
using a computer to simulate the possible outcomes of a deaf person
(i.e., a guessing subject). Each time the experiment was simulated the
number of correct trials was counted and recorded. This process was
repeated several times, and the results are shown below.

+--------------------------------------+-------------+
| Outcome from                         | |image51|   |
|                                      |             |
| Study                                |             |
+======================================+=============+
| Likely Outcomes from a Deaf Person   | |image52|   |
+--------------------------------------+-------------+

*Questions:*

1. The subject gave the correct answer in 36 of the 100 trials. What do
   you think about the subject’s claim that he suffers from hearing
   loss?

2. Complete the following fictitious medical records form for this
   subject. Provide a written justification to support your decision.

+-------------------------------------------------------------------------------------------------------+----------------------------------------+
| The evidence suggests this subject has suffered substantial from hearing loss? \_\_\_ Yes \_\_\_ No   |
+=======================================================================================================+========================================+
| Rationale:                                                                                            |
+-------------------------------------------------------------------------------------------------------+----------------------------------------+
|                                                                                                       |
+-------------------------------------------------------------------------------------------------------+----------------------------------------+
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_                                | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   |
|                                                                                                       |                                        |
| Signed                                                                                                | Date                                   |
+-------------------------------------------------------------------------------------------------------+----------------------------------------+

1. Your friend makes the following statement. “This subject got too few
   correct in this hearing test. So, obviously, this person suffers from
   complete hearing loss!” Why is this statement incorrect?

Section 1.2: Applications of 2-AFC in Forensic Sciences

| A suspected serial-rape murderer, an ex-con with a history of sex
  crimes, was interrogated by police after he was overheard bragging to
  others that he raped, killed, and buried a young woman victim in an
  isolated valley outside of the city in which he resided. He told
  police that he had never met the victim and that he had never been to
  the valley. A series of 20 binary (yes/no) questions embedded within
  the interrogation was designed to test his knowledge of victim
  characteristics that only the perpetrator would know.
| *Source: Harold V. Hall and Jane Thompson. “Explicit Alternative
  Testing: Applications of the Binominal Probability Distribution to
  Clinical-Forensic Evaluations.” The Forensic Examiner, Spring 2007.*

*Questions*:

1. Suppose the suspect had no knowledge of the victim and thus was
   merely guessing the answers to the 20 questions. How many questions
   would you expect the suspect to answer correctly?

2. | At what point would you start to believe the suspect was
     intentionally giving incorrect answers in order to make the
     investigators believe they had no knowledge of the crime?
   | |image53|

Note that the even if the observed number of correct answers is less
than would be expected, this is not necessarily enough statistical
evidence to support the suspect’s guilt.

A key question is how to determine whether an individual’s score on the
20-question binary type quiz is surprising under the assumption that
they are simply guessing on each question. To answer this question, we
will *simulate* the process of guessing on 20 binary outcomes several
times. Each time we simulate the process, we’ll keep track of how many
questions the suspect answered ***correctly*** (note that you could also
keep track of the number of incorrect answers). Once we’ve repeated this
process several times, we’ll have a pretty good sense for what outcomes
would be very surprising, or somewhat surprising, or not so surprising
under the situation that an individual is really guessing.

Various technologies can be used for these simulations. For example, the
web page

http://course1.winona.edu/cmalone/2afc/

has been specifically set up for 2-alterative forced choice simulations.
For this simulation, you should specify the labels for the two outcomes
and specify the number of repeated trials.

|image54|

Click Run > to obtain the outcome from a single simulation.

Use the simulation on this web page to obtain 20 outcomes. For each
simulation, record the number of correct and plot the result on the
number line below.

|image55|

*Questions*:

1. How many simulations (i.e. dots) are represented in the above plot?

2. What outcomes would be very surprising to observe if the suspect is
   really guessing?

3. What outcomes would be NOT very surprising to observe if the suspect
   is really guessing?

4. Using the results from your 20 simulation, how many of the 20
   questions would an individual have to answer correctly in order for
   you to be convinced they were intentionally giving the wrong answers?

5. | Ask some of your neighbors at what point they would become
     convinced that an individual is trying to “throw the police off”?
   | Neighbor 1: \_\_\_\_\_\_\_\_\_\_\_ Neighbor 2:
     \_\_\_\_\_\_\_\_\_\_\_\_\_

   Neighbor 3: \_\_\_\_\_\_\_\_\_\_\_ Neighbor 4:
   \_\_\_\_\_\_\_\_\_\_\_\_\_

6. How these cutoff values compare to the one you obtained from your
   simulation? Discuss.

Consider the following graph from 20 trials.

|image56|

1. Is your graph the same as the one presented above? Should it be
   exactly the same? Explain why or why not?

2. Your friend makes the following statement regarding the graph above.
   “If the Number of Correct Answers is around 2, 3, 4, or 5; then I
   believe an individual is intentionally giving wrong answers. Your
   simulation did not produce any values in this region, so you must
   have done something wrong in the setup of your simulation.” Do you
   agree or disagree with this statement? Explain.

3. Your friend makes the following statement regarding the graph above.
   “Ten is the expected number and should be the most common outcome.
   However, this simulation resulted in eleven being the most common;
   thus, you must have done something wrong in the setup of your
   simulation.” Do you agree or disagree with this statement? Explain.

Section 1.3: Using Technologies to Construct Simulation Models

To save time and to gather more simulated results more quickly, a
software package called Tinkerplots\ :sup:`®` can be used to simulate
the outcomes obtained in class in Example 1.1. The results from the
simulation model can then be used to help us understand what outcomes
are likely (or unlikely) to occur. This simulation model will be
constructed using the following parameters (i.e., under these
conditions).

+---------------------------------------------------------------+-----------------------------------------+
| Necessary information for building a model                    | Deaf Example                            |
+===============================================================+=========================================+
| -  Number of completed trials                                 | 20                                      |
+---------------------------------------------------------------+-----------------------------------------+
| -  The likelihood or chance of obtaining a correct response   | 1 out of 2; i.e., :math:`\frac{1}{2}`   |
+---------------------------------------------------------------+-----------------------------------------+

*Setting up the Spinner in Tinkerplots*

Open Tinkerkplots\ :sup:`®` on your computer. Drag a new **Sampler**
from the tool shelf into your blank document, as shown below.

|image57|

The default sampler is called a **Mixer** sampler which simply is a
“hat” that contains three objects (two objects labeled as “a” and one
object labeled as “b”). Tinkerkplots\ :sup:`®` gives you various options
for the type of sampler to use. For this example, a **Spinner** sampler
will be utilized.

+---------------------------------------------------------------------------------------------------------------------------------+-------------------+
| Mixer Sampler (Default)                                                                                                         | Spinner Sampler   |
|                                                                                                                                 |                   |
| |image58|                                                                                                                       | |image59|         |
+=================================================================================================================================+===================+
| The default labeling for the outcomes on the Spinner are *a* and *b*. Re-label the outcomes as **Correct** and **Incorrect**.   | |image60|         |
+---------------------------------------------------------------------------------------------------------------------------------+-------------------+

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Recall that the chance of a deaf person correctly identifying the correct color light bulb is 1 out of 2, or 50%. This value must be specified on our spinner so that the correct simulation model is used. To change the percentages on the spinner, select **Show Percent** from the drop-down menu in the lower left-hand corner of the spinner and enter the desired percentages.   | |image61|   |
+=========================================================================================================================================================================================================================================================================================================================================================================================+=============+
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

Two additional changes must be made to the Spinner sampler.

-  The **Repeat** value indicates the number of trials to be completed
   (change this to 20)

-  Change the **Draw** from 2 to 1

The final setup of the spinner should look as follows.

|image62|

*Questions*

1. Which of the following is true about the setup of this spinner?

   a. This spinner is meant to mimic the outcomes of a deaf person.

   b. This spinner is meant to mimic the outcomes of a person who is
      thought to be lying about their ability to hear.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| *Running the Simulation                                                                                                                                           | |image63|   |
| *                                                                                                                                                                 |             |
|                                                                                                                                                                   |             |
| Click the **Run** button in the upper-left corner of the spinner. A table of the results for the 20 simulated trials will be generated.                           |             |
|                                                                                                                                                                   |             |
| *Questions*                                                                                                                                                       |             |
|                                                                                                                                                                   |             |
| 1. What was the result from the first trial? How about the 10\ :sup:`th` trial?                                                                                   |             |
|                                                                                                                                                                   |             |
| 2. How many Correct results were obtained overall?                                                                                                                |             |
|                                                                                                                                                                   |             |
| 3. What is the expected number of Correct results for this simulation model? Was the total Number of Correct close to the expected outcome for a deaf person? *   |             |
|    *                                                                                                                                                              |             |
+===================================================================================================================================================================+=============+
| 1. Click Run a second time. How many Correct responses were obtained for this deaf person?                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

Click Run a few more times. Count the number of Correct (out of 20) for
each iteration of the simulation and plot this outcome on the number
line below. Gather the outcomes from a few classmates in class. Does the
overall trend appear to mimic the outcomes we obtained in class?

|image64|

Tinkerplots\ :sup:`®` has the ability to keep a “history” of the number
of correct trials obtained over repeated iterations of the simulation.
This feature allows us to more easily record or keep track of the
outcomes over several iterations. In order to use this feature in
Tinkerplots\ :sup:`®`, we must first obtain a summary of the outcomes. A
plot and count will be used as our summary here.

Drag a new **Plot** into an open space.

|image65|

Next, drag the variable to be summarized (i.e., DeafExample) onto the
x-axis of the plot as is shown below on the right.

+----------------------------------------------------------------+-------------+
| | A plot summarizing the results is shown below. This          | |image67|   |
| | plot simply separates out the number of Correct responses.   |             |
|                                                                |             |
| |image66|                                                      |             |
+================================================================+=============+
+----------------------------------------------------------------+-------------+

Tinkerplots has the ability to automatically count the number of Correct
and Incorrect outcomes. Select the “N” icon from the menu bar.

|image68|

*Recording the Outcomes over Repeated Iterations
*\ To record the total number of Correct responses for each iteration of
the simulation, right-click on the value for the number of Correct in
your plot and select **Collect Statistic**.

|image69|

+------------------------------------------------------------------------------+
| Definition                                                                   |
+==============================================================================+
| The ***statistic*** is a summary measurement computed from collected data.   |
+------------------------------------------------------------------------------+

The number of Correct responses will now be recorded in the History
table provided. To run additional iterations of this simulation, say 27
more to mimic our class size, put 27 in the Collect box and click
*Collect*. This will record the statistic for an additional 27
iterations.

|image70|

*Comment*: The Collect box is used to identify the number of additional
times the simulation will be repeated. Each row in the History table
represents the number of correct outcomes (out of 20).

+---------------+---------------+-------------------------------+----------------+----+-------------+
|               |               | Recording of Number of        |
|               |               | Correct from each iteration   |
+===============+===============+===============================+================+====+=============+
| Iteration 1   | Iteration 2   | …                             | Iteration 28   |    |             |
+---------------+---------------+-------------------------------+----------------+----+-------------+
| |image71|     | |image72|     | …                             | |image73|      |    | |image74|   |
+---------------+---------------+-------------------------------+----------------+----+-------------+

*Questions*

1. The number correct for Iteration 1 is 11. Verify this quantity by
   counting the number of correct guess for this iteration.

2. What is the smallest number of correct? For which iteration did this
   occur? What is the largest number of correct responses?

3. The values in the history table should be centered around 10. Why?

***
***

*Plotting the Outcomes over Repeated Iterations*

Although we can see each individual outcome in the table shown above, it
may be better to organize and display these outcomes using a plot.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Drag a new Plot onto your workspace. Next, click on the variable name from your collection in which the outcomes from the repeated iterations are stored and drag this onto the x-axis of the new plot.   | |image75|   |
+===========================================================================================================================================================================================================+=============+
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| In order to see the number of 8’s, 9’s, etc. from each iteration, you should drag any point all the way to the right so that the plot displays the individual numbers. The vertical Stack button can be used to neatly stack the points. Also, the size of the plotting symbol can be reduced with the slider on the bottom of the plot.   | |image76|   |
+============================================================================================================================================================================================================================================================================================================================================+=============+
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

A dotplot showing the outcomes from the 28 repeated iterations from this
simulation is shown below.

|image77|

*
Comment:* The lower and upper limit on the number line should be set to
0 and 20, respectively. This communicates the fact that values from 0 to
20 are possible outcomes. The axis limits can be set by double clicking
on the smallest axis label and entering 0 for Axis starts at. The upper
limit can be set to 20 by double clicking on the largest axis label.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| The Collect box can be used to obtain additional outcomes from this simulation model. For example, if the value 100 is entered in the Collect box, the graph will display a total of 128 outcomes. Each dot in this graph corresponds to the number of correct responses out of a possible 20 trials.   | |image78|   |
|                                                                                                                                                                                                                                                                                                         |             |
| The outcomes from my simulation model are shown below.                                                                                                                                                                                                                                                  |             |
+=========================================================================================================================================================================================================================================================================================================+=============+
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

|image79|

On the number line below, give a rough sketch of the outcomes from your
simulation model.

|image80|

*Questions*

1. What does each dot on your graph represent? Discuss.

2. If an individual is really deaf, what outcomes are we likely to
   observe?

3. What is the smallest value in your dotplot?
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   a. Is it possible to obtain a value smaller than this if more
      simulations were carried out?

   b. If one additional simulation is done, is this outcome likely to be
      smaller, larger, or about the same as the previous smallest value?
      Discuss.

4. A statistician might argue that a plot based on 128 iterations of the
   simulation is *better* than a plot based on 28 iterations. Do you
   agree? Explain.

+-----------------------------------+-------------+
| Effect of Additional Iterations   |
+===================================+=============+
| Graph A                           | |image81|   |
|                                   |             |
| 28 iterations                     |             |
+-----------------------------------+-------------+
| Graph B                           | |image82|   |
|                                   |             |
| 128 iterations                    |             |
+-----------------------------------+-------------+
| Graph C                           | |image83|   |
|                                   |             |
| 1000 iterations                   |             |
+-----------------------------------+-------------+
| Graph D                           | |image84|   |
|                                   |             |
| 10,000 iterations                 |             |
+-----------------------------------+-------------+

*Questions*

1. What are the similarities amongst these four graphs?

2. What would you consider an *unusual* outcome (i.e., outlier) to be in
   Graph A? How about Graph B?

+-------------------------------------------------------------------------------------------------------------------------------+
| Developing a Rule for Identifying Outliers                                                                                    |
+===============================================================================================================================+
| An ***outlier rule*** determines the location on the distribution for which you begin to believe observations are unlikely.   |
+-------------------------------------------------------------------------------------------------------------------------------+

*Comments: *

-  A statistician might argue that the determination of what constitutes
   an outlier should not be adversely affected by the number of
   iterations conducted in the simulation. In fact, if enough iterations
   of the simulation model are completed, eventually all possible values
   will appear on the dotplot.

-  An outlier rule is used to separate *likely* from *unlikely*
   observations. This is the main goal of obtaining the distribution for
   the number of correct responses. For example, a statistician might
   say that a value of **6 or less** would be a reasonable outlier rule.
   Such a rule can and should be applied consistently with any of the
   graphs shown above.

-  In Tinkerplots\ :sup:`®`, the Divider icon from the tool shelf can be
   used to count the number of outcomes in a particular region in the
   graph. For example, there are 539 outcomes at 6 or less.

|image85|

Suppose a statistician decides to use 6 or less as the rule for
determining when somebody is lying about their ability to hear. This
rule would result in accusing a deaf person of lying about
:math:`\frac{539}{10000} = 0.0539 \approx 5\%` , which is about 1 out of
every 20 times.

*
*

*Questions*

1. Suppose instead of using 6 or less as the rule, 7 or less was used.
   Would this result in more or less deaf people being identified as
   lying? Would you advocate changing the rule to 7? Discuss.

2. Would an insurance company who fears insurance fraud rather a
   statistician use the rule of 6 or less or 7 or less? Discuss.

*Task*:

Set up a spinner in Tinkerplots\ :sup:`®` as follows to evaluate the
subject presented in the article by Pankratz, Fausti, and Peed titled “A
Forced-Choice Technique to Evaluate Deafness in the Hysterical or
Malingering Patient.” *Source: Journal of Consulting and Clinical
Psychology, 1975, Vol. 43, pg. 421-422. *

In this study, the subject was asked to complete 100 trials (instead of
20 as used above). The Repeat value on the spinner should thus be set to
100.

+--------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| +--------------------------------------------------------------------------------------------------+-----------------------------------------+   | |image86|                                       |
| | Necessary information for building a model                                                       | Deaf Example                            |   |                                                 |
| +==================================================================================================+=========================================+   |                                                 |
| | -  Number of completed trials                                                                    | 100                                     |   |                                                 |
| +--------------------------------------------------------------------------------------------------+-----------------------------------------+   |                                                 |
| | -  The likelihood or chance of obtaining a correct response *assuming* the subject cannot hear   | 1 out of 2; i.e., :math:`\frac{1}{2}`   |   |                                                 |
| +--------------------------------------------------------------------------------------------------+-----------------------------------------+   |                                                 |
|                                                                                                                                                  |                                                 |
| Sketch the final graph obtained in Tinkerplots\ :sup:`®` for your simulation.                                                                    |                                                 |
+==================================================================================================================================================+=================================================+
| Outcome from                                                                                                                                     | |image87|                                       |
|                                                                                                                                                  |                                                 |
| Study                                                                                                                                            |                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| Likely Outcomes from a Deaf Person                                                                                                               | |image88|                                       |
|                                                                                                                                                  |                                                 |
|                                                                                                                                                  | Number of Correct Responses for a Deaf Person   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+

*Questions*:

1. If a person is truly deaf, how likely is it that they would obtain 36
   or less correct out of 100 trials?

NOT VERY LIKELY \| SOMEWHAT LIKELY \| LIKELY \| VERY LIKELY

1. Does your investigation support or refute the notion that the subject
   under investigation is most likely lying about his ability to hear?
   Discuss.

Section 1.4: Additional Applications of Two-Alternative Forced Choice
Models

*Example 1.4.1*: Gender Discrimination

This fictitious example involves an evaluation of possible
discrimination against female employees. Suppose a large supermarket
chain occasionally selects employees to receive management training. A
group of female employees has claimed that they are less likely than
male employees of similar qualifications to be chosen for this training.

The large employee pool that can be tapped for management training is
60% female and 40% male; however, since the management program began, 9
of the 20 employees chosen for management training were female (only
45%).

*Question of Interest*: Is there evidence of gender discrimination for
those chosen for management training? **
**

***Setting up the Simulation Study***

To investigate this research question, we will carry out a simulation in
Tinkerplots 2®. Once again, note that you will have to revise a few
elements of the simulation that relate to the following questions:

*Questions*

1. What are the two possible outcomes for each trial?

2. What is the chance or probability for each outcome, given that there
   is no discrimination?

3. How many employees were selected for management training?

Use the answer to the above questions to setup the appropriate spinner
in Tinkerplots.

|image89|

For this problem, it is necessary to change the chance or probability on
the spinner to match the situation presented here.

+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
| To specify a proportion different than 50/50, select Show Proportion from the drop down menu on the lower left of the spinner. This is shown here.   | Next, change the proportion to the appropriate values.   |
+======================================================================================================================================================+==========================================================+
| |image90|                                                                                                                                            | |image91|                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+

The following shows the outcome from one trial.

|image92|

*Questions*

1. In this study 20 individuals were selected for management training.
   The anticipated number of females is \*not\* 10. It actually larger
   than 10? What is the anticipated number of females? Explain.

2. Propose a formula for determining the anticipated number of females.
   Use your formula to determine the anticipated number of females if 50
   individuals were selected for management training.

The following plot shows the outcomes from 1000 trials.

**
**\ |image93|

*Questions*

1. Under which situation were these dots generated?

i.   These dots were generated under the situation of possible
     discrimination against women and that this discrimination was
     intentional.

ii.  These dots were generated under the situation of possible
     discrimination against women, but believe the discrimination was
     unintentional.

iii. These dots were generated under the situation of no discrimination
     against women.

Explain your reasoning.

1. What does each dot on the graph represent?

2. Using the outcomes from the above simulation of 1000 trials, how many
   women (out of 20) would you have to see in order to say
   discrimination is likely occurring? Sketch this cutoff value on the
   number line below. Explain how you obtained this cutoff value.

    |image94|

1. The outcome from this study had 9 women out of 20 selected for
   management training? Does this outcome provide evidence to suggest
   discrimination against women is occurring? Explain.

*Example 1.4.2*: Ear Infections (Source: Rosner)\ **
**\ A common symptom of otitis media (ear infection) in young children
is the prolonged presence of fluid in the middle ear. The hypothesis has
been proposed that babies who are breast-fed for at least 1 month may
build up some immunity against the effects of the condition. A small
study of 24 pairs of babies is set up, where the babies are matched on a
one-to-one basis according to age, sex, socioeconomic status, and type
of medications taken. One member of the matched pair is a breast-fed
baby and the other was bottle-fed.

The primary outcome measurement recorded in this study was the duration
(in days) of fluid in the middle ear after the first episode of otitis
media. The results from the 24 pairs are below. Of interest is to make
comparisons between the breast-fed and bottle-fed babies. These
comparisons should be done *within each pair* of babies because of the
auxiliary factors that were considered in this study.

+-----------------------------------------------+
| Who did better in head-to-head comparisons?   |
+===============================================+
| |image95|                                     |
+-----------------------------------------------+

+------------------------------------------------------------------------------------------+
| Definition                                                                               |
+==========================================================================================+
| -  *Response Variable*: The primary outcome or measurement of interest in an analysis.   |
|                                                                                          |
|    -  Also known as: Dependent Variable or Y-Variable                                    |
+------------------------------------------------------------------------------------------+

Count the number of times breast-fed and bottle-fed babies did better
and complete the following table.

+-------------------------+-------------------+
| Outcome                 | Number of Pairs   |
+=========================+===================+
| Bottle-fed did better   |                   |
+-------------------------+-------------------+
| Breast-fed did better   |                   |
+-------------------------+-------------------+
| Tie                     |                   |
+-------------------------+-------------------+
| Total                   | 24                |
+-------------------------+-------------------+

Question

1. Pair #8 is a tie, what does this mean in the context of this problem?
   Does Pair #8 provide evidence for bottle-fed doing better, breast-fed
   doing better, or neither? Explain.

Consider the following pamphlet on Ear Infections in Children from the
Department of Health from the State of New York.

Link to Pamphlet:
`*http://www.health.state.ny.us/nysdoh/antibiotic/4815.pdf* <http://www.health.state.ny.us/nysdoh/antibiotic/4815.pdf>`__

|image96|

Do a Google search and identify other factors (i.e. called Risk Factors)
that are thought to influence the likelihood of a child getting an ear
infection.

Mayo Clinic Link:
`*http://www.mayoclinic.com/health/ear-infections/DS00303/DSECTION=risk-factors* <http://www.mayoclinic.com/health/ear-infections/DS00303/DSECTION=risk-factors>`__

Question

1. What are some of these risk factors? Discuss their potential
   influence.

*Setting Up an Experiment of this Type*

Consider the following mock situation. A researcher has obtained 48
volunteers for their study. They have obtained important demographic
variables for each of these 48 study participants and ask you to
determine how to best match-up these two sets of participants so that
comparisons will be done most fairly.

*Goal*: Propose a matching strategy for this study using the demographic
information provided below. (This data is provided on course web site.)

|image97|

Question

1. Discuss the process used for matching these pairs of babies for this
   mock experiment.

Consider the following mock study participants. Notice the ages for the
bottle-fed babies is considerably higher than the ages for the
breast-fed babies.

|image98|

*Questions*

1. Suppose Age is known to influence the occurrence of ear infections.
   Explain why the differences in the ages between the two groups
   hinders our ability to compare these two groups.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Definition                                                                                                                                                      |
+=================================================================================================================================================================+
| -  *Confounding Variable*: A variable that cannot be delineated from another variable when attempting to establish a relationship with the response variable.   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

*
*

In all our analyses thus far, we have been restricted to only two
outcomes. Recall, for this example we have three outcomes: 1) breast-fed
better, bottle-fed better, and one tie; as a result, when we construct
our spinner in Tinkerplots, we will not include the outcome from the
tie.

*Questions*

1. If the tie is removed, how many pairs do we have in our sample?

2. If there is no difference in the duration of ear infection between
   breast-fed and bottle-fed, for how many pairs should the bottle-fed
   babies do better than the breast-fed babies?

Set up a simulation in Tinkerplots to investigate the situation for
which there is no difference between the bottle-fed and breast-fed
babies. In your simulation, you should track the number of breast-fed
pairs.

|image99|

*Questions*

1. What would it mean in the context of this problem, if the outcome
   from our sample was at the smallest possible value on our graph?

2. What would it mean in the context of this problem, if the outcome
   from our sample was at the largest possible value on our graph?

3. Is the outcome from our sample (i.e. 16 pairs for which breast-fed
   doing better) an outlier? Discuss.

4. For this example, we will have two cutoff values. The reason we have
   two cutoff values is because the original question asked if there was
   a simply a difference (i.e. no preference to bottle-fed or breast-fed
   was given).

-  Upper cutoff value: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

-  Lower cutoff value: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1. Does the observed outcome from our sample provide enough
   *statistical* evidence to suggest breast or bottle fed babies have a
   lower duration of fluid in their inner ear? Explain.

.. |image0| image:: img_malone/media/image1.png
   :width: 5.76497in
   :height: 1.94444in
.. |image1| image:: img_malone/media/image2.png
   :width: 2.93396in
   :height: 2.61135in
.. |image2| image:: img_malone/media/image3.png
   :width: 2.81686in
   :height: 1.84722in
.. |image3| image:: img_malone/media/image4.png
   :width: 1.30171in
   :height: 1.45833in
.. |image4| image:: img_malone/media/image5.png
   :width: 4.80189in
   :height: 0.40426in
.. |image5| image:: img_malone/media/image6.png
   :width: 3.79245in
   :height: 0.47913in
.. |image6| image:: img_malone/media/image7.png
   :width: 2.38679in
   :height: 2.28015in
.. |image7| image:: img_malone/media/image8.png
   :width: 0.68829in
   :height: 0.64583in
.. |image8| image:: img_malone/media/image9.png
   :width: 0.68686in
   :height: 0.67676in
.. |image9| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image10| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image11| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image12| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image13| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image14| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image15| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image16| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image17| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image18| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image19| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image20| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image21| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image22| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image23| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image24| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image25| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image26| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image27| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image28| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image29| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image30| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image31| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image32| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image33| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image34| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image35| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image36| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image37| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image38| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image39| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image40| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image41| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image42| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image43| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image44| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image45| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image46| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image47| image:: img_malone/media/image10.png
   :width: 0.74528in
   :height: 0.49080in
.. |image48| image:: img_malone/media/image11.png
   :width: 0.21911in
   :height: 0.22642in
.. |image49| image:: img_malone/media/image5.png
   :width: 4.80189in
   :height: 0.40426in
.. |image50| image:: img_malone/media/image12.png
   :width: 4.93750in
   :height: 1.13542in
.. |image51| image:: img_malone/media/image13.png
   :width: 4.86458in
   :height: 0.19792in
.. |image52| image:: img_malone/media/image14.png
   :width: 4.88679in
   :height: 1.04644in
.. |image53| image:: img_malone/media/image15.png
   :width: 5.49758in
   :height: 0.40625in
.. |image54| image:: img_malone/media/image16.png
   :width: 2.99016in
   :height: 2.16506in
.. |image55| image:: img_malone/media/image17.png
   :width: 5.64151in
   :height: 0.83598in
.. |image56| image:: img_malone/media/image18.png
   :width: 5.14151in
   :height: 1.45087in
.. |image57| image:: img_malone/media/image19.png
   :width: 1.91510in
   :height: 1.23182in
.. |image58| image:: img_malone/media/image20.png
   :width: 2.18868in
   :height: 1.84773in
.. |image59| image:: img_malone/media/image21.png
   :width: 2.10337in
   :height: 1.84906in
.. |image60| image:: img_malone/media/image22.png
   :width: 2.16038in
   :height: 1.80869in
.. |image61| image:: img_malone/media/image23.png
   :width: 2.14151in
   :height: 1.85088in
.. |image62| image:: img_malone/media/image24.png
   :width: 3.04717in
   :height: 2.63461in
.. |image63| image:: img_malone/media/image25.png
   :width: 1.55011in
   :height: 3.89623in
.. |image64| image:: img_malone/media/image5.png
   :width: 4.80189in
   :height: 0.40426in
.. |image65| image:: img_malone/media/image26.png
   :width: 2.16981in
   :height: 0.63560in
.. |image66| image:: img_malone/media/image27.png
   :width: 2.24528in
   :height: 2.13124in
.. |image67| image:: img_malone/media/image28.png
   :width: 2.37892in
   :height: 2.39623in
.. |image68| image:: img_malone/media/image29.png
   :width: 2.70528in
   :height: 2.52830in
.. |image69| image:: img_malone/media/image30.png
   :width: 3.85862in
   :height: 2.26415in
.. |image70| image:: img_malone/media/image31.png
   :width: 2.80189in
   :height: 1.22004in
.. |image71| image:: img_malone/media/image25.png
   :width: 0.94208in
   :height: 2.36792in
.. |image72| image:: img_malone/media/image32.png
   :width: 0.85849in
   :height: 2.36792in
.. |image73| image:: img_malone/media/image33.png
   :width: 0.84906in
   :height: 2.36223in
.. |image74| image:: img_malone/media/image34.png
   :width: 1.58490in
   :height: 3.91595in
.. |image75| image:: img_malone/media/image35.png
   :width: 2.60377in
   :height: 1.55253in
.. |image76| image:: img_malone/media/image36.png
   :width: 2.76415in
   :height: 2.06148in
.. |image77| image:: img_malone/media/image37.png
   :width: 6.50000in
   :height: 1.09097in
.. |image78| image:: img_malone/media/image38.png
   :width: 1.49211in
   :height: 0.33962in
.. |image79| image:: img_malone/media/image39.png
   :width: 6.50000in
   :height: 2.37014in
.. |image80| image:: img_malone/media/image40.png
   :width: 6.50000in
   :height: 2.28611in
.. |image81| image:: img_malone/media/image37.png
   :width: 3.65348in
   :height: 0.61321in
.. |image82| image:: img_malone/media/image39.png
   :width: 3.65094in
   :height: 1.33127in
.. |image83| image:: img_malone/media/image41.png
   :width: 3.81876in
   :height: 1.30189in
.. |image84| image:: img_malone/media/image42.png
   :width: 3.82075in
   :height: 1.28052in
.. |image85| image:: img_malone/media/image43.png
   :width: 4.66038in
   :height: 1.64557in
.. |image86| image:: img_malone/media/image44.png
   :width: 1.86245in
   :height: 1.67049in
.. |image87| image:: img_malone/media/image45.png
   :width: 5.51886in
   :height: 0.27358in
.. |image88| image:: img_malone/media/image46.png
   :width: 5.55858in
   :height: 0.33019in
.. |image89| image:: img_malone/media/image47.png
   :width: 2.80168in
   :height: 2.39028in
.. |image90| image:: img_malone/media/image48.png
   :width: 3.23427in
   :height: 1.14151in
.. |image91| image:: img_malone/media/image49.png
   :width: 2.14287in
   :height: 1.65919in
.. |image92| image:: img_malone/media/image50.png
   :width: 2.25472in
   :height: 2.44567in
.. |image93| image:: img_malone/media/image51.png
   :width: 6.50000in
   :height: 3.03889in
.. |image94| image:: img_malone/media/image52.png
   :width: 5.73585in
   :height: 0.36768in
.. |image95| image:: img_malone/media/image53.png
   :width: 1.84847in
   :height: 3.96709in
.. |image96| image:: img_malone/media/image54.png
   :width: 6.50000in
   :height: 3.57358in
.. |image97| image:: img_malone/media/image55.png
   :width: 6.50000in
   :height: 2.53001in
.. |image98| image:: img_malone/media/image56.png
   :width: 6.50000in
   :height: 2.46389in
.. |image99| image:: img_malone/media/image57.png
   :width: 6.50000in
   :height: 2.39306in
