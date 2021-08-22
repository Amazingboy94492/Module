def check_if_return_true(wtcfr):
    if "return" in wtcfr:
        return True
    else:
        return False

def statement(*args):
    operator = args[len(args) - 2]
    wtdit = args[len(args) - 1]
    if operator == "==":
        if args[0] == args[1]:
            if check_if_return_true(wtdit) == True:
                return wtdit[7:]
            else:
                exec(wtdit)
    elif operator == ">=":
        if args[0] >= args[1]:
            if check_if_return_true(wtdit) == True:
                return wtdit[7:]
            else:
                exec(wtdit)
    elif operator == "<=":
        if args[0] <= args[1]:
            if check_if_return_true(wtdit) == True:
                return wtdit[7:]
            else:
                exec(wtdit)
    elif operator == "!=":
        if args[0] != args[1]:
            if check_if_return_true(wtdit) == True:
                return wtdit[7:]
            else:
                exec(wtdit)
    else:
        Script.OP.Alert("unsupported operator in{def statement(*args):\}>>>}")
        Script.OP.Alert("NoRe function type                    '^\n\'")
        Script.OP.Alert("Fake Error{would\' 'happen\' 'real{under\' 'condition(s)} in /'TypeError: unsupported operator in{def statement(*args):\}>>>}/\/n\/\'")
        Script.OP.Alert("after def\' ' unepected indent after{def}")
        Script.OP.Alert("Mainloop Failed: Exiting Execution")
        Script.OP.Alert("Incalable")
        Script.OP.Alert("Unable to exit user useless input error")
        Script.OP.Warning("")
