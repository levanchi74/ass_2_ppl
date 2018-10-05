import unittest
from TestUtils import TestParser
class ParserSuite(unittest.TestCase):

    def test_variable_decla(self):
        """test variable declar many"""
        input="""var a,b ,c : integer ;"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,300))

    def test_variable_decla_list(self):
        """test variable declar many"""
        input="""var a,b ,c : integer ; e,f : real ;"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,301))
    def test_variable_decla_error(self):
        """test variable declar many"""
        input="""d,b : array [    1 .. 5    ] of integer ;"""
        expect = str()        
        self.assertTrue(TestAST.test(input,expect,302))
    def test_variable_decla_array(self):
        """test variable declar many"""
        input="""var d , b : array [    1 .. 5    ] of integer ;"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,303))
    def test_variable_decla_error_1(self):
        """test variable declar many"""
        input="""d , b : array [    1 .. 5    ] of integer ;"""
        expect = str()        
        self.assertTrue(TestAST.test(input,expect,304))
    #test function declar
    def test_function_decla(self):
        """test function declar """
        input="""function foo (a , b : integer ; c : real ) : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,305))
    def test_function_decla_error_(self):
        """test function declar para """
        input="""function foo (a , b : integer  ;) : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,306))
    def test_function_empty_para(self):
        """test function declar """
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,307))
    def test_wrong_miss_close(self):
        """test function declar """
        input="""function foo ( : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,308))
    def test_var_declaration1(self):
        """Simple var declaration"""
        input = """var a,b:integer;
                       x,y:real;
                       z:string;"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,309))   
    def test_miss_var_declaration1(self):
        """Miss ) int main( {}"""
        input = """a:integer;"""
        expect = str()        
        self.assertTrue(TestAST.test(input,expect,310))

    def test_var_declaration_array1(self):
        """More complex program"""
        input = """var d : array [1 .. 5] of integer ;"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,311))

    def test_var_declaration_array2(self):
        """More complex program"""
        input = """var d,c : array [1 .. 5] of integer ;"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,312))
    def test_func_declaration(self):
        """More complex program"""
        input = """function foo(i:integer):real;
                   var s:real;
                    begin
                    end"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,313)) 
    def test_for_veryfirst(self):
        """simple program"""
        input = """var i : integer ;
            function f( ) : integer ;
            begin

            end
            procedure main () ;begin end"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,314))
    def test_miss_colon(self):
        """test wrong miss colon """
        input="""function foo ()  array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = str()ray"
        self.assertTrue(TestAST.test(input,expect,315))
    def test_wrong_miss_body(self):
        """test wrong miss body """
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real ;  """
           
        expect = str()ne 2 col 32: <EOF>"
        self.assertTrue(TestAST.test(input,expect,316))
    def test_miss_return(self):
        """ test wrong miss return """
        input="""function foo ();
            var x , y : real ; 
            begin
            
            end"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,317))
    def test_miss_semi(self):
        """test wrong miss semi """
        input="""function foo () : array [ 1 .. 2 ] of integer 
            var x , y : real ;
            begin
            
            end"""
        expect = str()ne 2 col 12: var"
        self.assertTrue(TestAST.test(input,expect,318))
    def test_for_nomain(self):
        """simple program no main"""
        input = """var i : integer ;
            function f( ) : integer ;
            begin

            end"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,319))

    def test_for_function_not_end(self):
        """no end function"""
        input = """var i : integer ;
            function f( ) : integer ;
            begin

            """
        expect = str()ne 5 col 12: <EOF>"
        self.assertTrue(TestAST.test(input,expect,320))

    def test_for_function(self):
        """just function"""
        input = """
            function f( ) : integer ;
            begin
            end
            """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,321))

    def test_for_function_not_compoundstmt(self):
        """no end function no compound statement"""
        input = """
            function f( ) : integer ;

            """
        expect = str()ne 4 col 12: <EOF>"
        self.assertTrue(TestAST.test(input,expect,322))

    def test_for_function_not_returntype(self):
        """function no return type"""
        input = """
            function f( ) ;
            begin
            end
            """
        expect = str()ne 2 col 26: ;"
        self.assertTrue(TestAST.test(input,expect,323))

    def test_for_function_no_semi(self):
        """function no semi"""
        input = """
            function f( ) : string
            begin
            end
            """
        expect = str()ne 3 col 12: begin"
        self.assertTrue(TestAST.test(input,expect,324))
    def test_for_function_array1(self):
        """function return array type"""
        input = """
            function f( ) : array
            begin
            end
            """
        expect = str()ne 3 col 12: begin"
        self.assertTrue(TestAST.test(input,expect,325))

    def test_for_function_array2(self):
        """function return array type"""
        input = """
            function f( ) : array [1 .. 5] of integer;
            begin
            end
            """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,326))

    def test_for_function_array3(self):
        """function return array type"""
        input = """
            function f( ) : array [1 .. 5] of integer;
            begin
            end
            """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,327))

    def test_for_function_array4(self):
        """function return array type"""
        input = """
            function f( ) : array [1 .. 5] of integer;
            begin
            end
            """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,328))

    def test_for_procedure(self):
        """function procedure"""
        input = """
            procedure f( );
            begin
            end
            """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,329))

    def test_for_procedure_with_returntype(self):
        """function procedure with return type"""
        input = """
            procedure f( ) : boolean;
            begin
            end
            """
        expect = str()ne 2 col 27: :"
        self.assertTrue(TestAST.test(input,expect,330))

    def test_for_procedure2(self):
        """function procedure"""
        input = """
            procedure f(a,b:integer;c:real);
            begin
            end
            """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,331))

    def test_for_procedure3(self):
        """function procedure"""
        input = """
            procedure f(a,b,,c:integer;c:real);
            begin
            end
            """
        expect = str()ne 2 col 28: ,"
        self.assertTrue(TestAST.test(input,expect,332))

    def test_for_procedure4(self):
        """function procedure"""
        input = """
            procedure f(a,b,c:integer;c:array);
            begin
            end
            """
        expect = str()ne 2 col 45: )"
        self.assertTrue(TestAST.test(input,expect,333))

    def test_for_procedure5(self):
        """function procedure"""
        input = """
            procedure f(a,b,c:integer;c:real);
            var x , y :real;
            begin
            end
            """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,334))

    def test_for_procedure6(self):
        """function procedure"""
        input = """
            procedure f(a,b,c:integer;c:real);

            """
        expect = str()ne 4 col 12: <EOF>"
        self.assertTrue(TestAST.test(input,expect,335))

    def test_for_procedure_in_function(self):
        """function procedure"""
        input = """
            function foo (i:integer):real;
            procedure child_of_foo (f :real)
                begin
                end
            begin
            end
            """
        expect = str()ne 3 col 12: procedure"
        self.assertTrue(TestAST.test(input,expect,336))

    def test_for_vardecl1(self):
        """var declaration"""
        input = """
            var a , b , c : integer ;
                d : array [ 1 .. 5 ] of integer ;
                e , f : real ;
            """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,337))   
    def test_assignment_stmt(self):
        """test_assignment_stmt"""
        input= """procedure abc ();
            var x , y : real ; 
            begin
                a:=12;
            end"""
        expect='successful'
        self.assertTrue(TestAST.test(input,expect,338))
    def test_assignment_stmt_many(self):
        """test_assignment_stmt_many"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                a:=b:=c:=d:=12;
            end"""
        expect='successful'
        self.assertTrue(TestAST.test(input,expect,339))
    def test_if_statement1(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    else foo();
                   END"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,340))
    def test_if_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    else if (1<2)<>(2<3) then x:=1 ;
                    else foo(a+1,3);
                   END"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,341))
    def test_if_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    if (1<2) then beGin x:=1 ; end
                    else foo(a+1,3);
                   END"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,342))
    def test_if_statement4(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if a>1 then beGin
                        a:=1 ;
                        if 1=1 then a:=b;
                        
                    end
                    END"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,343))
    def test_while_statement1(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin end
                   END"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,344))
    def test_while_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin
                        if(a=1) then x:=1;
                        foo();
                    end
                   END"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,345))
    def test_while_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin
                        while(1) do x:=1;
                    end
                   END"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,346))
    def test_break_state(self):
        """test_break_state"""
        input= """procedure break_state ();
        var x , y : real ; 
            begin
                while  a =4 do  break;
            end"""
        expect='successful'
        self.assertTrue(TestAST.test(input,expect,347))
    def test_break_state_miss_semi(self):
        """test_break_state_miss_semi"""
        input= """procedure break_state ();
        var x , y : real ; 
            begin
                while  a =4 do  break;
            end"""
        expect='successful'
        self.assertTrue(TestAST.test(input,expect,348))
    def test_continue_state_withfor(self):
        """test_continue_state_withfor"""
        input= """procedure continue_state();
        var x , y : real ; 
            begin
                for  a :=4 to 23 do  continue;
            end"""
        expect='successful'
        self.assertTrue(TestAST.test(input,expect,349))
    def test_continue_state_withwhile(self):
        """test_continue_state_withwhile"""
        input= """procedure continue_state();
        var x , y : real ; 
            begin
                while  a =4 do  continue;;
            end"""
        expect='Error on line 4 col 41: ;'
        self.assertTrue(TestAST.test(input,expect,350))
    def test_continue_state_wrong_stmt(self):
        """test_continue_state_wrong_stmt"""
        input= """procedure continue_state();
        var x , y : real ; 
            begin
                while  a =4 do  coninue+fg**3;;
            end"""
        expect='Error on line 4 col 39: +'
        self.assertTrue(TestAST.test(input,expect,351))
    def test_with_statement1(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do
                    d := c [a] + b ;
                   END"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,352))
    def test_with_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    d := c [a] + b ;
                    foo();foo1(a,b,c);
                    end
                   END"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,353))
    def test_with_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    d := c [a] + b ;
                    foo();foo1(a,b,c);
                    with a , b : integer ; do begin
                        foo2(a,b,"anc");
                    end
                    end
                   END"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,354))
    def test_return_state_non_expr(self):
        """test_return_state_non_expr"""
        input= """procedure return_state();
        var x , y : real ; 
            begin
                return ;
            end"""
        expect='successful'
        self.assertTrue(TestAST.test(input,expect,355))
    def test_return_state_miss_semi(self):
        """test_return_state_non_expr"""
        input= """procedure return_state();
        var x , y : real ; 
            begin
                return 
            end"""
        expect='Error on line 5 col 12: end'
        self.assertTrue(TestAST.test(input,expect,356))
    def test_call_state_simple(self):
        """test_call_state_simple"""
        input= """procedure call_state();
        var x , y : real ; 
            begin
                foo () ;
            end"""
        expect='successful'
        self.assertTrue(TestAST.test(input,expect,357))
    def test_call_state_many_para(self):
        """test_call_state_many_para"""
        input= """procedure call_state();
        var x , y : real ; 
            begin
                foo (23+45, hello) ;
            end"""
        expect='successful'
        self.assertTrue(TestAST.test(input,expect,358))
    def test_call_statement2(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,a<>1,a[1]);
                    return 1;
                   END"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,359))
    def test_call_statement3(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,x and then y,a[1],foo(1,3)[m+1]);
                    return foo2();
                   END"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,360))
    def test_compound_state(self):
        """test_compound_state"""
        input= """procedure compound_state();
           var x , y : real ; 
            begin
                
            end"""
        expect="successful"
        self.assertTrue(TestAST.test(input,expect,361))
    def test_error(self):
        """test_compound_state"""
        input= """function ok(i : integer):boolean;
                var k : integer;
                begin
                 ok := true;
                 for k := 2 to i div 2 do
                  if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then
                   begin
                    ok := false;
                    exit();
                   end
                end"""
        expect="successful"
        self.assertTrue(TestAST.test(input,expect,362))
    def test_case_insensitive(self):
        """test_case_insensitive"""
        input="""FuNctIon _ADVCDfoo     (): array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,363))
    def test_wrong_type_return(self):
        """test_wrong_type_return"""
        input="""function _ADVCDfoo     (): array [ 1 .. 2 ] of array [ 1 .. 2 ] ;
            var x , y : real ; 
            begin
            
            end"""
        expect = str()ray"
        self.assertTrue(TestAST.test(input,expect,364))
    def test_case_insensitive2(self):
        """test_case_insensitive"""
        input="""prOceDure _ADVCDfoo ();
            var x , y : real ; 
            begin
            
            end"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,365))
    def test_wrong_redundancy_colon(self):
        """test_wrong_redundancy_colon"""
        input="""procedure abc (): array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,366))
    def test_wrong_miss_semi_produre(self):
        """test_wrong_redundancy_colon"""
        input="""procedure abc ()
            var x , y : real ; 
            begin
            
            end"""
        expect = str()ne 2 col 12: var"
        self.assertTrue(TestAST.test(input,expect,367))
    def test_assign_stmt_with_expr(self):
        """test_assign_stmt_with_expr"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                a:=b:=c:=d:=(12+3);
            end"""
        expect='successful'
        self.assertTrue(TestAST.test(input,expect,368))
    def test_assign_stmt_with_funcall(self):
        """test_assign_stmt_with_expr"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                a:=b:=c:=d:=foo();
            end"""
        expect='successful'
        self.assertTrue(TestAST.test(input,expect,369))
    def test_aProgram1(self):
        input = """
                procedure test1() ;
                begin
                   if a=b then
                   begin
                         b := c ;
                         if(e <> f) then foo(a,c) ;
                   end
                end
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,370))
    def test_aProgram2(self):
        input = """
                procedure test2() ;
                begin
                   if a=b then if c=d then while (d=e) do
                   beGin
                   eND
               else c := 1;
                end
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,371))
    
    def test_aProgram3(self):
        input = """
                proceDure Hello(a, b:integer);
                begin
                    a := b + c;
                    writeln("Hello, world!");
                end
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,372))

    def test_aProgram4(self):
        input = """
                Var
                    Num1, Num2, Sum : Integer;
                Procedure concaheo(a, c:Real);
                Begin {no semicolon}
                    Write("nhap so 1:");
                    Readln(Num1);
                    Writeln("nhap so 2:");
                    Readln(Num2);
                    Sum := Num1 + Num2; {phep cong}
                    Write(Sum);
                    Readln();
                End
        """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,373))

    def test_aProgram5(self):
        input = """
                Var name, surname: String;
                Procedure Main();
                Begin
                   write("Nhap ten cua ban:");
                   readln(name);
                   write("Nhap ho cua ban:");
                   readln(surname);
                   writeln();(*new line*)
                   writeln();//new line}
                   writeln("Ten day du cua ban la : ",name," ",surname);
                   readln();
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,374))

    def test_aProgram6(self):
        input = """
                Var PD, Dname, Cmodel : String;
                CostPD, TCostPD, Distance : Real;
                {real is a decimal (described later on)}
                Procedure main();
                Begin
                    textbackground(brown); {background colour}
                    ClrScr(); {Clear screen with a brown colour. Try run the program without this..}
                    TextColor(lightgreen); {text colour}
                    TCostPD := 0;
                    Writeln("This program prompts you to input the cost per litre of");
                    Writeln("the petrol/diesel you spend in and the average distance you travel");
                    Writeln("with your car every week. Then, the computer calculates the total cost");
                    Writeln("you spend in fuel every week.");
                    Readkey(); {program move on as soon as a key is pressed}
                    ClrScr(); {short for clear screen}
                    GotoXy(28,3); {move to a position on the screen: x (horizontal), y (vertical)}
                    Readln();
                End
        """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,375))
    def test_aProgram7(self):
        input = """
                var i: integer ;
                function f(): integer ;
                begin
                   return 200;
                end
                procedure main() ;
                var
                   main: integer ;
                begin
                   main := f() ;
                   putIntLn(main);
                   with
                        i: integer;
                        main: integer;
                        f: integer;
                   do begin
                        main := f := i:= 100;
                        putIntLn (i);
                        putIntLn (main );
                        putIntLn (f);
                   end
                   putIntLn (main);
                end
                var g: real ;
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,376))
    def test_aProgram8(self):
        input = """
                procedure main() ;
                beGin
                 a[b[2]] := 10;
                 foo();
                 return ;
                eND
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,377))
    
    def test_aProgram9(self):
        input = """
                procedure main() ;
                var a: array[0 .. 5] of integer;
                 i,j,temp: integer;
                beGin
                    for i := 0 to n - 2 do
                        for j:= i+1 to n-1 do
                            if(a[i]>a[j]) then beGin
                                temp := a[i];
                                a[i] := a[j];
                                a[j] := temp;
                            eND
                    print(a);
                eND
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,378))
    def test_aProgram10(self):
        input = """
                procedure main() ;
                beGin
                 if a=b then if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                eND
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,379))
    def test_aProgram11(self):
        input = """
                function sum_real_array(a: array[0 .. 5] of real;n:integer):real;
                var i:integer;s:real;
                beGin
                    s:=0.;
                    for i:=n-1 doWnTO 0 do s:=s+a[i];
                    reTuRn s;
                eND
                procedure main() ;
                var a: array[0 .. 5] of real; n:integer;
                beGin
                    Writeln("Sum of real array: "+sum_real_array(a,n));
                eND
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,380))
    def test_aProgram12(self):
        input = """
                Procedure NhapMang1C(A : array[0 .. 10] of integer;N:Integer);
                Var i: Integer;
                Begin
                Write("So luong phan tu:");
                Readln( N);
                For i:=0 to N do
                    Begin
                        Write("Nhap phan tu thu", i," ");
                        Readln( A[i] );
                    End
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,381))
    
    def test_aProgram13(self):
        input = """
                Function LaSoNT(N:Integer) :Integer;
                Var i:Integer;
                Begin
                 For i:=2 to N-1 do
                  If(N mod i = 0) then
                    return 0;
                  Else
                    return 1;
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,382))
    def test_aProgram14(self):
        input = """
                Function DemPtuX(A:array[0 .. 10] of integer; N,X : Integer) : Integer;
                Var i , Count : Integer;
                Begin
                 Count := 0;
                 For i:=0 to N do
                  If ( A[i] = X ) then
                   Count := Count + 1;
                 return Count;
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,383))
    def test_aProgram15(self):
        input = """
                Function Tong_So_Chia_Het_Cho5(A:array[0 .. 10] of integer ; N:Integer):Integer;
                Var S,i :Integer;
                Begin
                    S:=0;
                    For i:=0 to N do
                    If(A[i] mod 5=0) then
                    S := S+A[i];
                    return S;
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,384))
    def test_aProgram16(self):
        input = """
                Procedure ThayTheTatCa (A:array[0 .. 10] of integer;N, x,y:Integer);
                Var i:Integer;
                Begin
                 For i:=0 to N do
                  If(A[i] = x) then { Tim thay x ==> thay the thanh y }
                  A[i] := y;
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,385))
    def test_aProgram17(self):
        input = """
                Procedure ThayTheBangTong(A:array[0 .. 10] of integer; N:Integer; X, Y:Integer);
                Var i,k:Integer;
                Begin
                 For i:=0 to N do
                 If( (A[i-1]+A[i]) mod 10 = 0) then
                 Begin
                  k := (A[i-1]+A[i]);
                  A[i-1] := k;
                  A[i] := k;
                 End
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,386))
    def test_aProgram18(self):
        input = """
                Function KtraMangTang ( A:array[0 .. 10] of REAL; N :Integer) : Boolean;
                Var Flag : Boolean;
                 i :Integer;
                Begin
                 Flag := True;
                 i:= 0;
                 while(i<n) do begin
                  If(A[i] < A[i-1]) Then
                   Flag :=False; { Cham dut kiem tra, ket qua qua trinh : khong tang }
                  i:=i+1;
                 end
                 return Flag;
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,387))
    def test_aProgram19(self):
        input = """
                Function KtraMangCapSoCong (A:Mang20;  N:Integer; k:Integer):Boolean;
                Var flag :boolean;
                i :Integer;
                Begin
                 for i:=1 to N do
                 if(A[i] <> A[i-1] + k) then
                  flag:=false;     // Cham dut, ket qua: khong phai
                 return flag; {Ket qua kiem tra la mang cap so cong}
                End
                """
        expect = str()ne 2 col 46: Mang20"
        self.assertTrue(TestAST.test(input,expect,388))
    def test_aProgram20(self):
        input = """
                Function KtraDoiXung (A:array[0 .. 10] of REAL; N:Integer ) : Boolean;
                Var Flag:Boolean;
                    i :Integer;
                Begin
                 Flag:=True;
                 For  i :=1 to N do
                 If(A[i] <> A[N-i  +1]) Then
                 Flag :=False;       { Cham dut kiem tra, ket qua qua trinh : khong doi xung }
                 return flag;
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,389))
    def test_aProgram21(self):
        input = """
                Procedure ChenPhanTu(A:array[0 .. 10] of REAL;N: Integer; k, X:Integer);
                Var i :Integer;
                Begin
                 For i:=N downto k+ 1 do
                  A[i] := A[i-1];
                 A[k] := X;
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,390))
    def test_aProgram22(self):
        input = """
                function gt(x:integer):integer;
                begin
                if x = 0 then
                 return 1;
                else
                 return x*gt(x-1);
                end
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,391))
    def test_aProgram23(self):
        input = """
                function fibo(x: integer): integer;
                var f1,f2: integer;
                Begin
                 if x<=2 then
                  return 1;
                 else
                  return fibo(x-2)+ fibo(x-1);
                end
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,392))
    def test_aProgram24(self):
        input = """
                function ok(i : integer):boolean;
                var k : integer;
                begin
                 ok := true;
                 for k := 2 to i div 2 do
                  if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then
                   begin
                    ok := false;
                    exit();
                   end
                end
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,393))
    
    def test_aProgram25(self):
        input = """
                Function UCLN(m,n:integer):integer;
                Begin
                 If(m=n) then RETURN m ;
                 else
                  If (m>n) then return UCLN(m-n,n);
                  else return UCLN(m,n-m);
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,394))
    def test_aProgram26(self):
        input = """
                Var r,dt,cv:real;
                pROCEDURE main() ;
                Begin
                 Clrscr();
                 Writeln("TINH DIEN TICH & CHU VI HINH TRON:");
                 Writeln("--------------------------------------------------");
                 Write ("Nhap ban kinh R="); readln(r);
                 dt:=pi*r*r;
                 cv:=2*pi*r;
                 Writeln("Dien tich hinh tron la:",dt);
                 Writeln("Chu vi hinh tron la:",cv);
                 Readln();
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,395))
    def test_aProgram27(self):
        input = """
                Procedure Daoso(n: integer);
                Begin
                 Assign(f,fo);
                  Rewrite(f);
                 If n > 0 then
                  Begin
                  Write(f,n mod 10);
                  Daoso(n div 10);
                  End
                 Close(f);
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,396))
    def test_aProgram28(self):
        input = """
                pROCEDURE main() ;
                Var a,b,x:real;
                Begin
                Clrscr();
                Writeln("GIAI PHUONG TRINH BAC NHAT: AX + B=0");
                Writeln("-------------------------------------------------------");
                Write ("Nhap a= "); readln(a);
                Write ("Nhap b= ");readln(b);
                If(a=0) then
                 If(b=0) then Writeln(" Phuong trinh co vo so nghiem");
                 Else writeln("Phuong tring vo nghiem");
                Else Writeln("Phuong trinh co nghiem x=",-b/a);
                Readln();
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,397))
   
    def test_aProgram29(self):
        input = """
                Procedure DrawLine(X : Integer; Y : Integer);
                { the declaration of the variables in brackets are called parameters }
                Var Counter : Integer; { this is called a local variable }
                Begin
                 GotoXy(X,Y); {here I use the arguments of X and Y}
                 textcolor(green);
                 For Counter := 1 to 10 do
                 Begin
                  Write(chr(196));
                 End
                End
                procedure main();
                Begin
                 DrawLine(10,5);
                 DrawLine(10,6);
                 DrawLine(10,7);
                 DrawLine(10,10);
                 Readkey();
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,398))
    def test_aProgram30(self):
        input="""
              (
              var i: integer;
              )()
              """
        expect = str()ne 2 col 14: ("
        self.assertTrue(TestAST.test(input,expect,399))
    def test_aProgram31(self):
        input= """
             function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                   var x:real ;
                   BEGIN
                    while (a=3 or a+b = 6) do 
                    begin
                         
                    end
                   END
               """
        expect = str()ne 5 col 38: ="
        self.assertTrue(TestAST.test(input,expect,300))
    def test_aProgram32(self):
        input = """
                Var a,b,c,s,p: real;
                pROCEDURE main() ;
                Begin
                Clrscr();
                Writeln("BAI TOAN TAM GIAC:");
                Writeln("---------------------------------");
                Write("nhap a =");readln(a);
                Write("nhap b =");readln(b);
                Write("nhap c =");readln(c);
                If ((a+b)>c)and((b+c)>a)and((a+c)>b) then
                 Begin
                  p:=(a+b+c)/2;
                  s:=sqrt(p*(p-a)*(p-b)*(p-c));
                  Writeln("Chu vi tam giac:",3*p);
                  Writeln("Dien tich tam giac:",s);
                 End
                Else Writeln(a,", ", b,", ", c, " khong phai la ba canh cua tam giac");
                Readln();
                End
                """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,301))
    