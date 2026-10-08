# 1007. Corregir un error en palabras de código con suma de control

[Timus 1007](https://acm.timus.ru/problem.aspx?space=1&num=1007) · dificultad 404 · math

Problema original del Campeonato de la Universidad Estatal de los Urales 1997.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada palabra enviada es una cadena de `N` caracteres `0`/`1`
(`4 ≤ N ≤ 1000`) cuyo **peso** —la suma de las posiciones, contando desde 1,
de sus unos— es divisible entre `N + 1` (el peso 0 también vale). Cada palabra
sufre en el camino como mucho uno de estos cambios:

- un `0` se reemplaza por `1`;
- se borra un carácter;
- se inserta un carácter (`0` o `1`) en cualquier posición.

Dadas las palabras recibidas, imprime las enviadas. La palabra enviada
siempre queda determinada de forma única.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego como mucho 2001 palabras recibidas, una por línea. La entrada
puede contener además espacios y líneas vacías de sobra.

## Salida

Las palabras enviadas en el orden de la entrada, una por línea.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
00000
10101
1011
111000
```

Salida:

```
00000
10001
11011
11100
```

### Ejemplo 2

Entrada:

```
6   

001100  
   10101


0100110 
110111

```

Salida:

```
001100
101101
010010
110011
```

## Solución

Sea `m = N + 1`, `w` el peso de la palabra recibida y `L` su longitud.

- `L = N`: o la palabra está intacta (`w ≡ 0`), o un `0` en la posición `p`
  se volvió `1`, lo que sumó exactamente `p`; entonces `p = w mod m` y el
  carácter de la posición `p` vuelve a ser `0`.
- `L = N - 1` (un borrado): insertar un dígito `d` en la posición `i` suma
  `d·i` más uno por cada `1` a su derecha, porque estos se desplazan una
  posición. Se recorre `i = L+1, L, ..., 1`, llevando la cuenta de unos a la
  derecha, y se toman los primeros `i` y `d` con
  `w + ones_right + d·i ≡ 0 (mod m)`.
- `L = N + 1` (una inserción): borrar el carácter `d` de la posición `i` resta
  `d·i` y uno por cada `1` a la derecha. El mismo recorrido de derecha a
  izquierda encuentra `i` con `w - ones_right - d·i ≡ 0 (mod m)`.

Son los códigos de Varshamov–Tenengolts, que corrigen un borrado o una
inserción (y, aquí, un cero convertido en uno): dos palabras enviadas
distintas nunca dan la misma palabra recibida, así que cualquier posición que
deje el peso correcto da la palabra enviada. Cada palabra se procesa en
`O(N)`, toda la entrada en `O(longitud total)`.

Detalles a tener en cuenta:

- las palabras están separadas por espacios en blanco arbitrarios: lee tokens,
  no líneas;
- en un borrado puede faltar el último carácter: hay que probar también la
  posición tras el final;
- una fuerza bruta que reconstruye y vuelve a pesar cada palabra candidata es
  `O(N^2)` por palabra, hasta `4·10^9` pasos en total.

## Notas por lenguaje

El mismo recorrido lineal en todos los lenguajes. Python arma la respuesta con
cortes de cadenas; por palabra son dos pasadas `O(N)`, suficiente incluso para
CPython.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1007_math.cpp](1007_math.cpp) | G++ 13.2 x64 | math | O(total length) | AC | 0.015 s | 2420 KB |
| [1007_math.go](1007_math.go) | Go 1.14 x64 | math | O(total length) | AC | 0.015 s | 3336 KB |
| [1007_math.java](1007_math.java) | Java 1.8 | math | O(total length) | AC | 0.109 s | 13200 KB |
| [1007_math.py](1007_math.py) | Python 3.12 x64 | math | O(total length) | AC | 0.281 s | 4516 KB |
| [1007_math.rs](1007_math.rs) | Rust 1.75 x64 | math | O(total length) | AC | 0.015 s | 3104 KB |
