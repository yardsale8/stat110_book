
For paired data, we subtract each pair, then compute the mean of these
differences. Consequently, the hypotheses for paired data will revolve around
the population mean of the differences between all pairs, which is denoted
`\mu_{diff}`.

Paired Versus Unpaired Data
---------------------------

.. raw:: html

    <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
    <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=1_hhkpj6mf&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_rizfu6pg" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0" title="Kaltura Player"></iframe>
    </div>

.. **
    
In this chapter, we will be comparing groups using two different types of data,
*paired* or *unpaired*.  Data is **paired** if we can pair each measurement of
one variable with exactly one measurement of the other.  Typical designs that
result in paired data are before-and-after studies, where measurements are taken
before a treatment and then again after the treatment.  Another example of a
design that results in paired data is pairing similar individuals, say siblings
or identical twins, and applying a different treatment to each member of the
pair.

Data is **ungrouped** when there is no way to pair specific measurements from
each group. Ungrouped data is most commonly acquired through randomization, be
it either two different random samples or randomly assigned treatments.

Finding the Null and Alternative Hypotheses
+++++++++++++++++++++++++++++++++++++++++++


.. raw:: html

    <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
    <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=1_kon9dgjs&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_x5z6q0dc" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0" title="Kaltura Player"></iframe>
    </div>

.. **



When running hypothesis test to compare to groups, it is natural to set the null
hypothesis to represent *no difference*.  As our statistic, the mean, is
quantitative, "no difference" means (a) we subtracted two values (in some way) and (b) the
result was 0.  The difference between paired and unpaired data comes in *how* we
subtract.

For paired data, we subtract each pair, then compute the mean of these
differences. Consequently, the hypotheses for paired data will revolve around
the population mean of the differences between all pairs, which is denoted

.. math::

    \mu_{diff}.

On the other hand, for unpaired data first compute the mean of each group, the
we subtract these means. In this case, the hypotheses will revolve around the
difference population mean of the differences between all pairs, which is denoted

.. math::

    \mu_{1} - \mu_{2},


where the subscripts (1 and 2) represent the group number and can be replaced
with the name of the group.  For example, if we were comparing a treatment group
to a control group, we might use

.. math::

    \mu_{treatment} - \mu_{control}.

When determining the alternative hypothesis, it is important to consider the
research question **and** the direction of subtraction.  Suppose that we have
the following research question.

.. admonition:: Research question:

    Is there evidence that the treatment resulted in values that were smaller
    than the control group?

Since we computed *treatment - control*, smaller numbers for the treatment would
result in negative numbers (i.e.  *small - large* would be negative).
Consequently, the hypotheses would be given by

.. math::

    H_0: \mu_{treatment} - \mu_{control} = 0 \\
    H_a: \mu_{treatment} - \mu_{control} < 0

Now suppose you have a classmate that chose to compute

.. math::

    \mu_{control} - \mu_{treatment}.

In this case, the research question would result in positive values (i.e.  *large
- small* would be positive) and the hypotheses become 

.. math::

    H_0: \mu_{control} - \mu_{treatment} = 0 \\
    H_a: \mu_{control} - \mu_{treatment} < 0

This same logic applies to the paired test as well.

.. note::

    Always consider the research question AND the direction of subtraction when
    determining the hypotheses when comparing two groups.


Getting Started with Paired Data
--------------------------------

The hypothesis testing procedures presented in this section should be
used when the observations are paired and the two groups being compared are
*dependent*. Whether or not the observations are paired/dependent is determined
by how the data are collected. To see this, consider the following
example.

Example 6.1: Thanksgiving Holiday Weight Gain
+++++++++++++++++++++++++++++++++++++++++++++

In a 2006 study published in *Nutrition Journal*, researchers were
interested in assessing potential changes that occur in body weight
during the Thanksgiving holiday break in college students. This
paper’s abstract indicates that “a total of 94 college students
reported to the human body composition laboratory at the University of
Oklahoma following a 6-hour fast with testing occurring prior to, and
immediately following the Thanksgiving holiday break. Body weight was
assessed using a balance beam scale while participants were dressed in
minimal clothing.”

.. admonition:: Source: 

    Hull et al. The Effects of the Thanksgiving Holiday on Weight Gain. Nutrition Journal 2006, **5**:29; doi:10.1186/1475-2891-5-29.

.. admonition:: Research Question: 

    On average, does body weight of college students increase over the Thanksgiving holiday break?

.. admonition:: Questions:

    1. What is the response variable of interest?

    2. What is the predictor variable of interest?

The raw data from this study were not available; however, the data in
the file **ThanksgivingWeightData.jmp** are similar to the actual
results obtained by the researchers. A portion of these data is shown
below:

|image600|

.. admonition:: Questions:

    1. What can be said about the weight of Subject #1 as compared to
       Subject #7, for example, regardless of whether the data were
       collected before or after Thanksgiving?

.. note::

    For these data, the first pre-weight is related to the first
    post-weight (the two measurements were made on the same person). Thus,
    these two samples are **dependent**.

In other words, some of the variability in the responses might be due to
differences between time periods (before vs. after), but much of the variability
in the observations is likely due to differences between people! So, to control
for this variability in weights from person to person (which will help us
isolate the effect of Thanksgiving break), we will work with the *DIFFERENCES*
on each subject, instead. This will remove the structure of dependence between
the pre- and post-Thanksgiving groups and will control for the fact that some
people, in general, tend to weigh more (or less) than others. In the end, this
helps us to isolate the effect of Thanksgiving break (i.e., before vs.  after).
