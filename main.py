import sys
from antlr4 import *
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser

#objetivo: hacer un hola mundo, reconocer sumas y multiplicaciones entre digitos. 
#generar un analizador léxico 
#generar un analizador sintactico 


def main():
    #leer el archivo de input
    input_stream = InputStream("3+4*5")

    lexer= GramaticaLexer(input_stream)
    stream= CommonTokenStream(lexer)
    parser= GramaticaParser(stream)

    tree= parser.expr()
    print(tree.toStringTree(recog=parser))

main()