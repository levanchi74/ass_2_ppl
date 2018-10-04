import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_comment1(self):
        """test commments"""
        input="""(*abc*)"""
        expect="""<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,101))
    def test_comment2(self):
        """test commments"""
        input="""(*abc1234A*)"""
        expect="""<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,102))
    def test_comment3(self):
        """test commments"""
        input="""(*abc1234A**//%*)"""
        expect="""<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,103))
    def test_comment4(self):
        """test commments"""
        input="""//abc1234A"""
        expect="""<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,104))
    def test_comment5(self):
        """test commments"""
        input="""{*abc1234A*}"""
        expect="""<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,105))
    def test_comment6(self):
        """test commments"""
        input="""{*//abc*}"""
        expect="""<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,106))
    def test_comment7(self):
        """test commments"""
        input="""{*//abc*}/bc"""
        expect="""/,bc,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,107))
    def test_comment8(self):
        """test commments"""
        input="""{*//abc*}abc"""
        expect="""abc,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,108))
    def test_comment9(self):
        """test commments"""
        input="""{*//abc(**}abc*)//*)abc"""
        expect="""abc,*,),<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,109))
    def test_identifier1(self):
        """test identifiers"""
        input="""ABbc"""
        expect="""ABbc,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,110))
    def test_identifier2(self):
        """test identifiers"""
        input="""12_abc34"""
        expect="""12,_abc34,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,111))
    def test_identifier3(self):
        """test identifiers"""
        input="""12abc"""
        expect="""12,abc,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,112))
    def test_identifier4(self):
        """test identifiers"""
        input="""12_abc"""
        expect="""12,_abc,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,113))
    def test_identifier5(self):
        """test identifiers"""
        input="""12_abc34"""
        expect="""12,_abc34,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,114))
    def test_identifierAndComment1(self):
        """test identifiers"""
        input="""12_abc34//abc"""
        expect="""12,_abc34,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,115))
    def test_identifierAndComment2(self):
        """test identifiers"""
        input="""12_abc34{*abc*}"""
        expect="""12,_abc34,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,116))
    def test_identifierAndComment3(self):
        """test identifiers"""
        input="""12_abc34(*abc*)"""
        expect="""12,_abc34,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,117))
    def test_Float1(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.2","1.2,<EOF>",118))
    def test_Float2(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.","1.,<EOF>",119))
    def test_Float3(self):
        """test float"""
        self.assertTrue(TestLexer.test(".1",".1,<EOF>",120))
    def test_Float4(self):
        """test float"""
        self.assertTrue(TestLexer.test("1e2","1e2,<EOF>",121))
    def test_Float5(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.2E-2","1.2E-2,<EOF>",122))
    def test_Float6(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.2e-2","1.2e-2,<EOF>",123))
    def test_Float7(self):
        """test float"""
        self.assertTrue(TestLexer.test(".1E2",".1E2,<EOF>",124))
    def test_Float8(self):
        """test float"""
        self.assertTrue(TestLexer.test("9.0","9.0,<EOF>",125))
    def test_Float9(self):
        """test float"""
        self.assertTrue(TestLexer.test("12e8","12e8,<EOF>",126))
    def test_Float10(self):
        """test float"""
        self.assertTrue(TestLexer.test("0.33E-3","0.33E-3,<EOF>",127))
    def test_Float11(self):
        """test float"""
        self.assertTrue(TestLexer.test("128e-42","128e-42,<EOF>",128))
    def test_FloatAndIndentifier(self):
        """test float"""
        self.assertTrue(TestLexer.test("_Abc128e-42e","_Abc128e,-,42,e,<EOF>",129))
    def test_Float12_Error(self):
        """test float"""
        self.assertTrue(TestLexer.test("e-12","e,-,12,<EOF>",130))
    def test_Float13_Error(self):
        """test float"""
        self.assertTrue(TestLexer.test("143e","143,e,<EOF>",131))
    def test_Float14(self):
        """test float"""
        input="""12.56E-12abc"""
        expect="12.56E-12,abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,132))
    def test_String1(self):
        """test string simple"""
        input=""" "string" """
        expect="""string,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,133))
    def test_String2(self):
        """test string simple"""
        input="""ab"abc"cd"""
        expect="""ab,abc,cd,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,134))
    def test_String3(self):
        """test string """
        input=""" "23a" "34b" """
        expect="23a,34b,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,135))
    def test_String4(self):
        """test string simple"""
        input=""" "" """
        expect=""",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,136))
    def test_String_UncloseString1(self):
        """test string """
        input=""" "abcd"""
        expect="""Unclosed String: abcd"""
        self.assertTrue(TestLexer.test(input,expect,137))  
    def test_String_UncloseString2(self):
        """test string """
        input= """ " """
        expect="""Unclosed String:  """
        self.assertTrue(TestLexer.test(input,expect,138))
    def test_String_illegalEscape1(self):
        """test string """
        input= """ "abc \m" """
        expect="""Illegal Escape In String: abc \\m"""
        self.assertTrue(TestLexer.test(input,expect,139))
    def test_ErrorToken1(self):
        """test Error Token"""
        input="""$"""
        expect="""Error Token $"""
        self.assertTrue(TestLexer.test(input,expect,140))
    def test_ErrorToken2(self):
        """test Error Token"""
        input="""~"""
        expect="""Error Token ~"""
        self.assertTrue(TestLexer.test(input,expect,141))
    def test_ErrorToken3(self):
        """test Error Token"""
        input="""@"""
        expect="""Error Token @"""
        self.assertTrue(TestLexer.test(input,expect,142))
    def test_ErrorToken4(self):
        """test Error Token"""
        input="""#"""
        expect= """Error Token #"""
        self.assertTrue(TestLexer.test(input,expect,143))
    def test_ErrorToken5(self):
        """test Error Token"""
        input="""."""
        expect="""Error Token ."""
        self.assertTrue(TestLexer.test(input,expect,144))
    
    def test_Keyword1(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("break", "break,<EOF>", 145))
    def test_Keyword2(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("BREAK", "BREAK,<EOF>", 146))   
    def test_Keyword3(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("Or     elSe", "Or,elSe,<EOF>", 147))  
    def test_Keyword5(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("or       else", "or,else,<EOF>", 148)) 
    def test_Keyword6(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("Or elSe", "Or,elSe,<EOF>", 149))  
    def test_Keyword7(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("OR ELSE", "OR,ELSE,<EOF>", 150))
    def test_Keyword8(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("or else", "or,else,<EOF>", 151))      
    def test_Keyword9(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("ANd    TheN", "ANd,TheN,<EOF>", 152))     
    def test_Keyword11(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("and      then", "and,then,<EOF>", 153))
    def test_Keyword12(self):
         self.assertTrue(TestLexer.test("ANd TheN", "ANd,TheN,<EOF>", 154))   
    def test_Keyword14(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("and then", "and,then,<EOF>", 155))    
    def test_Keyword15(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("REtUrn", "REtUrn,<EOF>", 156))      
    def test_Keyword17(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("return", "return,<EOF>", 157))   
    def test_Keyword18(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("continue", "continue,<EOF>", 158))     
    def test_Keyword20(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("CoNtInUe", "CoNtInUe,<EOF>", 159))
    def test_Keyword21(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("for", "for,<EOF>", 160))
    def test_Keyword22(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("FOR", "FOR,<EOF>", 161))
    def test_Keyword23(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("fOr", "fOr,<EOF>", 162))
    def test_Keyword24(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("to", "to,<EOF>", 163))
    def test_Keyword25(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("TO", "TO,<EOF>", 164))
    def test_Keyword26(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("To", "To,<EOF>", 165))
    def test_Keyword27(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("downto", "downto,<EOF>", 166))
    def test_Keyword28(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("DOWNTO", "DOWNTO,<EOF>", 167))
    def test_Keyword29(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("DowNTo", "DowNTo,<EOF>",168))
    def test_Keyword30(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("do", "do,<EOF>", 169))
    def test_Keyword31(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("DO", "DO,<EOF>", 170))
    def test_Keyword32(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("Do", "Do,<EOF>", 171))
    def test_Keyword33(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("if", "if,<EOF>", 172))
    def test_Keyword34(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("IF", "IF,<EOF>", 173))
    def test_Keyword35(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("If", "If,<EOF>", 174))
    def test_Keyword36(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("then", "then,<EOF>", 175))
    def test_Keyword37(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("THEN", "THEN,<EOF>", 176))
    def test_Keyword39(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("THen", "THen,<EOF>", 177))
    def test_Keyword40(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("else", "else,<EOF>", 178))
    def test_Keyword41(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("ELSE", "ELSE,<EOF>", 179))
    def test_Keyword42(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("return", "return,<EOF>", 180))
    def test_integer1(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",181))
    def test_integer2(self):
        """test integers"""
        self.assertTrue(TestLexer.test("000000","000000,<EOF>",182))
    def test_integer3(self):
        """test integers"""
        self.assertTrue(TestLexer.test("0123456","0123456,<EOF>",183))   
    def test_operator(self):
        self.assertTrue(TestLexer.test("+ - * / not mod or and <> = < > <= >= div","+,-,*,/,not,mod,or,and,<>,=,<,>,<=,>=,div,<EOF>",184))
    def test_sperators(self):
        self.assertTrue(TestLexer.test("[ ] : ( ) ; .. ,","[,],:,(,),;,..,,,<EOF>",185))
    def test_integet_type(self):
        self.assertTrue(TestLexer.test("var i:integer;","var,i,:,integer,;,<EOF>",186))
    def test_real_type(self):
        self.assertTrue(TestLexer.test("var a,b,c:real;","var,a,,,b,,,c,:,real,;,<EOF>",187))
    def test_string_type(self):
        self.assertTrue(TestLexer.test("var a:string;","var,a,:,string,;,<EOF>",188))
    def test_boolean_type(self):
        self.assertTrue(TestLexer.test("var b:boolean;","var,b,:,boolean,;,<EOF>",189))
    def test_array(self):
        self.assertTrue(TestLexer.test("var x:array[1 .. 6] of integer;","var,x,:,array,[,1,..,6,],of,integer,;,<EOF>",190))
    def test_variable1(self):
        self.assertTrue(TestLexer.test("Var a,b,c:Integer;","Var,a,,,b,,,c,:,Integer,;,<EOF>",191))  
    def test_variable3(self):
        self.assertTrue(TestLexer.test("Var d:array[1 .. 5] of real;","Var,d,:,array,[,1,..,5,],of,real,;,<EOF>",192)) 
    def test_Operators_1(self):
        self.assertTrue(TestLexer.test("notorand*div", "notorand,*,div,<EOF>", 193))
    def test_Operators_2(self):
        self.assertTrue(TestLexer.test("=>=", "=,>=,<EOF>", 194))
    def test_while(self):
        self.assertTrue(TestLexer.test(" while(a>9) do a:=a-1;", "while,(,a,>,9,),do,a,:=,a,-,1,;,<EOF>", 196))
    def test_for(self):
        self.assertTrue(TestLexer.test(" for a := 10 downto 5 do if(a<8) then return a;", "for,a,:=,10,downto,5,do,if,(,a,<,8,),then,return,a,;,<EOF>", 197))
    def test_continue(self):
        self.assertTrue(TestLexer.test("for a := 5 to 10 do if(a=7) Then a:=b[10]:=5 ; else continuE ;", "for,a,:=,5,to,10,do,if,(,a,=,7,),Then,a,:=,b,[,10,],:=,5,;,else,continuE,;,<EOF>", 198))
    def test_break(self):
        self.assertTrue(TestLexer.test("for a := 5 to 10 do if(a=7) Then return 1 ;else break ;", "for,a,:=,5,to,10,do,if,(,a,=,7,),Then,return,1,;,else,break,;,<EOF>", 199))
    def test_assignment(self):
        self.assertTrue(TestLexer.test(" a:=1:=c[10]=foo(3)[5]", "a,:=,1,:=,c,[,10,],=,foo,(,3,),[,5,],<EOF>",200))
    def test_funcall(self):
        self.assertTrue(TestLexer.test("foo(3,a+1,m(2));", "foo,(,3,,,a,+,1,,,m,(,2,),),;,<EOF>",201))