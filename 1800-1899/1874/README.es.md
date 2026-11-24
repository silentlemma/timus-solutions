# 1874. Portería de fútbol

[Timus 1874](https://acm.timus.ru/problem.aspx?space=1&num=1874) · dificultad 199 · geometry

Problema original de Fedor Fominykh, del Concurso Regional de Programación por Equipos de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una portería se construye con un abedul vertical, el suelo y dos palos
de longitudes a y b: el abedul es un poste, y los palos forman el otro
poste y el larguero. La portería puede ser cualquier cuadrilátero. Hay
que hallar su mayor área. El abedul es más alto que a + b.

## Entrada

a y b (1 ≤ a, b ≤ 10 000).

## Salida

La mayor área, con al menos seis cifras tras el punto decimal.

## Evaluación

Se compara el valor numérico con la tolerancia indicada y las cotas de redondeo demostradas abajo.

- `1874_geometry_optimized.go` (Go 1.14 x64): 13 pruebas del repositorio; 13 comparaciones adicionales de fuente exacta.

- `1874_geometry_optimized.java` (Java 1.8). Los 13 casos del repositorio y otros 30 casos se ejecutaron en procesos Java independientes. Otras 40 292 llamadas comprobaron los seis decimales y el área frente a una referencia de alta precisión, incluso con lecturas fragmentadas.

- `1874_geometry_optimized.py` (PyPy 3.10 x64): 13 pruebas del repositorio; 204 comparaciones adicionales de fuente exacta.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2
```

Salida:

```
4.828427125
```

## Solución

El cuadrilátero tiene un ángulo recto donde el abedul toca el suelo. Su
diagonal c, del punto alto del abedul al extremo lejano en el suelo, lo
divide en dos. Una parte es un triángulo rectángulo de hipotenusa c,
cuya área es como mucho c²/4, alcanzada con catetos iguales. La otra es
el triángulo de los dos palos con ángulo t entre ellos. Entonces
c² = a² + b² − 2ab·cos t, y el total es
(a² + b² − 2ab·cos t)/4 + ab·sin t/2. Su derivada se anula cuando
sin t + cos t = 0, es decir t = 135°, y el área es
(a² + b² + 2√2·ab)/4. `O(1)`.

Para a = b = 2 da (4 + 4 + 8√2)/4 = 2 + 2√2 ≈ 4.828427125.

Trampas:

- la portería no tiene por qué ser un rectángulo; lo único fijo es el
  ángulo recto al pie del abedul;
- el ángulo entre los palos es 135°, no 90°: un ángulo recto solo da
  (a + b)²/4;
- el enunciado garantiza que el abedul es lo bastante alto, así que su
  altura nunca limita la respuesta.

La fórmula coincide con una búsqueda directa sobre el ángulo entre los
palos y con una implementación aceptada independiente en todas las
pruebas.

## Soluciones optimizadas

Se conserva la fórmula geométrica (a*a+b*b+2*sqrt(2)*a*b)/4 y las bases claras. Java lee los dos enteros positivos por bloques y reutiliza el búfer de 32 bytes para escribir seis decimales. Calcula exactamente el término cuadrático en millonésimas y redondea una sola vez el término que contiene el producto de las longitudes. El error absoluto es inferior a 0,000000522 en todo el intervalo permitido. Go y Python calculan el resultado y lo redondean una vez a seis decimales mediante un entero escalado por 10^6; no hay tabla de respuestas. Para a, b <= 10000 el valor escalado es menor que 2^47: error real más medio micro de redondeo queda por debajo de 10^-6 absoluto. La fracción se emite con seis posiciones y ceros iniciales. Solo cambia la representación/E/S; tiempo y espacio O(1).

- `1874_geometry_optimized.go`: 0.031 s / 304 KB; base `1874_geometry.go`: 0.031 s / 1136 KB; cambio respecto a la base: tiempo -0.0%, memoria -73.2%.
- `1874_geometry_optimized.java`. La versión sencilla de Java obtuvo 0,140 s y 1832 KB en el envío #11290975. La versión optimizada anterior obtuvo 0,109 s y 544 KB en el envío #11308337. El nuevo envío #11328166 obtuvo 0,093 s y 344 KB.
- `1874_geometry_optimized.py`: 0.140 s / 316 KB; base `1874_geometry.py`: 0.078 s / 452 KB; cambio respecto a la base: tiempo +79.5%, memoria -30.1%.

`1874_geometry_optimized.rs`. Mantiene la misma fórmula cerrada del área en f64 e imprime nueve decimales directamente con printf. La optimización cambia la representación de entrada y salida, conservando la fórmula geométrica y su tipo de precisión. Tiempo y espacio auxiliar siguen siendo O(1). Rust usa el entorno de C para entrada y salida, evitando cadenas String completas decodificadas y el formato de Rust. La fuente sencilla aceptada se conserva sin cambios.

Frente a `1874_geometry.rs`: tiempo 0.031 s → 0.046 s; memoria 236 KB → 112 KB.

## Notas por lenguaje

En la muestra de Java 1.8 del 1 de noviembre de 2026, el envío ocupa el puesto 2/61 en tiempo y el 1/61 en memoria. Con menos de 1 MiB, el puesto en tiempo cumple el criterio estricto.

Los resultados de Rust se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1874_geometry_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1874_geometry.cpp](1874_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 132 KB | 11309209 |
| [1874_geometry.go](1874_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1136 KB | 11290968 |
| [1874_geometry.java](1874_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1832 KB | 11290975 |
| [1874_geometry.py](1874_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 452 KB | 11290970 |
| [1874_geometry.rs](1874_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 236 KB | 11309210 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1874_geometry_optimized.go](1874_geometry_optimized.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 304 KB | 11309758 |
| [1874_geometry_optimized.java](1874_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 344 KB | 11328166 |
| [1874_geometry_optimized.py](1874_geometry_optimized.py) \* | PyPy 3.10 x64 | geometry | O(1) | AC | 0.140 s | 316 KB | 11309748 |
| [1874_geometry_optimized.rs](1874_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 112 KB | 11325114 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
