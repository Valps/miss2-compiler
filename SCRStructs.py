from dataclasses import dataclass
from decimal import Decimal

@dataclass
class TreeNode:
    pass

@dataclass
class StatementSequence(TreeNode):
    sequence : list[TreeNode]

@dataclass
class Int(TreeNode):
    value : int

@dataclass
class Float(TreeNode):
    value : Decimal

@dataclass
class PlayerPed(TreeNode):
    name : str
    x : Float
    y : Float
    z : Float
    remap : int
    rotation : int

@dataclass
class CharData(TreeNode):
    name : str

@dataclass
class Counter(TreeNode):
    name : str

@dataclass
class LevelStart(TreeNode):
    pass

@dataclass
class CreateChar(TreeNode):
    name : str
    x : Float
    y : Float
    z : Float
    remap : int
    rotation : int
    occupation : int

@dataclass
class ClearWantedLevel(TreeNode):
    name : str



# Boolean stuff

@dataclass
class BooleanCondition:     # (TreeNode) ?
    pass    # TODO

@dataclass
class While(TreeNode):
    condition : BooleanCondition
    body : StatementSequence

@dataclass
class If(TreeNode):
    condition : BooleanCondition
    
    body_true : StatementSequence
    body_else : StatementSequence = None        # TODO: is "= None" necessary?

