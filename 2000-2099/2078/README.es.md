# 2078. Cotas del marcador de bolos a partir de los totales por cuadro

[Timus 2078](https://acm.timus.ru/problem.aspx?space=1&num=2078) · dificultad 275 · dp

Problema original de Alexander Krasnoselskikh, preparado por Oleg Dolgorukov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una partida de bolos tiene diez cuadros. En los cuadros 1 a 9 se lanza a
10 bolos hasta dos veces; derribarlos todos con el primer lanzamiento es
un pleno (el segundo se omite), y con los dos, un semipleno. Un pleno
suma al cuadro los dos lanzamientos siguientes, un semipleno el
siguiente. El último cuadro da un tercer lanzamiento tras un pleno o un
semipleno, con bolos nuevos cada vez que caen todos, y no recibe bonos.
Solo se conoce cuántos bolos cayeron en cada cuadro. Hallar el menor y
el mayor marcador posibles. Los límites son 2 segundos y 256 MB.

## Entrada

Diez números: los bolos de los cuadros 1 a 9 (de 0 a 10) y del último
cuadro (de 0 a 30).

## Salida

El menor y el mayor marcador.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 2 4 8 3 8 1 9 8 7
```

Salida:

```
60 62
```

### Ejemplo 2

Entrada:

```
2 4 6 8 10 10 8 6 4 2
```

Salida:

```
60 86
```

## Solución

Los bolos en sí suman lo mismo con cualquier reparto de los cuadros en
lanzamientos; solo cambian los bonos, y estos miran a lo sumo dos
lanzamientos adelante. Así que una DP recorre los cuadros del último al
primero y guarda, para cada par (x, y) de los dos primeros lanzamientos
desde el cuadro actual, el menor y el mayor marcador de los cuadros de
ahí al final.

Para el último cuadro se prueban todas las secuencias válidas con el
total correcto: dos lanzamientos sin pleno ni semipleno, y en otro caso un
tercero con bolos nuevos (o con los que quedan tras un pleno y un
segundo lanzamiento parcial). Su par son sus dos primeros lanzamientos y
su marcador es su total.

Un cuadro con menos de 10 bolos se reparte como (r, t − r) para
cualquier r, y su par son esos dos lanzamientos. Un cuadro con 10 bolos
es un pleno, con par (10, x) para el par (x, y) del cuadro siguiente y
bono x + y, o un semipleno (r, 10 − r) con bono x. La respuesta es el
extremo sobre los pares del primer cuadro; hay a lo sumo 121 pares, así
que el trabajo es O(1).

En el primer ejemplo el primer cuadro es un pleno o un semipleno,
seguido de un cuadro de 2 bolos: como pleno suma los dos lanzamientos de
ese cuadro (2 puntos), como semipleno no suma nada si ese cuadro empieza
con 0; de ahí 60 y 62.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2078_dp.cpp](2078_dp.cpp) | G++ 13.2 x64 | dp | O(1) | AC | 0.015 s | 136 KB |
| [2078_dp.go](2078_dp.go) | Go 1.14 x64 | dp | O(1) | AC | 0.031 s | 1144 KB |
| [2078_dp.java](2078_dp.java) | Java 1.8 | dp | O(1) | AC | 0.125 s | 1664 KB |
| [2078_dp.py](2078_dp.py) | Python 3.12 x64 | dp | O(1) | AC | 0.093 s | 708 KB |
| [2078_dp.rs](2078_dp.rs) | Rust 1.75 x64 | dp | O(1) | AC | 0.046 s | 232 KB |
