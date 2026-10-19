# 1986. Expansión exacta de mezclas recursivas

[Timus 1986](https://acm.timus.ru/problem.aspx?space=1&num=1986) · dificultad 1177 · matrix

Problema original de Pavel Klimov, del Campeonato Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada mezcla se define mediante porcentajes enteros de otros componentes.
Un componente con receta propia es una mezcla; los demás son
ingredientes básicos. Expandir cada receta en porcentajes de todos los
ingredientes básicos, incluidos ceros, en orden lexicográfico. Se
permiten autorreferencias y ciclos, y se garantiza una expansión única.

Hay como máximo `n=10` recetas y `m=10` ingredientes básicos. Los
nombres tienen de 1 a 10 letras latinas minúsculas. Cada porcentaje de
entrada es un entero de 1 a 100 y cada receta suma 100. Límites: 0,5
segundos y 64 MB.

## Entrada

Líneas de recetas hasta EOF, sin contador inicial. Formato: `name :
component percentage component percentage ...`. Las recetas y sus
componentes están ordenados lexicográficamente.

## Salida

Para cada receta, una línea `name : base percentage ...`, con nombres de
recetas y todos los ingredientes básicos globales en orden
lexicográfico. Incluir ceros explícitos para ingredientes ausentes. Cada
receta expandida suma 100%.

## Evaluación

Un comprobador resuelve las ecuaciones de forma exacta y compara cada
porcentaje con error absoluto o relativo 10⁻³; también verifica los
nombres, su orden y los totales.

## Ejemplos

Entrada 1:

```
razduv : cucumber 30 razgon 50 tomato 20
razgon : bread 40 cucumber 20 razduv 40
```

Salida 1:

```
razduv : bread 25.0 cucumber 50.0 tomato 25.0
razgon : bread 50.0 cucumber 40.0 tomato 10.0
```

Entrada 2:

```
razduv : cucumber 100
razgon : tomato 100
```

Salida 2:

```
razduv : cucumber 100.0 tomato 0
razgon : cucumber 0 tomato 100.0
```

## Solución

Recoger y ordenar todos los nombres de recetas. Los componentes fuera de
ese conjunto son ingredientes básicos; ordenar también su unión. Sea
`P[i,j]` el porcentaje de la receta `j` dentro de `i`, y `b[i]` el
porcentaje directo de un ingrediente básico elegido. Su fracción final
`x[i]`, entre cero y uno, satisface `A x=b`, donde `A=100I−P`. El lado
derecho es el porcentaje de entrada, sin multiplicarlo otra vez por 100.

La expansión válida única garantiza un sistema no singular. Calcular
`d=det(A)` y, para cada posición `i` e ingrediente, `dᵢ=det(A con la
columna i reemplazada por b)`. Por Cramer, `x[i]=dᵢ/d`. Usar solo
enteros hasta imprimir evita pérdida de precisión en ciclos que vuelven
repetidamente al inicio y escapan hacia ingredientes básicos tras
transiciones muy raras.

### Determinantes sin fracciones

Aplicar eliminación de Bareiss a una copia de la matriz entera. El
pivote anterior empieza en 1. En la etapa `k`, buscar un elemento no
nulo de la columna `k` desde la diagonal hacia abajo, intercambiar esa
fila y registrar el signo. Si no existe pivote, el determinante es cero,
lo cual es correcto para un ingrediente ausente. Para `i,j>k`,
actualizar `(a[i,j]·pivot−a[i,k]·a[k,j])/previous` y después anular la
columna eliminada. La división es exacta. Guardar el pivote actual como
anterior. El último elemento diagonal, ajustado por el signo, es el
determinante.

¿Por qué bastan 128 bits con signo? Cada fila de `[A | −b]` es una suma
ponderada de vectores `eᵢ−eⱼ` o `eᵢ`, con pesos enteros no negativos que
suman 100. Restringiendo filas y columnas, una matriz de esos vectores
de incidencia tiene determinante 0 o ±1: expandir una columna con a lo
sumo un elemento no nulo; si no existe, todas las filas y columnas
tienen dos y las sumas de filas son cero. Por multilinealidad, todo
menor de orden `k` está acotado por `100ᵏ`. La sustitución de columna
conserva la cota salvo un cambio de signo. Bareiss almacena menores. Con
diez filas, la mayor resta antes de dividir combina dos productos de
menores de orden nueve: como máximo `2·100¹⁸=2·10³⁶<2¹²⁷`. Los
determinantes finales no superan `10²⁰`; no hay desbordamiento.

### Salida cuya suma es exacta

Tomar `S=10⁶` unidades por punto porcentual y calcular
`u[b]=floor(100S·d_b/d)`. Las fracciones son no negativas y suman uno,
así que los redondeos hacia abajo suman como máximo `100S`. Añadir las
unidades faltantes al componente de mayor numerador. Faltan menos de
`m≤10` unidades. Imprimir seis cifras decimales da suma exactamente 100
y error absoluto menor de `10⁻⁵` puntos por componente, inferior al
`10⁻³` requerido. El producto de formato no supera `10²⁸`, también
dentro de 128 bits.

En el primer ejemplo, sustituir la segunda ecuación en la primera da
para `razduv` 25% bread, 50% cucumber y 25% tomato; sustituyendo de
vuelta se obtiene 50%, 40%, 10% para `razgon`. El segundo ejemplo ya usa
ingredientes básicos, pero también debe mostrar el otro ingrediente
global con cero.

Se calculan como máximo `nm+1` determinantes, cada uno con `O(n³)`
operaciones enteras. Tiempo `O((nm+1)n³)`, espacio de matrices y
numeradores `O(n²+nm)`. Las magnitudes enteras cumplen las cotas
anteriores.

Trampas:

- Leer hasta EOF y clasificar componentes después de reunir todos los
  nombres de recetas.
- Las referencias futuras, propias y cíclicas requieren ecuaciones, no
  sustitución recursiva.
- `A=100I−P` calcula fracciones; convertir a porcentajes una sola vez al
  imprimir.
- Un determinante de columna reemplazada igual a cero indica un
  componente nulo, no un sistema inválido.
- Registrar el signo de intercambios y el pivote anterior de Bareiss;
  usar división entera exacta.
- Mostrar todos los ingredientes básicos en cada receta, incluidos los ceros.

## Notas por lenguaje

Python usa enteros de precisión arbitraria, Go `math/big.Int` y Java
`BigInteger`. C++ usa `__int128_t` con signo y Rust `i128`; la prueba
cubre sus valores intermedios. Todos formatean directamente unidades
enteras de micropercentaje, sin depender de la configuración regional.
Los empates de componente máximo pueden asignar el residuo a
ingredientes distintos con la misma cota de error.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1986_matrix.cpp](1986_matrix.cpp) | G++ 13.2 x64 | matrix | O((n*m+1)*n^3) | AC | 0.015 s | 496 KB |
| [1986_matrix.go](1986_matrix.go) | Go 1.14 x64 | matrix | O((n*m+1)*n^3) | AC | 0.031 s | 6384 KB |
| [1986_matrix.java](1986_matrix.java) | Java 1.8 | matrix | O((n*m+1)*n^3) | AC | 0.140 s | 5616 KB |
| [1986_matrix.py](1986_matrix.py) | Python 3.12 x64 | matrix | O((n*m+1)*n^3) | AC | 0.093 s | 828 KB |
| [1986_matrix.rs](1986_matrix.rs) | Rust 1.75 x64 | matrix | O((n*m+1)*n^3) | AC | 0.015 s | 300 KB |
