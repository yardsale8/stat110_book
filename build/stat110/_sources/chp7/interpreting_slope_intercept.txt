Interpreting Slope and the :math:`y`-intercept
----------------------------------------------

To write out an interpretation for the slope and :math:`y`-intercept, we start
with the standard interpretations that are taught in mathematics.  Recall that
the slope is the amount of change in :math:`y` when adding one unit to
:math:`x`.  Since the relationships in regression are rarely perfect, but
instead describe a general tendency, we change this interpretation as follows.

.. admonition:: The standard interpretation of the slope of a regression line

    The slope of the regression line is the *average* amount of change in
    :math:`y` when adding one unit to :math:`x`.

It is, as always, important to add the context to our interpretations and the
following figure shows a basic template for writing about the slope, along with
an example.

|image7024|

The :math:`y`-intercept is the value of the :math:`y` variable when :math:`x` is
zero.  Adjusting to the inexact nature of regression, we get the following
interpretation of the :math:`y`-intercept.

.. admonition:: The standard interpretation of the :math:`y`-intercept of a regression line

    The :math:`y`-intercept of the regression line  is the *average* value of 
    :math:`y` when the :math:`x` variable is zero.

The following figure contains a template for and example of adding context to
our interpretation.

|image7025|

We need to be careful to only apply these interpretations when they are viable.
In the case of the slope, it is important that the association is fairly linear.
Non-linear associations will have a variable rate of change, and assigning a
fixed amount of change in :math:`y` for a given value of :math:`x` would be
misleading.

In terms of the :math:`y`-intercept, we need to assure that an :math:`x` value
of zero is meaningful.  If :math:`x` represents *the profit of a business*, a
value of zero is meaningful as it is definitely conceivable for a business to
have a profit of zero. On the other hand, if the :math:`x` values represent the
heights of people, then an :math:`x` value of zero is nonsensical: A height of
zero is inconceivable.

Another consideration when applying these interpretations is the scope of the
data.  We have no idea what is happening outside our data window and it would be
a mistake to assume that the pattern that we see will continue past the largest
and/or smallest data values.  For example, the slope might start to change if we
push past our maximum y-value.  Similarly, if we do not have any data with
:math:`x` values around zero, we should not interpret the value of the
intercept.

To summarize, use the following advise before interpreting the slope or
intercept.

.. admonition:: Interpreting the slope of the regression line is viable when ...

    1. the :math:`x` value is between the minimum and maximum values of :math:`x`
    2. the association is fairly linear.

.. admonition:: Interpreting the :math:`y`-intercept is viable when ...

    1. there is data with :math:`x` values around zero.
    2. a :math:`x` value of zero is meaningful.
