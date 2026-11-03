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

- `1874_geometry_optimized.java` (Java 1.8): 13 pruebas del repositorio.

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

Se conserva la fórmula geométrica (a*a+b*b+2*sqrt(2)*a*b)/4 y las bases claras. Java reduce costes de lectura/formato. Go y Python calculan el resultado y lo redondean una vez a seis decimales mediante un entero escalado por 10^6; no hay tabla de respuestas. Para a, b <= 10000 el valor escalado es menor que 2^47: error real más medio micro de redondeo queda por debajo de 10^-6 absoluto. La fracción se emite con seis posiciones y ceros iniciales. Solo cambia la representación/E/S; tiempo y espacio O(1).

- `1874_geometry_optimized.go`: 0.031 s / 304 KB; base `1874_geometry.go`: 0.031 s / 1136 KB; cambio respecto a la base: tiempo -0.0%, memoria -73.2%.
- `1874_geometry_optimized.java`: 0.109 s / 544 KB; base `1874_geometry.java`: 0.140 s / 1832 KB; cambio respecto a la base: tiempo -22.1%, memoria -70.3%.
- `1874_geometry_optimized.py`: 0.140 s / 316 KB; base `1874_geometry.py`: 0.078 s / 452 KB; cambio respecto a la base: tiempo +79.5%, memoria -30.1%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1874_geometry.cpp`; fuente que cubre `1874_geometry.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 68/68.

- Go: base didáctica preferida `1874_geometry.go`; fuente que cubre `1874_geometry_optimized.go`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Java: base didáctica preferida `1874_geometry.java`; fuente que cubre `1874_geometry_optimized.java`; puestos tiempo/memoria 2/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1874_geometry.py`; fuente que cubre `1874_geometry_optimized.py`; puestos tiempo/memoria 13/1, registros de otros autores 16/16.

- Rust: base didáctica preferida `1874_geometry.rs`; fuente que cubre `1874_geometry.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

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
| [1874_geometry_optimized.java](1874_geometry_optimized.java) \* | Java 1.8 | geometry | O(1) | AC | 0.109 s | 544 KB | 11308337 |
| [1874_geometry_optimized.py](1874_geometry_optimized.py) \* | PyPy 3.10 x64 | geometry | O(1) | AC | 0.140 s | 316 KB | 11309748 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
