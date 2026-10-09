# 1074. Reescribir un número real con exactamente N cifras tras el punto

[Timus 1074](https://acm.timus.ru/problem.aspx?space=1&num=1074) · dificultad 2110 · parsing

Problema original de Alexander Klepinin, del Ural State University Personal Contest Online, febrero de 2001, Students Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número real es un signo opcional, luego cifras, `.cifras` o
`cifras.cifras`, y luego opcionalmente `e` o `E` con un entero que puede
llevar signo. La entrada tiene pares de líneas: una línea `S` de hasta 100
caracteres con códigos 32–255 y un entero `0 ≤ N ≤ 100`; una línea `#`
termina la entrada. Para cada par imprime `Not a floating point number`
si `S` no es un número real; si lo es, imprime su valor con exactamente
`N` cifras tras el punto, cortando el resto sin redondear, sin ceros a la
izquierda en la parte entera (una parte entera nula es un solo `0`) y sin
signo `+`. Se garantiza que la respuesta no pasa de 200 caracteres.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Pares de líneas `S` y `N`, y luego la línea `#`.

## Salida

Una línea por cada par.

## Evaluación

La salida se compara línea a línea; dentro de una línea, token a token.
Las pruebas guardan las líneas en UTF-8 y se las dan a las soluciones en
latin-1, un byte por cada carácter de 32 a 255.

## Ejemplos

### Ejemplo 1

Entrada:

```
10.23
0
.04
1
-0.051e0
1
1.1e30
10
-1.1E-30
1
2468097632.1358642324268913e-2
20
e23
3
1 e3
1
#
```

Salida:

```
10
0.0
0.0
1100000000000000000000000000000.0000000000
0.0
24680976.32135864232426891300
Not a floating point number
Not a floating point number
```

## Solución

La línea se analiza a mano, exactamente según la gramática: un signo
opcional, las cifras antes del punto, luego o bien un punto seguido de al
menos una cifra, o bien ningún punto pero al menos una cifra antes, luego
un exponente opcional con al menos una cifra, y nada más. Cualquier otro
carácter, incluido un espacio, hace inválida la línea.

El número nunca se convierte en un valor de coma flotante. Las cifras de
antes y de después del punto se unen en una cadena `D`; el punto decimal
queda tras `len(antes) + exponente` de sus cifras, una posición que puede
ser negativa o caer más allá del final de `D`. La parte entera son las
cifras de `D` antes de esa posición, completadas con ceros a la derecha y
sin ceros a la izquierda (o `0`); la fracción son las `N` cifras
siguientes, completadas con ceros. Cortar las cifras es exactamente el
truncamiento pedido. `O(|S| + N)`.

Detalles a tener en cuenta:

- el signo menos solo se queda si alguna cifra impresa no es cero:
  `-0.051` con una cifra es `0.0`, igual que `-1.1E-30`;
- con `N = 0` no hay punto decimal;
- `5.`, `.`, `e5`, `1e`, `1e+`, `1.e5` y una línea vacía no son números;
  `.5`, `+.5` y `-0` sí lo son;
- el exponente puede tener decenas de cifras: su valor se limita a 1000 al
  leerlo; uno mayor o bien hace cero la respuesta (con como mucho 100
  cifras en `D`) o queda excluido por la garantía de 200 caracteres, salvo
  que todas las cifras sean cero, y entonces no importa;
- los caracteres por encima de 127 no deben contar como cifras ni como
  espacios: `str.isdigit` de Python acepta `²`, y leer la entrada como
  UTF-8 falla con esos bytes, así que la entrada se lee como bytes o
  latin-1 y las cifras se comprueban como `'0' ≤ c ≤ '9'`;
- de cada línea solo se quita un retorno de carro final; los espacios son
  parte de `S`.

Las respuestas se comprobaron con una expresión regular para la gramática
y aritmética exacta de fracciones para el valor, en las líneas hechas a
mano y en miles de líneas aleatorias.

## Notas por lenguaje

- C++ lee las líneas con `std::getline`, que conserva cada byte.
- Go y Rust leen toda la entrada como bytes y la parten en cada `\n`.
- Java lee los bytes y los decodifica como ISO-8859-1, que hace
  corresponder un carácter a cada byte.
- Python decodifica `sys.stdin.buffer` como latin-1 por la misma razón.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1074_parsing.cpp](1074_parsing.cpp) | G++ 13.2 x64 | parsing | O(len(S) + N) | AC | 0.015 s | 372 KB |
| [1074_parsing.go](1074_parsing.go) | Go 1.14 x64 | parsing | O(len(S) + N) | AC | 0.031 s | 948 KB |
| [1074_parsing.java](1074_parsing.java) | Java 1.8 | parsing | O(len(S) + N) | AC | 0.109 s | 940 KB |
| [1074_parsing.py](1074_parsing.py) | Python 3.12 x64 | parsing | O(len(S) + N) | AC | 0.078 s | 752 KB |
| [1074_parsing.rs](1074_parsing.rs) | Rust 1.75 x64 | parsing | O(len(S) + N) | AC | 0.015 s | 236 KB |
