# 1632. Láseres

[Timus 1632](https://acm.timus.ru/problem.aspx?space=1&num=1632) · dificultad 4325 · shortest_paths

Problema original de Dmitry Ivankov (preparado por Alex Samsonov), del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N rayos láser cruzan una sala. El rayo i sale de (X_i, Y_i, Z_i) en la
dirección (u_i, v_i, w_i); se conoce todo salvo las alturas Z_i. Para
algunos pares se sabe que el rayo i está por encima del rayo j: donde se
cruzan sus proyecciones verticales, en un mismo (X, Y), el rayo i está
estrictamente más alto. Hay que dar unas alturas cualesquiera compatibles
con todos los pares, cada una de valor absoluto a lo sumo 10⁶.

## Entrada

La primera línea contiene N (1 ≤ N ≤ 100); cada una de las N líneas
siguientes contiene X_i, Y_i, u_i, v_i, w_i, enteros de valor absoluto
hasta 100. Luego M (0 ≤ M ≤ 10000) y M líneas «i j»: el rayo i está por
encima del rayo j. Ningún rayo es vertical y no hay dos rayos en un mismo
plano vertical; existe una disposición válida.

## Salida

N números reales Z_i, uno por línea, con la mayor precisión posible.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0 1 0 0
1 0 0 1 0
1 1 -1 0 0
0 1 0 -1 0
3
1 2
2 3
3 4
```

Salida:

```
4.000
3.000
2.000
1.000
```

## Solución

Donde se cruzan las proyecciones de los rayos i y j, en los parámetros t_i
y t_j (dos ecuaciones lineales con dos incógnitas), las alturas son
Z_i + w_i t_i y Z_j + w_j t_j. Así, «i encima de j» se escribe
Z_i − Z_j > c con c = w_j t_j − w_i t_i: un sistema de restricciones de
diferencias, es decir, caminos más largos en un grafo con una arista
j → i de peso c.

Bellman–Ford desde una fuente imaginaria unida a cada rayo con peso 0 da
alturas que cumplen todas las restricciones con ≥ y tienen la menor
amplitud posible, así que si alguna respuesta cabe en [−10⁶, 10⁶], esta
también puede caber tras centrarla. Las rondas terminan pronto: solo se
relajan de nuevo los rayos subidos en la ronda anterior.

Las restricciones que se cumplen con igualdad exacta deben volverse
estrictas. Forman un grafo acíclico: un ciclo tendría peso 0, imposible en
una entrada válida. El código considera ajustadas las aristas con holgura
menor que 10⁻⁷, lo que puede incluir ciclos. Si el grafo es acíclico, cada
rayo recibe su nivel (la cadena más larga de aristas ajustadas que termina
en él) y sube step · level. Entonces cada arista ajustada gana al menos
un paso; las demás pierden a lo sumo step · levels. Si levels > 0, tomar
step = room / (2 · levels + 2), donde room es el espacio libre 2 · 10⁶
menos la amplitud, limitado por las holguras no ajustadas, mantiene
estrictas las demás aristas y la amplitud dentro de la caja. Al final las
alturas se centran y se imprimen con 10 decimales. `O(N · (M + 1))`.

Detalles a tener en cuenta:

- la relación no es transitiva y puede tener ciclos, ya que cada par se
  encuentra en su propio punto, así que ordenar topológicamente los pares
  de la entrada no funciona;
- con todas las diferencias en 0 (el ejemplo) todas las aristas están
  ajustadas y solo los pasos separan los rayos;
- imprimir pocos decimales puede borrar un margen diminuto.

El verificador comprueba cada par exactamente con aritmética racional, y
las respuestas lo pasan en todas las pruebas, igual que las de una
implementación aceptada independiente. Los cinco programas calculan en
double.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1632_shortest_paths.cpp](1632_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(N · (M + 1)) | AC | 0.015 s | 368 KB |
| [1632_shortest_paths.go](1632_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(N · (M + 1)) | AC | 0.031 s | 1608 KB |
| [1632_shortest_paths.java](1632_shortest_paths.java) | Java 1.8 | shortest_paths | O(N · (M + 1)) | AC | 0.125 s | 1580 KB |
| [1632_shortest_paths.py](1632_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(N · (M + 1)) | AC | 0.078 s | 1888 KB |
| [1632_shortest_paths.rs](1632_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(N · (M + 1)) | AC | 0.046 s | 596 KB |
