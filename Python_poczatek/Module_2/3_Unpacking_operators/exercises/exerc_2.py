def named_arguments(**kwargs):
    result = ""
    for named, arguments in kwargs.items():
        print(named + "=" + str(arguments))
    return result