# 1793. Bandeja 2

[Timus 1793](https://acm.timus.ru/problem.aspx?space=1&num=1793) · dificultad 403 · geometry

Problema original de Sofia Tekhazheva, del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una bandeja tiene un fondo de a × b y bordes verticales de altura d. Dos
platos son troncos de cono de la misma altura h, cada uno con un radio
de base y un radio superior mayor. ¿Pueden ponerse ambos platos con la
base entera apoyada en la bandeja?

## Entrada

a, b y d; luego el radio de base y el superior de cada plato; luego h.
Todos los números son enteros, de 1 a 1000.

## Salida

"YES" si los platos caben; si no, "NO".

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 10 10
1 2
1 2
5
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
8 4 1
1 2
1 3
1
```

Salida:

```
NO
```

## Solución

Un plato se ensancha hacia arriba, así que dentro de los bordes es más
ancho a la altura min(d, h), donde su radio es
w = r + (R − r)·min(d, h)/h. Por encima de los bordes puede sobresalir.
Por tanto el centro de cada plato debe quedar al menos a w de cada
lado, lo que requiere 2w ≤ a y 2w ≤ b. Dos platos de la misma altura
están más lejos de tocarse abajo y más cerca arriba, así que sus
centros deben estar al menos a R₁ + R₂. Los centros quedan lo más
lejos posible en esquinas opuestas de sus rectángulos permitidos, a
a − w₁ − w₂ en un sentido y a b − w₁ − w₂ en el otro. Multiplicar todo
por h deja números enteros, y comparar distancias al cuadrado evita
raíces, así que la prueba es exacta. `O(1)`.

En el primer ejemplo los bordes son más altos que los platos, así que
w = 2 para ambos; los centros pueden separarse 6 en cada sentido, unos
8,49 en total, y solo se necesitan 4.

Trampas:

- con bordes bajos la parte superior de un plato puede ser más ancha
  que la bandeja;
- los platos chocan por arriba, no a la altura de los bordes;
- platos que apenas se tocan sí caben, y una prueba en coma flotante
  puede fallar ahí.

Las respuestas coinciden con una implementación aceptada independiente
en 600 casos aleatorios, entre ellos platos que se tocan exactamente a
lo largo de una diagonal 3-4-5.

## Soluciones optimizadas

`1793_geometry_optimized.java`. Java conserva el algoritmo y las estructuras descritas para la versión sencilla. Un búfer fijo de bytes y FastInput sustituyen Scanner y su maquinaria de expresiones regulares y configuración regional. Los enteros se analizan directamente; las cadenas siguen decodificándose como UTF-8 cuando se solicitan y los decimales mantienen conversión numérica explícita. La anticipación guarda un token solo cuando hace falta. El algoritmo de salida no cambia. Se elimina el coste del análisis general; la tabla describe el trabajo algorítmico, con lectura lineal en bytes y un búfer acotado.

Frente a `1793_geometry.java`: tiempo 0.156 s → 0.109 s; memoria 1592 KB → 504 KB.

C++ y Go conservan la misma prueba exacta con radios escalados. Primero comprueban si cada plato cabe en el lado corto a la altura del borde. Después comparan la separación al cuadrado de las esquinas permitidas opuestas con el cuadrado de la suma de los radios superiores. Los productos finales usan enteros con signo de 64 bits y la salida es YES o NO. Go lee los ocho enteros positivos con un búfer fijo de bytes, sin tokens de Scanner ni conversiones de cadenas. Accede directamente a los descriptores estándar, reintenta las llamadas interrumpidas y completa las escrituras parciales.

Las implementaciones base aceptadas [1793_geometry.java](1793_geometry.java), [1793_geometry.py](1793_geometry.py), [1793_geometry.rs](1793_geometry.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1793_geometry_implementation_optimized.rs`. La entrada de C llama directamente al solucionador y vacía la salida de Rust antes de volver; se conserva la implementación de entrada habitual.

Accepted #11328965 (Rust 1.75 x64): **0.031 s / 172 KB**. Comparación archivada: `1793_geometry.rs` (Rust 1.75 x64) — 0.046 s / 216 KB (#11325607).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Conserva los algoritmos didácticos. Las filas básicas revalidadas usan sus nuevas métricas e IDs de Accepted de fuente exacta; estas pruebas no cuentan como optimizaciones.

`1793_geometry_optimized.java`: puesto de tiempo 8/31 y de memoria 3/31 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1793_geometry.cpp](1793_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 368 KB | 11325581 |
| [1793_geometry.go](1793_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1076 KB | 11289865 |
| [1793_geometry.java](1793_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 1592 KB | 11289867 |
| [1793_geometry.py](1793_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 432 KB | 11289866 |
| [1793_geometry.rs](1793_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 216 KB | 11325607 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1793_geometry_optimized.cpp](1793_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 104 KB | 11310893 |
| [1793_geometry_optimized.go](1793_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 312 KB | 11311212 |
| [1793_geometry_optimized.java](1793_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 504 KB | 11324814 |
| [1793_geometry_implementation_optimized.rs](1793_geometry_implementation_optimized.rs) | Rust 1.75 x64 | geometry, implementation | O(1) | AC | 0.031 s | 172 KB | 11328965 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
