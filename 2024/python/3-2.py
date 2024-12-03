from enum import Enum
import re

input_txt = open("3.txt").read()


sum = 0

enabled = True


class Number:
    value: int


class Token(Enum):
    MUL = 1
    DO = 2
    DONT = 3
    NUMBER = Number
    COMMA = 5
    OPEN_PAREN = 6
    CLOSE_PAREN = 7


i = 0

tokens = []

length = len(input_txt)

while i < length:
    if input_txt[i : i + 3] == "mul":
        tokens.append(Token.MUL)
        i += 3
    elif input_txt[i : i + 4] == "do()":
        tokens.append(Token.DO)
        i += 4
    elif input_txt[i : i + 7] == "don't()":
        tokens.append(Token.DONT)
        i += 7
    elif input_txt[i] == ",":
        tokens.append(Token.COMMA)
        i += 1
    elif input_txt[i] == "(":
        tokens.append(Token.OPEN_PAREN)
        i += 1
    elif input_txt[i] == ")":
        tokens.append(Token.CLOSE_PAREN)
        i += 1
    elif input_txt[i].isdigit():
        j = i + 1
        while j < length and input_txt[j].isdigit():
            j += 1
        token = Token.NUMBER.value.value = int(input_txt[i:j])
        tokens.append(token)
        i = j
    else:
        i += 1


in_mul = False

i = 0

while i < len(tokens):
    if (
        tokens[i] == Token.MUL
        and tokens[i + 1] == Token.OPEN_PAREN
        and isinstance(tokens[i + 2], int)
        and tokens[i + 3] == Token.COMMA
        and isinstance(tokens[i + 4], int)
        and tokens[i + 5] == Token.CLOSE_PAREN
    ):
        if enabled:
            sum += tokens[i + 2] * tokens[i + 4]
        i += 6
    elif tokens[i] == Token.DO:
        enabled = True
        i += 1
    elif tokens[i] == Token.DONT:
        enabled = False
        i += 1
    else:
        i += 1


print(sum)
