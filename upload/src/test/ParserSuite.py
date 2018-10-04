import unittest
from TestUtils import TestParser
class ParserSuite(unittest.TestCase):
    def test_variable_decla_list(self):
        """test variable declar many"""
        input="""var a,b ,c : integer ; e,f : real ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_variable_decla_error(self):
        """test variable declar many"""
        input="""d,b : array [    1 .. 5    ] of integer ;"""
        expect = "Error on line 1 col 0: d"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_variable_decla_array(self):
        """test variable declar many"""
        input="""var d , b : array [    1 .. 5    ] of integer ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_variable_decla_error_1(self):
        """test variable declar many"""
        input="""d , b : array [    1 .. 5    ] of integer ;"""
        expect = "Error on line 1 col 0: d"
        self.assertTrue(TestParser.test(input,expect,204))
    #test function declar
    def test_function_decla(self):
        """test function declar """
        input="""function foo (a , b : integer ; c : real ) : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
                foo(1);
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_function_decla_error_(self):
        """test function declar para """
        input="""function foo (a , b : integer  ;) : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 32: )"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_function_empty_para(self):
        """test function declar """
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_wrong_miss_close(self):
        """test function declar """
        input="""function foo ( : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 15: :"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_var_declaration1(self):
        """Simple var declaration"""
        input = """var a,b:integer;
                       x,y:real;
                       z:string;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))   
    def test_miss_var_declaration1(self):
        """Miss ) int main( {}"""
        input = """a:integer;"""
        expect = "Error on line 1 col 0: a"
        self.assertTrue(TestParser.test(input,expect,210))

    def test_var_declaration_array1(self):
        """More complex program"""
        input = """var d : array [1 .. 5] of integer ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_var_declaration_array2(self):
        """More complex program"""
        input = """var d,c : array [1 .. 5] of integer ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_func_declaration(self):
        """More complex program"""
        input = """function foo(i:integer):real;
                   var s:real;
                    begin
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213)) 
    def test_for_veryfirst(self):
        """simple program"""
        input = """var i : integer ;
            function f( ) : integer ;
            begin

            end
            procedure main () ;begin end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_miss_colon(self):
        """test wrong miss colon """
        input="""function foo ()  array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 17: array"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_wrong_miss_body(self):
        """test wrong miss body """
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real ;  """
           
        expect = "Error on line 2 col 32: <EOF>"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_miss_return(self):
        """ test wrong miss return """
        input="""function foo ();
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 15: ;"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_miss_semi(self):
        """test wrong miss semi """
        input="""function foo () : array [ 1 .. 2 ] of integer 
            var x , y : real ;
            begin
            
            end"""
        expect = "Error on line 2 col 12: var"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_for_nomain(self):
        """simple program no main"""
        input = """var i : integer ;
            function f( ) : integer ;
            begin

            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_for_function_not_end(self):
        """no end function"""
        input = """var i : integer ;
            function f( ) : integer ;
            begin

            """
        expect = "Error on line 5 col 12: <EOF>"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_for_function(self):
        """just function"""
        input = """
            function f( ) : integer ;
            begin
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_for_function_not_compoundstmt(self):
        """no end function no compound statement"""
        input = """
            function f( ) : integer ;

            """
        expect = "Error on line 4 col 12: <EOF>"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_for_function_not_returntype(self):
        """function no return type"""
        input = """
            function f( ) ;
            begin
            end
            """
        expect = "Error on line 2 col 26: ;"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_for_function_no_semi(self):
        """function no semi"""
        input = """
            function f( ) : string
            begin
            end
            """
        expect = "Error on line 3 col 12: begin"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_for_function_array1(self):
        """function return array type"""
        input = """
            function f( ) : array
            begin
            end
            """
        expect = "Error on line 3 col 12: begin"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_for_function_array2(self):
        """function return array type"""
        input = """
            function f( ) : array [1 .. 5] of integer;
            begin
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_for_function_array3(self):
        """function return array type"""
        input = """
            function f( ) : array [1 .. 5] of integer;
            begin
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_for_function_array4(self):
        """function return array type"""
        input = """
            function f( ) : array [1 .. 5] of integer;
            begin
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_for_procedure(self):
        """function procedure"""
        input = """
            procedure f( );
            begin
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_for_procedure_with_returntype(self):
        """function procedure with return type"""
        input = """
            procedure f( ) : boolean;
            begin
            end
            """
        expect = "Error on line 2 col 27: :"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_for_procedure2(self):
        """function procedure"""
        input = """
            procedure f(a,b:integer;c:real);
            begin
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_for_procedure3(self):
        """function procedure"""
        input = """
            procedure f(a,b,,c:integer;c:real);
            begin
            end
            """
        expect = "Error on line 2 col 28: ,"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_for_procedure4(self):
        """function procedure"""
        input = """
            procedure f(a,b,c:integer;c:array);
            begin
            end
            """
        expect = "Error on line 2 col 45: )"
        self.assertTrue(TestParser.test(input,expect,233))

    def test_for_procedure5(self):
        """function procedure"""
        input = """
            procedure f(a,b,c:integer;c:real);
            var x , y :real;
            begin
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_for_procedure6(self):
        """function procedure"""
        input = """
            procedure f(a,b,c:integer;c:real);

            """
        expect = "Error on line 4 col 12: <EOF>"
        self.assertTrue(TestParser.test(input,expect,235))

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
        expect = "Error on line 3 col 12: procedure"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_for_vardecl1(self):
        """var declaration"""
        input = """
            var a , b , c : integer ;
                d : array [ 1 .. 5 ] of integer ;
                e , f : real ;
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))   
    def test_assignment_stmt(self):
        """test_assignment_stmt"""
        input= """procedure abc ();
            var x , y : real ; 
            begin
                a:=12;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,238))
    def test_assignment_stmt_many(self):
        """test_assignment_stmt_many"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                a:=b:=c:=d:=12;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,239))
    def test_if_statement1(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    else foo();
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_if_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    else if (1<2)<>(2<3) then x:=1 ;
                    else foo(a+1,2);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_if_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    if (1<2) then beGin x:=1 ; end
                    else foo(a+1,2);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_if_statement4(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if a>1 then beGin
                        a:=1 ;
                        if 1=1 then a:=b;
                        
                    end
                    END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_while_statement1(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_while_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin
                        if(a=1) then x:=1;
                        foo();
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_while_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin
                        while(1) do x:=1;
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_break_state(self):
        """test_break_state"""
        input= """procedure break_state ();
        var x , y : real ; 
            begin
                while  a =4 do  break;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,247))
    def test_break_state_miss_semi(self):
        """test_break_state_miss_semi"""
        input= """procedure break_state ();
        var x , y : real ; 
            begin
                while  a =4 do  break;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,248))
    def test_continue_state_withfor(self):
        """test_continue_state_withfor"""
        input= """procedure continue_state();
        var x , y : real ; 
            begin
                for  a :=4 to 23 do  continue;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,249))
    def test_continue_state_withwhile(self):
        """test_continue_state_withwhile"""
        input= """procedure continue_state();
        var x , y : real ; 
            begin
                while  a =4 do  continue;;
            end"""
        expect='Error on line 4 col 41: ;'
        self.assertTrue(TestParser.test(input,expect,250))
    def test_continue_state_wrong_stmt(self):
        """test_continue_state_wrong_stmt"""
        input= """procedure continue_state();
        var x , y : real ; 
            begin
                while  a =4 do  coninue+fg**3;;
            end"""
        expect='Error on line 4 col 39: +'
        self.assertTrue(TestParser.test(input,expect,251))
    def test_with_statement1(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do
                    d := c [a] + b ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_with_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    d := c [a] + b ;
                    foo();foo1(a,b,c);
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_return_state_non_expr(self):
        """test_return_state_non_expr"""
        input= """procedure return_state();
        var x , y : real ; 
            begin
                return ;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,255))
    def test_return_state_miss_semi(self):
        """test_return_state_non_expr"""
        input= """procedure return_state();
        var x , y : real ; 
            begin
                return 
            end"""
        expect='Error on line 5 col 12: end'
        self.assertTrue(TestParser.test(input,expect,256))
    def test_call_state_simple(self):
        """test_call_state_simple"""
        input= """procedure call_state();
        var x , y : real ; 
            begin
                foo () ;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,257))
    def test_call_state_many_para(self):
        """test_call_state_many_para"""
        input= """procedure call_state();
        var x , y : real ; 
            begin
                foo (23+45, hello) ;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,258))
    def test_call_statement2(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,a<>1,a[1]);
                    return 1;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_call_statement3(self):
        input = """function _ADBfoo(a,b,c: real; a:array[1 .. -4] of string): array[1 .. 5] of boolean;
                   BEGIN
                    
                    foo(3,a+1,a[1],foo(1,2)[m+1],x and then y);
                    return foo2();
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_compound_state(self):
        """test_compound_state"""
        input= """procedure compound_state();
           var x , y : real ; 
            begin
                
            end"""
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,261))
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
        self.assertTrue(TestParser.test(input,expect,262))
    def test_case_insensitive(self):
        """test_case_insensitive"""
        input="""FuNctIon foo     (): array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_wrong_type_return(self):
        """test_wrong_type_return"""
        input="""function _ADVCDfoo     (): array [ 1 .. 2 ] of array [ 1 .. 2 ] ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 47: array"
        self.assertTrue(TestParser.test(input,expect,264))
    def test_case_insensitive2(self):
        """test_case_insensitive"""
        input="""prOceDure _ADVCDfoo ();
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_wrong_redundancy_colon(self):
        """test_wrong_redundancy_colon"""
        input="""procedure abc (): array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 16: :"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_wrong_miss_semi_produre(self):
        """test_wrong_redundancy_colon"""
        input="""procedure abc ()
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 2 col 12: var"
        self.assertTrue(TestParser.test(input,expect,267))
    def test_assign_stmt_with_expr(self):
        """test_assign_stmt_with_expr"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                a:=b:=c:=d:=(12+3);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,268))
    def test_assign_stmt_with_funcall(self):
        """test_assign_stmt_with_expr"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                a:=b:=c:=d:=foo();
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,269))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
    
    def test_aProgram3(self):
        input = """
                proceDure Hello(a, b:integer);
                begin
                    a := b + c;
                    writeln("Hello, world!");
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_aProgram8(self):
        input = """
                procedure main() ;
                beGin
                 a[b[2]] := 10;
                 foo();
                 return ;
                eND
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_aProgram10(self):
        input = """
                procedure main() ;
                beGin
                 if a=b then if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                eND
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
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
        expect = "Error on line 2 col 46: Mang20"
        self.assertTrue(TestParser.test(input,expect,288))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
   
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_aProgram30(self):
        input="""
              (
              var i: integer;
              )()
              """
        expect = "Error on line 2 col 14: ("
        self.assertTrue(TestParser.test(input,expect,299))
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
        expect = "Error on line 5 col 38: ="
        self.assertTrue(TestParser.test(input,expect,300))
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
                  Writeln("Chu vi tam giac:",2*p);
                  Writeln("Dien tich tam giac:",s);
                 End
                Else Writeln(a,", ", b,", ", c, " khong phai la ba canh cua tam giac");
                Readln();
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,301))
    