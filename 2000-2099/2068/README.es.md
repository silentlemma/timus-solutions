# 2068. La paridad del número de divisiones

[Timus 2068](https://acm.timus.ru/problem.aspx?space=1&num=2068) · dificultad 108 · games

Problema original de Alexey Danilyuk, del Concurso Regional por Equipos de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n montones de nueces, cada uno con un número impar de nueces. Dos
jugadores alternan turnos; una jugada divide un montón en tres montones
no vacíos, cada uno de nuevo con un número impar de nueces. Quien no
puede jugar pierde. Daenerys juega primero y luego Stannis. Hallar el
ganador con juego óptimo. Los límites son 1 segundo y 64 MB.

## Entrada

Un n impar, 1 ≤ n ≤ 777, y después n tamaños impares de montones entre
1 y 54321.

## Salida

`Daenerys` si ella gana, y `Stannis` en otro caso.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
3
```

Salida:

```
Daenerys
```

### Ejemplo 2

Entrada:

```
3
1 1 1
```

Salida:

```
Stannis
```

### Ejemplo 3

Entrada:

```
5
777 313 465 99 1
```

Salida:

```
Daenerys
```

## Solución

Aquí la estrategia no importa. Una jugada cambia un montón por tres, así
que el número de montones crece exactamente en dos, y el total de nueces
no cambia. El juego termina exactamente cuando cada montón tiene una
nuez: un montón de 3 o más nueces (impar) siempre se puede dividir como
1 + 1 + (a − 2). En ese momento hay tantos montones como nueces, de modo
que el número de jugadas es siempre (S − n) / 2, la suma de
(aᵢ − 1) / 2 sobre los montones.

Daenerys hace las jugadas impares, así que gana exactamente cuando ese
número es impar. En el tercer ejemplo los montones dan
388 + 156 + 232 + 49 + 0 = 825 jugadas, un número impar. El trabajo es
O(n).

## Soluciones optimizadas

`2068_games_optimized.java`. Conserva XOR de paridades ((montón−1)/2). Lee flujo estándar existente sin array adicional y escribe bytes fijos por System.out.write con flush. Evita codificación String usando flujo estándar normal, sin FileDescriptor. O(N) tiempo, espacio auxiliar constante.

Frente a `2068_games.java`: tiempo 0.109 s → 0.093 s; memoria 480 KB → 340 KB.

`2068_games_optimized.py`. Conserva el total fijo de movimientos: dividir añade dos montones, y uno de tamaño a aporta (a-1)//2 pasos hasta los unitarios. Solo importa la paridad de la suma. Aplica XOR a cada contribución al leer el entero, sin guardar todos los tokens de texto ni sumar el total completo. El lector de 65536 bytes mantiene bloques y un token incompleto; el juego usa un bit. Con tamaños acotados, tiempo O(N) y almacenamiento acotado independientemente de N. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `2068_games.py`: tiempo 0.093 s → 0.109 s; memoria 388 KB → 236 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`2068_games_optimized.py`: puesto de tiempo 33/50 y de memoria 1/50 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2068_games.cpp](2068_games.cpp) | G++ 13.2 x64 | games | O(n) | AC | 0.015 s | 124 KB | 11294416 |
| [2068_games.go](2068_games.go) | Go 1.14 x64 | games | O(n) | AC | 0.031 s | 1108 KB | 11294420 |
| [2068_games.java](2068_games.java) | Java 1.8 | games | O(n) | AC | 0.109 s | 480 KB | 11304044 |
| [2068_games.py](2068_games.py) | Python 3.12 x64 | games | O(n) | AC | 0.093 s | 388 KB | 11304045 |
| [2068_games.rs](2068_games.rs) | Rust 1.75 x64 | games | O(n) | AC | 0.015 s | 256 KB | 11304046 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2068_games_optimized.py](2068_games_optimized.py) \* | PyPy 3.10 x64 | games | O(N) | AC | 0.109 s | 236 KB | 11325080 |
| [2068_games_optimized.java](2068_games_optimized.java) \* | Java 1.8 | games | O(N) time; O(1) space | AC | 0.093 s | 340 KB | 11325849 |


\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
