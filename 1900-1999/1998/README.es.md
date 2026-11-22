# 1998. Completar elevaciones ordenadas con interrupciones

[Timus 1998](https://acm.timus.ru/problem.aspx?space=1&num=1998) · dificultad 378 · two_pointers

Problema original de Denis Dublennykh, preparado por Egor Shchelkonogov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los objetos se elevan en un orden fijo. Cada segundo normal eleva el
primero que todavía no se mantiene. En un segundo de interrupción no se
eleva nada: se sueltan objetos en orden inverso hasta que el peso total
soltado sea estrictamente mayor que `k` o no quede ninguno. Encontrar el
primer segundo con los `n` objetos elevados a la vez. Las interrupciones
posteriores ya no importan.

Límites: `1≤n,m≤100000`, `1≤k≤10^9`, pesos `1≤w[i]≤10000`, tiempos
estrictamente crecientes entre 1 y `10^9`. Tiempo 0,5 segundos; memoria
64 MB.

## Entrada

Primero `n m k`; después `n` pesos en orden de elevación y `m` tiempos
de interrupción. Cada peso y tiempo ocupa una línea.

## Salida

Un entero: el segundo de finalización.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
5 1 4
1
2
3
4
5
4
```

```
8
```

En los segundos 1–3 se mantienen pesos 1, 2, 3. En el segundo 4 no hay
elevación. Soltar solo 3 no supera 4, por lo que también cae 2, sumando
5. Queda el peso 1; los segundos 5–8 elevan los cuatro objetos
restantes. La respuesta es 8.

## Solución

Los objetos mantenidos siempre forman un prefijo: una elevación lo
amplía en uno y una interrupción elimina un sufijo. Su longitud `h`
describe completamente el estado.

### Precalcular cada retroceso

Sea `P[h]` la suma de los primeros `h` pesos, con `P[0]=0`. Definimos
`retreat[h]` como la longitud que queda tras una interrupción desde `h`.

Si `P[h]≤k`, caen todos y queda cero. En otro caso buscamos el mayor
`q<h` con `P[h]−P[q]>k`: corresponde al menor número soltado que ya
supera el límite. Para `q>0`, conservar el siguiente prefijo daría un
peso soltado como máximo `k`. Equivale al predecesor de la primera suma
prefija al menos `P[h]−k`, limitado inferiormente a cero.

Los pesos positivos hacen `P` estrictamente creciente; la posición
buscada nunca retrocede al aumentar `h`. Mantenemos un puntero `q`,
inicialmente cero. Para `h=1..n`, lo avanzamos mientras `q+1<h` y
`P[h]−P[q+1]>k`, y guardamos `retreat[h]=q`. El puntero anterior sigue
siendo admisible al aumentar el umbral y la condición final descarta
cualquier posición mayor. Mientras el peso total no supera `k`,
permanece en cero. También `retreat[0]=0`.

El puntero avanza como máximo `n` veces en total: preprocesamiento
lineal. La comparación estricta es decisiva; un peso soltado exactamente
`k` exige soltar otro objeto si queda alguno.

### Saltar entre eventos

Guardamos el último tiempo de interrupción `time` y la longitud `h`,
ambos inicialmente cero. Antes del siguiente evento `t` hay exactamente
`t−time−1` segundos normales. Si bastan para los `n−h` objetos
pendientes, devolvemos `time+n−h`, estrictamente anterior a `t`.

En otro caso incrementamos `h` por esos segundos, aplicamos `retreat[h]`
y fijamos `time=t`. En el propio segundo `t` no hay elevación. Después
del último evento la respuesta es `time+n−h`.

Por inducción, cada salto reproduce todas las elevaciones normales y la
tabla reproduce exactamente las caídas. La comprobación devuelve el
primer instante posible. Si la finalización prevista coincide con una
interrupción, queda bloqueada: hay que procesar el evento. Los prefijos
vacíos y eventos consecutivos siguen las mismas fórmulas.

### Complejidad y cotas

Tiempo `O(n+m)` y memoria `O(n+m)` con la entrada almacenada en todos
los lenguajes; tablas auxiliares `O(n)`. Las sumas no superan `10^9`; la
respuesta está acotada por `max(t)+n≤1000100000`. Los programas nativos
usan 64 bits para sumas y tiempos. El intervalo se convierte a índice
solo tras verificar que es menor que el número de objetos pendientes.

Superar el umbral, no solo alcanzarlo. El segundo interrumpido no eleva
nada. Terminar inmediatamente al mantener todos e ignorar eventos
futuros. Evitar simular segundos o cada caída: eventos distantes y
reinicios profundos pueden representar casi mil millones de acciones. El
retroceso depende solo de la longitud del prefijo.

## Soluciones optimizadas

`1998_two_pointers_optimized.java`. Conserva la tabla monótona de retroceso por dos punteros y la comparación estricta con limit. Construye prefijos al leer y consume las interrupciones una a una; si termina antes, sigue ignorando eventos posteriores. Hay como máximo 100000 pesos de hasta 10000, por lo que cada prefijo y diferencia no supera 10^9: bastan arreglos int para prefijos e índices. Los tiempos y limit siguen siendo long y ordinary=event-time-1 no cambia. Un analizador de bytes de 4 KB reemplaza al lector genérico; tiempo O(N+M), espacio O(N). Se conservan las versiones simples.

Frente a `1998_two_pointers.java`: tiempo 0.125 s → 0.093 s; memoria 3104 KB → 1152 KB.

La versión optimizada de C++ conserva el algoritmo de dos punteros. Al leer los pesos, mantiene el total del sufijo actual y retira su primer objeto mientras el resto aún supere estrictamente el límite. Cada peso ocupa 16 bits. Las interrupciones se procesan a medida que se leen y la lectura se detiene en cuanto se puede terminar. El tiempo es O(n+m) y el espacio adicional es O(n). El envío aceptado usó 672 KB en lugar de 2740 KB, con el mismo tiempo de 0,015 s.

Las bases aceptadas conservadas [1998_two_pointers.go](1998_two_pointers.go), [1998_two_pointers.py](1998_two_pointers.py), [1998_two_pointers.rs](1998_two_pointers.rs) también cumplen la admisión estricta del conjunto rápido en la comparación guardada: diez primeros puestos o 15% superior en las métricas requeridas. Se reutilizan sin copias idénticas. Java utiliza el fuente optimizado separado de arriba y conserva el didáctico. Un asterisco indica el objetivo de clasificación propio del lenguaje.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Conserva los algoritmos didácticos. Las filas básicas revalidadas usan sus nuevas métricas e IDs de Accepted de fuente exacta; estas pruebas no cuentan como optimizaciones.

Accepted del fuente exacto #11326586: 0.093 s / 1152 KB. En la muestra Java 1.8 guardada el 2026-11-20: puesto de tiempo 1/40, de memoria 2/40. El asterisco sigue indicando el objetivo de clasificación propio del lenguaje.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1998_two_pointers.cpp](1998_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n+m) | AC | 0.015 s | 2740 KB | 11292423 |
| [1998_two_pointers.go](1998_two_pointers.go) \* | Go 1.14 x64 | two_pointers | O(n+m) | AC | 0.125 s | 6872 KB | 11292424 |
| [1998_two_pointers.java](1998_two_pointers.java) \* | Java 1.8 | two_pointers | O(n+m) | AC | 0.125 s | 3104 KB | 11325563 |
| [1998_two_pointers.py](1998_two_pointers.py) \* | Python 3.12 x64 | two_pointers | O(n+m) | AC | 0.156 s | 27000 KB | 11292425 |
| [1998_two_pointers.rs](1998_two_pointers.rs) \* | Rust 1.75 x64 | two_pointers | O(n+m) | AC | 0.031 s | 6272 KB | 11292427 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1998_two_pointers_optimized.cpp](1998_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(n+m) | AC | 0.015 s | 672 KB | 11310347 |
| [1998_two_pointers_optimized.java](1998_two_pointers_optimized.java) \* | Java 1.8 | two_pointers | O(N+M) | AC | 0.093 s | 1152 KB | 11326586 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
