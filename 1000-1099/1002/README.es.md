# 1002. Escribir un número con la menor cantidad de palabras

[Timus 1002](https://acm.timus.ru/problem.aspx?space=1&num=1002) · dificultad 226 · dp, hashing

Problema original de la Olimpiada Centroeuropea de Informática 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada letra latina minúscula representa un dígito:

| Dígito | Letras |
|--------|--------|
| 1 | i j |
| 2 | a b c |
| 3 | d e f |
| 4 | g h |
| 5 | k l |
| 6 | m n |
| 7 | p r s |
| 8 | t u v |
| 9 | w x y |
| 0 | o q z |

Una palabra escribe la cadena de dígitos de sus letras. Dados un número (una
cadena de como máximo 100 dígitos) y un diccionario de `n ≤ 50 000` palabras,
encuentra una secuencia de palabras del diccionario con la menor cantidad de
palabras cuyas escrituras, concatenadas, den el número. Cada palabra puede
usarse cualquier cantidad de veces.

La entrada contiene varias pruebas de este tipo; su tamaño total es como máximo
300 KB.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Las pruebas van una tras otra. Una prueba es una línea con el número, una línea
con `n` y `n` líneas con una palabra cada una (de 1 a 50 letras minúsculas).
Una línea `-1` termina la entrada.

## Salida

Para cada prueba, una línea: las palabras de una secuencia más corta separadas
por espacios simples, o `No solution.` si el número no se puede escribir.

## Evaluación

Se acepta cualquier secuencia más corta: el verificador comprueba que las
palabras estén en el diccionario, que escriban el número y que no exista una
secuencia más corta.

## Ejemplos

### Ejemplo 1

Entrada:

```
8733
3
use
e
tree
12
2
ab
cd
-1
```

Salida:

```
tree
No solution.
```

### Ejemplo 2

Entrada:

```
22
4
ac
ba
b
c
-1
```

Salida:

```
ac
```

## Solución

Programación dinámica sobre los prefijos del número: `best[i]` es la menor
cantidad de palabras que escriben los primeros `i` dígitos, `best[0] = 0`.
Desde cada `i` alcanzable se prueba cada palabra cuya escritura coincide con la
subcadena que empieza en `i`, y se guarda la última palabra para reconstruir la
respuesta.

Probar las `n` palabras en cada posición cuesta `O(100 · n · 50)` por prueba.
Es mucho más rápido guardar el diccionario en una tabla hash de escritura a
palabra: una palabra tiene como máximo 50 letras, así que en cada posición solo
hay que buscar las subcadenas de longitud 1 a 50. Son `O(100 · 50)` búsquedas
por prueba más `O(longitud total de las palabras)` para construir la tabla,
rápido en cualquier lenguaje.

Detalles a tener en cuenta:

- varias palabras pueden tener la misma escritura: basta con guardar cualquiera;
- una palabra puede usarse muchas veces;
- la salida debe ser exactamente `No solution.` cuando no hay respuesta.

## Notas por lenguaje

- **C++**: `std::unordered_map<std::string, int>`; leer con `cin` después de
  `sync_with_stdio(false)`.
- **Go**: `map[string]int`, donde `phone[i:i+l]` es una subcadena barata.
- **Python**: la tabla es un `dict` y las escrituras salen de `str.translate`;
  la versión con búsquedas es rápida, mientras que comparar cada palabra en cada
  posición sería demasiado lento.
- **Java**: `HashMap<String, Integer>` con `putIfAbsent`; entrada con
  `BufferedReader` y `StringTokenizer`.
- **Rust**: `HashMap<Vec<u8>, usize>` consultado con porciones de bytes del
  número.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1002_dp_hashing.cpp](1002_dp_hashing.cpp) | G++ 13.2 x64 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.015 s | 2764 KB |
| [1002_dp_hashing.go](1002_dp_hashing.go) | Go 1.14 x64 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.031 s | 3016 KB |
| [1002_dp_hashing.java](1002_dp_hashing.java) | Java 1.8 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.109 s | 7032 KB |
| [1002_dp_hashing.py](1002_dp_hashing.py) | Python 3.12 x64 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.093 s | 5424 KB |
| [1002_dp_hashing.rs](1002_dp_hashing.rs) | Rust 1.75 x64 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.031 s | 2540 KB |
