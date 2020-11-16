from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):

    def visitProgram(self, ctx: BKITParser.ProgramContext):
        return Program(self.visit(ctx.declarations()))

    def visitDeclarations(self, ctx: BKITParser.DeclarationsContext):
        arr = []
        if ctx.getChildCount() == 0:
            return []
        else:
            for i in range(ctx.getChildCount()):
                arr += self.visit(ctx.getChild(i))
            return arr

    def visitVar_decl(self, ctx: BKITParser.Var_declContext):
        return self.visit(ctx.many_var_decl())

    def visitMany_var_decl(self, ctx: BKITParser.Many_var_declContext):
        if ctx.many_var_decl():
            return self.visit(ctx.one_var_decl()) + self.visit(ctx.many_var_decl())
        else:
            return self.visit(ctx.one_var_decl())

    def visitOne_var_decl(self, ctx: BKITParser.One_var_declContext):
        if ctx.scalar():
            dimen = []
            id = self.visit(ctx.scalar())
            if ctx.ASSIGN():
                literal = self.visit(ctx.literal())
            else:
                literal = None
            return [VarDecl(id, dimen, literal)]
        else:
            dimen = self.visit(ctx.composit())
            id = Id(ctx.ID().getText())
            if ctx.ASSIGN():
                literal = self.visit(ctx.literal())
            else:
                literal = None
            return [VarDecl(id, dimen, literal)]

    def visitScalar(self, ctx: BKITParser.ScalarContext):
        return Id(ctx.ID().getText())

    def visitComposit(self, ctx: BKITParser.CompositContext):
        intlist = ctx.INT_LIT()
        lst = []
        #['1','0xFF','0o77','6']
        #['1','255','555','6']
        for j in intlist:
            i=j.getText()
            x = i.find('x')
            X = i.find('X')
            o = i.find('o')
            O = i.find('O')
            if(x != -1 or X != -1):
                lst += [str(int(i, 16))]
            elif(o != -1 or O != -1):
                lst += [str(int(i, 8))]
            else:
                lst += [i]
        return list(map(lambda x: int(x), lst))

    def visitArray_lit(self, ctx: BKITParser.Array_litContext):
        lst = []
        for i in range(len(ctx.array_value())):
            lst += self.visit(ctx.array_value(i))
        return ArrayLiteral(lst)

    def visitArray_value(self, ctx: BKITParser.Array_valueContext):
        arr = []
        if ctx.INT_LIT():
            i = ctx.INT_LIT().getText()
            x = i.find('x')
            X = i.find('X')
            o = i.find('o')
            O = i.find('O')
            if(x != -1 or X != -1):
                convert = int(i, 16)
            elif(o != -1 or O != -1):
                convert = int(i, 8)
            else:
                convert = int(i)
            arr += [IntLiteral(convert)]
        if ctx.FLOAT_LIT():
            arr += [FloatLiteral(float(ctx.FLOAT_LIT().getText()))]
        if ctx.BOOLEAN_LIT():
            arr += [BooleanLiteral(bool(ctx.BOOLEAN_LIT().getText()))]
        if ctx.STRING_LIT():
            arr += [StringLiteral(ctx.STRING_LIT().getText())]
        if ctx.array_lit():
            arr += [self.visit(ctx.array_lit())]
        return arr

    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        if ctx.INT_LIT():
            i = ctx.INT_LIT().getText()
            x = i.find('x')
            X = i.find('X')
            o = i.find('o')
            O = i.find('O')
            if(x != -1 or X != -1):
                convert = int(i, 16)
            elif(o != -1 or O != -1):
                convert = int(i, 8)
            else:
                convert = int(i)
            return IntLiteral(convert)
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.BOOLEAN_LIT():
            return BooleanLiteral(ctx.BOOLEAN_LIT().getText())
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        else:
            return self.visit(ctx.array_lit())

    def visitFunc_decl(self, ctx: BKITParser.Func_declContext):
        name = self.visit(ctx.func_name())
        if ctx.para_decl():
            param = self.visit(ctx.para_decl())
        else:
            param = []
        var = []
        stm = []
        if ctx.var_decl():
            for i in range(len(ctx.var_decl())):
                var += self.visit(ctx.var_decl(i))
        if ctx.stm_list():
            for j in range(len(ctx.stm_list())):
                stm += self.visit(ctx.stm_list(j))
        body = tuple([var] + [stm])
        return [FuncDecl(name, param, body)]

    def visitFunc_name(self, ctx: BKITParser.Func_nameContext):
        return Id(ctx.ID().getText())

    def visitPara_decl(self, ctx: BKITParser.Para_declContext):
        return self.visit(ctx.many_para_decl())

    def visitMany_para_decl(self, ctx: BKITParser.Many_para_declContext):
        if ctx.many_para_decl():
            return self.visit(ctx.one_para_decl()) + self.visit(ctx.many_para_decl())
        else:
            return self.visit(ctx.one_para_decl())

    def visitOne_para_decl(self, ctx: BKITParser.One_para_declContext):
        if ctx.scalar():
            dimen = []
            id = self.visit(ctx.scalar())
            literal = None
            return [VarDecl(id, dimen, literal)]
        else:
            dimen = self.visit(ctx.composit())
            id = Id(ctx.ID().getText())
            literal = None
            return [VarDecl(id, dimen, literal)]

    def visitStm_list(self, ctx: BKITParser.Stm_listContext):
        if ctx.assign_stm():
            return self.visit(ctx.assign_stm())
        elif ctx.while_stm():
            return self.visit(ctx.while_stm())
        elif ctx.if_stm():
            return self.visit(ctx.if_stm())
        elif ctx.for_stm():
            return self.visit(ctx.for_stm())
        elif ctx.do_while_stm():
            return self.visit(ctx.do_while_stm())
        elif ctx.call_stm():
            return self.visit(ctx.call_stm())
        elif ctx.break_stm():
            return self.visit(ctx.break_stm())
        elif ctx.continue_stm():
            return self.visit(ctx.continue_stm())
        else:
            return self.visit(ctx.return_stm())

    # ASSIGN

    def visitAssign_stm(self, ctx: BKITParser.Assign_stmContext):
        if ctx.ID():
            lhs = Id(ctx.ID().getText())
        else:
            lhs = self.visit(ctx.element_exp())
        rhs = self.visit(ctx.exp())
        return [Assign(lhs, rhs)]

    def visitElement_exp(self, ctx: BKITParser.Element_expContext):
        if ctx.ID():
            arr = Id(ctx.ID().getText())
        elif ctx.func_call():
            name,lst = self.visit(ctx.func_call())
            arr = CallExpr(name, lst)
        else:
            arr = self.visit(ctx.exp())
        idx = self.visit(ctx.index_op())
        return ArrayCell(arr, idx)

    def visitFunc_call(self, ctx: BKITParser.Func_callContext):
        lst = []
        name = Id(ctx.ID().getText())
        if ctx.list_argument():
            lst += self.visit(ctx.list_argument())
            return name,lst
        else:
            return name,[]

    def visitIndex_op(self, ctx: BKITParser.Index_opContext):
        lst = []
        if ctx.index_op():
            lst = [self.visit(ctx.exp())]+ self.visit(ctx.index_op())
            
        else:
            lst += [self.visit(ctx.exp())]
        return lst

    def visitList_argument(self, ctx: BKITParser.List_argumentContext):
        lst = []
        if ctx.list_argument():
            lst = [self.visit(ctx.exp())] + self.visit(ctx.list_argument())
        else:
            lst += [self.visit(ctx.exp())]
        return lst

    # IF
    def visitIf_stm(self, ctx: BKITParser.If_stmContext):
        ifthenStm = []  # list of tuples

        # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        # elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
        ifthenStm += [self.visit(ctx.ifthen_stm())]
        elseStm=None
        if ctx.else_stm():
            elseStm = self.visit(ctx.else_stm())
        else:
            elseStm = ([],[])
        if ctx.elif_stm():
            for i in range(len(ctx.elif_stm())):
                ifthenStm += [self.visit(ctx.elif_stm(i))]
        return [If(ifthenStm, elseStm)]

    def visitIfthen_stm(self, ctx: BKITParser.Ifthen_stmContext):
        expr = self.visit(ctx.exp())
        varlst = []
        stmlst = []
        if ctx.var_decl():
            for i in range(len(ctx.var_decl())):
                varlst += self.visit(ctx.var_decl(i))
        if ctx.stm_list():
            for i in range(len(ctx.stm_list())):
                stmlst += self.visit(ctx.stm_list(i))
        return (expr, varlst, stmlst)

    def visitElse_stm(self, ctx: BKITParser.Else_stmContext):
        varlst = []
        stmlst = []
        if ctx.var_decl():
            for i in range(len(ctx.var_decl())):
                varlst += self.visit(ctx.var_decl(i))
        if ctx.stm_list():
            for i in range(len(ctx.stm_list())):
                stmlst += self.visit(ctx.stm_list(i))
        return (varlst, stmlst)

    def visitElif_stm(self, ctx: BKITParser.Elif_stmContext):
        expr = self.visit(ctx.exp())
        varlst = []
        stmlst = []
        if ctx.var_decl():
            for i in range(len(ctx.var_decl())):
                varlst += self.visit(ctx.var_decl(i))
        if ctx.stm_list():
            for i in range(len(ctx.stm_list())):
                stmlst += self.visit(ctx.stm_list(i))
        return (expr, varlst, stmlst)

    # FOR
    def visitFor_stm(self, ctx: BKITParser.For_stmContext):
        idx1 = self.visit(ctx.scalar())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2))
        varlst = []
        stmlst = []
        if ctx.var_decl():
            for i in range(len(ctx.var_decl())):
                varlst += self.visit(ctx.var_decl(i))
        if ctx.stm_list():
            for i in range(len(ctx.stm_list())):
                stmlst += self.visit(ctx.stm_list(i))
        loop = (varlst, stmlst)
        return [For(idx1, expr1, expr2, expr3, loop)]

    def visitDo_while_stm(self, ctx: BKITParser.Do_while_stmContext):
        varlst = []
        stmlst = []
        if ctx.var_decl():
            for i in range(len(ctx.var_decl())):
                varlst += self.visit(ctx.var_decl(i))
        if ctx.stm_list():
            for i in range(len(ctx.stm_list())):
                stmlst += self.visit(ctx.stm_list(i))
        sl = (varlst, stmlst)
        expr = self.visit(ctx.exp())

        return [Dowhile(sl, expr)]

    def visitWhile_stm(self, ctx: BKITParser.While_stmContext):
        varlst = []
        stmlst = []
        if ctx.var_decl():
            for i in range(len(ctx.var_decl())):
                varlst += self.visit(ctx.var_decl(i))
        if ctx.stm_list():
            for i in range(len(ctx.stm_list())):
                stmlst += self.visit(ctx.stm_list(i))
        sl = (varlst, stmlst)
        expr = self.visit(ctx.exp())
        return [While(expr, sl)]

    def visitBreak_stm(self, ctx: BKITParser.Break_stmContext):
        return [Break()]

    def visitContinue_stm(self, ctx: BKITParser.Continue_stmContext):
        return [Continue()]

    def visitCall_stm(self, ctx: BKITParser.Call_stmContext):
        name,lst = self.visit(ctx.func_call())
        return [CallStmt(name,lst)]

    def visitReturn_stm(self, ctx: BKITParser.Return_stmContext):
        if ctx.exp():
            expr = self.visit(ctx.exp())
        else:
            expr = None
        return [Return(expr)]

    def visitExp(self, ctx: BKITParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        else:
            left_exp = self.visit(ctx.getChild(0))
            right_exp = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left_exp, right_exp)

    def visitExp1(self, ctx: BKITParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2())
        else:
            left_exp = self.visit(ctx.getChild(0))
            right_exp = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left_exp, right_exp)

    def visitExp2(self, ctx: BKITParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        else:
            left_exp = self.visit(ctx.getChild(0))
            right_exp = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left_exp, right_exp)

    def visitExp3(self, ctx: BKITParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        else:
            left_exp = self.visit(ctx.getChild(0))
            right_exp = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left_exp, right_exp)

    def visitExp4(self, ctx: BKITParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        else:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.getChild(1))
            return UnaryOp(op, body)

    def visitExp5(self, ctx: BKITParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        else:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.getChild(1))
            return UnaryOp(op, body)

    def visitExp6(self, ctx: BKITParser.Exp6Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.func_call():
            name,lst= self.visit(ctx.func_call())
            return CallExpr(name,lst)
        if ctx.exp():
            return self.visit(ctx.exp())
        else:
            return self.visit(ctx.element_exp())
