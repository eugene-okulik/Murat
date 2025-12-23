text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
words = text.split()
text_ing = []
for word in words:
    if word.endswith('.') or word.endswith(','):
        znak = word[-1]
        word_ing = word[:-1] + 'ing' + znak
        text_ing.append(word_ing)
    else:
        word_ing = word + 'ing'
        text_ing.append(word_ing)
print(' '.join(text_ing))
