Assessing the Normality of a Data Set
-------------------------------------
.. raw:: html

    <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
    <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=1_fnm0wj15&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=1_n9aapek4" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen frameborder="0" title="Kaltura Player"></iframe> 
    </div>


The application of the central limit theorem (CLT) for means highlights the need for
determining if a given data set is "normal."  In particular, we need to be
careful about the application of the CLT to a small data set and *a
normal quantile plot* will give us the needed tool.

A first attempt at trying to determine that a data set is normal might involve
drawing a normal curve over a dot plot or histogram.  Unfortunately, it is
difficult to determine how close a given histogram is to the curve.

|image510|

A better solution is to use a normal quantile plot.  These plots are
designed to provide a simple distinction between data that is fairly normal and
data that is not.

Creating a Normal Quantile Plot in JMP
++++++++++++++++++++++++++++++++++++++

The following GIF illustrates the process for constructing a normal quantile
plot in JMP.

|image516|

.. admonition:: Reading a Normal Quantile Plot

    **Normal data is straight** 
    
    A quantile plot with points that are close to a straight line indicate data
    that is fairly normal.  
    
    **Non-normal data is curved** 
    
    The presence of curvature in a quantile plot is an indication of the
    presence of tails that are longer or shorter than expected for data that
    comes from the normal distribution.

+------------+------------+
| |image511| | |image512| |
+------------+------------+

As a consequence of the random nature of data, we need to allow for some
flexibility in our interpretations of such graphs.  Notice that each probability
plot shown above includes curved confidence bands.  These bands aid by giving
us a visual cue about how picky we should be when determining the normality of a
plot, only claiming *the data is clearly non-normal* when at least 5% of the
points fall outside the bands.

.. mchoice:: assess_normal_1
    :answer_a: points with obvious curvature with a number of points outside the confidence bands.
    :answer_b: points that roughly form a straight line with almost all points falling inside the confidence bands.
    :correct: a

    A quantile plot of data that is clearly not from a normal distribution is characterized by ...

.. mchoice:: assess_normal_2
    :answer_a: points with obvious curvature with a number of points outside the confidence bands.
    :answer_b: points that roughly form a straight line with almost all points falling inside the confidence bands.
    :correct: b

    A quantile plot of data that is from a distribution that is approximately normal is characterized by ...

