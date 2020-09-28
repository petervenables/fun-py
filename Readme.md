# Python Fun 

A simple project around demonstrating coded solutions to arbitrary problems.

## Morph.py

morph.py -- implementation of an interview question as follows:
   "Implement a function that returns the number of transformations
   between two strings where the possible transformations are:
       - add a single character
       - remove a single character
       - change a single character"

### Examples:
   
Given two strings: "CAT" and "FAT" the number of changes are 1
- C -> F (change)

Given two strings: "AFT" and "FAT" the number of changes is 2
- A -> F (change)
- F -> A (change)
* There is no "swap" action

Given the two strings: "FART" and "FLEET" the number of changes are 3
- A -> L (change)
- R -> E (change)
- E (add)   
