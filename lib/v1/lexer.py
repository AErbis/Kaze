from rply import LexerGenerator
lg = LexerGenerator()

# Keywords
lg.add('ENTITY',    r'entity')
lg.add('OBJECT',    r'object')
lg.add('IF',        r'if')
lg.add('ELSE',      r'else')
lg.add('FOR',       r'for')
lg.add('WHILE',     r'while')

# Some types
lg.add('UINT8',     r'uint8')
lg.add('UINT16',    r'uint16')
lg.add('UINT32',    r'uint32')
lg.add('UINT64',    r'uint64')
lg.add('INT8',      r'int8')
lg.add('INT16',     r'int16')
lg.add('INT32',     r'int32')
lg.add('INT64',     r'int64')
lg.add('BOOL',      r'bool')
lg.add('FLOAT',     r'float')
lg.add('DOUBLE',    r'double')
lg.add('LIST',      r'list')
lg.add('DIC',       r'dic')

# Operations
lg.add('ADD',       r'\+')
lg.add('SUB',       r'-')
lg.add('DIV',       r'/')
lg.add('MUL',       r'\*')
lg.add('ARROW',     r'=>')

# Lists
lg.add('LBRACKET',  r'\[')
lg.add('RBRACKET',  r'\]')
lg.add('COMMA',     r',')

# Objects
lg.add('LBRACE',    r'{')
lg.add('RBRACE',    r'}')
lg.add('COLON',     r':')

# Methods
lg.add('LPAREN',    r'\(')
lg.add('RPAREN',    r'\)')

# Variables and instructions
lg.add('SEMICOLON', r';')
lg.add('ASSIGN',    r'=')
lg.add('DOT',       r'\.')
lg.add('RETURN',    r'return')
lg.add('NUMBER',    r'\d+')
lg.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z_0-9]*')

# Ignore
lg.ignore(r"\s+")  # Whitespaces and such
lg.ignore(r"#.*\n")  # comments
