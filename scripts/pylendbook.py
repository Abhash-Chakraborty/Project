import pickle
import keyboard
import time
import datetime
from required import pyread
from required import pynogen


def lendbook(book_name, name, username="", phone=""):
    ref = pynogen.referenceno()
    a = book_name.upper()
    book = []
    name = name.upper()
    username = username
    phone = str(phone)
    with open("assets\\files\\booklist.dat", "rb") as f:
        try:
            print(
                f"_________________________________________________________________________________"
                f"________________________________________________________________")
            print(
                f"S.no.    Book I.D.            Author                       "
                f"Availability                          Book Name                                       ")
            print(
                f"_________________________________________________________________________________"
                f"________________________________________________________________")
            b = a.split(" ")
            w = 1
            n = 1
            while True:
                l = pickle.load(f)
                r0 = l[0].split(" ")
                r1 = l[1].split(" ")
                r2 = l[2].split(" ")
                r3 = l[3].split(" ")
                r4 = l[4].split(" ")
                w1 = 0
                w2 = 0
                w3 = 0
                w4 = 0
                for i in r0:
                    for k in b:
                        if k == i:
                            if l in pyread.readlendbook():
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Not available    {' ' * (30 - len('Not available'))}{l[1]}")
                                w += 1
                                n += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1
                                break
                            else:
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Available    {' ' * (30 - len('Available'))}{l[1]}")
                                w += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1
                                book = l

                for i in r1:
                    for k in b:
                        if k in i and w1 == 0 and len(k) != 0:
                            if l in pyread.readlendbook():
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Not available    {' ' * (30 - len('Not available'))}{l[1]}0")
                                w += 1
                                n += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1
                            else:
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Available    {' ' * (30 - len('Available'))}{l[1]}")
                                w += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1

                for i in r2:
                    for k in b:
                        if k in i and w2 == 0 and len(k) != 0:
                            if l in pyread.readlendbook():
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Not available    {' ' * (30 - len('Not available'))}{l[1]}")
                                w += 1
                                n += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1
                            else:
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Available    {' ' * (30 - len('Available'))}{l[1]}")
                                w += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1

                for i in r3:
                    for k in b:
                        if k == i and w3 == 0:
                            if l in pyread.readlendbook():
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Not available    {' ' * (30 - len('Not available'))}{l[1]}")
                                w += 1
                                n += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1
                            else:
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Available    {' ' * (30 - len('Available'))}{l[1]}")
                                w += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1

                for i in r4:
                    for k in b:
                        if k == i and w4 == 0:
                            if l in pyread.readlendbook():
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Not available    {' ' * (30 - len('Not available'))}{l[1]}")
                                w += 1
                                n += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1
                            else:
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Available    {' ' * (30 - len('Available'))}{l[1]}")
                                w += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1

        except EOFError:
            if w == 2:
                if w == n:
                    print(
                        f"_________________________________________________________________________________"
                        f"________________________________________________________________")
                    print(
                        f"                                                   "
                        f"The book is not available in the library")
                    print(
                        f"_________________________________________________________________________________"
                        f"________________________________________________________________\n")

                else:
                    if book_name[0] == "#":
                        print(
                            f"_________________________________________________________________________________"
                            f"________________________________________________________________")
                        if phone == "":
                            phone = input(
                                f"\nEnter your 10 digit mobile no.:  ")
                        try:
                            phon = int(phone)
                            if len(phone) == 10:
                                print(f"\nYour Name = {name}\n"
                                      f"Your username = {username}\n"
                                      f"Phone no. = {phon}\n"
                                      f"Book Name = {book[1]}\n"
                                      f"Price = ₹{book[3]}/week or ₹{book[4]}/month\n"
                                      f"\nIf you want to continue press [Ctrl + 1] otherwise press[Ctrl + 2].")
                                while True:
                                    if keyboard.is_pressed('Ctrl + 1'):
                                        time.sleep(0.2)
                                        print(
                                            f"\nFor weekly subscription press [Ctrl + 3] for monthly subscription press [Ctrl + 4]:")
                                        while True:
                                            if keyboard.is_pressed('Ctrl + 3'):
                                                with open("assets\\files\\lendbook.dat", "ab") as m:
                                                    pickle.dump(book, m)
                                                with open("assets\\files\\lendbookdet.dat", "ab") as m:
                                                    book.append(name)
                                                    book.append(username)
                                                    book.append(phon)
                                                    book.append(datetime.date.today())
                                                    book.append(datetime.date.today() + datetime.timedelta(days=7))
                                                    book.append("Borrowed")
                                                    book.append(ref)
                                                    pickle.dump(book, m)
                                                print(
                                                    f"\nPlease renew the book before {datetime.date.today() + datetime.timedelta(days=7)}. Your reference number is {ref}.")
                                                break
                                            elif keyboard.is_pressed('Ctrl + 4'):
                                                with open("assets\\files\\lendbook.dat", "ab") as m:
                                                    pickle.dump(book, m)
                                                with open("assets\\files\\lendbookdet.dat", "ab") as m:
                                                    book.append(name)
                                                    book.append(username)
                                                    book.append(phon)
                                                    book.append(datetime.date.today())
                                                    book.append(datetime.date.today() + datetime.timedelta(days=30))
                                                    book.append("Borrowed")
                                                    book.append(ref)
                                                    pickle.dump(book, m)
                                                print(
                                                    f"\nPlease renew the book before {datetime.date.today() + datetime.timedelta(days=30)}. Your reference number is {ref}.")
                                                break
                                            elif keyboard.is_pressed('q'):
                                                print(f"\nOperation canceled")
                                                break
                                    if keyboard.is_pressed('Ctrl + 2'):
                                        print(f"\nOperation canceled")
                                        break
                                    if keyboard.is_pressed("Ctrl + 3") or keyboard.is_pressed("Ctrl + 4"):
                                        break
                                    if keyboard.is_pressed("q"):
                                        print(f"\nOperation canceled")
                                        break
                            else:
                                print(f"\nInvalid Input")
                        except Exception:
                            print(f"\nInvalid Input")

                    else:
                        print(
                            f"_________________________________________________________________________________"
                            f"________________________________________________________________")
                        print(
                            f"                                                   "
                            f"{w - 1} book found in the library")
                        print(
                            f"_________________________________________________________________________________"
                            f"________________________________________________________________")
                        book_name = input(
                            f"\nEnter Book I.D.(Book I.D. should start with # symbol):  ")
                        print()
                        lendbook(book_name, name, username, phone)

            elif w == 1:
                print(
                    f"                                                   "
                    f"Sorry no book found in the library")
                print(
                    f"_________________________________________________________________________________"
                    f"________________________________________________________________")
            else:
                if w == n:
                    print(
                        f"_________________________________________________________________________________"
                        f"________________________________________________________________")
                    print(
                        f"                                                   "
                        f"No books available in the library")
                    print(
                        f"_________________________________________________________________________________"
                        f"________________________________________________________________\n")

                else:
                    print(
                        f"_________________________________________________________________________________"
                        f"________________________________________________________________")
                    print(
                        f"                                                   "
                        f"{w - 1} books available in the library")
                    print(
                        f"_________________________________________________________________________________"
                        f"________________________________________________________________\n")

                    if book_name[0] == "#":
                        pass
                    else:
                        book_name = input(
                            f"Enter Book I.D.(Book I.D. should start with # symbol):  ")
                        print()
                        lendbook(book_name, name, username, phone)
