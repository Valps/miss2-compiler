from SCRTokenizer import Tokenizer, TokenType, Token
from SCRGrammar import SCR_TOKEN_RULES_STR
from dataclasses import dataclass


def get_grammar() -> list[list[Token]]:
    grammar_list = []
    for pattern in SCR_TOKEN_RULES_STR:
        grammar_list.append(list(Tokenizer(pattern))[:-1])
    
    return grammar_list





class Parser:

    def __init__(self, tokens : list[Token]):
        self.tokens = tokens
        self.next_token_idx = 0    # pointer to the next token to be consumed
        self.rules = get_grammar()

    def peek(self, skip: int = 0) -> TokenType | None:
        peek_at = self.next_token_idx + skip
        if peek_at < len(self.tokens):
            return self.tokens[peek_at]
        else:
            return None
        
    def eat(self, expected_token_types: list[TokenType]) -> Token:
        """Return the next token if it's of a expected type. Raise an error otherwise."""
        next_token = self.tokens[self.next_token_idx]
        #self.next_token_idx += 1       # do this later depending on the pattern found
        if next_token.type not in expected_token_types:
            types_expected = [ str(token_type) for token_type in expected_token_types ]
            raise RuntimeError(f"Expected {", ".join(types_expected)} types, but ate {next_token!r}.")
        return next_token
    

    def search_for_default_pattern(self, command : Token, start_idx : int = 0, end_idx : int = -1):
        """Default pattern: Command, and then stuff"""

        if end_idx == -1:
            rules_list = self.rules[start_idx : ]
        else:
            rules_list = self.rules[start_idx : end_idx]

        i = start_idx

        for pattern in rules_list:

            if command.type == pattern[0].type: # first token must be an opcode/command
                return (pattern, i)

            i += 1

        raise RuntimeError(f"Pattern not found for command {command.value}")
            


    def parse(self):
        
        finished = False
        while not finished:
            
            curr_token = self.eat([TokenType.COMMAND, TokenType.STRING])

            if curr_token.type == TokenType.COMMAND:
                
                start_idx = 0
                while True:
                    pattern = self.search_for_default_pattern(curr_token, start_idx)
                    

            elif curr_token.type == TokenType.STRING:
                if self.peek(1).type == TokenType.EQUAL and self.peek(2).type == TokenType.COMMAND:
                    # CREATE_CHAR
                    # CREATE_CHAR_INSIDE_CAR
                    # CREATE_SOUND etc
                    pass
                elif self.peek(1).type == TokenType.COLON:
                    # function
                    pass
                else:
                    raise RuntimeError(f"Expected 'EQUAL' type, but found {self.peek(1).type!r}.")
                
            
