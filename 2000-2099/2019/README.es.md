# 2019. Emparejar Tipos sin Cruces

[Timus 2019](https://acm.timus.ru/problem.aspx?space=1&num=2019) · dificultad 297 · greedy

Problema original de Denis Dublennykh, preparado por Oleg Merkurev, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `2n` extremos distintos ordenados en una semicircunferencia, representados
por letras latinas: exactamente `n` mayúsculas y `n` minúsculas. Empareje cada
mayúscula con una minúscula de la misma letra, usando cada extremo una vez.
Los segmentos rectos no deben cruzarse. Encuentre cualquier emparejamiento
válido o indique que es imposible.

Se cumple `1 ≤ n ≤ 5 000`; los 26 tipos pueden repetirse. Las mayúsculas y
las minúsculas se numeran **por separado** de 1 a `n`, en orden de aparición.
Límites: 1 segundo y 64 MB.

## Entrada

La primera línea contiene `n`. La segunda contiene la palabra de exactamente
`2n` letras latinas mayúsculas y minúsculas.

## Salida

Si existe solución, imprima los `n` índices distintos de las minúsculas
emparejadas, en orden de las mayúsculas. Se permite cualquier solución.
En caso contrario, imprima exactamente `Impossible`.

## Evaluación

Un comprobador verifica que las parejas unen letras del mismo tipo, usan
cada extremo una vez y no se cruzan; `Impossible` solo se acepta si no
existe emparejamiento. Se acepta cualquier emparejamiento válido.

## Ejemplos

```
2
AbBa
```

```
2 1
```

```
2
AbaB
```

```
Impossible
```

```
1
Ab
```

```
Impossible
```

## Solución

Dos cuerdas de una semicircunferencia se cruzan exactamente cuando sus
extremos se alternan. Las parejas anidadas o separadas son seguras. Todo
emparejamiento completo sin cruces contiene una pareja interior cuyos
extremos son adyacentes entre los restantes. Eliminando esas parejas se
vacía la palabra. Recíprocamente, cancelar letras iguales de caso opuesto
adyacentes construye una solución sin cruces: su interior ya quedó emparejado.

Recorra de izquierda a derecha con una pila de extremos pendientes. Asigne
a cada extremo el siguiente índice de su propio caso. Si la letra actual
y la cima tienen el mismo tipo y caso opuesto, retire la cima y registre
la pareja; si no, apile el extremo actual. Ambos órdenes de casos sirven.
Guarde siempre el índice minúsculo en la posición de respuesta de la
mayúscula, independientemente del orden de llegada. Una pila final no vacía
significa `Impossible`.

La cancelación voraz no puede perder una solución. Dos eliminaciones
adyacentes posibles son disjuntas, por lo que conmutan, o se solapan en
`xXx` o `XxX`, donde ambas dejan la misma letra. Cada eliminación acorta la
palabra. Por inducción sobre su longitud, todas las secuencias completas de
cancelaciones tienen el mismo resultado irreducible: tras primeras elecciones
distintas, los resultados ya coinciden o coinciden al eliminar la otra pareja;
los términos más cortos cumplen la hipótesis inductiva.

La pila conserva una forma irreducible del prefijo procesado. Un símbolo
nuevo cancela la cima o mantiene el prefijo irreducible. Por tanto calcula
ese resultado común. Si existe un emparejamiento completo sin cruces, sus
parejas interiores dan una reducción a vacío y la pila también se vacía.
Un residuo no vacío demuestra imposibilidad. Si se vacía, las parejas
registradas son anidadas o separadas, compatibles por tipo y cubren todos
los extremos una vez, lo que demuestra corrección.

En `AbBa` se cancela primero `bB` y luego `Aa`, dando `2 1`.
En `AbaB`, las únicas parejas compatibles alternan sus extremos y se cruzan.
En `Ab` los tipos no coinciden. Tener cantidades equilibradas por tipo
no basta: `ABab` también es imposible.

Cada extremo se apila como máximo una vez y se retira como máximo una vez.
Tiempo `O(n)` y espacio `O(n)`, con hasta `2n ≤ 10 000` extremos en la pila.

Trampas:

- Numerar mayúsculas y minúsculas por separado, sin usar posiciones de
  la palabra.
- Cancelar solo letras del mismo tipo y caso opuesto.
- Permitir que la minúscula aparezca antes de su pareja mayúscula.
- No confundir equilibrio por tipos con existencia de una solución sin cruces.
- Emitir las parejas en orden de mayúsculas y escribir exactamente `Impossible`.

## Soluciones optimizadas

C++ y Go usan la misma regla de cancelación con pila, con vectores separados para letras e índices de 16 bits. C++ lee letra por letra. Go reutiliza la parte ya procesada del búfer de entrada como pila de letras. Una inserción no escribe más allá de la posición actual, de modo que las letras aún sin leer quedan intactas.

Las implementaciones base aceptadas [2019_greedy.java](2019_greedy.java), [2019_greedy.py](2019_greedy.py), [2019_greedy.rs](2019_greedy.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

Se usan bytes o caracteres ASCII; los dos casos de una letra difieren en el
bit 32. C++ y Go usan estructuras de extremos, Rust y Python usan pares,
y Java usa dos arreglos paralelos y un tamaño de pila. No hay recursión y
los índices caben en enteros ordinarios.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2019_greedy.cpp](2019_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 468 KB | 11292657 |
| [2019_greedy.go](2019_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 1412 KB | 11292663 |
| [2019_greedy.java](2019_greedy.java) \* | Java 1.8 | greedy | O(n) | AC | 0.140 s | 912 KB | 11292672 |
| [2019_greedy.py](2019_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.109 s | 1200 KB | 11292667 |
| [2019_greedy.rs](2019_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.046 s | 396 KB | 11292677 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2019_greedy_optimized.cpp](2019_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 148 KB | 11310619 |
| [2019_greedy_optimized.go](2019_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 960 KB | 11310515 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
