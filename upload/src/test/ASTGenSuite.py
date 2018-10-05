import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_38(self):
        input = """procedure foo(); begin
                    while (a > b ) do 
                    begin
                        a :=3;
                    end
                 end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp(">",Id("a"),Id("b")),[Assign(Id("a"),IntLiteral(3))])])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_39(self):
        input = """procedure foo();
                    begin
                        a := 1 and then 2;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('a'),BinaryOp('andthen',IntLiteral(1),IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input,expect,301))
    

    def test_variable_decla_error(self):
        input=  """
                var d,b : array [    1 .. 5    ] of integer ;
                """
        expect = str(Program([VarDecl(Id("d"),ArrayType(1,5,IntType())),VarDecl(Id("b"),ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_variable_decla_array(self):
        input=  """
                var d , b : array [    1 .. 5    ] of integer ; a: string
                """
        expect = str(Program([VarDecl(Id("d"),ArrayType(1,5,IntType())),VarDecl(Id("b"),ArrayType(1,5,IntType())),VarDecl(Id("a"),StringType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_function_decla(self):
        input="""function foo (a : integer) : integer ;      
            begin
        
            end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_funcall(self):
        """"""
        input = """function foo(a,b:real):integer;
                    var x:integer;
                    Begin
                        foo();
                    end """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType())],[VarDecl(Id("x"),IntType())],[CallStmt(Id("foo"),[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_funcall_123(self):
        """function with para and body """
        input = """function foo(a,b:real):array[1 .. 100] of boolean;
                    Begin
                        foo(1);
                    end """

        input = """procedure main(a,b : integer; c:array[1 .. 100] of string);
                    var a : integer;
                    Begin
                        foo();
                        foo(2);
                        foo(3);
                    end """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,100,StringType()))],[VarDecl(Id("a"),IntType())],[CallStmt(Id("foo"),[]),CallStmt(Id("foo"),[IntLiteral(2)]),CallStmt(Id("foo"),[IntLiteral(3)])])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_stmt(self):
        """More complex program"""
        input = """function foo(a:real):INTEGER; 
        begin
            return 3;
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),FloatType())],[],[Return(IntLiteral(3))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_function_empty_para(self):
        input="""function foo () : array [ 1 .. 2 ] of integer ;
        
            begin
        
            end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,308))


    def test_var_declaration1(self):
        """Simple var declaration"""
        input = """var a,b:integer;
                    x,y:real;
                    z:string;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),StringType())]))
        self.assertTrue(TestAST.test(input,expect,309)) 
      
    def test_miss_var_declaration1(self):
        """Miss ) int main( {}"""
        input = """a:integer;"""
        expect = str(Program([]))        
        self.assertTrue(TestAST.test(input,expect,310))
    
    def test_var_declaration_array1(self):
        """More complex program"""
        input = """var d : array [1 .. 5] of integer ;"""
        expect = str(Program([VarDecl(Id("d"),ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_var_declaration_array2(self):
        """More complex program"""
        input = """var d,c : array [1 .. 5] of integer ;"""
        expect = str(Program([VarDecl(Id("d"),ArrayType(1,5,IntType())),VarDecl(Id("c"),ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_program_2(self):
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
        self.assertTrue(TestAST.test(input,expect,313))
    
    def test_for_veryfirst(self):
        """simple program"""
        input = """
            var i : integer ;
            function f( ) : integer ;
            begin

            end
            procedure main () ;begin end"""
        expect = str(Program([VarDecl(Id("i"),IntType()),FuncDecl(Id("f"),[],[],[],IntType()),FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,314))

    

    def test_call_program_7(self):
        input = """procedure foo();
                    begin
                        if a > 3 then a := 3;
                        else a := 1;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[If(BinaryOp('>',Id('a'),IntLiteral(3)),[Assign(Id('a'),IntLiteral(3))],[Assign(Id('a'),IntLiteral(1))])])]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_call_program_6(self):
        input = """procedure foo();
                    begin
                        begin
                            return b;
                        end
                        return a;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Return(Id('b')),Return(Id('a'))])]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_call_program_5(self):
        input = """procedure foo();
                    begin
                        a := 1 and then 2;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('a'),BinaryOp('andthen',IntLiteral(1),IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input,expect,317))
    
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
        self.assertTrue(TestAST.test(input,expect,318))

    def test_function_declare_1(self):
        """function foo(): integer;
		begin
		end"""
        input = """function foo(): integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_function_declare_2(self):
        """function foo(): real;
		begin
		end"""
        input = """function foo(): real;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_function_declare_3(self):
        """function foo(): string;
		begin
		end"""
        input = """function foo(): string;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],StringType())]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_function_declare_4(self):
        """function foo(): boolean;
		begin
		end"""
        input = """function foo(): boolean;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_function_declare_5(self):
        """function foo(): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_function_declare_6(self):
        """function foo(a: integer): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(a: integer): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_function_declare_7(self):
        """function foo(a,b: integer): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(a,b: integer): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,325))
		
    def test_function_declare_8(self):
        """function foo(a,b: integer ; c: real): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(a,b: integer ; c: real): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType())],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,326))

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
        self.assertTrue(TestAST.test(input,expect,327))

    def test_function_declare_15(self):
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
        self.assertTrue(TestAST.test(input,expect,328))

    def test_function_declare_329(self):
        """function foo(a: integer): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(a: integer): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,329))

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
        self.assertTrue(TestAST.test(input,expect,330))


    def test_assignment_3(self):
        """test"""
        input = """function foo(): integer;
		begin
			a:=exp;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),Id("exp"))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,331))

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
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("andthen",Id("b"),Id("c")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,332))

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
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("orelse",Id("b"),Id("c")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,333))

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
        self.assertTrue(TestAST.test(input,expect,334))

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
        self.assertTrue(TestAST.test(input,expect,335))

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
        self.assertTrue(TestAST.test(input,expect,336))

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
        self.assertTrue(TestAST.test(input,expect,337))

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
        self.assertTrue(TestAST.test(input,expect,338))

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
        self.assertTrue(TestAST.test(input,expect,339))

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
        self.assertTrue(TestAST.test(input,expect,340))

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
        self.assertTrue(TestAST.test(input,expect,341))

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
        self.assertTrue(TestAST.test(input,expect,342))

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
        self.assertTrue(TestAST.test(input,expect,343))

    def test_expression_13(self):
        """"""
        input = """function foo(): integer;
		begin
			a:=5 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),IntLiteral(5))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_expression_14(self):
        """test"""
        input = """function foo(): integer;
		begin
			b[5] := c + 6 ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(ArrayCell(Id("b"),IntLiteral(5)),BinaryOp("+",Id("c"),IntLiteral(6)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,345))

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
        self.assertTrue(TestAST.test(input,expect,346))

    def test_expression_347(self):
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
        self.assertTrue(TestAST.test(input,expect,347))

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
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("x"),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),Id("x")),Assign(ArrayCell(Id("b"),IntLiteral(10)),ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3))),Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(10)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,348))

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

    def test_statement_221(self):
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
        self.assertTrue(TestAST.test(input,expect,352))

    def test_statement_31(self):
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
        self.assertTrue(TestAST.test(input,expect,353))

    def test_statement_313(self):
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

    def test_expression_355(self):
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
        self.assertTrue(TestAST.test(input,expect,355))

    def test_statement_412(self):
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

    def test_statement_5asf(self):
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

    def test_statement_6dh(self):
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

    def test_statement_359(self):
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

    def test_statement_360(self):
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
        self.assertTrue(TestAST.test(input,expect,360))

    def test_complex_1asdg(self):
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
        self.assertTrue(TestAST.test(input,expect,361))

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
        self.assertTrue(TestAST.test(input,expect,362))

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
        self.assertTrue(TestAST.test(input,expect,363))

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
        self.assertTrue(TestAST.test(input,expect,364))

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
        self.assertTrue(TestAST.test(input,expect,365))

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
        self.assertTrue(TestAST.test(input,expect,366))

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
        self.assertTrue(TestAST.test(input,expect,367))

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
        self.assertTrue(TestAST.test(input,expect,368))

#--------------------------------------------
    def test_function_declare_369(self):
        """function foo(): integer;
		begin
		end"""
        input = """function foo(): integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,369))

    def test_function_declare_370(self):
        """function foo(): real;
		begin
		end"""
        input = """function foo(): real;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,370))

		
		
    def test_function_declare_371(self):
        """function foo(): string;
		begin
		end"""
        input = """function foo(): string;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],StringType())]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test_function_declare_372(self):
        """function foo(): boolean;
		begin
		end"""
        input = """function foo(): boolean;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_function_declare_373(self):
        """function foo(): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test_function_declare_374(self):
        """function foo(a: integer): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(a: integer): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test_function_declare_375(self):
        """function foo(a,b: integer): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(a,b: integer): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,375))
		
    def test_function_declare_376(self):
        """function foo(a,b: integer ; c: real): array [1 .. 5] of integer;
		begin
		end"""
        input = """function foo(a,b: integer ; c: real): array [1 .. 5] of integer;
		begin
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType())],[],[],ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,376))

#============================
    def test_function_declare_377(self):
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
        self.assertTrue(TestAST.test(input,expect,377))

    def test_function_declare_378(self):
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
        self.assertTrue(TestAST.test(input,expect,378))

    def test_expression_379(self):
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
        self.assertTrue(TestAST.test(input,expect,379))

    def test_assignment_380(self):
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
        self.assertTrue(TestAST.test(input,expect,380))


    def test_assignment_381(self):
        """test"""
        input = """function foo(): integer;
		begin
			a[2] := 6;
		end
		"""
        input = """function foo(): integer;
		begin
			a[2] := 6;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(6))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_expression_382(self):
        """function foo(): integer;
		begin
			a := b and then c ;
		end"""
        input = """function foo(): integer;
		begin
			a := b and then c ;
		end
		"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("andthen",Id("b"),Id("c")))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,382))



#///////////////////////////////////////
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
        self.assertTrue(TestAST.test(input,expect,389))

    def test_26(self):
        input = """var a:integer;
                       b:real;
                       c:boolean;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test_27(self):
        input = """var a:array[1 .. 2] of real;
                       s:string;
                       """
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,2,FloatType())),VarDecl(Id("s"),StringType())]))
        self.assertTrue(TestAST.test(input,expect,391))


    def test_28(self):
        input = """var a:integer;
                       a,b:array[1 .. 5] of integer;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("a"),ArrayType(1,5,IntType())),VarDecl(Id("b"),ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,392))

    def test_29(self):
        input = """var a:integer;
                       c,d:array[-1 .. 6] of string;
        """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("c"),ArrayType(-1,6,StringType())),VarDecl(Id("d"),ArrayType(-1,6,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test_30(self):
        input = """var a : integer;
                b,c:real;
                c:array[1 .. 100] of boolean;
                d:string;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),
        VarDecl(Id("c"),FloatType()),VarDecl(Id("c"),ArrayType(1,100,BoolType())),VarDecl(Id("d"),StringType())]))
        self.assertTrue(TestAST.test(input,expect,394))

    def test_31(self):
        input="""function foo (a , b : integer ; c : real ) : array [ 1 .. 2 ] of integer ;
            var x , y : real ;
            begin
            end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType())],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType())],[],ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,395))

    def test_32(self):
        input = """
        procedure main();
        begin
            with i :integer; do a := 1;
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("i"),IntType())],[Assign(Id("a"),IntLiteral(1))])])]))
        self.assertTrue(TestAST.test(input,expect,396))

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
        self.assertTrue(TestAST.test(input,expect,397))

    def test_34(self):
        input = """procedure foo();
                    begin
                        a := 1 and then 2 or else 3 > 4;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('a'),BinaryOp('orelse',BinaryOp('andthen',IntLiteral(1),IntLiteral(2)),BinaryOp('>',IntLiteral(3),IntLiteral(4))))])]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test_35(self):
        input = """procedure foo();
                    begin
                        c := a and then putIntLn( i ) or else c and then d ;
                    end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id("c"),BinaryOp("andthen",BinaryOp("orelse",BinaryOp("andthen",Id("a"),CallExpr(Id('putIntLn'),[Id('i')])),Id("c")),Id("d")))])]))
        self.assertTrue(TestAST.test(input,expect,399))

    def test_36(self):
        input = """procedure main();begin begin end end"""
        expect = str (Program([FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,400))

    def test_37(self):
        input = """procedure foo(); begin begin return b; end return c; end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Return(Id("b")),Return(Id("c"))])]))
        self.assertTrue(TestAST.test(input,expect,401))

    # def test_if6(self):
    #     input = """procedure main();
    #         var a : integer;
    #         Begin
    #         if True then a:=2;
            
    #         end"""
    #     expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[If(BooleanLiteral(True),[If(BooleanLiteral(False),[Assign(Id("a"),BooleanLiteral(False))],[Assign(Id("a"),BooleanLiteral(True))])],[])],VoidType())]))
    #     self.assertTrue(TestAST.test(input,expect,402))


    


