try:
    import keyboard
    import time
    import pyaddremovebook, pylendbook, pyreturnrenew, pysearchbooklist, pysuggestion
    from required import pyread
except Exception as e:
    print(f"There is some error occurred while importing modules.{e}")


def admin():
    print("+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+-+")
    print("|W|E|L|C|O|M|E| |T|O| |A|D|M|I|N| |M|O|D|E|")
    print("+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+-+")
    time.sleep(1)
    while True:
        print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("|    * To view all books press       [Ctrl + 1]  |")
        print("|    * To view borrowed books press  [Ctrl + 2]  |")
        print("|    * To view borrowed books detail [Ctrl + 3]  |")
        print("|    * To view library books detail  [Ctrl + 4]  |")
        print("|    * To view suggested book press  [Ctrl + 5]  |")
        print("|    * To view read book detail      [Ctrl + 6]  |")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        while True:
            if keyboard.is_pressed("Ctrl + 1"):
                pysearchbooklist.book_list()
                time.sleep(1)
                while True:
                    if keyboard.is_pressed("Enter"):
                        break
                break

            if keyboard.is_pressed("Ctrl + 2"):
                a = pyread.readlendbook()
                print(a)
                break
            if keyboard.is_pressed("Ctrl + 3"):
                a = pyread.lendbookdet()
                print(a)
                break
            if keyboard.is_pressed("Ctrl + 4"):
                a = pyread.libbookdet()
                print(a)
                break
            if keyboard.is_pressed("Ctrl + 5"):
                a = pyread.suggestion()
                print(a)
                break
            if keyboard.is_pressed("Ctrl + 6"):
                a = pyread.readbookdet()
                break
