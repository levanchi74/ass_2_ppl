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
    # def visitProgram(self,ctx:MPParser.ProgramContext):
    #    return Program(flatten(list(map(lambda x:self.visit(x),ctx.decl()))))
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(flatten([self.visit(x) for x in ctx.decl()]))

    def visitDecl(self,ctx:MPParser.DeclContext):
        if (ctx.vardel()):
            return self.visit(ctx.vardel())
        elif (ctx.funcdel()):
            return self.visit(ctx.funcdel())
        else: 
            return self.visit(ctx.procedel())

    def visitVardel(self,ctx:MPParser.VardelContext):
        return flatten([self.visit(x) for x in ctx.var_decla()])

    def visitVar_decla(self,ctx:MPParser.Var_declaContext):
        return flatten([VarDecl(Id(x.getText()),self.visit(ctx.return_type())) for x in ctx.ID()])
        
    def visitReturn_type(self,ctx:MPParser.Return_typeContext):
        if (ctx.primitive_type()):
            return (self.visit(ctx.primitive_type()))
        else: 
            return (self.visit(ctx.array_type()))

    def visitPrimitive_type(self,ctx:MPParser.Primitive_typeContext):
        if (ctx.BOOLEANTYPE()):
            return BoolType()
        if (ctx.INTTYPE()):
            return IntType()
        if (ctx.REALTYPE()):
            return FloatType()
        if (ctx.STRINGTYPE()): 
            return StringType()

    def visitArray_type(self,ctx:MPParser.Array_typeContext):
        return ArrayType(self.visit(ctx.subscript(0)),
                         self.visit(ctx.subscript(1)),
                         self.visit(ctx.primitive_type())
                         )

    def visitSubscript(self,ctx:MPParser.SubscriptContext):
        if (ctx.getChildCount()==1) : 
            return int(ctx.INTLIT().getText())
        else: 
            return -int(ctx.INTLIT().getText())

    def visitFuncdel(self,ctx:MPParser.FuncdelContext):
        return FuncDecl(Id(ctx.ID().getText()),
                        flatten([self.visit(x) for x in ctx.var_decla()]) if (ctx.var_decla()) else [],    
                        self.visit(ctx.vardel()) if (ctx.vardel()) else [],
                        self.visit(ctx.compound_statement()),
                        self.visit(ctx.return_type())
            )
    def visitCompound_statement(self,ctx:MPParser.Compound_statementContext):
        return flatten([self.visit(x) for x in ctx.statement()]) if (ctx.getChildCount()!=2) else []
        
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
    def visitIf_statement(self,ctx:MPParser.If_statementContext):
        return If(self.visit(ctx.expression()),
                  flatten([self.visit(ctx.statement(0))]),
                  flatten([self.visit(ctx.statement(1))]) if ctx.statement(1) else []
            )
    def visitFor_statement(self,ctx:MPParser.For_statementContext):
        return For(Id(ctx.ID().getText()),
                   self.visit(ctx.expression(0)),
                   self.visit(ctx.expression(1)),
                   True if (ctx.TO()) else False,
                   flatten([self.visit(ctx.statement())])                               
            )

    def visitWhile_statement(self,ctx:MPParser.While_statementContext):
        return While(self.visit(ctx.expression()),
                     flatten([self.visit(ctx.statement())])
            )

    def visitBreak_statement(self,ctx:MPParser.Break_statementContext):
        return Break()

    def visitContinue_statement(self,ctx:MPParser.Continue_statementContext):
        return Continue()

    def visitReturn_statement(self,ctx:MPParser.Return_statementContext):
        return Return(self.visit(ctx.expression())) if ctx.expression() else Return(None)

    def visitCall_statement(self,ctx:MPParser.Call_statementContext):
        return CallStmt(Id(ctx.ID().getText()),            
                        [self.visit(x) for x in ctx.expression()] if (ctx.expression()) else []  
                        
            )
    def visitWith_statement(self,ctx:MPParser.With_statementContext):
        return With(flatten([self.visit(x) for x in ctx.var_decla()]),
                    flatten([self.visit(ctx.statement())])
            )

    def visitProcedel(self,ctx:MPParser.ProcedelContext):
        return FuncDecl(Id(ctx.ID().getText()),     
                        flatten([self.visit(x) for x in ctx.var_decla()])  if (ctx.var_decla()) else []
                        ,self.visit(ctx.vardel()) if (ctx.vardel()) else []
                        ,self.visit(ctx.compound_statement())
                        ,VoidType()
            )

    def visitExpression(self,ctx:MPParser.ExpressionContext):
        if (ctx.getChildCount()==1):
            return self.visit(ctx.getChild(0))
        else: 
            return BinaryOp("andthen" if ((ctx.AND()) and (ctx.THEN())) else "orelse",
                            self.visit(ctx.expression()),
                            self.visit(ctx.expr1())
          )

    def visitExpr1(self,ctx:MPParser.Expr1Context):
        if (ctx.getChildCount()==1):
            return self.visit(ctx.getChild(0))
        else: 
            return BinaryOp(ctx.getChild(1).getText(),
                            self.visit(ctx.expr2(0)),
                            self.visit(ctx.expr2(1))
            )

    def visitExpr2(self,ctx:MPParser.Expr2Context):
        if (ctx.getChildCount()==1):
            return self.visit(ctx.getChild(0))
        else: 
            return BinaryOp(ctx.getChild(1).getText(),
                            self.visit(ctx.expr2()),
                            self.visit(ctx.expr3())
            )

    def visitExpr3(self,ctx:MPParser.Expr3Context):
        if (ctx.getChildCount()==1):
            return self.visit(ctx.getChild(0))
        else: 
            return BinaryOp(ctx.getChild(1).getText(),
                            self.visit(ctx.expr3()),
                            self.visit(ctx.expr4()),
            )

    def visitExpr4(self,ctx:MPParser.Expr4Context):
        if (ctx.getChildCount()==1):
            return self.visit(ctx.getChild(0))
        else: 
            return UnaryOp(ctx.getChild(0).getText(),
                           self.visit(ctx.expr4())
            )

    def visitExpr5(self,ctx:MPParser.Expr5Context):
        if (ctx.getChildCount()==3):
            return  self.visit(ctx.expression())
        if (ctx.index_exp()): 
            return self.visit(ctx.index_exp())
        if (ctx.funcall()):
            return self.visit(ctx.funcall())
        if (ctx.literal()):
            return self.visit(ctx.literal())
        if (ctx.ID()):
            return Id(ctx.ID().getText())

    def visitFuncall(self,ctx:MPParser.FuncallContext):           
        return CallExpr(Id(ctx.ID().getText()),             
                        flatten([self.visit(x) for x in ctx.expression()])  if (ctx.getChildCount()!=3) else []                      
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
    

