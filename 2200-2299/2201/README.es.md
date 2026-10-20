# 2201. Un servidor de chat donde cada gl y hf cambia la suerte de quien lo lee

[Timus 2201](https://acm.timus.ru/problem.aspx?space=1&num=2201) · dificultad 1875 · parsing, prefix_sums

Problema original de Vadim Barinov, de la Olimpiada Académica Universitaria Escolar de Informática 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un servidor de juego procesa N comandos de chat: entrar, salir, número
de conectados, mensaje público, mensaje privado y dos comandos de
comparación para admin. Los mensajes están hechos de los pares "gl" y
"hf", y cada lector conectado multiplica su suerte por A por cada "gl" y
la divide por B por cada "hf"; a los autores no les afecta. Imprimir la
respuesta del servidor a cada comando, incluidas las comparaciones de la
suerte de dos jugadores. Los límites son 2.5 segundos y 256 MB.

## Entrada

N, M, A y B, 1 ≤ N ≤ 86400, 2 ≤ M ≤ 10, 1 ≤ A, B ≤ 10⁹, y luego N
líneas de registro "[hh:mm:ss] NICK: /command".

## Salida

La respuesta del servidor a cada comando.

## Ejemplos

### Ejemplo 1

Entrada:

```
18 4 2 4
[00:00:23] admin: /online
[00:01:02] j0e: /j
[00:01:15] j0e: /s hfhf
[00:01:17] j0e: /q
[00:01:18] admin: /write<j0e> hfhf
[00:03:25] Tea_: /join
[00:04:11] j0e: /join
[00:07:54] Tea_: /j
[00:08:30] admin: /say glgl
[00:08:37] admin: /write<j0e> hfhf
[00:09:00] Tea_: /compare<j0e>
[00:13:41] admin: /c<j0e>-<Tea_>
[00:13:44] j0e: /quit
[00:13:57] admin: /compare<j0e>
[00:27:49] j0e: /j
[00:28:01] j0e: /s hfhf
[00:30:19] admin: /compare<j0e>
[00:30:43] admin: /compare<Tea_>-<j0e>
```

Salida:

```
There are 1 players on the server
Successful
j0e: hfhf
Successful
admin (to j0e): hfhf
Successful
Successful
Failed: Tea_ is already on the server
admin: glgl
admin (to j0e): hfhf
Failed: you have no such rights
Tea_ is a lucky guy
Successful
Failed: j0e is not on the server
Successful
j0e: hfhf
j0e is a lucky guy
Their luck is equal
```

## Solución

La suerte de un jugador es A^g / B^f, donde g y f cuentan los pares que
ha leído, así que basta guardar dos contadores. Los mensajes públicos
llegan a la vez a todos los conectados, así que van a dos totales
acumulados, y cada jugador guarda contadores relativos a ellos: al
entrar se restan los totales, al salir se suman de vuelta, y el autor de
un mensaje público resta sus propios pares. Para dos jugadores
conectados los totales se cancelan, y la diferencia de suerte la
describen dos enteros Δg y Δf. Los mensajes privados solo cambian los
contadores del destinatario.

Comparar A^Δg con B^Δf mediante logaritmos falla cerca de la igualdad:
con A = 5, B = 34, Δg = 165363 y Δf = 75472 los logaritmos difieren solo
en 9 · 10⁻⁹, y una tolerancia como 10⁻⁶ llamaría iguales a dos suertes
distintas. Por eso la igualdad se decide de forma exacta. Se escribe
A = r^s y B = q^t con los mayores exponentes posibles. Si A^Δg = B^Δf
con A, B > 1, ambos son potencias de un mismo entero, y entonces r = q,
así que la igualdad se cumple exactamente cuando r = q y s·Δg = t·Δf, o
cuando Δg = Δf = 0 para bases no relacionadas; una base 1 simplemente
desaparece. Solo cuando las suertes difieren se usa el signo de
Δg·ln A − Δf·ln B, y la doble precisión distingue diferencias muy por
debajo de esos 9 · 10⁻⁹.

El resto es un análisis cuidadoso: nombres cortos y largos de los
comandos, los textos de respuesta y el orden de las comprobaciones de
las comparaciones.

Cada comando cuesta O(1) aparte de leer su línea, así que todo el
registro se procesa en tiempo lineal.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2201_parsing_prefix_sums.cpp](2201_parsing_prefix_sums.cpp) | G++ 13.2 x64 | parsing, prefix_sums | O(N) | AC | 0.078 s | 4176 KB |
| [2201_parsing_prefix_sums.go](2201_parsing_prefix_sums.go) | Go 1.14 x64 | parsing, prefix_sums | O(N) | AC | 0.109 s | 16820 KB |
| [2201_parsing_prefix_sums.java](2201_parsing_prefix_sums.java) | Java 1.8 | parsing, prefix_sums | O(N) | AC | 0.203 s | 10020 KB |
| [2201_parsing_prefix_sums.py](2201_parsing_prefix_sums.py) | Python 3.12 x64 | parsing, prefix_sums | O(N) | AC | 0.328 s | 16696 KB |
| [2201_parsing_prefix_sums.rs](2201_parsing_prefix_sums.rs) | Rust 1.75 x64 | parsing, prefix_sums | O(N) | AC | 0.078 s | 11700 KB |
