def connection_writting(*args):
    sentences = ""
    for words in args:
        sentences += words
        sentences += "-"
    return sentences