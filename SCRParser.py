from SCRTokenizer import Tokenizer, TokenType, Token
from dataclasses import dataclass

class Parser:

    def __init__(self, tokens : list[Token]):
        self.tokens = tokens
        self.next_token_idx = 0    # pointer to the next token to be consumed

    def peek(self, skip: int = 0) -> TokenType | None:
        peek_at = self.next_token_idx + skip
        if peek_at < len(self.tokens):
            return self.tokens[peek_at]
        else:
            return None
        
    def eat(self, expected_token_type: TokenType) -> Token:
        """Return the next token if it's of a expected type. Raise an error otherwise."""
        next_token = self.tokens[self.next_token_idx]
        self.next_token_idx += 1
        if next_token.type != expected_token_type:
            raise RuntimeError(f"Expected {expected_token_type} type, but ate {next_token!r}.")
        return next_token

    def parse(self):
        pass