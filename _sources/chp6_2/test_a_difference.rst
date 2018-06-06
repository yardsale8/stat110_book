
Testing for a Difference in Between Two Unpaired Groups
-------------------------------------------------------


.. raw:: html

    <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
        <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=1_omhtbwvj&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_ufgc0n1c" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0" title="Kaltura Player"></iframe>
    </div>

.. **

**Back to Example 6.5:** Carry out the hypothesis test associated with
the following research question: Is the average birth weight lower when
mothers are classified as smokers?

**Step 0:** Check the assumptions behind the test to be sure that the t-test is valid.

1. Are the two groups independent? Explain.

2. Are both sample sizes sufficiently large? If not, is it reasonable to assume that both populations are normally distributed?

|image616|

**Step 1:** Convert the research question into H\ :sub:`0` and H\ :sub:`a`.

H\ :sub:`0`:

H\ :sub:`a`:

**Step 2:** Calculate the *test statistic* from your data.

To do this in JMP, click on the red drop-down arrow next to "One-way Analysis..."
and select **t-test**.

|image6124|

JMP returns the following:

|image6110|

Verify the value of the test statistic in JMP:


|image618|

.. math::

    SE_{\bar{x}_1-\bar{x}_2} = \sqrt{\frac{s_1^2}{n_1}+ \frac{s_2^2}{n_2}}\\
    t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{SE_{\bar{x}_1-\bar{x}_2}}


**Step 3:** Determine the *p-value*.

|image619|

*p-value*:

**Step 4:** Write a conclusion in terms of the original research question.

    "We have evidence that the average birth weight is lower when mothers are classified as smokers (p-value = .0038)."

