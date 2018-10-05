import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):		
    def test_statement_22(self):
        """var a,b,c: integer ; d,e: real ;
		var e: integer; f: real ;"""
        input = """
			var a,b: integer ;
			c,d: real;
			function foo(a,b: integer; c: array [1 .. 3] of integer): integer;
			var a,b: integer ;
			c,d: real ;
			begin
				a := 3 ;
			end
		"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType()),VarDecl(Id("d"),FloatType()),FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,3,IntType()))],[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType()),VarDecl(Id("d"),FloatType())],[Assign(Id("a"),IntLiteral(3))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,367))

    def test_variable_declare_1(self):
        """var a: integer ;"""
        input = """var a: integer ;"""
        expect = str(Program([VarDecl(Id("a"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,300))

		
    def test_variable_declare_2(self):
        """var a,b,c: integer ;"""
        input = """var a,b,c: integer ;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_variable_declare_3(self):
        """var a,b,c: integer; 
		d: integer;"""
        input = """var a: integer ;
		b: integer;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_variable_declare_4(self):
        """var a,b,c: real ;"""
        input = """var a,b,c: real ;"""
        expect = str(Program([VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_variable_declare_5(self):
        """var a,b,c: string ;"""
        input = """var a,b,c: string ;"""
        expect = str(Program([VarDecl(Id("a"),StringType()),VarDecl(Id("b"),StringType()),VarDecl(Id("c"),StringType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_variable_declare_6(self):
        """var a,b,c: boolean ;"""
        input = """var a,b,c: boolean ;"""
        expect = str(Program([VarDecl(Id("a"),BoolType()),VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_variable_declare_7(self):
        """var a: array [1 .. 5] of integer ;"""
        input = """var a: array [1 .. 5] of integer ;"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_variable_declare_8(self):
        """var a: array [2 .. 10] of real ;"""
        input = """var a: array [2 .. 10] of real ;"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(2,10,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_variable_declare_9(self):
        """var a: array [2 .. 10] of real ;"""
        input = """var a,b,c: array [2 .. 10] of integer;"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(2,10,IntType())),VarDecl(Id("b"),ArrayType(2,10,IntType())),VarDecl(Id("c"),ArrayType(2,10,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_variable_declare_10(self):
        """var a: array [2 .. 10] of real ;"""
        input = """var a,b,c: array [2 .. 10] of boolean;"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(2,10,BoolType())),VarDecl(Id("b"),ArrayType(2,10,BoolType())),VarDecl(Id("c"),ArrayType(2,10,BoolType()))]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_variable_declare_11(self):
        """var a: array [2 .. 10] of string ;"""
        input = """var a,b,c: array [2 .. 10] of string;"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(2,10,StringType())),VarDecl(Id("b"),ArrayType(2,10,StringType())),VarDecl(Id("c"),ArrayType(2,10,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_function_declare_1(self):
        """function foo(): integer;
		begin
		end"""
        input = """function foo(): integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_function_declare_2(self):
        """function foo(): real;
		begin
		end"""
        input = """function foo(): real;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,312))

		
		
    def test_function_declare_3(self):
        """function foo(): string;
		begin
		end"""
        input = """function foo(): string;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],StringType())]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_function_declare_4(self):
        """function foo(): boolean;
		begin
		end"""
        input = """function foo(): boolean;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_function_declare_5(self):
        """function foo(): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_function_declare_6(self):
        """function foo(a: integer): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(a: integer): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_function_declare_7(self):
        """function foo(a,b: integer): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(a,b: integer): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,317))
		
    def test_function_declare_8(self):
        """function foo(a,b: integer ; c: real): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(a,b: integer ; c: real): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType())],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_function_declare_9(self):
        """function foo(): integer;
		var b: integer;
		begin
		end"""
        input = """function foo(): integer;
		var b: integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("b"),IntType())],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_function_declare_8(self):
        """function foo(): integer;
		begin
			a := 3;
		end"""
        input = """function foo(): integer;
		begin
			a := 3;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),IntLiteral(3))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_assignment_1(self):
        """function foo(): integer;
		begin
			a := b := 4;
		end"""
        input = """function foo(): integer;
		begin
			a := b := 4;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("b"),IntLiteral(4)),Assign(Id("a"),Id("b"))]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_assignment_2(self):
        """function foo(): integer;
		begin
			a := b := c := d := 4;
		end"""
        input = """function foo(): integer;
		begin
			a := b := c := d := 4;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("d"),IntLiteral(4)),Assign(Id("c"),Id("d")),Assign(Id("b"),Id("c")),Assign(Id("a"),Id("b"))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,322))


    def test_assignment_3(self):
        """function foo(): integer;
		begin
			a[2] := 6;
		end"""
        input = """function foo(): integer;
		begin
			a[2] := 6;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(6))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_expression_1(self):
        """function foo(): integer;
		begin
			a := b and then c ;
		end"""
        input = """function foo(): integer;
		begin
			a := b and then c ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("and then",Id("b"),Id("c")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_expression_2(self):
        """function foo(): integer;
		begin
			a := b or else c ;
		end"""
        input = """function foo(): integer;
		begin
			a := b or else c ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("or else",Id("b"),Id("c")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_expression_3(self):
        """function foo(): integer;
		begin
			a := b + c ;
		end"""
        input = """function foo(): integer;
		begin
			a := b + c ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("+",Id("b"),Id("c")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_expression_4(self):
        """function foo(): integer;
		begin
			a := b - c ;
		end"""
        input = """function foo(): integer;
		begin
			a := b - c ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("-",Id("b"),Id("c")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_expression_5(self):
        """function foo(): integer;
		begin
			a := b * c ;
		end"""
        input = """function foo(): integer;
		begin
			a := b * c ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("*",Id("b"),Id("c")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_expression_6(self):
        """function foo(): integer;
		begin
			a := b / c ;
		end"""
        input = """function foo(): integer;
		begin
			a := b / c ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("/",Id("b"),Id("c")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_expression_7(self):
        """function foo(): integer;
		begin
			a := b <> c ;
		end"""
        input = """function foo(): integer;
		begin
			a := b <> c ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("<>",Id("b"),Id("c")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_expression_8(self):
        """function foo(): integer;
		begin
			a := b and c ;
		end"""
        input = """function foo(): integer;
		begin
			a := b and c ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("and",Id("b"),Id("c")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_expression_9(self):
        """function foo(): integer;
		begin
			a := -b;
		end"""
        input = """function foo(): integer;
		begin
			a := -b;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),UnaryOp("-",Id("b")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_expression_10(self):
        """function foo(): integer;
		begin
			a := not b;
		end"""
        input = """function foo(): integer;
		begin
			a := not b;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),UnaryOp("not",Id("b")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_expression_11(self):
        """function foo(): integer;
		begin
			a := (b + c);
		end"""
        input = """function foo(): integer;
		begin
			a := (b + c);
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("+",Id("b"),Id("c")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_expression_12(self):
        """function foo(): integer;
		begin
			a := b + c*d - e ;
		end"""
        input = """function foo(): integer;
		begin
			a := b + c*d - e ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("-",BinaryOp("+",Id("b"),BinaryOp("*",Id("c"),Id("d"))),Id("e")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_expression_13(self):
        """function foo(): integer;
		begin
			a[3] := 3 ;
		end"""
        input = """function foo(): integer;
		begin
			a[3] := 3 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(ArrayCell(Id("a"),IntLiteral(3)),IntLiteral(3))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_expression_14(self):
        """function foo(): integer;
		begin
			a := b[5] := c + 6 ;
		end"""
        input = """function foo(): integer;
		begin
			a := b[5] := c + 6 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),Assign(ArrayCell(Id("b"),IntLiteral(5)),BinaryOp("+",Id("c"),IntLiteral(6))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_expression_15(self):
        """function foo(): integer;
		begin
			a := true ;
		end"""
        input = """function foo(): integer;
		begin
			a := true ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BooleanLiteral(True))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_expression_16(self):
        """function foo(): integer;
		begin
			a := false ;
		end"""
        input = """function foo(): integer;
		begin
			a := false ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BooleanLiteral(False))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_expression_17(self):
        """function foo(): integer;
		begin
			a := true or false or true and false ;
		end"""
        input = """function foo(): integer;
		begin
			a := true or false or true and false ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("or",BinaryOp("or",BooleanLiteral(True),BooleanLiteral(False)),BinaryOp("and",BooleanLiteral(True),BooleanLiteral(False))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_expression_18(self):
        """function foo(): integer;
		begin
			a := "xin chao cac ban" ;
		end"""
        input = """function foo(): integer;
		begin
			a := "xin chao cac ban" ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),StringLiteral("xin chao cac ban"))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_expression_19(self):
        """function foo(): integer;
		begin
			a := "day la mon nguyen ly ngon ngu lap trinh" ;
		end"""
        input = """function foo(): integer;
		begin
			a := "day la mon nguyen ly ngon ngu lap trinh" ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),StringLiteral("day la mon nguyen ly ngon ngu lap trinh"))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_expression_20(self):
        """function foo(): integer;
		begin
			a := 2.5 ;
		end"""
        input = """function foo(): integer;
		begin
			a := 2.5 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),FloatLiteral(2.5))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_expression_21(self):
        """function foo(): integer;
		begin
			a := 2.1e-2 ;
		end"""
        input = """function foo(): integer;
		begin
			a := 2.1e-2 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),FloatLiteral(2.1e-2))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_expression_22(self):
        """function foo(): integer;
		begin
			a[2] := b[3] := c[4] := d[5] ;
		end"""
        input = """function foo(): integer;
		begin
			a[2] := b[3] := c[4] := d[5] ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(ArrayCell(Id("c"),IntLiteral(4)),ArrayCell(Id("d"),IntLiteral(5))),Assign(ArrayCell(Id("b"),IntLiteral(3)),ArrayCell(Id("c"),IntLiteral(4))),Assign(ArrayCell(Id("a"),IntLiteral(2)),ArrayCell(Id("b"),IntLiteral(3)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_expression_23(self):
        """function foo(): integer;
		begin
			a := b[c[d[6]]] ;
		end"""
        input = """function foo(): integer;
		begin
			a := b[c[d[6]]] ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),ArrayCell(Id("b"),ArrayCell(Id("c"),ArrayCell(Id("d"),IntLiteral(6)))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_expression_24(self):
        """function foo(): integer;
		begin
			a[b[3]] := c[d[2]] ;
		end"""
        input = """function foo(): integer;
		begin
			a[b[3]] := c[d[2]] ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(3))),ArrayCell(Id("c"),ArrayCell(Id("d"),IntLiteral(2))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_expression_25(self):
        """function foo(): integer;
		begin
			a := foo(3) ;
		end"""
        input = """function foo(): integer;
		begin
			a := foo(3) ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(3)]))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_expression_26(self):
        """function foo(): integer;
		begin
			a := foo(3,4,5,6,7) ;
		end"""
        input = """function foo(): integer;
		begin
			a := foo(3,4,5,6,7) ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7)]))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_expression_26(self):
        """function foo(): integer;
		begin
			a := foo(b,c,d) ;
		end"""
        input = """function foo(): integer;
		begin
			a := foo(b,c,d) ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),CallExpr(Id("foo"),[Id("b"),Id("c"),Id("d")]))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_expression_26(self):
        """function foo(): integer;
		begin
			a := foo(1 + 2,3 * b,c[d[2 + 4]]) ;
		end"""
        input = """function foo(): integer;
		begin
			a := foo(1 + 2,3 * b,c[d[2 + 4]]) ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(1),IntLiteral(2)),BinaryOp("*",IntLiteral(3),Id("b")),ArrayCell(Id("c"),ArrayCell(Id("d"),BinaryOp("+",IntLiteral(2),IntLiteral(4))))]))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_statement_1(self):
        """function foo(): integer;
		begin
			a := b[10] := foo()[3] := x := 1 ;
		end"""
        input = """function foo(): integer;
		begin
			a := b[10] := foo()[3] := x := 1 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("x"),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),Id("x")),Assign(ArrayCell(Id("b"),IntLiteral(10)),ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),Id("x"))),Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(10)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,352))
		
    def test_statement_2(self):
        """function foo(): integer;
		begin
			if a < 5 then
				a := a + 1 ;
		end"""
        input = """function foo(): integer;
		begin
			if a < 5 then
				a := a + 1 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp("<",Id("a"),IntLiteral(5)),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_statement_3(self):
        """function foo(): integer;
		begin
			if a < 5 then
				a := a + 1 ;
			else
				a := a - 1 ;
		end"""
        input = """function foo(): integer;
		begin
			if a < 5 then
				a := a + 1 ;
			else
				a := a - 1 ;				
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp("<",Id("a"),IntLiteral(5)),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],[Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,354))
		
    def test_statement_4(self):
        """function foo(): integer;
		begin
			while a < 5
			do
				a := a + 1 ;
		end"""
        input = """function foo(): integer;
		begin
			while a < 5
			do
				a := a + 1 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp("<",Id("a"),IntLiteral(5)),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_statement_5(self):
        """function foo(): integer;
		begin
			while a <= b
			do
				a := a*b - 6 ;
		end"""
        input = """function foo(): integer;
		begin
			while a <= b
			do
				a := a*b - 6 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp("<=",Id("a"),Id("b")),[Assign(Id("a"),BinaryOp("-",BinaryOp("*",Id("a"),Id("b")),IntLiteral(6)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_statement_6(self):
        """function foo(): integer;
		begin
			while a <= b
			do
			begin
				a := a*b - 6 ;
			end	
		end"""
        input = """function foo(): integer;
		begin
			while a <= b
			do
			begin
				a := a*b - 6 ;
			end	
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp("<=",Id("a"),Id("b")),[Assign(Id("a"),BinaryOp("-",BinaryOp("*",Id("a"),Id("b")),IntLiteral(6)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_statement_7(self):
        """function foo(): integer;
		begin
			while a <= b
			do
			begin
				a := a*b - 6 ;
			end	
		end"""
        input = """function foo(): integer;
		begin
			while a <= b
			do
			begin
				a := a*b - 6 ;
			end	
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp("<=",Id("a"),Id("b")),[Assign(Id("a"),BinaryOp("-",BinaryOp("*",Id("a"),Id("b")),IntLiteral(6)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_statement_8(self):
        """function foo(): integer;
		begin
			while a <= b
			do
			begin
				a := a + 1 ;
				b := b + 1 ;
			end	
		end"""
        input = """function foo(): integer;
		begin
			while a <= b
			do
			begin
				a := a + 1 ;
				b := b + 1 ;
			end	
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp("<=",Id("a"),Id("b")),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(1)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_statement_9(self):
        """function foo(): integer;
		begin
			if a < 5 then
				begin
					a := a + 1 ;
					a := a * 3 ;					
				end
			else
				begin
					a := a - 1 ;
					a := a / 3 ;					
				end
		end"""
        input = """function foo(): integer;
		begin
			if a < 5 then		
				begin
					a := a + 1 ;
					a := a * 3 ;					
				end
			else
				begin
					a := a - 1 ;
					a := a / 3 ;					
				end
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp("<",Id("a"),IntLiteral(5)),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Assign(Id("a"),BinaryOp("*",Id("a"),IntLiteral(3)))],[Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Assign(Id("a"),BinaryOp("/",Id("a"),IntLiteral(3)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_statement_10(self):
        """function foo(): integer;
		begin
			if a < 5 then
					a := a + 1 ;
			else
				begin
					a := a - 1 ;
					a := a / 3 ;					
				end
		end"""
        input = """function foo(): integer;
		begin
			if a < 5 then		
					a := a + 1 ;
			else
				begin
					a := a - 1 ;
					a := a / 3 ;					
				end
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp("<",Id("a"),IntLiteral(5)),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],[Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Assign(Id("a"),BinaryOp("/",Id("a"),IntLiteral(3)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_statement_11(self):
        """function foo(): integer;
		begin
			if a < 5 then
				begin
					a := a + 1 ;
					a := a * 3 ;					
				end	
			else
					a := a - 1 ;
		end"""
        input = """function foo(): integer;
		begin
			if a < 5 then
				begin
					a := a + 1 ;
					a := a * 3 ;					
				end	
			else
					a := a - 1 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp("<",Id("a"),IntLiteral(5)),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Assign(Id("a"),BinaryOp("*",Id("a"),IntLiteral(3)))],[Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_statement_12(self):
        """function foo(): integer;
		begin
			for i := 0 to 10
			do
				a := a + 1 ;
		end"""
        input = """function foo(): integer;
		begin
			for i := 0 to 10
			do
				a := a + 1 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id("i"),IntLiteral(0),IntLiteral(10),True,[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_statement_13(self):
        """function foo(): integer;
		begin
			for i := 0 to 10
			do
			begin
				a := a + 1 ;
			end	
		end"""
        input = """function foo(): integer;
		begin
			for i := 0 to 10
			do
			begin
				a := a + 1 ;
			end	
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id("i"),IntLiteral(0),IntLiteral(10),True,[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_statement_14(self):
        """function foo(): integer;
		begin
			for i := 0 to 10
			do
			begin
				a := a + 1 ;
				b := b + 1 ;				
			end	
		end"""
        input = """function foo(): integer;
		begin
			for i := 0 to 10
			do
			begin
				a := a + 1 ;
				b := b + 1 ;								
			end	
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id("i"),IntLiteral(0),IntLiteral(10),True,[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(1)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,360))

    def test_statement_15(self):
        """function foo(): integer;
		begin
			for i := 10 downto 1
			do
			begin
				a := a + 1 ;
				b := b + 1 ;				
			end	
		end"""
        input = """function foo(): integer;
		begin
			for i := 10 downto 1
			do
			begin
				a := a + 1 ;
				b := b + 1 ;								
			end	
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id("i"),IntLiteral(10),IntLiteral(1),False,[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(1)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,361))

    def test_statement_16(self):
        """function foo(): integer;
		begin
			for i := a * 5 downto b /10
			do
			begin
				a := a + 1 ;
				b := b + 1 ;				
			end	
		end"""
        input = """function foo(): integer;
		begin
			for i := a * 5 downto b /10
			do
			begin
				a := a + 1 ;
				b := b + 1 ;								
			end	
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id("i"),BinaryOp("*",Id("a"),IntLiteral(5)),BinaryOp("/",Id("b"),IntLiteral(10)),False,[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(1)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_statement_17(self):
        """function foo(): integer;
		begin
			for i := a * 5 downto b /10
			do
			begin
				a := a + 1 ;
				b := b + 1 ;
				break ;					
			end	
		end"""
        input = """function foo(): integer;
		begin
			for i := a * 5 downto b /10
			do
			begin
				a := a + 1 ;
				b := b + 1 ;								
				break ;									
			end	
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id("i"),BinaryOp("*",Id("a"),IntLiteral(5)),BinaryOp("/",Id("b"),IntLiteral(10)),False,[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(1))),Break()])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,363))

    def test_statement_18(self):
        """function foo(): integer;
		begin
			a := a + 1 ;
			return a;
		end"""
        input = """function foo(): integer;
		begin
			a := a + 1 ;
			return a;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Return(Id("a"))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test_statement_19(self):
        """function foo(): integer;
		begin
			a := a + 1 ;
			return a*6/9 + -2;
		end"""
        input = """function foo(): integer;
		begin
			a := a + 1 ;
			return a*6/9 + -2;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Return(BinaryOp("+",BinaryOp("/",BinaryOp("*",Id("a"),IntLiteral(6)),IntLiteral(9)),UnaryOp("-",IntLiteral(2))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,365))

    def test_statement_20(self):
        """function foo(): integer;
		begin
			a := a + 1 ;
			return ;
		end"""
        input = """function foo(): integer;
		begin
			a := a + 1 ;
			return ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Return()],IntType())]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test_statement_21(self):
        """function foo(): integer;
		begin
			with a: integer ;
			do
				a := a + 1 ;
		end"""
        input = """function foo(): integer;
		begin
			with a: integer ;
			do
				a := a + 1 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[With([VarDecl(Id("a"),IntType())],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,367))

    def test_statement_22(self):
        """function foo(): integer;
		begin
			a := 1.2e3 ;
		end"""
        input = """function foo(): integer;
		begin
			a := 1.2e3 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),FloatLiteral(1.2e3))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,368))

    def test_statement_23(self):
        """function foo(): integer;
		begin
			foo(3) ;
		end"""
        input = """function foo(): integer;
		begin
			foo(3) ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("foo"),[IntLiteral(3)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,369))

    def test_statement_24(self):
        """function foo(): integer;
		begin
			a ;= foo(3) + 5;
		end"""
        input = """function foo(): integer;
		begin
			a := foo(3) + 5;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(3)]),IntLiteral(5)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test_statement_25(self):
        """function foo(): integer;
		begin
			if a > 3 then
				if a < 7 then
					b := b + 2 ;
				else
					b := "huhuhu" ;
		end"""
        input = """function foo(): integer;
		begin
			if a > 3 then
				if a < 7 then
					b := b + 2 ;
				else
					b := "huhuhu" ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp(">",Id("a"),IntLiteral(3)),[If(BinaryOp("<",Id("a"),IntLiteral(7)),[Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(2)))],[Assign(Id("b"),StringLiteral("huhuhu"))])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test_statement_26(self):
        """function foo(): integer ;
		begin
			if a > 3 then
				if a < 7 then
					b := b + 2 ;
			else
					b := "huhuhu" ;
		end"""
        input = """function foo(): integer ;
		begin
			if a > 3 then
				if a < 7 then
					b := b + 2 ;
			else
					b := "huhuhu" ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp(">",Id("a"),IntLiteral(3)),[If(BinaryOp("<",Id("a"),IntLiteral(7)),[Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(2)))],[Assign(Id("b"),StringLiteral("huhuhu"))])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test_procedure_1(self):
        """procedure foo();
		begin
			if a > 3 then
				if a < 7 then
					b := b + 2 ;
			else
					b := "huhuhu" ;
		end"""
        input = """procedure foo();
		begin
			if a > 3 then
				if a < 7 then
					b := b + 2 ;
			else
					b := "huhuhu" ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp(">",Id("a"),IntLiteral(3)),[If(BinaryOp("<",Id("a"),IntLiteral(7)),[Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(2)))],[Assign(Id("b"),StringLiteral("huhuhu"))])])])]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_procedure_2(self):
        """procedure foo();
		begin
		end"""
        input = """procedure foo();
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_procedure_2(self):
        """procedure foo(a,b: integer; c: real);
		var x,y: real ;
		begin			
		end"""
        input = """procedure foo(a,b: integer; c: real);
		var x,y: real ;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType())],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType())],[])]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_procedure_3(self):
        """procedure foo(a,b: integer; c: real);
		var x,y: real ;		
		begin
			a := x + y ;
			b := c + x - y ;
		end"""
        input = """procedure foo(a,b: integer; c: real);
		var x,y: real ;
		begin
			a := x + y ;
			b := c + x - y ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType())],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType())],[Assign(Id("a"),BinaryOp("+",Id("x"),Id("y"))),Assign(Id("b"),BinaryOp("-",BinaryOp("+",Id("c"),Id("x")),Id("y")))])]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test_procedure_4(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			a := x + y ;
			b := c + x - y ;		
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			a := x + y ;
			b := c + x - y ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[Assign(Id("a"),BinaryOp("+",Id("x"),Id("y"))),Assign(Id("b"),BinaryOp("-",BinaryOp("+",Id("c"),Id("x")),Id("y")))])]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test_procedure_5(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			if x < 5 then
			begin
				x := y + z ;
				a := b - c ;
			end
			else
			begin
				x := y - z ;
				a := b + c ;			
			end
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			if x < 5 then
			begin
				x := y + z ;
				a := b - c ;
			end
			else
			begin
				x := y - z ;
				a := b + c ;			
			end
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[If(BinaryOp("<",Id("x"),IntLiteral(5)),[Assign(Id("x"),BinaryOp("+",Id("y"),Id("z"))),Assign(Id("a"),BinaryOp("-",Id("b"),Id("c")))],[Assign(Id("x"),BinaryOp("-",Id("y"),Id("z"))),Assign(Id("a"),BinaryOp("+",Id("b"),Id("c")))])])]))
        self.assertTrue(TestAST.test(input,expect,375))

    def test_complex_1(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			if x < 5 then
			begin
				x := y + z ;
				a := b - c ;
			end
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			if x < 5 then
			begin
				x := y + z ;
				a := b - c ;
			end
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[If(BinaryOp("<",Id("x"),IntLiteral(5)),[Assign(Id("x"),BinaryOp("+",Id("y"),Id("z"))),Assign(Id("a"),BinaryOp("-",Id("b"),Id("c")))],[])])]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test_complex_2(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			if x < 5 then
			begin
			if x < 5 then
				if z < 20 then
					if y < 3 then
						a := b + 1 ;
					else
						a := c + 1 ;
			end
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			if x < 5 then
				if z < 20 then
					if y < 3 then
						a := b + 1 ;
					else
						a := c + 1 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[If(BinaryOp("<",Id("x"),IntLiteral(5)),[If(BinaryOp("<",Id("z"),IntLiteral(20)),[If(BinaryOp("<",Id("y"),IntLiteral(3)),[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(1)))],[Assign(Id("a"),BinaryOp("+",Id("c"),IntLiteral(1)))])])])])]))
        self.assertTrue(TestAST.test(input,expect,377))

    def test_complex_3(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			if x < 5 then
			begin
				x := y + z ;
				a := b - c ;
			end
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			if x < 5 then
				a := b + 1 ;
			else
				if y < 10 then
					if z < 20 then
						b := b - 2 ; 
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[If(BinaryOp("<",Id("x"),IntLiteral(5)),[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(1)))],[If(BinaryOp("<",Id("y"),IntLiteral(10)),[If(BinaryOp("<",Id("z"),IntLiteral(20)),[Assign(Id("b"),BinaryOp("-",Id("b"),IntLiteral(2)))])])])])]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test_complex_4(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			if x < 5 then
				a := b + 1 ;
			else
				if y < 10 then
					if z < 20 then
						b := b - 2 ; 
					else
						c := c + 5 ;
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			if x < 5 then
				a := b + 1 ;
			else
				if y < 10 then
					if z < 20 then
						b := b - 2 ; 
					else
						c := c + 5 ;						
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[If(BinaryOp("<",Id("x"),IntLiteral(5)),[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(1)))],[If(BinaryOp("<",Id("y"),IntLiteral(10)),[If(BinaryOp("<",Id("z"),IntLiteral(20)),[Assign(Id("b"),BinaryOp("-",Id("b"),IntLiteral(2)))],[Assign(Id("c"),BinaryOp("+",Id("c"),IntLiteral(5)))])])])])]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test_complex_5(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			if x < 5 then
				a := b + 1 ;
			else
				if y < 10 then
					if z < 20 then
						b := b - 2 ; 
					else
						c := c + 5 ;
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			if x < 5 then
				a := b + 1 ;
			else
				if y < 10 then
					if z < 20 then
						b := b - 2 ; 
					else
						if c < 12 then
							c := c * 5 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[If(BinaryOp("<",Id("x"),IntLiteral(5)),[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(1)))],[If(BinaryOp("<",Id("y"),IntLiteral(10)),[If(BinaryOp("<",Id("z"),IntLiteral(20)),[Assign(Id("b"),BinaryOp("-",Id("b"),IntLiteral(2)))],[If(BinaryOp("<",Id("c"),IntLiteral(12)),[Assign(Id("c"),BinaryOp("*",Id("c"),IntLiteral(5)))])])])])])]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_procedure_6(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			a := x + y ;
			b := c + x - y ;		
		end"""
        input = """procedure foo(a,b: integer; c: array [-1 .. -5] of string);
		var x,y: real ;
		z: array [10 .. -20] of integer ;
		begin
			a := x + y ;
			b := c + x - y ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(-1,-5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,-20,IntType()))],[Assign(Id("a"),BinaryOp("+",Id("x"),Id("y"))),Assign(Id("b"),BinaryOp("-",BinaryOp("+",Id("c"),Id("x")),Id("y")))])]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_complex_6(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			while a < 5
				do
				begin
					x := x + 1 ;
					y := y + 1 ;
					z := z + 1 ;
				end
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			while a < 5
				do
				begin
					x := x + 1 ;
					y := y + 1 ;
					z := z + 1 ;
				end
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[While(BinaryOp("<",Id("a"),IntLiteral(5)),[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(1))),Assign(Id("z"),BinaryOp("+",Id("z"),IntLiteral(1)))])])]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_procedure_7(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			a := x + y ;
			b := c + x - y ;		
		end"""
        input = """procedure foo(a,b: integer; c: array [-1 .. -5] of string);
		var x,y: real ;
		z: array [10 .. -20] of integer ;
		begin
			begin
				a := a + 1 ;
			end
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(-1,-5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,-20,IntType()))],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test_procedure_8(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			return true ;
		end"""
        input = """procedure foo(a,b: integer; c: array [-1 .. -5] of string);
		var x,y: real ;
		z: array [10 .. -20] of integer ;
		begin
			return true ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(-1,-5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,-20,IntType()))],[Return(BooleanLiteral(True))])]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test_complex_7(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			while a < 5
				do
				begin
					while b < 11
					do
					begin
						while c < 12
						do
						begin
							x := x + 1 ;
							y := y + 1 ;
						end
					end
				end
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			while a < 5
				do
				begin
					while b < 11
					do
					begin
						while c < 12
						do
						begin
							x := x + 1 ;
							y := y + 1 ;
						end
					end
				end
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[While(BinaryOp("<",Id("a"),IntLiteral(5)),[While(BinaryOp("<",Id("b"),IntLiteral(11)),[While(BinaryOp("<",Id("c"),IntLiteral(12)),[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(1)))])])])])]))
        self.assertTrue(TestAST.test(input,expect,384))

    def test_complex_8(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			for a := 3 to 10
			do
			begin
				for b := 15 downto 9
				do
				begin
					for c := 10 downto 0
					do
					begin
						x := x + 1 ;
						y := y + 1 ;
					end
				end
			end		
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			for a := 3 to 10
			do
			begin
				for b := 15 downto 9
				do
				begin
					for c := 10 downto 0
					do
					begin
						x := x + 1 ;
						y := y + 1 ;
					end
				end
			end
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[For(Id("a"),IntLiteral(3),IntLiteral(10),True,[For(Id("b"),IntLiteral(15),IntLiteral(9),False,[For(Id("c"),IntLiteral(10),IntLiteral(0),False,[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(1)))])])])])]))
        self.assertTrue(TestAST.test(input,expect,385))

    def test_complex_9(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			for a :=  b*c - y/z to b/c + y*z
			do
				x := x + 1 ;		
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			for a :=  b*c - y/z to b/c + y*z
			do
				x := x + 1 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[For(Id("a"),BinaryOp("-",BinaryOp("*",Id("b"),Id("c")),BinaryOp("/",Id("y"),Id("z"))),BinaryOp("+",BinaryOp("/",Id("b"),Id("c")),BinaryOp("*",Id("y"),Id("z"))),True,[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])])]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test_complex_10(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			for a := 1 to 10
			do
			begin
				if a = 8 then
					break ;
				if a = 5 then
					continue ;				
				x := x + 1 ;
			end	
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			for a := 1 to 10
			do
			begin
				if a = 8 then
					break ;
				if a = 5 then
					continue ;				
				x := x + 1 ;
			end	
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[For(Id("a"),IntLiteral(1),IntLiteral(10),True,[If(BinaryOp("=",Id("a"),IntLiteral(8)),[Break()]),If(BinaryOp("=",Id("a"),IntLiteral(5)),[Continue()]),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])])]))
        self.assertTrue(TestAST.test(input,expect,387))

    def test_complex_11(self):
        """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;		
		begin
			for a :=  b*c - y/z to b/c + y*z
			do
				x := x + 1 ;		
		end"""
        input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			with d: integer;
			do
			begin
				with e,f: real ;
				do
				begin
					with g,h: real ; i,j: array [-1 .. 2] of integer ;
					do
					begin
						x := x + 1 ;
						y := y + 1 ;
					end
				end
			end
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[With([VarDecl(Id("d"),IntType())],[With([VarDecl(Id("e"),FloatType()),VarDecl(Id("f"),FloatType())],[With([VarDecl(Id("g"),FloatType()),VarDecl(Id("h"),FloatType()),VarDecl(Id("i"),ArrayType(-1,2,IntType())),VarDecl(Id("j"),ArrayType(-1,2,IntType()))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(1)))])])])])]))
        self.assertTrue(TestAST.test(input,expect,388))




		