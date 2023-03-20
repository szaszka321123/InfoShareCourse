def named_arguments(**kwargs):
    result = ""
    for named, arguments in kwargs.items():
        print(named + "=" + str(arguments))
    return result

def print_call_str(**kwargs):
    call_str = "print_call_str("
    for argument_name, argument_value in kwargs.items():
        call_str += f"{argument_name}={argument_value}, "
    call_str += ")"
    print(call_str)
