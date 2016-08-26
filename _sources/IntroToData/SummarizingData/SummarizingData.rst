Summarizing Data
================

In this chapter, we will present some basic methods for summarizing a
distribution, both numerically and graphically.

Graphing Distributions - Dotplots and Histograms
------------------------------------------------

.. raw:: html

   <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=0_6ynkx72e&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_f75efnqr" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen frameborder="0"></iframe> 

Shapes of a Distribution
++++++++++++++++++++++++

One of the important features of a distribution is the shape of the
distribution.  In this class, we will describe the shape of the distribution in
words using terms like *symmetric*, *skewed left*, *skewed right*, and
*bimodal*.

.. glossary::
    Symmetric
        A distribution is described as *symmetric* if portion of the graph to
        the left of the mean/average is approximately a *mirror image* of the
        portion of the graph to the right side of the mean/average.

|image0|

We will distinguish between symmetric graphs that are *bell-shaped* or *not
bell-shaped*.

On the other hand, when a distribution is **not** symmetric, we focus on the
*tails* of the distribution.

.. glossary::
    Skewed Left
        A distribution is *skewed left* when it has a long left tail, that is
        its left tail is much longer than its right tail.
    Skewed Right
        A distribution is *skewed right* when it has a long left tail, that is
        its right tail is much longer than its left tail.
|image1|

Finally, it is possible that we might have a graph with two peaks.

.. glossary::
    Bimodal
        A distribution is *bimodal* if it has two distinct peaks.  (The term
        bimodal literally means *two modes*, where a mode is a peak.)

|image2|

.. mchoice:: mc_shape_1 
    :answer_a: Symmetric
    :answer_b: Skewed left
    :answer_c: Skewed right
    :correct: a 
    :feedback_a: A symmetric graph has two tails that are about the same.
    :feedback_b: A skewed left graph has a longer left tail.
    :feedback_c: A skewed right graph has a longer right tail.

    A distribution with two similar tails is ...

.. mchoice:: mc_shape_2 
    :answer_a: Symmetric
    :answer_b: Skewed left
    :answer_c: Skewed right
    :correct: b 
    :feedback_a: A symmetric graph has two tails that are about the same.
    :feedback_b: A skewed left graph has a longer left tail.
    :feedback_c: A skewed right graph has a longer right tail.

    A distribution with long left tail is ...

.. mchoice:: mc_shape_3 
    :answer_a: Symmetric
    :answer_b: Skewed left
    :answer_c: Skewed right
    :correct: c 
    :feedback_a: A symmetric graph has two tails that are about the same.
    :feedback_b: A skewed left graph has a longer left tail.
    :feedback_c: A skewed right graph has a longer right tail.

    A distribution with long right tail is ...

Measures of Center - Finding a Typical Value
--------------------------------------------

.. raw:: html

    <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=0_z1rwp030&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_o0p0im2f" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen frameborder="0"></iframe>

.. glossary::
    Mean or Average
        This is the (arithmetic) average of the data.  It is caluculated by
        all the values of the variable and dividing by the number of
        individuals.
    Median
        A value that splits the data into groups that consist of approximately
        half of the data.  It is computed by (1) Putting the data in order and
        (2) Finding the middle value.  If the data set has an even number of
        values, the average of the middle two values is used for the median.

While being able to compute the value of a summary statistic is important, *it
is even more important to understand what each number tells us about the
distribution.  Here are the standard interpretations for these statistics.

.. admonition:: Standard Interpretation of the Mean

    The mean is the balance point or center of mass of the distribution, that
    is, it is the location at which the dot plot would balance on your finger.

.. admonition:: Standard Interpretation of the Median

    The median splits the data in half.  Approximately 50% of the data will be
    above and below the median. (The only situation where this is not exactly 50%
    is when there are multiple values stacked at the median.)

.. mchoice:: mc_mean
    :answer_a: 252.0
    :answer_b: 283.0
    :answer_c: 293.8
    :correct: c
    :feedback_a: You need to add up all the values and divide by the number of individuals.
    :feedback_b: You need to add up all the values and divide by the number of individuals.

    The following values are the serum cholesterol levels (mg/dLi) of six men with
    high cholesterol.  
   
    366 327 230 274 292 274
    
    Compute the **mean** of these data.

.. mchoice:: mc_median
    :answer_a: 252.0
    :answer_b: 283.0
    :answer_c: 293.8
    :correct: b
    :feedback_a: Make sure you reorder the data, *then* find the middle value.
    :feedback_c: Sort the data and find the middle value.

    The following values are the serum cholesterol levels (mg/dLi) of six men with
    high cholesterol.  
   
    366 327 230 274 292 274
    
    Compute the **median** of these data.


Unsual Values and the p-Value
-----------------------------

.. raw:: html

    <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=0_b91c7frv&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_0ep0lw91" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen frameborder="0"></iframe>

Reading Goes Here

Measures of Spread - Finding the Amount of Concentration or Spread
------------------------------------------------------------------

Video Goes Here

Reading Goes Here


.. |image0| image:: img/symmetric.png
   :width: 2.51873in
   :height: 3.30189in
.. |image1| image:: img/skewed_left_right.png
   :width: 2.51873in
   :height: 3.30189in
.. |image2| image:: img/bimodal.png
   :width: 2.51876in
   :height: 1.30189in
