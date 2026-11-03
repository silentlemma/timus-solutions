# 1794. Obras maestras de la arquitectura mundial

[Timus 1794](https://acm.timus.ru/problem.aspx?space=1&num=1794) · dificultad 197 · implementation

Problema original de Vladislav Isenbaev (preparado por Oleg Dolgorukov), del Concurso Regional de Programación por Equipos de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n estudiantes se sientan en círculo, numerados de 1 a n en sentido
horario, y hablarán uno tras otro en sentido horario. El estudiante i
quiere hablar en el turno aᵢ. Elegir quién habla primero para que el
mayor número posible de estudiantes hable justo en el turno que quiere.
Se acepta cualquier mejor elección.

## Entrada

n (2 ≤ n ≤ 10⁵), luego a₁, …, aₙ (1 ≤ aᵢ ≤ n).

## Salida

El número del estudiante que empieza.

## Evaluación

Se acepta cualquier estudiante inicial que maximice los deseos cumplidos; no se exige el menor índice.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
4 1 2 3
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
3
1 1 1
```

Salida:

```
3
```

## Solución

Si empieza el estudiante k, el estudiante i habla en el turno
((i − k) mod n) + 1. Así que al estudiante i le conviene exactamente un
inicio, k = ((i − aᵢ) mod n) + 1. Se cuentan esos votos de todos los
estudiantes y se imprime un inicio con más votos. `O(n)`.

En el primer ejemplo los cuatro estudiantes votan por el inicio 2: por
ejemplo, el estudiante 1 quiere ser cuarto, y 2, 3, 4, 1 lo pone
cuarto.

Trampas:

- i − aᵢ puede ser negativo, y en C++, Go y Java el resto también lo es
  entonces;
- varios inicios pueden empatar, como en el segundo ejemplo, donde se
  acepta cualquiera de los tres.

El verificador cuenta los votos por sí mismo y acepta cualquier inicio
con el máximo. Coincide con un recuento directo sobre todos los inicios
en 300 clases pequeñas, y las respuestas coinciden con una
implementación aceptada independiente en las grandes.

## Soluciones optimizadas

Se mantiene el número de votos por inicio. La diferencia está estrictamente entre el tamaño negativo y positivo de la clase, por lo que basta una suma condicional. La entrada con búfer evita retener preferencias; los contadores sin signo de 32 bits bastan porque cada uno no supera el tamaño de la clase. Se elige el primer máximo, aunque el enunciado acepta cualquier inicio óptimo.

- `1794_implementation_optimized.cpp`: 0.015 s / 520 KB; base `1794_implementation.cpp`: 0.078 s / 568 KB; cambio respecto a la base: tiempo -80.8%, memoria -8.5%.
- `1794_implementation_optimized.py`: 0.187 s / 912 KB; base `1794_implementation.py`: 0.125 s / 8004 KB; cambio respecto a la base: tiempo +49.6%, memoria -88.6%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1794_implementation.cpp`; versión que cubre `1794_implementation_optimized.cpp`; puestos tiempo/memoria 1/8, registros de otros autores 96/96.

- Go: base didáctica preferida `1794_implementation.go`; versión que cubre `1794_implementation.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1794_implementation.java`; versión que cubre `1794_implementation.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1794_implementation.py`; versión que cubre `1794_implementation_optimized.py`; puestos tiempo/memoria 13/1, registros de otros autores 13/13.

- Rust: base didáctica preferida `1794_implementation.rs`; versión que cubre `1794_implementation.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1794_implementation.cpp](1794_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.078 s | 568 KB | 11308931 |
| [1794_implementation.go](1794_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 2400 KB | 11289873 |
| [1794_implementation.java](1794_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 792 KB | 11308933 |
| [1794_implementation.py](1794_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.125 s | 8004 KB | 11308935 |
| [1794_implementation.rs](1794_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 2124 KB | 11308936 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1794_implementation_optimized.cpp](1794_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 520 KB | 11308385 |
| [1794_implementation_optimized.py](1794_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N) | AC | 0.187 s | 912 KB | 11309462 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
