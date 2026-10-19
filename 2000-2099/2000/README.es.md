# 2000. Grand Theft Array V

[Timus 2000](https://acm.timus.ru/problem.aspx?space=1&num=2000) · dificultad 160 · games

Problema original de Ilya Kuchumov. (Prepared by Kirill Devyatkin), del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos jugadores parten de posiciones dadas en un arreglo no negativo. El
primero comienza y alternan turnos. En cada turno se recoge el valor
actual, se sustituye por cero y se avanza una celda a izquierda o
derecha sin salir. Pueden compartir celda. Termina cuando todos los
valores son cero. Cada cual maximiza su puntuación final y, ante empate,
minimiza la contraria. Hallar ambas puntuaciones óptimas.

`10≤n≤100000`, valores 0–10000, posiciones `p,q` desde 1. Tiempo 0,5
segundos, memoria 64 MB.

## Entrada

Longitud `n`, los `n` valores y después las posiciones del primer y
segundo jugador, en ese orden.

## Salida

Dos enteros: puntuaciones del primero y del segundo.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
10
1 2 3 4 5 6 7 8 9 0
4 8
```

```
21 24
```

Los inicios 4 y 8 tienen punto medio 6, ganado por el primer jugador en
la carrera equidistante. Las celdas 1–6 suman 21; las restantes 7–10,
24.

## Solución

Al terminar, la suma de puntuaciones es la suma original, de modo que
maximizar la propia ya minimiza la otra. La no negatividad permite
garantizar el peso de una región completa sin necesitar evitar celdas.

### Inicios diferentes

Los primeros turnos globales posibles para recoger la celda `i` son
`T1(i)=2·|i−p|+1` y `T2(i)=2·|i−q|+2`. Una distancia igual favorece al
primero. Esto divide la línea en territorios contiguos: si `p<q`, con
`c=floor((p+q)/2)` el primero obtiene 1..c; si `p>q`, con
`c=ceil((p+q)/2)` obtiene c..n. El segundo recibe el complemento.

Las distancias por sí solas no prueban que se pueda recorrer en ambas
direcciones. La estrategia de garantía consiste en avanzar hacia el
rival hasta la frontera propia, recogerla antes de que el otro pueda
hacerlo y regresar inmediatamente hacia el extremo exterior. El rival
debe pasar por esa frontera para entrar en la región exterior. Compartir
posiciones está permitido, pero ahora recoge más tarde y tiene la misma
velocidad: puede seguir, sin adelantar el recorrido exterior. Así se
garantiza toda la región.

Ambos pueden garantizar sus sumas y estas suman el total, por lo que
ninguno fuerza más contra la defensa del otro. Las puntuaciones son
óptimas. Es un argumento de prioridad temporal de recogida, no un
bloqueo físico de las celdas ocupadas.

### El mismo inicio

El primero recoge el valor inicial. Sean `L,R` las sumas estrictamente a
izquierda y derecha. Puede elegir la mayor y caminar al extremo,
garantizando `a[p]+max(L,R)`; quien siga permanece detrás. El segundo
observa la primera dirección y elige la opuesta, defendiendo su frente
móvil. Si el primero regresa, no puede recoger antes que ese frente. Así
el primero no supera el inicio más el lado elegido inicialmente, como
máximo la garantía anterior. En un extremo el lado opuesto está vacío y
el segundo sigue, obteniendo cero.

El resultado es `a[p]+max(L,R)` y `min(L,R)`. Un arreglo completamente
nulo termina inmediatamente con dos ceros.

### Complejidad y horizonte de comprobación

Tiempo `O(n)`, memoria de entrada `O(n)` y espacio aritmético adicional
`O(1)`. La suma no supera `10^9`; los programas nativos usan 64 bits.

Cada defensa recoge su región en como máximo `2n` turnos propios, por lo
que bastan `4n` turnos alternos. En minimax truncado la defensa del
primero da la misma cota inferior y la del segundo la superior
complementaria; el peso no recogido es no negativo. Por tanto este
horizonte ya da el valor completo, y un minimax de `4n` turnos comprueba
exactamente los casos pequeños.

Recoger antes de mover. El empate del punto medio es del primero en
ambos órdenes izquierda/derecha. Inicios iguales requieren el lado de
mayor suma. Cruzar ceros cuesta turnos; compartir celda no bloquea.
Conservar las identidades si el primero empieza a la derecha.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2000_games.cpp](2000_games.cpp) | G++ 13.2 x64 | games | O(n) | AC | 0.031 s | 1224 KB |
| [2000_games.go](2000_games.go) | Go 1.14 x64 | games | O(n) | AC | 0.062 s | 2484 KB |
| [2000_games.java](2000_games.java) | Java 1.8 | games | O(n) | AC | 0.109 s | 1252 KB |
| [2000_games.py](2000_games.py) | Python 3.12 x64 | games | O(n) | AC | 0.125 s | 11780 KB |
| [2000_games.rs](2000_games.rs) | Rust 1.75 x64 | games | O(n) | AC | 0.046 s | 2916 KB |
