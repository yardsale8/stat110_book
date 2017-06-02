 .. raw:: html
 
     <script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

Bootstrap Confidence Intervals
------------------------------

Our current method for finding a confidence interval involves the following
steps:

1. Simulate the sampling distribution of the mean by taking many samples from
   the population.
2. Compute the standard error, i.e. the standard deviation of the statistics 
   in the simulated distribution. 
3. Add and subtract 2 times this value to get a 95% confidence interval.

Unfortunately, there is a big problem with this approach.

.. caution:: 

    **Problem with the Current Approach**

    We need to know the whole population to produce the standard error.  This
    approach is very impractical, as taking a census is either very expensive
    and many times impossible.

Our solution will be to use a bootstrap sample, which is acquired by sampling the
sample.

Bootstrap Samples
+++++++++++++++++


.. raw:: html

    <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
    <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=0_nesk0z7b&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_nturh0wf" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen frameborder="0"></iframe>
    </div>

Since we can't be expected to have the entire population at our disposal, we
will use the best tool at our disposal: the sample.  Instead of taking many
samples from the population to simulate the sampling distribution, we will take
many *bootstrap samples* from the sample, allowing us to simulate the
*bootstrap distribution*.

.. glossary::
    Bootstrap Samples
        A **bootstrap sample** is a sample of the sample that uses

        1. Sampling with replacement.
        2. The same sample size as the original sample.
    Bootstrap Statistic
        A **bootstrap statistic**  is a statistic taken from a bootstrap
        sample.  
    Bootstrap Distribution
        The **bootstrap distribution** is the distribution of many, many
        bootstrap statistics.
    Bootstrap Standard Error
        The **bootstrap standard error** is the standard deviation of bootstrap
        distribution, which can be used as an estimate of the actual standard
        error of a statistic.

Using sampling with replacement allows for some variability from one bootstrap
sample to the next, as some values will be selected more than once and other
values will be left out of the sample.  It turns out that the variability between
bootstrap statistics is very similar to the variability between the actual
statistics in the sampling distribution.

Another way to understand bootstrap samples is to imagine that we are sampling
from a population where we have *huge* stacks of copies of each item in the
sample.  In effect we are using the best approximation for the population that
we have available.

|image3007|

In the next image, we illustrate the process of constructing the bootstrap
distribution using the `StatKey's Confidence Intervals for a Mean page
<http://www.lock5stat.com/StatKey/bootstrap_1_quant/bootstrap_1_quant.html>`_.
The bootstrap distribution is constructed by repeating steps 1-3 many times.

|image3008|

Finally, we will compare and contrast the sampling distribution and the 
bootstrap distribution.  The two distributions tend to have the same shape and
spread, but different centers.  In particular, the sampling distribution is
centered at the population mean and the bootstrap distribution is centered at
the original sample mean.

|image3009|

.. mchoice:: mc_bootstrap_1
    :answer_a: a sample of the sample.
    :answer_b: a statistic from a sample of a sample.
    :answer_c: a collection of statistics from a sample of a sample.
    :answer_d: the standard deviation of statistics from a sample of a sample.
    :correct: a
    
    The bootstrap sample is ...

.. mchoice:: mc_bootstrap_2
    :answer_a: a sample of the sample.
    :answer_b: a statistic from a sample of a sample.
    :answer_c: a collection of statistics from a sample of a sample.
    :answer_d: the standard deviation of statistics from a sample of a sample.
    :correct: b
    
    The bootstrap statistic is ...

.. mchoice:: mc_bootstrap_3
    :answer_a: a sample of the sample.
    :answer_b: a statistic from a sample of a sample.
    :answer_c: a collection of statistics from a sample of a sample.
    :answer_d: the standard deviation of statistics from a sample of a sample.
    :correct: c
    
    The bootstrap distribution is ...

.. mchoice:: mc_bootstrap_4
    :answer_a: a sample of the sample.
    :answer_b: a statistic from a sample of a sample.
    :answer_c: a collection of statistics from a sample of a sample.
    :answer_d: the standard deviation of statistics from a sample of a sample.
    :correct: d
    
    The bootstrap standard error is ...

Constructing Bootstrap Confidence Intervals
+++++++++++++++++++++++++++++++++++++++++++

Now we have two choices for making a confidence interval using the bootstrap
distribution.

1. Use the bootstrap standard error to construct a 95% confidence interval by
   adding and subtracting a margin of error of :math:`2SE`.  
2. Use the limits of the middle 95% of the bootstrap statistics as the
   boundaries for our 95% confidence interval.

The advantage of the second approach is that we can quickly and easily change
the level of confidence of the interval by changing the middle percentage.  For
example, if we want a 99% confidence interval, we will highlight the middle 99%
of the bootstrap statistics and use the lower and upper bounds of this
collection for our confidence interval.

On the other hand, if we wanted to construct a confidence interval using the
bootstrap standard error for a confidence level that is different than 95%, we
would need to figure out how many standard errors to use for the margin of
error.  There is a theoretical solution to this problem, which we will highlight
in the next section.




..  TODO:: Add an example from the statkey website.

 Bootstrap Confidence Intervals for Other Parameters
 ---------------------------------------------------
 
 .. raw:: html
 
     <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
     <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=0_zqujc0rn&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_zwrperag" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen frameborder="0"></iframe>
     </div>
 
 We can use these bootstrap techniques to find confidence intervals for other
 confidence levels and other parameters
 
 .. admonition:: Other Confidence Levels
 
     Change the middle percent from 95% to the desired confidence level, which
     will result in intervals that work (roughly) for that percent of samples.
     For example, setting the middle percent to 99% will result in intervals that
     work for approximately 99% of samples.
 
 .. admonition:: Other Parameters
 
     To construct confidence intervals for other parameters, use the bootstrap
     technique, collecting the corresponding statistic from each bootstrap
     sample.  For example, to construct a confidence interval for the population
     standard deviation we would generate 1000 bootstrap samples and collect the
     sample standard deviation from each.
 
 .. note::
 
     The StatKey website allows you to construct confidence intervals for the
     median and the standard deviation by changing *mean* to the desired
     parameter in the drop down box, as shown below.
 
 Below we see a 95% confidence interval for the population median price of a used
 Mustang.  This was constructed by taking 1000 bootstrap samples from the
 original sample and collecting the median of each of these bootstrap samples.
 The 95% confidence interval consists of the cut-offs for the middle 95% of all
 bootstrap sample medians.
 
 |image30010|


