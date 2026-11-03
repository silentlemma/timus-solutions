# 1114. Colocar hasta A y B bolas idénticas de dos colores en N cajas

[Timus 1114](https://acm.timus.ru/problem.aspx?space=1&num=1114) · dificultad 194 · combinatorics, math

Problema original de la primera competición de selección del equipo búlgaro para la IOI.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` cajas en fila (`1 ≤ N ≤ 20`), `A` bolas rojas idénticas y `B`
bolas azules idénticas (`0 ≤ A, B ≤ 15`). En cada caja puede ir cualquier
número de bolas de cualquier color, las cajas pueden quedar vacías y las
bolas pueden quedar sin usar. Cuenta las distintas colocaciones.

Límite de tiempo: 0,6 segundos. Límite de memoria: 64 MB.

## Entrada

`N A B` en una línea.

## Salida

El número de colocaciones.

## Evaluación

Comparar un token entero exacto. El nuevo Python ejecutó las 5120 ternas legales y 12 entradas del repositorio tanto en CPython 3.12 como en PyPy 3.10; cada entorno lanzó además 12 procesos nuevos para las entradas del repositorio. Las respuestas se contrastaron con DP independiente que distribuye caja por caja y suma todas las cantidades usadas permitidas por color. Incluye cero bolas y el máximo superior a 64 bits con signo. Java conserva por separado su prueba de coeficientes y producto sin signo vinculada al código exacto para las 5120 ternas.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 1 1
```

Salida:

```
9
```

## Solución

Los colores son independientes. Una distribución de hasta `A` bolas
rojas en `N` cajas distintas se extiende de forma única a exactamente `A`
bolas en `N + 1` cajas, poniendo las no usadas en la extra. A la inversa,
se elimina esa caja. Por estrellas y barras hay `C(N + A,N)` formas;
la independencia da `C(N + A,N) × C(N + B,N)`.

Las bases legibles C++, Go, Java y Rust construyen Pascal con `TOP = 40`
y consultan dos valores: tiempo y espacio `O(TOP²)`, con índices necesarios
de hasta 35. Python llama dos veces a `math.comb`, sin tabla. Como los
límites son fijos, todas son `O(1)` respecto al tamaño permitido.
Se conservan las cinco fuentes Accepted originales.

Los coeficientes consultados no superan `C(35,15) = 3247943160 < 2^32`;
esto no afirma que toda la tabla Pascal mayor quepa en 32 bits. El máximo
`10549134770590785600` supera 64 bits con signo, pero es menor que `2^64`.
C++, Go y Rust usan producto sin signo; Java guarda los 64 bits bajos
y los imprime con `Long.toUnsignedString`. Los enteros Python no están
limitados a una palabra de máquina.

## Soluciones optimizadas

Java calcula cada combinación por productos: tras el paso i, r=C(N+i,i), y la siguiente división es exacta. El producto previo no supera 35*C(35,15)=113678010600 y cabe en long con signo. La respuesta puede superar 64 bits con signo, pero es menor que 2^64: se conservan los 64 bits y se usa Long.toUnsignedString. Elimina Pascal y preserva las bases claras.

Java se admite por reducir memoria un 77,4%; una diferencia temporal de un solo tic no prueba una mejora de velocidad.

La optimización Python mantiene estrellas y barras y la base breve con math.comb. Lee texto del flujo estándar existente, importa solo los flujos de sys y calcula cada coeficiente mediante productos y divisiones exactas. Tras el paso i, coefficient=C(N+i,i), por lo que dividir entre i es exacto. Cada factor es como máximo C(35,15)=3247943160 y el producto previo a dividir no supera 113678010600. Multiplica los dos coeficientes completos una sola vez y escribe el decimal exacto. El entero ilimitado de Python admite el máximo 10549134770590785600, superior a 64 bits con signo. No necesita Pascal ni importar math. Usa O(A+B) pasos, con tamaños numéricos acotados por las restricciones.

Su Accepted 11309624 usa PyPy 3.10 x64: 0,125 s y 240 KB, frente a la base CPython 3.12 intacta con 0,078 s y 372 KB. Reduce memoria 35,5%, pero el tiempo aumenta 60,3%. Se admite solo por memoria y conserva la estrella por no alcanzar la meta. Cada medición pertenece a su envío e intérprete reales; no se trasladan métricas entre intérpretes.

- `1114_combinatorics_math.java`: 0.093 s / 372 KB; base `1114_combinatorics.java`: 0.109 s / 1648 KB; cambio respecto a la base: tiempo -14.7%, memoria -77.4%.
- `1114_combinatorics_optimized.py`: 0.125 s / 240 KB; base `1114_combinatorics.py`: 0.078 s / 372 KB; cambio respecto a la base: tiempo +60.3%, memoria -35.5%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1114_combinatorics.cpp`; fuente que cubre `1114_combinatorics.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 45/45.

- Go: base didáctica preferida `1114_combinatorics.go`; fuente que cubre `1114_combinatorics.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1114_combinatorics.java`; fuente que cubre `1114_combinatorics_math.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1114_combinatorics.py`; fuente que cubre `1114_combinatorics_optimized.py`; puestos tiempo/memoria 22/1, registros de otros autores 24/24.

- Rust: base didáctica preferida `1114_combinatorics.rs`; fuente que cubre `1114_combinatorics.rs`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1114_combinatorics.cpp](1114_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(TOP^2) | AC | 0.015 s | 140 KB | 11279222 |
| [1114_combinatorics.go](1114_combinatorics.go) | Go 1.14 x64 | combinatorics | O(TOP^2) | AC | 0.015 s | 1060 KB | 11279223 |
| [1114_combinatorics.java](1114_combinatorics.java) | Java 1.8 | combinatorics | O(TOP^2) | AC | 0.109 s | 1648 KB | 11279225 |
| [1114_combinatorics.py](1114_combinatorics.py) | Python 3.12 x64 | combinatorics | O(1) under fixed bounds | AC | 0.078 s | 372 KB | 11279224 |
| [1114_combinatorics.rs](1114_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(TOP^2) | AC | 0.015 s | 232 KB | 11279226 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1114_combinatorics_math.java](1114_combinatorics_math.java) | Java 1.8 | combinatorics, math | O(A+B) exact coefficient steps; bounded storage | AC | 0.093 s | 372 KB | 11308284 |
| [1114_combinatorics_optimized.py](1114_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O(A+B) exact coefficient steps; bounded storage | AC | 0.125 s | 240 KB | 11309624 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
