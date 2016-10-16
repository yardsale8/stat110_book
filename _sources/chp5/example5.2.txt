
**Example 5.2:** Another “simulation study”….
+++++++++++++++++++++++++++++++++++++++++++++

Suppose we set up a hypothetical population of smokers suffering from
nicotine withdrawal. We will do this by taking bootstrap samples from the sample
in TinkerPlots.

|image1|

.. note::

    We could also generate this distribution using StatKey, but we will use
    TinkerPlots here as an introduction.

.. admonition:: Question

    In this simulation study, what is our value of μ, the true population
    mean?

Note that in reality, the true population mean is usually an unknown
quantity which we are trying to estimate. Since it is not feasible to
collect data on the entire population of smokers suffering from nicotine
withdrawal, the researchers took a random sample of 20 subjects in order
to estimate the average perceived elapsed time. Let’s see what happens
when we take various samples of size 20 from this population.

We can use Tinkerplots to carry out this simulation. Each of the
elements in the mixer represents the perceived elapsed time for a smoker
suffering from nicotine withdrawal in the population (e.g., the
highlighted subject thought that 50 seconds had passed during a
45-second period). We set the repeat value to 20 in order to randomly
select 20 subjects from the population for our study.

|image2|

Click Run to randomly select our first sample of 20 subjects, and we can
then create a plot of their perceived elapsed times. Note that the mean
of these 20 subjects is shown on this plot.

Sample # 1:
+++++++++++

|image3|


.. .. admonition:: Questions:
.. 
..     1. What is the average (or mean) perceived elapsed time of the 20
..        subjects in this study?
.. 
..     2. Does this necessarily mean that the average perceived elapsed time is
..        greater than 45 seconds for *all* smokers suffering from nicotine
..        withdrawal? What would you say to a researcher who tried to use only
..        this sample mean to draw this conclusion?

Even though in reality we would carry out a study only once, we will
use Tinkerplots to take a sample of 20 subjects from this population
over and over again so that we get an idea of how much the sample mean
*could* change from sample to sample. Our second and third random
samples of 20 subjects and their sample means are shown below:

Sample #2:
++++++++++

|image4|

Sample #3:
++++++++++

|image5|

We can start to collect these sample means in a new plot to create the
distribution of sample means:

|image6|

To get a really good idea of what values are likely to occur by chance
when taking random samples of size 20 from the population, we should
take more than just three samples. The graphic below shows the process
we used to create the distribution of sample means and the final plot of
the means of 1,000 random samples.

|image7|

|image8|

This is a distribution of sample means. Recall that these 1,000 samples
(each consisting of 20 subjects) came from a population with a true mean
perceived elapsed time of 45 seconds. So, this distribution gives us a
good idea of what sample means from 20 subjects are likely (or unlikely)
to occur by chance if the true mean is 45 seconds.

.. Next, note that the researchers wanted to show that the mean perceived
.. elapsed time for smokers suffering from nicotine withdrawal was in
.. fact *greater* than 45 seconds. The null and alternative hypotheses to
.. address this research question are given as follows.
.. 
.. H\ :sub:`o`: The mean perceived elapsed time for smokers suffering
.. from nicotine withdrawal is equal
.. to 45 seconds.
.. 
.. H\ :sub:`a`: The mean perceived elapsed time for smokers suffering
.. from nicotine withdrawal is greater
.. than 45 seconds.
.. 
.. Note that the distribution of sample means was created assuming the null
.. hypothesis is true. To test this hypothesis, we compare our actual
.. observed mean to this null model. If the sample mean from the actual
.. research study is not likely to occur by chance according to this null
.. model (i.e., if it is an outlier on this null model), then we have
.. evidence against the null model and in support of the research question.
.. 
.. Recall that in the actual research study, the mean perceived elapsed
.. time for the 20 subjects studied was 55.05 seconds. Sketch this observed
.. value on the null model:
.. 
.. |image9|
.. 
.. There are two explanations for this observed mean of 55.05 seconds:
.. either (1) the true mean perceived elapsed time for smokers suffering
.. from nicotine withdrawal really is greater than 45 seconds, or (2) their
.. time perception is not impaired (i.e., the true mean is actually 45
.. seconds) and the sample mean was greater than 45 seconds simply because
.. of random chance.
.. 
.. .. admonition:: Questions:
.. 
..     1. Was a sample mean of 55.05 seconds likely to occur by chance if the
..        true population mean is actually 45 seconds? What does this imply
..        about the research question?
.. 
..     2. Give an approximate p-value based on this simulation study.
.. 
.. 
