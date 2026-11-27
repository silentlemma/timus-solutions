# 1140. El camino más corto de vuelta al centro de una cuadrícula hexagonal tras un paseo

[Timus 1140](https://acm.timus.ru/problem.aspx?space=1&num=1140) · dificultad 383 · geometry

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un pantano está dividido en celdas hexagonales, y tres de las seis
direcciones entre celdas vecinas se llaman `X`, `Y` y `Z`, con `Y` entre
`X` y `Z`. Un estudiante empieza en la celda central y recorre hasta 32000
tramos rectos, cada uno dado por una dirección y una longitud con signo
no nula; una longitud negativa va en sentido contrario. El estudiante
nunca se aleja más de 100 celdas del centro. Describe un camino de vuelta
al centro por el menor número de celdas, en el mismo formato.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` (`1 ≤ n ≤ 32000`) y luego `n` líneas con la letra de la dirección y
una longitud con signo.

## Salida

El número de tramos `m ≥ 0` del camino de vuelta y luego los tramos.

## Evaluación

Se acepta cualquier camino más corto. El comprobador verifica el formato,
que el camino acaba en el centro y que su longitud total es igual a la
distancia hexagonal desde la última celda.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
Z -2
Y 3
Z 3
X -1
```

Salida:

```
2
Y -2
Z -2
```

## Solución

En una cuadrícula hexagonal la dirección del medio es la suma de las otras
dos: un paso por `Y` lleva a la misma celda que un paso por `X` seguido de
uno por `Z`. Así que se suman las longitudes por dirección y el final del
paseo se escribe como `a·X + b·Z`, con `a = X + Y` y `b = Z + Y`. Un camino
de vuelta con `m` pasos por `Y` necesita además `a − m` por `X` y `b − m`
por `Z`, hacia atrás, y tiene `|a − m| + |m| + |b − m|` pasos. Una suma de
distancias de `m` a los puntos `a`, `0` y `b` es mínima en su mediana, así
que se toma `m` como la mediana de `a`, `0` y `b` y se imprimen las partes
no nulas de `X −(a − m)`, `Y −m`, `Z −(b − m)`. `O(n)`.

El estado geométrico son tres totales y hasta tres segmentos candidatos:
O(1) palabras numéricas acotadas en todas las versiones, sin recursión.
C++/Go/Java simples leen incrementalmente con búferes acotados. Python
simple retiene entrada y tokens split, Rust el String: O(I) bytes
adicionales. Go/Rust optimizados no retienen entrada completa; para
Rust esto sí cambia la base. Python optimizado guarda bloque de 4096
bytes, partes split y token incompleto: O(4096+T), longitud máxima de
token T, en vez de O(I). Leer I bytes añade O(I) tiempo a O(n)
actualizaciones geométricas.

Detalles a tener en cuenta:

- cuando `a` y `b` tienen el mismo signo, parte del camino va por `Y`;
  cuando los signos difieren, `m = 0` y `Y` no se usa;
- no se permiten tramos de longitud cero, así que se descartan, y la
  respuesta puede tener `0` tramos;
- la entrada debe tener al menos un tramo aunque termine en el centro
  (prueba 03); en el modo 1, el generador usa dos tramos que se cancelan
  cuando el tamaño solicitado produciría una ruta de entrada vacía;
- puede haber varios caminos más cortos; se acepta cualquiera.

Las respuestas se comprobaron con el comprobador en todas las pruebas y en
1200 paseos aleatorios; la fórmula de distancia del comprobador se comparó
con una búsqueda en anchura sobre todas las celdas a 100 o menos del
centro.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

Las dos optimizadas nativas conservan la fórmula de mediana. Go cambia
map[string]int por un arreglo de tres enteros, sort.Ints de tres valores
por clamp explícito, fmt.Fscan por Scanner/ScanWords y strconv.Atoi,
y líneas fmt por pequeño búfer de bytes. Su base ya guardaba solo
tres totales. Rust sustituye read_to_string y parser genérico por
stdin.lock().bytes() y lector decimal con signo, con tres totales i32.
Su base ya hallaba mediana con min/max: clamp es la misma operación
constante, no nueva geometría. Se omiten longitudes cero y ambas
bases legibles permanecen.

El envío aceptado en Rust 1.75 x64 tarda 0.031 s frente a 0.015 s de la base y usa 188 KB frente a 344 KB.

La caché exacta confirma C++/Java reutilizados solo tiempo bajo 1 MiB.
Python simple 0.125 s/776 KB falla la referencia temporal pequeña;
la revisión separada 0.062 s/828 KB cubre Python. Go simple cumple
ambas métricas pequeñas, Go optimizado solo tiempo; ambos Rust cumplen
puestos temporales ordinarios bajo 1 MiB. Rigen los
[criterios compartidos](../../RATING_CRITERIA.md), sin estrellas en
fuentes didácticos ni copias optimizadas idénticas.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1140_geometry_implementation_optimized.py`. Sustituye lectura/split
de texto completo por bloques os.read, llevando solo token incompleto
entre bloques. Sigue sumando tres direcciones en un diccionario,
luego deriva dos ejes y ordena (a,0,b) como la base; no acumula
directamente dos ejes. Claves byte y os._exit tras vaciar salida
completa son cambios de implementación; geometría y base permanecen.

Accepted #11329035 (Python 3.12 x64): **0.062 s / 828 KB**. Comparación archivada: `1140_geometry.py` (Python 3.12 x64) — 0.125 s / 776 KB (#11279441).

La revisión Python optimizada solo nombra el umbral ASCII intacto
32 de espacio al separar bloques. Fórmula de mediana, valores,
base y comentarios sustantivos se conservan.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes suman las longitudes y toman la misma mediana.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1140_geometry.cpp](1140_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 188 KB | 11279439 |
| [1140_geometry.go](1140_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1348 KB | 11279440 |
| [1140_geometry.java](1140_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.093 s | 828 KB | 11279442 |
| [1140_geometry.py](1140_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.125 s | 776 KB | 11279441 |
| [1140_geometry.rs](1140_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.015 s | 344 KB | 11279443 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1140_geometry_optimized.go](1140_geometry_optimized.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 908 KB | 11311067 |
| [1140_geometry_optimized.rs](1140_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 188 KB | 11311072 |
| [1140_geometry_implementation_optimized.py](1140_geometry_implementation_optimized.py) | Python 3.12 x64 | geometry, implementation | O(n) | AC | 0.078 s | 796 KB | 11331074 |
