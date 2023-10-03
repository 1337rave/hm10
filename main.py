text = input("Enter a text: ")
sentences = text.split(".") + text.split("!") + text.split("?")
num_sentences = len(sentences)
print("Number of sentences: ", num_sentences)
