# 1130. Elegir el sentido de cada vector para que el paseo termine a no más de √2·L del inicio

[Timus 1130](https://acm.timus.ru/problem.aspx?space=1&num=1130) · dificultad 937 · geometry, greedy

Problema original de Dmitry Filimonenkov, del sexto concurso universitario de programación de la Universidad Estatal de los Urales, 21 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un niño corre por turnos a lo largo de `N ≤ 10000` vectores enteros, cada
uno no más largo que `L ≤ 100`, y para cada uno la maestra decide si
corre a favor o en contra. Elige los sentidos de modo que el niño termine
a no más de `√2·L` del inicio. Imprime `YES` y la elección como una línea
de `+` y `-`, o `WRONG ANSWER` si ninguna elección sirve.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

`N`, luego `L` y luego `N` líneas con las dos coordenadas de un vector.

## Salida

`YES` y una línea de `N` signos, `+` para correr a favor del vector y `-`
para correr en contra; o `WRONG ANSWER`.

## Evaluación

Se acepta cualquier elección válida. El comprobador verifica la línea de
signos y compara exactamente el cuadrado de la distancia del punto final
con `2L²`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
5
5 0
0 5
0 0
-3 4
```

Salida:

```
YES
+--+
```

## Solución

Siempre existe una buena elección, así que la respuesta es siempre `YES`.
El hecho clave: entre tres vectores cualesquiera no más largos que `L`,
hay dos cuya suma o diferencia no es más larga que `L`. Las tres rectas
que los contienen dividen la media vuelta en tres ángulos, así que dos de
ellas forman como mucho 60°; tomando esos dos vectores con los signos que
los dejan a como mucho 60°, la diferencia tiene longitud al cuadrado
`a² + b² − 2ab·cos θ ≤ a² + b² − ab`, que es como mucho `max(a, b)² ≤ L²`.

Así que se guardan como mucho dos vectores libres. Cuando llega un
tercero, se busca un par y un signo que den un vector no más largo que
`L` y se sustituye el par por esa combinación. Al final quedan como mucho
dos vectores; se elige el signo que hace su producto escalar no positivo,
y el cuadrado de la longitud del resultado es como mucho `2L²`. Cada
combinación es un nodo de un bosque cuyos hijos guardan un signo
relativo; el signo final de un vector de entrada es el producto de los
signos relativos en su camino hasta la raíz. Cada nodo se crea después de
sus hijos, así que una pasada por los nodos en orden inverso fija los
signos. Toda la aritmética es entera. `O(N)`.

Detalles a tener en cuenta:

- `WRONG ANSWER` nunca es la respuesta;
- comparar cuadrados de longitudes lo mantiene todo exacto; no hacen
  falta raíces;
- cambiar el signo de un vector combinado cambia el de todos los vectores
  que contiene, y los signos relativos del bosque lo resuelven sin
  tocarlos;
- los vectores nulos y `L = 0` no necesitan un caso aparte.

Las respuestas se comprobaron con el comprobador en todas las pruebas y en
150 conjuntos aleatorios de vectores, entre ellos vectores cerca de tres
direcciones separadas 120°, donde el paso de fusión tiene menos margen.

## Notas por lenguaje

- Todos los lenguajes hacen la misma fusión con el mismo orden de
  búsqueda, así que sus respuestas son idénticas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1130_geometry.cpp](1130_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 528 KB |
| [1130_geometry.go](1130_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 2636 KB |
| [1130_geometry.java](1130_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.125 s | 2340 KB |
| [1130_geometry.py](1130_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.140 s | 3796 KB |
| [1130_geometry.rs](1130_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.046 s | 1864 KB |
