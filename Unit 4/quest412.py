
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}

    gen_translate = " ".join(words[word] for word in sentence.split())

    print(gen_translate)


translate("el gato esta en la casa")