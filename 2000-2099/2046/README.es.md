# 2046. Ajuste por palabras en un horario fijo

[Timus 2046](https://acm.timus.ru/problem.aspx?space=1&num=2046) · difficulty 507 · implementation

Problema original de Oleg Dolgorukov, del Campeonato de Programación Deportiva de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dibujar cuatro filas de clases y tres columnas de días en el orden
Tuesday, Thursday, Saturday.
Cada celda tiene diez caracteres de contenido por línea. Conservar las
palabras y su orden, con un espacio entre palabras de la misma línea.
Colocar la siguiente palabra en la línea actual si cabe junto con ese
espacio; si no, comenzar otra línea. No dividir palabras. Alinear arriba
y a la izquierda, rellenar cada línea hasta diez caracteres y completar
las líneas ausentes con espacios. La altura de una fila es la máxima de
sus celdas, o uno si todas están vacías. Usar `+` en intersecciones, `-`
horizontalmente y `|` verticalmente, sin encabezados adicionales.

## Entrada

Leer `1≤n≤12` cursos, cada uno en dos líneas: su nombre y luego día y
número de clase. El nombre tiene de una a cinco palabras, separadas por
un solo espacio y sin espacios exteriores. Cada palabra tiene de una a
diez letras latinas mayúsculas o minúsculas. Los nombres son distintos.
El día es `Tuesday`, `Thursday` o `Saturday` y la clase está en `1..4`.
No hay cursos en el mismo hueco. Límites: 1 segundo y 64 MB.

## Salida

Imprimir únicamente la tabla. Se comprueba el texto exacto, incluidos
espacios internos, saltos y bordes. Terminar con salto de línea. Un
borde es `+----------+----------+----------+` y cada línea tiene 34
caracteres. Si `H` suma las cuatro alturas de contenido, habrá `H+5`
líneas, como máximo 25.

## Evaluación

La salida se compara exactamente, carácter a carácter; solo puede
diferir el último salto de línea.

## Ejemplos

```
9
Physics
Thursday 3
Maths
Tuesday 1
Chemistry
Thursday 1
Physical education
Saturday 2
Astronomy
Saturday 4
Urban geography
Tuesday 4
History
Saturday 1
Modeling
Thursday 2
Biology
Thursday 4
```

```
+----------+----------+----------+
|Maths     |Chemistry |History   |
+----------+----------+----------+
|          |Modeling  |Physical  |
|          |          |education |
+----------+----------+----------+
|          |Physics   |          |
+----------+----------+----------+
|Urban     |Biology   |Astronomy |
|geography |          |          |
+----------+----------+----------+
```

Los tres nombres de la primera fila ocupan una línea. En la segunda,
`Physical education` no cabe en diez columnas y se divide en `Physical`
y `education`. Toda esa fila pasa a dos líneas; el martes vacío y la
segunda línea de `Modeling` se rellenan con espacios. `Urban geography`
produce igualmente la segunda línea de la última fila. Cada curso
conserva su día y clase.

## Solución

Ajustar cada nombre por separado. Mantener una línea actual: si está
vacía, colocar la palabra; en otro caso, añadir espacio y palabra si el
total no supera diez, o terminar la línea y comenzar otra con esa
palabra. Guardar las líneas en la celda indicada por clase menos uno e
índice fijo del día.

Después de cada palabra, todas las líneas terminadas contienen el
prefijo consecutivo más largo que cabe desde su inicio, y la actual
contiene las restantes palabras procesadas en orden. Añadir una palabra
que cabe mantiene el invariante. Si no cabe, la línea anterior más esa
palabra superaría diez, por lo que comenzar otra es exactamente la regla
exigida. Cada palabra cabe individualmente: no se pierde, divide ni
desborda ninguna.

Para cada clase tomar el máximo de uno y las tres alturas. Imprimir ese
número de líneas. En el nivel `r` cada celda aporta su línea `r`, o una
vacía, y se completa con espacios hasta diez caracteres. Se conserva el
ajuste independiente y la alineación superior izquierda. La altura basta
para todas las celdas y mantiene una línea en una fila completamente
vacía. Un borde antes de la tabla y otro después de cada clase sitúan
los cinco bordes horizontales. Los huecos únicos impiden sobrescribir
cursos.

Sean `L` la suma de longitudes de nombres, `C=3`, `W=10` y `H≤20` la
suma de alturas. El tiempo y espacio son `O(L+WCH)` incluyendo la salida
almacenada; los puertos con salida progresiva usan menos almacenamiento.
Aquí `L≤648` y la salida tiene como máximo 875 bytes.

## Soluciones optimizadas

C++ y Go conservan el ajuste voraz, dibujando en celdas fijas: cuatro clases, tres días, cinco líneas como máximo y ancho diez requieren 600 caracteres. Alturas desde uno, cada palabra copiada una vez a su lugar final; se reutilizan línea y borde de 35 bytes. Las palabras y el relleno comparten el arreglo de celdas. Leer nombres enteros y conservar mayúsculas, filas vacías y espacios finales. Con L bytes de entrada y B de salida, el tiempo es O(L+B). La cuadrícula y el búfer de línea tienen tamaño fijo. C++ lee un nombre y escribe una línea cada vez. Go lee del manejador estándar en un búfer de 1024 bytes y reúne hasta 875 bytes de salida antes de escribirlos. Java, Python y Rust reutilizan sus bases admitidas.

Las implementaciones base aceptadas [2046_implementation.java](2046_implementation.java), [2046_implementation.py](2046_implementation.py), [2046_implementation.rs](2046_implementation.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Go original usa scanner; C++/Go nuevos leen nombres completos y celdas fijas. Contar espacios al envolver, conservar orden Tuesday/Thursday/Saturday, filas vacías, caja y relleno derecho. Java usa listas tipadas y builder pequeño; Rust, cadenas propias; Python, listas independientes bajo CPython3.12.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2046_implementation.cpp](2046_implementation.cpp) | G++ 13.2 x64 | implementation | O(L+WCH) | AC | 0.015 s | 436 KB | 11293468 |
| [2046_implementation.go](2046_implementation.go) | Go 1.14 x64 | implementation | O(L+WCH) | AC | 0.031 s | 1112 KB | 11293471 |
| [2046_implementation.java](2046_implementation.java) | Java 1.8 | implementation | O(L+WCH) | AC | 0.093 s | 524 KB | 11328370 |
| [2046_implementation.py](2046_implementation.py) \* | Python 3.12 x64 | implementation | O(L+WCH) | AC | 0.078 s | 536 KB | 11293472 |
| [2046_implementation.rs](2046_implementation.rs) \* | Rust 1.75 x64 | implementation | O(L+WCH) | AC | 0.015 s | 232 KB | 11293480 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2046_implementation_optimized.cpp](2046_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(L+B) | AC | 0.015 s | 112 KB | 11315447 |
| [2046_implementation_optimized.go](2046_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(L+B) | AC | 0.015 s | 276 KB | 11315843 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
