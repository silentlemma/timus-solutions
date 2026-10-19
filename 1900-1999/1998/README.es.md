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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1998_two_pointers.cpp](1998_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n+m) | AC | 0.015 s | 2740 KB |
| [1998_two_pointers.go](1998_two_pointers.go) | Go 1.14 x64 | two_pointers | O(n+m) | AC | 0.125 s | 6872 KB |
| [1998_two_pointers.java](1998_two_pointers.java) | Java 1.8 | two_pointers | O(n+m) | AC | 0.140 s | 3128 KB |
| [1998_two_pointers.py](1998_two_pointers.py) | Python 3.12 x64 | two_pointers | O(n+m) | AC | 0.156 s | 27000 KB |
| [1998_two_pointers.rs](1998_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(n+m) | AC | 0.031 s | 6272 KB |
