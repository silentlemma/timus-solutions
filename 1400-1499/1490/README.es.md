# 1490. Círculo de fuego

[Timus 1490](https://acm.timus.ru/problem.aspx?space=1&num=1490) · dificultad 196 · math

Problema original de Alexander Ipatov, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El suelo está cubierto de baldosas de 1 × 1. Un círculo de fuego de
radio entero R (R ≤ 10⁵) tiene el centro en un punto donde se juntan
cuatro baldosas. Una baldosa se estropea si tiene al menos dos puntos en
común con el círculo. Hay que contar las baldosas estropeadas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

R.

## Salida

El número de baldosas estropeadas.

## Evaluación

Se comparan los tokens exactos; los espacios no afectan.

- `1490_two_pointers.java` (Java 1.8): 14 pruebas del repositorio.

- `1490_two_pointers.py` (PyPy 3.10 x64): 14 pruebas del repositorio.

- `1490_two_pointers.rs` (Rust 1.75 x64): 14 pruebas del repositorio.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
16
```

### Ejemplo 2

Entrada:

```
4
```

Salida:

```
60
```

## Solución

Los ejemplos muestran que cuenta todo el disco, no solo su borde. Una
baldosa comparte más de un punto con el disco justo cuando su esquina
más cercana al centro está estrictamente dentro; una baldosa cuya
esquina más cercana está en la circunferencia solo la toca en ese punto.

Por simetría se cuenta un cuarto y se multiplica por 4. Ahí la baldosa
con esquina inferior izquierda (i, j) cuenta cuando i² + j² < R², así
que la columna i tiene ⌊√(R² − i² − 1)⌋ + 1 baldosas, con i de 0 a
R − 1. Una raíz cuadrada entera lo mantiene exacto. La respuesta llega
a unos π·10¹⁰ y necesita 64 bits. `O(R)`.

Detalles a tener en cuenta:

- una baldosa que solo toca el disco en una esquina, como la que hay
  tras (3, 4) para R = 5, no cuenta (pruebas 04, 05, 06);
- la respuesta para R = 10⁵ es 31 416 325 412, más de 32 bits
  (prueba 07);
- una raíz en coma flotante debe corregirse hasta la raíz entera exacta
  (pruebas 06, 07).

## Soluciones optimizadas

Se conservan las bases con raíz cuadrada. two_pointers recorre x=0..R-1 manteniendo y esquinas cercanas del primer cuadrante estrictamente dentro del disco. Mientras x*x+(y-1)*(y-1)>=R*R se reduce y; se suma y y al final se multiplica por cuatro. La frontera es monótona: y baja como máximo R veces, O(R) operaciones enteras y estado constante. La igualdad queda fuera y excluye tangencias, sin redondeos ni doble conteo de ejes. R<=100000 cabe en64bits con signo. Python desactiva explícitamente el JIT PyPy para acotar caché y elimina un marco adicional; se declara el intercambio de mayor tiempo por menor memoria.

- `1490_two_pointers.java`: 0.125 s / 456 KB; base `1490_math.java`: 0.109 s / 1612 KB; cambio respecto a la base: tiempo +14.7%, memoria -71.7%.
- `1490_two_pointers.py`: 0.234 s / 308 KB; base `1490_math.py`: 0.078 s / 472 KB; cambio respecto a la base: tiempo +200.0%, memoria -34.7%.
- `1490_two_pointers.rs`: 0.031 s / 36 KB; base `1490_math.rs`: 0.031 s / 232 KB; cambio respecto a la base: tiempo -0.0%, memoria -84.5%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1490_math.cpp`; fuente que cubre `1490_math.cpp`; puestos tiempo/memoria 1/15, registros de otros autores 93/93.

- Go: base didáctica preferida `1490_math.go`; fuente que cubre `1490_math.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1490_math.java`; fuente que cubre `1490_two_pointers.java`; puestos tiempo/memoria 4/2, registros de otros autores 4/4.

- Python/PyPy: base didáctica preferida `1490_math.py`; fuente que cubre `1490_two_pointers.py`; puestos tiempo/memoria 14/1, registros de otros autores 15/15.

- Rust: base didáctica preferida `1490_math.rs`; fuente que cubre `1490_two_pointers.rs`; puestos tiempo/memoria 2/1, registros de otros autores 1/1.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1490_math.cpp](1490_math.cpp) | G++ 13.2 x64 | math | O(R) | AC | 0.015 s | 128 KB | 11287181 |
| [1490_math.go](1490_math.go) | Go 1.14 x64 | math | O(R) | AC | 0.031 s | 1088 KB | 11287183 |
| [1490_math.java](1490_math.java) | Java 1.8 | math | O(R) | AC | 0.109 s | 1612 KB | 11287185 |
| [1490_math.py](1490_math.py) | Python 3.12 x64 | math | O(R) | AC | 0.078 s | 472 KB | 11287184 |
| [1490_math.rs](1490_math.rs) | Rust 1.75 x64 | math | O(R) | AC | 0.031 s | 232 KB | 11287186 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1490_two_pointers.java](1490_two_pointers.java) \* | Java 1.8 | two_pointers | O(R) time; O(1) working state | AC | 0.125 s | 456 KB | 11307985 |
| [1490_two_pointers.py](1490_two_pointers.py) \* | PyPy 3.10 x64 | two_pointers | O(R) time; O(1) working state | AC | 0.234 s | 308 KB | 11309772 |
| [1490_two_pointers.rs](1490_two_pointers.rs) \* | Rust 1.75 x64 | two_pointers | O(R) time; O(1) working state | AC | 0.031 s | 36 KB | 11309706 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
