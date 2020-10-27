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

You are given a dictionary of three letter words

## Scrabble Solver (idea)

An interesting problem (that was not asked in an interview to date) is a variation on the theme of word searching. Develop an algorithm that finds the best words from a rack of seven letters (as one would have in a scrabble game). The point of this is not to solve for a specific board game position but to find candidate words that not only take into account length of word but also weighted by letter point value.

This would require a mapping of letters and values as well as an algorithm that efficiently identifies candidates from the set of characters. 

Scrabble sets have 100 tiles with the following distribution and values
2 blank tiles (scoring 0 points)
1 point: E ×12, A ×9, I ×9, O ×8, N ×6, R ×6, T ×6, L ×4, S ×4, U ×4
2 points: D ×4, G ×3
3 points: B ×2, C ×2, M ×2, P ×2
4 points: F ×2, H ×2, V ×2, W ×2, Y ×2
5 points: K ×1
8 points: J ×1, X ×1
10 points: Q ×1, Z ×1
