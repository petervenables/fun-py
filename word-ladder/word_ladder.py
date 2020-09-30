
import word_list as WL

def solve(start: str, end: str) -> list:
    if start.lower() not in WL.dictionary or end.lower() not in WL.dictionary:
        # there is no solution
        return []
    diffs = count_differences(start.lower(), end.lower())
    if diffs == 0:
        # same word in both, return 1 
        return [start]
    elif diffs == 1:
        # trivial case, return the original words
        return [start, end]
    else:
        # we should have 2 or 3 differences at this point:
        # we need to identify candidate words from start that include
        # the end word letters in position for the straightforward 
        # algorithm. 
        ladder = [start, end]
        while diffs > 1:
            candidate = find_candidate_word(ladder)
            if candidate != "":
                ladder.insert(-1,candidate)
            else:
                # no candidate found, we should abort
                return []
            # diffs = count_differences(ladder[-1],ladder[-2])
            diffs -= 1
        return ladder

# NB: this will take the first candidate word it finds
# Also assuming 3 letter words because we can.
def find_candidate_word(in_list: list) -> str:
    start = in_list[-2].lower()
    end = in_list[-1].lower()
    cand = ""
    for i, lch in enumerate(start):
        if i == end[i]:
            next
        else:
            if i == 0: 
                cand = f"{end[i]}{start[1:]}"
            if i == 1:
                cand = f"{start[0]}{end[i]}{start[2]}"
            if i == 2:
                cand = f"{start[:2]}{end[i]}"
            if cand in WL.dictionary:
                break
            else:
                cand = ""
    return cand


def count_differences(left: str, right: str) -> int:
    return sum([1 for (l, r) in zip(left, right) if l != r])


def main():
    print(solve("cat", "dog"))
    print(solve("gnu", "ism"))


if __name__ == "__main__":
    main()