from SCRTokenizer import Tokenizer, TokenType
from pathlib import Path


ROOT_FOLDER = Path(__file__).parent





TEST_CODE = """PLAYER_PED p1 = (97.50, 73.50, 2.00) 5 1
PLAYER_PED p2 = (150.50, 68.50, 2.00) 7 1"""

TEST_CODE = """IF ( HAS_CHAR_BEEN_ARRESTED(p1) )
   CLEAR_ALL_BRIEFS ()
   DISPLAY_BRIEF_NOW (1609)   //  "That wasn't so smart, now was it"
   SET flag_failed_mission = 1
   SET flag_failed_tutorial = 1
   RETURN
 ENDIF"""

def test_tokenizer():
    list_of_tokens = Tokenizer(TEST_CODE)
    for token in list_of_tokens:

        if token.type == TokenType.STRING or token.type == TokenType.INT or token.type == TokenType.FLOAT:
            print(token.type, end=" ")
        else:
            print(token.type, end=" ")

        if token.type == TokenType.EOF:
            break

FILENAME = "wil_ye2.mis"
miss2_test_file = ROOT_FOLDER / "sample" / FILENAME

def tokenize_mis_file():
    if miss2_test_file.exists():
        code = str()
        with open(str(miss2_test_file), "r") as file:
            code = file.read()

        list_of_tokens = Tokenizer(code)
        num = 0
        for token in list_of_tokens:
            num += 1
            if token.type == TokenType.EOF:
                break
        print(f"Total tokens: {num}")
        
    else:
        print(f"File not found: {miss2_test_file}")




def main():
    test_tokenizer()
    #tokenize_mis_file()

if __name__ == "__main__":
    main()