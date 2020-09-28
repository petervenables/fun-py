import random

def morph_count(first, second):
    count = 0
    if first == second:
        return count
    if len(second) > len(first):
        count += len(second) - len(first)
        second = remove_added(first, second)
    elif len(first) > len(second):
        count += len(first) - len(second)
        first = remove_added(second, first)
    for i in range(len(first)):
        if first[i] == second[i]:
            continue
        else:
            count += 1
    return count

# Remove the characters from the longer string to 
# account for those changes
def remove_added(shorter, longer):
    while len(longer) > len(shorter):
        idx = random.randrange(len(longer))
        if longer[idx] not in shorter:
            longer = longer.replace(longer[idx], '', 1)
        else:
            continue
    return longer


def main():
    print("Morph count of CAT->FAT:", morph_count("CAT", "FAT"))
    print("Morph count of AFT->FAT:", morph_count("AFT", "FAT"))
    print("Morph count of FART->FLEET", morph_count("FART", "FLEET"))


if __name__ == "__main__":
    main()