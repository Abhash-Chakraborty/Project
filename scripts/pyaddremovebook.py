import pickle
import os
from required import pynogen
import datetime


def addbook():
    with open("assets\\files\\booklist.dat", "ab") as f:
        bookid = pynogen.bookid()
        bname = input("Enter book name:")
        author = input("Enter author name:")
        wfee = int(input("Enter weekly fees:"))
        mfee = int(input("Enter monthly fees:"))
        file = input("Do you want to add pdf of the book[y/n]? ")
        if file == "y" or file == "Y":
            bookpath = input("Enter book source path: ")
            bookdir = f"assets\\books\\{bookid}.pdf"
            os.system(f"copy {bookpath} {bookdir}")
            l1 = [bookid, bname.upper(), author.upper(), wfee, mfee, "Yes"]
            l2 = [bookid, bname.upper(), author.upper(), wfee, mfee, "Admin", "Added(pdf)", 9632587415,
                  datetime.date.today()]
        else:
            l1 = [bookid, bname.upper(), author.upper(), wfee, mfee, "No"]
            l2 = [bookid, bname.upper(), author.upper(), wfee, mfee, "Admin", "Added", 9632587415, datetime.date.today()]
        pickle.dump(l1, f)
        with open("assets\\files\\libbookdet.dat", "ab") as y:
            pickle.dump(l2, y)
        print(f"operation completed successfully. Book Id is {bookid}.")


def removebook():
    with open("assets\\files\\booklist.dat", "rb") as f:
        bookid = input("Enter Book Id: ")
        bookdir = f"assets\\books\\{bookid}.pdf"
        lostdir = f"lost.dir"
        s = 0
        l = []
        l2 = []
        try:
            while True:
                p = pickle.load(f)
                if bookid != p[0]:
                    l.append(p)
                else:
                    l2 = p
                    l2.append("Admin")
                    l2.append("Removed")
                    l2.append(9632587415)
                    l2.append(datetime.date.today())
                    s += 1
        except Exception:
            if s == 0:
                print("No book is found")
            elif s == 1:
                with open("assets\\files\\libbookdet.dat", "ab") as y:
                    pickle.dump(l2, y)
                print("One book is removed")
            else:
                with open("assets\\files\\libbookdet.dat", "ab") as y:
                    pickle.dump(l2, y)
                print("Multiple books are removed")
            try:
                os.system(f"move {bookdir} {lostdir}")
            except Exception:
                pass
            with open("assets\\files\\temp.dat", "wb") as q:
                for i in l:
                    pickle.dump(i, q)
    os.remove("assets\\files\\booklist.dat")
    os.rename("assets\\files\\temp.dat", "assets\\files\\booklist.dat")
    print("Operation completed successfully.")


def donation():
    con = input("Do you want to continue[y/n]?")
    if con == "y" or con == "Y":
        with open("assets\\files\\booklist.dat", "ab") as f:
            print(f"\n+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+\n"
                  f"|W|E|L|C|O|M|E| |T|O| |D|O|N|A|T|I|O|N| |B|O|X|\n"
                  f"+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+\n")
            bookid = pynogen.bookid()
            bname = input("Enter book name:")
            author = input("Enter author name:")
            name = input("Enter your full name:")
            phone = int(input("Enter your phone no.:"))
            file = input("Do you want to add pdf of the book[y/n]? ")
            if file == "y" or file == "Y":
                bookpath = input("Enter book source path: ")
                bookdir = f"assets\\books\\{bookid}.pdf"
                os.system(f"copy {bookpath} {bookdir}")
                l1 = [bookid, bname.upper(), author.upper(), "Free", "Free", "Yes"]
                l2 = [bookid, bname.upper(), author.upper(), "Free", "Free", name, "Added(pdf)", phone, datetime.date.today()]
            else:
                l1 = [bookid, bname.upper(), author.upper(), "Free", "Free", "No"]
                l2 = [bookid, bname.upper(), author.upper(), "Free", "Free", name, "Added", phone, datetime.date.today()]
            pickle.dump(l1, f)
            with open("assets\\files\\libbookdet.dat", "ab") as y:
                pickle.dump(l2, y)
            print(f"operation completed successfully. Book Id is {bookid}.")
            print("Thanking you for your contribution.")
        pass
    else:
        pass
