# 1791. El tío Styopa y los autobuses

[Timus 1791](https://acm.timus.ru/problem.aspx?space=1&num=1791) · dificultad 1471 · greedy

Problema original de Eugene Kurpilyansky, del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tramo de carretera de un solo carril lo comparten autobuses en ambos
sentidos, de uno en uno, y cada autobús tarda exactamente un minuto en
pasar. El autobús i llega en el minuto tᵢ y puede pasar como mucho pᵢ
minutos en el tramo, espera incluida. Los autobuses de un mismo sentido
deben pasar en su orden de llegada. Decidir si todos pueden llegar a
tiempo.

## Entrada

n (1 ≤ n ≤ 100000), luego n pares tᵢ pᵢ de un sentido; luego m
(1 ≤ m ≤ 100000) y m pares del otro. Todos los números van de 1 a 10⁸,
y cada sentido está en orden de llegada.

## Salida

"YES" si todos los autobuses pueden llegar a tiempo; si no, "NO".

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1 1
1 2
1
2 2
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
2
1 1
1 2
1
2 1
```

Salida:

```
NO
```

## Solución

El autobús i debe entrar en uno de los minutos tᵢ … tᵢ + pᵢ − 1, y en
cada minuto entra un solo autobús. En un mismo sentido un autobús entra
antes que el siguiente, así que su último minuto es como mucho el
último minuto del siguiente menos uno; una pasada desde el final baja
los últimos minutos en consecuencia. Luego se recorren los minutos: de
los dos autobuses de cabeza que ya han llegado, pasa el de último
minuto más temprano; si no ha llegado ninguno, se salta a la siguiente
llegada. Si un autobús pasa después de su último minuto, la respuesta
es NO. Dejar pasar al más urgente de los que esperan nunca es peor, ya
que cambiarlo por uno posterior mantiene a ambos a tiempo. La respuesta
es YES si pasan todos. `O(n + m)`.

En el primer ejemplo el primer autobús entra en el minuto 1, el segundo
en el 2 y el del otro sentido en el 3, el último que puede usar. En el
segundo ejemplo ese autobús debe entrar a más tardar en el minuto 2,
pero también el segundo autobús, y el minuto 1 lo ocupa el primero.

Trampas:

- un autobús con prisa detrás de uno paciente en el mismo sentido hace
  que el paciente también tenga prisa, de lo que se encarga la pasada
  desde el final;
- los tiempos llegan a 10⁸, así que el reloj debe saltar los periodos
  vacíos en lugar de contar cada minuto;
- la espera cuenta en pᵢ, así que un autobús que llega en tᵢ debe
  entrar a más tardar en tᵢ + pᵢ − 1.

Las respuestas coinciden con una búsqueda sobre todas las mezclas de
las dos colas en 400 casos pequeños aleatorios, y con una
implementación aceptada independiente en casos grandes: planes con
minutos de sobra, planes llenos con un autobús al que le falta un
minuto, y tiempos aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1791_greedy.cpp](1791_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.281 s | 2872 KB |
| [1791_greedy.go](1791_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.078 s | 6852 KB |
| [1791_greedy.java](1791_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.140 s | 3560 KB |
| [1791_greedy.py](1791_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.562 s | 46212 KB |
| [1791_greedy.rs](1791_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.031 s | 8328 KB |
