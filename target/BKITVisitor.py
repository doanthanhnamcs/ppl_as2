# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#declarations.
    def visitDeclarations(self, ctx:BKITParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl.
    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_var_decl.
    def visitMany_var_decl(self, ctx:BKITParser.Many_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#one_var_decl.
    def visitOne_var_decl(self, ctx:BKITParser.One_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_decl.
    def visitFunc_decl(self, ctx:BKITParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_name.
    def visitFunc_name(self, ctx:BKITParser.Func_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_decl.
    def visitPara_decl(self, ctx:BKITParser.Para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_para_decl.
    def visitMany_para_decl(self, ctx:BKITParser.Many_para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#one_para_decl.
    def visitOne_para_decl(self, ctx:BKITParser.One_para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composit.
    def visitComposit(self, ctx:BKITParser.CompositContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#scalar.
    def visitScalar(self, ctx:BKITParser.ScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_lit.
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_value.
    def visitArray_value(self, ctx:BKITParser.Array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stm_list.
    def visitStm_list(self, ctx:BKITParser.Stm_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stm.
    def visitAssign_stm(self, ctx:BKITParser.Assign_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stm.
    def visitIf_stm(self, ctx:BKITParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifthen_stm.
    def visitIfthen_stm(self, ctx:BKITParser.Ifthen_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elif_stm.
    def visitElif_stm(self, ctx:BKITParser.Elif_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_stm.
    def visitElse_stm(self, ctx:BKITParser.Else_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stm.
    def visitFor_stm(self, ctx:BKITParser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stm.
    def visitWhile_stm(self, ctx:BKITParser.While_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_stm.
    def visitDo_while_stm(self, ctx:BKITParser.Do_while_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stm.
    def visitBreak_stm(self, ctx:BKITParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stm.
    def visitContinue_stm(self, ctx:BKITParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stm.
    def visitCall_stm(self, ctx:BKITParser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stm.
    def visitReturn_stm(self, ctx:BKITParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#element_exp.
    def visitElement_exp(self, ctx:BKITParser.Element_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_op.
    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_argument.
    def visitList_argument(self, ctx:BKITParser.List_argumentContext):
        return self.visitChildren(ctx)



del BKITParser