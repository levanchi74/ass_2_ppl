from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

def flatten(lst):  
    flat=[]
    for i in lst:
        if isinstance(i,list):
            for j in i:
                flat.append(j)   
        else:flat.append(i)
    return flat

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(flatten([self.visit(x) for x in ctx.decl()]))

    def visitDecl(self,ctx:MPParser.DeclContext):
        if (ctx.vardecl()):
            return self.visit(ctx.vardecl())
        elif (ctx.funcdecl()):
            return self.visit(ctx.funcdecl())
        else:
            return self.visit(ctx.procedecl())

#---------------------------------vardecl-------------------------------

    def visitVardecl(self,ctx:MPParser.VardeclContext):
        return flatten([self.visit(x) for x in ctx.var_decl()])

    def visitVar_decl(self,ctx:MPParser.Var_declContext):
        return flatten([VarDecl(Id(x.getText()),self.visit(ctx.return_type())) for x in ctx.ID()])

    def visitReturn_type(self,ctx:MPParser.Return_typeContext):
        if(ctx.primitive_type()):
            return self.visit(ctx.primitive_type())
        else: 
            return self.visit(ctx.compound_type())
    def visitPrimitive_type(self,ctx:MPParser.Primitive_typeContext):
        if (ctx.BOOLEANTYPE()):
            return BoolType()
        elif(ctx.INTTYPE()):
            return IntType()
        elif(ctx.REALTYPE()):
            return FloatType()
        else: 
            return StringType()
    def visitCompound_type(self,ctx:MPParser.Compound_typeContext):
        return ArrayType(self.visit(ctx.index_arr(0)),
                         self.visit(ctx.index_arr(1)),
                         self.visit(ctx.primitive_type()))
    def visitIndex_arr(self,ctx:MPParser.Index_arrContext):
        if (ctx.getChildCount()==1) : 
            return int(ctx.INTLIT().getText())
        else: 
            return -int(ctx.INTLIT().getText())

 #--------------------------------funcdecl---------------------------------

    #name: Id
    #param: list(VarDecl)
    #local:list(VarDecl)
    #body: list(Stmt)
    #returnType: Type => VoidType for Procedure
    def visitFuncdecl(self,ctx:MPParser.FuncdeclContext):
        return FuncDecl(
                        Id(ctx.ID().getText()),
                        flatten([self.visit(x) for x in ctx.var_decl()]) if (ctx.var_decl()) else [] ,
                        self.visit(ctx.vardecl()) if (ctx.vardecl()) else [],
                        self.visit(ctx.compound_statement()),
                        self.visit(ctx.return_type())
                        )
    def visitCompound_statement(self,ctx:MPParser.Compound_statementContext):
        return flatten([self.visit(x) for x in ctx.statement()]) if (ctx.statement()) else []
    
    def visitStatement(self,ctx:MPParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitAssignment_statement(self,ctx:MPParser.Assignment_statementContext):    
        l=[self.visit(x) for x in ctx.lhs()] + [self.visit(ctx.expression())]
        l1=l[::-1]
        l2=[]
        for y in range(0,len(l1)-1):
          l2.append(Assign(l1[y+1],l1[y])) 
        return flatten(l2)       
        
         
    def visitLhs(self,ctx:MPParser.LhsContext):
        if (ctx.ID()): 
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.index_exp())

    #expr:Expr
    #thenStmt:list(Stmt)
    #elseStmt:list(Stmt)
    def visitIf_statement(self,ctx:MPParser.If_statementContext):
        return If(  self.visit(ctx.expression()),
                    flatten([self.visit(ctx.statement(0))]),
                    flatten([self.visit(ctx.statement(1))]) if (ctx.statement(1)) else [] 
                )

    #exp: Expr
    #sl:list(Stmt)
    def visitWhile_statement(self,ctx:MPParser.While_statementContext):
        return While(
            self.visit(ctx.expression()),
            flatten([self.visit(ctx.statement())]) 
        )

    #id:Id
    #expr1,expr2:Expr
    #up:Boolean #True => increase; False => decrease
    #loop:list(Stmt)
    def visitFor_statement(self,ctx:MPParser.For_statementContext):
        return For(
            Id(ctx.ID().getText()),
            self.visit(ctx.expression(0)),
            self.visit(ctx.expression(1)),
            True if (ctx.TO()) else False,
            flatten([self.visit(ctx.statement())]) 
        )

    def visitBreak_statement(self,ctx:MPParser.Break_statementContext):
        return Break()

    def visitContinue_statement(self,ctx:MPParser.Continue_statementContext):
        return Continue()

    #expr:Expr
    def visitReturn_statement(self,ctx:MPParser.Return_statementContext):
        return Return(self.visit(ctx.expression())) if(ctx.expression()) else Return(None)
        
    #decl:list(VarDecl)
    #stmt:list(Stmt)
    def visitWith_statement(self,ctx:MPParser.With_statementContext):
        return With(
            flatten([ self.visit(x) for x in ctx.var_decl()]),
            flatten([self.visit(ctx.statement())]) 
        )

    #method:Id
    #param:list(Expr)
    def visitCall_statement(self,ctx:MPParser.Call_statementContext):
        return CallStmt(
            Id(ctx.ID().getText()),
            [self.visit(x) for x in ctx.expression()] if (ctx.expression()) else []
        )
    
#-------------------------------------procedecl---------------------------------------

    def visitProcedecl(self,ctx:MPParser.ProcedeclContext):
        return FuncDecl(
            Id(ctx.ID().getText()),
            flatten([self.visit(x) for x in ctx.var_decl()]) if (ctx.var_decl()) else [],
            self.visit(ctx.vardecl()),
            self.visit(ctx.compound_statement()),
            VoidType()
        )

#-------------------------------------expression--------------------------------------
    #Binary
    #op:string: AND THEN => andthen; OR ELSE => orelse; other => keep it
    #left:Expr
    #right:Expr
    #expression: expression (AND THEN|OR ELSE) exp1 | exp1
    def visitExpression(self,ctx:MPParser.ExpressionContext):
        if(ctx.getChildCount()==1):
            return self.visit(ctx.exp1())
        else :
            return BinaryOp(
                "andthen" if (ctx.AND() and ctx.THEN()) else "orelse",
                self.visit(ctx.expression()),
                self.visit(ctx.exp1())
            )
    #exp1: exp2 (EQUAL | NOTEQUAL | LESS | LESSOREQUAL | GREATER | GREATEROREQUAL) exp2 | exp2
    def visitExp1(self,ctx:MPParser.Exp1Context):
        if(ctx.getChildCount()==1):
            return self.visit(ctx.exp2(0))
        else :
            return BinaryOp(
                ctx.getChild(1).getText(),
                self.visit(ctx.exp2(0)),
                self.visit(ctx.exp2(1))
            )
    #exp2: exp2 (ADD | SUB | OR) exp3 | exp3
    def visitExp2(self,ctx:MPParser.Exp2Context):
        if(ctx.getChildCount()==1):
            return self.visit(ctx.exp3())
        else :
            return BinaryOp(
                ctx.getChild(1).getText(),
                self.visit(ctx.exp2()),
                self.visit(ctx.exp3())
            )

    #exp3: exp3 (DIVISION | MUL | DIV | MOD | AND) exp4 | exp4
    def visitExp3(self,ctx:MPParser.Exp3Context):
        if(ctx.getChildCount()==1):
            return self.visit(ctx.exp4())
        else :
            return BinaryOp(
                ctx.getChild(1).getText(),
                self.visit(ctx.exp3()),
                self.visit(ctx.exp4())
            )
    #Unary
    #op:string
    #body:Expr
    #exp4: (SUB | NOT) exp4 | exp5
    def visitExp4(self,ctx:MPParser.Exp4Context):
        if(ctx.getChildCount()==1):
            return self.visit(ctx.exp5())
        else :
            return UnaryOp(
                ctx.getChild(0).getText(),
                self.visit(ctx.exp4())
            )

    #exp5: LB expression RB | index_exp | funcall | literal | ID ;
    def visitExp5(self,ctx:MPParser.Exp5Context):
        if (ctx.getChildCount()==3):
            return self.visit(ctx.expression())
        elif (ctx.index_exp()):
            return self.visit(ctx.index_exp())
        elif (ctx.funcall()):
            return self.visit(ctx.funcall())
        elif (ctx.literal()):
            return self.visit(ctx.literal())
        else:
            return Id(ctx.ID().getText())

    def visitFuncall(self,ctx:MPParser.FuncallContext):
        return CallExpr(
            Id(ctx.ID().getText()),
            [self.visit(x) for x in ctx.expression()] if (ctx.getChildCount()!=3) else []
        )

    def visitLiteral(self,ctx:MPParser.LiteralContext):
        if (ctx.INTLIT()): 
            return IntLiteral(int(ctx.INTLIT().getText()))
        if (ctx.FLOATLIT()):
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if (ctx.STRINGLIT()):
            return StringLiteral(ctx.STRINGLIT().getText())
        if (ctx.BOOLEANLIT()):
            return BooleanLiteral(bool(ctx.BOOLEANLIT().getText()))

    def visitIndex_exp(self,ctx:MPParser.Index_expContext):
        if (ctx.ID()): 
            return ArrayCell(Id(ctx.ID().getText()),self.visit(ctx.expression()))
        if (ctx.funcall()): 
            return ArrayCell(self.visit(ctx.funcall()),self.visit(ctx.expression()))
        if (ctx.INTLIT()): 
            return ArrayCell(IntLiteral(int(ctx.INTLIT().getText())),self.visit(ctx.expression()))
    
    