#!/usr/bin/python3
"""
Module 5-text_indentation
Prints a text using a specific format.
"""


def text_indentation(text):
    """Prints a text in a specific format.

    Args:
        text (str): input string.
    Returns:
        Nothing
    """
    # INPUT TYPE CHECK
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # ACTUAL PRINTING
    pattern = ".,?:"
    for _ in pattern:
        text = text.replace(_, _ + ("\n" * 2))
    sentences = [x.strip() for x in text.split("\n")]
    # PUT \n AT END OF EACH SENTENCE AND PRINT
    print("\n".join(sentences), end="")
    return None


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/5-text_indentation.txt")
