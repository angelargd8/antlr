# Generated from Gramatica.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("\61\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\6\7\"\n\7\r\7\16\7#\3\b\6\b\'\n\b")
        buf.write("\r\b\16\b(\3\t\6\t,\n\t\r\t\16\t-\3\t\3\t\2\2\n\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\3\2\5\4\2C\\c|\3\2\62;\5")
        buf.write("\2\13\f\17\17\"\"\2\63\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\3\23\3\2\2\2\5\30\3\2\2\2\7\32\3\2\2\2\t")
        buf.write("\34\3\2\2\2\13\36\3\2\2\2\r!\3\2\2\2\17&\3\2\2\2\21+\3")
        buf.write("\2\2\2\23\24\7j\2\2\24\25\7q\2\2\25\26\7n\2\2\26\27\7")
        buf.write("c\2\2\27\4\3\2\2\2\30\31\7-\2\2\31\6\3\2\2\2\32\33\7,")
        buf.write("\2\2\33\b\3\2\2\2\34\35\7*\2\2\35\n\3\2\2\2\36\37\7+\2")
        buf.write("\2\37\f\3\2\2\2 \"\t\2\2\2! \3\2\2\2\"#\3\2\2\2#!\3\2")
        buf.write("\2\2#$\3\2\2\2$\16\3\2\2\2%\'\t\3\2\2&%\3\2\2\2\'(\3\2")
        buf.write("\2\2(&\3\2\2\2()\3\2\2\2)\20\3\2\2\2*,\t\4\2\2+*\3\2\2")
        buf.write("\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2./\3\2\2\2/\60\b\t\2\2")
        buf.write("\60\22\3\2\2\2\6\2#(-\3\b\2\2")
        return buf.getvalue()


class GramaticaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    PALABRA = 6
    NUMERO = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'hola'", "'+'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "PALABRA", "NUMERO", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "PALABRA", "NUMERO", 
                  "WS" ]

    grammarFileName = "Gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


