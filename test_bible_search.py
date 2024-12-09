import pytest
from bible_search import find_scriptures, \
count_keywords, find_books, find_chapters, \
find_verses, find_text

test_scriptures = [
    [1,"Genesis",1,1,1,"¶ In the beginning God created the heaven and the earth."],
    [22403,"Amos",30,3,7,"Surely the Lord GOD will do nothing, but he revealeth his secret unto his servants the prophets."],
    [26137,"John",43,3,16,"‹For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.›"],
    [28741,"1 Corinthians",46,15,22,"For as in Adam all die, even so in Christ shall all be made alive."]
]


def test_find_scriptures():
    """Verify that the find_scriptures function works correctly.
    Parameters: none
    Return: nothing
    """
    keyword1 = "God"
    keyword2 = "god"
    keyword3 = "God created"
    
    scriptures1 = find_scriptures(test_scriptures, keyword1)
    assert scriptures1 == [
        [1,"Genesis",1,1,1,"¶ In the beginning God created the heaven and the earth."],
        [22403,"Amos",30,3,7,"Surely the Lord GOD will do nothing, but he revealeth his secret unto his servants the prophets."],
        [26137,"John",43,3,16,"‹For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.›"]
    ]
    scriptures2 = find_scriptures(test_scriptures, keyword2)
    assert scriptures2 == [
        [1,"Genesis",1,1,1,"¶ In the beginning God created the heaven and the earth."],
        [22403,"Amos",30,3,7,"Surely the Lord GOD will do nothing, but he revealeth his secret unto his servants the prophets."],
        [26137,"John",43,3,16,"‹For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.›"]
    ]
    scriptures3 = find_scriptures(test_scriptures, keyword3)
    assert scriptures3 == [
        [1,"Genesis",1,1,1,"¶ In the beginning God created the heaven and the earth."]
    ]


def test_count_keywords():
    """Verify that the count_keywords_scriptures function works correctly.
    Parameters: none
    Return: nothing
    """
    keyword1 = "God"
    keyword2 = "god"
    keyword3 = "God created"

    count1 = count_keywords(test_scriptures, keyword1)
    assert count1 == 3

    count2 = count_keywords(test_scriptures, keyword2)
    assert count2 == 3

    count3 = count_keywords(test_scriptures, keyword3)
    assert count3 == 1


def test_find_books():
    """Verify that the find_books function works correctly.
    Parameters: none
    Return: nothing
    """
    books1 = find_books(test_scriptures)
    assert books1 == ["Genesis", "Amos", "John", "1 Corinthians"]

    books2 = find_books([])
    assert books2 == []


def test_find_chapters():
    """Verify that the find_chapters function works correctly.
    Parameters: none
    Return: nothing
    """
    book1 = "Genesis"
    book2 = "Amos"
    book3 = "John"

    chapters1 = find_chapters(test_scriptures, book1)
    assert chapters1 == [1]

    chapters2 = find_chapters(test_scriptures, book2)
    assert chapters2 == [3]

    chapters3 = find_chapters(test_scriptures, book3)
    assert chapters3 == [3]


def test_find_verses():
    """Verify that the find_verses function works correctly.
    Parameters: none
    Return: nothing
    """
    desired_book1 = "Genesis"
    desired_book2 = "Amos"
    desired_book3 = "John"

    desired_chapter1 = 1
    desired_chapter2 = 3
    desired_chapter3 = 3

    verses1 = find_verses(test_scriptures, desired_book1, desired_chapter1)
    assert verses1 == [1]

    verses2 = find_verses(test_scriptures, desired_book2, desired_chapter2)
    assert verses2 == [7]

    verses3 = find_verses(test_scriptures, desired_book3, desired_chapter3)
    assert verses3 == [16]


def test_find_text():
    """Verify that the find_text function works correctly.
    Parameters: none
    Return: nothing
    """
    desired_book1 = "Genesis"
    desired_book2 = "Amos"
    desired_book3 = "John"

    desired_chapter1 = 1
    desired_chapter2 = 3
    desired_chapter3 = 3

    desired_verse1 = 1
    desired_verse2 = 7
    desired_verse3 = 16

    verse_text1 = find_text(test_scriptures, desired_book1, desired_chapter1, desired_verse1)
    assert verse_text1 == "¶ In the beginning God created the heaven and the earth."

    verse_text2 = find_text(test_scriptures, desired_book2, desired_chapter2, desired_verse2)
    assert verse_text2 == "Surely the Lord GOD will do nothing, but he revealeth his secret unto his servants the prophets."

    verse_text3 = find_text(test_scriptures, desired_book3, desired_chapter3, desired_verse3)
    assert verse_text3 == "‹For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.›"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])