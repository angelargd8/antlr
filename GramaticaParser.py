# Generated from Gramatica.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("#\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\5\2\13\n\2\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\26\n\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\7\4\36\n\4\f\4\16\4!\13\4\3\4\2\3\6\5\2\4\6\2")
        buf.write("\2\2#\2\n\3\2\2\2\4\f\3\2\2\2\6\25\3\2\2\2\b\13\5\4\3")
        buf.write("\2\t\13\5\6\4\2\n\b\3\2\2\2\n\t\3\2\2\2\13\3\3\2\2\2\f")
        buf.write("\r\7\3\2\2\r\16\7\b\2\2\16\5\3\2\2\2\17\20\b\4\1\2\20")
        buf.write("\21\7\6\2\2\21\22\5\6\4\2\22\23\7\7\2\2\23\26\3\2\2\2")
        buf.write("\24\26\7\t\2\2\25\17\3\2\2\2\25\24\3\2\2\2\26\37\3\2\2")
        buf.write("\2\27\30\f\6\2\2\30\31\7\4\2\2\31\36\5\6\4\7\32\33\f\5")
        buf.write("\2\2\33\34\7\5\2\2\34\36\5\6\4\6\35\27\3\2\2\2\35\32\3")
        buf.write("\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \7\3\2\2")
        buf.write("\2!\37\3\2\2\2\6\n\25\35\37")
        return buf.getvalue()


class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hola'", "'+'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PALABRA", "NUMERO", "WS" ]

    RULE_inicio = 0
    RULE_saludo = 1
    RULE_expr = 2

    ruleNames =  [ "inicio", "saludo", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    PALABRA=6
    NUMERO=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InicioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def saludo(self):
            return self.getTypedRuleContext(GramaticaParser.SaludoContext,0)


        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_inicio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicio" ):
                listener.enterInicio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicio" ):
                listener.exitInicio(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicio" ):
                return visitor.visitInicio(self)
            else:
                return visitor.visitChildren(self)




    def inicio(self):

        localctx = GramaticaParser.InicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_inicio)
        try:
            self.state = 8
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GramaticaParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.saludo()
                pass
            elif token in [GramaticaParser.T__3, GramaticaParser.NUMERO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaludoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PALABRA(self):
            return self.getToken(GramaticaParser.PALABRA, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_saludo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaludo" ):
                listener.enterSaludo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaludo" ):
                listener.exitSaludo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaludo" ):
                return visitor.visitSaludo(self)
            else:
                return visitor.visitChildren(self)




    def saludo(self):

        localctx = GramaticaParser.SaludoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_saludo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(GramaticaParser.T__0)
            self.state = 11
            self.match(GramaticaParser.PALABRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERO(self):
            return self.getToken(GramaticaParser.NUMERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class SumaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicacionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicacion" ):
                listener.enterMultiplicacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicacion" ):
                listener.exitMultiplicacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicacion" ):
                return visitor.visitMultiplicacion(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GramaticaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GramaticaParser.T__3]:
                localctx = GramaticaParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 14
                self.match(GramaticaParser.T__3)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(GramaticaParser.T__4)
                pass
            elif token in [GramaticaParser.NUMERO]:
                localctx = GramaticaParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(GramaticaParser.NUMERO)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 27
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = GramaticaParser.SumaContext(self, GramaticaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 22
                        self.match(GramaticaParser.T__1)
                        self.state = 23
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = GramaticaParser.MultiplicacionContext(self, GramaticaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 25
                        self.match(GramaticaParser.T__2)
                        self.state = 26
                        self.expr(4)
                        pass

             
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




