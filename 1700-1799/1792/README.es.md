# 1792. Código de Hamming

[Timus 1792](https://acm.timus.ru/problem.aspx?space=1&num=1792) · dificultad 84 · implementation

Problema original de Sofia Tekhazheva (preparado por Olga Soboleva), del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuatro discos que se cortan tienen un bit cada uno, y tres pétalos, las
zonas comunes a tres discos, tienen la paridad de la suma de los discos
que los cubren. En el orden de la figura del enunciado, el pétalo j
está en todos los discos salvo el disco j, y el cuarto disco cubre los
tres pétalos. Se cambió como mucho uno de los siete bits. Restaurar un
código válido.

## Entrada

Siete bits: los cuatro discos y luego los tres pétalos.

## Salida

Los siete bits de un código válido que difiera de la entrada en a lo
sumo un lugar.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos. Imprime los siete bits recuperados en el orden original.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 1 0 1 1 0 1
```

Salida:

```
0 1 0 0 1 0 1
```

### Ejemplo 2

Entrada:

```
1 1 1 1 1 1 1
```

Salida:

```
1 1 1 1 1 1 1
```

## Solución

Se comprueba la palabra tal cual: el pétalo j debe ser igual a la suma
de los discos distintos del disco j, módulo 2. Si falla, se prueba a
cambiar cada uno de los siete bits por turno y se conserva el primer
cambio que hace válida la palabra. Dos palabras válidas siempre
difieren en al menos tres lugares, así que la respuesta es única.
`O(1)`.

En el primer ejemplo los tres pétalos están mal, y solo el cuarto disco
está bajo todos ellos; cambiarlo de 1 a 0 hace que los pétalos sean 1,
0, 1, como están escritos.

Trampas:

- el bit cambiado puede ser un pétalo, no un disco;
- la palabra puede ser ya válida, y entonces se imprime sin cambios.

Cada una de las 128 entradas posibles da la misma respuesta que una
implementación aceptada independiente.

## Soluciones optimizadas

`1792_bitmask_optimized.py`. Mantiene decodificación por síndrome, empaquetando siete bits en un entero. Tres máscaras derivadas de paridad usan bit_count módulo dos; síndrome no nulo identifica una columna de datos/control errónea. Invierte ese bit y rellena plantilla de 14 bytes. Máscaras son ecuaciones, no tabla de respuestas. Trabajo lógico O(1), lectura/split del texto de longitud L O(L) tiempo/espacio. Salida directa y os._exit(0) dentro de main reducen sobrecostes. Los 128 recibidos se comprobaron independientemente desde 16 códigos válidos con cero/un error. Conserva el PyPy anterior de menor memoria y la base simple de siete valores.

Fuente exacto: Python 3.12 x64 Accepted #11327532: 0.078 s / 828 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 1/69; 68/69. Admisión estricta usa solo tiempo bajo 1024 KB: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. Conserva asterisco por la meta propia de primer puesto en ambas. La variante anterior conservada tiene su par propio #11325479 (PyPy 3.10 x64): 0.14 s / 264 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `1792_bitmask_optimized.py`: 0.078 s / 828 KB; base didáctica conservada `1792_implementation.py` (Python 3.12 x64): 0.093 s / 464 KB.

`1792_bitmask.py`. Decodifica tres paridades mediante síndrome en vez de construir y probar ocho candidatos de siete bits. Un bit de síndrome señala una paridad; 7 señala dato 3; los otros síndromes de dos bits señalan el dato por su comprobación ausente. Bajo a lo sumo un error invierte ese bit, o no cambia un síndrome cero. Este método bitmask distinto tiene nombre propio; conserva la enumeración sencilla. Ambos tienen tamaño constante para siete bits. La fila Accepted indica el runtime real y sus medidas emparejadas. Vacía salida antes de os._exit(0), que omite cierre del intérprete; la mejora medida de memoria depende del runtime y no implica aceleración asintótica.

Frente a `1792_implementation.py`: tiempo 0.093 s → 0.14 s; memoria 464 KB → 264 KB.

Las soluciones optimizadas (C++, Java) leen los siete bits como
caracteres sueltos con `getchar` y `System.in.read` en lugar de
`iostream` y `Scanner`, y escriben la respuesta carácter a carácter
(C++) o como un solo arreglo de bytes (Java). La búsqueda entre los
cambios de un solo bit es la misma. C++: 84 KB en lugar de 396 KB, con
el mismo tiempo; Java: 0.109 s en lugar de 0.156 s y 380 KB en lugar de
1604 KB.

`1792_bitmask.rs`. Sustituye las modificaciones de prueba por un síndrome de paridad de tres bits. Un bit invertido altera exactamente su columna de comprobaciones; las siete columnas son los patrones no nulos distintos de tres bits. El síndrome cero no requiere cambio; en otro caso se invierte el único bit de esa columna. Con como máximo un error se restablecen todas las comprobaciones. Una palabra fija de siete bytes sustituye los vectores candidatos clonados; tiempo y espacio O(1). Rust usa el entorno de C para entrada y salida, evitando cadenas String completas decodificadas y el formato de Rust. La fuente sencilla aceptada se conserva sin cambios.

Frente a `1792_implementation.rs`: tiempo 0.046 s → 0.046 s; memoria 228 KB → 60 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1792_bitmask.py`: puesto de tiempo 63/69 y de memoria 2/69 en esta muestra comparable.

`1792_bitmask.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1792_implementation.cpp](1792_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 396 KB | 11303512 |
| [1792_implementation.go](1792_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1168 KB | 11289857 |
| [1792_implementation.java](1792_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1604 KB | 11303513 |
| [1792_implementation.py](1792_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 464 KB | 11303514 |
| [1792_implementation.rs](1792_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB | 11303515 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1792_implementation_optimized.cpp](1792_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 84 KB | 11303639 |
| [1792_implementation_optimized.java](1792_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 380 KB | 11303516 |
| [1792_bitmask.rs](1792_bitmask.rs) \* | Rust 1.75 x64 | bitmask | O(1) | AC | 0.046 s | 60 KB | 11324860 |
| [1792_bitmask.py](1792_bitmask.py) \* | PyPy 3.10 x64 | bitmask | O(1) | AC | 0.14 s | 264 KB | 11325479 |
| [1792_bitmask_optimized.py](1792_bitmask_optimized.py) \* | Python 3.12 x64 | bitmask | O(1) logical work; O(L) input time/storage | AC | 0.078 s | 828 KB | 11327532 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
