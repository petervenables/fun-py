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
note: There is no character "swap" action

Given the two strings: "FART" and "FLEET" the number of changes are 3
- A -> L (change)
- R -> E (change)
- E (add)   

## Word Ladder

A word ladder is a series of words where each word differs from the previous in exactly one place. For example, cold -> cord is a 2-element word ladder.

 Word ladders can span between two totally different words. For example, if we wanted to get from start word "cold" to end word "warm", we could use this sequence: cold -> cord -> card -> ward -> warm.

We want to automatically solve this kind of problem _specifically_ for 3-letter words: write a method, `solve`, which accepts a `start` and an `end` word, then returns a sequence of words that solves the puzzle.

The output sequence should include both the start word and the end word, and should be returned in-order.

You may assume that both input words are exactly 3 letters long.

There are test cases at the bottom of the file. Try to fulfill the easy cases first, before enabling the harder cases.

You are given a dictionary of three letter words: