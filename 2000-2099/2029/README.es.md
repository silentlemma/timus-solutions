# 2029. Distancia a un estado arbitrario de discos

[Timus 2029](https://acm.timus.ru/problem.aspx?space=1&num=2029) · dificultad 601 · math

Problema original de Nikita Sivukhin y Édouard Lucas, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay tres postes `A`, `B`, `C` y `n` discos distintos de tamaños 1 a `n`.
Todos empiezan en `A`, con los pequeños encima de los grandes. Un
movimiento lleva un disco superior a otro poste vacío o con un disco
superior mayor. Calcula el mínimo para llegar a la asignación objetivo.
La posición `i`, desde uno, indica el poste del disco de tamaño `i`: el
menor aparece primero. El orden de cada poste lo fijan los tamaños, así
que toda cadena de `A,B,C` representa un estado válido.

Restricciones: `1 ≤ n ≤ 50`, 1 segundo, 64 MB. Se garantiza que una
respuesta existente no supera `10^18`; de hecho todos los estados
legales son alcanzables en como máximo `2^n-1` movimientos.

## Entrada

La primera línea contiene `n`; la segunda, exactamente `n` letras
mayúsculas `A`, `B`, `C`.

## Salida

El mínimo número de movimientos. El formato admite `-1` para un estado
inalcanzable, pero la demostración garantiza que todo caso legal de esta
tarea es alcanzable.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
1
A
```

```
0
```

```
4
BBBB
```

```
15
```

```
7
BCCBABC
```

```
95
```

## Solución

Considera los `m` discos restantes, todos empezando en `s`. Si el mayor,
`m`, termina también en `s`, déjalo y resuelve el subproblema menor. Si
termina en `d` distinto, sea `u` el tercer poste: lleva la torre de
`m-1` discos a `u`, mueve el mayor a `d` y resuelve el objetivo menor
desde la esquina `u`. Las dos primeras partes cuestan
`(2^(m-1)-1)+1 = 2^(m-1)`.

El traslado de una torre completa cuesta `T(m)=2^m-1`. Antes del primer
movimiento del mayor, los pequeños deben formar una torre en el tercer
poste, con al menos `T(m-1)` movimientos. Después de su último
movimiento al destino, la torre pequeña necesita otros `T(m-1)`. La
construcción recursiva usual con un movimiento del mayor alcanza
`T(m)=2T(m-1)+1`.

La construcción para un objetivo arbitrario usa, por inducción, como
máximo `2^m-1`: solo mueve los pequeños, o paga `2^(m-1)` al principio y
como máximo `2^(m-1)-1` después. Esto demuestra también la
alcanzabilidad.

La legalidad de los movimientos pequeños no depende del lugar del mayor:
caben sobre él o sobre un poste vacío. Si el mayor visita un mismo poste
dos veces, elimina sus movimientos entre esas visitas manteniendo todos
los pequeños. Sigue siendo legal, con el mismo final y menos
movimientos. Su ruta óptima de postes es, por tanto, simple. Si inicio y
final coinciden, no se mueve; si difieren, solo quedan un movimiento
directo o dos por `u`. La ruta `s→u→d` exige primero la torre pequeña de
`s` a `d` y luego de `d` a `s`, más dos movimientos del mayor: al menos
`2T(m-1)+2 = 2^m`. Ya supera la construcción directa. Luego el mayor se
mueve una sola vez cuando su destino difiere, justificando la
recurrencia óptima.

Itera con `source = A` y respuesta cero, recorriendo índices desde `n-1`
hasta 0. Si el destino del índice `i` difiere de `source`, añade `2^i` y
cambia `source` al tercer poste; en otro caso no cambies nada.
Codificando postes como 0, 1, 2, el tercero es `3-source-target`.
`source` representa la esquina inicial del subproblema menor.

El primer ejemplo ya es inicial: cero. El segundo traslada cuatro discos
completos: `2^4-1=15`. Para `BCCBABC`, el recorrido suma
`64+16+8+4+2+1=95`; el disco 6 ya coincide con el inicio de su
subproblema.

Tiempo `O(n)`, estado del recorrido `O(1)` y entrada almacenada `O(n)`.
No se construye una secuencia de movimientos ni el grafo exponencial de estados.

Trampas:

- La entrada escribe el menor primero, mientras que el cálculo empieza
  por el mayor.
- Actualiza el origen del subproblema solo cuando añades una contribución.
- El destino no tiene que estar en una ruta óptima fija de la torre
  completa `A` a `B`.
- Usa un uno de 64 bits al desplazar: `2^50-1 = 1125899906842623` excede
  32 bits.
- No hay estados inalcanzables entre las asignaciones válidas de esta tarea.

## Notas por lenguaje

C++ usa `1LL`, Go `int64(1)`, Java `1L` y Rust `1_u64` antes del
desplazamiento. Python tiene enteros exactos. Los postes usan enteros
ordinarios; la resta sin signo de Rust es segura en la rama de postes
distintos. No hacen falta potencias en coma flotante.

## Soluciones optimizadas

La versión optimizada en C++ usa un búfer fijo para las etiquetas de los 50 discos como máximo. Al recorrer los discos desde el mayor, añade un bit a la respuesta en cada paso. Ese bit vale uno si la clavija de destino difiere de la clavija de origen actual. El tiempo es O(n) y el espacio adicional al búfer de entrada es O(1). Las métricas corresponden al envío 11316969.

**Envíos de las versiones sencillas en Timus**

Java 1.8 №11317028 · G++ 13.2 x64 №11322304 · Go 1.14 x64 №11322305 · Python 3.12 x64 №11322306 · Rust 1.75 x64 №11322307.

La versión de Python lee las etiquetas de las clavijas como bytes y construye la respuesta bit a bit, del disco mayor al menor. Python 3.12 x64, envío 11320817. Tiempo 0,078 → 0,093 s, memoria 460 → 360 KB.

Go recorre las etiquetas de las clavijas al revés y construye el número de movimientos bit a bit. Go 1.14 x64, envío 11322415. Tiempo 0,031 → 0,031 s, memoria 1228 → 804 KB.

Rust determina la respuesta bit a bit, procesando las varillas de destino desde el disco mayor hasta el menor. Rust 1.75 x64, envío 11323324. Tiempo 0,031 → 0,031 s, memoria 236 → 52 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2029_math.cpp](2029_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 420 KB | 11322304 |
| [2029_math.go](2029_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1228 KB | 11322305 |
| [2029_math.java](2029_math.java) | Java 1.8 | math | O(n) | AC | 0.109 s | 344 KB | 11317028 |
| [2029_math.py](2029_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 460 KB | 11322306 |
| [2029_math.rs](2029_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 236 KB | 11322307 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2029_math_optimized.cpp](2029_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 116 KB | 11316969 |
| [2029_math_optimized.py](2029_math_optimized.py) \* | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 360 KB | 11320817 |
| [2029_math_optimized.go](2029_math_optimized.go) \* | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 804 KB | 11322415 |
| [2029_math_optimized.rs](2029_math_optimized.rs) \* | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 52 KB | 11323324 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
