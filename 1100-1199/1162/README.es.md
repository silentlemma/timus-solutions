# 1162. ¿Puede una cadena de cambios de divisas con comisiones aumentar el dinero?

[Timus 1162](https://acm.timus.ru/problem.aspx?space=1&num=1162) · dificultad 185 · shortest_paths

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

`1 ≤ S ≤ N ≤ 100`, `1 ≤ M ≤ 100` y `0 ≤ V ≤ 1000`.
Los tipos están en `[0.01, 100]` y las comisiones en `[0, 100]`, ambos con
un máximo de dos decimales. Los decimales de `V` no están limitados.
Para cualquier secuencia que utilice cada casa de cambio como máximo una
vez, la razón entre la cantidad final y la inicial es menor que `10000`.

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

Las divisas son vértices y cada sentido de cambio es una arista.
Usamos Bellman–Ford con `best[c]` como la mayor cantidad alcanzable de la
divisa `c`. Al principio solo se alcanza `S`, con cantidad `V`. Cada pasada
lee el arreglo anterior y escribe uno nuevo: tras la pasada `k` se han
considerado recorridos de hasta `k` cambios. Se resta primero la comisión
y luego se multiplica por el tipo; se omiten los cambios que no se pueden pagar.

Usamos enteros exactos en lugar de coma flotante. Sea `P` el máximo entre
dos y el número de decimales de `V`; el denominador común inicial es
`D = 10^P`. Los tipos y las comisiones se almacenan multiplicados por 100.
Para un numerador `x`, un tipo `R` y una comisión `C`, el nuevo numerador
es `(x − C·(D/100))·R`, con denominador `100·D`. También multiplicamos por
100 las cantidades conservadas y la cantidad inicial, y actualizamos `D`.
Así todas las comparaciones de disponibilidad y mejora son exactas.

Si no hay ciclos alcanzables con ganancia, eliminar el tramo entre dos
visitas a un vértice no reduce el dinero. Bastan entonces caminos simples
de hasta `N − 1` cambios. Una mejora en la pasada `N` demuestra que hay un
ciclo alcanzable con ganancia. Con tipos positivos y comisiones no negativas,
su multiplicador supera uno y repetirlo aumenta el capital sin límite.
Como cada casa opera en ambos sentidos, finalmente se puede pagar el
regreso a `S`. Respondemos `YES` en ese caso o cuando `best[S] > V`;
si una pasada no mejora nada, respondemos `NO`.

Hay `O(N·M)` relajaciones y se copian `O(N²)` elementos de los arreglos.
Los enteros tienen `O(P+N)` dígitos, por lo que la aritmética exacta requiere
`O(N·(N+M)·(P+N))` tiempo y `O(N·(P+N)+M)` espacio.

Detalles a tener en cuenta:

- se cobra primero la comisión en la divisa de origen; cero es una cantidad
  válida y debe distinguirse de una divisa inalcanzable;
- obtener beneficio puede requerir un ciclo lejos de `S`;
- en la prueba **08**, `0.000000001` se duplica: una tolerancia absoluta
  oculta la ganancia, mientras que quitarla en cálculos de coma flotante
  puede confundir redondeo con beneficio. Hay que leer `V` exactamente,
  sin redondearlo a dos decimales.

Se verificaron las 8 pruebas guardadas, 101 casos del generador, 2500
entradas aleatorias mediante enumeración exhaustiva de caminos simples
y ciclos con fracciones exactas, y 600 casos de equilibrio o márgenes mínimos.

## Notas por lenguaje

- Todos los lenguajes hacen las mismas pasadas sobre la misma lista de
  cambios dirigidos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1162_shortest_paths.cpp](1162_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(N·(N+M)·(P+N)) | AC | 0.031 s | 700 KB |
| [1162_shortest_paths.go](1162_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(N·(N+M)·(P+N)) | AC | 0.015 s | 5444 KB |
| [1162_shortest_paths.java](1162_shortest_paths.java) | Java 1.8 | shortest_paths | O(N·(N+M)·(P+N)) | AC | 0.109 s | 4980 KB |
| [1162_shortest_paths.py](1162_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(N·(N+M)·(P+N)) | AC | 0.093 s | 740 KB |
| [1162_shortest_paths.rs](1162_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(N·(N+M)·(P+N)) | AC | 0.031 s | 312 KB |
