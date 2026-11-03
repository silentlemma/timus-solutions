# 1205. La forma más rápida de cruzar la ciudad a pie y en metro

[Timus 1205](https://acm.timus.ru/problem.aspx?space=1&num=1205) · dificultad 234 · graphs

Problema original de Alexander Klepinin, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se puede caminar a cualquier sitio a una velocidad o ir en metro a una
velocidad no menor, entre `2 ≤ N ≤ 200` estaciones unidas por hasta 400
tramos rectos de doble sentido; solo se sube, se baja y se cambia de
tren en las estaciones, sin coste de tiempo. Hay que hallar el camino
más rápido del punto A al punto B y las estaciones por las que pasa.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las velocidades a pie y en metro; `N` y las coordenadas de las
estaciones; los tramos como pares de números de estación, terminados en
`0 0`; y luego A y B.

## Salida

El menor tiempo, con precisión `10⁻⁶`, y luego el número de estaciones
de la ruta seguido de las estaciones en el orden en que se visitan.

## Evaluación

El verificador comprueba óptimo y ruta/pareja válida, sin exigir salida literal.

- `1205_graphs_optimized.java` (Java 1.8): 13 pruebas del repositorio; 77 comparaciones adicionales de fuente exacta.

- `1205_graphs_optimized.py` (PyPy 3.10 x64): 13 pruebas del repositorio.

- `1205_graphs_optimized.rs` (Rust 1.75 x64): 13 pruebas del repositorio; 77 comparaciones adicionales de fuente exacta.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 100
4
0 0
1 0
9 0
9 9
1 2
1 3
2 4
0 0
10 10
10 0
```

Salida:

```
2.6346295
4 4 2 1 3
```

## Solución

Se forma un grafo completo sobre las estaciones, A y B: entre dos puntos
cualesquiera el coste es el tiempo a pie, salvo entre estaciones unidas,
donde es el tiempo en tren; por la misma recta el tren nunca es más
lento. El algoritmo de Dijkstra sobre este grafo denso de `N + 2` nodos,
eligiendo el siguiente nodo con un recorrido lineal, da el menor tiempo,
y los predecesores dan la ruta; sus estaciones son la ruta sin A ni B.
`O(N²)`.

Detalles a tener en cuenta:

- la ruta puede estar vacía: con velocidades iguales, o cuando el metro
  no ayuda, la respuesta es ir a pie en línea recta e imprimir `0`
  estaciones;
- caminar entre dos estaciones está permitido y puede formar parte de la
  mejor ruta, por ejemplo para cambiar a una línea cercana;
- la lista de tramos puede estar vacía, con `0 0` justo después de las
  estaciones.

Las rutas se compararon con una solución escrita aparte en 200 ciudades
aleatorias y en todas las pruebas, con el verificador en ambos sentidos.

## Soluciones optimizadas

Se conservan los caminos mínimos matriciales claros. Las variantes compactas ejecutan Dijkstra denso sobre el grafo geométrico completo implícito: calculan tiempo con hypot al relajar y guardan predecesores con IDs originales. La pertenencia al metro usa bits, sin matriz real de tiempos. Una estación sin enlace ferroviario se omite: reemplazar dos tramos a pie por el directo no aumenta tiempo por desigualdad triangular. Solo quedan extremos y estaciones con enlace. Pesos no negativos justifican fijar el mínimo no visitado. Igual velocidad, ausencia de metro o extremos coincidentes permiten caminar directamente. Con K activos, tiempo O(N+M+K²), O(N²)bits y O(N)estado numérico. Se conservan hypot robusto y etiquetas; el verificador admite cualquier ruta mínima válida.

- `1205_graphs_optimized.java`: 0.093 s / 712 KB; base `1205_graphs.java`: 0.125 s / 1416 KB; cambio respecto a la base: tiempo -25.6%, memoria -49.7%.
- `1205_graphs_optimized.py`: 0.265 s / 636 KB; base `1205_graphs.py`: 0.062 s / 1012 KB; cambio respecto a la base: tiempo +327.4%, memoria -37.2%.
- `1205_graphs_optimized.rs`: 0.015 s / 208 KB; base `1205_graphs.rs`: 0.046 s / 344 KB; cambio respecto a la base: tiempo -67.4%, memoria -39.5%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1205_graphs.cpp`; fuente que cubre `1205_graphs.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 83/83.

- Go: base didáctica preferida `1205_graphs.go`; fuente que cubre `1205_graphs.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1205_graphs.java`; fuente que cubre `1205_graphs_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1205_graphs.py`; fuente que cubre `1205_graphs_optimized.py`; puestos tiempo/memoria 36/1, registros de otros autores 36/36.

- Rust: base didáctica preferida `1205_graphs.rs`; fuente que cubre `1205_graphs_optimized.rs`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1205_graphs.cpp](1205_graphs.cpp) | G++ 13.2 x64 | graphs | O(N²) | AC | 0.015 s | 256 KB | 11283587 |
| [1205_graphs.go](1205_graphs.go) | Go 1.14 x64 | graphs | O(N²) | AC | 0.031 s | 1208 KB | 11283588 |
| [1205_graphs.java](1205_graphs.java) | Java 1.8 | graphs | O(N²) | AC | 0.125 s | 1416 KB | 11283593 |
| [1205_graphs.py](1205_graphs.py) | Python 3.12 x64 | graphs | O(N²) | AC | 0.062 s | 1012 KB | 11283591 |
| [1205_graphs.rs](1205_graphs.rs) | Rust 1.75 x64 | graphs | O(N²) | AC | 0.046 s | 344 KB | 11283594 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1205_graphs_optimized.java](1205_graphs_optimized.java) | Java 1.8 | graphs | O(N+M+K²) time; O(N²) bits + O(N) numbers | AC | 0.093 s | 712 KB | 11309389 |
| [1205_graphs_optimized.py](1205_graphs_optimized.py) \* | PyPy 3.10 x64 | graphs | O(N+M+K²) time; O(N²) bits + O(N) numbers | AC | 0.265 s | 636 KB | 11309737 |
| [1205_graphs_optimized.rs](1205_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(N+M+K²) time; O(N²) bits + O(N) numbers | AC | 0.015 s | 208 KB | 11309390 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
