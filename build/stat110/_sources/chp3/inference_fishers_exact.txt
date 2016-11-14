Statistical Inference: Fisher’s Exact Test to Obtain Exact p-values
-------------------------------------------------------------------

We just used a simulation study to investigate the Mythbusters’
research hypothesis. This is a valid analysis; however, it provides
only an approximate p-value. We can obtain the exact p-value using
probability theory and a distribution known as the hypergeometric
distribution. Details about the hypergeometric distribution are
beyond the scope of this course; however, we will discuss **Fisher’s
Exact Test** which uses the hypergeometric distribution to calculate
p-values. This is easily carried out in JMP.

Note the output obtained when you used the **Analyze > Fit Y by X**
option:

|image309|

JMP has already used the hypergeometric probability distribution to
calculate the probability of observing results at least as extreme as
those observed in the MythBusters actual experiment. Now, you can use
this output to carry out the test.

Carrying out Fisher’s Exact Test
++++++++++++++++++++++++++++++++

This test is based on the probability of observing data at least as
extreme as the actual observed data. The procedure is carried out as
follows.

|image3047|
