grammar Gramatica;

// ----------- Reglas sintacticas  ------------

// Regla: puede ser un saludo o una expresión aritmética
inicio
    : saludo
    | expr
    ;

// Saludo
saludo
    : 'hola' PALABRA
    ;

// Expresiones aritmeticas
expr
    : expr '+' expr   # Suma
    | expr '*' expr   # Multiplicacion
    | '(' expr ')'    # Parentesis
    | NUMERO          # Numero
    ;

// ----------- Reglas lexicas  ------------

PALABRA: [a-zA-Z]+;
NUMERO: [0-9]+;

WS: [ \t\r\n]+ -> skip;