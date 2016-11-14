
Calculating the Difference in JMP
---------------------------------

First, open the file called **ThanksgivingWeightData.**. To calculate
the difference, create an additional column (double click on empty
column next to “‘Post Weight”) and title it “Difference.” Right-click
on the new column header and select **Formula**.

|image601|

In the edit window, tell JMP to calculate the difference as follows:

|image602|

Click **Apply** and then **OK**, and JMP returns the following (only the
results for the first 10 subjects are shown below):

|image603|

.. admonition:: Questions:

    1. What does a positive difference of 3.9 indicate?

    2. What does a difference of -1.9 indicate?

To determine what the average difference is, we can analyze the
distribution of the differences using the descriptive methods
discussed in Chapter 4:

|image604|

.. admonition:: Questions:

    3. What is the average difference of the 94 subjects? Interpret this
       value.

    4. If Thanksgiving break had no effect on body weight, what would you
       expect these differences to be, on average?

    5. If the research hypothesis is correct (body weights of college
       students increase over Thanksgiving break), what would you expect
       these differences to be, on average?

.. note::

    Note that these differences are represented by a single column
    of data. *So, instead of viewing this as a problem involving a
    categorical predictor and a numerical response, you could view this as a
    problem involving a single numerical variable – the differences!*
    Therefore, the hypothesis testing procedure is *exactly* the same as the
    procedure for testing a single population mean we discussed in Chapter
    5.

That is, the parameter of interest is the true population average of the
differences which we will represent by :math:`\mu_{difference}`.

-  Our best estimate for this parameter is the *sample mean* of the
   observed differences. We’ll call this quantity :math:`\bar{x}_{difference}`.

-  The sample standard deviation of the differences will be denoted by
   :math:`s_{difference}`
