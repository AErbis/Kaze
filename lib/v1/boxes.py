from rply.token import BaseBox
import cgen as c
from enum import Enum


class Entity(BaseBox):
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def eval(self):
        return self.body.eval()

    def __repr__(self):
        return f'class {self.name}'

class EntityBody(BaseBox):
    def __init__(self, method_list):
        self.method_list = method_list
    
    def eval(self):
        return self.method_list.eval()

class ExprList(BaseBox):
    def __init__(self, value=None, other=None):
        self.value = value
        self.other = other

    def eval(self):
        if self.other:
            return [self.value] + self.other.eval()
        elif self.value:
            return [self.value]
        return []

class Method(BaseBox):
    def __init__(self, name, arguments, body):
        self.name = name
        self.arguments = arguments
        self.body = body

    def __repr__(self):
        return f'{self.name}({", ".join(str(x) for x in self.arguments.eval())})'
    
class Argument(object):
    def __init__(self, dtype, name):
        self.dtype = dtype
        self.name = name

    def __str__(self):
        return f'{self.dtype} {self.name}'

class Instruction(BaseBox):
    def __init__(self, expr):
        self.expr = expr

class Return(Instruction):
    pass

class UnaryExpr(BaseBox):
    def __init__(self, value):
        self.value = value

class ParensExpr(UnaryExpr):
    pass
    
class BinaryExpr(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Assignment(BaseBox):
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

class Declaration(BaseBox):
    def __init__(self, var, dtype, expr):
        self.var = var
        self.dtype = dtype
        self.expr = expr

class Call(BaseBox):
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

class List(BaseBox):
    def __init__(self, elements):
        self.elements = elements
