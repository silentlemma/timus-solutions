# 1801. La Copa de la Revolución

[Timus 1801](https://acm.timus.ru/problem.aspx?space=1&num=1801) · dificultad 4973 · graphs

Problema original de Magaz Asanov, de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

g·t equipos están en t bombos de g equipos cada uno, y cada equipo
pertenece a un partido político. Repartirlos en g grupos de t equipos
de modo que cada grupo tenga exactamente un equipo de cada bombo y
ningún par de equipos del mismo partido. Imprimir cualquier reparto así
o indicar que no existe.

## Entrada

g y t (1 ≤ g, t ≤ 100), luego los bombos uno tras otro, separados por
líneas vacías, cada línea con el nombre de un equipo y el de su
partido. Los nombres tienen hasta 10 letras minúsculas, y todos los
nombres de equipos son distintos.

## Salida

"No", o "Yes" seguido de los g grupos, cada uno precedido por una línea
vacía y con sus t nombres de equipos, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
cavalry red
guard white

infantry red
guerilla green

czechs white
gunners latvia
```

Salida:

```
Yes

cavalry
guerilla
czechs

guard
infantry
gunners
```

### Ejemplo 2

Entrada:

```
2 2
cavalry red
guard white

czechs white
cossacks white
```

Salida:

```
No
```

## Solución

Se forma un multigrafo bipartito con los bombos de un lado y los
partidos del otro, y cada equipo es una arista entre su bombo y su
partido. Un grupo es un color: se colorean las aristas con g colores
sin que ningún vértice vea un color dos veces. Cada bombo tiene
exactamente g aristas, así que ve cada color una vez, y un partido ve
cada color como mucho una vez. Por el teorema de König un grafo
bipartito se colorea con tantos colores como su mayor grado, así que la
respuesta es "No" exactamente cuando algún partido tiene más de g
equipos.

La coloración se construye arista por arista. Para una arista del bombo
u al partido v, se toma un color a libre en u y un color b libre en v.
Si difieren, se sigue el camino desde u que alterna los colores b y a.
En un grafo bipartito no puede terminar en v, que no tiene arista de
color b. Intercambiar a y b a lo largo de él libera b en u, y la nueva
arista recibe el color b. El camino visita cada bombo como mucho una
vez, así que tiene como mucho 2t + 1 aristas. `O(g·t·(g + t))`.

En el primer ejemplo los dos equipos rojos, cavalry e infantry, van a
grupos distintos, y lo mismo los blancos, guard y czechs.

Trampas:

- basta comprobar el tamaño de los partidos para responder "No";
- una elección voraz simple de colores se atasca, así que hace falta
  recolorear a lo largo de caminos alternantes;
- las líneas vacías entre bombos en la entrada se saltan mejor leyendo
  palabras.

El verificador exige cada equipo una vez, un equipo de cada bombo en
cada grupo y partidos distintos dentro de un grupo. Todas las
soluciones lo superan en cientos de sorteos pequeños y en sorteos
completos de 100 bombos con partidos ajustados, holgados y
desbordados, y coinciden en "No" con una implementación aceptada
independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1801_graphs.cpp](1801_graphs.cpp) | G++ 13.2 x64 | graphs | O(g t (g + t)) | AC | 0.015 s | 5440 KB |
| [1801_graphs.go](1801_graphs.go) | Go 1.14 x64 | graphs | O(g t (g + t)) | AC | 0.046 s | 12424 KB |
| [1801_graphs.java](1801_graphs.java) | Java 1.8 | graphs | O(g t (g + t)) | AC | 0.140 s | 10672 KB |
| [1801_graphs.py](1801_graphs.py) | Python 3.12 x64 | graphs | O(g t (g + t)) | AC | 0.156 s | 13072 KB |
| [1801_graphs.rs](1801_graphs.rs) | Rust 1.75 x64 | graphs | O(g t (g + t)) | AC | 0.031 s | 9652 KB |
