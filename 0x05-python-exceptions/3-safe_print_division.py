#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        pass
    else:
        return result
    finally:
        print("Inside result: {}".format(result))
    return None
