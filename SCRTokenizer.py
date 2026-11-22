from dataclasses import dataclass
from string import digits, ascii_letters, punctuation
from SCRCMD import *
from typing import Any
from decimal import Decimal

ALLOWED_CONCAT_STR_PUNCT = ",():"
ALLOWED_CONCAT_FLOAT_PUNCT = ",():"

@dataclass
class Token:
    type: TokenType
    value: Any = None


def get_token_type_from_string(word : str) -> TokenType:
    word_upper = word.upper()
    if word_upper in SCR_COMMANDS:
        return TokenType.COMMAND
    elif word_upper in SCR_OBJECTS:
        return TokenType.OBJECT
    elif word_upper in SCR_CARS:
        return TokenType.CAR
    elif word_upper in SCR_SOUNDS:
        return TokenType.SOUND
    
    # ...


    else:
        return TokenType.STRING


class Tokenizer:

    def __init__(self, code: str):
        self.code = code
        self.ptr: int = 0
        self.curr_line: int = 1


    def __iter__(self):
        while (token := self.next_token()) != TokenType.EOF:
            yield token
        yield token     # also yield the end of line
    
    def peek(self):
        """Get the next char without pushing the pointer. Return 0 if gets EOF."""
        if self.ptr != len(self.code):
            return self.code[self.ptr]
        else:
            return 0

    def next_token(self) -> Token:

        while self.ptr < len(self.code) and self.code[self.ptr].isspace():
            self.ptr += 1

        one_line_comment = False
        scope_comment = False

        while True:
        
            if self.ptr == len(self.code):
                return Token(TokenType.EOF)
            
            char = self.code[self.ptr]
            self.ptr += 1

            if char == '\n':
                self.curr_line += 1
                if one_line_comment:
                    one_line_comment = False

            # comment stuff

            if scope_comment:
                if char == '*' and self.peek() == '/':
                    scope_comment = False
                    continue

            if char == '/' and self.peek() == '/':
                one_line_comment = True

            if char == '/' and self.peek() == '*':
                scope_comment = True
            
            if one_line_comment or scope_comment:
                continue

            # punctuation chars

            if char == ",":
                return Token(TokenType.COMMA)
            
            if char == "(":
                return Token(TokenType.OPEN_BRACKET)
            
            if char == ")":
                return Token(TokenType.CLOSE_BRACKET)
            
            if char == "=":
                return Token(TokenType.EQUAL)
            
            if char == "+":
                return Token(TokenType.PLUS)
            
            if char == "-":
                return Token(TokenType.MINUS)
            
            if char == ":":
                return Token(TokenType.COLON)
            
            # digits and letters (numbers and strings)
            
            if char in digits:      # can be both integer or float

                number_str = f"{char}"
                while self.ptr < len(self.code) and not (self.code[self.ptr].isspace() or self.code[self.ptr] in ALLOWED_CONCAT_FLOAT_PUNCT):
                    number_str += f"{self.code[self.ptr]}"
                    self.ptr += 1

                for punct in punctuation:
                    if punct != '.' and punct in number_str:
                        raise Exception(f"Invalid number on line {self.curr_line}: '{number_str}'")
                    
                for letter in ascii_letters:
                    if letter in number_str:
                        raise Exception(f"Invalid number on line {self.curr_line}: '{number_str}'")
                
                if number_str.count('.') == 1:
                    return Token(TokenType.FLOAT, Decimal(number_str))
                elif number_str.count('.') > 1:
                    raise Exception(f"Invalid float on line {self.curr_line}: '{number_str}'")
                else:
                    return Token(TokenType.INT, int(number_str))
                
            
            elif char in ascii_letters:

                word_str = f"{char}"
                while self.ptr < len(self.code) and not (self.code[self.ptr].isspace() or self.code[self.ptr] in ALLOWED_CONCAT_STR_PUNCT):
                    word_str += f"{self.code[self.ptr]}"
                    self.ptr += 1

                for punct in punctuation:
                    if punct != '_' and punct in word_str:
                        raise Exception(f"Invalid string on line {self.curr_line}: '{word_str}'")

                word_str = word_str.strip()

                return Token(get_token_type_from_string(word_str), word_str)
            