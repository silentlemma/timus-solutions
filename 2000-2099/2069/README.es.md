# 2069. La mejor ruta con a lo sumo dos giros

[Timus 2069](https://acm.timus.ru/problem.aspx?space=1&num=2069) · dificultad 226 · greedy

Problema original de Oleg Merkurev, preparado por Alexander Borzunov, del Concurso Regional de Programación por Equipos de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad es una cuadrícula de n calles verticales y m horizontales, y
cada calle tiene su propia popularidad. Una ruta va por las calles desde
la esquina superior izquierda hasta la inferior derecha, y su genialidad
es la menor popularidad entre las calles en las que recorre una
distancia no nula. Hallar la mayor genialidad posible. Los límites son
1 segundo y 64 MB.

## Entrada

n y m, 2 ≤ n, m ≤ 10⁵, después las n popularidades de las calles
verticales de izquierda a derecha y las m de las horizontales de arriba
abajo, una por línea, cada una de 1 a 10⁹.

## Salida

La mayor genialidad.

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
4
8
2
7
3
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
4 3
12
4
12
3
21
5
16
```

Salida:

```
12
```

## Solución

Sean v₁ … vₙ las calles verticales y h₁ … hₘ las horizontales; la ruta
empieza donde se cruzan v₁ y h₁ y termina donde se cruzan vₙ y hₘ. Su
primer paso va por v₁ o por h₁, y el último por vₙ o por hₘ, así que hay
cuatro casos.

- Empieza en v₁ y termina en hₘ. La genialidad es como mucho
  min(v₁, hₘ), y bajar por v₁ y luego ir a la derecha por hₘ la alcanza.
- Empieza en h₁ y termina en vₙ: como mucho min(h₁, vₙ), que se alcanza
  yendo a la derecha y luego hacia abajo.
- Empieza en h₁ y termina en hₘ. Para cambiar de fila la ruta debe
  recorrer alguna calle vertical, así que la genialidad es como mucho
  min(h₁, max v, hₘ). Ir a la derecha por h₁ hasta la mejor calle
  vertical, bajar por ella e ir a la derecha por hₘ da al menos ese valor.
- Empieza en v₁ y termina en vₙ: de forma simétrica min(v₁, max h, vₙ).

Toda ruta cae en uno de los casos y cada cota se alcanza, así que la
respuesta es el mayor de los cuatro valores, en O(n + m).

En el primer ejemplo los dos primeros casos dan min(4, 3) = 3 y
min(2, 8) = 2, mientras que el último baja por v₁ = 4, va a la derecha
por h₂ = 7 y baja por v₂ = 8, con genialidad 4.

## Soluciones optimizadas

Se calculan en flujo máximos y valores extremos de las calles de ambas direcciones, sin guardarlas todas. Un umbral es viable si y solo si alguna calle de cada dirección lo alcanza y cada extremo tiene una calle incidente adecuada. Su rejilla cruzada es conexa, de modo que las condiciones son necesarias y suficientes. El mínimo de los máximos direccionales y de los extremos produce la respuesta con memoria constante.

- `2069_greedy_optimized.cpp`: 0.015 s / 84 KB; base `2069_greedy.cpp`: 0.156 s / 964 KB; cambio respecto a la base: tiempo -90.4%, memoria -91.3%.
- `2069_greedy_optimized.go`: 0.031 s / 1020 KB; base `2069_greedy.go`: 0.062 s / 5704 KB; cambio respecto a la base: tiempo -50.0%, memoria -82.1%.
- `2069_greedy_optimized.java`: 0.109 s / 404 KB; base `2069_greedy.java`: 0.140 s / 1260 KB; cambio respecto a la base: tiempo -22.1%, memoria -67.9%.
- `2069_greedy_optimized.py`: 0.171 s / 412 KB; base `2069_greedy.py`: 0.125 s / 21628 KB; cambio respecto a la base: tiempo +36.8%, memoria -98.1%.
- `2069_greedy_optimized.rs`: 0.031 s / 196 KB; base `2069_greedy.rs`: 0.015 s / 6308 KB; cambio respecto a la base: tiempo +106.7%, memoria -96.9%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `2069_greedy.cpp`; versión que cubre `2069_greedy_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 51/51.

- Go: base didáctica preferida `2069_greedy.go`; versión que cubre `2069_greedy_optimized.go`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Java: base didáctica preferida `2069_greedy.java`; versión que cubre `2069_greedy.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `2069_greedy.py`; versión que cubre `2069_greedy_optimized.py`; puestos tiempo/memoria 2/1, registros de otros autores 4/4.

- Rust: base didáctica preferida `2069_greedy.rs`; versión que cubre `2069_greedy_optimized.rs`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2069_greedy.cpp](2069_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.156 s | 964 KB | 11309218 |
| [2069_greedy.go](2069_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.062 s | 5704 KB | 11294438 |
| [2069_greedy.java](2069_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.140 s | 1260 KB | 11309219 |
| [2069_greedy.py](2069_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.125 s | 21628 KB | 11309220 |
| [2069_greedy.rs](2069_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.015 s | 6308 KB | 11309221 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2069_greedy_optimized.cpp](2069_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N+M) | AC | 0.015 s | 84 KB | 11308572 |
| [2069_greedy_optimized.go](2069_greedy_optimized.go) | Go 1.14 x64 | greedy | O(N+M) | AC | 0.031 s | 1020 KB | 11308575 |
| [2069_greedy_optimized.java](2069_greedy_optimized.java) | Java 1.8 | greedy | O(N+M) | AC | 0.109 s | 404 KB | 11308581 |
| [2069_greedy_optimized.py](2069_greedy_optimized.py) \* | Python 3.12 x64 | greedy | O(N+M) | AC | 0.171 s | 412 KB | 11308586 |
| [2069_greedy_optimized.rs](2069_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(N+M) | AC | 0.031 s | 196 KB | 11308590 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
