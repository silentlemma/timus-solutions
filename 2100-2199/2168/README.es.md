# 2168. Cubrir una cadena con trozos disjuntos que tienen borde

[Timus 2168](https://acm.timus.ru/problem.aspx?space=1&num=2168) · dificultad 2963 · dp, strings

Problema original de Vadim Barinov, del Concurso Escolar de Programación de los Urales 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una fila de N runas es una cadena de letras minúsculas. Un movimiento
levanta un bloque contiguo de runas que siguen todas en su sitio, si
algún prefijo propio del bloque es igual a su sufijo de la misma
longitud (el bloque tiene borde, como abcdab o aa, pero no abc ni a).
Hallar el mayor número de runas que se pueden levantar. Los límites son
2 segundos y 256 MB.

## Entrada

N, 1 ≤ N ≤ 10⁵, y luego la cadena.

## Salida

El mayor número de runas levantadas.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
abcdab
```

Salida:

```
6
```

### Ejemplo 2

Entrada:

```
7
abcdabd
```

Salida:

```
6
```

### Ejemplo 3

Entrada:

```
6
abacdc
```

Salida:

```
6
```

## Solución

Los bloques levantados son intervalos disjuntos de la cadena original,
así que sea f(i) el menor número de runas que quedan entre las primeras
i, y la respuesta es N − f(N). Un bloque [l, e] tiene un borde de
longitud L exactamente cuando el texto en l reaparece en algún p > l con
LCP(l, p) ≥ L y e = p + L − 1. Así, un inicio l y una coincidencia
posterior p dejan que cada final en p … p + LCP(l, p) − 1 herede f(l),
y si no, f(i + 1) = f(i) + 1.

Dos hechos lo mantienen pequeño.

- **Quedan como mucho 26 runas.** De izquierda a derecha: una runa cuya
  letra vuelve a aparecer empieza un bloque hasta la última aparición de
  esa letra, y una runa cuya letra no vuelve a aparecer se salta. Cada
  letra se salta a lo sumo una vez, así que f solo toma valores 0 … 26.
- **Para una letra solo importan inicios con coste decreciente.** Sean
  inicios l₁ < l₂ con la misma letra c y f(l₁) ≤ f(l₂), y un bloque
  [l₂, e] con borde de longitud L hallado en p. Si L = 1, s[p] = c y
  [l₁, p] es un bloque con borde c que ya llega a e con coste f(l₁). Si
  L ≥ 2, el bloque [l₁, l₂] da f(l₂ + 1) ≤ f(l₁), y [l₂ + 1, e] tiene el
  borde de longitud L − 1 hallado en p + 1. Repetir el argumento con el
  borde más corto termina en L = 1, así que l₂ nunca hace falta.

Por eso cada letra guarda una pila de inicios cuyo coste baja
estrictamente, como mucho 27. En la posición p la solución recorre la
pila de s[p] desde el inicio más nuevo, pide LCP(l, p) al arreglo de
sufijos con un mínimo de rango sobre el arreglo LCP (una tabla dispersa
en Python, un árbol de segmentos en los demás lenguajes) y registra, para cada coste k, el final
más lejano que alcanza un bloque de coste k. Un inicio más antiguo solo
ayuda si su LCP es más largo, porque su coste es mayor. Luego f(p + 1)
es el menor coste cuyo final registrado cubre p, o f(p) + 1.

En el tercer ejemplo los bloques aba y cdc levantan las seis runas.

Trampa (prueba 32): un inicio posterior de menor coste no debe sustituir
a uno anterior de la misma letra; el anterior puede tener un borde útil más largo.

En C++, Go, Java y Rust, la ordenación por conteo de pares de rangos
construye el arreglo de sufijos en O(N log N), y el árbol de segmentos
se construye en O(N). El recorrido hace como mucho 27 consultas LCP por
posición, cada una en O(log N), por lo que añade O(27 N log N); el total
es O(N log N) tiempo y O(N) espacio.
Python usa ordenación por comparaciones durante O(log N) rondas de
duplicación, lo que da una cota de O(N log² N) tiempo para el arreglo de
sufijos. Su tabla dispersa se construye en O(N log N) tiempo y espacio
y responde cada consulta LCP en O(1), así que el recorrido añade O(27 N).
La cota total es O(N log² N) tiempo y O(N log N) espacio.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2168_dp_strings.cpp](2168_dp_strings.cpp) | G++ 13.2 x64 | dp, strings | O(N log N) | AC | 0.062 s | 4128 KB |
| [2168_dp_strings.go](2168_dp_strings.go) | Go 1.14 x64 | dp, strings | O(N log N) | AC | 0.109 s | 10720 KB |
| [2168_dp_strings.java](2168_dp_strings.java) | Java 1.8 | dp, strings | O(N log N) | AC | 0.218 s | 4992 KB |
| [2168_dp_strings.py](2168_dp_strings.py) | PyPy 3.10 x64 | dp, strings | O(N log² N) | AC | 0.968 s | 34932 KB |
| [2168_dp_strings.rs](2168_dp_strings.rs) | Rust 1.75 x64 | dp, strings | O(N log N) | AC | 0.093 s | 5604 KB |
