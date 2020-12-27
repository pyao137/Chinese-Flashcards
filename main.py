import json
from random import randint
from typing import Dict, List

secs: List[str] = []
secs_ind: List[int] = []
data: Dict[str, List[str]] = {}
data["words"] = []
data["pinyin"] = []
data["english"] = []


def main() -> None:
    """Main function."""
    i: int = 0
    with open("words.txt", "r", encoding = "utf8") as file:
        for line in file:
            try:
                int(line[0])
                note_section(line, i)
                i += 1
            except:
                if ord(line[0]) >= 0x4e00 and ord(line[0]) <= 0x9fff: #Checks if the first character of a line is a Chinese character
                    count1: int = line.count("-")
                    count2: int = line.count("–")
                    count3: int = line.count("—")
                    if count1 + count2 + count3 != 2:
                        print("A line with a Chinese word did not contain 3 elements set off by dashes/hyphens and was thus dicarded.")
                    else:
                        note_words(line)
    #test_correctness()  #Use this to see if the data was organized correctly.
    show_sections()
    flash_cards()
    """Optional dump of results into a json file."""
    # with open('result.txt', 'w', encoding = "utf8") as outfile:
    #     json.dump(data, outfile)
        

def note_words(line: str) -> None:
    """Adds a line of text data to the list for Chinese words and two related elements."""
    positions: List[int] = [0, 0, 0, 0, 0, len(line)]
    for i in range(0, len(line)):
        if line[i] == "-" or line[i] == "–" or line[i] == "—":
            positions[1]= i
            positions[2] = i + 1
            break
    for k in range(positions[0] + 1, len(line)):
        if line[k] == "-" or line[k] == "–" or line[k] == "—":
            positions[3] = k
            positions[4] = k + 1
    data["words"].append(line[positions[0]: positions[1]].strip())
    data["pinyin"].append(line[positions[2]: positions[3]].strip())
    data["english"].append(line[positions[4]: positions[5]].strip())
            

def note_section(line: str, sec: int) -> None:
    """Processes a line of section data."""
    line = line.replace("\n", "")
    line = "SEC " + str(sec) + ": " + line
    data["words"].append(line)
    data["pinyin"].append("NEW DECK")
    data["english"].append("NEW DECK")
    secs.append(line)
    secs_ind.append(len(data["words"]) - 1)


def ask_repeats() -> bool:
    """Asks the user about repeats in the flashcards game."""
    repeats: bool = True
    while True:
        reps: str = input("Would you like repeats? 'y' for yes and 'n' for no: ")
        if reps == "y":
            break
        elif reps == "n":
            repeats = False
            break
        else:
            print("Error, inputted value is invalid")
    print(f"Repeats set: {repeats}\n")
    return repeats


def choose_deck() -> List[int]:
    """Chooses a deck for the user in the flashcard game."""
    first: int = 0
    last: int = len(data["words"]) - 1
    print("")
    if len(secs) == 0 and len(secs_ind) == 0:
        print("No indicated sections, so all cards will be reviewed.")
        return [first, last]
    while True:
        sec: int = int(input("Enter the section you want to review (or -1 for all cards): "))
        if sec > len(secs) - 1 or sec < -1:
            print("error, inputted value is invalid")
        else:
            if sec != -1:
                print(f"section chosen - {secs[sec]}")
            else:
                print("section chosen - all cards")
            break
    if sec != -1 and sec != len(secs_ind) - 1:
        first = secs_ind[sec]
        last = secs_ind[sec + 1]
    elif sec == len(secs_ind) - 1:
        first = secs_ind[sec]
    return [first, last]


def flash_cards() -> None:
    """The flashcard game."""
    section: List[int] = choose_deck()
    reps: bool = ask_repeats()
    done_before: List[int] = []
    while True:
        num: int = randint(section[0], section[1])
        if num in secs_ind:
            if reps is False and num not in done_before:
                done_before.append(num)
        elif len(done_before) == section[1] - section[0] + 1 and reps is False:
            print("All cards in deck have been reviewed and repeats are False.")
            while True:
                option: str = input("Would you like to quit the game? Enter 'q' to quit or 'c' to continue and change decks: ")
                if option == "q" or option == "Q" or option == "c" or option == "C":
                    break
                else:
                    print("Error, input was invalid.")
            if option == "q" or option == "Q":
                print("\nquitting...")
                break
            else:
                print("\nChanging decks...")
                show_sections()
                section = choose_deck()
                reps = ask_repeats()
                done_before.clear()
        elif num in done_before and reps is False:
            pass
        else:
            done_before.append(num)
            print(data["words"][num])
            entry: str = input("Enter above word, or q to quit, or c to change decks: ")
            print(f"{data['pinyin'][num]} -- {data['english'][num]}\n")
            if entry == "q" or entry == "Q":
                print("quitting game...")
                break
            elif entry == "c" or entry == "C":
                show_sections()
                section = choose_deck()
                reps = ask_repeats()
                done_before.clear()


def show_sections() -> None:
    """Shows the card sections."""
    print("card sections: ")
    if len(secs) == 0 and len(secs_ind) == 0:
        print("No indicated sections")
    else:
        for x in range(0, len(secs)):
            print(secs[x])


def test_correctness() -> None:
    """Tests if the word data was correctly parsed and flashcards were correctly generated."""
    if len(data["words"]) != len(data["pinyin"]) or len(data["words"]) != len(data["english"]):
        print("Error: lists storing word data and related information don't match.")
    else:
        print("No word data list mismatch")
    if len(secs) != len(secs_ind):
        print("Error: section tracking mismatch.")
    else:
        print("No section tracking mismatch")
    print("The three lists:")
    for x in range(0, len(data["words"])):
        if data['pinyin'][x] == "NEW DECK":
            print("")
        print(f"#{x} {data['words'][x]} -- {data['pinyin'][x]} -- {data['english'][x]}")
    print("The section trackers:")
    for i in range(0, len(secs)):
        print(f"{secs[i]} ----- {secs_ind[i]}")


if __name__ == "__main__":
    main()