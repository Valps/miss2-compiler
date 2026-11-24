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
    id: int = None

def get_index_from_array(value, array : list):
    try:
        return array.index(value)
    except ValueError:
        return None


def get_token_type_from_string(word : str) -> TokenType:
    word_upper = word.upper()

    id = None

    if (id := get_index_from_array(word_upper, SCR_COMMAND_KEYWORDS)) is not None:
        return (TokenType.COMMAND, id)
    elif (id := get_index_from_array(word_upper, SCR_OBJECTS)) is not None:
        return (TokenType.OBJECT, id)
    elif (id := get_index_from_array(word_upper, SCR_CARS)) is not None:
        return (TokenType.CAR, id)
    elif (id := get_index_from_array(word_upper, SCR_SOUNDS)) is not None:
        return (TokenType.SOUND, id)
    elif (id := get_index_from_array(word_upper, SCR_OBJECTIVES)) is not None:
        return (TokenType.OBJECTIVE, id)
    elif (id := get_index_from_array(word_upper, SCR_OCCUPATIONS)) is not None:
        return (TokenType.OCCUPATION, id)
    elif (id := get_index_from_array(word_upper, SCR_DAMAGE_TYPE)) is not None:
        return (TokenType.DAMAGE_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_WEAPONS)) is not None:
        return (TokenType.WEAPON, id)
    elif (id := get_index_from_array(word_upper, SCR_RADIO_STATIONS)) is not None:
        return (TokenType.RADIO_STATION, id)
    elif (id := get_index_from_array(word_upper, SCR_TRAIN_TYPE)) is not None:
        return (TokenType.TRAIN_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_THREAT_SEARCH_TYPE)) is not None:
        return (TokenType.THREAT_SEARCH_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_THREAT_REACTION_TYPE)) is not None:
        return (TokenType.THREAT_REACTION_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_LOCKS)) is not None:
        return (TokenType.CAR_DOOR_LOCK, id)
    elif (id := get_index_from_array(word_upper, SCR_GROUP_FOLLOW_TYPE)) is not None:
        return (TokenType.GROUP_FOLLOW_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_EXCLUSIVE)) is not None:
        return (TokenType.EXCLUSIVE, id)
    elif (id := get_index_from_array(word_upper, SCR_COLOURS)) is not None:
        return (TokenType.COLOUR, id)
    elif (id := get_index_from_array(word_upper, SCR_CHAR_OVERLAY)) is not None:
        return (TokenType.CHAR_OVERLAY, id)
    elif (id := get_index_from_array(word_upper, SCR_BRAVERY)) is not None:
        return (TokenType.BRAVERY, id)
    elif (id := get_index_from_array(word_upper, SCR_BONUS_TYPE)) is not None:
        return (TokenType.BONUS_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_BONUS_WHICH)) is not None:
        return (TokenType.BONUS_WHICH, id)
    elif (id := get_index_from_array(word_upper, SCR_ACCURACY)) is not None:
        return (TokenType.ACCURACY, id)
    elif (id := get_index_from_array(word_upper, SCR_SOUND_PLAY_TYPE)) is not None:
        return (TokenType.SOUND_PLAY_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_CAR_DAMAGE_POS)) is not None:
        return (TokenType.CAR_DAMAGE_POS, id)
    elif (id := get_index_from_array(word_upper, SCR_DROPS)) is not None:
        return (TokenType.BLOCK_DROP, id)
    elif (id := get_index_from_array(word_upper, SCR_ROTATION_LIST)) is not None:
        return (TokenType.ROTATION_LIST, id)
    elif (id := get_index_from_array(word_upper, SCR_BULLETWALL_TYPES)) is not None:
        return (TokenType.BULLETWALL_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_WALL_TYPES)) is not None:
        return (TokenType.WALL_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_BLOCK_TYPES)) is not None:
        return (TokenType.BLOCK_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_BLOCK_FLAT_TYPES)) is not None:
        return (TokenType.BLOCK_FLAT_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_BLOCK_FLIP_TYPES)) is not None:
        return (TokenType.BLOCK_FLIP_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_ON_OFF)) is not None:
        return (TokenType.ON_OFF, id)
    elif (id := get_index_from_array(word_upper, SCR_CRANE_TYPES)) is not None:
        return (TokenType.CRANE_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_DOOR_REVERSED)) is not None:
        return (TokenType.DOOR_REVERSED, id)
    elif (id := get_index_from_array(word_upper, SCR_DOOR_FLIP_TYPES)) is not None:
        return (TokenType.DOOR_FLIP_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_DOOR_CLOSE_TYPES)) is not None:
        return (TokenType.DOOR_CLOSE_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_DOOR_OPEN_TYPES)) is not None:
        return (TokenType.DOOR_OPEN_TYPE, id)
    elif (id := get_index_from_array(word_upper, SCR_BLOCK_FACES)) is not None:
        return (TokenType.BLOCK_FACE, id)

    else:
        return (TokenType.STRING, None)


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

                token_type, scr_id = get_token_type_from_string(word_str)
                return Token(token_type, word_str, scr_id)
            