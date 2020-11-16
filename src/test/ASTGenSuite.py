import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_01(self):
        """Test Complex """
        input = """
            Var: x=3;
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 1))

    def test_02(self):
        """Test Complex """
        input = """ 
            Var: x=3,y,z=1.5e-1,t="abcd";
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3)), VarDecl((Id('y')), [],None), VarDecl(Id('z'), [], FloatLiteral(0.15)), VarDecl(Id('t'), [], StringLiteral('abcd'))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 2))

    def test_03(self):
        """Test Complex """
        input = """
            Var: x[2][3][4]=True;
        """
        expect = Program([VarDecl(Id('x'),[IntLiteral(2),IntLiteral(3),IntLiteral(4)],BooleanLiteral('True'))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 3))
    
    def test_04(self):
        """Test Complex """
        input = """
            Var: x={1,{"a"}};
        """
        expect = Program([VarDecl(Id('x'),[],ArrayLiteral([IntLiteral(1),ArrayLiteral([StringLiteral('a')])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 4))

    def test_05(self):
        """Test Complex """
        input = """
            Var : a=1e4,b=0.0e-5,c=0.00,d=0x322,e=0O12345;
        """
        expect = Program([VarDecl(Id('a'),[],FloatLiteral(10000.0)),VarDecl(Id('b'),[],FloatLiteral(0.0)),VarDecl(Id('c'),[],FloatLiteral(0.0)),VarDecl(Id('d'),[],IntLiteral(802)),VarDecl(Id('e'),[],IntLiteral(5349))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 5))

    def test_06(self):
        """Test Complex """
        input = """
            Var: x;
            Var: y;
            Var: z;
            Var: t;
        """
        expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None),VarDecl(Id('t'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 6))  

    def test_07(self):
        """Test simple FuncDecl """
        input = """
            Function: nam
            Body:
            EndBody.
        """
        expect = Program([FuncDecl(Id('nam'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 7))

    def test_08(self):
        """Test simple FuncDecl """
        input = """
            Function: nam
            Parameter: m,n
            Body:
            EndBody.
        """
        expect = Program([FuncDecl(Id('nam'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 8))

    def test_09(self):
        """Test simple FuncDecl """
        input = """
            Function: nam
            Parameter: m,n
            Body:
            Var:hello=5;
            EndBody.
        """
        expect = Program([FuncDecl(Id('nam'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None)],([VarDecl(Id('hello'),[],IntLiteral(5))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 9))

    def test_10(self):
        """Test simple FuncDecl """
        input = """
            Function: nam
            Parameter: m,n
            Body:
            Var:hello=5;
            Return;
            EndBody.
        """
        expect = Program([FuncDecl(Id('nam'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None)],([VarDecl(Id('hello'),[],IntLiteral(5))],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 10))
    
    def test_11(self):
        """Test simple FuncDecl """
        input = """
            Function: a_Nam123456
            Parameter: m[2][3],n[6][9][8]
            Body:
            EndBody.
        """
        expect = Program([FuncDecl(Id('a_Nam123456'),[VarDecl(Id('m'),[IntLiteral(2),IntLiteral(3)],None),VarDecl(Id('n'),[IntLiteral(6),IntLiteral(9),IntLiteral(8)],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 11))

    def test_12(self):
        """Test simple FuncDecl """
        input = """
            Function: a_Nam123456
            Parameter: m[2][3],n[6][9][8]
            Body:
            Var: x=0xFF,y=0xFF,z=0o22;
            EndBody.
        """
        expect = Program([FuncDecl(Id('a_Nam123456'),[VarDecl(Id('m'),[IntLiteral(2),IntLiteral(3)],None),VarDecl(Id('n'),[IntLiteral(6),IntLiteral(9),IntLiteral(8)],None)],([VarDecl(Id('x'),[],IntLiteral(255)),VarDecl(Id('y'),[],IntLiteral(255)),VarDecl(Id('z'),[],IntLiteral(18))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 12))
    
    def test_13(self):
        """Test simple FuncDecl """
        input = """
            Function: thanhnam_1813130
            Parameter: m[2][3],n[6][9][8]
            Body:
            Var: x[1]={1,2,3};
            Var: y = "$%^%$^$";
            EndBody.
        """
        expect = Program([FuncDecl(Id('thanhnam_1813130'),[VarDecl(Id('m'),[IntLiteral(2),IntLiteral(3)],None),VarDecl(Id('n'),[IntLiteral(6),IntLiteral(9),IntLiteral(8)],None)],([VarDecl(Id('x'),[IntLiteral(1)],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id('y'),[],StringLiteral('$%^%$^$'))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 13))
    
    def test_14(self):
        """Test FuncDecl with assign_stm """
        input = """
            Function: nam
        Parameter: x,y,a[20]
        Body:
            y=x*2;
        EndBody.
        """
        expect = Program([FuncDecl(Id('nam')[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id(a),[IntLiteral(20)])],([][Assign(Id(y),BinaryOp(*,Id(x),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 14))

    def test_15(self):
        """Test Complex FuncDecl """
        input = """
            Function: thanhnam_1813130
           
            Body:
            a = foo(2)[0xFF];
            foo(2); 
            foo(2)[3] = a+1; 
            a=foo(2);
            EndBody.
        """
        expect = Program([FuncDecl(Id('thanhnam_1813130'),[],([],[Assign(Id('a'),ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),[IntLiteral(255)])),CallStmt(Id('foo'),[IntLiteral(2)]),Assign(ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp('+',Id('a'),IntLiteral(1))),Assign(Id('a'),CallExpr(Id('foo'),[IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 15))

    def test_16(self):
        """Test Complex FuncDecl """
        input = """
            Function: sort
        Parameter: arr[0o100], left, right
        Body:
            For(i = left + 1, i <= right, 1) Do
                Var: temp, j;
                temp = arr[i];
                j = i - 1;
                While (j >= left) && (arr[j] > temp) Do
                    arr[j + 1] = arr[j];
                    j = j - 1;
                EndWhile.
                arr[j + 1] = temp;
            EndFor.
        EndBody.
            
        """
        expect =  Program([FuncDecl(Id('sort'), [VarDecl(Id('arr'), [0o100], None), VarDecl(Id('left'), [], None), VarDecl(Id('right'), [], None)], ([], [\
                For(Id('i'), BinaryOp('+', Id('left'), IntLiteral(1)), BinaryOp('<=', Id('i'), Id('right')), IntLiteral(1), ([VarDecl(Id('temp'), [], None), VarDecl(Id('j'), [], None)], \
                [Assign(Id('temp'), ArrayCell(Id('arr'), [Id('i')])), Assign(Id('j'), BinaryOp('-', Id('i'), IntLiteral(1))),\
                While(BinaryOp('&&', BinaryOp('>=', Id('j'), Id('left')), BinaryOp('>', ArrayCell(Id('arr'), [Id('j')]), Id('temp'))),([], [Assign(ArrayCell(Id('arr'), [BinaryOp('+', Id('j'), IntLiteral(1))]), ArrayCell(Id('arr'), [Id('j')])), Assign(Id('j'), BinaryOp('-', Id('j'), IntLiteral(1)))])),\
                Assign(ArrayCell(Id('arr'), [BinaryOp('+', Id('j'), IntLiteral(1))]), Id('temp'))
                ]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 16))

    def test_17(self):
        """Test Complex FuncDecl """
        input = """
            Function: main
        Body:
            a = f(2, 3 + 4)[10 * 0xFF];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [], ([], [Assign(Id('a'), ArrayCell(CallExpr(Id('f'), [IntLiteral(2), BinaryOp('+', IntLiteral(3), IntLiteral(4))]), [BinaryOp('*', IntLiteral(10), IntLiteral(255))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 17))

    def test_18(self):
        """Test Complex FuncDecl """
        input = """
            Function: main
        Body:
            **If statement**
            If a Then b();  Else EndIf.
        EndBody.
        """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 18))
    def test_19(self):
        """Test Complex FuncDecl """
        input = """
            Function: main
        Body:
            **If statement**
            If a Then  Else EndIf.
        EndBody.
        """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 19))

    def test_20(self):
        """Test Complex """
        input = """
            Var: a=\"hello\",b=0.0e4,c=25,d={0};
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 20))
    def test_21(self):
        """Test Complex """
        input = """
            Function: nam
        Parameter: x,y,a[20]
        Body:
            y=x*2;
            foo(5);
            a[6]=5*foo(4);
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 21))
    def test_22(self):
        """Test Complex """
        input = """
            Function: nam
        Parameter: x,y,a[20]
        Body:
            While ((x != 2) && (y \\ 3)) Do **nothing**
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 22))
    def test_23(self):
        """Test Complex """
        input = """
            Function: nam
        Parameter: x,y,a[20]
        Body:
            a=-a;
            a=1+2;
            b=!a;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 23))
    def test_24(self):
        """Test Complex """
        input = """
            Function: nam
        Parameter: x,y,a[20]
        Body:
            If(abcxyz == them) Then
                For(i=2,i<9,a+2) Do
                x=x+y;
                EndFor.
            ElseIf (True) Then
                **do nothing**
            Else 
            a=b+d;
            foo(2);
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 24))
    def test_25(self):
        """Test Complex """
        input = """
             Function: nam
        Body:
            For(a9=0xFFFF,b<5,d+.3e4) Do
            foo(4+.5*.r*.r);
            Return (!x);
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 25))
    def test_26(self):
        """Test Complex """
        input = """
            Function: nam
        Body:
            print("Hello World");
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 26))

    def test_27(self):
        """Test Complex """
        input = """
            Function: nam
        Parameter: n
        Body:
            If((n % 2) == 0) Then print("even");
            Else print("odd");
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 27))
    def test_28(self):
        """Test Complex """
        input = """
            Function: nam
        Parameter: n
        Body:
            For(i=0,i<n,1) Do
            print(i);
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 28))
    def test_29(self):
        """Test Complex """
        input = """
            Var: x=3,y[5]={\"a\",0e4};
        Function: nam
        Parameter: k,m,n
        Body:
            foo(12.5+True)[4] = \"hello\";
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 29))
    def test_30(self):
        """Test Complex """
        input = """
             Var: nam,thy=\"thy\",hello=9;
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 30))
    def test_31(self):
        """Test Complex """
        input = """
            Var: a,b,c,l[0x4332A];
        Function: nam **#$%#$%#$%#$**
        Parameter: rapViet,kingOf_rAp
        Body:
            Var:html,css=3;
            While (x == 1) Do
            If(3<2) Then i=3+2;
            Else
            Break;
            EndIf.
            EndWhile. 
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 31))
    def test_32(self):
        """Test Complex """
        input = """
            Var: x[3][0xFFFAA];
        Function: n___Am___hahsdh_
        Parameter: namngaytho
        Body:
            For(i=3+y,i<5,2) Do
            If(nothing(nothing(nothing(1)))) Then
            If(nothing(2)) Then EndIf.
            EndIf.
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 32))

    def test_33(self):
        """Test Complex """
        input = """
            Function: n__________A_______Mkaka23132141wq123
        Parameter: noneed
        Body:
            Break;
            Break;
            Continue;
            Break;
            Break;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 33))

    def test_34(self):
        """Test Complex """
        input = """
            Var : a,b,c={{1,2,3},{3,4,"String never die"}};
        Function: main
        Body:
            Return;
            Return foo(3-.fooooo("abc"));
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 34))

    def test_35(self):
        """Test Complex """
        input = """
            
        Function: main
        Body:
            Do
            x=a(x+x(5+x(5)));
            Return 0;
            While (x!=2)
            EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect,35))

    def test_36(self):
        """Test Complex """
        input = """
            Var: m, n[10]; 
            Function: main 
           
                Parameter: n 
                Body: 
                x = 12e+4444;
               If n =/= 0 Then 
                   Return 1; 
               Else    Return n*main({4,5});
                EndIf.
                 EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 36))

    def test_37(self):
        """Test Complex """
        input = """
            Function:main
        Body:
        Var: i = 5;
        While(i>0) Do
        print(print(print(i)));
        Continue;
        EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 37))

    def test_38(self):
        """Test Complex """
        input = """
            Function:main
        Body:
        Var: i = 5;
        While(i>0) Do
        print(print(print(i)));
        Continue;
        EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 38))

    def test_39(self):
        """Test Complex """
        input = """
            Function: ma__ABCDE____Fin
         Body:
            foo(print(ggwp({{1,2,3},{"abC:???"}})));
            Continue;
            Break;Continue;
            Break;Continue;
            Break;Continue;
            Break;
                     EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 39))

    def test_40(self):
        """Test Complex """
        input = """
            Var: x,a,bcd;
        Function: nam
        Parameter: m[5],n[100]
        Body:
            Var:k,j;
            x=a(5)[6][0xFA][0o44];
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 40))

    def test_41(self):
        """Test Complex """
        input = """
            **Var: x="?#!@!$!@$!",y=5,****z=12.6,k={"@#$@#$@dsadjkhasdjkhas"};**
        Function: noname
        Parameter: x
         Body:
            Return;
            Return;
            Return;
            Return;
            Return;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 41))

    def test_42(self):
        """Test Complex """
        input = """
            Var: a,b,c;
        Function: n_o_n_a_m_e
        Parameter: none
         Body:
            If(i == 1) Then print(i);print(i);print(i);print(i);print(i);print(i);
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 42))

    def test_43(self):
        """Test Complex """
        input = """
            Var: x = "%%%%%%%%%", y = 6 , m[0o1111] = 1e9999;
        Function: mainSDADASD12312132
         Body:
         Var:x,y,z;
         While(!!!!6=/=9)
         Do print(print(print(in(in(i)))));
         EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 43))

    def test_44(self):
        """Test Complex """
        input = """
            Var: x = "\b\b\b\b\b", y = 6e444 , m[0o1111];
        Function: nam__t_h_y
         Body:
            **do nothing**
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 44))

    def test_45(self):
        """Test Complex """
        input = """
            Function: nAm
        Parameter: n[100],m[1000]
        Body: 
            Var: kkk[5][6]="@#!$!@$!!!!!",a=0.e+4 ;
            Var: kkk[5][6]="@#!$!@$!!!!!",a=0.e+4 ;
            Var: kkk[5][6]="@#!$!@$!!!!!",a=0.e+4 ;
            c= c(**555555**)+ a[0xBCD];
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 45))

    def test_46(self):
        """Test Complex """
        input = """
            Function: nAm___
        Parameter: n[100],m[1000]
        Body: 
            foo(2. +. 4., 2 *. 10,c(in(in(in4))));
            Do While(x<3) EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 46))

    def test_47(self):
        """Test Complex """
        input = """
            Function: fact
        Body:
        a[foo(3*foo(3))]= a[1+foo(3)[5]]; 
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 47))

    def test_48(self):
        """Test Complex """
        input = """
            Var:a,b,c;
        Function: fact
        Parameter:x,y,z
        Body:
        Var: sadasd=4455;
            While(x>3) Do
                If(False) Then 
                ElseIf(!!!a) Then
                Else
                    For(i=0xFF,i<5,1) Do
                    **no thing**
                    EndFor.
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 48))
    def test_49(self):
        """Test Complex """
        input = """
            Var:a,b,c;
        Function: fact
        Parameter:x,y,z
        Body:
        Var: sad____asd=4455;
            While(x>3) Do
                If(False) Then 
                Return;
                ElseIf(!!!a) Then
                Break;
                Else
                    For(i=0xFF,i<5,1) Do
                    **no thing**
                    Continue;
                    Break;
                    Return {1,2,3};
                    EndFor.
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 49))
    def test_50(self):
        """Test Complex """
        input = """
            Var:a__11_22[3]={1,2,"#@$@#$2"};
        Function: fact_1
        
        Parameter:f,f,f,f,f
        Body:
        If "**hello**" Then
        inxxx= 128983 - 4234 +. 43223.55e+4 || !!!!False;
        inpa231 = {123, 435, 423} * in;
        EndIf.
            
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 50))
    def test_51(self):
        """Test Complex """
        input = """
            Function: main
        **good comment **
        Body:
            If(x == (2==1)) =/= 3 Then foo(3);
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 51))
    def test_52(self):
        """Test Complex """
        input = """
            Function: main
        **good comment **
        Body:
            If(x == (2==1)) =/= 3 Then 
            x = (4 +. True * "abcy#$@@#$" --.-- (5\\foo(2)));
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 52))
    def test_53(self):
        """Test Complex """
        input = """
            Var : x = 3, y = 12.e004;
        Function: main
        Body:
        **** 
        EndBody.
        Function: main
        Body:
        **a=b;** 
        EndBody.
        Function: main_1
        Body:
         a=b; 
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 53))
    def test_54(self):
        """Test Complex """
        input = """
            Function: main
        Body:
        a=f(f(f(f(****))));
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 54))
    def test_55(self):
        """Test Complex """
        input = """
            Function: fact
        Parameter: x, a[2]
        Body:
            For (i = 0, i < 10, 2) Do
                If (x) Then Break; EndIf.
            EndFor.
            If (x) Then Break; EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 55))
    def test_56(self):
        """Test Complex """
        input = """
            Function: breaktest
        Parameter: x
        Body:
            While x >= 1 Do
                If y<100 Then Break;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 56))
    def test_57(self):
        """Test Complex """
        input = """
            Function: testreturn
        Parameter: n
        Body:
            Var: t=False;
            If n<100 Then t=True;
            EndIf.
            Return t;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 57))
    def test_58(self):
        """Test Complex """
        input = """
            Function: array
        Parameter: x[123]
        Body:
            Var: i = 0;
            x[123]={996,712,216};
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 58))
    def test_59(self):
        """Test Complex """
        input = """
            Function: array_null
        Body:
            a[12] = {  };
            x[45]={{{{{}}}}};

        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 59))
    def test_60(self):
        """Test Complex """
        input = """
            Function: callincall
        Body:
            a =func1(foo(3))+23 - func2(goo(foo(a)));
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 60))
    def test_61(self):
        """Test Complex """
        input = """
            Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            If (a + 5) && (j-6) || (k*7) Then

                a[i] = b +. 1.0;
                b = i - b * a -. b \ c - -.d;
            EndIf.
            Return a+func(123);
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 61))
    def test_62(self):
        """Test Complex """
        input = """
            Function: main
        Body:
            func();
            Return 0;
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 62))
    def test_63(self):
        """Test Complex """
        input = """
            Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            If bool_of_string ("True") Then
                a = int_of_string (read ());
                b = float_of_int (a) +. 2.0;
            ElseIf a == 5 Then
                a = a + main(123);
                Return a;
            ElseIf a == 6 Then
                a = a *. 2;
                Break;
            Else Continue;
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 63))
    def test_64(self):
        """Test Complex """
        input = """
            Function: index
        Body:
            arr(leanhthy + thanhnam[61.2 *. (x + y)])[2] = b[2][3];
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 64))
    def test_65(self):
        """Test Complex """
        input = """
            Function: test1
        Body:
            m = test2(a,b) + test1 (x);
        EndBody.
        Function: test2
        Body:
            Do
                If(z == 1) Then
                    x = !(-a);
                    a=foo(2)[0o77];
                EndIf.
            While x
            EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 65))
    def test_66(self):
        """Test Complex """
        input = """
            Function: alias
            Parameter: a,b
            Body:
                a[3 +. 10e2] = (foo(x) +. 12.e3) *. 0x123 - a[b[0xff][0o22]] + 4;
            EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 66))
    def test_67(self):
        """Test Complex """
        input = """
            Function: namngaytho69
            Body:
                Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
                Var: b = True, c = False;
                For (i = 0, i < 10, 2) Do
                    For (i = 1, i < x*x , i + 1 ) Do
                        If(z == False) Then
                            x = haha();
                        EndIf.
                        For( j = 1, j < x*x ,j + 1) Do
                            Do
                                a = a * 1;
                            While( 1 )
                            EndDo.
                        EndFor.
                    EndFor.
                EndFor.
            EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 67))
    def test_68(self):
        """Test Complex """
        input = """
            Function: test
        Body:
            While True Do
                s = str(input());
                If len(s) == 0 Then
                    Continue;
                EndIf.
                arr[arr + i] = append(split(arr, " "));
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 68))
    def test_69(self):
        """Test Complex """
        input = """
            Function: nA____mmmm_________mm
        Parameter: a, b
        Body:
            Var: sum = 0.;
            If len(a) =/= len(b) Then raise(error()); EndIf.
            For(i = 0, i < len(a), 1) Do
                sum = sum + (a[i] - b[i]) * (a[i] - b[i]);
            EndFor.
            print(sum * sum \. 2);
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 69))
    def test_70(self):
        """Test Complex """
        input = """
            Var: x, y, z, t;
        Function: test___
        Body:
            Var: a, b, c;
            Var: ksd[123][0x10][0o231340];
            Var: s = "132";
            Var: f = 0x13, sd = 123, s = "ad", k = 0.123, u = {1, 2, 4, 5, 6};
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 70))
    def test_71(self):
        """Test Complex """
        input = """
            Function: t_2937124
        Parameter: arr[100]
        Body:
            Var: sum = 0;
            create_multi_threads(num_threads);
            For (i = 0, i < len, 1) Do
                lock();
                sum = sum + arr[i];
                unlock();
            EndFor.
            destroy_all_resources();
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 71))
    def test_72(self):
        """Test Complex """
        input = """
            Var:x;
        Function: test
        Body:
            f = -1234.;
            Do 
                Do
                    If k Then If k Then EndIf. EndIf.
                While False
                EndDo.
            While f < 10
            EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 72))
    def test_73(self):
        """Test Complex """
        input = """
            Var: b = False, arr[0o10] = {120, 0x123};
        Function: supertest **comment**
        Body:
            Do
                While True Do
                    lock(a+b[2]);
                    send(i + 1);
                    unlock();
                EndWhile.
            While True EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 73))
    def test_74(self):
        """Test Complex """
        input = """
            Var: var = {0o123, 123., 123e-1, "das", 0x123};
        Function: vadaylaRapViet
        Body:
            Var: x = 12;
            For(i = "dasd" * 12, "dasd", "d") Do
                Var: m = 10;
                If m != 10 Then
                    Var: x;
                    x = int(input());
                ElseIf m && False Then
                    Var: x;
                    print(x);
                Else
                    Do
                        Var: k;
                        king_Of_Rap = int(input());
                        If k == 10 Then
                            Var: i;
                            Break;
                        EndIf.
                    While True EndDo.
                EndIf.
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 74))
    def test_75(self):
        """Test Complex """
        input = """
            Function: test
        Body:
            If n == 0 Then
                Return n;
            Else
                If test > 0 Then
                    print("akakakak");
                EndIf.
                Return n % 10 + test(n \ 10);
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 75))
    def test_76(self):
        """Test Complex """
        input = """
            Var : x[0xabc];
            Function: wjbu
            Body:
                print("************");
                print("*    OoO   *");
                print("************");
            EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 76))
    def test_77(self):
        """Test Complex """
        input = """
            Function: test
        Parameter: str
        Body:
            Var: dt;
            For(i = 0, i < len(str), 1) Do
                dt[dt[dt[arr[i]]]] = dt[arr[dt[arr[i]]]] + 1;
                f(dt, k * {1, 2, 3, 4});
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 77))
    def test_78(self):
        """Test Complex """
        input = """
            Var: arr[123] = {1, 2, 3, 5, "dasd", {12, {12}}};
        Function: test
        Parameter: array
        Body:
            While array Do
                If arr Then
                    For(i = 0, i < length(arr), step()) Do
                        print(arr[i] * kk);
                    EndFor.
                    If True && (123 == 3123) Then
                        do();
                        Break;
                    EndIf.
                EndIf.
            EndWhile.
            Return;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 78))
    def test_79(self):
        """Test Complex """
        input = """
            Function: senpaiiiiiiiiiiiiiiiiiii
        Body:
            For(i = 0, i < len(row), 1) Do
                For(j = 0, i < len(col), 1) Do
                    result[i][j] = row[i] * col[j];
                EndFor.
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 79))
    def test_80(self):
        """Test Complex """
        input = """
            Var: arr[10][0o10] = {{1,2,3,4}, {1,2,3}, {2,3,4}};
            Var: arr[10][0o10] = {{1,2,3,4}, {1,2,3}, {2,3,4}};
            Var: arr[10][0o10] = {{1,2,3,4}, {1,2,3}, {2,3,4}};
            Var: arr[10][0o10] = {{1,2,3,4}, {1,2,3}, {2,3,4}};
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 80))
    def test_81(self):
        """Test Complex """
        input = """
            Var: arr[10][0o10] = {{1,2,3,4}, {1,2,3}, {2,3,4}};
            Var: arr[10][0o10] = {{1,2,3,4}, {1,2,3}, {2,3,4}};
            Var: arr[10][0o10] = {{1,2,3,4}, {1,2,3}, {2,3,4}};
            Var: arr[10][0o10] = {{1,2,3,4}, {1,2,3}, {2,3,4}};
            Function: test
            Parameter: arr[10][0o10],arr[10][0o10],arr[10][0o10]
            Body:
            EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 81))
    def test_82(self):
        """Test Complex """
        input = """
            Var: t = 0;

        Function: mk
        Parameter: x
        Body:
            If n == 0 Then p = 0;
            ElseIf n == 1 Then p = 1;
            ElseIf n == 2 Then p = 3;
            Else p = n+3;
            EndIf.
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 82))
    def test_83(self):
        """Test Complex """
        input = """
            Var: t = 0;
        Function: mk
        Parameter: x
        Body:
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
            While 2==2 Do
                Do
                    a = 9;
                While x==2 EndDo.
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 83))
    def test_84(self):
        """Test Complex """
        input = """
            Function: ff 
        Parameter: nq,p,o,i
        Body: 
            While n == 0 Do
                Var: awq = 7;
                Return 1;
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 84))
    def test_85(self):
        """Test Complex """
        input = """
            Function: ccd 
        Parameter: n 
        Body: 
            For (k=4,k<2,3) Do x=6; EndFor.
            For (i = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 85))
    def test_86(self):
        """Test Complex """
        input = """
            Function: bar 
        Parameter: n
        Body: 
            a= (a==b)!= c ;
            x= (x =/= y) <. z;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 86))
    def test_87(self):
        """Test Complex """
        input = """
            Function: foo 
        Parameter: n
        Body: 
            x= (x*3)*. 0x3E \ (y \. 0.123) % 5;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 87))
    def test_88(self):
        """Test Complex """
        input = """
            Function: dsa 
        Parameter: n
        Body: 
            For (i = 0, i != 5, i*1) Do ewx=6; EndFor.
            Do
                ewx = a + b;
                writeln(ewx);
            While(True || False || True || (a > b)) EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 88))
    def test_89(self):
        """Test Complex """
        input = """
            Function: ge35 
        Parameter: n
        Body: 
            Do
                Do
                    x=5;
                While(a!=3) EndDo.
            While(c != 3) EndDo.
            For (i = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 89))
    def test_90(self):
        """Test Complex """
        input = """
            Var: t = 0;
        Function: mk
        Parameter: x    
        Body:
            Var: t[3], b[5][6] = {}, r;
            Return b;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 90))
    def test_91(self):
        """Test Complex """
        input = """
            Var: t = 0;
        Function: mk
        Parameter: x
        Body:
            x = False == True;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 91))
    def test_92(self):
        """Test Complex """
        input = """
            Function: df 
        Parameter: n 
        Body: 
            c = !a; 
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 92))
    def test_93(self):
        """Test Complex """
        input = """
            Function: nam
            Body: 
            EndBody.
            Function: nam
            Body: 
            EndBody.
            Function: nam
            Body: 
            EndBody.
            Function: nam
            Body: 
            EndBody.
            Function: nam
            Body: 
            EndBody.
            Function: nam
            Body: 
            EndBody.
            Function: nam
            Body: 
            EndBody.
            Function: nam
            Body: 
            EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 93))
    def test_94(self):
        """Test Complex """
        input = """
            Function: nam
            Body: 
                If a Then b(); Else c(a[3]+0xff); EndIf.
                If a Then b(); Else c(a[3]+0xff); EndIf.
                If a Then b(); Else c(a[3]+0xff); EndIf.
                If a Then b(); Else c(a[3]+0xff); EndIf.
                If a Then b(); Else c(a[3]+0xff); EndIf.
            EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 94))
    def test_95(self):
        """Test Complex """
        input = """
            Function: import 
        Parameter: n 
        Body: 
            For (i=0, x<10, i*1) Do x=6; EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 95))
    def test_96(self):
        """Test Complex """
        input = """
            Function: po_h_u_b
        Parameter: y, x, fn, theta
        Body:
            Var: sum = 0.;
            sum = mean(abs(y - fn(x)), "mean");
            If sum <= theta Then
                Return mean(square(y - fn(x)), "mean") \. 2;
            Else
                Return theta * abs(y - fn(x)) - theta * theta \. 2;
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 96))
    def test_97(self):
        """Test Complex """
        input = """
            Function: callwithoutsemi
        Body:
            iden__TI_FIerOf_Function(a,b_,c+.3.e-2);
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 97))
    def test_98(self):
        """Test Complex """
        input = """
            Var: max_length = 100;
        Function: countintSort
        Parameter: arr[100]
        Body:
            Var: output[100];
            Var: count[100], i;
            memset(count, 0, sizeof(count));
            For(i = 0, arr[i] > 0, 1) Do
                count[arr[i]] = count[arr[i]] + 1;
            EndFor.
            For(i = 1, i <= range(arr), 1) Do
                count[i] = count[i] + count[i - 1];
            EndFor.
            For(i = 0, arr[i] > 0, 1) Do
                output[count[arr[i]] - 1] = arr[i];
                count[arr[i]] = count[arr[i]] - 1;
            EndFor.
            For( i = 0, arr[i] != 0, 1) Do
                If i % 2 == 0 Then
                    arr[i] = i \\ 2;
                ElseIf i % 3 == 0 Then
                    arr[i] = 3 *. i;
                ElseIf i % 5 == 1 Then
                    arr[i] = i;
                Else
                    arr[i] = output[i];
                EndIf.
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 98))
    def test_99(self):
        """Test Complex """
        input = """
            Var:x;
            Function:hello
            Body:
            print("hello,world");
            EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 99))
    
    def test_100(self):
        """Test Complex """
        input = """
            Var:x;
            Function:bye
            Body:
            print("hello,world");
            print("goodbye,world");
            EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 100))
    