# 2197. El prefijo repetido más corto de una cadena bajo sobrescrituras de bloques

[Timus 2197](https://acm.timus.ru/problem.aspx?space=1&num=2197) · dificultad 2200 · hashing, fenwick

Problema original de Konstantin Rychkov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cadena S de longitud N se imprime como varias copias de uno de sus
prefijos, e imprimir una vez un prefijo de longitud l cuesta l²
segundos. Q veces un patrón t_k de un conjunto fijo sobrescribe S desde
la posición p. Imprimir el menor tiempo de impresión para la cadena
inicial y tras cada sobrescritura. Los límites son 3 segundos y 256 MB.

## Entrada

N, M y Q, 1 ≤ N ≤ 2 · 10⁵, 0 ≤ M, Q ≤ 2 · 10⁵, luego S, luego los M
patrones de longitud total hasta 10⁶, y luego las sobrescrituras p k.

## Salida

Q + 1 tiempos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3 3
abab
be
ebb
ee
3 1
1 2
2 3
```

Salida:

```
8
16
16
4
```

## Solución

Imprimir N / l copias de un prefijo de longitud l cuesta N · l segundos,
así que se busca la menor l que divide a N y genera S.

Las longitudes que dividen a N y generan S son cerradas bajo el mcd, así
que la menor divide a todas las demás. Empezando en l = N, la solución
intenta dividir l por cada factor primo de N mientras el prefijo más
corto siga generando S; lo que queda es el periodo más corto. Un prefijo
de longitud c genera S exactamente cuando el hash de S es igual al hash
del prefijo repetido N / c veces, una suma geométrica
h(prefix) · (B^N − 1) / (B^c − 1), comparada tras multiplicar por el
denominador. Dos módulos hacen despreciables las colisiones.

Lo difícil es calcular el hash de una cadena que cambia con
sobrescrituras largas. Todo el texto que puede aparecer, S y cada
patrón, se pone en una cadena fuente con hashes de prefijo. La S actual
es una lista de fragmentos, cada uno apuntando a un trozo de la fuente,
y cada fragmento guarda su hash ya desplazado a su posición en S, en un
árbol de Fenwick según la posición de inicio. Una sobrescritura corta
los fragmentos en sus dos extremos, quita los de dentro y añade un
fragmento para el patrón, así que cada sobrescritura crea solo un número
constante de fragmentos. El hash de un prefijo es una suma de prefijo de
Fenwick sobre fragmentos completos más el hash de la parte del último
fragmento, leído de la fuente. Las respuestas además se guardan por el
hash de la cadena entera.

En el ejemplo "abab" tiene periodo 2, así que el tiempo es 4 · 2 = 8, y
"eeee" tiene periodo 1, así que es 4.

Cada consulta cuesta O(log N) por factor primo de N, y las
sobrescrituras O(log N) por fragmento creado o eliminado.

## Notas por lenguaje

- Python se ejecuta con PyPy y se acepta en 2.593 s de los 3 s. Además
  descarta los períodos cuyo número de copias no divide la suma de los
  códigos de los caracteres, porque repetir un prefijo repite esa suma.
  Con CPython 3.12 los tests más grandes de aquí ya tardan unos 2.7 s,
  así que no se usa.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2197_hashing_fenwick.cpp](2197_hashing_fenwick.cpp) | G++ 13.2 x64 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 0.375 s | 32896 KB |
| [2197_hashing_fenwick.go](2197_hashing_fenwick.go) | Go 1.14 x64 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 0.468 s | 65604 KB |
| [2197_hashing_fenwick.java](2197_hashing_fenwick.java) | Java 1.8 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 1.250 s | 71216 KB |
| [2197_hashing_fenwick.py](2197_hashing_fenwick.py) | PyPy 3.10 x64 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 2.593 s | 94140 KB |
| [2197_hashing_fenwick.rs](2197_hashing_fenwick.rs) | Rust 1.75 x64 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 0.328 s | 45500 KB |
