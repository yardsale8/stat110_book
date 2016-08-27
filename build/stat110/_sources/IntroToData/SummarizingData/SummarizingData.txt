.. role:: math(raw)
   :format: html latex

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

We will spend a considerable amount of time in this course trying to decide if a
value is unusually large or unusually small.  For example, if we were trying to determine if the
hiring practices in a school disctrict are discriminatory, we will need to
determine if the school hires an unusually low number of African-American
teachers.

Before we can determine if a value is unusual, we need a good definition of what it
means to be unusually large or unusually small in a statistical sense.

.. glossary::

    Unusually large values
        A value is considered unusually large if it is in the largest 5% of the
        distribution.
    Unsuaually small values
        A value is considered unusually small if it is in the smallest 5% of the
        distribution.

.. note::

     There is nothing special about picking 5%, and in fact later in the course
     we will see that adjusting this value gives us some control over a certain
     type of error. For now, we will stick to 5% and call this **the 5% rule**.

|image3|

Now that we know what it means to be unusually large or small, we
need a method of determining if a specific value of interest is unusually large.  
For example, I have a friend that is 78 inches tall (6' 6").  I know that he is
fairly tall, but is he unusually tall, in the staistical sense?

When answering this question intuitively, I believe that it is natural to
compare my friend to other tall people, asking *What
percentage of the time do I meet men that is 78 inches tall or taller*.  This
is the exact intuition that leads to our definition of an *upper p-value*.  

On the other side of the coin (or in this case distribution), we might ask if
someone that is 63.5 inches tall, like my wife, is unusually short. Again in 
a statistical sense.  This time it is natural to compare someone on the small side of
the distribution with other small values, leading to what I like to call a
*lower p-value*.

.. glossary::
    Upper p-value
        The upper p-value of a given value :math:`x` is the proportion of the 
        distribution that is at or above the value.  This measurement is useful
        in determining if a value is unusually large.
    Lower p-value
        The lower p-value of a given value :math:`x` is the proportion of the 
        distribution that is at or below the value. This measurement is useful
        in determining if a value is unusually large.

Example: Using a lower p-value to determine if 4 is unusually small.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Consider the distribution shown below.  There are 117 dots on the graph, and we
want to answer the question *Is the value 4 unusually small*.  Because we are
focusing on small values, we will use a *lower p-value*, because it makes sense
to compare a potentially small value to other small values.  There are 7 dots
that are at or below 4, so the lower p-value of 4 rounds up to 0.06 or 6%. Since 
there is more than 5% of the distribution below 4, **4 is not in the smallest 5%
of the distribution** and therefore is not unusually small.

|image4|

Thus, a value is only unusually small if its lower p-value is smaller than 5%
(when using the 5% rule).  The same is true for an upper p-value.  


Example: Using a upper p-value to determine if 12 is unusually large.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This time, consider the question *Is 12 unusually large?*  In this case the 
upper p-value is a little less that 1%.  Since less than 5% of the distribution 
is above 12, we see that

    1. 12 is in the largest 1%, and
    2. 12 is unusually large, according to the 5% rule.

|image5|

.. mchoice:: mc_pvalues_1
    :answer_a: lower p-value.
    :answer_b: upper p-value.
    :correct: a
    :feedback_a: When looking at a potentially small value, compare it to other small values.
    :feedback_b: Focus on the smallest part of the distribution, i.e. the left tail.

    When deciding if a value is unusually small, use a ...


.. mchoice:: mc_pvalues_2
    :answer_a: lower p-value.
    :answer_b: upper p-value.
    :correct: b
    :feedback_a: Focus on the largest part of the distribution, i.e. the right tail.
    :feedback_b: When looking at a potentially large value, compare it to other large values.

    When deciding if a value is unusually large, use a ...

.. mchoice:: mc_pvalues_3 
    :answer_a: Yes
    :answer_b: No
    :correct: a
    :feedback_a: If the lower p-value is smaller that 5%, the value is in the smallest 5% and thus unusually smallest.
    :feedback_b: Consider the fact that the value has only 2.3% of the distribution below it.  Is it in the smallest 5% of the distribution?

    Suppose that a value has an lower p-value of 2.3%.  According to the 5% rule, is this value unusually small?

.. mchoice:: mc_pvalues_4 
    :answer_a: Yes
    :answer_b: No
    :correct: b
    :feedback_a: Consider the fact that the value more than 12.7% of the distribution above it.  Is it in the largest 5% of the distribution?
    :feedback_b: If the upper p-value is larger that 5%, the value is NOT in the largest 5% and thus NOT unusually large.

    Suppose that a value has an upper p-value of 12.7%.  According to the 5% rule, is this value unusually large?

.. admonition:: General P-value Rule

    A value is unusually small when the lower p-value is less than 5% (when
    using the 5% rule). 

    A value is unusually large when the upper p-value is less than 5% (when
    using the 5% rule).

    **In both cases, small p-values mean unusual values**.

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
.. |image3| image:: img/unusual_values.png
   :width: 5.51876in
   :height: 2.30189in
.. |image4| image:: img/lower_pvalue.png
   :width: 4.51876in
   :height: 4.30189in
.. |image5| image:: img/upper_pvalue.png
   :width: 3.51876in
   :height: 4.30189in
