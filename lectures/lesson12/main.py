from typing import Optional, Union


def divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    try:
        100+100
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except TypeError:
        print("check variable types!")
    else:
        print("blabla")
    finally:
        print('Executing finally clause')

    return "laba diena"

print(divide(1, 0))