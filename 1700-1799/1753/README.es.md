# 1753. Estantería

[Timus 1753](https://acm.timus.ru/problem.aspx?space=1&num=1753) · dificultad 335 · geometry

Problema original de Dmitry Ivankov, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una estantería de longitud L tiene bordes de altura h en ambos
extremos. Un libro de altura H está de pie junto al borde izquierdo. Su
canto inferior se arrastra hacia la derecha por la estantería mientras
su lado sigue apoyado en lo alto del borde izquierdo, hasta que el
libro queda tumbado. Todo tiene grosor cero. Hallar cuánto se aleja a
la izquierda del borde izquierdo el centro del libro.

## Entrada

Enteros h, H y L (1 ≤ h < H < L ≤ 1000).

## Salida

El mayor desplazamiento del centro del libro a la izquierda del borde,
con un error de a lo sumo 10⁻⁵.

## Evaluación

Las pruebas del repositorio comparan tokens numéricos con |resultado-referencia| <= 1e-5·max(1,|referencia|), rechazan valores no finitos y comparan exactamente los tokens no numéricos.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 120 200
```

Salida:

```
39.850361
```

## Solución

Se pone lo alto del borde izquierdo en (0, h) y el pie del libro en
(x, 0). El libro sigue la recta del pie a lo alto del borde, un tramo
de longitud r = √(x² + h²), así que su centro, a distancia H/2 del pie,
está en la posición horizontal x(1 − H / 2r). El desplazamiento a la
izquierda es f(x) = x(H / 2r − 1).

Su derivada es H·h² / 2r³ − 1, así que f crece mientras r³ < H·h²/2 y
decrece después, y el mejor momento es r = ∛(H·h²/2). Ese r nunca pasa
de H, así que el libro aún se apoya en el borde. Si ese r no supera h,
lo que ocurre justo cuando H ≤ 2h, el centro nunca pasa el borde y la
respuesta es 0; si no, x = √(r² − h²) y la respuesta es f(x). L no
influye, pues el libro siempre cabe en la estantería. `O(1)`.

En el ejemplo r = ∛2940 ≈ 14,33, x ≈ 12,50 y el desplazamiento es de
unos 39,85.

Trampas:

- un libro de a lo sumo el doble del borde da 0, no un desplazamiento
  negativo;
- el borde está a la izquierda, así que mover el pie a la derecha
  empuja el centro a la izquierda solo mientras el libro está empinado.

La fórmula coincide con un barrido de 200001 posiciones del pie en 100
entradas aleatorias y con una implementación aceptada independiente en
otras 300.

## Soluciones optimizadas

`1753_geometry_optimized.java`. Java conserva el algoritmo y las estructuras descritas para la versión sencilla. Un búfer fijo de bytes y FastInput sustituyen Scanner y su maquinaria de expresiones regulares y configuración regional. Los enteros se analizan directamente; las cadenas siguen decodificándose como UTF-8 cuando se solicitan y los decimales mantienen conversión numérica explícita. La anticipación guarda un token solo cuando hace falta. El algoritmo de salida no cambia. Se elimina el coste del análisis general; la tabla describe el trabajo algorítmico, con lectura lineal en bytes y un búfer acotado.

Frente a `1753_geometry.java`: tiempo 0.109 s → 0.125 s; memoria 1816 KB → 984 KB.

Go y Rust reescriben el mismo óptimo con la razón q = cbrt(H/(2h)). Si H ≤ 2h, el desplazamiento es cero. En otro caso toman f = (q−1)(q+1) y calculan h·f·sqrt(f). El factor compartido se calcula una vez y se evita restar cuadrados de longitudes grandes. El resultado se imprime directamente con seis decimales. Ambas versiones usan búferes fijos de bytes y redondean a millonésimas antes de escribir las cifras decimales. Go usa directamente los descriptores estándar. Rust arranca mediante C main y transfiere los búferes con la biblioteca de C.

Las implementaciones base aceptadas [1753_geometry.cpp](1753_geometry.cpp), [1753_geometry.java](1753_geometry.java), [1753_geometry.py](1753_geometry.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Conserva los algoritmos didácticos. Las filas básicas revalidadas usan sus nuevas métricas e IDs de Accepted de fuente exacta; estas pruebas no cuentan como optimizaciones.

`1753_geometry_optimized.java`: puesto de tiempo 19/37 y de memoria 9/37 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1753_geometry.cpp](1753_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 132 KB | 11325580 |
| [1753_geometry.go](1753_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB | 11289561 |
| [1753_geometry.java](1753_geometry.java) \* | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1816 KB | 11289563 |
| [1753_geometry.py](1753_geometry.py) \* | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 400 KB | 11289562 |
| [1753_geometry.rs](1753_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 236 KB | 11325633 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1753_geometry_optimized.go](1753_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 284 KB | 11311227 |
| [1753_geometry_optimized.rs](1753_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 56 KB | 11311226 |
| [1753_geometry_optimized.java](1753_geometry_optimized.java) \* | Java 1.8 | geometry | O(1) | AC | 0.125 s | 984 KB | 11324797 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
