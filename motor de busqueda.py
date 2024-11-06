def search(text, word):
    lower_text = text.lower()
    lower_word = word.lower()

    if lower_word in lower_text:
        return "Word found"
    else:
        return "Word not found"
    
text = input()
word = input()

print(search(text, word))