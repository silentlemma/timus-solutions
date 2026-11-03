# 1491. Totales tras sumas en intervalos inclusivos

[Timus 1491](https://acm.timus.ru/problem.aspx?space=1&num=1491) · dificultad 203 · prefix_sums

Problema original de Alexander Toropov, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `2 ≤ N ≤ 100000` posiciones con total inicial cero. La operación
0 da `c` monedas a cada posición `a..b`, inclusive; después hay otra
operación por cada `i = 1..N`. Siempre `1 ≤ a ≤ b ≤ N`, `1 ≤ c ≤ 10000`.
La operación `i` excluye su posición (`a_i > i` o `b_i < i`); la operación
0 no tiene esa restricción. Obtenga los totales finales. No se descuenta
ningún coste a las posiciones. Tiempo: 1 segundo. Memoria: 64 MB.

## Entrada

`N`, la terna inicial `a b c`, y después las otras `N` ternas en orden.

## Salida

Los `N` totales en orden de posición, separados por espacios.

## Evaluación

El Python compacto real pasó 812 entradas: 800 pequeñas válidas
frente a sumar directamente cada regalo a cada receptor, más 12 casos
de frontera o máximos con totales conocidos independientemente.
Incluyen `N = 2, 1023, 1024, 1025, 2048, 100000`, mil millones de monedas
y diferencias negativas grandes. Los regalos excluyen al propio donante
como exige el problema. El máximo legal es `N × 10000` porque una
posición no recibe su propio regalo; la cota más amplia anterior también
cubre las celdas intermedias. Los cinco candidatos reales pasaron además
14 entradas del repositorio cada uno en Docker y obtuvieron sus propios
Accepted. Las 812 comprobaciones fueron ejecuciones Python, no 812
ejecuciones de cada lenguaje.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
2 3 2
2 4 1
3 4 1
1 2 1
1 1 1
```

Salida:

```
2 4 4 2
```

### Ejemplo 2

Entrada:

```
7
1 7 1
2 3 4
3 5 3
1 2 1
5 7 4
2 4 10
3 4 2
1 6 3
```

Salida:

```
5 19 23 19 11 8 5
```

## Solución

Inicializamos un arreglo de diferencias de `N + 2` celdas.
En cada una de las `N + 1` operaciones sumamos `c` en `a` y restamos
`c` en `b + 1`; las sumas prefijas de `1..N` dan los totales.

Una operación aporta `+c` al prefijo `j` cuando `j ≥ a`, y después
`−c` cuando `j ≥ b + 1`: exactamente `c` dentro de `a ≤ j ≤ b` y cero
fuera. Sumar estas identidades prueba el algoritmo. La celda `N + 1`
permite terminar un intervalo en `N`, pero no se imprime. Hay que incluir
la operación inicial; excluir el regalo propio no cambia las sumas.

Con números de entrada y salida de longitud acotada, tiempo y espacio
auxiliar `O(N)`. Las bases nativas legibles usan celdas de 64 bits,
Python listas ordinarias de enteros. Se conservan sin cambios las cinco
fuentes Accepted originales.

## Soluciones optimizadas

La suma `S` de los importes no supera
`(N + 1) × 10000 ≤ 1000010000 < 2^31`. Cada operación cambia una celda
concreta a lo sumo en su importe, por lo que incluso las celdas intermedias
están en `[-S,S]`. El acumulador suma importes positivos activos y está
en `[0,S]`. Bastan enteros con signo de 32 bits, incluidas diferencias
negativas grandes.

Arreglos de 32 bits sustituyen celdas nativas de 64 bits o listas de
objetos Python; ocupan `4 × (N + 2)` bytes en la ABI comprobada. C++ y
Java usan búferes fijos de E/S de 4 KiB y arreglos temporales de diez
bytes para dígitos, suficientes para la cota. Go reduce su búfer de
entrada de 1 MiB a 4 KiB y conserva salida con búfer. Rust lee el flujo
bloqueado y escribe con búfer, sin retener entrada y todas las cadenas
de respuesta. Python usa `array("i")`, lee las líneas indicadas en flujo
y escribe grupos de hasta 1024 cadenas numéricas. Un grupo completo
termina en espacio si quedan números, o salto de línea si no; el último
grupo parcial también termina en salto. No se pierden separadores.

Tiempo y espacio siguen en `O(N)`: es una optimización de implementación
y memoria del mismo algoritmo de diferencias, de ahí `_optimized`.
Cada fuente publicada tiene su propio Accepted de bytes exactos y
reduce memoria al menos un 30%. Menor memoria no implica menor tiempo
registrado; abajo se muestran ambas métricas.

Cambios medidos frente a la base del mismo lenguaje:

- C++: 0.187 s / 980 KB → 0.046 s / 516 KB; reducción de memoria 47.3%.
- Go: 0.031 s / 4540 KB → 0.031 s / 2972 KB; reducción de memoria 34.5%.
- Java: 0.109 s / 8872 KB → 0.125 s / 852 KB; reducción de memoria 90.4%.
- Python: 0.328 s / 35944 KB → 0.250 s / 1236 KB; reducción de memoria 96.6%.
- Rust: 0.046 s / 9428 KB → 0.062 s / 584 KB; reducción de memoria 93.8%.

## Notas por lenguaje

El perfil establecido exige para C++ estar entre el 15% superior o los primeros 10 puestos en tiempo y memoria; para Go, Java, Python/PyPy y Rust exige primero en ambas métricas. Los empates comparten puesto y las muestras vacías se registran aparte.

Instantánea del 2 de noviembre de 2026 (puesto temporal / de memoria; registros filtrados de otros autores):

- C++: 5 / 3; 113 / 113; objetivo cumplido.
- Go: 1 / 1; 0 / 0; muestra vacía; la cobertura formal no demuestra superioridad competitiva.
- Java: 1 / 1; 4 / 4; objetivo cumplido.
- Python: 10 / 1; 20 / 20; objetivo de clasificación pendiente.
- Rust: 1 / 1; 0 / 0; muestra vacía; la cobertura formal no demuestra superioridad competitiva.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1491_prefix_sums.cpp](1491_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.187 s | 980 KB | 11287189 |
| [1491_prefix_sums.go](1491_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 4540 KB | 11287190 |
| [1491_prefix_sums.java](1491_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.109 s | 8872 KB | 11287195 |
| [1491_prefix_sums.py](1491_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.328 s | 35944 KB | 11287194 |
| [1491_prefix_sums.rs](1491_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.046 s | 9428 KB | 11287196 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1491_prefix_sums_optimized.cpp](1491_prefix_sums_optimized.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.046 s | 516 KB | 11308370 |
| [1491_prefix_sums_optimized.go](1491_prefix_sums_optimized.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 2972 KB | 11308372 |
| [1491_prefix_sums_optimized.java](1491_prefix_sums_optimized.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.125 s | 852 KB | 11308375 |
| [1491_prefix_sums_optimized.py](1491_prefix_sums_optimized.py) \* | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.250 s | 1236 KB | 11308367 |
| [1491_prefix_sums_optimized.rs](1491_prefix_sums_optimized.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.062 s | 584 KB | 11308383 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
