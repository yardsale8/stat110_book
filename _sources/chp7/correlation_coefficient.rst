
Pearson Correlation Coefficient
-------------------------------

The Pearson correlation coefficient (denoted by *r*) is used to describe
and measure the relationship between two numerical variables. It is
appropriate to use when the following are true:

-  The relationship between the two variables is a LINEAR relationship

-  Both variables are measured on interval or ratio scales

.. admonition:: Formula for the Correlation Coefficient

    The formula for the Pearson product-moment correlation coefficient is given
    below:

    .. math::
        
         r = \frac{\sum_{i=1}^n \left( x_i - \bar{x}\right)\left( y_i - \bar{y}\right)}{s_x s_y(n-1)}

.. admonition:: Calculating Correlation in JMP

    We can also use JMP to directly calculate the Pearson correlation
    coefficient. Select **Analyze > Multivariate Methods > Multivariate**.

|image704|

Place both variables in the Y, columns box, and JMP returns the
following:
|image705|
|image706|

.. admonition:: Interpreting the Pearson Correlation Coefficient

    1. A positive correlation coefficient indicates a positive association between the two numerical variables, and negative correlation indicates a negative association.

    2. The correlation coefficient is always between -1 and 1 (-1 ≤ *r* ≤ 1).

       -  Values near zero indicate a very weak relationship exists.
       -  Values close to 1 indicate a very strong positive relationship exists.
       -  Values close to -1 indicate a very strong negative relationship exists.

.. admonition:: Questions

    1. What does this correlation coefficient say about the direction of the
       relationship between a lion’s age and its proportion of nose
       blackness?

    2. What does this correlation coefficient say about the strength of the
       relationship between a lion’s age and its proportion of nose
       blackness?

.. caution:: 

    You should never use a correlation coefficient without also looking
    at a scatterplot of the data. Why? Consider the data in the file
    **Anscombe\_Example.JMP**.

|image707|

To avoid misinterpreting a correlation, always accompany the correlation
coefficient with a scatterplot of the data and make sure the assumptions
behind the Pearson product-moment correlation are met!
