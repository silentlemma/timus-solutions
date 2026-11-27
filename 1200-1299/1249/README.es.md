# 1249. ¿Son rectángulos todas las zonas oscuras?

[Timus 1249](https://acm.timus.ru/problem.aspx?space=1&num=1249) · dificultad 221 · implementation

Problema original de Nikita Shamgunov y Leonid Volkov, del Concurso Abierto por Equipos de la Universidad Estatal de los Urales, 15 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da una imagen binaria `N × M` de como máximo 3000 filas y 3000 columnas. Decide si cada componente de unos conectados por lados es un rectángulo lleno paralelo a los ejes. Tocar solo una esquina no conecta celdas. Tiempo: 2,5 segundos. Memoria: 4 MB.

## Entrada

`N M`, seguidos de `N` filas con `M` ceros o unos separados por espacios.

## Salida

Imprime `Yes` si cada componente es un rectángulo lleno; en otro caso, `No`.

## Evaluación

Comparación por tokens: `Yes` o `No` con las mayúsculas indicadas. Los espacios de formato no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
1 1 1
1 0 1
```

Salida:

```
No
```

### Ejemplo 2

Entrada:

```
3 4
1 1 0 1
1 1 0 1
0 0 0 1
```

Salida:

```
Yes
```

## Solución

Una ventana 2 × 2 con exactamente tres celdas oscuras pertenece a una
misma componente que no puede ser un rectángulo lleno. Recíprocamente,
el borde de una componente conectada por lados que no llena un rectángulo
tiene una esquina entrante, también alrededor de un hueco. Esa esquina
produce una ventana con tres celdas oscuras. Basta prohibir esas ventanas.

Se guardan filas adyacentes y se comprueba cada ventana 2×2 al llegar su última celda. Nativos sencillos examinan celdas, Python representa filas por enteros bitset. Lectura O(NM), estado de fila O(M) entradas o bits Python más línea actual. Una imagen máxima 3000×3000 de un byte/píxel ocupa 9000000 bytes y supera 4 MiB; imágenes pequeñas caben, e incluso la máxima empaquetada en bits puede caber. No toda imagen completa es imposible de guardar: el flujo evita el peor almacenamiento no comprimido. Contacto solo en esquina no conecta componentes.

Solo se revisó el comentario inexacto de memoria de estos cinco fuentes; se conservan código ejecutable y explicaciones útiles. Las tablas retienen pares Accepted históricos.

`1249_implementation.cpp` (#11283966); `1249_implementation.go` (#11283967); `1249_implementation.java` (#11283977); `1249_implementation.rs` (#11283979); `1249_implementation_parsing_optimized.go` (#11329324).

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1249_implementation_optimized.rs`. Conserva prueba de suma tres en 2×2. Una fila de bytes con celdas izquierda/superior-izquierda guardadas sustituye dos; actualiza columna tras comprobar. Mismos No anticipado y Yes final. O(NM) tiempo, O(M) espacio.

Frente a `1249_implementation.rs`: tiempo 0.031 s → 0.625 s; memoria 224 KB → 68 KB.

Para dos filas, `B = previous AND current` marca columnas verticales
llenas y `S = previous XOR current` las de una sola celda oscura. Una
ventana prohibida es una columna llena junto a una sencilla; la expresión
`(B AND (S >> 1)) OR (S AND (B >> 1))` comprueba ambos órdenes.

Python factoriza así su expresión anterior y elimina los blancos de la
fila con una transformación. C++ empaqueta columnas en palabras de 64 bits,
lee con un búfer acotado, comprueba cada palabra en paralelo y verifica
explícitamente las parejas que cruzan su límite. Retiene la fila anterior
empaquetada y la palabra actual. La comprobación lógica por fila cuesta
`O(ceil(M/64))`; leer sigue costando `O(N M)` y las filas ocupan `O(M/64)`
palabras. Python usa `O(M)` bits más la línea actual de entrada.

Pares conservados: C++ 0.531 s/208 KB→0.078 s/128 KB (85.3% menos tiempo, 38.5% menos memoria); Python 0.218 s/1532 KB→0.125 s/3684 KB (42.7% menos tiempo, más memoria). Python rápido no se admite solo por tiempo: 3684 KB≥1024 obliga memoria. Su referencia exacta permite 2060.8 KB; falla memoria aunque pase tiempo y conserva estrella. Python sencillo 1532 KB intacto pasa ambas y cubre el lenguaje, sin excepción separada por acelerar.

`1249_implementation_parsing_optimized.go` analiza dimensiones enteras y decodifica bloques directamente en la fila byte actual; luego comprueba ventanas con la anterior. Búfer 8192 bytes con refill/EOF, sin llamada auxiliar por píxel. fastPrint solo admite cadenas y escribe texto fijo Yes/No más salto con búfer reutilizable. No convierte salida numérica; rutinas numéricas son de entrada. Geometría intacta.

El par Accepted Go siguiente pertenece al fuente histórico anterior al comentario revisado. Se conservan pares y versiones sencillas/distintas.

Accepted #11329324 (Go 1.14 x64): **0.031 s / 820 KB**.

## Notas por lenguaje

Python se comparó en 75.254 imágenes pequeñas con un recorrido
independiente de componentes y sus cajas delimitadoras, incluidas todas
las imágenes binarias con cada dimensión hasta cuatro. Ambos programas
reales superaron 14 entradas del repositorio en Docker, incluidas imágenes
3000 × 3000. Se comprobaron además las cuatro orientaciones de esquina
ausente y contactos diagonales en límites de palabras en C++ y Python.

Las posiciones filtradas antiguas del 2 noviembre quedan sustituidas por caché exacta y [criterios compartidos](../../RATING_CRITERIA.md): C++ rápido y Java sencillo pasan solo tiempo; el Go parser histórico pasa tiempo frente al segundo de dos rivales exactos, Go base falla tiempo. Ambos Rust pasan ampliando al mismo lenguaje, no por muestra vacía. C++ base queda docente. Admitir métricas del hash histórico no crea Accepted para bytes revisados.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1249_implementation.cpp](1249_implementation.cpp) | G++ 13.2 x64 | implementation | O(N M) | AC | 0.562 s | 188 KB | 11331141 |
| [1249_implementation.go](1249_implementation.go) | Go 1.14 x64 | implementation | O(N M) | AC | 0.062 s | 1052 KB | 11331015 |
| [1249_implementation.java](1249_implementation.java) | Java 1.8 | implementation | O(N M) | AC | 0.125 s | 476 KB | 11331046 |
| [1249_implementation.py](1249_implementation.py) | Python 3.12 x64 | implementation | O(N M) | AC | 0.218 s | 1532 KB | 11283970 |
| [1249_implementation.rs](1249_implementation.rs) | Rust 1.75 x64 | implementation | O(N M) | AC | 0.046 s | 216 KB | 11331109 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1249_implementation_optimized.cpp](1249_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N M) | AC | 0.078 s | 128 KB | 11308213 |
| [1249_implementation_optimized.py](1249_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N M) | AC | 0.125 s | 3684 KB | 11308214 |
| [1249_implementation_optimized.rs](1249_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(NM) time; O(M) space | AC | 0.625 s | 68 KB | 11325546 |
| [1249_implementation_parsing_optimized.go](1249_implementation_parsing_optimized.go) | Go 1.14 x64 | implementation, parsing | O(nm) time; O(m) row state + bounded input buffer | AC | 0.062 s | 816 KB | 11331016 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
