import csv
import pytest
import random

# VERSE_ID_INDEX = 0
BOOK_NAME_INDEX = 1
BOOK_NUMBER_INDEX = 2
CHAPTER_INDEX = 3
VERSE_INDEX = 4
TEXT_INDEX = 5


def main():
    # Create a compound list of each verse in the Bible
    kjv_compound_list = read_csv_file("kjv.csv")

    # Get keyword(s) from user
    keywords = input("Enter a word or phrase to search: ")

    # Search the Bible for keyword(s)
    scriptures = find_scriptures(kjv_compound_list, keywords)

    print(scriptures)


def read_csv_file(filename):
    """Read a CSV file, skip the first line, and append 
    each line to a list
    Parameter: csv filename
    Return: a compound list
    """
    # Create an empty list
    compound_list = []

    # Read CSV file
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        # Skip the first line (header)
        next(reader)

        for line in reader:
            compound_list.append(line)

    # Return compound list
    return compound_list


def find_scriptures(kjv_compound_list, keywords):
    """Search for keyword(s) within a compound list
    Parameters:
        compound list
        keyword(s)
    Return: a list of scriptures that 
    include keyword(s)
    """
    # Create an empty list
    scriptures = []

    # Search each verse for keywords
    for verse in kjv_compound_list:
        verse_text = verse[TEXT_INDEX]

        if keywords.lower() in verse_text.lower():
            scriptures.append(verse)

    return scriptures


def navigate_scriptures():
    pass


def random_scripture():
    pass


if __name__ == "__main__":
    main()