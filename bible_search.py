# imports
import csv
import random

VERSE_ID_INDEX = 0
BOOK_NAME_INDEX = 1
BOOK_NUMBER_INDEX = 2
CHAPTER_INDEX = 3
VERSE_INDEX = 4
TEXT_INDEX = 5


def main():
    # Create a compound list of each verse in the Bible
    kjv_compound_list = read_csv_file("kjv.csv")

    # Get keyword(s) from user
    while True:
        print()
        keywords = input("Enter a word or phrase to search: ")

        # Search the Bible for keyword(s)
        scriptures = find_scriptures(kjv_compound_list, keywords)

        if not scriptures:
            print("Keyword not found. Try again.")
        else:
            break

    # Get keyword count
    count = count_keywords(scriptures, keywords)

    # Display keyword count
    print(
        f'\"{keywords.capitalize()}\" ' 
        f"is found in {count} verses in the Bible."
    )

    # Navigate scriptures including keyword(s)
    # Find books
    books = find_books(scriptures)
    
    while True:
        print()
        print(f'Books including \"{keywords.title()}\":')

        # Display books
        for book in books:
            print(book)

        # Get desired book from user
        print()
        desired_book = input("Select book: ")

        if desired_book.title() not in books:
                print("Book not found. Try again.")
        else:
            break

    # Find chapters
    chapters = find_chapters(scriptures, desired_book)

    while True:
        print()
        print(f'Chapters including \"{keywords.title()}\":')

        # Display chapters
        for chapter in chapters:
            print(chapter)

        # Get desired chapter from user
        print()
        desired_chapter = input("Select chapter: ")

        if desired_chapter not in chapters:
                    print("Chapter not found. Try again.")
        else:
            break

    # Find verses
    verses = find_verses(scriptures, desired_book, desired_chapter)

    while True:
        print()
        print(f'Verses including \"{keywords.title()}\":')

        # Display verses
        for verse in verses:
            print(verse)

        # Get desired verse from user
        print()
        desired_verse = input("Select verse: ")

        if desired_verse not in verses:
                    print("Verse not found. Try again.")
        else:
            break

    # Find verse text
    verse_text = find_text(
        scriptures, desired_book, 
        desired_chapter, 
        desired_verse
    )

    print()
    print(f'Verse including \"{keywords.title()}\":')
    print()

    # Display verse text
    print(f"{desired_book.title()} {desired_chapter}:{desired_verse}")
    print(verse_text)
    print()

    # Get random scripture
    random_scripture = random_scripture_choice(kjv_compound_list)
    
    # Access attributes of random scripture
    random_book = random_scripture[BOOK_NAME_INDEX]
    random_chapter = random_scripture[CHAPTER_INDEX]
    random_verse = random_scripture[VERSE_INDEX]
    random_text = random_scripture[TEXT_INDEX]

    # Print random scripture
    print("Random verse:")
    print()
    print(f"{random_book.title()} {random_chapter}:{random_verse}")
    print(random_text)
    print()


def read_csv_file(filename):
    """Read a CSV file, skip the first line (header), and read the content
    into a compound list.

    Parameter:
        filename: The name of a CSV file.

    Returns:
        compound_list: A list containing lists of verse information in this
        format: [Verse ID, Book Name, Book Number, Chapter,Verse, Text].
    """
    # Create an empty list for scriptures
    compound_list = []

    # Read CSV file
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        # Skip the first line (header)
        next(reader)

        for line in reader:
            compound_list.append(line)

    return compound_list


def find_scriptures(kjv_compound_list, keywords):
    """Search the text content of verses for keyword(s).

    Parameters:
        kjv_compound_list: A compound list of the Bible.
        keywords: Desired keyword(s) from user.

    Returns:
        scriptures: A list containing sciptures that include keyword(s) in
        this format: [Verse ID, Book Name, Book Number, Chapter,Verse, Text].
    """
    # Create an empty list
    scriptures = []

    # Search each verse for keywords
    for verse in kjv_compound_list:
        verse_text = verse[TEXT_INDEX]

        if keywords.lower() in verse_text.lower():
            scriptures.append(verse)

    return scriptures


def count_keywords(scriptures, keywords):
    """Count how many verses include keyword(s)
    
    Parameters:
        scriptures: A list containing sciptures that include keyword(s).
        keywords: Desired keyword(s) from user.

    Returns:
        keyword_count: How many verses include the keyword(s)
    """
    keyword_count = 0
    
    # Count how many verses include keyword(s) 
    for verse in scriptures:
        if keywords.lower() in verse[TEXT_INDEX].lower():
            keyword_count += 1
    
    return keyword_count


def find_books(scriptures):
    """Find books that include the desired keyword(s).

    Parameters:
        scriptures: A list containing sciptures that include keyword(s).

    Returns:
        book: A list of books that contain the desired keyword(s).
    """
    # Create and empty string and empty list
    book_name = ""
    books = []
    
    # Append each book that contains the desired keyword(s)
    for verse in scriptures:
        if verse[BOOK_NAME_INDEX] != book_name:
            book_name = verse[BOOK_NAME_INDEX]
            books.append(book_name)
    
    return books


def find_chapters(scriptures, desired_book):
    """Find chapters in a desired book that include the desired keyword(s).

    Parameters:
        scriptures: A list containing sciptures that include keyword(s).
        desired_book: The book desired by the user.

    Returns:
        chapters: a list of chapters that contain the desired keyword(s).
    """
    # Create and empty string and empty list
    chapter_number = ""
    chapters = []
    
    # Append each chapter that contains the desired keyword(s)
    for verse in scriptures:
        if (
            verse[BOOK_NAME_INDEX].lower() == desired_book.lower() 
            and verse[CHAPTER_INDEX] != chapter_number
        ):
            chapter_number = verse[CHAPTER_INDEX]
            chapters.append(chapter_number)
    
    return chapters


def find_verses(scriptures, desired_book, desired_chapter):
    """Find verses in a desired book and chapter that include the desired
    keyword(s).

    Parameters:
        scriptures: A list containing sciptures that include keyword(s).
        desired_book: The book desired by the user.
        desired_chapter: The chapter desired by the user.

    Returns:
        verses: a list of verses that contain the desired keyword(s).
    """
    # Create and empty string and empty list
    verse_number = -1
    verses = []
    
    # Append each verse that contains the desired keyword(s)
    for verse in scriptures:
        if (
            verse[BOOK_NAME_INDEX].lower() == desired_book.lower() 
            and verse[CHAPTER_INDEX] == desired_chapter
            and verse[VERSE_INDEX] != verse_number
        ):
            verse_number = verse[VERSE_INDEX]
            verses.append(verse_number)
    
    return verses


def find_text(scriptures, desired_book, desired_chapter, desired_verse):
    """Find text in a desired book, chapter, and verse that include the
    desired keyword(s).

    Parameters:
        scriptures: A list containing sciptures that include keyword(s).
        desired_book: The book desired by the user.
        desired_chapter: The chapter desired by the user.
        desired_verse: The verse desired by the user.

    Returns:
        text: a string of the verse text that contain the desired keyword(s).
    """
    verse_text = ""
    # Find the text of the verse that contains the desired keyword(s)
    for verse in scriptures:
        if (
            verse[BOOK_NAME_INDEX].lower() == desired_book.lower()
            and verse[CHAPTER_INDEX] == desired_chapter
            and verse[VERSE_INDEX] == desired_verse
        ):
            verse_text = verse[TEXT_INDEX]
    
    return verse_text


def random_scripture_choice(kjv_compound_list):
    random_scripture = random.choice(kjv_compound_list)

    return random_scripture


if __name__ == "__main__":
    main()