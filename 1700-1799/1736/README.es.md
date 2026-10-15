# 1736. Hockey chino

[Timus 1736](https://acm.timus.ru/problem.aspx?space=1&num=1736) · dificultad 1177 · greedy

Problema original de Alexander Ipatov (preparado por Igor Chevdar), del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En una liga de todos contra todos de n equipos de hockey, cada partido
da 3 puntos: 3 : 0 por ganar en tiempo reglamentario y 2 : 1 por ganar
en la prórroga. Dados los puntos finales de cada equipo, decidir si tal
temporada existe y, en ese caso, mostrar los resultados de todos los
partidos.

## Entrada

n (2 ≤ n ≤ 200) y luego los puntos en orden no creciente; suman
3n(n − 1)/2 y ninguno pasa de 3(n − 1).

## Salida

`INCORRECT`, o `CORRECT` y cada partido como `i ? j`, donde `?` es `<`,
`<=`, `>=` o `>` para una derrota en tiempo reglamentario, una derrota
en la prórroga, una victoria en la prórroga o una victoria en tiempo
reglamentario del equipo i. Se acepta cualquier temporada válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
8 7 2 1
```

Salida:

```
CORRECT
2 <= 1
3 >= 4
1 > 3
4 < 2
1 > 4
2 > 3
```

### Ejemplo 2

Entrada:

```
4
8 8 1 1
```

Salida:

```
INCORRECT
```

## Solución

Cada partido reparte 3 puntos de cualquiera de las cuatro formas, así
que solo importan los totales. Se toma el equipo al que le quedan menos
puntos, s, y se resuelven a la vez todos sus partidos pendientes: de los
3(m − 1) puntos de sus m − 1 partidos se queda s y reparte el resto, 3
puntos por partido primero a los equipos más fuertes y lo que sobre al
siguiente. Luego se quita y se repite. Si en algún momento el equipo más
débil tiene más puntos de los que dan sus partidos, alguien necesitaría
puntos negativos, o a un equipo le quedan puntos al final, la tabla es
imposible.

Dar primero a los más fuertes deja el mayor margen a los débiles, que
son los que los partidos restantes pueden dejar sin puntos; un
argumento de intercambio como el del método de Havel–Hakimi para grafos
muestra que así nunca se pierde una temporada, y las comprobaciones de
abajo lo confirman. Ordenar en cada ronda da `O(n² log n)`.

En el primer ejemplo el equipo 4 se queda 1 punto y reparte 8: 3 al
equipo 1, 3 al equipo 2 y 2 al equipo 3. Luego el equipo 3 reparte sus
6 entre los equipos 1 y 2, y el equipo 2 se queda 1 contra el equipo 1.

Trampas:

- una tabla que suma bien puede ser imposible igualmente: en el segundo
  ejemplo los dos equipos más débiles juegan entre sí, y ese partido ya
  da 3 puntos, más que sus 2;
- los signos van desde el lado del primer equipo, así que `i < j`
  significa que el equipo i perdió en tiempo reglamentario.

Una tabla es posible justo cuando los k equipos más débiles tienen al
menos 3·C(k, 2) puntos para cada k, pues sus partidos entre sí dan eso;
es la condición de flujo máximo para repartir los puntos. Los
veredictos coinciden con ella en 260 tablas aleatorias de hasta 200
equipos, 154 de ellas imposibles, y el comprobador reprodujo cada
temporada impresa. Para n hasta 5 se comparó cada tabla con el total
correcto con una enumeración de todas las temporadas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1736_greedy.cpp](1736_greedy.cpp) | G++ 13.2 x64 | greedy | O(n² log n) | AC | 0.031 s | 280 KB |
| [1736_greedy.go](1736_greedy.go) | Go 1.14 x64 | greedy | O(n² log n) | AC | 0.031 s | 2188 KB |
| [1736_greedy.java](1736_greedy.java) | Java 1.8 | greedy | O(n² log n) | AC | 0.171 s | 5408 KB |
| [1736_greedy.py](1736_greedy.py) | Python 3.12 x64 | greedy | O(n² log n) | AC | 0.109 s | 2968 KB |
| [1736_greedy.rs](1736_greedy.rs) | Rust 1.75 x64 | greedy | O(n² log n) | AC | 0.031 s | 940 KB |
