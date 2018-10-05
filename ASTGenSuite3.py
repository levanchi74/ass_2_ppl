import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """var a:integer; b: real;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_2(self):
        input = """var a,b:integer;c,b,a,c,d:real;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("a"),FloatType()),VarDecl(Id("c"),FloatType()),VarDecl(Id("d"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_3(self):
        input = """var a: array [1 .. 3] of integer;c,b,a,c,d:real;"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,3,IntType())),VarDecl(Id("c"),FloatType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("a"),FloatType()),VarDecl(Id("c"),FloatType()),VarDecl(Id("d"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_4(self):
        input = """var a: array [-1 .. 3] of integer;c: real;"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(-1,3,IntType())),VarDecl(Id("c"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_5(self):
        input = """var a: array [-1 .. -3] of boolean; c: array [2 .. -4] of real;"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(-1,-3,BoolType())),VarDecl(Id("c"),ArrayType(2,-4,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_6(self):
        """More complex program"""
        input = """function foo ():INTEGER; begin
         putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_7(self):
        input = """function foo ():INTEGER;
         var a:integer;
        begin
    
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("a"),IntType())],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_8(self):
      
        input = """ var a,b: integer;
                        d: real;
                        e: array [1 .. 5] of real;
                    """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),
                              VarDecl(Id("d"),FloatType()),
                              VarDecl(Id("e"),ArrayType(1,5,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_9(self):
        """More complex program"""
        input = """ function foo (a,b:integer):INTEGER; 
                    var a:integer;
                    begin
                        
                    end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],
                [VarDecl(Id("a"),IntType())],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,308))
    
    def test_10(self):
        """More complex program"""
        input = """ procedure main (); 
                    var a:real;
                    begin
            
                    end
                    function foo (c:integer):INTEGER; 
                    var b: string;
                    begin
                        
                    end"""
        expect = str(Program([
                FuncDecl(Id("main"),[],[VarDecl(Id("a"),FloatType())],[],VoidType()),
                FuncDecl(Id("foo"),[VarDecl(Id("c"),IntType())],[VarDecl(Id("b"),StringType())],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_11(self):
        input = """var a,b,c,d: integer;
                        """
        expect = str(Program([VarDecl(Id("a"),IntType()),
                              VarDecl(Id("b"),IntType()),
                              VarDecl(Id("c"),IntType()),
                              VarDecl(Id("d"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_12(self):
        input = """var a:integer;"""
        expect = str(Program([VarDecl(Id('a'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_13(self):
        input = """var a,b:integer;
                         c:real;"""
        expect = str(Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_14(self):
        input = """var a:array [3 .. -1] of real;"""
        expect = str(Program([VarDecl(Id('a'),ArrayType(3,-1,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_15(self):
        input = """var a:integer;
                   var b:real;"""
        expect = str(Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_16(self):
        input = """ var a: integer;
                    procedure main(); begin end"""
        expect = str(Program([VarDecl(Id('a'),IntType()),FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_17(self):
        input = """function foo ():INTEGER; begin
        break;
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Break()],IntType())]))
        self.assertTrue(TestAST.test(input,expect,316))


    def test_18(self):
        input = """procedure foo();
                    begin
                        return a;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Return(Id('a'))])]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_19(self):
        input = """procedure foo();
                    begin
                        c := exp;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id("c"),Id("exp"))])]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_20(self):
        input = """procedure foo();
                    begin
                        a := b := c := exp;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id("c"),Id("exp")),Assign(Id("b"),Id("c")),Assign(Id("a"),Id("b"))])]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_21(self):
        input = """procedure foo();
                    begin
                        a := 1 and then 2;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('a'),BinaryOp('andthen',IntLiteral(1),IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_22(self):
        input = """procedure foo();
                    begin
                        begin
                            return b;
                        end
                        return a;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Return(Id('b')),Return(Id('a'))])]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_23(self):
        input = """procedure foo();
                    begin
                        if a > 3 then a := 3;
                        else a := 1;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[If(BinaryOp('>',Id('a'),IntLiteral(3)),[Assign(Id('a'),IntLiteral(3))],[Assign(Id('a'),IntLiteral(1))])])]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_24(self):
        input = """procedure foo();
                    begin
                        a := 1 and then 2 or else 3 or else 4;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('a'),BinaryOp('orelse',BinaryOp('orelse',BinaryOp('andthen',IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)))])]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_25(self):
        input = """procedure proc();
        begin
            if a > 3 then
                if a < 7 then
                    b := b + 2;
                else
                    b := "huhuhu";
        end"""
        expect = str(Program([FuncDecl(Id('proc'),[],[],[If(BinaryOp('>',Id('a'),IntLiteral(3)),[If(BinaryOp('<',Id('a'),IntLiteral(7)),[Assign(Id('b'),BinaryOp('+',Id('b'),IntLiteral(2)))],[Assign(Id('b'),StringLiteral('huhuhu'))])],[])])]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_26(self):
        input = """var a:integer;
                       b:real;
                       c:boolean;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_27(self):
        input = """var a:array[1 .. 2] of real;
                       s:string;
                       """
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,2,FloatType())),VarDecl(Id("s"),StringType())]))
        self.assertTrue(TestAST.test(input,expect,326))


    def test_28(self):
        input = """var a:integer;
                       a,b:array[1 .. 5] of integer;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("a"),ArrayType(1,5,IntType())),VarDecl(Id("b"),ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_29(self):
        input = """var a:integer;
                       c,d:array[-1 .. 6] of string;
        """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("c"),ArrayType(-1,6,StringType())),VarDecl(Id("d"),ArrayType(-1,6,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_30(self):
        input = """var a : integer;
                b,c:real;
                c:array[1 .. 100] of boolean;
                d:string;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),
        VarDecl(Id("c"),FloatType()),VarDecl(Id("c"),ArrayType(1,100,BoolType())),VarDecl(Id("d"),StringType())]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_31(self):
        input="""function foo (a , b : integer ; c : real ) : array [ 1 .. 2 ] of integer ;
            var x , y : real ;
            begin
            end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType())],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType())],[],ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_32(self):
        input = """
        procedure main();
        begin
            with i :integer; do a := 1;
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("i"),IntType())],[Assign(Id("a"),IntLiteral(1))])])]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_33(self):
        input = """
        var i :integer;
        function f (): integer;
        begin
            return 200;
        end
        procedure main();
        var
        main: integer;
        begin
            main := f ();
            putIntLn(main);
            with i :integer;
            main:integer;
            f :integer;
            do begin
                main := f := i := 100;
                putIntLn( i );
                putIntLn(main);
                putIntLn(f );
            end
            putIntLn(main);
        end
        var g: real ;"""
        expect = str(Program([VarDecl(Id("i"),IntType()),
                    FuncDecl(Id("f"),[],[],[Return(IntLiteral(200))],IntType()),
                    FuncDecl(Id("main"),[],[VarDecl(Id("main"),IntType())],[Assign(Id("main"),CallExpr(Id("f"),[])),CallStmt(Id("putIntLn"),[Id("main")]),With([VarDecl(Id("i"),IntType()),VarDecl(Id("main"),IntType()),VarDecl(Id("f"),IntType())],[Assign(Id("i"),IntLiteral(100)),Assign(Id("f"),Id("i")),Assign(Id("main"),Id("f")),CallStmt(Id("putIntLn"),[Id("i")]),CallStmt(Id("putIntLn"),[Id("main")]),CallStmt(Id("putIntLn"),[Id("f")])]),CallStmt(Id("putIntLn"),[Id("main")])]),
                    VarDecl(Id("g"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_34(self):
        input = """procedure foo();
                    begin
                        a := 1 and then 2 or else 3 > 4;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('a'),BinaryOp('orelse',BinaryOp('andthen',IntLiteral(1),IntLiteral(2)),BinaryOp('>',IntLiteral(3),IntLiteral(4))))])]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_35(self):
        input = """procedure foo();
                    begin
                        c := a and then putIntLn( i ) or else c and then d ;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id("c"),BinaryOp("andthen",BinaryOp("orelse",BinaryOp("andthen",Id("a"),CallExpr(Id('putIntLn'),[Id('i')])),Id("c")),Id("d")))])]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_36(self):
        input = """procedure main();begin begin end end"""
        expect = str (Program([FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_37(self):
        input = """procedure foo(); begin begin return b; end return c; end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Return(Id("b")),Return(Id("c"))])]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_38(self):
        input = """procedure foo(); begin
                    while (a > b ) do 
                    begin
                        a :=3;
                    end
                 end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp(">",Id("a"),Id("b")),[Assign(Id("a"),IntLiteral(3))])])]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_39(self):
        input = """procedure foo();
                    begin
                        a := 1 and then 2;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('a'),BinaryOp('andthen',IntLiteral(1),IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input,expect,338))
