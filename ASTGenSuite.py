import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var(self):
        
        """Simple var """
        input = """var a : integer; """
        expect = str(Program([VarDecl(Id("a"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,300))
        
        """full var test """
        input = """var a : integer; 
                    b,c:real;
                    c:array[1 .. 100] of boolean;
                    d:string;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),
        VarDecl(Id("c"),FloatType()),VarDecl(Id("c"),ArrayType(1,100,BoolType())),VarDecl(Id("d"),StringType())]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_funcall(self):
        """function with para and body """
        input = """function foo(a,b:real):array[1 .. 100] of boolean;
                    Begin
                        foo(1);
                    end """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType())]
        ,[],[CallStmt(Id("foo"),[IntLiteral(1)])],ArrayType(1,100,BoolType()))]))
        self.assertTrue(TestAST.test(input,expect,302))

        input = """procedure main(a,b : integer; c:array[1 .. 100] of string);
                    var a : integer;
                    Begin
                        foo();
                        foo(2);
                        foo(3);
                    end """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())
        ,VarDecl(Id("c"),ArrayType(1,100,StringType()))]
        ,[VarDecl(Id("a"),IntType())],[CallStmt(Id("foo"),[])
        ,CallStmt(Id("foo"),[IntLiteral(2)]),CallStmt(Id("foo"),[IntLiteral(3)])])]))
        self.assertTrue(TestAST.test(input,expect,303))



        



   