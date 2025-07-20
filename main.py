import sys
from antlr4 import *
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser

#objetivo: hacer un hola mundo, reconocer sumas y multiplicaciones entre digitos. 
#generar un analizador léxico 
#generar un analizador sintactico 


def main():
    #contiene el texto a analizar
    input_stream = InputStream("3+4*5")

    #instancia del lexer
    lexer= GramaticaLexer(input_stream)

    #almacen de tokens
    #organiza los tokens generados por el lexer en un flujo para el parser
    stream= CommonTokenStream(lexer)

    #instancia del parser
    parser= GramaticaParser(stream)

    #llama a la regla inicial de la gramatica, expr, para que el parser comience a analizar
    #construye un arbol de analisis sintactico
    tree= parser.expr()
    print(tree.toStringTree(recog=parser))

main()