# Based on SCR_COMMANDS_TM

SCR_TOKEN_RULES_STR = [
    "PLAYER_PED p1 = (25.5, 25.5, 2.0) 0 0",
    "CHAR_DATA my_char",
    "CHAR_DATA mugger_one = (123.4, 23.2) 0 180 MUGGER",
    "CHAR_DATA just_a_dummy = (4.4, 110.5, 4.0) 3 45 DUMMY",
    "CAR_DATA name",
    "CAR_DATA name = (25.0, 25.0) 0 180 TANK",
    "CAR_DATA name = (25.0, 25.0, 2.0) 0 180 TANK",
    "CAR_DATA name = (25.0, 25.0) 0 180 TRUKCAB2 TANKER",
    "CAR_DATA name = (25.0, 25.0, 2.0) 0 180 TRUKCAB2 TANKER",
    "OBJ_DATA name",
    "OBJ_DATA football = (10.5, 127.5) 0 FOOTY",
    "OBJ_DATA football = (10.5, 127.5, 2.0) 0 FOOTY",
    "OBJ_DATA football = (10.5, 127.5) 0 CAR_SHOP 5",
    "OBJ_DATA football = (10.5, 127.5, 2.0) 0 CAR_SHOP 5",
    "OBJ_DATA football = (10.5, 127.5) 0 CAR_SHOP MINES_SHOP",
    "OBJ_DATA football = (10.5, 127.5, 2.0) 0 CAR_SHOP MINES_SHOP",
    "COUNTER my_counter",
    "COUNTER my_counter = 0",
    "ARROW_DATA arrow1",
    "THREAD_ID my_thread (1)",
    "CONVEYOR name",
    "CONVEYOR name = ( 103.5 , 131.0 ) ( 1.0 , 12.0 ) 0 1",
    "CONVEYOR name = ( 103.5 , 131.0 , 3.0 ) ( 1.0 , 12.0 ) 0 1",
    "GENERATOR name",
    "GENERATOR name = (103.5 , 131.0) 180 ROCKET_LAUNCHER 300 1500",
    "GENERATOR name = (103.5 , 131.0, 2.0) 180 ROCKET_LAUNCHER 300 1500",
    "GENERATOR name = (103.5 , 131.0) 180 ROCKET_LAUNCHER 300 1500 20",
    "GENERATOR name = (103.5 , 131.0, 2.0) 180 ROCKET_LAUNCHER 300 1500 20",
    "DESTRUCTOR name",
    "DESTRUCTOR destructora = ( 103.5 , 137.0 ) ( 1.0 , 1.0 )",
    "DESTRUCTOR destructorb = ( 103.5 , 137.0 , 3.0 ) ( 1.0 , 1.0 )",
    "CRANE_DATA name",
    "CRANE_DATA name = (103.5, 137.0) 270 homecrane",
    "CRANE_DATA name = (103.5, 137.0) 270 NO_HOMECRANE FIRST (99.5 , 129.5) 0",
    "CRANE_DATA name = (103.5, 137.0) 270 homecrane FIRST (99.5 , 129.5) 180 SECOND (102.5 , 125.5) 90",
    "CRUSHER name = (103.5, 137.0)",

    # TODO
    "CREATE_CHAR_2D", 
    "CREATE_CHAR_3D", 
    "CREATE_CAR_2D", 
    "CREATE_CAR_3D", 
    "CREATE_CAR_2D_STR", 
    "CREATE_CAR_3D_STR", 
    "CREATE_OBJ_2D", 
	"CREATE_OBJ_3D", 
    "CREATE_OBJ_3D_INT", 
    "CREATE_OBJ_2D_INT", 
    "CREATE_OBJ_3D_STR", 
    "CREATE_OBJ_2D_STR", 
    "CREATE_CONVEYOR_2D", 
    "CREATE_CONVEYOR_3D", 
    "CREATE_GENERATOR_2D", 
	"CREATE_GENERATOR_3D", 
    "CREATE_DESTRUCTOR_2D", 
    "CREATE_DESTRUCTOR_3D",

    "LEVELSTART", 
    "LEVELEND",
    "CREATE_THREAD (my_thread)",
    "STOP_THREAD (my_thread)",
    "EXEC",
    "ENDEXEC",
    "FOR",
    "DO",
    "my_function:"
    "RETURN", 
    "WHILE", 
    "WHILE_EXEC", 

    # boolean stuff
    "NOT", 
    "AND", 
    "OR", 
    "IF", 
    "THEN", 
    "ELSE", 

    "GOTO", 
    "GOSUB",

    # some math stuff
    "num + 2",
    "2 + num",
    "ab + cd",
    "num - 2",
    "2 - num",
    "ab - cd",

    "SET my_counter = "  # obs: different pattern here!

    "num < 1",
    "a < b",
    "num <= 1",
    "a <= b",
    "num > 1",
    "a > b",
    "num >= 1",
    "a >= b",
    "a = 1",     # OBS: S_EQUAL_I
    "a = b",     # OBS: S_EQUAL_S
    "++count",
    "--count",

    "IF_JUMP",  # OBS: only for internal use

    "FORWARD do_kill_frenzy_1:",
    "MAKE_CAR_A_DUMMY (name)",
    "MAP_ZONE name",
    "MAP_ZONE City01 = (1000,350,200,000, 1000,100,100,100,700,000)"  # OBS: test for 10 or 11 params
]

