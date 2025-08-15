import re


if __name__ == "__main__":
    string = "ahoj světe"
    match = re.finditer(r"oj", string)
    for m in match:
        print(m.span())
        print(m.start())
        print(m.end()-1)
    for i, c in enumerate(string):
        print(i, c)