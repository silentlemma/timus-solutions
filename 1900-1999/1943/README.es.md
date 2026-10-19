# 1943. Un prefijo ganador de cinco cartas

[Timus 1943](https://acm.timus.ru/problem.aspx?space=1&num=1943) · difficulty 906 · bruteforce, constructive

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Ambas colas iniciales son permutaciones de rangos 1..n. Se revelan sus
frentes a la vez: iguales se descartan ambos; si difieren, la mayor gana
las dos y añade primero la menor y después la mayor al final de su cola.
Una cola vacía pierde, ambas vacías empatan. Conocido el orden rival,
elegir una permutación propia que gane o demostrar que no existe.
Empatar o repetir para siempre no basta. Límites: 1 segundo, 64 MB.

## Entrada

n, 2≤n≤500, y una permutación de 1..n del rival, de arriba abajo.
Cada rango aparece una vez por baraja inicial.

## Salida

NO solo si es imposible; si no, YES en la primera línea y cualquier
permutación ganadora en la segunda, de arriba abajo.

## Evaluación

Un comprobador juega la partida completa con la baraja impresa y acepta
cualquiera que gane de verdad. Con cinco cartas o más `NO` nunca es
correcto, por el lema de abajo.

## Ejemplos

```
4
2 3 4 1
```

```
YES
2 4 1 3
```

## Solución

Tomar los primeros m=min(n,5) rangos rivales, enumerar sus permutaciones
y simular cada partida de m cartas. Repetir un par de colas indica ciclo;
elegir la primera victoria real. Para n≤5 se prueban todas las respuestas,
de modo que no hallar victoria demuestra NO.

El lema clave: todo orden de cinco rangos distintos tiene una respuesta
ganadora. Solo importa el orden de los rangos, así que bastan los rangos
del 1 al 5, y el lema se comprueba jugando los 120² = 14 400 pares de
órdenes. Este guion corto lo hace, junto con las barajas menores:

```python
from collections import deque
from itertools import permutations

def game(a, b):
    a, b = deque(a), deque(b)
    seen, steps = set(), 0
    while a and b:
        state = tuple(a), tuple(b)
        if state in seen:
            return False, steps
        seen.add(state)
        x, y = a.popleft(), b.popleft()
        steps += 1
        if x > y:
            a.extend((y, x))
        elif y > x:
            b.extend((x, y))
    return bool(a), steps

for size in range(2, 6):
    orders = list(permutations(range(1, size + 1)))
    possible, longest = 0, 0
    for opponent in orders:
        results = [game(own, opponent) for own in orders]
        possible += any(won for won, _ in results)
        longest = max(longest, max(steps for _, steps in results))
    print(size, len(orders), possible, longest)
```

| Cards | Opponent orders | Orders with a winning reply | Longest game |
|---:|---:|---:|---:|
| 2 | 2 | 0 | 4 |
| 3 | 6 | 3 | 7 |
| 4 | 24 | 22 | 16 |
| 5 | 120 | 120 | 49 |

Hay estados finitos porque quedan como máximo diez cartas; un estado
repetido no gana. La enumeración termina y cada uno de los 120 órdenes
de cinco cartas tiene un testigo. Las pruebas guardan los 6 datos y
respuestas ganadoras, además de los 13 órdenes menores: certificado
finito reproducible. Cinco es el mínimo tamaño universal, pues cuatro
cartas tienen dos órdenes imposibles.

Para n>5, cambiar solo las cinco primeras cartas por una permutación
local ganadora y copiar el resto del rival. Durante las primeras n rondas,
las originales no jugadas preceden a todas las capturas; ninguna cola
puede vaciarse antes. Las últimas n−5 parejas originales iguales se
eliminan. Tras ronda n quedan exactamente las colas del juego local
tras ronda cinco; las rondas siguientes coinciden. Una victoria local
en t rondas se convierte en victoria en n+t−5≤n+44. El lema garantiza
éxito para n≥5 y la enumeración menor establece completitud.

Tiempo y espacio O(n), más búsqueda local fija de hasta 5! candidatos.
El dominio local completo establece ≤49 rondas y ≤10 cartas activas.
Son cotas verificadas, no cortes del programa. La primera victoria se
halla como máximo en intento 68; se enumera hasta ganar o agotar candidatos.

Capturar en orden menor, mayor. Las iguales desaparecen ambas; vaciarse
a la vez es empate. Solo vale victoria, no sobrevivir o adivinar tras
un corte. Cinco cartas no significa cinco rondas. Las cartas sin cambiar
deben ocupar posiciones originales iguales para cancelarse antes de las
capturas. Patrones observados en barajas ordenadas no sustituyen al lema.

## Notas por lenguaje

C++ usa next_permutation, Python itertools.permutations; Go, Java y Rust
implementan pivote, sucesor e inversión del sufijo. Los motores conservan
estados exactos para detectar ciclos. Go usa índices de frente; Java y
Rust usan deques. El resto se copia. Solo bibliotecas estándar, sin tabla
de respuestas prealmacenadas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1943_bruteforce_constructive.cpp](1943_bruteforce_constructive.cpp) | G++ 13.2 x64 | bruteforce, constructive | O(n) | AC | 0.015 s | 520 KB |
| [1943_bruteforce_constructive.go](1943_bruteforce_constructive.go) | Go 1.14 x64 | bruteforce, constructive | O(n) | AC | 0.031 s | 1236 KB |
| [1943_bruteforce_constructive.java](1943_bruteforce_constructive.java) | Java 1.8 | bruteforce, constructive | O(n) | AC | 0.109 s | 848 KB |
| [1943_bruteforce_constructive.py](1943_bruteforce_constructive.py) | Python 3.12 x64 | bruteforce, constructive | O(n) | AC | 0.062 s | 600 KB |
| [1943_bruteforce_constructive.rs](1943_bruteforce_constructive.rs) | Rust 1.75 x64 | bruteforce, constructive | O(n) | AC | 0.046 s | 468 KB |
