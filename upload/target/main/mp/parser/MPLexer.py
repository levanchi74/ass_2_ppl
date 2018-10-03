# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u028c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\3\2\3\2\3\2\3\2\7\2\u00c4\n\2\f\2\16\2\u00c7")
        buf.write("\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\7\3\u00d0\n\3\f\3\16")
        buf.write("\3\u00d3\13\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00dd")
        buf.write("\n\4\f\4\16\4\u00e0\13\4\3\4\3\4\3\5\3\5\5\5\u00e6\n\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3A\3")
        buf.write("B\3B\3B\3C\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3")
        buf.write("J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3O\3P\3P\3Q\6Q\u01eb")
        buf.write("\nQ\rQ\16Q\u01ec\3R\6R\u01f0\nR\rR\16R\u01f1\3R\3R\7R")
        buf.write("\u01f6\nR\fR\16R\u01f9\13R\3S\7S\u01fc\nS\fS\16S\u01ff")
        buf.write("\13S\3S\3S\6S\u0203\nS\rS\16S\u0204\3T\6T\u0208\nT\rT")
        buf.write("\16T\u0209\3T\3T\5T\u020e\nT\3T\6T\u0211\nT\rT\16T\u0212")
        buf.write("\3U\7U\u0216\nU\fU\16U\u0219\13U\3U\3U\6U\u021d\nU\rU")
        buf.write("\16U\u021e\3U\3U\5U\u0223\nU\3U\6U\u0226\nU\rU\16U\u0227")
        buf.write("\3V\3V\3V\3V\5V\u022e\nV\3W\6W\u0231\nW\rW\16W\u0232\3")
        buf.write("W\3W\3X\3X\7X\u0239\nX\fX\16X\u023c\13X\3Y\3Y\3Y\7Y\u0241")
        buf.write("\nY\fY\16Y\u0244\13Y\3Y\3Y\3Y\3Z\3Z\3Z\7Z\u024c\nZ\fZ")
        buf.write("\16Z\u024f\13Z\3Z\3Z\3[\7[\u0254\n[\f[\16[\u0257\13[\3")
        buf.write("[\3[\3[\7[\u025c\n[\f[\16[\u025f\13[\3[\3[\3\\\3\\\3\\")
        buf.write("\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3")
        buf.write("\\\5\\\u0274\n\\\3]\3]\3]\3^\3^\7^\u027b\n^\f^\16^\u027e")
        buf.write("\13^\3^\3^\7^\u0282\n^\f^\16^\u0285\13^\3^\3^\3^\3_\3")
        buf.write("_\3_\b\u00c5\u00d1\u0255\u025d\u027c\u0283\2`\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G\2I\2K\2M\2O\2Q\2S")
        buf.write("\2U\2W\2Y\2[\2]\2_\2a\2c\2e\2g\2i\2k\2m\2o\2q\2s\2u\2")
        buf.write("w\2y\2{%}&\177\'\u0081(\u0083)\u0085*\u0087+\u0089,\u008b")
        buf.write("-\u008d.\u008f/\u0091\60\u0093\61\u0095\62\u0097\63\u0099")
        buf.write("\64\u009b\65\u009d\66\u009f\67\u00a18\u00a3\2\u00a5\2")
        buf.write("\u00a7\2\u00a9\2\u00ab9\u00ad:\u00af;\u00b1<\u00b3=\u00b5")
        buf.write(">\u00b7?\u00b9\2\u00bb@\u00bdA\3\2#\4\2\f\f\17\17\4\2")
        buf.write("CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4")
        buf.write("\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPp")
        buf.write("p\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2")
        buf.write("WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\3\2\62")
        buf.write(";\5\2\13\f\16\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\6\2\f\f")
        buf.write("\17\17$$^^\n\2$$))^^ddhhppttvv\2\u0290\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00bb")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\3\u00bf\3\2\2\2\5\u00cd\3\2\2")
        buf.write("\2\7\u00d8\3\2\2\2\t\u00e5\3\2\2\2\13\u00e7\3\2\2\2\r")
        buf.write("\u00ed\3\2\2\2\17\u00f6\3\2\2\2\21\u00fa\3\2\2\2\23\u00fd")
        buf.write("\3\2\2\2\25\u0104\3\2\2\2\27\u0107\3\2\2\2\31\u010a\3")
        buf.write("\2\2\2\33\u010f\3\2\2\2\35\u0114\3\2\2\2\37\u011b\3\2")
        buf.write("\2\2!\u0121\3\2\2\2#\u0126\3\2\2\2%\u012c\3\2\2\2\'\u0130")
        buf.write("\3\2\2\2)\u0139\3\2\2\2+\u0143\3\2\2\2-\u0147\3\2\2\2")
        buf.write("/\u014c\3\2\2\2\61\u0152\3\2\2\2\63\u0158\3\2\2\2\65\u015b")
        buf.write("\3\2\2\2\67\u0160\3\2\2\29\u0168\3\2\2\2;\u0170\3\2\2")
        buf.write("\2=\u0177\3\2\2\2?\u017b\3\2\2\2A\u017f\3\2\2\2C\u0182")
        buf.write("\3\2\2\2E\u0186\3\2\2\2G\u018a\3\2\2\2I\u018c\3\2\2\2")
        buf.write("K\u018e\3\2\2\2M\u0190\3\2\2\2O\u0192\3\2\2\2Q\u0194\3")
        buf.write("\2\2\2S\u0196\3\2\2\2U\u0198\3\2\2\2W\u019a\3\2\2\2Y\u019c")
        buf.write("\3\2\2\2[\u019e\3\2\2\2]\u01a0\3\2\2\2_\u01a2\3\2\2\2")
        buf.write("a\u01a4\3\2\2\2c\u01a6\3\2\2\2e\u01a8\3\2\2\2g\u01aa\3")
        buf.write("\2\2\2i\u01ac\3\2\2\2k\u01ae\3\2\2\2m\u01b0\3\2\2\2o\u01b2")
        buf.write("\3\2\2\2q\u01b4\3\2\2\2s\u01b6\3\2\2\2u\u01b8\3\2\2\2")
        buf.write("w\u01ba\3\2\2\2y\u01bc\3\2\2\2{\u01be\3\2\2\2}\u01c1\3")
        buf.write("\2\2\2\177\u01c3\3\2\2\2\u0081\u01c5\3\2\2\2\u0083\u01c8")
        buf.write("\3\2\2\2\u0085\u01cb\3\2\2\2\u0087\u01ce\3\2\2\2\u0089")
        buf.write("\u01d0\3\2\2\2\u008b\u01d2\3\2\2\2\u008d\u01d4\3\2\2\2")
        buf.write("\u008f\u01d6\3\2\2\2\u0091\u01d8\3\2\2\2\u0093\u01da\3")
        buf.write("\2\2\2\u0095\u01dc\3\2\2\2\u0097\u01de\3\2\2\2\u0099\u01e0")
        buf.write("\3\2\2\2\u009b\u01e2\3\2\2\2\u009d\u01e4\3\2\2\2\u009f")
        buf.write("\u01e7\3\2\2\2\u00a1\u01ea\3\2\2\2\u00a3\u01ef\3\2\2\2")
        buf.write("\u00a5\u01fd\3\2\2\2\u00a7\u0207\3\2\2\2\u00a9\u0217\3")
        buf.write("\2\2\2\u00ab\u022d\3\2\2\2\u00ad\u0230\3\2\2\2\u00af\u0236")
        buf.write("\3\2\2\2\u00b1\u023d\3\2\2\2\u00b3\u0248\3\2\2\2\u00b5")
        buf.write("\u0255\3\2\2\2\u00b7\u0262\3\2\2\2\u00b9\u0275\3\2\2\2")
        buf.write("\u00bb\u0278\3\2\2\2\u00bd\u0289\3\2\2\2\u00bf\u00c0\7")
        buf.write("*\2\2\u00c0\u00c1\7,\2\2\u00c1\u00c5\3\2\2\2\u00c2\u00c4")
        buf.write("\13\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c8\3\2\2\2")
        buf.write("\u00c7\u00c5\3\2\2\2\u00c8\u00c9\7,\2\2\u00c9\u00ca\7")
        buf.write("+\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\b\2\2\2\u00cc\4")
        buf.write("\3\2\2\2\u00cd\u00d1\7}\2\2\u00ce\u00d0\13\2\2\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d1\u00cf\3\2\2\2\u00d2\u00d4\3\2\2\2\u00d3\u00d1\3")
        buf.write("\2\2\2\u00d4\u00d5\7\177\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write("\u00d7\b\3\2\2\u00d7\6\3\2\2\2\u00d8\u00d9\7\61\2\2\u00d9")
        buf.write("\u00da\7\61\2\2\u00da\u00de\3\2\2\2\u00db\u00dd\n\2\2")
        buf.write("\2\u00dc\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e1\u00e2\b\4\2\2\u00e2\b\3\2\2\2\u00e3")
        buf.write("\u00e6\5-\27\2\u00e4\u00e6\5/\30\2\u00e5\u00e3\3\2\2\2")
        buf.write("\u00e5\u00e4\3\2\2\2\u00e6\n\3\2\2\2\u00e7\u00e8\5I%\2")
        buf.write("\u00e8\u00e9\5i\65\2\u00e9\u00ea\5O(\2\u00ea\u00eb\5G")
        buf.write("$\2\u00eb\u00ec\5[.\2\u00ec\f\3\2\2\2\u00ed\u00ee\5K&")
        buf.write("\2\u00ee\u00ef\5c\62\2\u00ef\u00f0\5a\61\2\u00f0\u00f1")
        buf.write("\5m\67\2\u00f1\u00f2\5W,\2\u00f2\u00f3\5a\61\2\u00f3\u00f4")
        buf.write("\5o8\2\u00f4\u00f5\5O(\2\u00f5\16\3\2\2\2\u00f6\u00f7")
        buf.write("\5Q)\2\u00f7\u00f8\5c\62\2\u00f8\u00f9\5i\65\2\u00f9\20")
        buf.write("\3\2\2\2\u00fa\u00fb\5m\67\2\u00fb\u00fc\5c\62\2\u00fc")
        buf.write("\22\3\2\2\2\u00fd\u00fe\5M\'\2\u00fe\u00ff\5c\62\2\u00ff")
        buf.write("\u0100\5s:\2\u0100\u0101\5a\61\2\u0101\u0102\5m\67\2\u0102")
        buf.write("\u0103\5c\62\2\u0103\24\3\2\2\2\u0104\u0105\5M\'\2\u0105")
        buf.write("\u0106\5c\62\2\u0106\26\3\2\2\2\u0107\u0108\5W,\2\u0108")
        buf.write("\u0109\5Q)\2\u0109\30\3\2\2\2\u010a\u010b\5m\67\2\u010b")
        buf.write("\u010c\5U+\2\u010c\u010d\5O(\2\u010d\u010e\5a\61\2\u010e")
        buf.write("\32\3\2\2\2\u010f\u0110\5O(\2\u0110\u0111\5]/\2\u0111")
        buf.write("\u0112\5k\66\2\u0112\u0113\5O(\2\u0113\34\3\2\2\2\u0114")
        buf.write("\u0115\5i\65\2\u0115\u0116\5O(\2\u0116\u0117\5m\67\2\u0117")
        buf.write("\u0118\5o8\2\u0118\u0119\5i\65\2\u0119\u011a\5a\61\2\u011a")
        buf.write("\36\3\2\2\2\u011b\u011c\5s:\2\u011c\u011d\5U+\2\u011d")
        buf.write("\u011e\5W,\2\u011e\u011f\5]/\2\u011f\u0120\5O(\2\u0120")
        buf.write(" \3\2\2\2\u0121\u0122\5s:\2\u0122\u0123\5W,\2\u0123\u0124")
        buf.write("\5m\67\2\u0124\u0125\5U+\2\u0125\"\3\2\2\2\u0126\u0127")
        buf.write("\5I%\2\u0127\u0128\5O(\2\u0128\u0129\5S*\2\u0129\u012a")
        buf.write("\5W,\2\u012a\u012b\5a\61\2\u012b$\3\2\2\2\u012c\u012d")
        buf.write("\5O(\2\u012d\u012e\5a\61\2\u012e\u012f\5M\'\2\u012f&\3")
        buf.write("\2\2\2\u0130\u0131\5Q)\2\u0131\u0132\5o8\2\u0132\u0133")
        buf.write("\5a\61\2\u0133\u0134\5K&\2\u0134\u0135\5m\67\2\u0135\u0136")
        buf.write("\5W,\2\u0136\u0137\5c\62\2\u0137\u0138\5a\61\2\u0138(")
        buf.write("\3\2\2\2\u0139\u013a\5e\63\2\u013a\u013b\5i\65\2\u013b")
        buf.write("\u013c\5c\62\2\u013c\u013d\5K&\2\u013d\u013e\5O(\2\u013e")
        buf.write("\u013f\5M\'\2\u013f\u0140\5o8\2\u0140\u0141\5i\65\2\u0141")
        buf.write("\u0142\5O(\2\u0142*\3\2\2\2\u0143\u0144\5q9\2\u0144\u0145")
        buf.write("\5G$\2\u0145\u0146\5i\65\2\u0146,\3\2\2\2\u0147\u0148")
        buf.write("\5m\67\2\u0148\u0149\5i\65\2\u0149\u014a\5o8\2\u014a\u014b")
        buf.write("\5O(\2\u014b.\3\2\2\2\u014c\u014d\5Q)\2\u014d\u014e\5")
        buf.write("G$\2\u014e\u014f\5]/\2\u014f\u0150\5k\66\2\u0150\u0151")
        buf.write("\5O(\2\u0151\60\3\2\2\2\u0152\u0153\5G$\2\u0153\u0154")
        buf.write("\5i\65\2\u0154\u0155\5i\65\2\u0155\u0156\5G$\2\u0156\u0157")
        buf.write("\5w<\2\u0157\62\3\2\2\2\u0158\u0159\5c\62\2\u0159\u015a")
        buf.write("\5Q)\2\u015a\64\3\2\2\2\u015b\u015c\5i\65\2\u015c\u015d")
        buf.write("\5O(\2\u015d\u015e\5G$\2\u015e\u015f\5]/\2\u015f\66\3")
        buf.write("\2\2\2\u0160\u0161\5I%\2\u0161\u0162\5c\62\2\u0162\u0163")
        buf.write("\5c\62\2\u0163\u0164\5]/\2\u0164\u0165\5O(\2\u0165\u0166")
        buf.write("\5G$\2\u0166\u0167\5a\61\2\u01678\3\2\2\2\u0168\u0169")
        buf.write("\5W,\2\u0169\u016a\5a\61\2\u016a\u016b\5m\67\2\u016b\u016c")
        buf.write("\5O(\2\u016c\u016d\5S*\2\u016d\u016e\5O(\2\u016e\u016f")
        buf.write("\5i\65\2\u016f:\3\2\2\2\u0170\u0171\5k\66\2\u0171\u0172")
        buf.write("\5m\67\2\u0172\u0173\5i\65\2\u0173\u0174\5W,\2\u0174\u0175")
        buf.write("\5a\61\2\u0175\u0176\5S*\2\u0176<\3\2\2\2\u0177\u0178")
        buf.write("\5a\61\2\u0178\u0179\5c\62\2\u0179\u017a\5m\67\2\u017a")
        buf.write(">\3\2\2\2\u017b\u017c\5G$\2\u017c\u017d\5a\61\2\u017d")
        buf.write("\u017e\5M\'\2\u017e@\3\2\2\2\u017f\u0180\5c\62\2\u0180")
        buf.write("\u0181\5i\65\2\u0181B\3\2\2\2\u0182\u0183\5M\'\2\u0183")
        buf.write("\u0184\5W,\2\u0184\u0185\5q9\2\u0185D\3\2\2\2\u0186\u0187")
        buf.write("\5_\60\2\u0187\u0188\5c\62\2\u0188\u0189\5M\'\2\u0189")
        buf.write("F\3\2\2\2\u018a\u018b\t\3\2\2\u018bH\3\2\2\2\u018c\u018d")
        buf.write("\t\4\2\2\u018dJ\3\2\2\2\u018e\u018f\t\5\2\2\u018fL\3\2")
        buf.write("\2\2\u0190\u0191\t\6\2\2\u0191N\3\2\2\2\u0192\u0193\t")
        buf.write("\7\2\2\u0193P\3\2\2\2\u0194\u0195\t\b\2\2\u0195R\3\2\2")
        buf.write("\2\u0196\u0197\t\t\2\2\u0197T\3\2\2\2\u0198\u0199\t\n")
        buf.write("\2\2\u0199V\3\2\2\2\u019a\u019b\t\13\2\2\u019bX\3\2\2")
        buf.write("\2\u019c\u019d\t\f\2\2\u019dZ\3\2\2\2\u019e\u019f\t\r")
        buf.write("\2\2\u019f\\\3\2\2\2\u01a0\u01a1\t\16\2\2\u01a1^\3\2\2")
        buf.write("\2\u01a2\u01a3\t\17\2\2\u01a3`\3\2\2\2\u01a4\u01a5\t\20")
        buf.write("\2\2\u01a5b\3\2\2\2\u01a6\u01a7\t\21\2\2\u01a7d\3\2\2")
        buf.write("\2\u01a8\u01a9\t\22\2\2\u01a9f\3\2\2\2\u01aa\u01ab\t\23")
        buf.write("\2\2\u01abh\3\2\2\2\u01ac\u01ad\t\24\2\2\u01adj\3\2\2")
        buf.write("\2\u01ae\u01af\t\25\2\2\u01afl\3\2\2\2\u01b0\u01b1\t\26")
        buf.write("\2\2\u01b1n\3\2\2\2\u01b2\u01b3\t\27\2\2\u01b3p\3\2\2")
        buf.write("\2\u01b4\u01b5\t\30\2\2\u01b5r\3\2\2\2\u01b6\u01b7\t\31")
        buf.write("\2\2\u01b7t\3\2\2\2\u01b8\u01b9\t\32\2\2\u01b9v\3\2\2")
        buf.write("\2\u01ba\u01bb\t\33\2\2\u01bbx\3\2\2\2\u01bc\u01bd\t\34")
        buf.write("\2\2\u01bdz\3\2\2\2\u01be\u01bf\7<\2\2\u01bf\u01c0\7?")
        buf.write("\2\2\u01c0|\3\2\2\2\u01c1\u01c2\7-\2\2\u01c2~\3\2\2\2")
        buf.write("\u01c3\u01c4\7,\2\2\u01c4\u0080\3\2\2\2\u01c5\u01c6\7")
        buf.write(">\2\2\u01c6\u01c7\7@\2\2\u01c7\u0082\3\2\2\2\u01c8\u01c9")
        buf.write("\7>\2\2\u01c9\u01ca\7?\2\2\u01ca\u0084\3\2\2\2\u01cb\u01cc")
        buf.write("\7@\2\2\u01cc\u01cd\7?\2\2\u01cd\u0086\3\2\2\2\u01ce\u01cf")
        buf.write("\7/\2\2\u01cf\u0088\3\2\2\2\u01d0\u01d1\7\61\2\2\u01d1")
        buf.write("\u008a\3\2\2\2\u01d2\u01d3\7?\2\2\u01d3\u008c\3\2\2\2")
        buf.write("\u01d4\u01d5\7>\2\2\u01d5\u008e\3\2\2\2\u01d6\u01d7\7")
        buf.write("@\2\2\u01d7\u0090\3\2\2\2\u01d8\u01d9\7]\2\2\u01d9\u0092")
        buf.write("\3\2\2\2\u01da\u01db\7_\2\2\u01db\u0094\3\2\2\2\u01dc")
        buf.write("\u01dd\7<\2\2\u01dd\u0096\3\2\2\2\u01de\u01df\7*\2\2\u01df")
        buf.write("\u0098\3\2\2\2\u01e0\u01e1\7+\2\2\u01e1\u009a\3\2\2\2")
        buf.write("\u01e2\u01e3\7=\2\2\u01e3\u009c\3\2\2\2\u01e4\u01e5\7")
        buf.write("\60\2\2\u01e5\u01e6\7\60\2\2\u01e6\u009e\3\2\2\2\u01e7")
        buf.write("\u01e8\7.\2\2\u01e8\u00a0\3\2\2\2\u01e9\u01eb\t\35\2\2")
        buf.write("\u01ea\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ea\3")
        buf.write("\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u00a2\3\2\2\2\u01ee\u01f0")
        buf.write("\t\35\2\2\u01ef\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1")
        buf.write("\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\3\2\2\2")
        buf.write("\u01f3\u01f7\7\60\2\2\u01f4\u01f6\t\35\2\2\u01f5\u01f4")
        buf.write("\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7")
        buf.write("\u01f8\3\2\2\2\u01f8\u00a4\3\2\2\2\u01f9\u01f7\3\2\2\2")
        buf.write("\u01fa\u01fc\t\35\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01ff")
        buf.write("\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe")
        buf.write("\u0200\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0202\7\60\2")
        buf.write("\2\u0201\u0203\t\35\2\2\u0202\u0201\3\2\2\2\u0203\u0204")
        buf.write("\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205")
        buf.write("\u00a6\3\2\2\2\u0206\u0208\t\35\2\2\u0207\u0206\3\2\2")
        buf.write("\2\u0208\u0209\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020d\t\7\2\2\u020c")
        buf.write("\u020e\7/\2\2\u020d\u020c\3\2\2\2\u020d\u020e\3\2\2\2")
        buf.write("\u020e\u0210\3\2\2\2\u020f\u0211\t\35\2\2\u0210\u020f")
        buf.write("\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0210\3\2\2\2\u0212")
        buf.write("\u0213\3\2\2\2\u0213\u00a8\3\2\2\2\u0214\u0216\t\35\2")
        buf.write("\2\u0215\u0214\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215")
        buf.write("\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u021a\3\2\2\2\u0219")
        buf.write("\u0217\3\2\2\2\u021a\u021c\7\60\2\2\u021b\u021d\t\35\2")
        buf.write("\2\u021c\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u021c")
        buf.write("\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0220\3\2\2\2\u0220")
        buf.write("\u0222\t\7\2\2\u0221\u0223\7/\2\2\u0222\u0221\3\2\2\2")
        buf.write("\u0222\u0223\3\2\2\2\u0223\u0225\3\2\2\2\u0224\u0226\t")
        buf.write("\35\2\2\u0225\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227")
        buf.write("\u0225\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u00aa\3\2\2\2")
        buf.write("\u0229\u022e\5\u00a3R\2\u022a\u022e\5\u00a5S\2\u022b\u022e")
        buf.write("\5\u00a7T\2\u022c\u022e\5\u00a9U\2\u022d\u0229\3\2\2\2")
        buf.write("\u022d\u022a\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022c\3")
        buf.write("\2\2\2\u022e\u00ac\3\2\2\2\u022f\u0231\t\36\2\2\u0230")
        buf.write("\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0230\3\2\2\2")
        buf.write("\u0232\u0233\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235\b")
        buf.write("W\2\2\u0235\u00ae\3\2\2\2\u0236\u023a\t\37\2\2\u0237\u0239")
        buf.write("\t \2\2\u0238\u0237\3\2\2\2\u0239\u023c\3\2\2\2\u023a")
        buf.write("\u0238\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u00b0\3\2\2\2")
        buf.write("\u023c\u023a\3\2\2\2\u023d\u0242\7$\2\2\u023e\u0241\5")
        buf.write("\u00b7\\\2\u023f\u0241\n!\2\2\u0240\u023e\3\2\2\2\u0240")
        buf.write("\u023f\3\2\2\2\u0241\u0244\3\2\2\2\u0242\u0240\3\2\2\2")
        buf.write("\u0242\u0243\3\2\2\2\u0243\u0245\3\2\2\2\u0244\u0242\3")
        buf.write("\2\2\2\u0245\u0246\7$\2\2\u0246\u0247\bY\3\2\u0247\u00b2")
        buf.write("\3\2\2\2\u0248\u024d\7$\2\2\u0249\u024c\5\u00b7\\\2\u024a")
        buf.write("\u024c\n!\2\2\u024b\u0249\3\2\2\2\u024b\u024a\3\2\2\2")
        buf.write("\u024c\u024f\3\2\2\2\u024d\u024b\3\2\2\2\u024d\u024e\3")
        buf.write("\2\2\2\u024e\u0250\3\2\2\2\u024f\u024d\3\2\2\2\u0250\u0251")
        buf.write("\bZ\4\2\u0251\u00b4\3\2\2\2\u0252\u0254\13\2\2\2\u0253")
        buf.write("\u0252\3\2\2\2\u0254\u0257\3\2\2\2\u0255\u0256\3\2\2\2")
        buf.write("\u0255\u0253\3\2\2\2\u0256\u0258\3\2\2\2\u0257\u0255\3")
        buf.write("\2\2\2\u0258\u0259\7^\2\2\u0259\u025d\t\"\2\2\u025a\u025c")
        buf.write("\13\2\2\2\u025b\u025a\3\2\2\2\u025c\u025f\3\2\2\2\u025d")
        buf.write("\u025e\3\2\2\2\u025d\u025b\3\2\2\2\u025e\u0260\3\2\2\2")
        buf.write("\u025f\u025d\3\2\2\2\u0260\u0261\b[\5\2\u0261\u00b6\3")
        buf.write("\2\2\2\u0262\u0273\7^\2\2\u0263\u0264\7d\2\2\u0264\u0274")
        buf.write("\b\\\6\2\u0265\u0266\7h\2\2\u0266\u0274\b\\\7\2\u0267")
        buf.write("\u0268\7t\2\2\u0268\u0274\b\\\b\2\u0269\u026a\7p\2\2\u026a")
        buf.write("\u0274\b\\\t\2\u026b\u026c\7v\2\2\u026c\u0274\b\\\n\2")
        buf.write("\u026d\u026e\7)\2\2\u026e\u0274\b\\\13\2\u026f\u0270\7")
        buf.write("$\2\2\u0270\u0274\b\\\f\2\u0271\u0272\7^\2\2\u0272\u0274")
        buf.write("\b\\\r\2\u0273\u0263\3\2\2\2\u0273\u0265\3\2\2\2\u0273")
        buf.write("\u0267\3\2\2\2\u0273\u0269\3\2\2\2\u0273\u026b\3\2\2\2")
        buf.write("\u0273\u026d\3\2\2\2\u0273\u026f\3\2\2\2\u0273\u0271\3")
        buf.write("\2\2\2\u0274\u00b8\3\2\2\2\u0275\u0276\7^\2\2\u0276\u0277")
        buf.write("\n\"\2\2\u0277\u00ba\3\2\2\2\u0278\u027c\7$\2\2\u0279")
        buf.write("\u027b\13\2\2\2\u027a\u0279\3\2\2\2\u027b\u027e\3\2\2")
        buf.write("\2\u027c\u027d\3\2\2\2\u027c\u027a\3\2\2\2\u027d\u027f")
        buf.write("\3\2\2\2\u027e\u027c\3\2\2\2\u027f\u0283\5\u00b9]\2\u0280")
        buf.write("\u0282\13\2\2\2\u0281\u0280\3\2\2\2\u0282\u0285\3\2\2")
        buf.write("\2\u0283\u0284\3\2\2\2\u0283\u0281\3\2\2\2\u0284\u0286")
        buf.write("\3\2\2\2\u0285\u0283\3\2\2\2\u0286\u0287\7$\2\2\u0287")
        buf.write("\u0288\b^\16\2\u0288\u00bc\3\2\2\2\u0289\u028a\13\2\2")
        buf.write("\2\u028a\u028b\b_\17\2\u028b\u00be\3\2\2\2\37\2\u00c5")
        buf.write("\u00d1\u00de\u00e5\u01ec\u01f1\u01f7\u01fd\u0204\u0209")
        buf.write("\u020d\u0212\u0217\u021e\u0222\u0227\u022d\u0232\u023a")
        buf.write("\u0240\u0242\u024b\u024d\u0255\u025d\u0273\u027c\u0283")
        buf.write("\20\b\2\2\3Y\2\3Z\3\3[\4\3\\\5\3\\\6\3\\\7\3\\\b\3\\\t")
        buf.write("\3\\\n\3\\\13\3\\\f\3^\r\3_\16")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRADI_CMT = 1
    BLOCK_CMT = 2
    LINE_CMT = 3
    BOOLEANLIT = 4
    BREAK = 5
    CONTINUE = 6
    FOR = 7
    TO = 8
    DOWNTO = 9
    DO = 10
    IF = 11
    THEN = 12
    ELSE = 13
    RETURN = 14
    WHILE = 15
    WITH = 16
    BEGIN = 17
    END = 18
    FUNCTION = 19
    PROCEDURE = 20
    VAR = 21
    TRUE = 22
    FALSE = 23
    ARRAY = 24
    OF = 25
    REALTYPE = 26
    BOOLEANTYPE = 27
    INTTYPE = 28
    STRINGTYPE = 29
    NOT = 30
    AND = 31
    OR = 32
    DIV = 33
    MOD = 34
    ASSIGN = 35
    ADD = 36
    MUL = 37
    NOTEQUAL = 38
    LESSOREQUAL = 39
    GREATEROREQUAL = 40
    SUB = 41
    DIVISION = 42
    EQUAL = 43
    LESS = 44
    GREATER = 45
    LSB = 46
    RSB = 47
    COLON = 48
    LB = 49
    RB = 50
    SEMI = 51
    DD = 52
    COMMA = 53
    INTLIT = 54
    FLOATLIT = 55
    WS = 56
    ID = 57
    STRINGLIT = 58
    UNCLOSE_STRING = 59
    ERR = 60
    ESCAPE = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'+'", "'*'", "'<>'", "'<='", "'>='", "'-'", "'/'", 
            "'='", "'<'", "'>'", "'['", "']'", "':'", "'('", "')'", "';'", 
            "'..'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRADI_CMT", "BLOCK_CMT", "LINE_CMT", "BOOLEANLIT", "BREAK", 
            "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", 
            "RETURN", "WHILE", "WITH", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
            "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REALTYPE", "BOOLEANTYPE", 
            "INTTYPE", "STRINGTYPE", "NOT", "AND", "OR", "DIV", "MOD", "ASSIGN", 
            "ADD", "MUL", "NOTEQUAL", "LESSOREQUAL", "GREATEROREQUAL", "SUB", 
            "DIVISION", "EQUAL", "LESS", "GREATER", "LSB", "RSB", "COLON", 
            "LB", "RB", "SEMI", "DD", "COMMA", "INTLIT", "FLOATLIT", "WS", 
            "ID", "STRINGLIT", "UNCLOSE_STRING", "ERR", "ESCAPE", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "TRADI_CMT", "BLOCK_CMT", "LINE_CMT", "BOOLEANLIT", "BREAK", 
                  "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
                  "ELSE", "RETURN", "WHILE", "WITH", "BEGIN", "END", "FUNCTION", 
                  "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REALTYPE", 
                  "BOOLEANTYPE", "INTTYPE", "STRINGTYPE", "NOT", "AND", 
                  "OR", "DIV", "MOD", "A", "B", "C", "D", "E", "F", "G", 
                  "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
                  "S", "T", "U", "V", "W", "X", "Y", "Z", "ASSIGN", "ADD", 
                  "MUL", "NOTEQUAL", "LESSOREQUAL", "GREATEROREQUAL", "SUB", 
                  "DIVISION", "EQUAL", "LESS", "GREATER", "LSB", "RSB", 
                  "COLON", "LB", "RB", "SEMI", "DD", "COMMA", "INTLIT", 
                  "CASE1", "CASE2", "CASE3", "CASE4", "FLOATLIT", "WS", 
                  "ID", "STRINGLIT", "UNCLOSE_STRING", "ERR", "ESCAPE", 
                  "ILL", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[87] = self.STRINGLIT_action 
            actions[88] = self.UNCLOSE_STRING_action 
            actions[89] = self.ERR_action 
            actions[90] = self.ESCAPE_action 
            actions[92] = self.ILLEGAL_ESCAPE_action 
            actions[93] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             
             temp=Lexer.text.fget(self)
             temp1=(temp[1:len(temp)-1])
             Lexer.text.fset(self,temp1)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             
              raise UncloseString(self.text[1:])

     

    def ERR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

              raise ErrorToken('\\')

     

    def ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            Lexer.text.fset(self,"\b")
     

        if actionIndex == 4:
            Lexer.text.fset(self,"\f")
     

        if actionIndex == 5:
            Lexer.text.fset(self,"\r")
     

        if actionIndex == 6:
            Lexer.text.fset(self,"\n")
     

        if actionIndex == 7:
            Lexer.text.fset(self,"\t")
     

        if actionIndex == 8:
            Lexer.text.fset(self,"\'")
     

        if actionIndex == 9:
            Lexer.text.fset(self,"\"")
     

        if actionIndex == 10:
            Lexer.text.fset(self,"\\")
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 11:
                
             temp=Lexer.text.fget(self) 
             temp1=temp.find('\\')
             raise IllegalEscape(self.text[1:temp1+2])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 12:

             raise ErrorToken(self.text)

     


