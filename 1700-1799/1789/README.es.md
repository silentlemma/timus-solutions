# 1789. En busca del Dodecaedro

[Timus 1789](https://acm.timus.ru/problem.aspx?space=1&num=1789) · dificultad 220 · constructive

Problema original de Mikhail Rubinchik, del Concurso Regional por Equipos de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un artefacto está sobre uno de n pedestales en fila, y en los demás hay
copias. En cada turno se toca un pedestal. Si el artefacto está allí,
se encuentra; si no, el artefacto pasa a un pedestal vecino, izquierdo
o derecho, a su elección. Imprimir una secuencia de a lo sumo 1000
toques que encuentre el artefacto dondequiera que empiece y como sea
que se mueva.

## Entrada

n (2 ≤ n ≤ 100).

## Salida

El número de toques y luego los pedestales tocados en orden.

## Evaluación

Validar como máximo 1000 toques con pedestales en 1..N; propagar las posiciones posibles tras cada toque fallido y exigir que no sobreviva ninguna. Se acepta cualquier secuencia con esta garantía. El nuevo código Python exacto pasó 13 pruebas del repositorio con PyPy 3.10. Además 99 comparaciones de construcción por flujo frente a listas para todo N=2..100. Las otras variantes conservan sus propias pruebas de destino y Accepted exactos. La salida se compara según el verificador del problema.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
2
2 2
```

## Solución

Tras cada toque fallido el artefacto se mueve, así que la paridad de su
pedestal cambia en cada turno. Se tocan 2, 3, …, n − 1. Si en el primer
toque el artefacto está en un pedestal par, en cada turno tiene la
misma paridad que el tocado y no está a su izquierda, así que no puede
saltarlo y queda atrapado en n − 1 a más tardar. Si no, tras esos
n − 2 toques tiene la paridad de n − 1, y tocar n − 1, n − 2, …, 2 lo
barre igual desde la derecha. Para n > 2, los pedestales 1 y n
nunca se tocan: un artefacto allí tiene que moverse hacia dentro. Eso
da 2(n − 2) toques. Con n = 2 no hay parte central, y basta tocar el
pedestal 1 dos veces. `O(n)`.

En el ejemplo ambas pasadas son el único toque del pedestal 2: un
artefacto en 2 se atrapa enseguida, y uno en 1 o 3 tiene que ir al 2.

Trampas:

- la pasada desde la izquierda sola pierde el artefacto que empieza con
  la otra paridad, que simplemente se cuela;
- con n > 2, tocar los extremos es inútil, el artefacto no puede
  quedarse en ellos;
- n = 2 necesita su propia respuesta, ya que la fórmula da cero toques.

El verificador sigue el conjunto de pedestales donde el artefacto aún
puede estar y exige que se vacíe. Todo n de 2 a 100 pasa, y una
búsqueda completa sobre esos conjuntos para n hasta 12 confirma que no
existe una secuencia más corta.

## Soluciones optimizadas

Se mantiene la construcción que cubre ambas paridades y su prueba. Para N>2, recorrer 2..N-1 y luego N-1..2, con 2*(N-2) toques. Para N=2, emitir 1,1. Las variantes compactas escriben el recorrido sin listas concatenadas ni expansión de argumentos. Secuencia y garantía no cambian; salida O(N), estado de trabajo acotado. Se conservan todos los archivos sencillos.

- `1789_constructive_optimized.cpp`: 0.015 s / 108 KB; base `1789_constructive.cpp`: 0.031 s / 380 KB; cambio respecto a la base: tiempo -51.6%, memoria -71.6%.
- `1789_constructive_optimized.py`: 0.156 s / 240 KB; base `1789_constructive.py`: 0.062 s / 396 KB; cambio respecto a la base: tiempo +151.6%, memoria -39.4%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1789_constructive.cpp`; fuente que cubre `1789_constructive_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 51/51.

- Go: base didáctica preferida `1789_constructive.go`; fuente que cubre `1789_constructive.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1789_constructive.java`; fuente que cubre `1789_constructive.java`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Python/PyPy: base didáctica preferida `1789_constructive.py`; fuente que cubre `1789_constructive_optimized.py`; puestos tiempo/memoria 8/1, registros de otros autores 7/7.

- Rust: base didáctica preferida `1789_constructive.rs`; fuente que cubre `1789_constructive.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1789_constructive.cpp](1789_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.031 s | 380 KB | 11308929 |
| [1789_constructive.go](1789_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1108 KB | 11289832 |
| [1789_constructive.java](1789_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 1604 KB | 11308930 |
| [1789_constructive.py](1789_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.062 s | 396 KB | 11289833 |
| [1789_constructive.rs](1789_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 204 KB | 11289836 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1789_constructive_optimized.cpp](1789_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 108 KB | 11308552 |
| [1789_constructive_optimized.py](1789_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(N) | AC | 0.156 s | 240 KB | 11309701 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
