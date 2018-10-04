import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    
    def test_variable_decla(self):
        """test variable declar many"""
        input="""var a,b ,c : integer ;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_variable_decla_list(self):
        """test variable declar many"""
        input="""var a,b ,c : integer ; e,f : real ;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType()),VarDecl(Id("e"),FloatType()),VarDecl(Id("f"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_variable_decla_error(self):
        """test variable declar many"""
        input="""var d,b : array [    1 .. 5    ] of integer ;"""
        expect = str(Program([VarDecl(Id("d"),ArrayType(1,5,IntType())),VarDecl(Id("b"),ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_variable_decla_array(self):
        """test variable declar many"""
        input="""var d , b : array [    1 .. 5    ] of integer ; a: string"""
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
        self.assertTrue(TestAST.test(input,expect,305))

    def test_stmt(self):
        """More complex program"""
        input = """function foo(a:real):INTEGER; 
        begin
            return 3;
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),FloatType())],[],[Return(IntLiteral(3))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_function_empty_para(self):
        """test function declar """
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            
            begin
            
            end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,307))

    # def test_wrong_miss_close(self):
    #     """test function declar """
    #     input="""function foo ( : array [ 1 .. 2 ] of integer ;
    #         var x , y : real ; 
    #         begin
            
    #         end"""
    #     expect = str()
    #     self.assertTrue(TestAST.test(input,expect,308))

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
    # def test_func_declaration(self):
    #     """More complex program"""
    #     input = """function foo(i:integer):real;
    #                var s:real;
    #                 begin
    #                 end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("i"),IntType())],[VarDecl(Id("s"),FloatType())],[],FloatType())]))
    #     self.assertTrue(TestAST.test(input,expect,313)) 
    # def test_for_veryfirst(self):
    #     """simple program"""
    #     input = """
    #         var i : integer ;
    #         function f( ) : integer ;
    #         begin

    #         end
    #         procedure main () ;begin end"""
    #     expect = str()
    #     self.assertTrue(TestAST.test(input,expect,314))
    # def test_miss_colon(self):
    #     """test wrong miss colon """
    #     input="""function foo ()  array [ 1 .. 2 ] of integer ;
    #         var x , y : real ; 
    #         begin
            
    #         end"""
    #     expect = str()ray"
    #     self.assertTrue(TestAST.test(input,expect,315))
    # def test_wrong_miss_body(self):
    #     """test wrong miss body """
    #     input="""function foo () : array [ 1 .. 2 ] of integer ;
    #         var x , y : real ;  """
           
    #     expect = str()ne 2 col 32: <EOF>"
    #     self.assertTrue(TestAST.test(input,expect,316))
    # def test_miss_return(self):
    #     """ test wrong miss return """
    #     input="""function foo ();
    #         var x , y : real ; 
    #         begin
            
    #         end"""
    #     expect = str()
    #     self.assertTrue(TestAST.test(input,expect,317))
    # def test_miss_semi(self):
    #     """test wrong miss semi """
    #     input="""function foo () : array [ 1 .. 2 ] of integer 
    #         var x , y : real ;
    #         begin
            
    #         end"""
    #     expect = str()ne 2 col 12: var"
    #     self.assertTrue(TestAST.test(input,expect,318))
    # def test_for_nomain(self):
    #     """simple program no main"""
    #     input = """var i : integer ;
    #         function f( ) : integer ;
    #         begin

    #         end"""
    #     expect = str()
    #     self.assertTrue(TestAST.test(input,expect,319))

    # def test_for_function_not_end(self):
    #     """no end function"""
    #     input = """var i : integer ;
    #         function f( ) : integer ;
    #         begin

    #         """
    #     expect = str()ne 5 col 12: <EOF>"
    #     self.assertTrue(TestAST.test(input,expect,320))

