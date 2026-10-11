# 1269. Filtro de palabrotas

[Timus 1269](https://acm.timus.ru/problem.aspx?space=1&num=1269) · dificultad 832 · strings

Problema original de Pavel Atnashev, del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dadas n ≤ 10 000 palabras prohibidas (cualquier byte salvo 0, 10 y 13,
como mucho 10 000 cada una y 100 KB en total) y un texto de m líneas
(como mucho 900 KB), hay que hallar dónde aparece por primera vez una
palabra prohibida como subcadena: el número de línea y la posición del
primer carácter de la palabra en ella. Si no hay ninguna, se imprime
`Passed`. El límite de memoria es de solo 8 MB.

Límite de tiempo: 1 segundo. Límite de memoria: 8 MB.

## Entrada

n, las n palabras una por línea, m, y luego las m líneas del texto.

## Salida

La línea y la posición, o `Passed`.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
dear
sweetie
angel
dream
baby
8
Had I the heavens' embroidered cloths, 
Enwrought with golden and silver light, 
The blue and the dim and the dark cloths 
Of night and light and the half-light, 
I would spread the cloths under your feet: 
But I, being poor, have only my dreams; 
I have spread my dreams under your feet; 
Tread softly because you tread on my dreams.
```

Salida:

```
6 33
```

## Solución

Se construye un autómata de Aho–Corasick con las palabras. En cada nodo
se guarda la longitud de la palabra más larga que termina allí, contando
las alcanzables por enlaces de fallo. Cada línea se pasa por el
autómata. Tras el i-ésimo byte, la palabra más larga que termina allí
empieza en i − longest + 1, el comienzo más temprano entre las palabras
que terminan en i. La respuesta de la línea es el menor de esos
comienzos en toda la línea, y la primera línea con alguna coincidencia
da la respuesta.

Una tabla de 256 hijos por nodo no cabe en 8 MB con 100 000 nodos. Así
que el trie se construye primero con listas de hijo y hermano y luego se
renumera en orden de anchura, de modo que los hijos de cada nodo reciben
números consecutivos. Un hijo se busca entonces recorriendo un tramo
corto de bytes (`memchr`, `bytes.IndexByte`, `bytearray.find`), y los
enlaces de fallo se calculan en el mismo orden, con el nodo de destino
siempre antes. Con W bytes de palabras, T bytes de texto y como máximo
σ = 253 hijos por nodo, construir el trie y los enlaces cuesta O(W · σ),
y buscar cuesta O(T · σ). Python ordena primero las n palabras, añadiendo
O(W log n) comparaciones de bytes, y construye una caché de transiciones
acotada. El tiempo total es O((W + T) · σ) en los demás lenguajes y
O(W log n + (W + T) · σ) en Python.

Detalles a tener en cuenta:

- se busca el comienzo más temprano, no el final más temprano: en
  `xabcdefx` la palabra `abcdef` en 2 va antes que `cd` en 4
  (prueba 02);
- las palabras pueden tener espacios, tabuladores y puntuación, así que
  las líneas no se deben partir en tokens (pruebas 03, 07);
- los enlaces de fallo representan sufijos más cortos. Un nodo no terminal
  puede tener un sufijo terminal; se conserva el sufijo coincidente más
  largo para obtener el comienzo más temprano;
- los retornos de carro internos del texto son datos: cuentan en la posición
  y reinician el autómata, pues no pueden aparecer en las palabras. Quitarlos
  desplaza coincidencias o une bytes en coincidencias falsas (prueba 09);
- las líneas pueden estar vacías, y una sola línea puede ocupar casi
  todo el texto (prueba 06, gen7).

Las respuestas se compararon con buscar cada palabra en cada línea en
60 casos generados.

## Notas por lenguaje

- Todos los lenguajes construyen el mismo trie renumerado en arreglos
  planos y leen el texto línea a línea.
- Java construye el trie directamente con los bytes de la entrada y
  recorre cada línea del texto sin guardarla: las cadenas de las palabras
  y las líneas no cabrían en 8 MB. Python lee bytes y guarda los arreglos
  en `array` y `bytearray` para no pasar del límite de memoria.
- La solución en Python corre en CPython y guarda una caché de unos 2 MB
  de transiciones del autómata; una versión anterior sin ella superaba
  el límite de tiempo en la prueba 13 del juez. PyPy no es salida,
  porque su entorno de ejecución ya necesita más de los 8 MB permitidos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1269_strings.cpp](1269_strings.cpp) | G++ 13.2 x64 | strings | O((W + T) · σ) | AC | 0.046 s | 6004 KB |
| [1269_strings.go](1269_strings.go) | Go 1.14 x64 | strings | O((W + T) · σ) | AC | 0.078 s | 6352 KB |
| [1269_strings.java](1269_strings.java) | Java 1.8 | strings | O((W + T) · σ) | AC | 0.203 s | 3560 KB |
| [1269_strings.py](1269_strings.py) | Python 3.12 x64 | strings | O(W log n + (W + T) · σ) | AC | 0.562 s | 7048 KB |
| [1269_strings.rs](1269_strings.rs) | Rust 1.75 x64 | strings | O((W + T) · σ) | AC | 0.109 s | 6072 KB |
