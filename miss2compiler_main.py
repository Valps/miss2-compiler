from SCRTokenizer import Tokenizer, TokenType
from SCRGrammar import SCR_TOKEN_RULES_STR
from SCRCMD import SCR_COMMAND_KEYWORDS, SCR_COMMANDS_TM     # debug only
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

TEST_CODE = """IF ( ( ( ( ( ( ( ( ( ( CHECK_WEAPON_TYPE_HIT_CAR(r_m_1_cortez_limo_car, BY_EXPLOSION) )
										OR ( CHECK_WEAPON_TYPE_HIT_CAR(r_m_1_cortez_limo_car, BY_GUN) ) )
										OR ( CHECK_WEAPON_TYPE_HIT_CAR(r_m_1_cortez_limo_car, BY_FLAMETHROWER) ) )
										OR ( CHECK_WEAPON_TYPE_HIT_CAR(r_m_1_cortez_limo_car, BY_GRENADE) ) )
										OR ( CHECK_WEAPON_TYPE_HIT_CAR(r_m_1_cortez_limo_car, BY_MOLOTOV) ) )
										OR ( CHECK_WEAPON_TYPE_HIT_CAR(r_m_1_cortez_limo_car, BY_ROCKET_LAUNCHER) ) )
										OR ( CHECK_WEAPON_TYPE_HIT_CAR(r_m_1_cortez_limo_car, BY_ELECTRO_WEAPON) ) )
										OR ( CHECK_WEAPON_TYPE_HIT_CAR(r_m_1_cortez_limo_car, BY_ROCKET_LAUNCHER) ) )
										OR ( CHECK_WEAPON_TYPE_HIT_CAR(r_m_1_cortez_limo_car, BY_ELECTRO_WEAPON) ) )
										OR ( CHECK_WEAPON_TYPE_HIT_CAR(r_m_1_cortez_limo_car, BY_SHOTGUN) ) )"""

TEST_CODE = "PLAYER_PED p1 = (108.5,150.5,255.0) 0 1"

TEST_CODE = "WHILE_EXEC ( ( NOT ( IS_CHAR_PRESSING_HORN(p1) ) ) OR ( player_fit_conditions = 0 ) )"

def test_tokenizer(code : str):
    list_of_tokens = Tokenizer(code)
    for token in list_of_tokens:

        if token.type == TokenType.STRING or token.type == TokenType.INT or token.type == TokenType.FLOAT or token.type == TokenType.COMMAND:
            print(token.value, end=" ")
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



def get_grammar():
    grammar_list = []
    for pattern in SCR_TOKEN_RULES_STR:
        grammar_list.append(list(Tokenizer(pattern))[:-1])
    
    return grammar_list


def test_grammar():
    grammar_list = get_grammar()
    for pattern in grammar_list:
        #print([token.value if token.value is not None else str(token.type) for token in pattern])
        print([str(token.type) for token in pattern])

def main():
    #TEST_CODE = "-5"
    #test_tokenizer(TEST_CODE)
    #tokenize_mis_file()
    #num = 120
    print(SCR_TOKEN_RULES_STR[-1])
    print(SCR_COMMANDS_TM[len(SCR_TOKEN_RULES_STR) - 1 + 5])



if __name__ == "__main__":
    main()