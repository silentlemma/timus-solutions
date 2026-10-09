# 1103. Una circunferencia por tres lápices que divide al resto por la mitad

[Timus 1103](https://acm.timus.ru/problem.aspx?space=1&num=1103) · dificultad 503 · geometry

Problema original de Katya Ovechkina, del Tetrahedron Team Contest, mayo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` lápices en puntos enteros (`N` impar, `3 ≤ N ≤ 5000`, coordenadas
de valor absoluto como mucho `10^8`). No hay tres en una recta ni cuatro
en una circunferencia. Elige tres lápices de modo que la circunferencia
que pasa por ellos deje dentro exactamente `(N − 3) / 2` de los demás
lápices y el mismo número fuera. Si no existe tal circunferencia, imprime
`No solution`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas `x y`.

## Salida

Las coordenadas de los tres lápices, un lápiz por línea.

## Evaluación

Se acepta cualquier circunferencia válida. El comprobador verifica que
los tres puntos son lápices distintos y cuenta los lápices de dentro y de
fuera con un determinante entero exacto.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
0 0
1 0
2 -1
2 1
1 1
0 2
-3 -1
```

Salida:

```
-3 -1
2 -1
1 1
```

## Solución

Siempre hay solución. Toma `A`, el lápiz más bajo (el de más a la
izquierda entre los más bajos), y `B`, su vecino en la envolvente
convexa, elegido de modo que todos los demás lápices queden a la
izquierda de la recta `AB`. Entonces toda circunferencia por `A` y `B`
corta ese semiplano de la misma forma: un lápiz `P` está dentro de la
circunferencia por `A`, `B` y `C` exactamente cuando ve el segmento `AB`
bajo un ángulo mayor que `C`. Todos los ángulos `APB` son menores de 180°
y, como no hay cuatro lápices en una circunferencia, todos distintos.
Ordena los otros `N − 2` lápices por ese ángulo y toma el del medio como
`C`: `(N − 3) / 2` lápices ven `AB` bajo un ángulo mayor y quedan dentro,
y otros tantos bajo uno menor y quedan fuera. `O(N log N)`.

Los ángulos se comparan sin coma flotante. La cotangente del ángulo es
`dot / cross`, donde `dot = (A − P)·(B − P)` y `cross` es el área
orientada de `P`, `A`, `B`, positiva para todo `P`. A mayor ángulo,
menor cotangente, así que `P` va antes que `Q` cuando
`dot_P · cross_Q > dot_Q · cross_P`.

Detalles a tener en cuenta:

- las coordenadas llegan a `10^8`, así que `dot` y `cross` llegan a unos
  `8 · 10^16` y sus productos a unos `6 · 10^33`, mucho más de 64 bits;
- comparar ángulos con `atan2` es arriesgado: dos lápices lejanos pueden
  ver `AB` bajo ángulos que difieren menos que el error de redondeo;
- `B` tiene que ser vecino de `A` en la envolvente; con un segundo punto
  cualquiera, los lápices a ambos lados de `AB` no se ordenan por un solo
  ángulo.

Las respuestas se comprobaron con un determinante exacto de punto en
circunferencia en todas las pruebas, incluidos conjuntos aleatorios de
miles de lápices en todo el rango de coordenadas.

## Notas por lenguaje

- C++ y Rust comparan los productos en enteros de 128 bits y eligen el
  elemento central con `nth_element` y `select_nth_unstable_by`.
- Go y Java no tienen un tipo de 128 bits en estas versiones y comparan
  los productos como enteros grandes al ordenar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1103_geometry.cpp](1103_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 444 KB |
| [1103_geometry.go](1103_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 2628 KB |
| [1103_geometry.java](1103_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 7336 KB |
| [1103_geometry.py](1103_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.171 s | 1548 KB |
| [1103_geometry.rs](1103_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 1160 KB |
