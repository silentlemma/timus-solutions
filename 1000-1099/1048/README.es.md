# 1048. Sumar dos números de un millón de cifras

[Timus 1048](https://acm.timus.ru/problem.aspx?space=1&num=1048) · dificultad 200 · implementation

Problema original de Stanislav Vasiliev y Alexander Klepinin, del concurso universitario de programación de la Universidad Estatal de los Urales, 25 de marzo de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos enteros positivos tienen `N` cifras cada uno (`1 ≤ N ≤ 10^6`, se
permiten ceros a la izquierda), y su suma también cabe en `N` cifras. Se
dan en columnas: la línea `i` contiene la `i`-ésima cifra de cada número.
Imprime la suma con exactamente `N` cifras.

Límite de tiempo: 2 segundos. Límite de memoria: 16 MB.

## Entrada

`N` y luego `N` líneas con dos cifras separadas por un espacio.

## Salida

Las `N` cifras de la suma en una línea.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 4
4 2
6 8
3 7
```

Salida:

```
4750
```

### Ejemplo 2

Entrada:

```
3
0 0
4 5
5 5
```

Salida:

```
100
```

## Solución

Suma escolar: se guardan las sumas de las columnas (de 0 a 18) en un
arreglo de bytes y luego se recorre desde la última columna hasta la
primera, sumando el acarreo y quedándose con `t mod 10` y el nuevo acarreo
`t div 10`. El mismo arreglo de `N` bytes pasa a ser las cifras de la
respuesta. Tiempo `O(N)` y `N` bytes de memoria.

La dificultad está solo en el tamaño: unos 4 MB de entrada con un límite
de memoria de 16 MB. Hay que leer rápido y no guardar objetos ni enteros
de 4 bytes por cifra.

Detalles a tener en cuenta:

- los ceros a la izquierda de la suma se imprimen: la salida tiene
  exactamente `N` cifras;
- un acarreo puede recorrer el millón de cifras (`0999…9 + 000…1`);
- convertir los números a un tipo de enteros grandes no hace falta y, en
  muchos lenguajes, es cuadrático.

## Notas por lenguaje

- **C++**, **Java**: lectura por bytes con búfer mediante `fread` /
  `DataInputStream`; **Go**: `bufio.Reader.ReadByte`; **Rust**: toda la
  entrada en un vector de bytes.
- **Python**: toda la entrada es un objeto `bytes`; `translate` borra los
  espacios, los cortes con paso 2 separan los dos números y el bucle del
  acarreo escribe en un `bytearray`. Convertir con `int()` sería
  cuadrático (y Python 3.12 rechaza por defecto cadenas de más de 4300
  cifras).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1048_implementation.cpp](1048_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 1184 KB |
| [1048_implementation.go](1048_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.062 s | 1976 KB |
| [1048_implementation.java](1048_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.140 s | 2080 KB |
| [1048_implementation.py](1048_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.406 s | 10360 KB |
| [1048_implementation.rs](1048_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 10248 KB |
