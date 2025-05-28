# Intérprete de Pascal

Este proyecto es un intérprete simple para un lenguaje de programación similar a Pascal. Implementa los conceptos fundamentales de la teoría de compiladores para analizar y ejecutar código Pascal.

## 📚 Teoría y Fundamentos

### 🎯 ¿Qué es un Intérprete?

Un **intérprete** es un programa que analiza y ejecuta código fuente directamente, línea por línea, sin generar un archivo ejecutable intermedio. A diferencia de un compilador que traduce todo el código a lenguaje máquina, el intérprete procesa y ejecuta el código en tiempo real.

### 🔍 Componentes Principales

Nuestro intérprete está dividido en **tres etapas principales** que siguen el flujo clásico de procesamiento de lenguajes:

```
Código Fuente → [Lexer] → Tokens → [Parser] → AST → [Intérprete] → Resultado
```

---

## 1️⃣ **Análisis Léxico (Lexer)**

### ¿Qué es el Análisis Léxico?

El **analizador léxico** o **lexer** es la primera etapa del procesamiento. Su función es:

- **Leer** el código fuente carácter por carácter
- **Reconocer** patrones y agrupar caracteres en unidades significativas
- **Generar** una secuencia de **tokens** (elementos básicos del lenguaje)

### Ejemplo de Tokenización

```pascal
x := 5 + 3;
```

Se convierte en los siguientes tokens:
```
IDENTIFIER(x) → ASSIGN(:=) → INTEGER(5) → PLUS(+) → INTEGER(3) → SEMICOLON(;) → EOF
```

### Tipos de Tokens Soportados

| Categoría | Ejemplos | Descripción |
|-----------|----------|-------------|
| **Literales** | `123`, `3.14`, `'a'`, `"hello"`, `true` | Valores constantes |
| **Identificadores** | `x`, `variable`, `contador` | Nombres de variables |
| **Operadores** | `+`, `-`, `*`, `/`, `>`, `<`, `:=` | Símbolos de operación |
| **Delimitadores** | `(`, `)`, `;`, `,` | Símbolos de estructura |
| **Palabras Clave** | `if`, `while`, `begin`, `end` | Comandos del lenguaje |

---

## 2️⃣ **Análisis Sintáctico (Parser)**

### ¿Qué es el Análisis Sintáctico?

El **analizador sintáctico** o **parser** es la segunda etapa que:

- **Recibe** la secuencia de tokens del lexer
- **Verifica** que la sintaxis sea correcta según la gramática del lenguaje
- **Construye** un Árbol de Sintaxis Abstracta (AST)

### Gramática de Pascal Simplificada

Nuestra implementación sigue esta gramática básica:

```
programa      ::= 'program' identificador ';' declaraciones 'begin' sentencias 'end'
declaraciones ::= ('var' identificador ':' tipo ';')*
sentencias    ::= sentencia*
sentencia     ::= asignación | condicional | bucle
asignación    ::= identificador ':=' expresión ';'
expresión     ::= término (('+'|'-') término)*
término       ::= factor (('*'|'/') factor)*
factor        ::= número | identificador | '(' expresión ')'
```

### Árbol de Sintaxis Abstracta (AST)

El AST es una representación en árbol de la estructura sintáctica del código:

```pascal
x := 5 + 3
```

Se convierte en:
```
    AssignmentNode
    ├── variable: "x"
    └── expression: BinaryOperationNode
                    ├── left: LiteralNode(5)
                    ├── operator: PLUS
                    └── right: LiteralNode(3)
```

---

## 3️⃣ **Interpretación (Interpreter)**

### ¿Qué es la Interpretación?

El **intérprete** es la etapa final que:

- **Recorre** el AST generado por el parser
- **Evalúa** las expresiones y ejecuta las instrucciones
- **Mantiene** el estado del programa (variables, valores)
- **Produce** el resultado final

### Patrón Visitor

Utilizamos el **patrón Visitor** para recorrer el AST:

```python
def interpret(self, node):
    method_name = f'visit_{type(node).__name__}'
    visitor = getattr(self, method_name)
    return visitor(node)
```

### Entorno de Ejecución

El **Environment** mantiene el estado de las variables:

```python
environment = Environment()
environment.set('x', 10)    # Asignar valor
value = environment.get('x') # Obtener valor
```

---

## 🚀 Características Implementadas

- **Tipos de Datos**: `integer`, `real`, `char`, `boolean`, `string`, `set of char`
- **Declaraciones**: Variables globales con tipos
- **Literales**: Enteros, reales, caracteres, booleanos, cadenas y conjuntos
- **Expresiones**: Operaciones aritméticas, relacionales y de conjuntos
- **Estructuras de Control**: Sentencias condicionales y operador ternario
- **Entrada/Salida**: Operaciones `read` y `write`

## Estructura del Proyecto

```
pascal-interpreter
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── lexer
│   │   ├── __init__.py
│   │   ├── lexer.py
│   │   └── tokens.py
│   ├── parser
│   │   ├── __init__.py
│   │   ├── parser.py
│   │   └── ast_nodes.py
│   ├── interpreter
│   │   ├── __init__.py
│   │   ├── interpreter.py
│   │   └── environment.py
│   ├── types
│   │   ├── __init__.py
│   │   └── data_types.py
│   └── utils
│       ├── __init__.py
│       └── exceptions.py
├── tests
│   ├── __init__.py
│   ├── test_lexer.py
│   ├── test_parser.py
│   └── test_interpreter.py
├── examples
│   ├── sample1.pas
│   └── sample2.pas
├── requirements.txt
├── setup.py
└── README.md
```

## Instalación

1. Clona el repositorio:
   ```
   git clone <repository-url>
   ```
2. Navega al directorio del proyecto:
   ```
   cd pascal-interpreter
   ```
3. Instala las dependencias requeridas:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar el intérprete, utiliza el siguiente comando:
```
python src/main.py
```

Puedes escribir tus programas en Pascal en el directorio `examples` y probarlos usando el intérprete.

## Contribuciones

¡Las contribuciones son bienvenidas! No dudes en enviar un pull request o abrir un issue para cualquier sugerencia o mejora.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.