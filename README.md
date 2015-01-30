
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
algorithm for cheaply generating random numbers with period of at least 2^19937
- 1. Let `s` be the server and `c` be a client. The protocol follows:

* `c` generates `static_seed_n` for each class using MT.
* `s` generates `public_seed` using MT and distributes it to `c`.
* `c` uses CLCG to generate random variables using `static_seed_n XOR 
public_seed`
