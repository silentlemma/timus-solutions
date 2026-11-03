# 1049. La última cifra del número de divisores de un producto

[Timus 1049](https://acm.timus.ru/problem.aspx?space=1&num=1049) · dificultad 249 · number_theory

Problema original de Stanislav Vasiliev, del concurso universitario de programación de la Universidad Estatal de los Urales, 25 de marzo de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan diez enteros `a1 … a10`, cada uno de 1 a 10000. Halla la última
cifra del número de divisores positivos del producto `a1 · … · a10`.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Diez enteros, uno por línea.

## Salida

Una cifra: la última cifra del número de divisores.

## Evaluación

Se comparan los tokens exactos; los espacios no afectan.

- `1049_number_theory_optimized.go` (Go 1.14 x64): 14 pruebas del repositorio; 14 comparaciones adicionales de fuente exacta.

- `1049_number_theory_optimized.java` (Java 1.8): 14 pruebas del repositorio; 172 comparaciones adicionales de fuente exacta.

- `1049_number_theory_optimized.py` (PyPy 3.10 x64): 14 pruebas del repositorio.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
2
6
1
3
1
1
1
1
1
```

Salida:

```
9
```

### Ejemplo 2

Entrada:

```
1
1
1
1
1
1
1
1
1
1
```

Salida:

```
1
```

## Solución

Si `P = p1^e1 · p2^e2 · … · pk^ek`, un divisor de `P` elige cada
exponente de forma independiente entre `0` y `ei`, así que `P` tiene
`(e1 + 1)(e2 + 1)…(ek + 1)` divisores.

El producto puede tener 40 cifras, pero no hace falta: se factoriza cada
número por división de prueba hasta su raíz cuadrada (como mucho 100
pasos), se suman los exponentes de los primos iguales y se multiplican los
`(e + 1)` módulo 10. `O(10 · √10000)`.

Detalles a tener en cuenta:

- los exponentes deben sumarse sobre los diez números antes del `+ 1`:
  `2 · 2` tiene 3 divisores, no `2 · 2`;
- un factor primo mayor que la raíz cuadrada queda tras la división de
  prueba y también cuenta;
- la última cifra puede ser 0 (48 = `2^4 · 3` tiene 10 divisores).

## Soluciones optimizadas

La fórmula no cambia: factorizar los diez valores, sumar exponentes y multiplicar exponente+1 módulo diez. Se retira toda la potencia de dos y luego solo se prueban divisores impares; el residuo mayor que uno es primo. Go usa exponentes uint8 y una lista de primos tocados; Java, char de 16 bits sin cajas. El máximo 10*floor(log2(10000))=130 cabe en uint8, pero no en byte Java con signo. Seis primos distintos ya multiplican 30030: cada entrada aporta como máximo cinco. Los arreglos requieren O(V) inicialización/espacio y las diez factorizaciones O(C sqrt(V)). Python conserva un pequeño diccionario y operaciones de bits; el intercambio de tiempo por memoria se declara aparte.

- `1049_number_theory_optimized.go`: 0.015 s / 292 KB; base `1049_number_theory.go`: 0.031 s / 1108 KB; cambio respecto a la base: tiempo -51.6%, memoria -73.6%.
- `1049_number_theory_optimized.java`: 0.109 s / 368 KB; base `1049_number_theory.java`: 0.140 s / 3880 KB; cambio respecto a la base: tiempo -22.1%, memoria -90.5%.
- `1049_number_theory_optimized.py`: 0.109 s / 296 KB; base `1049_number_theory.py`: 0.078 s / 456 KB; cambio respecto a la base: tiempo +39.7%, memoria -35.1%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1049_number_theory.cpp`; fuente que cubre `1049_number_theory.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 121/121.

- Go: base didáctica preferida `1049_number_theory.go`; fuente que cubre `1049_number_theory_optimized.go`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Java: base didáctica preferida `1049_number_theory.java`; fuente que cubre `1049_number_theory_optimized.java`; puestos tiempo/memoria 3/1, registros de otros autores 4/4.

- Python/PyPy: base didáctica preferida `1049_number_theory.py`; fuente que cubre `1049_number_theory_optimized.py`; puestos tiempo/memoria 44/1, registros de otros autores 54/54.

- Rust: base didáctica preferida `1049_number_theory.rs`; fuente que cubre `1049_number_theory.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1049_number_theory.cpp](1049_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(10 · √10000) | AC | 0.015 s | 184 KB | 11278665 |
| [1049_number_theory.go](1049_number_theory.go) | Go 1.14 x64 | number_theory | O(10 · √10000) | AC | 0.031 s | 1108 KB | 11278667 |
| [1049_number_theory.java](1049_number_theory.java) | Java 1.8 | number_theory | O(10 · √10000) | AC | 0.140 s | 3880 KB | 11278675 |
| [1049_number_theory.py](1049_number_theory.py) | Python 3.12 x64 | number_theory | O(10 · √10000) | AC | 0.078 s | 456 KB | 11278673 |
| [1049_number_theory.rs](1049_number_theory.rs) | Rust 1.75 x64 | number_theory | O(10 · √10000) | AC | 0.015 s | 416 KB | 11278679 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1049_number_theory_optimized.go](1049_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(C sqrt(V)+V) time; O(V) space | AC | 0.015 s | 292 KB | 11309757 |
| [1049_number_theory_optimized.java](1049_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(C sqrt(V)+V) time; O(V) space | AC | 0.109 s | 368 KB | 11308799 |
| [1049_number_theory_optimized.py](1049_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(C sqrt(V)) time; O(C log V) prime records | AC | 0.109 s | 296 KB | 11309728 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
