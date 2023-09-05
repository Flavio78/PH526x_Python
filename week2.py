#!/usr/bin/python3

"""test example
"""

import sys


class MyList(list):
    """example of class

    Args:
        list (_type_): inheritated class
    """

    def remove_min(self):
        self.remove(min(self))

    def remove_max(self):
        self.remove(max(self))


def update(n: int, x: list) -> None:
    """update function

    Args
        n(int):
        x(list):

    Returns
        None: function returns no value
    """
    print("Start of function 'update'")

    # +++your code here+++
    n = 2
    x.append(4)
    print("update:", n, x)

    print("End of function 'update'")


def main() -> None:
    """Main function()

    Args
        None: this function requires no value

    Returns
        None: this function returns no value
    """
    print("Start of program")

    if len(sys.argv) > 1:
        print(f"First argument: {sys.argv[1]}")
    # +++your code here+++
    n = 1
    x = [0, 1, 2, 3]
    print("main: ", n, x)
    update(n, x)
    print("main: ", n, x)
    print("End of program")


if __name__ == "__main__":
    main()
