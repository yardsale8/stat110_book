.. raw::

    <script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

Introduction to Confidence Intervals
====================================

In this chapter we will introduce some important ideas from statistics.  We
will be focusing on quantitative data and in particular *estimation* of a 
population parameter.

Confidence Intervals Basics
---------------------------

.. raw:: html

    <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
   <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=0_uavvslod&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_7t0i2d8n" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen frameborder="0"></iframe>
    </div>

Recall that statistical inference is the process of using sample statistics to
make guesses/inferences about a population parameter.  One of the primary
examples of this type of inference is *estimating the value of a parameter*.

In this section, we discuss the two types of estimates we can make (point and
interval estimates), explore the proportion of sample means in a sampling
distribution that fall within 2 standard errors of the mean, leverage this
proportion to develop a good margin of error for a sample mean, put this all
together to construct a confidence interval for the mean, and investigate what
a statistician means when claiming to be "95% confident."

.. note::

    The *other* standard type of statistical inference involves testing a
    hypothesis about a parameter, a topic that we will devote more time on later
    in the course.

Point Estimates and Interval Estimates for Parameters
+++++++++++++++++++++++++++++++++++++++++++++++++++++

When estimating the value of a parameter, we can choose between one of two types
of estimates.

.. glossary::
    Point Estimate
        A **point estimate** is a single values estimate of the parameter (i.e.
        one number).  Examples of point estimates are sample statistics like the
        sample mean and sample standard deviation that are used as point
        estimates for the population mean and population standard deviation,
        respectively.
    Interval Estimate
       An **interval estimate** consists of a range of values that we believe
       are likely to contain the actual parameter.  Interval estimates usually
       come with a measure of how confident we are in the estimate (e.g. 95%
       confident).

When possible, it is best to use an interval estimate, because

1. We get a measurement of accuracy, as in how often the interval will 
   successfully contain the parameter.  This is called the *confidence level* 
   of the interval. An interval that comes with a confidence level is called a 
   *confidence interval*.
2. We get a sense of the precision of the estimate, which can be seen in the
   width of the interval.  Specifically, more precise estimates have narrower
   confidence intervals.

.. mchoice:: mc_type_estimate_1
    :answer_a: Point Estimate
    :answer_b: Interval Estimate
    :correct: a

    We estimate that the population mean height of all Winona State students to be 67 inches.  This is an example of a ...

.. mchoice:: mc_type_estimate_2
    :answer_a: Point Estimate
    :answer_b: Interval Estimate
    :correct: b

    We estimate that the population mean height of all Winona State students is between 65 and 69 inches.

.. TODO:: Add a section about biased guesses with pictures. Goal: Why the parameter in the middle is good

Approximating the Standard Error of a Statistic
+++++++++++++++++++++++++++++++++++++++++++++++

When constructing a confidence interval for the population mean, we will
construct the interval by creating a buffer around the sample mean.  To create
this buffer, we add and subtract the *margin of error* to/from the sample mean.  
The right width of buffer is dependent on how 
spread out the sample means tend to be, i.e. the spread of the sampling 
distribution.  The specific measure of spread that we use is the estimated 
standard deviation of the sample means, which is referred to as the 
*standard error of the mean*.

.. glossary::
    Margin of Error
        The **margin of error** is the buffer that is added to and subtracted 
        from the sample mean to construct an interval with a good chance of 
        containing the population mean.
    Standard Error of the Mean
        Our estimate of the standard deviation of all sample means, taken from
        random samples of the same size, is called **the standard error of the
        mean** and demoted with SE.

.. mchoice:: mc_definition_SE
    :answer_a:  the amount of buffer that is added to and subtracted from the sample mean.
    :answer_b:  a common mistake made by students in a statistics class when calculating the mean.
    :answer_c: the estimated standard deviation of the distribution of sample means.
    :correct: c

    The standard error of the mean is ...

Plus or Minus Two Standard Error and the Middle 95% of Statistics
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

For simplicity, we will focus on constructing a 95% confidence interval.  It
turns out that when the distribution of a statistic is symmetric and
bell-shaped, going out 2 SE from the population mean will cover about 95% of the
sample means.

To illustrate this fact, we have simulated the distribution of the sample mean
using the `StatKey Website
<http://www.lock5stat.com/StatKey/sampling_1_quant/sampling_1_quant.html>`_,
which is depicted in the figure shown below.  The middle 95% of the sample means
are shown with black dots, and we have colored the largest and smallest 2.5% of
the sample means red.  Furthermore, we can use this distribution to estimate the
SE of the mean, which can be found in the top right of the graph. Notice that 
adding and subtracting 2 SE to the population mean leads to upper and lower
bounds that are very close to the cut offs for the middle 95% of the
distribution. 

|image3005|

In the above figure we see that the limits generated by adding and subtracting 2
standard errors from the population mean (5.79 and 8.93) are very close to the cut-offs of
the middle 95% of the distribution (5.83 and 8.93).

.. caution::

    The above result will only work for distributions that are symmetric and
    bell shaped.  We will need a different approach for skewed distributions.

Due to the fact that about 95% of the sample means are within 2 standard errors
of the population mean, it makes sense to use this distance as the margin of
error for a 95% confidence interval.

.. admonition:: The Margin of Error for a 95% Confidence Interval for the Mean

    The **margin of error** for a 95% confidence interval is given by

    .. math::

        MoE = 2*SE

    This margin of error works because

    1. "A sample mean is in the middle 95% of the sample means" implies that the
       population mean will be within 2 SE of the sample mean.  
    2. Only the sample means in the lowest and highest 2.5% of the distribution
       will fail to capture the population mean in an interval using this
       margin of error.

In other words, if the sample mean is *close enough* to the population mean, the
population mean is *close enough* to the sample mean.

.. admonition:: The Main Point

    If the sample mean is *close enough* to the population mean, the population 
    mean is *close enough* to the sample mean.  Using a margin of error of 2
    standard errors means that about 95% of sample means are *close enough*.

          
.. mchoice:: mc_margin_95_percent
    :answer_a: 100%
    :answer_b: 95%
    :answer_c: We can't determine X, as the samples were randomly selected.
    :correct: b
    :feedback_a: You are too *confident* (that is a statistics joke)
    :feedback_c: While random samples are uncertain in the short term, they are predicitable in the long run.

     The interval constructed by adding and subtracting 2 SE to/from the
     population mean will contain X% of the sample means.  Identify the value of
     X.

Being (95%) Confident
+++++++++++++++++++++

Let's make sure we are clear on what it means to be 95% confident. Consider the
following figure, created using `StatKey Website
<http://www.lock5stat.com/StatKey/sampling_1_quant/sampling_1_quant.html>`_.
Each of the dots is a sample mean and each of the line segments extends out 2
standard errors.  The population mean is located at the solid vertical line,
recall that our goal in constructing such an interval is to capture the
population mean.

|image3006|

The intervals that are green successfully captured the population mean, and the
intervals that failed to capture the population mean are colored red.  Notice
that about 95% of the intervals successfully capture the population mean.

.. admonition:: Being "95% confident"

    When a statistician says that she is "95% confident", she means that she is
    using a procedure, that when used repeatedly on many random samples, will
    work 95% of the time.

.. caution::

    We purposely avoid the phrase "95% probability".  This is because each
    specific interval either works 100% of the time (captured the mean) or fails
    100% of the time (fails to capture the mean).  For example, suppose we take
    a sample and construct an interval, which turns out to be from 2.4 to 7.6.
    The population mean is either between these numbers or it is not.  Using
    "95% probability" in place of "95% confidence" makes it sound like this
    specific interval only works some of the time, when in fact it either always
    works or never works.

.. mchoice:: mc_meaning_of_confidence
    :answer_a: We are really pretty sure of the result.
    :answer_b: The interval we constructed from a specific sample will work 95% of the time.
    :answer_c: We are using a procedure that works 95% of the time, when applied to many, many samples.
    :correct: c
    :feedback_a: This answer is too vague, try being more specific.
    :feedback_b: Unfortunately, any single interval either works 100% of the time or 0% of the time.
    :feedback_c: Statisticians define success "in the long run."

    To a statistician, what does it mean to be "95% confident"?
 
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


.. include:: bootstrap_CI.rst

Confidence Intervals Based on the Normal Distribution
-----------------------------------------------------

In our bootstrap activities we have seen some common results.

.. admonition:: Important Points

    1. The distribution of the sample mean was often (but not always) a
       bell-shaped curve.
    2. Using a margin of error of 2 standard errors resulted in intervals that
       worked about 95% of the time.

In this section, we leverage these facts and introduce a theoretical
approach to confidence intervals that will save us the work of running a
simulation every time we want an interval.

.. include:: example5.1.rst

.. include:: example5.2.iverson.rst

.. include:: confidence_interval_single_mean.rst

Confidence Intervals for Regression
-----------------------------------

.. raw:: html

    <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
    <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=0_m4ma89cr&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_vt11rp0u" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0" title="Kaltura Player"></iframe>:
    </div>


.. include:: ../chp7/bootstrap_intervals_for_regression.rst


.. |image500| image:: ../chp5/img/media/image1.png
   :width: 4.73105in
   :height: 2.12936in
.. |image501| image:: ../chp5/img/media/image2.png
   :width: 5.88000in
   :height: 2.21941in
.. |image502| image:: ../chp5/img/media/image3.png
   :width: 5.44792in
   :height: 3.50089in
.. |image503| image:: ../chp5/img/media/image4.png
   :width: 5.21875in
   :height: 1.28125in
.. |image504| image:: ../chp5/img/media/image5.png
   :width: 4.79452in
   :height: 1.28425in
.. |image505| image:: ../chp5/img/media/image6.png
   :width: 4.84247in
   :height: 1.14563in
.. |image506| image:: ../chp5/img/media/image7.png
   :width: 3.00685in
   :height: 1.48201in
.. |image507| image:: ../chp5/img/media/image8.png
   :width: 6.24657in
   :height: 4.04893in
.. |image508| image:: ../chp5/img/media/image9.png
   :width: 5.80208in
   :height: 2.16973in
.. |image509| image:: ../chp5/img/media/image10.png
   :width: 4.36476in
   :height: 1.66241in
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
.. |image5018| image:: ../chp5/img/media/image1.png
   :width: 5.21875in
   :height: 2.34886in
.. |image5019| image:: ../chp5/img/media/image12.png
   :width: 4.71875in
   :height: 1.79193in
.. |image5020| image:: ../chp5/img/media/image27.png
   :width: 4.91667in
   :height: 1.90355in
.. |image5021| image:: ../chp5/img/media/image28.png
   :width: 3.71875in
   :height: 1.67385in
.. |image5022| image:: ../chp5/img/media/image29.png
   :width: 2.20833in
   :height: 3.03125in
.. |image5023| image:: ../chp5/img/media/image30.png
   :width: 2.48958in
   :height: 1.96875in
.. |image5024| image:: ../chp5/img/media/image31.png
   :width: 2.83333in
   :height: 2.09375in
.. |image5025| image:: ../chp5/img/media/image32.png
   :width: 5.25343in
   :height: 2.36447in
.. |image5026| image:: ../chp5/img/media/image12.png
   :width: 4.16667in
   :height: 1.58228in
.. |image5027| image:: ../chp5/img/media/image27.png
   :width: 4.27083in
   :height: 1.65351in
.. |image5028| image:: ../chp5/img/media/image33.png
   :width: 2.27083in
   :height: 3.06250in
.. |image5029| image:: ../chp5/img/media/image34.png
   :width: 2.32292in
   :height: 1.26042in
.. |image5030| image:: ../chp5/img/media/image35.png
   :width: 2.86458in
   :height: 2.25000in
.. |image5031| image:: ../chp5/img/media/image36.png
   :width: 4.17708in
   :height: 1.91996in
.. |image5032| image:: ../chp5/img/media/image37.png
   :width: 2.38542in
   :height: 3.09375in
.. |image5033| image:: ../chp5/img/media/image38.png
   :width: 3.27083in
   :height: 1.70121in
.. |image5034| image:: ../chp5/img/media/image40.png
   :width: 1.73958in
   :height: 0.42708in
.. |image5035| image:: ../chp5/img/media/image41.png
   :width: 1.89583in
   :height: 0.65625in
.. |image5036| image:: ../chp5/img/media/image1.png
   :width: 5.21875in
   :height: 2.34886in
.. |image5037| image:: ../chp5/img/media/image1.png
   :width: 5.17123in
   :height: 2.32748in
.. |image5038| image:: ../chp5/img/media/image44.png
   :width: 4.48958in
   :height: 1.79167in
.. |image5039| image:: ../chp5/img/media/t_statistic.png
   :width: 5.18in
   :height: 0.69in
.. |image510| image:: img/histogram_normal_curve.png
   :width: 5.02in
   :height: 3.47in
.. |image511| image:: img/normal_data.png
   :width: 3.40in
   :height: 5.11in
.. |image512| image:: img/non_normal_data.png
   :width: 3.38in
   :height: 5.20in
.. |image513| image:: img/chi_square.png
   :width: 6.96in
   :height: 6.12in
.. .. |image514| image:: img/CI_in_JMP_sm.gif
.. |image514| image:: img/CI_in_JMP.gif
   :width: 6.36in
   :height: 3.21in
.. |image515| image:: img/t_quantile.gif
   :width: 7.23in
   :height: 4.41in
.. |image516| image:: img/normal_quantile_plot.gif
   :width: 7.23in
   :height: 4.41in
.. |image517| image:: img/picking_correct_procedure.png
   :width: 8.64in
   :height: 6.01in
.. |image3007| image:: ../IntroToCI/img/pretend_population.png
   :width: 6.92in
   :height: 2.90in
.. |image3008| image:: ../IntroToCI/img/bootstrap_distribution.png
   :width: 6.65in
   :height: 3.66in
.. |image3009| image:: ../IntroToCI/img/bootstrap_vs_sampling_distribution.png
   :width: 6.65in
   :height: 3.66in
.. |image30010| image:: img/bootstrap_median.png
   :width: 5.02in
   :height: 3.47in
.. |image7023| image:: ../chp7/img/media/bootstrap_correlation.gif
   :width: 9.58in
   :height: 4.85in
.. |image7024| image:: ../chp7/img/media/interpret_slope.png
   :width: 5.13in
   :height: 2.57in
.. |image7025| image:: ../chp7/img/media/interpret_intercept.png
   :width: 5.42in
   :height: 2.64in
.. |image7026| image:: ../chp7/img/media/image23.png
   :width: 3.32in
   :height: 3.06in
.. |image7022| image:: ../chp7/img/media/image24.png
   :width: 5.72in
   :height: 2.07in
