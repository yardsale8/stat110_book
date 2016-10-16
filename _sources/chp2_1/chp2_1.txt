Chapter 2 Part 1
================

The general approach used in a statistical investigation is shown in the
following diagram. Note that every investigation starts with a question
that gets converted to a research hypothesis. Though we will rarely
design our own studies in this course, we will discuss good strategies
and best practices for collecting data throughout the semester. Most of
our attention will be devoted to descriptive and inferential methods for
analyzing the data, how we decide whether the data supports the research
question, and how to write conclusions that appropriately summarize the
results of the study.

+-------------------------------+
| A Statistical Investigation   |
+===============================+
| |image0|                      |
+-------------------------------+

| In Chapter 2, we will discuss methods for making decisions concerning
  research hypotheses involving only a single categorical variable. Even
  though we’ll be adding lots of terminology and formalities along the
  way, we will use the same logical approach to investigating research
  questions that was introduced in Chapter 1.
| **
  *DESCRIPTIVE VS. INFERENTIAL STATISTICS
  ***

+---------------------------------------------------------------------------------------------------------------------------------------+
| Definitions                                                                                                                           |
+=======================================================================================================================================+
| -  **Descriptive statistics** are methods that describe, show, or summarize the data from our sample in a meaningful way.             |
|                                                                                                                                       |
| -  **Inferential statistics** are methods that allow us to draw conclusions about the larger population that the sample represents.   |
+---------------------------------------------------------------------------------------------------------------------------------------+

For example, recall the Helper vs. Hinder study from Example 1.2. In the
sample of 16 infants studied, 14 of the 16 picked the helper. What
descriptive methods might we use to *describe* the results of this
study?

***
FORMAL HYPOTHESIS TESTING***

| You are most likely already familiar with several methods for
  descriptive statistics (e.g., calculating percentages, constructing
  bar charts or pie charts, etc.). Inferential methods, however, may be
  new to you. Again, inferential statistics involves drawing conclusions
  about the larger population that our sample was supposed to represent.
  In several examples introduced in Chapter 1, we used a logical process
  to make statistical decisions concerning a population of interest – we
  were actually using inferential statistics already!
| Now, we will add more structure to these statistical investigations by
  introducing an inferential statistics procedure known as **hypothesis
  testing**. Note that in this chapter, we look at hypothesis testing
  for only research questions involving a single categorical variable.
  Before we discuss this procedure, however, we must introduce a few
  more definitions.

***Population Parameters vs. Sample Statistics***

In each of the previous examples, we tested a claim about a population
**parameter** of interest.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Definitions                                                                                                                                                                                                                            |
+========================================================================================================================================================================================================================================+
| -  A **parameter** is a numerical descriptive measure of a population. This value is almost always unknown, and our goal in a statistical investigation is typically to either estimate this parameter or test a claim regarding it.   |
|                                                                                                                                                                                                                                        |
| -  A **statistic** is a numerical descriptive measure of a sample. This value is calculated from the observed data.                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-------------------------------------------------------------------+-----------------+-----------------+
| **Example**                                                       | **Statistic**   | **Parameter**   |
+===================================================================+=================+=================+
| Example 1.2: Helper vs. Hinderer                                  |     **          |                 |
|                                                                   |     **          |                 |
+-------------------------------------------------------------------+-----------------+-----------------+
|     Example 1.3: Are women passed over for managerial training?   |                 |                 |
+-------------------------------------------------------------------+-----------------+-----------------+
|     Example 1.4: Font Preference                                  |                 |                 |
+-------------------------------------------------------------------+-----------------+-----------------+

*Hypothesis testing* is a procedure, based on sample evidence and
probability, used to test a claim regarding a population parameter. The
test will measure how well our observed sample statistic agrees with
some assumption about this population parameter.

Before you begin a hypothesis test, you should clearly state your
research hypothesis. For instance, let’s reconsider the research
hypotheses from three of our previous examples.

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| **Example**                                                       | **Research Hypothesis**                                                                              |
+===================================================================+======================================================================================================+
| Example 1.2: Helper vs. Hinderer                                  |     Ten-month-old infants prefer the helper toy over the hinderer toy.                               |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
|     Example 1.3: Are women passed over for managerial training?   |     This particular company is discriminating against females in the management selection process.   |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
|     Example 1.4: Font Preference                                  |     Consumers prefer one font over the other.                                                        |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

***
***\ Once the research hypothesis has been developed, we typically
formulate what are known as the null and alternative hypotheses. The
null and alternative hypotheses are both statements about the parameter
of interest in the study.

***Setting Up the Null and Alternative Hypothesis***

-  The *null hypothesis*, H\ :sub:`o`, is what we will assume to be true
   (i.e., we will assume for the time being that whatever effect we want
   to detect doesn’t exist in reality). We will then evaluate the
   observed outcome from our study against what outcomes we expected to
   see under the null hypothesis. This will always contain a statement
   saying that the population parameter is **equal** to some value.

-  The *alternative hypothesis*, H\ :sub:`a`, is what we are trying to
   show. Therefore, the research hypothesis is simply restated here as
   if it were true in the alternative hypothesis. This will always
   contain statements of inequality, saying that the population
   parameter is **less than, greater than, or different from** the value
   in the null hypothesis.

For our three examples, the null and alternative hypotheses are shown
below.

+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| **Research Hypothesis**                                                                              | **Null and Alternative Hypotheses**                                |
+======================================================================================================+====================================================================+
|     Ten-month-old infants tend to prefer the helper toy over the hinderer toy.                       | H\ :sub:`o`: The proportion of all 10-month-old infants            |
|                                                                                                      | that prefer the helper toy is only 50%.                            |
|                                                                                                      | H\ :sub:`a`: The proportion of all 10-month-old infants            |
|                                                                                                      | that prefer the helper toy is greater than 50%.                    |
+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
|     This particular company is discriminating against females in the management selection process.   |     | H\ :sub:`o`: The probability of a woman being selected       |
|                                                                                                      |     | for management is 60%.                                       |
|                                                                                                      |     | H\ :sub:`a`: The probability of a woman being selected       |
|                                                                                                      |     | for management is less than 60%.                             |
+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
|     Consumers prefer one font over the other.                                                        |     | H\ :sub:`o`: The proportion of all consumers that pick the   |
|                                                                                                      |     | Signet font is equal to 50%.                                 |
|                                                                                                      |     | H\ :sub:`a`: The proportion of all consumers that pick the   |
|                                                                                                      |     | Salem font is different from 50%.                            |
+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

***
***\ Note that we can also state these hypotheses in terms of the
population parameter of interest using formal notation:

+------------------------------------------------------------------------------------------------------+---------------------------------------+
| **Research Hypothesis**                                                                              | **Null and Alternative Hypotheses**   |
+======================================================================================================+=======================================+
|     Ten-month-old infants tend to prefer the helper toy over the hinderer toy.                       | H\ :sub:`o`:                          |
|                                                                                                      |                                       |
|                                                                                                      | H\ :sub:`a`:                          |
+------------------------------------------------------------------------------------------------------+---------------------------------------+
|     This particular company is discriminating against females in the management selection process.   | H\ :sub:`o`:                          |
|                                                                                                      |                                       |
|                                                                                                      | H\ :sub:`a`:                          |
+------------------------------------------------------------------------------------------------------+---------------------------------------+
|     Consumers prefer one font over the other.                                                        | H\ :sub:`o`:                          |
|                                                                                                      |                                       |
|                                                                                                      | H\ :sub:`a`:                          |
+------------------------------------------------------------------------------------------------------+---------------------------------------+

***Evaluating Evidence Using P-Values
***\ In in each of our three examples, we essentially *assumed the null
hypothesis was true* when setting up our spinner for the Tinkerplots
investigation. Then, we used the results simulated under this scenario
to help us decide whether observing results such as our sample data
would be an unusual event if the null hypothesis were true.

Up to this point, whether an observed study result was considered
unusual (or extreme) has been a rather subjective decision. Now, we will
discuss the guidelines used by statisticians to determine whether an
observed study result is extreme enough under the null hypothesis for us
to conclude that the evidence supports the research hypothesis.

First, note that in our three examples, we examined different parts of
the distribution of simulated outcomes when deciding whether the
observed study data was extreme. Each of these cases is an example of a
specific type of hypothesis test.

+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+-------------------------+
| **Research Hypothesis**                                                                              | **Hypotheses**                                                    | **Type of Test**        |
+======================================================================================================+===================================================================+=========================+
|     Ten-month-old infants tend to prefer the helper toy over the hinderer toy.                       | H\ :sub:`o`: π = .50                                              | Upper-tailed Test       |
|                                                                                                      | H\ :sub:`a`: π > .50                                              |                         |
|                                                                                                      | where π = the proportion that choose the helper                   |                         |
+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+-------------------------+
|     This particular company is discriminating against females in the management selection process.   |     | H\ :sub:`o`: π = .60                                        |     Lower-tailed Test   |
|                                                                                                      |     | H\ :sub:`a`: π < .60                                        |                         |
|                                                                                                      |     | where π = the proportion of those selected who are female   |                         |
+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+-------------------------+
|     Consumers prefer one font over the other.                                                        |     | H\ :sub:`o`: π = .50                                        |     Two-tailed Test     |
|                                                                                                      |     | H\ :sub:`a`: π ≠ .50                                        |                         |
|                                                                                                      |     | where π = the proportion that choose Signet font            |                         |
+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+-------------------------+

| ***
  ***\ Statisticians typically use the following guidelines to determine
  whether the observed data supports the research question:
| ***
  ***

+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Research Hypothesis**                                                                              | **Statistician’s Guideline for When**                                                                                                                      |
|                                                                                                      |                                                                                                                                                            |
|                                                                                                      | **Observed Outcome Supports the Research Question**                                                                                                        |
+======================================================================================================+============================================================================================================================================================+
|     Ten-month-old infants tend to prefer the helper toy over the hinderer toy.                       | |image1|                                                                                                                                                   |
|                                                                                                      |                                                                                                                                                            |
|                                                                                                      | *Upper-tailed test*: The observed outcome must fall in the *upper* 5% of the distribution obtained under the null hypothesis.                              |
+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|     This particular company is discriminating against females in the management selection process.   |     |image2|                                                                                                                                               |
|                                                                                                      |                                                                                                                                                            |
|                                                                                                      | *Lower-tailed test*: The observed outcome must fall in the *lower* 5% of the distribution obtained under the null hypothesis.                              |
+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|     Consumers prefer one font over the other.                                                        |     |image3|                                                                                                                                               |
|                                                                                                      |                                                                                                                                                            |
|                                                                                                      |     *Two-tailed test*: The observed outcome must fall in either the upper 2.5% or the lower 2.5% of the distribution obtained under the null hypothesis.   |
+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

Statisticians use what is called a ***p-value*** to quantify the amount
of evidence that an observed outcome from a set of data provides for a
research question.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Definition                                                                                                                                                                                       |
+==================================================================================================================================================================================================+
| *p-value*: The probability of observing an outcome as extreme (or even more extreme in favor of the research hypothesis) than the observed study result, assuming the null hypothesis is true.   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note that in each of the above examples, we obtained the simulation
results assuming the null hypothesis was true. Therefore, to *estimate*
the p-value, we simply determine how often outcomes as extreme (or even
more extreme) than the observed study results appeared in our simulation
study.

+--------------------------------------------------+---------------------------+
| **Example**                                      | **Estimate of p-value**   |
+==================================================+===========================+
| Helper vs. Hinderer? *                           |                           |
| *\ |image4|\ *                                   |                           |
| *\ |image5|                                      |                           |
+--------------------------------------------------+---------------------------+
| Are Women Passed Over for Managerial Training?   |                           |
|                                                  |                           |
| *                                                |                           |
| *\ |image6|                                      |                           |
|                                                  |                           |
| |image7|                                         |                           |
+--------------------------------------------------+---------------------------+
| | Font Preference?                               |                           |
| | |image8|                                       |                           |
|                                                  |                           |
| *                                                |                           |
| *\ |image9|                                      |                           |
+--------------------------------------------------+---------------------------+

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **Making a Decision with p-values**                                                                                                       |
+===========================================================================================================================================+
| -  If the p-value is less than .05 (5%), then the data provide enough statistical evidence to support the research question.              |
|                                                                                                                                           |
| -  If the p-value is not less than .05 (5%), then the data do not provide enough statistical evidence to support the research question.   |
+-------------------------------------------------------------------------------------------------------------------------------------------+

| Why does this decision rule work? Consider the “Helper vs. Hinderer”
  example. Because the p-value falls below 5%, the observed result
  *must* have been in the upper 5% of the reference distribution. As
  stated earlier, this implies that the observed study result is very
  unlikely to happen by chance under the null hypothesis, which supports
  the research question.
| On the other hand, consider the “Are Women Passed Over for Managerial
  Training” example. Because the p-value was larger than 5%, the
  observed result *can’*\ t have been in the lower 5% of the reference
  distribution. This implies that the observed study result is not all
  that unusual and could have easily happened by chance under the null
  hypothesis. Therefore, the null hypothesis *could* be true, and we
  have no evidence to support the research question.

This decision rule is widely accepted for determining whether study
results are statistically significant; however, some researchers do
advocate using a more flexible rule similar to the following:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Making a Decision with p-values, Revised**                                                                                                                    |
+=================================================================================================================================================================+
| -  If the p-value falls below .05, we have strong statistical evidence to support the alternative hypothesis (i.e., the research question).                     |
|                                                                                                                                                                 |
| -  If the p-value falls below .10 but above .05, we have “marginal” statistical evidence to support the alternative hypothesis (i.e., the research question).   |
|                                                                                                                                                                 |
| -  If the p-value is above .10, we have no evidence to support the research question.                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Next, we will review the steps involved in a formal hypothesis test for
each of our three examples. Note that our conclusions are written in the
context of the problem. Moreover, even a person with no statistical
background should be able to understand these conclusions (i.e., a
conclusion should NOT say something like “We reject the null
hypothesis.”)

+-------------------------------------+------------------------------------------------------------------------------------------+
| **Helper vs. Hinderer**             |
+=====================================+==========================================================================================+
| Research Hypothesis                 | Ten-month-old infants tend to prefer the helper toy over the hinderer toy.               |
+-------------------------------------+------------------------------------------------------------------------------------------+
| Null and Alternative Hypotheses     | H\ :sub:`o`: The proportion of all 10-month-olds that select the helper toy is 50%.      |
|                                     | H\ :sub:`a`: The proportion of all 10-month-olds that select the helper toy is greater   |
|                                     | than 50%.                                                                                |
+-------------------------------------+------------------------------------------------------------------------------------------+
| p-value estimated from simulation   |                                                                                          |
+-------------------------------------+------------------------------------------------------------------------------------------+
| Conclusion                          |                                                                                          |
+-------------------------------------+------------------------------------------------------------------------------------------+

+------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| **Are Women Passed Over for Managerial Training?**   |
+======================================================+==================================================================================================+
| Research Hypothesis                                  | This particular company is discriminating against females in the management selection process.   |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Null and Alternative Hypotheses                      | H\ :sub:`o`: The probability a woman is selected is 60%.                                         |
|                                                      | H\ :sub:`a`: The probability a woman is selected is less than 60%.                               |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| p-value estimated from simulation                    |                                                                                                  |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Conclusion                                           |                                                                                                  |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------+

+-------------------------------------+-------------------------------------------------------------------------------------------+
| **Font Preference**                 |
+=====================================+===========================================================================================+
| Research Hypothesis                 | Consumers prefer one font over the other.                                                 |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| Hypotheses                          | H\ :sub:`o`: The proportion of all consumers that select the Signet font is 50%.          |
|                                     |                                                                                           |
|                                     | | H\ :sub:`a`: The proportion of all consumers that select the Signet font is different   |
|                                     | | from 50%.                                                                               |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| p-value estimated from simulation   |                                                                                           |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| Conclusion                          |                                                                                           |
+-------------------------------------+-------------------------------------------------------------------------------------------+

Next, let’s carry out a formal hypothesis test for a few new examples.

| ***
  Example 2.1: Claims of Numbness after an Automobile Accident
  ***
| A 28-year-old white woman developed pain involving the spine and the
  left side of her body after an automobile collision. She was actively
  involved in a personal litigation against the company that owned the
  other vehicle, and she reported constant pain and numbness in the left
  arm. To test her claims, researchers touched her left arm with either
  1 finger or 2 fingers simultaneously while her eyes were closed. The
  word “touch” was said simultaneously with the presentation of the
  tactile stimulus so that the subject knew when to respond. She then
  had to indicate whether she felt 1 single touch or 2 simultaneous
  touches (with the double-touch stimulus, the fingertips were always
  spaced 2 inches apart). The subject received 100 stimuli overall; she
  was correct on 30 of them. Is there statistical evidence that she is
  intentionally answering incorrectly?

*Questions*:

1. Identify both the population and sample of interest.

2. Identify the single categorical variable of interest.

3. Identify both the parameter and statistic of interest.

4. Carry out the formal hypothesis test to address the research
   question.

+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **Claims of Numbness After Automobile Accident**   |
+====================================================+======================================================================================================================+
| Research Hypothesis                                | She is intentionally answering incorrectly.                                                                          |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Null and Alternative Hypotheses                    | H\ :sub:`o`:                                                                                                         |
|                                                    |                                                                                                                      |
|                                                    | H\ :sub:`a`:                                                                                                         |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| p-value estimated from simulation                  | Carry out the simulation study to investigate this p-value. Sketch in the spinner that you used:                     |
|                                                    |                                                                                                                      |
|                                                    | Sketch in the results of your simulation (keep track of the number of CORRECT responses on each trial):\ |image10|   |
|                                                    |                                                                                                                      |
|                                                    | Use the simulation results to estimate the p-value:                                                                  |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Conclusion                                         |                                                                                                                      |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

***Example 2.2: Effectiveness of an Experimental Drug***

Suppose a commonly prescribed drug for relieving nervous tension is
believed to be only 70% effective. Experimental results with a *new*
drug administered to a random sample of 20 adults who were suffering
from nervous tension show that 18 received relief. Is there statistical
evidence that the new experimental drug is more than 70% effective?

*Questions*:

1. Identify both the population and sample of interest.

2. Identify the single categorical variable of interest.

3. Identify both the parameter and statistic of interest.

4. Carry out the formal hypothesis test to address the research
   question.

+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| **Effectiveness of an Experimental Drug**   |
+=============================================+=============================================================================================================+
| Research Hypothesis                         | The new drug is more than 70% effective.                                                                    |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| Null and Alternative Hypotheses             | H\ :sub:`o`:                                                                                                |
|                                             |                                                                                                             |
|                                             | H\ :sub:`a`:                                                                                                |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| p-value estimated from the simulation       | Carry out the simulation study to estimate this p-value. Sketch in the spinner that you used:               |
|                                             |                                                                                                             |
|                                             | Sketch in the results of your simulation (keep track of the number that experience RELIEF on each trial):   |
|                                             |                                                                                                             |
|                                             | |image11|                                                                                                   |
|                                             |                                                                                                             |
|                                             | Use the simulation results to estimate the p-value:                                                         |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| Conclusion                                  |                                                                                                             |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+

***USING THE BINOMIAL DISTRIBUTION TO FIND EXACT P-VALUES
***

There is one caveat regarding our current approach to obtaining a
p-value. Certainly, different simulations will produce slightly
different simulated distributions. The general pattern will be the same,
but variations do exist. For example, consider the Helper vs. Hinderer
study.

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Helper vs. Hinderer**           |
+===================================+=======================================================================================================================================================================+
| Research Hypothesis               | Ten-month-olds show a preference for the helper toy over the hinderer toy.                                                                                            |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Null and Alternative Hypotheses   | Let π = the proportion of all ten-month-olds that choose the helper toy; equivalently, π = the probability a randomly selected 10-month-old selects the helper toy,   |
|                                   |                                                                                                                                                                       |
|                                   | | H\ :sub:`o`: π = 50%.                                                                                                                                               |
|                                   | | H\ :sub:`a`: π > 50%.                                                                                                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The study’s observed result was as follows: 14 out of 16 infants chose
the helper toy. What if two different researchers each carried out their
own simulation study to estimate the p-value?\ *
*

+--------------+------------------------------------------------------------------------+
| p-value      | | Simulation #1: p-value: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_               |
|              | | |image12|                                                            |
|              |                                                                        |
|              | | Simulation #2: p-value: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_               |
|              | | |image13|                                                            |
+==============+========================================================================+
| Conclusion   | We do have evidence that 10-month-old infants prefer the helper toy.   |
+--------------+------------------------------------------------------------------------+

| Fortunately, regardless of which simulation study we use in the
  previous example, the final conclusion is the same, and the
  discrepancy between the two estimated p-values is minimal; still, it’s
  not ideal that two different researchers get different results.
| Note that as the number of trials in our simulation study increases,
  we expect less discrepancy between these two estimates of the p-value.
  So, instead of using a simulation study with only 1,000 trials to
  *estimate* the p-value, we would ideally like to simulate this
  experiment over and over again, say an *infinite* number of times.
  This would provide us with the theoretical probabilities of interest
  so that can get exact p-values instead of an estimate of the p-value.
| The following graphic shows what the distribution would look like if
  we kept repeating the simulation study over and over again, each time
  counting and plotting the number of infants that chose the helper toy
  (assuming there was no real preference in the population of all
  infants). This theoretical probability distribution is known as the
  **binomial distribution**.
| |image14|

We can calculate these probabilities using the Excel file
**BinomialProbabilities.xls**, which can be found on the course website.

*Questions*:

1. Does the general pattern in the above graph agree with the simulated
   distributions obtained from the simulation study in Tinkerplots?

2. The binomial probability value for 14 is 0.0018, or .18%. What does
   this value mean? Explain.

3. When we estimated the p-value using the results of the simulation
   study, we calculated the proportion of dots at 14 or above. How would
   we obtain the p-value using binomial probabilities? Explain.

4. What is the p-value using the binomial probabilities?

Statisticians often use the binomial distribution to calculate p-values
when testing claims about a population proportion. However, before using
this distribution, we should check to make sure the following conditions
are met (note that these same conditions have to be met in order to
estimate the p-value via a simulation study, as well).

+---------------------------------------------------------------------------------------------------+
| ***The Binomial Distribution - When can we use it?***                                             |
|                                                                                                   |
| This distribution can be used whenever the following assumptions are met:                         |
|                                                                                                   |
| -  The study involves a fixed number of trials, n.                                                |
|                                                                                                   |
| -  There are only two possible outcomes on each trial (we call these a “success” or “failure”).   |
|                                                                                                   |
| -  The probability of “success” (π) remains constant from trial to trial.                         |
|                                                                                                   |
| -  The n trials are independent.                                                                  |
+===================================================================================================+
+---------------------------------------------------------------------------------------------------+

Check whether these assumptions seem reasonable for the Helper vs.
Hinderer study.

-  There exist a fixed number of trials, n.

-  There are only two possible outcomes on each trial (“success” or
       “failure”).

-  The probability of success (π) remains constant from trial to trial.

-  The n trials are independent.

***Example: Gender Discrimination
***

Recall that we already estimated the probability of observing 9 or fewer
women selected out of 20 if there was no discrimination (i.e., we
estimated the p-value with a simulation study).

|image15|\ ***
***

Estimated p-value = \_\_\_\_\_\_\_\_\_\_\_\_\_

Next, we will use the binomial distribution to find the exact p-value
for the Gender Discrimination Study. First, check whether the
assumptions behind the binomial distribution seem reasonable in this
case.

-  There exist a fixed number of trials, n.

-  There are only two possible outcomes on each trial (“success” or
       “failure”).

-  The probability of success (π) remains constant from trial to trial.

-  The n trials are independent.

+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| **Are Women Passed Over for Managerial Training?**   |
+======================================================+=======================================================================================================================================+
| Research Hypothesis                                  | The company is discriminating against women when they are selecting employees for management training.                                |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Null and Alternative Hypotheses                      | Let π = the probability the company selects a woman.                                                                                  |
|                                                      |                                                                                                                                       |
|                                                      | | H\ :sub:`o`: π = 60%.                                                                                                               |
|                                                      | | H\ :sub:`a`: π < 60%.                                                                                                               |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| p-value                                              | | To find the exact p-value, we will use the binomial distribution with…                                                              |
|                                                      | | n = \_\_\_\_\_\_\_\_                                                                                                                |
|                                                      |                                                                                                                                       |
|                                                      | | π = \_\_\_\_\_\_\_                                                                                                                  |
|                                                      | | |image16|                                                                                                                           |
|                                                      | | p-value: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_                                                                                   |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Conclusion                                           | We do not have enough evidence that the company is discriminating against females when selecting employees for management training.   |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+

***
***

***
***

***Example: Font Preference***

Finally, we will use the binomial distribution to find the exact p-value
for the Font Preference Study. Recall that we have already estimated
this p-value using a simulation study:

|image17|

Estimated p-value = \_\_\_\_\_\_\_\_\_\_\_\_\_

Before we use the binomial distribution to find the exact p-value, we
will first check whether the assumptions behind the binomial
distribution seem reasonable in this case.

-  There exist a fixed number of trials, n.

-  There are only two possible outcomes on each trial (“success” or
       “failure”).

-  The probability of success (π) remains constant from trial to trial.

-  The n trials are independent.

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Font Preference Study**         |
+===================================+==============================================================================================================================================================================+
| Research Hypothesis               | Consumers prefer one font over the other.                                                                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Null and Alternative Hypotheses   | Let π = the proportion of all consumers that would choose the Signet font; equivalently, let π = the probability of a randomly selected consumer choosing the Signet font.   |
|                                   |                                                                                                                                                                              |
|                                   | | H\ :sub:`o`: π = 50%.                                                                                                                                                      |
|                                   | | H\ :sub:`a`: π ≠ 50%.                                                                                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| p-value                           | | To find the exact p-value, we will use the binomial distribution with…                                                                                                     |
|                                   | | n = \_\_\_\_\_\_\_\_ and π = \_\_\_\_\_\_\_                                                                                                                                |
|                                   |                                                                                                                                                                              |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | **Number of "Successes"**   | **Binomial Probabilities**   |                                                                                                               |
|                                   | +=============================+==============================+                                                                                                               |
|                                   | | 0                           | 9.09495E-13                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 1                           | 3.63798E-11                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 2                           | 7.09406E-10                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 3                           | 8.98581E-09                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 4                           | 8.31187E-08                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 5                           | 5.98455E-07                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 6                           | 3.49099E-06                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 7                           | 1.69562E-05                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 8                           | 6.99444E-05                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 9                           | 0.000248691                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 10                          | 0.000770943                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 11                          | 0.002102571                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 12                          | 0.005081214                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 13                          | 0.010944152                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 14                          | 0.02110658                   |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 15                          | 0.036584738                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 16                          | 0.057163653                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 17                          | 0.080701628                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 18                          | 0.103118747                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 19                          | 0.119400655                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 20                          | 0.125370688                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 21                          | 0.119400655                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 22                          | 0.103118747                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 23                          | 0.080701628                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 24                          | 0.057163653                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 25                          | 0.036584738                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 26                          | 0.02110658                   |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 27                          | 0.010944152                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 28                          | 0.005081214                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 29                          | 0.002102571                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 30                          | 0.000770943                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 31                          | 0.000248691                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 32                          | 6.99444E-05                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 33                          | 1.69562E-05                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 34                          | 3.49099E-06                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 35                          | 5.98455E-07                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 36                          | 8.31187E-08                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 37                          | 8.98581E-09                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 38                          | 7.09406E-10                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 39                          | 3.63798E-11                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   | | 40                          | 9.09495E-13                  |                                                                                                               |
|                                   | +-----------------------------+------------------------------+                                                                                                               |
|                                   |                                                                                                                                                                              |
|                                   | |image18|                                                                                                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Conclusion                        | There is evidence that consumers have a preference towards one font over the other (more chose the Signet font).                                                             |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***Practice Problems***

1. Consider Example 2.1 (Claims of Numbness after an Automobile
   Accident).

   a. Check the conditions for the binomial distribution in the context
      of this example.

   b. Find the exact p-value using the binomial distribution.

2. Consider Example 2.2 (Effectiveness of an Experimental Drug).

   a. Check the conditions for the binomial distribution in the context
      of this example.

   b. Find the exact p-value using the binomial distribution.

***MORE ON USING P-VALUES TO MAKE DECISIONS
***

As mentioned earlier, some researchers advocate using the following
guidelines:

+---------------------------------------------------------------------------------------------------------------------+
| -  If the p-value falls below .05, there is strong evidence to support the research hypothesis.                     |
|                                                                                                                     |
| -  If the p-value falls below .10 but above .05, there is “marginal” evidence to support the research hypothesis.   |
|                                                                                                                     |
| -  If the p-value is above .10, there is not enough evidence to support the research hypothesis.                    |
+=====================================================================================================================+
+---------------------------------------------------------------------------------------------------------------------+

| In general, the smaller the p-value, the less likely the results of
  the study are due to random chance; thus, the more evidence we have
  that to support the research hypothesis. In some disciplines, the
  p-value must be much smaller than .05 in order to support a research
  hypothesis. For example, physics journals often like to see p < .001.
| Though the above guidelines allow for claims of “marginal” evidence
  when p-values fall between .05 and .10, some statisticians caution
  against this. For example, Irwin Bross argues that such modifications
  would be detrimental in evaluating evidence.

    *Anyone familiar with certain areas of the scientific literature
    will be well aware of the need for curtailing language-games. Thus
    if there were no 5% level firmly established, then some persons
    would stretch the level to 6% or 7% to prove their point. Soon
    others would be stretching to 10% and 15% and the jargon would
    become meaningless. Whereas nowadays a phrase such as statistically
    significant difference provides some assurance that the results are
    not merely a manifestation of sampling variation, the phrase would
    mean very little if everyone played language-games. To be sure,
    there are always a few folks who fiddle with significance
    levels--who will switch from two-tailed to one-tailed tests or from
    one significance test to another in an effort to get positive
    results. However such gamesmanship is severely frowned upon.*

    *Source:  Bross IDJ (1971), "Critical Levels, Statistical Language
    and Scientific Inference," in Foundations of Statistical Inference.
    *

The “.05 rule” is usually attributed to R.A. Fisher. His published
thoughts on the matter are given below.

    *In the investigation of living beings by biological methods
    statistical tests of significance are essential. Their function is
    to prevent us being deceived by accidental occurrences, due not to
    the causes we wish to study, or are trying to detect, but to a
    combination of the many other circumstances which we cannot control.
    An observation is judged significant, if it would rarely have been
    produced, in the absence of a real cause of the kind we are seeking.
    It is a common practice to judge a result significant, if it is of
    such a magnitude that it would have been produced by chance not more
    frequently than once in twenty trials. This is an arbitrary, but
    convenient, level of significance for the practical investigator,
    but it does not mean that he allows himself to be deceived once in
    every twenty experiments. The test of significance only tells him
    what to ignore, namely all experiments in which significant results
    are not obtained. He should only claim that a phenomenon is
    experimentally demonstrable when he knows how to design an
    experiment so that it will rarely fail to give a significant result.
    Consequently, isolated significant results which he does not know
    how to reproduce are left in suspense pending further
    investigation.*

    *Source: R.A. Fisher (1929), “The Statistical Method in Psychical
    Research,” from the* Proceedings of the Society for Psychical
    Research\ *, 39, 189-191.  *

| ***EXAMINING THE EFFECT OF SAMPLE SIZE
  Example 2.3: Gender Discrimination, Revisited
  ***
| Once again, consider the Gender discrimination example. Recall that of
  the 20 persons selected for management so far, only 9 (or 9/20 = 45%)
  were female. In an unbiased selection process, we expected to see a
  woman selected 60% of the time. We found that the probability of
  observing 9 or fewer women selected by chance if the company was in
  fact using a fair selection process was .1275.
| |image19|

| Now, suppose that the results had actually been as follows: Of the
  last 40 persons selected for management so far, only 18 (or 18/40 =
  45%) were female. How does this change the calculation of the p-value?
| The binomial probabilities for this scenario are shown below.

+-----------------------------+------------------------------+
| **Number of "Successes"**   | **Binomial Probabilities**   |
+=============================+==============================+
| 0                           | 1.20893E-16                  |
+-----------------------------+------------------------------+
| 1                           | 7.25355E-15                  |
+-----------------------------+------------------------------+
| 2                           | 2.12166E-13                  |
+-----------------------------+------------------------------+
| 3                           | 4.03116E-12                  |
+-----------------------------+------------------------------+
| 4                           | 5.59324E-11                  |
+-----------------------------+------------------------------+
| 5                           | 6.0407E-10                   |
+-----------------------------+------------------------------+
| 6                           | 5.28561E-09                  |
+-----------------------------+------------------------------+
| 7                           | 3.85094E-08                  |
+-----------------------------+------------------------------+
| 8                           | 2.38277E-07                  |
+-----------------------------+------------------------------+
| 9                           | 1.27081E-06                  |
+-----------------------------+------------------------------+
| 10                          | 5.90928E-06                  |
+-----------------------------+------------------------------+
| 11                          | 2.41743E-05                  |
+-----------------------------+------------------------------+
| 12                          | 8.76319E-05                  |
+-----------------------------+------------------------------+
| 13                          | 0.000283118                  |
+-----------------------------+------------------------------+
| 14                          | 0.000819021                  |
+-----------------------------+------------------------------+
| 15                          | 0.002129454                  |
+-----------------------------+------------------------------+
| 16                          | 0.004990908                  |
+-----------------------------+------------------------------+
| 17                          | 0.010568983                  |
+-----------------------------+------------------------------+
| 18                          | 0.020257217                  |
+-----------------------------+------------------------------+
| 19                          | 0.035183587                  |
+-----------------------------+------------------------------+
| 20                          | 0.055414149                  |
+-----------------------------+------------------------------+
| 21                          | 0.07916307                   |
+-----------------------------+------------------------------+
| 22                          | 0.102552159                  |
+-----------------------------+------------------------------+
| 23                          | 0.120387317                  |
+-----------------------------+------------------------------+
| 24                          | 0.127911524                  |
+-----------------------------+------------------------------+
| 25                          | 0.122795063                  |
+-----------------------------+------------------------------+
| 26                          | 0.106264959                  |
+-----------------------------+------------------------------+
| 27                          | 0.082650523                  |
+-----------------------------+------------------------------+
| 28                          | 0.057560186                  |
+-----------------------------+------------------------------+
| 29                          | 0.035727012                  |
+-----------------------------+------------------------------+
| 30                          | 0.019649857                  |
+-----------------------------+------------------------------+
| 31                          | 0.009507995                  |
+-----------------------------+------------------------------+
| 32                          | 0.004011185                  |
+-----------------------------+------------------------------+
| 33                          | 0.001458613                  |
+-----------------------------+------------------------------+
| 34                          | 0.000450454                  |
+-----------------------------+------------------------------+
| 35                          | 0.000115831                  |
+-----------------------------+------------------------------+
| 36                          | 2.41315E-05                  |
+-----------------------------+------------------------------+
| 37                          | 3.91321E-06                  |
+-----------------------------+------------------------------+
| 38                          | 4.63406E-07                  |
+-----------------------------+------------------------------+
| 39                          | 3.56467E-08                  |
+-----------------------------+------------------------------+
| 40                          | 1.33675E-09                  |
+-----------------------------+------------------------------+

| For this scenario, the p-value is given by
  \_\_\_\_\_\_\_\_\_\_\_\_\_\_.
| Finally, we can also consider a third study in which of the last 200
  persons selected for management so far, only 90 (or 90/200 = 45%) were
  female. How would you find the p-value for this scenario?
| For this scenario, the p-value is given by
  \_\_\_\_\_\_\_\_\_\_\_\_\_\_.

Recall that these binomial distributions give us an idea of what
outcomes occur by chance when the selection process does *not*
discriminate based on gender (because we used π = 60%).

+---------------------------+----+
| **Study #1: **            |    |
|                           |    |
| | **n = 20 trials         |    |
|   **\ Observed Result =   |    |
| | 9/20 = 45%              |    |
+===========================+====+
| **Study #2: **            |    |
|                           |    |
| | **n = 40 trials         |    |
|   **\ Observed Result =   |    |
| | 18/40 = 45%             |    |
+---------------------------+----+
| **Study #3:               |    |
| n = 200 trials**          |    |
| Observed Result =         |    |
| 90/200 = 45%              |    |
+---------------------------+----+

*
Question*\ **:
**

Which of the following statements is most correct?

i.   The three studies provide equally convincing statistical evidence
     that the selection process discriminates against women.

ii.  Study #1 provides the most convincing statistical evidence that the
     selection process discriminates against women.

iii. Study #2 provides the most convincing statistical evidence that the
     selection process discriminates against women.

iv.  Study #3 provides the most convincing statistical evidence that the
     selection process discriminates against women.

Explain your reasoning.

| ***
  PRACTICAL SIGNIFICANCE VERSUS STATISTICAL SIGNIFICANCE
  ***\ Consider the previous example. As discussed earlier, the result
  in Study #1 is not “statistically significant” because the observed
  outcome does not fall in the bottom 5% of simulated outcomes (i.e.,
  the p-value is not below .05). On the contrary, the results in Study
  #2 and Study #3 are “statistically significant.” The previous example
  illustrates that statistical significance depends on the sample size.
  All three studies resulted in an outcome of 45% of those selected for
  management being female, but this result was only statistically
  significant in the studies with the larger sample size.
| This presents a conundrum: If a study’s results are not statistically
  significant, it could be that the effect under study is real, but the
  sample size wasn’t large enough to detect that effect (this relates to
  a concept known as the *power* of a hypothesis test which is discussed
  in upper-level statistics courses). On the other hand, if the sample
  size is large enough, very small differences between the observed
  results and the expected value in the null hypothesis can lead to
  statistically significant differences.
| To counter this, researchers often consider “practical significance”
  in addition to “statistical significance.” A result is known as
  “practically significant” if the difference between the observed and
  expected result is large enough to be of value in the practical sense.

***Example 2.4: Dukes vs. Wal-mart Stores, Inc.***

The lead plaintiff in this case, Betty Dukes, was a Wal-Mart employee.
She and others alleged gender discrimination in promotion policies and
practices in Wal-Mart stores.

As the nation’s largest private employer, Wal-Mart makes tens of
thousands of promotion decisions each year. The following data was
provided during this trial: Wal-Mart promoted roughly 50,000 individuals
to management between 1997 and 2002. Female employees constituted about
60% of the group eligible for these promotions.

*Questions*:

1. How many of the 50,000 individuals promoted do you expect to be
   female if Wal-Mart is not discriminating based on gender?

2. Suppose that 29,780 of the individuals promoted were women (note that
   this was not the actual outcome in the court case). What percentage
   is this?

3. | A simulation study with 100 trials was conducted to see what
     outcomes occur by chance when the selection process is **not**
     discriminatory. The results are shown below.
   | |image20|
   | Recall the hypothetical observed value of 29,780 females being
     selected. The research hypothesis is that Wal-Mart is
     discriminating against women in their promotion policies and
     practices. Based on the results of the simulation study, is this
     result “statistically significant”? Explain.

4. In the previous question, you estimated the p-value for this research
   hypothesis. Use the binomial distribution to find the exact p-value.
   Again, is the result “statistically significant”?

5. Is this result “practically significant”? Explain.

6. Do you foresee any problems if we rely on only statistical
   significance when making decisions? Explain.

.. |image0| image:: img/media/image1.png
   :width: 6.50000in
   :height: 3.55833in
.. |image1| image:: img/media/image2.png
   :width: 4.29511in
   :height: 1.84332in
.. |image2| image:: img/media/image3.png
   :width: 4.45833in
   :height: 1.63377in
.. |image3| image:: img/media/image4.png
   :width: 4.53774in
   :height: 1.35987in
.. |image4| image:: img/media/image5.png
   :width: 4.31132in
   :height: 0.61492in
.. |image5| image:: img/media/image2.png
   :width: 4.15625in
   :height: 1.78372in
.. |image6| image:: img/media/image6.png
   :width: 4.48113in
   :height: 0.46295in
.. |image7| image:: img/media/image3.png
   :width: 4.25000in
   :height: 1.55743in
.. |image8| image:: img/media/image7.png
   :width: 4.45283in
   :height: 0.43006in
.. |image9| image:: img/media/image4.png
   :width: 4.42453in
   :height: 1.32594in
.. |image10| image:: img/media/image9.png
   :width: 5.21698in
   :height: 1.24405in
.. |image11| image:: img/media/image10.png
   :width: 4.79167in
   :height: 1.53528in
.. |image12| image:: img/media/image11.png
   :width: 3.70833in
   :height: 1.56548in
.. |image13| image:: img/media/image12.png
   :width: 3.65625in
   :height: 1.44243in
.. |image14| image:: img/media/image13.png
   :width: 6.50000in
   :height: 3.06389in
.. |image15| image:: img/media/image3.png
   :width: 5.82292in
   :height: 2.13383in
.. |image16| image:: img/media/image14.png
   :width: 5.35583in
   :height: 2.70881in
.. |image17| image:: img/media/image4.png
   :width: 6.15240in
   :height: 1.84375in
.. |image18| image:: img/media/image15.png
   :width: 4.85156in
   :height: 2.95707in
.. |image19| image:: img/media/image16.png
   :width: 6.50000in
   :height: 3.26042in
.. |image20| image:: img/media/image20.png
   :width: 5.83333in
   :height: 1.70201in
