.. raw::

    <script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>
Confidence Intervals Based on the Normal Distribution
=====================================================

We in our bootstrap activities we have seen some common result.

.. admonition:: Important Points

    1. The distribution of the sample mean was often (but not always) a
       bell-shaped curve.
    2. Using a margin of error of 2 standard errors resulted in intervals that
       worked about 95% of the time.

In this section, we leverage these facts and introduce a theoretical
approach to confidence intervals that will save us the work of running a
simulation every time we want an interval.

.. include:: example5.1.rst

.. include:: example5.2.iverson.rst

.. include:: central_limit_theorem.rst

.. include:: assessing_normality.rst

.. include:: confidence_interval_single_mean.rst


.. |image500| image:: ../chp5/img/media/image1.png
   :width: 4.73105in
   :height: 2.12936in
.. |image501| image:: ../chp5/img/media/image2.png
   :width: 5.88000in
   :height: 2.21941in
.. |image502| image:: ../chp5/img/media/image3.png
   :width: 5.44792in
   :height: 3.50089in
.. |image503| image:: ../chp5/img/media/image4.png
   :width: 5.21875in
   :height: 1.28125in
.. |image504| image:: ../chp5/img/media/image5.png
   :width: 4.79452in
   :height: 1.28425in
.. |image505| image:: ../chp5/img/media/image6.png
   :width: 4.84247in
   :height: 1.14563in
.. |image506| image:: ../chp5/img/media/image7.png
   :width: 3.00685in
   :height: 1.48201in
.. |image507| image:: ../chp5/img/media/image8.png
   :width: 6.24657in
   :height: 4.04893in
.. |image508| image:: ../chp5/img/media/image9.png
   :width: 5.80208in
   :height: 2.16973in
.. |image509| image:: ../chp5/img/media/image10.png
   :width: 4.36476in
   :height: 1.66241in
.. |image5010| image:: ../chp5/img/media/image12.png
   :width: 4.48663in
   :height: 1.70378in
.. |image5011| image:: ../chp5/img/media/image14.png
   :width: 2.25134in
   :height: 1.51344in
.. |image5012| image:: ../chp5/img/media/image15.png
   :width: 3.50802in
   :height: 1.68958in
.. |image5013| image:: ../chp5/img/media/image16.png
   :width: 2.19251in
   :height: 1.46647in
.. |image5014| image:: ../chp5/img/media/image17.png
   :width: 3.42781in
   :height: 1.73307in
.. |image5015| image:: ../chp5/img/media/image19.png
   :width: 3.25669in
   :height: 1.45399in
.. |image5016| image:: ../chp5/img/media/image21.png
   :width: 3.67708in
   :height: 1.74952in
.. |image5017| image:: ../chp5/img/media/image23.png
   :width: 3.71875in
   :height: 1.51978in
.. |image5018| image:: ../chp5/img/media/image1.png
   :width: 5.21875in
   :height: 2.34886in
.. |image5019| image:: ../chp5/img/media/image12.png
   :width: 4.71875in
   :height: 1.79193in
.. |image5020| image:: ../chp5/img/media/image27.png
   :width: 4.91667in
   :height: 1.90355in
.. |image5021| image:: ../chp5/img/media/image28.png
   :width: 3.71875in
   :height: 1.67385in
.. |image5022| image:: ../chp5/img/media/image29.png
   :width: 2.20833in
   :height: 3.03125in
.. |image5023| image:: ../chp5/img/media/image30.png
   :width: 2.48958in
   :height: 1.96875in
.. |image5024| image:: ../chp5/img/media/image31.png
   :width: 2.83333in
   :height: 2.09375in
.. |image5025| image:: ../chp5/img/media/image32.png
   :width: 5.25343in
   :height: 2.36447in
.. |image5026| image:: ../chp5/img/media/image12.png
   :width: 4.16667in
   :height: 1.58228in
.. |image5027| image:: ../chp5/img/media/image27.png
   :width: 4.27083in
   :height: 1.65351in
.. |image5028| image:: ../chp5/img/media/image33.png
   :width: 2.27083in
   :height: 3.06250in
.. |image5029| image:: ../chp5/img/media/image34.png
   :width: 2.32292in
   :height: 1.26042in
.. |image5030| image:: ../chp5/img/media/image35.png
   :width: 2.86458in
   :height: 2.25000in
.. |image5031| image:: ../chp5/img/media/image36.png
   :width: 4.17708in
   :height: 1.91996in
.. |image5032| image:: ../chp5/img/media/image37.png
   :width: 2.38542in
   :height: 3.09375in
.. |image5033| image:: ../chp5/img/media/image38.png
   :width: 3.27083in
   :height: 1.70121in
.. |image5034| image:: ../chp5/img/media/image40.png
   :width: 1.73958in
   :height: 0.42708in
.. |image5035| image:: ../chp5/img/media/image41.png
   :width: 1.89583in
   :height: 0.65625in
.. |image5036| image:: ../chp5/img/media/image1.png
   :width: 5.21875in
   :height: 2.34886in
.. |image5037| image:: ../chp5/img/media/image1.png
   :width: 5.17123in
   :height: 2.32748in
.. |image5038| image:: ../chp5/img/media/image44.png
   :width: 4.48958in
   :height: 1.79167in
.. |image5039| image:: ../chp5/img/media/t_statistic.png
   :width: 5.18in
   :height: 0.69in
.. |image510| image:: img/histogram_normal_curve.png
   :width: 5.02in
   :height: 3.47in
.. |image511| image:: img/normal_data.png
   :width: 3.40in
   :height: 5.11in
.. |image512| image:: img/non_normal_data.png
   :width: 3.38in
   :height: 5.20in
.. |image513| image:: img/chi_square.png
   :width: 6.96in
   :height: 6.12in
.. .. |image514| image:: img/CI_in_JMP_sm.gif
.. |image514| image:: img/CI_in_JMP.gif
   :width: 6.36in
   :height: 3.21in
.. |image515| image:: img/t_quantile.gif
   :width: 7.23in
   :height: 4.41in
.. |image516| image:: img/normal_quantile_plot.gif
   :width: 7.23in
   :height: 4.41in
.. |image517| image:: img/picking_correct_procedure.png
   :width: 8.64in
   :height: 6.01in
