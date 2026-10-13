# 1463. ¡Alegría para la gente!

[Timus 1463](https://acm.timus.ru/problem.aspx?space=1&num=1463) · dificultad 598 · dp

Problema original de Alexander Toropov, con agradecimiento especial a Alexander Ipatov, del concurso de la Universidad Estatal de los Urales en el campus de invierno de Petrozavodsk, enero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N ciudades (1 ≤ N ≤ 50000) que dan una alegría A[i] al visitarlas,
y K enlaces entre pares de ciudades que dan una alegría c al volar por
ellos, todos enteros no negativos hasta 10000. Entre dos ciudades hay
como mucho una ruta, así que los enlaces forman un bosque. Hay que
hallar una ruta por ciudades distintas, empezando donde sea, con la
mayor alegría total de sus ciudades y vuelos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y K, luego las alegrías A[i] y después K líneas a, b, c.

## Salida

La mayor alegría, el número de ciudades de la ruta y la ruta. Se acepta
cualquier ruta óptima.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 1
1 1
1 2 1
```

Salida:

```
3
2
1 2
```

### Ejemplo 2

Entrada:

```
8 7
1 5 4 6 10 1 2 2
1 2 1
2 3 10
2 4 1
4 5 1
4 6 2
6 7 2
6 8 3
```

Salida:

```
37
4
5 4 2 3
```

## Solución

Una ruta en un bosque es un camino dentro de un árbol, y todo camino
tiene una ciudad más alta cuando su árbol se cuelga de una raíz. Se
enraíza cada árbol en cualquier ciudad y se procesan las ciudades desde
las hojas hacia arriba. Para cada ciudad v se guarda la mejor ruta que
empieza en v y baja, down[v] = A[v] más el mejor valor de c + down[w]
entre sus hijos w, junto con el hijo que lo da. La mejor ruta cuya
ciudad más alta es v une a A[v] los dos mejores de esos valores; todos
los valores son no negativos, así que tomar dos hijos (o uno, o
ninguno) nunca empeora. La ruta se reconstruye bajando por los hijos
guardados por las dos ramas elegidas.

Los árboles pueden tener 50000 ciudades de profundidad, así que el
recorrido usa una pila explícita en lugar de recursión. `O(N + K)`.

Detalles a tener en cuenta:

- puede no haber ningún enlace, y la mejor ruta puede ser una sola
  ciudad (pruebas 03, 04, 07, gen5);
- una cadena larga desborda la recursión (gen2);
- con alegrías nulas cualquier ruta es óptima (prueba 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1463_dp.cpp](1463_dp.cpp) | G++ 13.2 x64 | dp | O(N + K) | AC | 0.125 s | 5364 KB |
| [1463_dp.go](1463_dp.go) | Go 1.14 x64 | dp | O(N + K) | AC | 0.109 s | 11948 KB |
| [1463_dp.java](1463_dp.java) | Java 1.8 | dp | O(N + K) | AC | 0.140 s | 3888 KB |
| [1463_dp.py](1463_dp.py) | Python 3.12 x64 | dp | O(N + K) | AC | 0.265 s | 35104 KB |
| [1463_dp.rs](1463_dp.rs) | Rust 1.75 x64 | dp | O(N + K) | AC | 0.031 s | 10112 KB |
