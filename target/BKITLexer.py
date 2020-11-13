# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0226\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\7\2\u009c\n\2\f\2\16\2\u009f\13\2\3\3\3\3\3")
        buf.write("\3\7\3\u00a4\n\3\f\3\16\3\u00a7\13\3\3\3\3\3\5\3\u00ab")
        buf.write("\n\3\3\4\3\4\5\4\u00af\n\4\3\5\6\5\u00b2\n\5\r\5\16\5")
        buf.write("\u00b3\3\5\5\5\u00b7\n\5\3\5\3\5\3\5\6\5\u00bc\n\5\r\5")
        buf.write("\16\5\u00bd\3\5\3\5\5\5\u00c2\n\5\5\5\u00c4\n\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\3=\3=\3=\3=\7=\u01a4\n=\f=\16=\u01a7\13")
        buf.write("=\3=\3=\3=\3=\3=\3>\3>\3?\3?\3@\3@\6@\u01b4\n@\r@\16@")
        buf.write("\u01b5\3@\6@\u01b9\n@\r@\16@\u01ba\3@\7@\u01be\n@\f@\16")
        buf.write("@\u01c1\13@\3A\3A\6A\u01c5\nA\rA\16A\u01c6\3A\6A\u01ca")
        buf.write("\nA\rA\16A\u01cb\3A\7A\u01cf\nA\fA\16A\u01d2\13A\3B\3")
        buf.write("B\5B\u01d6\nB\3B\6B\u01d9\nB\rB\16B\u01da\3C\3C\7C\u01df")
        buf.write("\nC\fC\16C\u01e2\13C\3D\6D\u01e5\nD\rD\16D\u01e6\3D\3")
        buf.write("D\3E\3E\3E\3E\5E\u01ef\nE\3F\3F\3F\3G\3G\3G\3G\5G\u01f8")
        buf.write("\nG\3H\3H\7H\u01fc\nH\fH\16H\u01ff\13H\3H\3H\3H\3I\3I")
        buf.write("\7I\u0206\nI\fI\16I\u0209\13I\3I\3I\3I\3J\3J\7J\u0210")
        buf.write("\nJ\fJ\16J\u0213\13J\3J\5J\u0216\nJ\3J\3J\3K\3K\3K\3K")
        buf.write("\3K\7K\u021f\nK\fK\16K\u0222\13K\3L\3L\3L\2\2M\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}")
        buf.write("@\177\2\u0081\2\u0083\2\u0085\2\u0087A\u0089\2\u008b\2")
        buf.write("\u008d\2\u008fB\u0091C\u0093D\u0095E\u0097F\3\2\25\3\2")
        buf.write("c|\6\2\62;C\\aac|\3\2\62\62\3\2,,\3\2\62;\3\2\63;\4\2")
        buf.write("ZZzz\4\2\63;CH\4\2\62;CH\4\2QQqq\3\2\639\3\2\629\5\2G")
        buf.write("Ggg~~\4\2--//\5\2\13\f\17\17\"\"\6\2\f\f$$))^^\t\2))^")
        buf.write("^ddhhppttvv\3\2$$\3\3\f\f\2\u023c\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2")
        buf.write("\2\5\u00aa\3\2\2\2\7\u00ae\3\2\2\2\t\u00c3\3\2\2\2\13")
        buf.write("\u00c5\3\2\2\2\r\u00ca\3\2\2\2\17\u00d0\3\2\2\2\21\u00d9")
        buf.write("\3\2\2\2\23\u00dc\3\2\2\2\25\u00e1\3\2\2\2\27\u00e8\3")
        buf.write("\2\2\2\31\u00f0\3\2\2\2\33\u00f6\3\2\2\2\35\u00fd\3\2")
        buf.write("\2\2\37\u0106\3\2\2\2!\u010a\3\2\2\2#\u0113\3\2\2\2%\u0116")
        buf.write("\3\2\2\2\'\u0120\3\2\2\2)\u0127\3\2\2\2+\u012c\3\2\2\2")
        buf.write("-\u0130\3\2\2\2/\u0136\3\2\2\2\61\u013b\3\2\2\2\63\u0141")
        buf.write("\3\2\2\2\65\u0147\3\2\2\2\67\u0149\3\2\2\29\u014c\3\2")
        buf.write("\2\2;\u014e\3\2\2\2=\u0151\3\2\2\2?\u0153\3\2\2\2A\u0156")
        buf.write("\3\2\2\2C\u0158\3\2\2\2E\u015b\3\2\2\2G\u015d\3\2\2\2")
        buf.write("I\u015f\3\2\2\2K\u0162\3\2\2\2M\u0165\3\2\2\2O\u0168\3")
        buf.write("\2\2\2Q\u016b\3\2\2\2S\u016d\3\2\2\2U\u016f\3\2\2\2W\u0172")
        buf.write("\3\2\2\2Y\u0175\3\2\2\2[\u0179\3\2\2\2]\u017c\3\2\2\2")
        buf.write("_\u017f\3\2\2\2a\u0183\3\2\2\2c\u0187\3\2\2\2e\u0189\3")
        buf.write("\2\2\2g\u018b\3\2\2\2i\u018d\3\2\2\2k\u018f\3\2\2\2m\u0191")
        buf.write("\3\2\2\2o\u0193\3\2\2\2q\u0195\3\2\2\2s\u0197\3\2\2\2")
        buf.write("u\u0199\3\2\2\2w\u019b\3\2\2\2y\u019d\3\2\2\2{\u01ad\3")
        buf.write("\2\2\2}\u01af\3\2\2\2\177\u01b1\3\2\2\2\u0081\u01c2\3")
        buf.write("\2\2\2\u0083\u01d3\3\2\2\2\u0085\u01dc\3\2\2\2\u0087\u01e4")
        buf.write("\3\2\2\2\u0089\u01ee\3\2\2\2\u008b\u01f0\3\2\2\2\u008d")
        buf.write("\u01f7\3\2\2\2\u008f\u01f9\3\2\2\2\u0091\u0203\3\2\2\2")
        buf.write("\u0093\u020d\3\2\2\2\u0095\u0219\3\2\2\2\u0097\u0223\3")
        buf.write("\2\2\2\u0099\u009d\t\2\2\2\u009a\u009c\t\3\2\2\u009b\u009a")
        buf.write("\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\4\3\2\2\2\u009f\u009d\3\2\2\2\u00a0")
        buf.write("\u00ab\t\4\2\2\u00a1\u00a5\5}?\2\u00a2\u00a4\5{>\2\u00a3")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\u00ab\3\2\2\2\u00a7\u00a5\3")
        buf.write("\2\2\2\u00a8\u00ab\5\177@\2\u00a9\u00ab\5\u0081A\2\u00aa")
        buf.write("\u00a0\3\2\2\2\u00aa\u00a1\3\2\2\2\u00aa\u00a8\3\2\2\2")
        buf.write("\u00aa\u00a9\3\2\2\2\u00ab\6\3\2\2\2\u00ac\u00af\5/\30")
        buf.write("\2\u00ad\u00af\5\61\31\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad")
        buf.write("\3\2\2\2\u00af\b\3\2\2\2\u00b0\u00b2\5{>\2\u00b1\u00b0")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00b7\5\u0085")
        buf.write("C\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\u00b9\5\u0083B\2\u00b9\u00c4\3\2\2\2\u00ba")
        buf.write("\u00bc\5{>\2\u00bb\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\3\2\2\2")
        buf.write("\u00bf\u00c1\5\u0085C\2\u00c0\u00c2\5\u0083B\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3")
        buf.write("\u00b1\3\2\2\2\u00c3\u00bb\3\2\2\2\u00c4\n\3\2\2\2\u00c5")
        buf.write("\u00c6\7D\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7f\2\2\u00c8")
        buf.write("\u00c9\7{\2\2\u00c9\f\3\2\2\2\u00ca\u00cb\7D\2\2\u00cb")
        buf.write("\u00cc\7t\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7c\2\2\u00ce")
        buf.write("\u00cf\7m\2\2\u00cf\16\3\2\2\2\u00d0\u00d1\7E\2\2\u00d1")
        buf.write("\u00d2\7q\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4")
        buf.write("\u00d5\7k\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7w\2\2\u00d7")
        buf.write("\u00d8\7g\2\2\u00d8\20\3\2\2\2\u00d9\u00da\7F\2\2\u00da")
        buf.write("\u00db\7q\2\2\u00db\22\3\2\2\2\u00dc\u00dd\7G\2\2\u00dd")
        buf.write("\u00de\7n\2\2\u00de\u00df\7u\2\2\u00df\u00e0\7g\2\2\u00e0")
        buf.write("\24\3\2\2\2\u00e1\u00e2\7G\2\2\u00e2\u00e3\7n\2\2\u00e3")
        buf.write("\u00e4\7u\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7K\2\2\u00e6")
        buf.write("\u00e7\7h\2\2\u00e7\26\3\2\2\2\u00e8\u00e9\7G\2\2\u00e9")
        buf.write("\u00ea\7p\2\2\u00ea\u00eb\7f\2\2\u00eb\u00ec\7D\2\2\u00ec")
        buf.write("\u00ed\7q\2\2\u00ed\u00ee\7f\2\2\u00ee\u00ef\7{\2\2\u00ef")
        buf.write("\30\3\2\2\2\u00f0\u00f1\7G\2\2\u00f1\u00f2\7p\2\2\u00f2")
        buf.write("\u00f3\7f\2\2\u00f3\u00f4\7K\2\2\u00f4\u00f5\7h\2\2\u00f5")
        buf.write("\32\3\2\2\2\u00f6\u00f7\7G\2\2\u00f7\u00f8\7p\2\2\u00f8")
        buf.write("\u00f9\7f\2\2\u00f9\u00fa\7H\2\2\u00fa\u00fb\7q\2\2\u00fb")
        buf.write("\u00fc\7t\2\2\u00fc\34\3\2\2\2\u00fd\u00fe\7G\2\2\u00fe")
        buf.write("\u00ff\7p\2\2\u00ff\u0100\7f\2\2\u0100\u0101\7Y\2\2\u0101")
        buf.write("\u0102\7j\2\2\u0102\u0103\7k\2\2\u0103\u0104\7n\2\2\u0104")
        buf.write("\u0105\7g\2\2\u0105\36\3\2\2\2\u0106\u0107\7H\2\2\u0107")
        buf.write("\u0108\7q\2\2\u0108\u0109\7t\2\2\u0109 \3\2\2\2\u010a")
        buf.write("\u010b\7H\2\2\u010b\u010c\7w\2\2\u010c\u010d\7p\2\2\u010d")
        buf.write("\u010e\7e\2\2\u010e\u010f\7v\2\2\u010f\u0110\7k\2\2\u0110")
        buf.write("\u0111\7q\2\2\u0111\u0112\7p\2\2\u0112\"\3\2\2\2\u0113")
        buf.write("\u0114\7K\2\2\u0114\u0115\7h\2\2\u0115$\3\2\2\2\u0116")
        buf.write("\u0117\7R\2\2\u0117\u0118\7c\2\2\u0118\u0119\7t\2\2\u0119")
        buf.write("\u011a\7c\2\2\u011a\u011b\7o\2\2\u011b\u011c\7g\2\2\u011c")
        buf.write("\u011d\7v\2\2\u011d\u011e\7g\2\2\u011e\u011f\7t\2\2\u011f")
        buf.write("&\3\2\2\2\u0120\u0121\7T\2\2\u0121\u0122\7g\2\2\u0122")
        buf.write("\u0123\7v\2\2\u0123\u0124\7w\2\2\u0124\u0125\7t\2\2\u0125")
        buf.write("\u0126\7p\2\2\u0126(\3\2\2\2\u0127\u0128\7V\2\2\u0128")
        buf.write("\u0129\7j\2\2\u0129\u012a\7g\2\2\u012a\u012b\7p\2\2\u012b")
        buf.write("*\3\2\2\2\u012c\u012d\7X\2\2\u012d\u012e\7c\2\2\u012e")
        buf.write("\u012f\7t\2\2\u012f,\3\2\2\2\u0130\u0131\7Y\2\2\u0131")
        buf.write("\u0132\7j\2\2\u0132\u0133\7k\2\2\u0133\u0134\7n\2\2\u0134")
        buf.write("\u0135\7g\2\2\u0135.\3\2\2\2\u0136\u0137\7V\2\2\u0137")
        buf.write("\u0138\7t\2\2\u0138\u0139\7w\2\2\u0139\u013a\7g\2\2\u013a")
        buf.write("\60\3\2\2\2\u013b\u013c\7H\2\2\u013c\u013d\7c\2\2\u013d")
        buf.write("\u013e\7n\2\2\u013e\u013f\7u\2\2\u013f\u0140\7g\2\2\u0140")
        buf.write("\62\3\2\2\2\u0141\u0142\7G\2\2\u0142\u0143\7p\2\2\u0143")
        buf.write("\u0144\7f\2\2\u0144\u0145\7F\2\2\u0145\u0146\7q\2\2\u0146")
        buf.write("\64\3\2\2\2\u0147\u0148\7-\2\2\u0148\66\3\2\2\2\u0149")
        buf.write("\u014a\7-\2\2\u014a\u014b\7\60\2\2\u014b8\3\2\2\2\u014c")
        buf.write("\u014d\7/\2\2\u014d:\3\2\2\2\u014e\u014f\7/\2\2\u014f")
        buf.write("\u0150\7\60\2\2\u0150<\3\2\2\2\u0151\u0152\7,\2\2\u0152")
        buf.write(">\3\2\2\2\u0153\u0154\7,\2\2\u0154\u0155\7\60\2\2\u0155")
        buf.write("@\3\2\2\2\u0156\u0157\7^\2\2\u0157B\3\2\2\2\u0158\u0159")
        buf.write("\7^\2\2\u0159\u015a\7\60\2\2\u015aD\3\2\2\2\u015b\u015c")
        buf.write("\7\'\2\2\u015cF\3\2\2\2\u015d\u015e\7#\2\2\u015eH\3\2")
        buf.write("\2\2\u015f\u0160\7(\2\2\u0160\u0161\7(\2\2\u0161J\3\2")
        buf.write("\2\2\u0162\u0163\7~\2\2\u0163\u0164\7~\2\2\u0164L\3\2")
        buf.write("\2\2\u0165\u0166\7#\2\2\u0166\u0167\7?\2\2\u0167N\3\2")
        buf.write("\2\2\u0168\u0169\7?\2\2\u0169\u016a\7?\2\2\u016aP\3\2")
        buf.write("\2\2\u016b\u016c\7>\2\2\u016cR\3\2\2\2\u016d\u016e\7@")
        buf.write("\2\2\u016eT\3\2\2\2\u016f\u0170\7>\2\2\u0170\u0171\7?")
        buf.write("\2\2\u0171V\3\2\2\2\u0172\u0173\7@\2\2\u0173\u0174\7?")
        buf.write("\2\2\u0174X\3\2\2\2\u0175\u0176\7?\2\2\u0176\u0177\7\61")
        buf.write("\2\2\u0177\u0178\7?\2\2\u0178Z\3\2\2\2\u0179\u017a\7>")
        buf.write("\2\2\u017a\u017b\7\60\2\2\u017b\\\3\2\2\2\u017c\u017d")
        buf.write("\7@\2\2\u017d\u017e\7\60\2\2\u017e^\3\2\2\2\u017f\u0180")
        buf.write("\7>\2\2\u0180\u0181\7?\2\2\u0181\u0182\7\60\2\2\u0182")
        buf.write("`\3\2\2\2\u0183\u0184\7@\2\2\u0184\u0185\7?\2\2\u0185")
        buf.write("\u0186\7\60\2\2\u0186b\3\2\2\2\u0187\u0188\7?\2\2\u0188")
        buf.write("d\3\2\2\2\u0189\u018a\7]\2\2\u018af\3\2\2\2\u018b\u018c")
        buf.write("\7_\2\2\u018ch\3\2\2\2\u018d\u018e\7}\2\2\u018ej\3\2\2")
        buf.write("\2\u018f\u0190\7\177\2\2\u0190l\3\2\2\2\u0191\u0192\7")
        buf.write("*\2\2\u0192n\3\2\2\2\u0193\u0194\7+\2\2\u0194p\3\2\2\2")
        buf.write("\u0195\u0196\7<\2\2\u0196r\3\2\2\2\u0197\u0198\7=\2\2")
        buf.write("\u0198t\3\2\2\2\u0199\u019a\7\60\2\2\u019av\3\2\2\2\u019b")
        buf.write("\u019c\7.\2\2\u019cx\3\2\2\2\u019d\u019e\7,\2\2\u019e")
        buf.write("\u019f\7,\2\2\u019f\u01a5\3\2\2\2\u01a0\u01a4\n\5\2\2")
        buf.write("\u01a1\u01a2\7,\2\2\u01a2\u01a4\n\5\2\2\u01a3\u01a0\3")
        buf.write("\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a8\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a8\u01a9\7,\2\2\u01a9\u01aa\7,\2\2\u01aa")
        buf.write("\u01ab\3\2\2\2\u01ab\u01ac\b=\2\2\u01acz\3\2\2\2\u01ad")
        buf.write("\u01ae\t\6\2\2\u01ae|\3\2\2\2\u01af\u01b0\t\7\2\2\u01b0")
        buf.write("~\3\2\2\2\u01b1\u01b3\7\62\2\2\u01b2\u01b4\t\b\2\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b9\t")
        buf.write("\t\2\2\u01b8\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bf\3\2\2\2\u01bc")
        buf.write("\u01be\t\n\2\2\u01bd\u01bc\3\2\2\2\u01be\u01c1\3\2\2\2")
        buf.write("\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u0080\3")
        buf.write("\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c4\7\62\2\2\u01c3")
        buf.write("\u01c5\t\13\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2\2")
        buf.write("\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c9")
        buf.write("\3\2\2\2\u01c8\u01ca\t\f\2\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01cc\u01d0\3\2\2\2\u01cd\u01cf\t\r\2\2\u01ce\u01cd\3")
        buf.write("\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1")
        buf.write("\3\2\2\2\u01d1\u0082\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3")
        buf.write("\u01d5\t\16\2\2\u01d4\u01d6\t\17\2\2\u01d5\u01d4\3\2\2")
        buf.write("\2\u01d5\u01d6\3\2\2\2\u01d6\u01d8\3\2\2\2\u01d7\u01d9")
        buf.write("\5{>\2\u01d8\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u0084\3\2\2\2\u01dc")
        buf.write("\u01e0\7\60\2\2\u01dd\u01df\5{>\2\u01de\u01dd\3\2\2\2")
        buf.write("\u01df\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3")
        buf.write("\2\2\2\u01e1\u0086\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e5")
        buf.write("\t\20\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6")
        buf.write("\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e8\u01e9\bD\2\2\u01e9\u0088\3\2\2\2\u01ea\u01ef\n")
        buf.write("\21\2\2\u01eb\u01ec\7)\2\2\u01ec\u01ef\7$\2\2\u01ed\u01ef")
        buf.write("\5\u008bF\2\u01ee\u01ea\3\2\2\2\u01ee\u01eb\3\2\2\2\u01ee")
        buf.write("\u01ed\3\2\2\2\u01ef\u008a\3\2\2\2\u01f0\u01f1\7^\2\2")
        buf.write("\u01f1\u01f2\t\22\2\2\u01f2\u008c\3\2\2\2\u01f3\u01f4")
        buf.write("\7^\2\2\u01f4\u01f8\n\22\2\2\u01f5\u01f6\7)\2\2\u01f6")
        buf.write("\u01f8\n\23\2\2\u01f7\u01f3\3\2\2\2\u01f7\u01f5\3\2\2")
        buf.write("\2\u01f8\u008e\3\2\2\2\u01f9\u01fd\7$\2\2\u01fa\u01fc")
        buf.write("\5\u0089E\2\u01fb\u01fa\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd")
        buf.write("\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0200\3\2\2\2")
        buf.write("\u01ff\u01fd\3\2\2\2\u0200\u0201\7$\2\2\u0201\u0202\b")
        buf.write("H\3\2\u0202\u0090\3\2\2\2\u0203\u0207\7$\2\2\u0204\u0206")
        buf.write("\5\u0089E\2\u0205\u0204\3\2\2\2\u0206\u0209\3\2\2\2\u0207")
        buf.write("\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u020a\3\2\2\2")
        buf.write("\u0209\u0207\3\2\2\2\u020a\u020b\5\u008dG\2\u020b\u020c")
        buf.write("\bI\4\2\u020c\u0092\3\2\2\2\u020d\u0211\7$\2\2\u020e\u0210")
        buf.write("\5\u0089E\2\u020f\u020e\3\2\2\2\u0210\u0213\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0215\3\2\2\2")
        buf.write("\u0213\u0211\3\2\2\2\u0214\u0216\t\24\2\2\u0215\u0214")
        buf.write("\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0218\bJ\5\2\u0218")
        buf.write("\u0094\3\2\2\2\u0219\u021a\7,\2\2\u021a\u021b\7,\2\2\u021b")
        buf.write("\u0220\3\2\2\2\u021c\u021d\n\5\2\2\u021d\u021f\n\5\2\2")
        buf.write("\u021e\u021c\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u021e\3")
        buf.write("\2\2\2\u0220\u0221\3\2\2\2\u0221\u0096\3\2\2\2\u0222\u0220")
        buf.write("\3\2\2\2\u0223\u0224\13\2\2\2\u0224\u0225\bL\6\2\u0225")
        buf.write("\u0098\3\2\2\2\37\2\u009d\u00a5\u00aa\u00ae\u00b3\u00b6")
        buf.write("\u00bd\u00c1\u00c3\u01a3\u01a5\u01b5\u01ba\u01bf\u01c6")
        buf.write("\u01cb\u01d0\u01d5\u01da\u01e0\u01e6\u01ee\u01f7\u01fd")
        buf.write("\u0207\u0211\u0215\u0220\7\b\2\2\3H\2\3I\3\3J\4\3L\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    INT_LIT = 2
    BOOLEAN_LIT = 3
    FLOAT_LIT = 4
    BODY = 5
    BREAK = 6
    CONTINUE = 7
    DO = 8
    ELSE = 9
    ELSEIF = 10
    ENDBODY = 11
    ENDIF = 12
    ENDFOR = 13
    ENDWHILE = 14
    FOR = 15
    FUNCTION = 16
    IF = 17
    PARAMETER = 18
    RETURN = 19
    THEN = 20
    VAR = 21
    WHILE = 22
    TRUE = 23
    FALSE = 24
    ENDDO = 25
    ADDINT = 26
    ADDFLOAT = 27
    SUBINT = 28
    SUBFLOAT = 29
    MULINT = 30
    MULFLOAT = 31
    DIVINT = 32
    DIVFLOAT = 33
    MODINT = 34
    NOT = 35
    AND = 36
    OR = 37
    NOT_EQUALINT = 38
    EQUALINT = 39
    LTHANINT = 40
    GTHANINT = 41
    LEQUALINT = 42
    GEQUALINT = 43
    NOT_EQUALFLOAT = 44
    LTHANFLOAT = 45
    GTHANFLOAT = 46
    LEQUALFLOAT = 47
    GEQUALFLOAT = 48
    ASSIGN = 49
    LSB = 50
    RSB = 51
    LB = 52
    RB = 53
    LP = 54
    RP = 55
    COLON = 56
    SEMI = 57
    DOT = 58
    COMMA = 59
    COMMENT = 60
    INT = 61
    INT_WITHOUT_0 = 62
    WS = 63
    STRING_LIT = 64
    ILLEGAL_ESCAPE = 65
    UNCLOSE_STRING = 66
    UNTERMINATED_COMMENT = 67
    ERROR_CHAR = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
            "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", 
            "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", 
            "'>.'", "'<=.'", "'>=.'", "'='", "'['", "']'", "'{'", "'}'", 
            "'('", "')'", "':'", "';'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT_LIT", "BOOLEAN_LIT", "FLOAT_LIT", "BODY", "BREAK", 
            "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
            "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", 
            "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "ADDINT", 
            "ADDFLOAT", "SUBINT", "SUBFLOAT", "MULINT", "MULFLOAT", "DIVINT", 
            "DIVFLOAT", "MODINT", "NOT", "AND", "OR", "NOT_EQUALINT", "EQUALINT", 
            "LTHANINT", "GTHANINT", "LEQUALINT", "GEQUALINT", "NOT_EQUALFLOAT", 
            "LTHANFLOAT", "GTHANFLOAT", "LEQUALFLOAT", "GEQUALFLOAT", "ASSIGN", 
            "LSB", "RSB", "LB", "RB", "LP", "RP", "COLON", "SEMI", "DOT", 
            "COMMA", "COMMENT", "INT", "INT_WITHOUT_0", "WS", "STRING_LIT", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "ID", "INT_LIT", "BOOLEAN_LIT", "FLOAT_LIT", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                  "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                  "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
                  "ADDINT", "ADDFLOAT", "SUBINT", "SUBFLOAT", "MULINT", 
                  "MULFLOAT", "DIVINT", "DIVFLOAT", "MODINT", "NOT", "AND", 
                  "OR", "NOT_EQUALINT", "EQUALINT", "LTHANINT", "GTHANINT", 
                  "LEQUALINT", "GEQUALINT", "NOT_EQUALFLOAT", "LTHANFLOAT", 
                  "GTHANFLOAT", "LEQUALFLOAT", "GEQUALFLOAT", "ASSIGN", 
                  "LSB", "RSB", "LB", "RB", "LP", "RP", "COLON", "SEMI", 
                  "DOT", "COMMA", "COMMENT", "INT", "INT_WITHOUT_0", "HEX", 
                  "OCT", "EXP", "DEC", "WS", "STR_CHAR", "ESCAPE_SEQUENCES", 
                  "ESCAPE_ILLEGAL", "STRING_LIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[70] = self.STRING_LIT_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[74] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    y = str(self.text)
                    
                    self.text = y[1:-1]
                  

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    y = str(self.text)
                    
                    raise IllegalEscape(y[1:]) 

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    y = str(self.text)
                    
                    if y[-1] == '\n': 
                            raise UncloseString(y[1:-1])
                    else: 
                            raise UncloseString(y[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             
                    raise ErrorToken(self.text)

     


