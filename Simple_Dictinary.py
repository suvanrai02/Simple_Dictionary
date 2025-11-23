import os
import csv
import time

fileName = "words.csv"

def loadfile():
    stuff = {}

    if os.path.exists(fileName):
        try:
            f = open(fileName, "r", encoding="utf-8")
            r = csv.reader(f)

            for row in r:
                if len(row) == 3:
                    w = row[0]
                    meaning = row[1]
                    tags = row[2].split(";")
                    stuff[w] = {"meaning": meaning, "tags": tags}
            f.close()
        except:
            print("Couldn't read the file properly")
    return stuff


def savefile(allwords):
    try:
        f = open(fileName, "w", encoding="utf-8", newline="")
        w = csv.writer(f)

        for word in allwords:
            info = allwords[word]
            tg = ";".join(info["tags"])
            w.writerow([word, info["meaning"], tg])
        f.close()
    except:
        print("Couldn't save... something went wrong")


def addword(d):
    print("Add New Word")
    word = input("Word: ")
    meaning = input("Meaning: ")

    tagtext = input("Tags (comma separated): ")
    if tagtext.strip() == "":
        tlist = []
    else:
        tlist = [x.strip() for x in tagtext.split(",")]

    d[word] = {"meaning": meaning, "tags": tlist}
    savefile(d)

    print("Saved!\n")


def find(d):
    print("Search Words")
    key = input("Search: ").lower()
    got = False

    for w in d:
        info = d[w]
        if key in w.lower() or key in info["meaning"].lower():
            print(w)
            print("Meaning:", info["meaning"])
            print("Tags:", info["tags"])
            print()
            got = True

    if not got:
        print("Nothing matched.\n")


def showall(d):
    print("All Words")
    if len(d) == 0:
        print("No words saved yet.\n")
        return

    for w in d:
        x = d[w]
        print("Word:", w)
        print("Meaning:", x["meaning"])
        print("Tags:", ", ".join(x["tags"]))
        print()


def main():
    data = loadfile()

    while True:
        print("1. Add word")
        print("2. Search word")
        print("3. Show all")
        print("4. Exit\n")

        c = input("Choose: ")

        if c == "1":
            addword(data)
        elif c == "2":
            find(data)
        elif c == "3":
            showall(data)
        elif c == "4":
            print("Goodbye")
            time.sleep(1)
            break
        else:
            print("Invalid option\n")


main()