
PRNG Testing
============

This is a simple set of scripts for correlating sequences derived from a
specific random number generator protocol.

Protocol
--------

The protocol defined here represents a client-server relationship for a game
environment, where randomness is valuable but not necessarily a cryptographical
necessity. Two RNG algorithms are used; CLCG, a weak algorithm for cheaply
generating random numbers with period of at least 100, and MT, a stronger
algorithm for cheaply generating random numbers with period of at least 
2^19937 - 1. Let `s` be the server and `c` be a client. The protocol follows:

* `c` generates `static_seed_n` for each class using MT.
* `s` generates `public_seed` using MT and distributes it to `c`.
* `c` uses CLCG to generate random variables using `static_seed_n XOR 
public_seed`

Desirables
----------

No sequence of random variables generated by `c` should correlate with another
sequence

Explanation
-----------

A c++ program is provided which generates a set of random numbers following the
protocol. Two python scripts can parse the format of these random numbers and
calculate cross-correlation between sequences that share a public seed.

Usage
-----

* Build the c++ program using `make only`
* Run the c++ program to see typical seeds as desired using `./bin/main`
* Generate graphs of cross-correlation sequences using `./bin/main | python 
correlate_graphs.py`
* Generate stats of peak cross-correlation values using `./bin/main | python 
correlate_stats.py`

Customization
-------------

* The number of tests, seeds, and samples can be adjusted in `main.cpp`
* The number of graphs generated (one per CLCG instance) can be adjusted in
`correlation_graphs.py`
* The number of histogram bins can be adjusted in `correlation_stats.py`

Requirements
------------

* The makefile uses g++ to compile; a linux environment is desirable but will
build in cygwin as well.
* Python 2.7, numpy, and matplotlib are required to generate stats and graphs.
Tested with python 2.7 AMD64, numpy 1.9 AMD64, and matplotlib 1.2 AMD64