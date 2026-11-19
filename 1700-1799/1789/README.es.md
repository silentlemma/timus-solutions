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

`1789_constructive_optimized.java`. Mantiene los barridos de paridad 2..n-1 y n-1..2, con respuesta especial 1,1 para n=2. Calcula 2(n-2) toques y emite números al recorrerlos. Java elimina la lista con objetos y el constructor completo; Rust elimina el vector, las cadenas individuales y su unión. Con n<=100 la salida y el tiempo son O(n), usando espacio auxiliar O(1) en vez de O(n). Mejora representación y salida de la misma construcción; conserva las fuentes didácticas.

Frente a `1789_constructive.java`: tiempo 0.125 s → 0.109 s; memoria 1604 KB → 504 KB.

`1789_constructive_optimized.rs`. Mantiene los barridos de paridad 2..n-1 y n-1..2, con respuesta especial 1,1 para n=2. Calcula 2(n-2) toques y emite números al recorrerlos. Java elimina la lista con objetos y el constructor completo; Rust elimina el vector, las cadenas individuales y su unión. Con n<=100 la salida y el tiempo son O(n), usando espacio auxiliar O(1) en vez de O(n). Mejora representación y salida de la misma construcción; conserva las fuentes didácticas.

Frente a `1789_constructive.rs`: tiempo 0.046 s → 0.046 s; memoria 204 KB → 52 KB.

Se mantiene la construcción que cubre ambas paridades y su prueba. Para N>2, recorrer 2..N-1 y luego N-1..2, con 2*(N-2) toques. Para N=2, emitir 1,1. Las variantes compactas escriben el recorrido sin listas concatenadas ni expansión de argumentos. Secuencia y garantía no cambian; salida O(N), estado de trabajo acotado. Se conservan todos los archivos sencillos.

- `1789_constructive_optimized.cpp`: 0.015 s / 108 KB; base `1789_constructive.cpp`: 0.031 s / 380 KB; cambio respecto a la base: tiempo -51.6%, memoria -71.6%.
- `1789_constructive_optimized.py`: 0.156 s / 240 KB; base `1789_constructive.py`: 0.062 s / 396 KB; cambio respecto a la base: tiempo +151.6%, memoria -39.4%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1789_constructive_optimized.java`: puesto de tiempo 14/35 y de memoria 5/35 en esta muestra comparable.

`1789_constructive_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

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
| [1789_constructive_optimized.java](1789_constructive_optimized.java) \* | Java 1.8 | constructive | O(n) | AC | 0.109 s | 504 KB | 11324970 |
| [1789_constructive_optimized.rs](1789_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 52 KB | 11325112 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
