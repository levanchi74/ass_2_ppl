grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program :decl+ EOF ;

decl: vardecl 
    | funcdecl 
    | procedecl
    ;

//-------------------------------------variable declaration--------------------------------

vardecl : VAR (var_decl SEMI)+;
var_decl: ID (COMMA ID)* COLON return_type;
return_type: primitive_type | compound_type ;
primitive_type: BOOLEANTYPE | INTTYPE | REALTYPE | STRINGTYPE;
compound_type: ARRAY LSB (index_arr) DD (index_arr) RSB OF primitive_type;
index_arr : SUB? INTLIT;

//------------------------------------function declaration----------------------------------

funcdecl:FUNCTION ID LB (var_decl(SEMI var_decl)*)? RB COLON return_type SEMI vardecl? compound_statement;
param_list: (var_decl (SEMI var_decl)*);
compound_statement:BEGIN (statement)* END;

//-------------------------------------statement--------------------------------------------
statement : assignment_statement
          | if_statement
          | for_statement
          | while_statement
          | break_statement
          | continue_statement
          | return_statement
          | call_statement
          | compound_statement
          | with_statement
            ;
assignment_statement: lhs+ expression SEMI;

lhs: (ID | index_exp) ASSIGN

if_statement: IF expression THEN statement (ELSE statement)?;

while_statement: WHILE expression DO statement;

for_statement: FOR ID ASSIGN expression (TO|DOWNTO) expression DO statement;

break_statement: BREAK SEMI;

continue_statement: CONTINUE SEMI;

return_statement: RETURN expression? SEMI;

with_statement: WITH (var_decl SEMI)+ DO statement ;

call_statement: ID LB (expression(COMMA expression)*)? RB SEMI;

//---------------------------------------Procedure declaration---------------------------------

procedecl: PROCEDURE ID LB param_list? RB SEMI vardecl? compound_statement ;

//---------------------------------------Expression--------------------------------------------
 
expression: expression (AND THEN|OR ELSE) exp1
          | exp1
          ;
exp1: exp2 (EQUAL | NOTEQUAL | LESS | LESSOREQUAL | GREATER | GREATEROREQUAL) exp2
      | exp2
      ;
exp2: exp2 (ADD | SUB | OR) exp3
    | exp3
    ;
exp3: exp3 (DIVISION | MUL | DIV | MOD | AND) exp4
    | exp4
    ;
 
exp4: (SUB | NOT) exp4
    | exp5
    ;
exp5: LB expression RB | index_exp | funcall | literal | ID ;

funcall :  ID LB list_exp? RB ;
literal: INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT;
index_exp: (ID|funcall|INTLIT) LSB expression RSB;

//------------------------Comments----------------------

TRADI_CMT: '(*' .*? '*)' ->  skip ;
BLOCK_CMT: '{' .*? '}' -> skip ;
LINE_CMT: '//'~[\n\r]* -> skip;

//---------------------------------Token Set--------------------------------

BOOLEANLIT: TRUE|FALSE;

BREAK:B R E A K ;
CONTINUE:C O N T I N U E;
FOR : F O R ;
TO: T O;
DOWNTO:D O W N T O;
DO: D O;
IF : I F;
THEN:T H E N;
ELSE : E L S E;
RETURN: R E T U R N;
WHILE: W H I L E;
WITH:W I T H;
BEGIN:B E G I N;
END:E N D;
FUNCTION:F U N C T I O N;
PROCEDURE:P R O C E D U R E;
VAR: V A R;
TRUE:T R U E;
FALSE:F A L S E; 
ARRAY:A R R A Y;
OF:O F; 
REALTYPE:R E A L;
BOOLEANTYPE:B O O L E A N;
INTTYPE: I N T E G E R;
STRINGTYPE: S T R I N G;
NOT:N O T;
AND:A N D;
OR:O R;
DIV:D I V;
MOD:M O D;

//----------------------------------Case-insensive-------------------------------

fragment A:('a'|'A');
fragment B:('b'|'B');
fragment C:('c'|'C');
fragment D:('d'|'D');
fragment E:('e'|'E');
fragment F:('f'|'F');
fragment G:('g'|'G');
fragment H:('h'|'H');
fragment I:('i'|'I');
fragment J:('j'|'J');
fragment K:('k'|'K');
fragment L:('l'|'L');
fragment M:('m'|'M');
fragment N:('n'|'N');
fragment O:('o'|'O');
fragment P:('p'|'P');
fragment Q:('q'|'Q');
fragment R:('r'|'R');
fragment S:('s'|'S');
fragment T:('t'|'T');
fragment U:('u'|'U');
fragment V:('v'|'V');
fragment W:('w'|'W');
fragment X:('x'|'X');
fragment Y:('y'|'Y');
fragment Z:('z'|'Z');

//------------------------------------Operator--------------------------------

ASSIGN :':=';
ADD:'+';
MUL:'*';
NOTEQUAL:'<>';
LESSOREQUAL:'<=';
GREATEROREQUAL:'>=';
SUB:'-';
DIVISION: '/';
EQUAL: '=';
LESS: '<';
GREATER: '>';

//------------------------------------Separators--------------------------------

LSB: '[';
RSB: ']';
COLON: ':';
LB: '(';
RB: ')';
SEMI: ';';
DD: '..';
COMMA: ',';

//------------------------------------Literals-----------------------------------

INTLIT: [0-9]+;

fragment CASE1: [0-9]+'.'[0-9]*;  
fragment CASE2: [0-9]*'.'[0-9]+; 
fragment CASE3: ([0-9]+[eE]'-'?[0-9]+) ;  	
fragment CASE4: [0-9]*'.'[0-9]+[eE]'-'?[0-9]+;  
FLOATLIT: (CASE1|CASE2|CASE3|CASE4);

WS: [ \t\r\n\f]+ -> skip ;
ID: [a-zA-Z_][0-9a-zA-Z_]*;


STRINGLIT: '"' (ESCAPE|~[\r\n"\\])* '"'
{ 
 temp=Lexer.text.fget(self)
 temp1=(temp[1:len(temp)-1])
 Lexer.text.fset(self,temp1)
}; 

//Unclose String
UNCLOSE_STRING: '"'(ESCAPE|~[\r\n"\\])*
{ 
  raise UncloseString(self.text[1:])
};

ERR: .*?'\\'('b'|'f'|'r'|'n'|'t'|'\''|'"'|'\\' ).*?
{
  raise ErrorToken('\\')
};

ESCAPE: '\\'
        (   'b'    {Lexer.text.fset(self,"\b")}
        |   'f'    {Lexer.text.fset(self,"\f")}
        |   'r'    {Lexer.text.fset(self,"\r")}
        |   'n'    {Lexer.text.fset(self,"\n")}
        |   't'    {Lexer.text.fset(self,"\t")}
        |   '\''   {Lexer.text.fset(self,"\'")}
        |   '"'    {Lexer.text.fset(self,"\"")}
        |   '\\'   {Lexer.text.fset(self,"\\")}
        );

fragment ILL: ('\\')~('b'|'f'|'r'|'n'|'"'|'\''|'\\'|'t');
ILLEGAL_ESCAPE: '"' .*?  ILL .*? '"' 
{    
 temp=Lexer.text.fget(self) 
 temp1=temp.find('\\')
 raise IllegalEscape(self.text[1:temp1+2])
};
ERROR_CHAR:.
{
 raise ErrorToken(self.text)
};



