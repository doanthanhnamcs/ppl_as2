import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # def test_01(self):
    #     """Test simple VarDecl """
    #     input = """
    #         Var: x=3;
    #     """
    #     expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 1))

    # def test_02(self):
    #     """Test simple VarDecl """
    #     input = """ 
    #         Var: x=3,y,z=1.5e-1,t="abcd";
    #     """
    #     expect = Program([VarDecl(Id('x'), [], IntLiteral(3)), VarDecl((Id('y')), [],None), VarDecl(Id('z'), [], FloatLiteral(0.15)), VarDecl(Id('t'), [], StringLiteral('abcd'))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 2))

    # def test_03(self):
    #     """Test simple VarDecl """
    #     input = """
    #         Var: x[2][3][4]=True;
    #     """
    #     expect = Program([VarDecl(Id('x'),[IntLiteral(2),IntLiteral(3),IntLiteral(4)],BooleanLiteral('True'))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 3))
    
    def test_04(self):
        """Test simple VarDecl """
        input = """
            Var: x={1,2,3,{True,False},{"abc"}},y,z[2][3];
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 4))