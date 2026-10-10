# 1162. ¿Puede una cadena de cambios de divisas con comisiones aumentar el dinero?

[Timus 1162](https://acm.timus.ru/problem.aspx?space=1&num=1162) · dificultad 197 · shortest_paths

Problema original de Nick Durov, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N ≤ 100` divisas y `M ≤ 100` casas de cambio, cada una entre dos
divisas en ambos sentidos con su propio tipo y comisión por sentido:
cambiar `x` da `(x − comisión)·tipo`, y la cantidad nunca puede ser
negativa. Empezando con `V` unidades de la divisa `S`, decide si alguna
secuencia de cambios termina en la divisa `S` con más de `V`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`, `M`, `S` y `V`, y luego `M` líneas con dos divisas y el tipo y la
comisión en cada sentido.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2 1 10.0
1 2 1.0 1.0 1.0 1.0
2 3 1.1 1.0 1.1 1.0
```

Salida:

```
NO
```

### Ejemplo 2

Entrada:

```
3 2 1 20.0
1 2 1.0 1.0 1.0 1.0
2 3 1.1 1.0 1.1 1.0
```

Salida:

```
YES
```

## Solución

Las divisas son vértices y cada sentido de una casa de cambio es una
arista. Sea `best[c]` la mayor cantidad de la divisa `c` que se puede
tener, empezando con `best[S] = V`. La relajación de Bellman–Ford
`best[b] = max(best[b], (best[a] − comisión)·tipo)`, permitida solo cuando
`best[a] ≥ comisión`, mejora esas cantidades pasada tras pasada. Cada paso
es creciente en la cantidad, así que tener más dinero nunca es peor.

Si ningún ciclo da ganancia, las mejores cantidades se alcanzan por
caminos simples, que tienen como mucho `N − 1` cambios, y para entonces
las pasadas dejan de cambiar. Así que si una pasada sigue cambiando algo
tras `N` pasadas, hay un ciclo con ganancia alcanzable; recorriéndolo una
y otra vez cualquier comisión se vuelve despreciable, y el camino de vuelta
a `S` existe porque cada casa funciona en ambos sentidos, así que la
respuesta es `YES`. También es `YES` en cuanto `best[S]` supera `V`. Si no,
es `NO`. `O(N·M)`.

Detalles a tener en cuenta:

- la comisión se cobra primero, en la divisa de origen, y no se puede
  cambiar una cantidad menor que la comisión;
- una ganancia puede necesitar un desvío por un ciclo lejos de `S`;
- los doubles se comparan con una pequeña tolerancia, para que el ruido
  de redondeo no parezca una ganancia.

Las respuestas se compararon en todas las pruebas y en 150 entradas
aleatorias con la misma relajación en fracciones exactas, ejecutada diez
veces más pasadas.

## Notas por lenguaje

- Todos los lenguajes hacen las mismas pasadas sobre la misma lista de
  cambios dirigidos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1162_shortest_paths.cpp](1162_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(N·M) | AC | 0.015 s | 212 KB |
| [1162_shortest_paths.go](1162_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(N·M) | AC | 0.015 s | 1120 KB |
| [1162_shortest_paths.java](1162_shortest_paths.java) | Java 1.8 | shortest_paths | O(N·M) | AC | 0.093 s | 752 KB |
| [1162_shortest_paths.py](1162_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(N·M) | AC | 0.093 s | 592 KB |
| [1162_shortest_paths.rs](1162_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(N·M) | AC | 0.031 s | 264 KB |
