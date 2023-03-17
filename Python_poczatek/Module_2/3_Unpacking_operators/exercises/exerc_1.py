def connection_writting(*args):
    sentences = ""
    for words in args:
        sentences += str(words)
        sentences += "-"
    return sentences[:-1]