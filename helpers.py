from enum import Enum, auto, verify, UNIQUE

# declare / create opcodes
DEC_OPCODES_LIST = ["OBJ_DATA", "GENERATOR", "CHAR_DATA", "CREATE_CHAR", "PARKED_CAR_DATA",
                    "CAR_DATA", "THREAD_WAIT_FOR_CHAR_IN_AREA", "LIGHT", "CRANE_DATA", "CREATE_OBJ", 
                     "CREATE_CAR", "CREATE_SOUND", "CREATE_LIGHT", "CREATE_GANG_CAR", "DOOR_DATA", 
                    "SOUND", "DECLARE_CRANE_POWERUP", "CRUSHER", "DESTRUCTOR", "SET_GANG_INFO", 
                    "RADIO_STATION", "CONVEYOR", "PLAYER_PED", "THREAD_WAIT_FOR_CHAR_IN_BLOCK",
                    "CREATE_CHAR_INSIDE_CAR",
                    ]

# execution opcodes
EXEC_OPCODES_LIST = ["POINT_ARROW_AT", "SET_CHAR_OBJECTIVE", "CHANGE_BLOCK", "REMOVE_BLOCK", 
                     "ADD_PATROL_POINT", "EXPLODE_NO_RING", "EXPLODE_LARGE", "EXPLODE_SMALL", 
                     "EXPLODE_WALL", "EXPLODE", "ADD_NEW_BLOCK", "WARP_FROM_CAR_TO_POINT", 
                    "LOWER_LEVEL", "SET_DIR_OF_TV_VANS", "PERFORM_SAVE_GAME", "SWITCH_ROAD"
                    ]

# boolean opcodes
BOOL_OPCODES_LIST = ["IS_CAR_IN_BLOCK", "LOCATE_CHARACTER_ANY_MEANS", "LOCATE_CHARACTER_BY_CAR", 
                     "LOCATE_CHARACTER_ON_FOOT", "IS_POINT_ONSCREEN", "CHECK_CAR_WRECKED_IN_AREA", 
                     "LOCATE_STOPPED_CHARACTER_ANY_MEANS", "LOCATE_STOPPED_CHARACTER_ON_FOOT", 
                     "LOCATE_STOPPED_CHARACTER_BY_CAR", "IS_CHAR_FIRING_IN_AREA"
                     ]

MAP_MAX_X = 256
MAP_MAX_Y = 256

DOOR_FACES = ["BOTTOM", "LEFT", "TOP", "RIGHT"]

@verify(UNIQUE)
class Cmd(Enum):
    OPCODE = auto()
    VAR_NAME = auto()
    EQUAL = auto()
    COORD_XY_F = auto()      # F = float
    COORD_XYZ_F = auto()
    COORD_XY_U8 = auto()     # U8 = unsigned integer 8 bits
    COORD_XYZ_U8 = auto()
    PARAM_ENUM = auto()         # generic enum param
    PARAM_NUM = auto()          # generic number param
    PARAM_XYZ_F = auto()
    PARAM_XYZ_WH_F = auto()
    WIDTH_HEIGHT = auto()
    ROTATION = auto()
    TWO_PARAMS_XYZ_U8 = auto()
    END = auto()
    OPT_PARAM_ENUM = auto()
    OPT_PARAM_NUM = auto()
    GANG_INFO = auto()
    PARAM_XYZ_F_OR_VAR = auto()
    COORD_XYZ_F_OR_VAR = auto()
    OPT_PARAM_ENUM_OR_NUM = auto()
    PARAM_FLOAT = auto()
    RGB = auto()
    TWO_PARAMS_XYZ_F = auto()
    COORD_XYZ_WH_F = auto()
    THREAD_AREA_TYPE = auto()
    THREAD_BLOCK_TYPE = auto()



def get_next_name(line) -> tuple[str, int]:
    """Get the next word in the line. It can be a var name (without being between parenthesis) 
    or an enum.

    It also returns the string position after that word. If it has reached the end of line, 
    return -1 instead.
    """
    name = ""
    for i, chr in enumerate(line):
        if not chr.isalnum() and not chr == '_':
            if len(name) != 0:
                return ( name , i )
            continue
        name += chr
    return ( name , -1 )    # finish of command line

def get_var_name(line):
    """Get the var name between parenthesis."""
    params_tuple = line[ line.find('(') + 1 : line.find(')') ]
    params = params_tuple.split(',')
    return params, line.find(')') + 1

def get_next_numeric_param(line):
    """Get the next parameter as number. It also returns the string position after it.

    If the line has ended after that number, it will return -1 as second return value.

    If there are not numbers until the end of line, the function will return (None, -2). This
    is the case of optional parameters that doesn't exists.
    """
    number_str = ""
    for i, chr in enumerate(line):
        if len(number_str) == 0 and chr == '-':
            number_str += chr
            continue
        if not chr.isdigit():
            if len(number_str) != 0:
                return ( int(number_str) , i )
            continue
        number_str += chr
    
    if number_str:
        return ( int(number_str) , -1 )  # last param: end of line
    else:
        return ( None , -2 )       # optional var doesn't exist

def is_next_param_num(line: str) -> bool:
    """Check if the next param is a number (return True) 
    or if it's either an enum or end of line (return False)
    """
    string = []
    for i, chr in enumerate(line):
        if not chr.isalnum():
            continue
        if chr.isdigit():   # check first alpha-num char
            return True     # it's a number
        else:
            return False    # it's an enum
    return False            # reached at the end of line (i.e. there is no param)

def get_next_float(line: str):
    """Get the next parameter as float. It also returns the string position after it."""
    float_str = ""
    for i, chr in enumerate(line):
        if not chr.isdigit() and chr != '.':
            if len(float_str) != 0:
                return ( float(float_str) , i )
            continue
        float_str += chr
    
    if float_str:
        return ( float(float_str) , -1 )  # last param: end of line
    else:
        return ( None , -2 )       # optional var doesn't exist

def get_coords(line, is_float: bool) -> tuple[tuple, int]:
    """Get the next coordinates in 'line' as a tuple.

    It also returns the string position of the first ')' plus one

    Ex: "(195.5, 15.5, 2.0) 25 0 END"  ->  (195.5, 15.5, 2.0) , 18
        "(195.5, 15.5) 25 0 END"       ->  (195.5, 15.5) , 13
    """
    end_point = line.find(')')
    coords_tuple = line[ line.find('(') + 1 : end_point ]

    params = coords_tuple.split(',')
    assert len(params) == 2 or len(params) == 3

    if is_float:
        params = [ float(param) for param in params ]
    else:
        params = [ int(param) for param in params ]
    
    return  tuple(params) , end_point + 1

def get_params_coords(line, num_params, is_float):
    """Get the next parameters in 'line' containing coordinates.

    If 'num_params' = 0, then 'line' must start with "(x,y,z)" or "(x,y,z, width, height)"
    If 'num_params' = 1, then 'line' must start with "(var1, x,y,z)" or "(var1, x,y,z, width, height)"
    If 'num_params' = 2, then 'line' must start with "(var1, var2, x,y,z)" etc.

    It also returns the string position at the end of the first parenthesis.
    """
    end_point = line.find(')')
    param_coords_tuple = line[ line.find('(') + 1 : end_point ]

    params = param_coords_tuple.split(',')

    if num_params:  # 1 or more parameters
        names = params[:num_params]
        coords = params[num_params:]
    else:           # coordinates only
        names = []
        coords = params

    assert len(coords) == 2 or len(coords) == 3 or len(coords) == 5

    if is_float:
        coords = [ float(coord.strip()) for coord in coords ]
    else:
        coords = [ int(coord.strip()) for coord in coords ]

    params = names
    params.append(tuple(coords))
    return ( params , end_point + 1 )


def get_info_manually(line, integer_indexes: list | None = [], float_indexes: list | None = []):
    """Get all parameters between parenthesis.
    
    If 'integer_indexes' is specified, then this function will convert each index to 'int' type.

    Analogously for 'float_indexes'.

    It also returns the string position at the end of parenthesis.
    """
    end_point = line.find(')')
    params = line[ line.find('(') + 1 : end_point ].split(',')
    
    # convert some params to int (if integer_indexes is specified)
    params = [ int(param) if i in integer_indexes else param for i, param in enumerate(params) ]
    # convert some params to float (if float_indexes is specified)
    params = [ float(param) if i in float_indexes else param for i, param in enumerate(params) ]

    return params, end_point + 1




def read_line(line, *args) -> list:
    """Read a command line string and return all parameters and opcodes from it as a list.
    """
    command = []
    pointer = 0
    for arg in args:
        
        is_float = True

        if (arg == Cmd.OPCODE 
            or arg == Cmd.VAR_NAME 
            or arg == Cmd.PARAM_ENUM
            or arg == Cmd.OPT_PARAM_ENUM):

            name, pointer = get_next_name(line)
            if name:
                command.append(name)
                if pointer == -1:       # has command line finished?
                    break
                line = line[pointer:]   # forward position in string
            
        elif arg == Cmd.EQUAL:
            line = line.replace('=','') # just remove the equal sign
            
        elif arg == Cmd.PARAM_NUM or arg == Cmd.ROTATION or arg == Cmd.OPT_PARAM_NUM:
            number, pointer = get_next_numeric_param(line)
            if number is not None:       # if it got a number
                command.append(number)
                if pointer == -1:
                    break               # command line has finished with last param
                line = line[pointer:]
            else:
                break                   # command line has finished with no optional last param

        elif (arg == Cmd.COORD_XYZ_F 
            or arg == Cmd.COORD_XYZ_U8
            or arg == Cmd.COORD_XY_F 
            or arg == Cmd.COORD_XY_U8 
            or arg == Cmd.WIDTH_HEIGHT
            or arg == Cmd.RGB):

            if arg == Cmd.COORD_XYZ_U8 or arg == Cmd.COORD_XY_U8 or arg == Cmd.RGB:
                is_float = False
            coords, pointer = get_coords(line, is_float=is_float)
            command.append(coords)      # note: always use "append" for "get_coords" just for ensure.
            line = line[pointer:]

        elif arg == Cmd.PARAM_XYZ_F or arg == Cmd.PARAM_XYZ_WH_F:
            params, pointer = get_params_coords(line, num_params=1, is_float=True)
            command.extend(params)
            line = line[pointer:]

        elif arg == Cmd.TWO_PARAMS_XYZ_U8 or arg == Cmd.TWO_PARAMS_XYZ_F:
            if arg == Cmd.TWO_PARAMS_XYZ_U8:
                is_float = False
            params, pointer = get_params_coords(line, num_params=2, is_float=is_float)
            command.extend(params)
            line = line[pointer:]

        elif arg == Cmd.PARAM_XYZ_F_OR_VAR:
            try:
                params, pointer = get_params_coords(line, num_params=1, is_float=True)
                command.extend(params)
            except AssertionError:
                name, pointer = get_var_name(line)
                command.extend(name)
            finally:
                line = line[pointer:]

        elif arg == Cmd.COORD_XYZ_F_OR_VAR:
            try:
                params, pointer = get_coords(line, is_float=True)
                command.append(params)
            except AssertionError:
                name, pointer = get_var_name(line)
                command.extend(name)
            finally:
                line = line[pointer:]
        
        elif arg == Cmd.OPT_PARAM_ENUM_OR_NUM:
            if is_next_param_num(line):
                number, pointer = get_next_numeric_param(line)
                command.append(number)
            else:
                name, pointer = get_next_name(line)
                if name:
                    command.append(name)
                    if pointer == -1:       # has command line finished?
                        break
                    line = line[pointer:]   # forward position in string

        elif arg == Cmd.PARAM_FLOAT:
            f_number, pointer = get_next_float(line)
            if f_number is not None:       # if it got a float number
                command.append(f_number)
                if pointer == -1:
                    break               # command line has finished with last param
                line = line[pointer:]
            else:
                break                   # command line has finished with no optional last param
        
        elif arg == Cmd.COORD_XYZ_WH_F:
            coords, pointer = get_params_coords(line, num_params=0, is_float=True)
            command.extend(coords)
            line = line[pointer:]

        elif arg == Cmd.THREAD_AREA_TYPE:
            raw_params, pointer = get_info_manually(line, float_indexes=[1,2,3,4,5])
            params = [raw_params[0]] + [tuple(raw_params[1:6])] + raw_params[6:]
            command.extend(params)
            line = line[pointer:]

        elif arg == Cmd.THREAD_BLOCK_TYPE:
            raw_params, pointer = get_info_manually(line, float_indexes=[1,2,3])
            params = [raw_params[0]] + [tuple(raw_params[1:4])] + raw_params[4:]
            command.extend(params)
            line = line[pointer:]


    # remove whitespaces
    for i, param in enumerate(command):
        if type(param) == str:
            command[i] = param.strip()

    return command