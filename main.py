# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    s = 'BLUETEST IS FUN'

    t = s[0:12]
    cp = [71, 82, 69, 65, 84]
    for c in cp:
        t += chr(c)

    u = ''
    for c in s:
        u = c + u
    print(u)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
