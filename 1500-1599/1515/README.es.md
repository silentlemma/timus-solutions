# 1515. Reforma financiera

[Timus 1515](https://acm.timus.ru/problem.aspx?space=1&num=1515) · dificultad 215 · greedy

Problema original de Ilya Grebnov, Nikita Rybak y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay un billete de cada uno de N valores (1 ≤ N ≤ 100), dados en orden
creciente, cada uno de 1 a 10⁶. Hay que hallar el menor valor positivo
que no es la suma de algunos de esos billetes; un solo billete cuenta
como suma.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los N valores en orden creciente.

## Salida

El menor valor que ningún conjunto de billetes suma.

## Evaluación

Se comparan enteros exactos. Las fuentes nuevas tienen pruebas completas de destino y Accepted propio; las bases publicadas conservan su propio Accepted, sin sustituir medidas del archivo antiguo.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1 2 4 9 100
```

Salida:

```
8
```

## Solución

Se recorren los valores en orden creciente guardando reach, el mayor
número tal que toda suma de 1 a reach se puede pagar. Si el siguiente
valor d es como mucho reach + 1, también se puede pagar toda suma hasta
reach + d: las sumas hasta reach como antes, y las mayores como d más
una suma hasta reach. Si d > reach + 1, entonces reach + 1 no se puede
pagar: los valores tomados suman solo reach, y cualquier otro valor ya
es mayor que reach + 1 por sí solo. La respuesta es reach + 1. La entrada ya está ordenada, por lo que no hace falta volver a ordenarla.
El tiempo es `O(N)` y el algoritmo mantiene `O(1)` de estado adicional.
C++, Go y Java leen los valores en flujo; Python y Rust también guardan
la entrada, usando `O(N)` de memoria.

Detalles a tener en cuenta:

- el orden creciente dado es esencial para la prueba voraz; no hace falta
  ordenar de nuevo (pruebas 05, 06 con N = 100);
- sin un billete de 1 la respuesta es 1 (pruebas 03, 06);
- la respuesta puede superar todos los valores, hasta la suma de todos
  más uno (pruebas 04, 05, gen2);
- el primer hueco termina el recorrido y ningún valor posterior lo
  llena: con 1 y 3 falta la suma 2 (prueba 07).

## Soluciones optimizadas

Las cinco versiones didácticas recorren en tiempo lineal la entrada ya ordenada. Si se pueden formar todas las sumas hasta `reach`, un billete cuyo valor no supera `reach + 1` amplía el intervalo hasta `reach + note`. Un billete mayor deja el primer hueco sin cubrir y termina el recorrido. La versión compacta de Python conserva el mismo invariante y escribe la respuesta directamente. La ejecución aceptada en PyPy usó 244 KB frente a los 352 KB de la versión didáctica, una reducción del 30,7%. El tiempo subió de 0,093 s a 0,125 s.

- `1515_greedy_optimized.py`: 0.125 s / 244 KB; base `1515_greedy.py`: 0.093 s / 352 KB; cambio respecto a la base: tiempo +34.4%, memoria -30.7%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1515_greedy.cpp`; fuente que cubre `1515_greedy.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 71/71.

- Go: base didáctica preferida `1515_greedy.go`; fuente que cubre `1515_greedy.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1515_greedy.java`; fuente que cubre `1515_greedy.java`; puestos tiempo/memoria 1/1, registros de otros autores 5/5.

- Python/PyPy: base didáctica preferida `1515_greedy.py`; fuente que cubre `1515_greedy_optimized.py`; puestos tiempo/memoria 7/1, registros de otros autores 7/7.

- Rust: base didáctica preferida `1515_greedy.rs`; fuente que cubre `1515_greedy.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1515_greedy.cpp](1515_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.015 s | 112 KB | 11307976 |
| [1515_greedy.go](1515_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.031 s | 1072 KB | 11307979 |
| [1515_greedy.java](1515_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.078 s | 420 KB | 11307981 |
| [1515_greedy.py](1515_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.093 s | 352 KB | 11307983 |
| [1515_greedy.rs](1515_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.015 s | 220 KB | 11307984 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1515_greedy_optimized.py](1515_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(N) time; O(N) input tokens | AC | 0.125 s | 244 KB | 11309746 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
