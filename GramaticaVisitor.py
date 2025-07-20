# Generated from Gramatica.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaParser.

class GramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaParser#inicio.
    def visitInicio(self, ctx:GramaticaParser.InicioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#saludo.
    def visitSaludo(self, ctx:GramaticaParser.SaludoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#Numero.
    def visitNumero(self, ctx:GramaticaParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#Suma.
    def visitSuma(self, ctx:GramaticaParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#Parentesis.
    def visitParentesis(self, ctx:GramaticaParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#Multiplicacion.
    def visitMultiplicacion(self, ctx:GramaticaParser.MultiplicacionContext):
        return self.visitChildren(ctx)



del GramaticaParser