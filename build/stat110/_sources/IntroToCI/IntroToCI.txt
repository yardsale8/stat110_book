 .. raw:: html
 
     <script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

Introduction to Sampling Distributions
======================================

In this chapter we will introduce some important ideas from statistics.  We
will be focusing on quantitative data and in particular *estimation* of a 
population parameter.

Evaluating Studies
------------------

.. raw:: html

    <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
    <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=0_1iqsp4zw&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_j21dy1gf" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen frameborder="0"></iframe>
    </div>

In class, we conducted some simulations to identity the effect of the first of
two forms of randomization, *randomized selection of individual units*.  Based
on these activities, we identified two main effects of randomization.

.. admonition:: The effect of random selection of individuals in sampling

    Using a random sampling technique to select individuals resulted in
    **unbiased estimates** of parameters.  In other words, our statistics did not
    tend to over- or under-estimate the parameter, but balanced these errors
    instead.  (This assumes no other source of bias.)
    
When evaluating a statistical study, the first thing that should be considered
is the *appropriate scope of the conclusions*, that is to say the types of
conclusions that are justified for this type of study.  The following table
gives some advice on what conclusions can be drawn based on whether or not there was random sampling.

.. figure:: ../IntroToCI/img/evaluating_studies.png

    Evaluating studies cheat sheet

.. admonition:: A study on flossing and gum disease (experiment)

    A recent study was conducted to determine the effectiveness of flossing on
    gum disease.  A group of 500 volunteers were randomly split into two groups.
    The first group was asked to floss once a day and the second group was asked
    to floss after each meal.  Suppose that the group that flossed after every
    meal was much less likely to have gum disease as the group that flossed
    once per day.

    .. mchoice:: mc_evaluate_1
        :answer_a: Yes
        :answer_b: No
        :correct: b
        :feedback_a: Note that the description mentioned that the participants were volunteers.
        :feedback_b: The participants volunteered and were not randomly selected.

        Did this study use random sampling?

    .. mchoice:: mc_evaluate_2
        :answer_a: Yes, the effects the flossing treatments would be the same for the general population.
        :answer_b: No, there is a danger that our estimates of the effects of flossing on gum disease is likely biased.
        :correct: b
        :feedback_a: The participants in the study were volunteers and not a randomly selected sample.
        :feedback_b: The lack of a randomly selected sample means that we are in danger of biased estimates.

        Is it safe to generalize the results of this study?

.. admonition:: Another study on flossing and gum disease (observational study)

    In another study on flossing and gum disease, a random sample of 500 people
    were surveyed on their flossing habits and whether or not they suffered from
    gum disease.  Suppose that it was estimated that the people that flossed 
    after every meal was much less likely to have gum disease as the group 
    that flossed once per day.

    .. mchoice:: mc_evaluate_5
        :answer_a: Yes
        :answer_b: No
        :correct: a
        :feedback_b: The text explicitly mentioned a random sample.

        Did this study use random sampling?

    .. mchoice:: mc_evaluate_6
        :answer_a: Yes, the effects the flossing treatments will be the same for the general population.
        :answer_b: No, there is a danger that our estimates of the effects of flossing on gum disease is likely biased.
        :correct: a
        :feedback_a: Because we are taking a random sample, our statistics should be unbiased and not over- or under-estimate the rates of gum disease in each group.
        :feedback_b: What is the effect of random sampling on bias and a statistics ability to estimate a parameter?

        Is it safe to generalize the results of this study?

Overview of Statistical Inference
---------------------------------

.. raw:: html

    <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
    <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=0_avjiobd9&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_gftztrz5" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen frameborder="0"></iframe>
    </div>

When asking questions about some population of individuals, the ideal situation
is collecting information on all of the individuals of interest.  This is referred
to as *taking a census* of the population.  Most of the time, it is not feasible
to collect information on the entire population.  In this case, we collect data
on a sample of the population and use this information to make educated guesses
about the population.  This is referred to as **statistical inference**.  More
specifically, in statistical inference, we use *sample statistics* to make
inferences (guesses) about *population parameters*.

.. glossary::
    Statistical Inference
        The process of making educated guess about population parameters using
        information collected from a random sample, e.g. a sample statistic.

|image3000|


.. note::

    The federal government of the United States takes a "census" every 10 years,
    but there are a number of reasons this census falls short of the statistical
    definition.

    1. The population is defined over *households* not *individual citizens*. 
    2. The Census Bureau only attempts to collect a small amount of information on all households.  The long form is collected on a sample of households.
    3. There is a fraction of the population for which it is nearly impossible to survey

Notation for Parameters and Statistics
++++++++++++++++++++++++++++++++++++++

In statistics there is a very big distinction between parameters (number
describing a population) and statistics (numbers describing a sample).

.. admonition:: Distinction between Parameters and Statistics

    1. Parameters are thought of as the exact values that we would like to make guesses about.  They are generally too expensive to find exactly and are almost always unknown.
    2. Statistics are thought of as a guess of the value of a parameter.  They are not particularly interesting in their own right. 

The difference between parameters and statistics is so important that we use
different symbols to represent each.  The first summary method that we will 
focus on is the mean or average of quantitative data.  The symbol that we use
for a population mean (parameter) is :math:`\mu`, while the symbol we use for a
sample mean (statistic) is :math:`\bar{x}`.  The following table gives the
symbols for various parameters and statistics we will work within this
course.

|image3001|

Sampling Distributions
----------------------

.. raw:: html

    <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
    <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=0_gg1rn336&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_vl739nux" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen frameborder="0"></iframe>
    </div>

The first and most important fact that you need to realize when working with
statistics is **statistics vary from sample to sample**.  This is known as
*sampling variability* and most of the procedures in statistics are methods for
dealing with sampling variability.

.. glossary::
    Sampling Variability
        **Sampling variability** refers to the natural variation in statistics taken
        from different samples. It is very important to quantify this variability.
    Standard Error
        The **standard error** is the estimated standard deviation of the
        sample statistics.  It is an important measure of sampling variability.

To get an idea of the typical location of and variability between
 sample statistics (i.e. center and spread), we study the *sampling distribution*.

.. glossary::
    Sampling Distribution
        The **sampling distribution** is the distribution of a statistic
        constructed by repeatedly sampling from the same population using 
        the same sample size.

The next figure shows a simulated sampling distribution for the sample mean.
Each of the 40 dots represents a sample mean from a sample of 10 individuals 
and together these statistics form the sampling distribution.  We are 
interested in the properties of this distribution, in particular the 
*shape*, *center*, and *spread* of the statistics.  To get a better idea of
these qualities of the sampling distribution, we would need to sample many more
statistics.

|image3002|

.. mchoice:: mc_samp_dist_definition
    :answer_a: The distribution of the sample.
    :answer_b: The distribution of population parameter.
    :answer_c: The distribution of the sample statistic.
    :correct: c
    :feedback_a: This answer is not specific enough, what exactly do we collect from each sample?
    :feedback_b: The parameter is one fixed value and doesn't vary.  Talking about the distribution of a parameter is therefore pointless.

    The sampling distribution is ...

We have seen examples of a sampling distribution earlier in many of the
activities so far in the course.  We will use the `StatKey Website
<http://www.lock5stat.com/StatKey/index.html>`_ to explore the sampling
distribution of the sample mean.  The image below illustrates the various
components of the `StatKey's Sampling Distribution for a Mean page
<http://www.lock5stat.com/StatKey/sampling_1_quant/sampling_1_quant.html>`_.

|image3003|

.. admonition:: Check your Understanding

    The following graph uses capital letters to label various elements of the
    StatKey sampling distribution page.  Use these designations to answer each
    of the following questions.

    |image3004|


    .. mchoice:: mc_parts_samp_dist_1
        :answer_a: A
        :answer_b: B
        :answer_c: C
        :answer_d: D
        :correct: c

        The mean and standard error (standard deviation) of the sampling distribution are located
        at ....

    .. mchoice:: mc_parts_samp_dist_2
        :answer_a: A
        :answer_b: B
        :answer_c: C
        :answer_d: D
        :correct: b

        The sampling distribution is illustrated by ...

    .. mchoice:: mc_parts_samp_dist_3
        :answer_a: A
        :answer_b: B
        :answer_c: C
        :answer_d: D
        :correct: a

        A sample statistic (in this case a sample mean) is illustrated by ...

    .. mchoice:: mc_parts_samp_dist_4
        :answer_a: A
        :answer_b: B
        :answer_c: C
        :answer_d: D
        :correct: d

        A population parameter (in this case a population mean) is located at ...

.. TODO:: Add examples of computing the p-value using StatKey on the sampling distribution

.. include:: ../chp5/central_limit_theorem.rst
.. include:: ../chp5/assessing_normality.rst

.. |image3000| image:: ../IntroToCI/img/inference.png
   :width: 5.51873in
   :height: 4.30189in
.. |image3001| image:: ../IntroToCI/img/notation.png
   :width: 8.22in
   :height: 3.22in
.. |image3002| image:: ../IntroToCI/img/a_sampling_distribution.png
   :width: 4.05in
   :height: 1.75in
.. |image3003| image:: ../IntroToCI/img/statkey_sampling_distribution_mean.png
   :width: 4.05in
   :height: 3.05in
.. |image3004| image:: ../IntroToCI/img/test_parts_of_sampling_distribution.png
   :width: 8.05in
   :height: 4.55in
.. |image3005| image:: ../IntroToCI/img/middle95percent.png
   :width: 8.05in
   :height: 4.55in
.. |image3006| image:: ../IntroToCI/img/many_intervals.png
   :width: 3.05in
   :height: 4.55in
.. |image5010| image:: ../chp5/img/media/image12.png
   :width: 4.48663in
   :height: 1.70378in
.. |image5011| image:: ../chp5/img/media/image14.png
   :width: 2.25134in
   :height: 1.51344in
.. |image5012| image:: ../chp5/img/media/image15.png
   :width: 3.50802in
   :height: 1.68958in
.. |image5013| image:: ../chp5/img/media/image16.png
   :width: 2.19251in
   :height: 1.46647in
.. |image5014| image:: ../chp5/img/media/image17.png
   :width: 3.42781in
   :height: 1.73307in
.. |image5015| image:: ../chp5/img/media/image19.png
   :width: 3.25669in
   :height: 1.45399in
.. |image5016| image:: ../chp5/img/media/image21.png
   :width: 3.67708in
   :height: 1.74952in
.. |image5017| image:: ../chp5/img/media/image23.png
   :width: 3.71875in
   :height: 1.51978in
.. |image510| image:: ../chp5/img/histogram_normal_curve.png
   :width: 5.02in
   :height: 3.47in
.. |image511| image:: ../chp5/img/normal_data.png
   :width: 3.40in
   :height: 5.11in
.. |image512| image:: ../chp5/img/non_normal_data.png
   :width: 3.38in
   :height: 5.20in
.. |image516| image:: ../chp5/img/normal_quantile_plot.gif
   :width: 7.23in
   :height: 4.41in
