try:
    import keyboard
    import time
    from scripts import pyaddremovebook, pylendbook, pyreturnrenew, pysearchbooklist, pysuggestion, pyadmin
    from required import pyread
except Exception as e:
    print(f"There is some error occurred while importing modules.{e}")


print("+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+-+")
print("|W|E|L|C|O|M|E| |T|O| |X|Y|Z| |L|I|B|R|A|R|Y|")
print("+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+-+")
time.sleep(1)
while True:
    print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("|    * To view all books press    [Ctrl + 1]  |")
    print("|    * To borrow book press       [Ctrl + 2]  |")
    print("|    * To return/renew book press [Ctrl + 3]  |")
    print("|    * To search book press       [Ctrl + 4]  |")
    print("|    * To donate book press       [Ctrl + 5]  |")
    print("|    * To suggest book press      [Ctrl + 6]  |")
    print("|    * To read book press(beta)   [Ctrl + 7]  |")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    while True:
        if keyboard.is_pressed("Ctrl + 1"):
            pysearchbooklist.book_list()
            time.sleep(1)
            while True:
                if keyboard.is_pressed("Enter"):
                    break
            break
        if keyboard.is_pressed("Ctrl + 2"):
            book_name = input("Enter Book Name or Book Id: ")
            name = input("Enter Your full name: ")
            pylendbook.lendbook(book_name, name)
            time.sleep(4)
            break
        if keyboard.is_pressed("Ctrl + 3"):
            print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("|    * To return book press       [Ctrl + 1]  |")
            print("|    * To renew book press        [Ctrl + 2]  |")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            while True:
                if keyboard.is_pressed("Ctrl + 1"):
                    ref = int(input("Enter Reference number: "))
                    name = input("Enter your full name: ")
                    phone = input("Enter your phone no.: ")
                    pyreturnrenew.returnlend(ref, name, phone)
                    break
                if keyboard.is_pressed("Ctrl + 2"):
                    ref = int(input("Enter Reference number: "))
                    pyreturnrenew.lendrenew(ref)
                    break
            time.sleep(4)
            break
        if keyboard.is_pressed("Ctrl + 4"):
            book = input("Enter Book Name, Book Price, Author Name or Book Id to search: ")
            pysearchbooklist.searchbook(book)
            time.sleep(2)
            while True:
                if keyboard.is_pressed("Enter"):
                    break
            break
        if keyboard.is_pressed("Ctrl + 5"):
            pyaddremovebook.donation()
            time.sleep(3)
            break
        if keyboard.is_pressed("Ctrl + 6"):
            pysuggestion.start()
            time.sleep(3)
            break
        if keyboard.is_pressed("Ctrl + 7"):
            pyread.readbook()
            break
        if keyboard.is_pressed("Ctrl + Shift + Alt + F1"):
            pyadmin.admin()
        if keyboard.is_pressed("Esc"):
            time.sleep(1)
            if keyboard.is_pressed("Esc"):
                break
    if keyboard.is_pressed("Esc"):
        time.sleep(2)
        if keyboard.is_pressed("Esc"):
            break
