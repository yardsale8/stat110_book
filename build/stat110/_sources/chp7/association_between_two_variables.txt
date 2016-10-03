Association Between Two Variables
---------------------------------


.. raw:: html

    <div class="embed-responsive embed-responsive-16by9 col-xs-12 text-center">
    <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/812561/sp/81256100/embedIframeJs/uiconf_id/33140371/partner_id/812561?iframeembed=true&playerId=kaltura_player&entry_id=0_e8grwx35&flashvars[mediaProtocol]=rtmp&amp;flashvars[streamerType]=rtmp&amp;flashvars[streamerUrl]=rtmp://www.kaltura.com:1935&amp;flashvars[rtmpFlavors]=1&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;&wid=0_o6byx9c7" width="420" height="336" allowfullscreen webkitallowfullscreen mozAllowFullScreen frameborder="0"></iframe>
    </div>

In this chapter we will be looking to identify any *association* between two
quantitative variables.  Consequently, we will be analyzing *bivariate data*.

.. glossary::

    Association between two variables
       We say that there is an **association between two variables** when we can
       use the value of one variable to improve out prediction of a second
       variable.
    Bivariate data
       **Bivariate data** consists of data that include two measurements on
       each individual.  Note that *bivariate* literally means "two variables."

Scatterplots and Displaying an Association
++++++++++++++++++++++++++++++++++++++++++

Creating a scatterplot is always the first step in determining if two variables
are associated.  A scatterplot is a constructed by plotting a point at each of
the :math:`(x,y)` pairs, where :math:`x` and :math:`y` are the values of the x
and y variables for each individual, respectively.  Here is the scatterplot for
the data from example 7.1, which was created in JMP.

|image7021|

Please answer the following questions while considering this scatterplot.

.. admonition:: Question

   1. Could you use the graph to predict the proportion of nose blackness for a
      lion that was, say, 7 years old?  
   2. How close do you think you could get for a randomly selected 7-year-old
      lion? 
   3. Would the quality of your prediction benefit from knowing the lion's age?
      In what way?


In this case a standard interpretation of this scatterplot would make note of the following.

- We see that there is a *positive association*, as the proportion of nose
  blackness tends to increase as age increases.  

- The basic shape of the cloud of points is *linear*, or described fairly well
  with a line.  

- Finally, we see that most of the points would be fairly close to a line drawn
  through the middle of the points, which indicates that this association is
  fairly strong.  

.. admonition:: Creating a Scatterplot in JMP

    To create a scatterplot in JMP, you need to

    1. Enter the data in a new data table (**File > New > New Data Table**),
       being careful to keep the :math:`(x,y)` pairs on the same row.

    2. Go to **Analyze > Fit Y by X** and drag-and-drop the x and y variables in
       the correct box.

    3. Click **OK** and the scatterplot will be displayed.

In the next section, we will discuss the three components of our standard
interpretation of a scatterplot, the *direction*, *strength*, and *form* of the
association.

Describing an Association Between Variables
+++++++++++++++++++++++++++++++++++++++++++

As always, interpretations in statistics are just as important as calculations or
the construction of graphical displays of data.  When describing a possible
association between two variables, we will focus on the *direction*, *strength*,
and *form* of the association.

.. admonition:: Describing an association between variables

    When describing an association between two variables, we will focus on the
    following attributes of association.

    .. glossary::

         Direction of association
             The **direction** of an association is either *positive* or
             *negative*.

             - A **positive direction** is indicated by a positive or direct
               relationship between the x and y variables, i.e. y increases as x
               increases.
             - A **negative direction** is indicated by a negative or inverse
               relationship between the x and y variables, i.e. y decreases as x
               increases.

         Strength of association
             A **strength of association** is a measure of our ability to predict
             the variable y using the value of the variable x.  

             - A **strong association** is an indication that we can make exact
               guesses at the value of y using the value of x.  

             - A **weak association** is an indication that knowing the value of
               the x variable does not improve our ability to guess the value of
               the y variable.

         Form of the association
             The **form of the association** is a mathematical description of
             the basic shape suggested by the cloud of points.  Examples of
             possible forms might be *linear*, *quadratic*, or *sinusoidal*.  For
             the purposes of this course, we will describe the form in one of two
             ways.

             - A **linear** form is typified by a cloud of points that is fairly
               straight and described well by a line.
             
             - A **non-linear** form consists of a cloud of points that has a
               curved shape.

.. note::

    When describing a scatterplot, we need to be careful to examine the shape of
    the whole cloud of points, as opposed to looking too closely at any of the
    points in isolation or local clusters.  I like to think of this process as
    the **fat marker method** of describing the plot:  If I were to cover the
    cloud of points by drawing a line or curve with a fat marker, what shape
    would I use?  Did I need a curve to cover the points or was a straight line
    sufficient?

.. admonition:: Check your understanding

   |image7026|

   Use the graph shown above to answer each of the following questions.


    .. mchoice:: describe_direction_1
        :answer_a: Positive
        :answer_b: Negative
        :answer_c: No direction
        :correct: a
        :feedback_b: Notice that the heights tend to rise as you scan from left to right.
        :feedback_c: Notice that the heights tend to rise as you scan from left to right.

        Which of the following best describes the direction of the association
        shown above?

    .. mchoice:: describe_strength_1
        :answer_a: Strong
        :answer_b: Moderately strong
        :answer_c: Weak
        :correct: a, b
        :feedback_b: Although most points would be within about 0.05, or 5%, ot the line.  This is bordering on a strong prediction.
        :feedback_c: Notice that most points would be within about 0.05, or 5%, ot the line.  This is bordering on a strong prediction.

        Which of the following best describes the strength of the association?

    .. mchoice:: describe_form_1
        :answer_a: Linear
        :answer_b: Non-linear
        :correct: a
        :feedback_b: There is no need to use a curve here, a line does just as well.

        Which of the following best describes the form of the association?

I find that the strength of the association is the most difficult trait to
describe, especially to someone that is new to statistics.  In the next section,
we will introduce a summary method that will help us determine the strength of a
linear association.
