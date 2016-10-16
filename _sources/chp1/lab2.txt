Lab 2: Using Technologies to Construct Simulation Models
--------------------------------------------------------

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
