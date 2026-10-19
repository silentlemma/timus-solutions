# 2106. Decodificar estructuras anidadas de un flujo de bytes en hex

[Timus 2106](https://acm.timus.ru/problem.aspx?space=1&num=2106) · dificultad 1057 · parsing

Problema original de Mikhail Vyatskov, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un protocolo binario conoce n tipos de estructura. Un campo es un int (4
bytes, big-endian, sin signo), una cadena (su longitud como int y luego
un byte por letra minúscula) o una estructura descrita antes, cuyos
campos van en orden. El flujo es una sucesión de registros: el número
del tipo de estructura empezando en 1 como int, y luego esa estructura.
Imprimir los registros como un árbol con sangría. Los límites son 2
segundos y 64 MB.

## Entrada

n y l, 1 ≤ n ≤ 240, 2n ≤ l ≤ 10³, y luego l líneas de descripción:
"struct nombre" empieza un tipo y cada línea siguiente tiene, tras un
espacio, el tipo de un campo. La última línea es el flujo en hex con
mayúsculas, de a lo sumo 10⁴ dígitos.

## Salida

Para cada registro, el nombre de su tipo y luego los campos uno por
línea, con un espacio más de sangría que su dueño: "int valor", "string
texto", o el nombre de una estructura anidada seguido de sus propios
campos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 5
struct a
 string
struct b
 a
 int
000000020000000361626300000004000000010000000568656C6C6F
```

Salida:

```
b
 a
  string abc
 int 4
a
 string hello
```

## Solución

Se leen las descripciones en una tabla de tipos de campo por estructura
y se decodifica la línea hex a bytes. Luego se recorre el flujo con una
pila explícita de pares (estructura, siguiente campo) en lugar de
recursión, porque las estructuras pueden anidarse unos 240 niveles. En
cada paso se toma el siguiente campo de la estructura de la cima: un int
imprime un número, una cadena lee su longitud y luego esa cantidad de
bytes, y una estructura imprime su nombre y se apila. La sangría de una
línea es la profundidad de la pila. Una estructura con todos sus campos
hechos se desapila, y una pila vacía empieza el siguiente registro.

Cada byte se lee una vez y cada línea impresa cuesta su longitud, así que
el trabajo es lineal en la entrada y la salida.

En el ejemplo el flujo contiene 2 (tipo b), luego la cadena "abc" del a
interior, luego 4, y después el registro 1 (tipo a) con "hello".

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2106_parsing.cpp](2106_parsing.cpp) | G++ 13.2 x64 | parsing | O(L + output) | AC | 0.015 s | 528 KB |
| [2106_parsing.go](2106_parsing.go) | Go 1.14 x64 | parsing | O(L + output) | AC | 0.031 s | 1364 KB |
| [2106_parsing.java](2106_parsing.java) | Java 1.8 | parsing | O(L + output) | AC | 0.093 s | 1076 KB |
| [2106_parsing.py](2106_parsing.py) | Python 3.12 x64 | parsing | O(L + output) | AC | 0.078 s | 828 KB |
| [2106_parsing.rs](2106_parsing.rs) | Rust 1.75 x64 | parsing | O(L + output) | AC | 0.046 s | 476 KB |
