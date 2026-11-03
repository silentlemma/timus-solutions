# 1501. Sentido de la belleza

[Timus 1501](https://acm.timus.ru/problem.aspx?space=1&num=1501) · dificultad 268 · dp

Problema original de Leonid Volkov y Stanislav Vasiliev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos montones de N cartas cada uno (4 ≤ N ≤ 1000) tienen en total N
cartas rojas y N negras. El crupier toma una y otra vez la carta de
arriba de uno de los montones y la pone en un montón rojo o negro, hasta
pasar todas las cartas. En todo momento los montones rojo y negro pueden
diferir en una carta como mucho. Hay que escribir de qué montón se toma
cada carta, como 2N cifras 1 y 2, o «Impossible».

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego los dos montones de arriba abajo, 1 para roja y 0 para negra.

## Salida

Las 2N cifras o «Impossible». Se acepta cualquier orden válido.

## Evaluación

Se acepta cualquier intercalación que mantenga el orden de ambas cadenas y el balance en cada prefijo.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0011
0110
```

Salida:

```
22121112
```

### Ejemplo 2

Entrada:

```
4
1100
1100
```

Salida:

```
Impossible
```

## Solución

Un momento se describe con los números i y j de cartas tomadas de los
dos montones. Con d = 2 · (cartas rojas) − (cartas) sobre la parte
tomada de cada montón, los montones rojo y negro difieren en
d1[i] + d2[j], así que el estado es válido cuando eso vale −1, 0 o 1.
Un estado es alcanzable si es válido y lo es el estado de encima o el
de la izquierda; (0, 0) es el inicio. Si (N, N) es alcanzable, se
vuelve desde él tomando cualquier predecesor alcanzable y se leen los
movimientos al revés. `O(N²)`.

Detalles a tener en cuenta:

- la condición rige tras cada movimiento, no solo al final (prueba 02,
  gen4);
- puede haber muchos órdenes correctos, así que las pruebas usan un
  comprobador (todas las pruebas);
- con el límite de 0,5 segundos la tabla de N² estados debe ser barata;
  la solución en Python guarda cada fila como una máscara entera y
  extiende la alcanzabilidad por los tramos de estados válidos con una
  sola suma.

## Soluciones optimizadas

Se conserva la DP de la rejilla de balances y se reconstruye por división y conquista. En una fila intermedia se calculan las fronteras alcanzables hacia delante y hacia atrás, y se recurre por una columna común. Cada parte conecta extremos alcanzables respetando el balance. Se reutilizan los búferes de frontera en vez de guardar la matriz. Un subproblema de una fila elige explícitamente la arista vertical de unión para reducir siempre la recursión.

- `1501_dp_optimized.cpp`: 0.015 s / 116 KB; base `1501_dp.cpp`: 0.015 s / 856 KB; cambio respecto a la base: tiempo -0.0%, memoria -86.4%.
- `1501_dp_optimized.go`: 0.015 s / 916 KB; base `1501_dp.go`: 0.031 s / 2216 KB; cambio respecto a la base: tiempo -51.6%, memoria -58.7%.
- `1501_dp_optimized.java`: 0.125 s / 456 KB; base `1501_dp.java`: 0.109 s / 2704 KB; cambio respecto a la base: tiempo +14.7%, memoria -83.1%.
- `1501_dp_optimized.rs`: 0.046 s / 196 KB; base `1501_dp.rs`: 0.031 s / 1164 KB; cambio respecto a la base: tiempo +48.4%, memoria -83.2%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1501_dp.cpp`; versión que cubre `1501_dp_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 61/61.

- Go: base didáctica preferida `1501_dp.go`; versión que cubre `1501_dp.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1501_dp.java`; versión que cubre `1501_dp_optimized.java`; puestos tiempo/memoria 3/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1501_dp.py`; versión que cubre `1501_dp.py`; puestos tiempo/memoria 1/1, registros de otros autores 7/7.

- Rust: base didáctica preferida `1501_dp.rs`; versión que cubre `1501_dp.rs`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1501_dp.cpp](1501_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 856 KB | 11287253 |
| [1501_dp.go](1501_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.031 s | 2216 KB | 11287254 |
| [1501_dp.java](1501_dp.java) | Java 1.8 | dp | O(N^2) | AC | 0.109 s | 2704 KB | 11287256 |
| [1501_dp.py](1501_dp.py) | Python 3.12 x64 | dp | O(N^2) | AC | 0.093 s | 836 KB | 11287255 |
| [1501_dp.rs](1501_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.031 s | 1164 KB | 11287257 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1501_dp_optimized.cpp](1501_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 116 KB | 11309287 |
| [1501_dp_optimized.go](1501_dp_optimized.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.015 s | 916 KB | 11309289 |
| [1501_dp_optimized.java](1501_dp_optimized.java) \* | Java 1.8 | dp | O(N^2) | AC | 0.125 s | 456 KB | 11309288 |
| [1501_dp_optimized.rs](1501_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(N^2) | AC | 0.046 s | 196 KB | 11309290 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
