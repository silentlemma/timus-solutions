# 1287. Canales en Marte

[Timus 1287](https://acm.timus.ru/problem.aspx?space=1&num=1287) · dificultad 383 · dp

Problema original de Alexander Mironenko (preparado por Igor Goldberg), del Concurso Individual de la Universidad Estatal de los Urales 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un campo de N × N (N ≤ 1400) está sembrado con dos clases de grano,
`s` y `S`, una por celda. Hay que hallar la racha recta más larga de
celdas iguales por fila, columna o cualquiera de las diagonales. Se
imprime la letra cuya racha más larga es mayor, o `?` si son iguales, y
luego esa longitud.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego N líneas de N letras.

## Salida

La letra ganadora o `?`, y luego la racha más larga.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
SsS
sSs
SsS
```

Salida:

```
S
3
```

### Ejemplo 2

Entrada:

```
2
sS
Ss
```

Salida:

```
?
2
```

## Solución

Se recorre el campo fila a fila. Para cada celda se guarda la longitud
de la racha que termina en ella en cada una de las cuatro direcciones:
desde la izquierda, desde arriba, desde arriba a la izquierda y desde
arriba a la derecha. Cada una es la racha del vecino más uno si el
vecino tiene la misma letra, y 1 si no. Solo hace falta la fila
anterior, y la racha más larga de cada letra se guarda por el camino.
La programación dinámica requiere `O(N²)` de tiempo y `O(N)` de
memoria para los estados; la memoria total depende de cómo se guarda
la entrada (véase abajo).

Detalles a tener en cuenta:

- la diagonal desde arriba a la derecha es fácil de olvidar (prueba 06);
- con rachas más largas iguales se imprime `?` (prueba 02);
- el campo tiene casi dos millones de celdas, así que la lectura debe
  ser rápida.

Las respuestas se compararon con recorrer cada racha desde cada celda
en 1200 campos aleatorios de hasta doce celdas de lado y en los 530
campos posibles de una a tres celdas de lado.

## Soluciones optimizadas

C++ usa SSE2 para actualizar ocho columnas a la vez en las rachas verticales y diagonales. La máscara de comparación conserva la longitud anterior donde coinciden las letras. Las rachas horizontales se recorren por separado. Go empaqueta longitud y letra en un entero de 16 bits y actualiza los tres vectores en el sitio, guardando el valor superior izquierdo para la siguiente columna. Ambas versiones usan O(N²) tiempo y O(N) espacio.

Las implementaciones base aceptadas [1287_dp.java](1287_dp.java), [1287_dp.py](1287_dp.py), [1287_dp.rs](1287_dp.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- C++, Go, Java y Rust guardan tres arreglos de rachas para cada una
  de dos filas y un contador para la racha horizontal. C++, Go y Java
  usan `O(N)` de memoria total; Rust conserva toda la entrada y usa `O(N²)`.
- Python sería demasiado lento celda a celda. Construye las filas, las
  columnas y las dos diagonales como cadenas de bytes: las diagonales
  son las columnas de las filas desplazadas un paso cada una, y `zip`
  hace la trasposición. Después una búsqueda binaria sobre k pregunta si
  aparecen k copias seguidas de una letra en el texto, con `bytes.find`.
  Los separadores y el relleno con puntos impiden que las rachas crucen
  entre líneas o salgan del campo. Construir el texto requiere `O(N²)`
  de tiempo y memoria; las búsquedas binarias requieren `O(N² log N)`
  de tiempo en el peor caso y la memoria total es `O(N²)`.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1287_dp.cpp](1287_dp.cpp) | G++ 13.2 x64 | dp | O(N²) | AC | 0.093 s | 232 KB | 11284526 |
| [1287_dp.go](1287_dp.go) | Go 1.14 x64 | dp | O(N²) | AC | 0.109 s | 6276 KB | 11284528 |
| [1287_dp.java](1287_dp.java) \* | Java 1.8 | dp | O(N²) | AC | 0.171 s | 4624 KB | 11284535 |
| [1287_dp.py](1287_dp.py) \* | Python 3.12 x64 | dp | O(N² log N) | AC | 0.406 s | 25392 KB | 11284533 |
| [1287_dp.rs](1287_dp.rs) | Rust 1.75 x64 | dp | O(N²) | AC | 0.046 s | 3160 KB | 11284536 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1287_dp_optimized.cpp](1287_dp_optimized.cpp) \* | G++ 13.2 x64 | dp | O(N²) | AC | 0.062 s | 124 KB | 11311205 |
| [1287_dp_optimized.go](1287_dp_optimized.go) \* | Go 1.14 x64 | dp | O(N²) | AC | 0.046 s | 916 KB | 11310411 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
