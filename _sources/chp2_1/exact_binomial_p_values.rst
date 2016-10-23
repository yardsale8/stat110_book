Using the Binomial Distribution to Find Exact p-Values
------------------------------------------------------

There is one caveat regarding our current approach to obtaining a
p-value. Certainly, different simulations will produce slightly
different simulated distributions. The general pattern will be the same,
but variations do exist. For example, consider the Helper vs. Hinderer
study.

|image32|

The study’s observed result was as follows: 14 out of 16 infants chose
the helper toy. What if two different researchers each carried out their
own simulation study to estimate the p-value?\ *

|image33|

Fortunately, regardless of which simulation study we use in the
previous example, the final conclusion is the same, and the
discrepancy between the two estimated p-values is minimal; still, it’s
not ideal that two different researchers get different results.
Note that as the number of trials in our simulation study increases,
we expect less discrepancy between these two estimates of the p-value.
So, instead of using a simulation study with only 1,000 trials to
*estimate* the p-value, we would ideally like to simulate this
experiment over and over again, say an *infinite* number of times.
This would provide us with the theoretical probabilities of interest
so that can get exact p-values instead of an estimate of the p-value.
The following graphic shows what the distribution would look like if
we kept repeating the simulation study over and over again, each time
counting and plotting the number of infants that chose the helper toy
(assuming there was no real preference in the population of all
infants). This theoretical probability distribution is known as the
**binomial distribution**.

|image14|

We can calculate these probabilities using the Excel file
**BinomialProbabilities.xls**, which can be found on the course website.

.. admontion:: Questions:

    1. Does the general pattern in the above graph agree with the simulated
       distributions obtained from the simulation study in Tinkerplots?

    2. The binomial probability value for 14 is 0.0018, or .18%. What does
       this value mean? Explain.

    3. When we estimated the p-value using the results of the simulation
       study, we calculated the proportion of dots at 14 or above. How would
       we obtain the p-value using binomial probabilities? Explain.

    4. What is the p-value using the binomial probabilities?

Statisticians often use the binomial distribution to calculate p-values
when testing claims about a population proportion. However, before using
this distribution, we should check to make sure the following conditions
are met (note that these same conditions have to be met in order to
estimate the p-value via a simulation study, as well).

.. admonition:: The Binomial Distribution - When can we use it?

    This distribution can be used whenever the following assumptions are met:

    -  The study involves a fixed number of trials, n.
    -  There are only two possible outcomes on each trial (we call these a “success” or “failure”).
    -  The probability of “success” (π) remains constant from trial to trial.
    -  The n trials are independent.

Check whether these assumptions seem reasonable for the Helper vs.
Hinderer study.

-  There exist a fixed number of trials, n.

-  There are only two possible outcomes on each trial (“success” or
       “failure”).

-  The probability of success (π) remains constant from trial to trial.

-  The n trials are independent.
