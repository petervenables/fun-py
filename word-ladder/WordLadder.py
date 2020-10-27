
alphabet = 'abcdefghijklmnopqrstuvwxyz'


class Ladder:

    def __init__(self, start, end):
        self.rungs = [Rung(start, end)]
        self.sep = " - "

    def print(self):
        if len(self.rungs) == 1:
            rung = self.rungs[0]
            print(self.sep.join([rung.start, rung.end]))
        else:
            ladder = []
            for rung in self.rungs:
                ladder.append(rung.start)
            ladder.append(self.rungs[0].end)
            return(self.sep.join(ladder))


class Rung:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.distance = hamming_distance(start, end)
        self.options = []

    def print(self):
        return(f"{self.start}, {self.end}, {self.distance}")

    def get_options(self, wordlist):
        options = set()
        for idx, ch in enumerate(self.start):
            for letter in alphabet:
                candidate = self.start[:idx] + letter + self.start[idx + 1:]
                if candidate in wordlist:
                    options.add(Rung(candidate, self.end))
        return options


def hamming_distance(start, end) -> int:
    if len(start) != len(end):
        raise ValueError("Error: Comparables not same length!")
    return sum(lch != rch for lch, rch in zip(start, end))
