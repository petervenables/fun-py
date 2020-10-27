from WordLadder import Ladder
import word_list


def main():
    ladder = Ladder("cat", "dog")
    for ridx, rung in enumerate(ladder.rungs):
        options = ladder.rungs[ridx].get_options(word_list.dictionary)
        print("---")
        for option in options:
            print(option.start)
            if option.distance < ladder.rungs[ridx].distance and option.distance >= 1:
                # we're taking the first, closer option
                if option.start != ladder.rungs[ridx].start:
                    ladder.rungs.append(option)
                    break
    print(ladder.print())


if __name__ == "__main__":
    main()
