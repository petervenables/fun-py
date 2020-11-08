# from itertools import permutations
import os
from collections import Counter


def load_words(wordfile: str) -> list:
    words = []
    try:
        with open(wordfile, 'r') as wordfile:
            for word in wordfile:
                words.append(word.strip())
        wordfile.close()
    except Exception as e:
        print(e, os.getcwd())
    return words


def solve(rack: str, wordfile: str) -> dict:
    tiles = Counter(rack)
    words = load_words(wordfile)
    sol = {}
    for word in words:
        wordc = Counter(word)
        if tiles & wordc == wordc:
            if sol.get(len(word)) is None:
                sol[len(word)] = []
            sol[len(word)].append(word)
    return sol


def score(sol: dict) -> dict:
    tile_vals = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
                 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
                 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
                 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
    score = {}
    for key in sol:
        for word in sol[key]:
            subtot = 0
            for ch in word:
                subtot += tile_vals[ch]
            if score.get(subtot, None) is None:
                score[subtot] = []
            score[subtot].append(word)
    return score


def main():
    rack = "ABCDEFG"
    print(f"Rack contains: {rack}")
    wordfile = "collins_scrabble_words-2019.txt"
    sol = solve(rack, wordfile)

    print("Found words:")
    for key in sorted(sol.keys()):
        print(f"{key} letters: {sol[key]}")

    print("\n")
    print("Scored words:")
    myscore = score(sol)
    for key in sorted(myscore.keys()):
        print(f"{key} points: {myscore[key]}")


if __name__ == "__main__":
    main()
