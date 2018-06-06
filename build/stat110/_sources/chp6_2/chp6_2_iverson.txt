Using the Bootstrap to Comparing Two Unpaired Groups
----------------------------------------------------

In Chapter 5, we considered inference for a single population mean.  Then, in
the first part of Chapter 6 we extended these ideas so that comparisons could be
made between two groups. Such comparisons were made using differences because
the observations in the two groups were related, or *dependent*.

In this section, we will consider making comparisons between two groups when the
observations in one group are *independent* of the observations in the other
group. The methodologies considered here are a bit more involved because it no
longer makes sense to simply work with differences. Consider the following
example.

Bootstrap Confidence Intervals for Unpaired Data
++++++++++++++++++++++++++++++++++++++++++++++++

Again, we will start by applying the bootstrap to get a confidence interval and
use the resulting interval to draw conclusions about the research questions.
The key to applying the bootstrap to unpaired groups is taking two bootstrap
samples, one for each group.  This is discussed in the following video.


.. raw:: html

    <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
        <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=1_t861e0ee&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_qz5l0hn3" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0" title="Kaltura Player"></iframe>
    </div>

.. include:: ../chp6_2/example6.5.rst

.. TODO Add a section on bootstrap intervals for two samples.

.. include:: ../chp6_iverson/bootstrap_two_independent_means.rst

.. include:: ../chp6_2/sampling_distribution_difference_means.rst

.. include:: ../chp6_2/test_a_difference.rst

.. include:: ../chp6_2/confidence_interval_difference_means.rst

.. include:: ../chp6_2/example6.6.rst

.. include:: ../chp6_2/example6.7.rst

.. .. include:: ../chp6_2/non_parametric_tests.rst

.. .. include:: ../chp6_2/pooled_test.rst
.. 
.. .. include:: ../chp6_1/images.rst
