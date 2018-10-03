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
        return ArrayType(self.visit(ctx.index_arr[0]),
                         self.visit(ctx.index_arr[1]),
                         self.visit(ctx.primitive_type()))
    def visitIndex_arr(self,ctx:MPParser.Index_arrContext):
        if (ctx.getChildCount()==1) : 
            return int(ctx.INTLIT().getText())
        else: 
            return -int(ctx.INTLIT().getText())

 #--------------------------------funcdecl---------------------------------

    def visitFuncdecl(self,ctx:MPParser.FuncdeclContex):
        return FuncDecl(Id(ctx.ID().getText()),
                        flatten([self.visit(x) for x in ctx.var_decl()]) if (ctx.var_decl()) else [] ,
                        self.visit(ctx.vardecl()) if (ctx.vardecl()) else [],
                        self.visit(ctx.compound_statement()),
                        seff.visit(ctx.return_type())
                        )
    def visitCompound_statement(self,ctx:MPParser.Compound_statementContex):
        return flatten([self.visit(x) for x in ctx.statement()]) if (ctx.statement()) else []
    
    # def visitStatement(self,ctx:MPParser.StatementContext):
    #     return self.visit(ctx.getChild(0))
    
    # def visitAssignment_statement(self,ctx:MPParser.Assignment_statementContext):    
    #     l=[x for x in ctx.lhs()] + [ctx.expression()]
    #     l1=l[::-1]
    #     l2=[] 
    #     return   [Assign(self.visit(l1[y]),self.visit(l1[y+1])) for y in range(0,len(l1)-1)]
    # def visitLhs(self,ctx:MPParser.LhsContext):
    #     if (ctx.ID()): 
    #         return Id(ctx.ID().getText())
    #     else:
    #         return self.visit(ctx.index_exp())

    def visitIf_statement(self,ctx:MPParser.If_statementContex):
        return If(  self.visit(ctx.expression()),
                    self.visit(ctx.statement(0)),
                    self.visit(ctx.statement(1)) if (ctx.statement(1)) else [] 
                )
    def visitWhile_statement(self,ctx:MPParser.While_statementContex):
        return While(
            self.visit(ctx.expression()),
            self.visit(ctx.statement())
        )

    def visitFor_statement(self,ctx:MPParser.For_statementContex):
        return For(
            Id(ctx.ID().getText()),
            self.visit(ctx.expression(0)),
            self.visit(ctx.expression(1)),
            True if (ctx.TO()) else False,
            self.visit(ctx.statement())
        )

    def visitBreak_statement(self,ctx:MPParser.Break_statementContex):
        return Break()

    def visitContinue_statement(self,ctx:MPParser.Continue_statementContex):
        return Continue()

    def visitReturn_statement(self,ctx:MPParser.Return_statementContex):
        return Return(self.visit(ctx.expression())) if(ctx.expression()) else [] 

    def visitWith_statement(self,ctx:MPParser.With_statementContex):
        return With(
            flatten([ self.visit(x) for x in ctx.var_decl()]),
            self.visit(ctx.statement())
        )
    def visitCall_statement(self,ctx:MPParser.Call_statementContex):
        return CallStmt(
            Id(ctx.ID().getText()),
            self.visit(ctx.list_exp()) if (ctx.list_exp()) else []
        )
    

        # def visitFuncdecl(self,ctx:MPParser.FuncdeclContext):
    #     local,cpstmt = self.visit(ctx.body()) 
    #     return FuncDecl(Id(ctx.ID().getText()),
    #                     [],
    #                     local,
    #                     cpstmt,
    #                     self.visit(ctx.mtype()))

    # def visitProcdecl(self,ctx:MPParser.ProcdeclContext):
    #     local,cpstmt = self.visit(ctx.body()) 
    #     return FuncDecl(Id(ctx.ID().getText()),
    #                     [],
    #                     local,
    #                     cpstmt)

    # def visitBody(self,ctx:MPParser.BodyContext):
    #     return [],[self.visit(ctx.stmt())] if ctx.stmt() else []
  
    # def visitStmt(self,ctx:MPParser.StmtContext):
    #     return self.visit(ctx.funcall())

    # def visitFuncall(self,ctx:MPParser.FuncallContext):
    #     return CallStmt(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    # def visitExp(self,ctx:MPParser.ExpContext):
    #     return IntLiteral(int(ctx.INTLIT().getText()))

    # def visitMtype(self,ctx:MPParser.MtypeContext):
    #     return IntType()
        

