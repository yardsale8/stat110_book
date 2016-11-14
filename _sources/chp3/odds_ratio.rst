
Calculating Odds and the Odds Ratio
-----------------------------------

Another quantity that is often used to describe differences in
categorical outcomes between groups is the *odds ratio*. This ratio is
used more commonly in practice than the relative risk ratio; however, it
is more difficult to interpret and is sometimes harder to understand.

Before computing an odds ratio, we first need to compute the *odds* for
both groups:

.. glossary::

    Odds 
        Consider our Adoption and Suicide Attempt example. For each
        group (Adopted and Not Adopted), the **odds** of attempting suicide is
        computed as the number of subjects in that group that attempted suicide
        divided by the number in that group that did not attempt suicide.

Recall the contingency table for this example.

+---------------+-------------------+----------------------+---------+
|               | Suicide Attempt   | No Suicide Attempt   | Total   |
+===============+===================+======================+=========+
| Adopted       | 47                | 645                  | 692     |
+---------------+-------------------+----------------------+---------+
| Not adopted   | 9                 | 531                  | 540     |
+---------------+-------------------+----------------------+---------+


Find the odds of attempting suicide for both groups:

-  Odds of Attempting Suicide in the Adopted Group:

.. math::

   \frac{\mathrm{Number\,that\,attempted\,Suicide\,in\,the\,Adopted\,Group}}
        {\mathrm{Number\,that\,DID\,NOT\,attempted\,Suicide\,in\,the\,Adopted\,Group}}=

-  Odds of Attempting Suicide in the Non-adopted Group:

.. math::

   \frac{\mathrm{Number\,that\,attempted\,Suicide\,in\,the\,Nonadopted\,Group}}
        {\mathrm{Number\,that\,DID\,NOT\,attempted\,Suicide\,in\,the\,Nonadopted\,Group}}=

The **odds ratio** is then simply the ratio of the odds for the two
groups:

.. math::

   \mathrm{Odds\,Ratio} = \frac{\mathrm{Odds\,of\,attempting\,Suicide\,in\,the\,Adopted\,Group}}
        {\mathrm{Odds\,of\,attempting\,Suicide\,in\,the\,Nonadopted\,Group}}

We interpret this quantity by saying that in this study, the odds of
attempting suicide were about \_\_\_\_\_\_\_\_ times as high for adopted
children as for non-adopted children.

We could also have calculated the odds ratio as follows:

.. math::

   \mathrm{Odds\,Ratio} = \frac
        {\mathrm{Odds\,of\,attempting\,Suicide\,in\,the\,Nonadopted\,Group}}
        {\mathrm{Odds\,of\,attempting\,Suicide\,in\,the\,Adopted\,Group}}

How would we interpret this value?

.. admonition:: Comments:

    1. An odds ratio of 1.0 implies that there is no observable difference
       between the two odds. This is always the reference value!

    2. Odds ratios are often used in health care experiments when we want to
       determine how much more likely a subject is to develop a disease
       when they have some risk factor as opposed to not having that
       risk factor. In a *retrospective study (*\ also called a
       *case-control study)*, samples are drawn from those who have the
       disease and those who do not. It is then determined whether each
       subject has the risk factor. In this type of study, the relative
       risk cannot be estimated because the study design does not allow
       us to estimate the probability of the disease for those with or
       for those without the risk factor (see the Example 3.8 for
       clarification on this). So, we must use the odds ratio instead of
       the relative risk for these studies. This is why statisticians
       put so much emphasis on the odds ratio even though the relative
       risk is easier to understand and interpret.

    3. If the probability of the outcome under study in the general
       population is very low, then the odds ratio is typically close to
       the relative risk and can thus be used as an *estimate* of the
       relative risk (see Example 3.9 for clarification on this). ***
