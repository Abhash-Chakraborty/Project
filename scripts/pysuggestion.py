import keyboard
import pickle


def suggestion_box():
    bname = input(f"Enter name of the book:")
    author = input(f"Enter name of the Author:")
    name = input(f"Enter your name:")
    phone = int(input(f"Enter your phone no.:"))
    print(f"The name of the book: {bname}\n"
          f"The name of the Author: {author}\n"
          f"Your name: {name}\n"
          f"Your phone no.: {phone}\n")
    con = input(F"Do you want to continue[y/n]:")
    if con == "y" or con == "Y":
        with open("assets/files/Suggestion.dat", "ab") as f:
            l = [bname, author, name, phone]
            pickle.dump(l, f)

        print(f"Thank you for your Suggestion. You will be notified when the book is added to the library.")


def start():
    s = 0
    print("\nPress [Ctrl + 1] to continue or [Ctrl + q] to quit")
    while s < 1:
        if keyboard.is_pressed("Ctrl + 1"):
            print(f"\n+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+-+\n"
                  f"|W|E|L|C|O|M|E| |T|O| |S|U|G|G|E|S|T|I|O|N| |B|O|X|\n"
                  f"+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+-+")
            suggestion_box()
            s += 1
            break
        if keyboard.is_pressed("q"):
            print("Quiting...")
            break
