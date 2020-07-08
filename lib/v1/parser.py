from rply import ParserGenerator
from .boxes import *


pg = ParserGenerator([
    "IDENTIFIER",
    "NUMBER",
    "ENTITY",
    "LBRACE",
    "RBRACE",
    "LPAREN",
    "RPAREN",
    "LBRACKET",
    "RBRACKET",
    "COMMA",
    "DOT",
    "UINT8",
    "UINT16",
    "UINT32",
    "UINT64",
    "INT8",
    "INT16",
    "INT32",
    "INT64",
    "BOOL",
    "FLOAT",
    "DOUBLE",
    "IF",
    "ELSE",
    "GREATER",
    "GEQ",
    "LESS", 
    "LEQ",
    "EQUAL",
    "DIFF",
    "LIST",
    "DIC",
    "ADD",
    "SUB",
    "DIV",
    "MUL",
    "ARROW",
    "ASSIGN",
    "COLON",
    "SEMICOLON",
    "RETURN"
], precedence=[
    ("left", ['ASSIGN']),
    ("left", ['IF', 'ELSE']),
    ("left", ['ADD', 'SUB']),
    ("left", ['MUL', 'DIV']),
    ("right", ['LPAREN']),
    ("left", ['RPAREN']),
    ("left", ['GREATER', 'GEQ', 'LESS', 'LEQ', 'EQUAL', 'DIFF'])
], cache_id="kaze")

@pg.production("entity : ENTITY IDENTIFIER LBRACE entity_body RBRACE")
def entity(p):
    return Entity(p[1].value, p[3])

@pg.production("entity_body : method_list")
def entity_body(p):
    return EntityBody(p[0])

@pg.production("method_list : method method_list")
def method_list(p):
    return ExprList(p[0], p[1])

@pg.production("method_list : ")
def method_list_empty(p):
    return ExprList()

@pg.production("method : IDENTIFIER LPAREN arguments RPAREN LBRACE method_body RBRACE")
def method(p):
    return Method(p[0].value, p[2], p[5])

@pg.production("arguments : IDENTIFIER COLON type COMMA arguments")
def arguments(p):
    return ExprList(Argument(p[2], p[0].value), p[4])

@pg.production("arguments : IDENTIFIER COLON type")
def argument_single(p):
    return ExprList(Argument(p[2], p[0].value))

@pg.production("arguments : ")
def arguments_none(p):
    return ExprList()

@pg.production("method_body : instruction method_body")
def method_body(p):
    return ExprList(p[0], p[1])

@pg.production("method_body : ")
def method_body_empty(p):
    return ExprList()

@pg.production("instruction : RETURN expression SEMICOLON")
def instr_ret(p):
    return Return(p[1])

@pg.production("instruction : attr COLON type assign")
def instr_decl(p):
    return Declaration(p[0], p[2], p[3])

@pg.production("instruction : attr assign")
def instr_assign(p):
    return Assignment(p[0], p[1])

@pg.production("assign : ASSIGN expression SEMICOLON")
def assign(p):
    return UnaryExpr(p[1])

@pg.production("instruction : expression SEMICOLON")
def intsr_expr(p):
    return Instruction(p[0])

@pg.production("instruction : IF LPAREN expression RPAREN LBRACE method_body RBRACE else_if_clausule")
def instr_if(p):
    return If(p[2], p[5], p[7])

@pg.production("else_if_clausule : ELSE IF LPAREN expression RPAREN LBRACE method_body RBRACE else_if_clausule")
def else_if_clausule(p):
    return ElseIf(p[3], p[6], p[8])

@pg.production("else_if_clausule : ELSE LBRACE method_body RBRACE")
def else_if_clausule_else(p):
    return Else(p[2])

@pg.production("else_if_clausule : ")
def else_if_clausule_none(p):
    return Terminus()

@pg.production("expression : attr")
@pg.production("expression : NUMBER")
def expression(p):
    return UnaryExpr(p[0])

@pg.production("expression : LPAREN expression RPAREN")
def expression_parens(p):
    return ParensExpr(p[1])

@pg.production("expression : expression ADD expression")
@pg.production("expression : expression SUB expression")
@pg.production("expression : expression DIV expression")
@pg.production("expression : expression MUL expression")
@pg.production("expression : expression GREATER expression")
@pg.production("expression : expression GEQ expression")
@pg.production("expression : expression LESS expression")
@pg.production("expression : expression LEQ expression")
@pg.production("expression : expression EQUAL expression")
@pg.production("expression : expression DIFF expression")
def expression_math(p):
    return BinaryExpr(p[0], p[2], p[1].value)

@pg.production("expression : attr LPAREN parameters RPAREN")
def expression_call(p):
    return Call(p[0], p[2])

@pg.production("expression : LBRACKET parameters RBRACKET")
def expression_list(p):
    return List(p[1])

@pg.production("expression : LPAREN arguments RPAREN ARROW LBRACE method_body RBRACE")
def expression_lambda(p):
    print('lambda', p)

@pg.production("attr : IDENTIFIER DOT attr")
def attr(p):
    return ExprList(p[0].value, p[1])

@pg.production("attr : IDENTIFIER")
def attr_single(p):
    return ExprList(p[0].value)

@pg.production("parameters : parameters_many")
@pg.production("parameters : parameters_one")
@pg.production("parameters : parameters_none")
def parameters(p):
    return p[0]

@pg.production("parameters_many : expression COMMA parameters_follow")
def parameters_many(p):
    return ExprList(p[0], p[1])

@pg.production("parameters_follow : parameters_many")
@pg.production("parameters_follow : parameters_one")
def parameters_follow(p):
    return p[0]

@pg.production("parameters_one : expression")
def parameters_one(p):
    return ExprList(p[0])

@pg.production("parameters_none : ")
def parameters_none(p):
    return ExprList()

@pg.production("type : UINT8")
@pg.production("type : UINT16")
@pg.production("type : UINT32")
@pg.production("type : UINT64")
@pg.production("type : INT8")
@pg.production("type : INT16")
@pg.production("type : INT32")
@pg.production("type : INT64")
@pg.production("type : BOOL")
@pg.production("type : FLOAT")
@pg.production("type : DOUBLE")
@pg.production("type : LIST")
@pg.production("type : DIC")
@pg.production("type : ENTITY")
def dtype(p):
    return p[0].value
