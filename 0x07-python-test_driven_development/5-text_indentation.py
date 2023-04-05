#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters '.', '?', and ':'
    Args:
        text: input string to be formatted
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = []
    current_sentence = ""
    for i, char in enumerate(text):
        if char in [".", "?", ":" ]:
            current_sentence += char
            sentences.append(current_sentence.strip())
            current_sentence = ""
        else:
            current_sentence += char

    if current_sentence:
        sentences.append(current_sentence.strip())

    print("\n\n".join(sentences))

