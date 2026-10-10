# 1202. El camino más corto a través de una cadena de rectángulos

[Timus 1202](https://acm.timus.ru/problem.aspx?space=1&num=1202) · dificultad 442 · greedy

Problema original de Leonid Volkov, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hasta `10⁵` rectángulos en papel cuadriculado forman una cadena de
izquierda a derecha: el primero tiene la esquina inferior izquierda en
`(0, 0)`, cada uno empieza donde termina horizontalmente el anterior y
cada lado mide de 2 a 100 casillas. Donde dos vecinos se tocan, su borde
común desaparece. Un viajero camina por las líneas de la cuadrícula
desde `(1, 1)` hasta el punto una casilla hacia dentro de la esquina
superior derecha del último rectángulo, no puede andar por ningún borde
de rectángulo y solo pasa de un rectángulo al siguiente por la parte
desaparecida del borde. Hay que hallar la longitud del camino más corto,
o `-1` si no existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` y luego cada rectángulo como `x1 y1 x2 y2`, las esquinas inferior
izquierda y superior derecha.

## Salida

La longitud del camino más corto, o `-1`.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 0 3 5
3 1 5 7
```

Salida:

```
8
```

## Solución

El camino debe ir de `x = 1` a `x = x2 − 1` del último rectángulo, y
siempre puede hacerlo sin dar ningún paso a la izquierda, así que la
parte horizontal es fija. Entre los rectángulos `i` e `i + 1` el camino
cruza la recta `x = x2ᵢ` a una altura entera estrictamente dentro de
ambos, es decir en `[max(y1) + 1, min(y2) − 1]`; si ese rango está
vacío, no hay camino. Dentro de un rectángulo la altura se puede cambiar
libremente por una línea vertical interior, así que la longitud vertical
es el cambio total de altura entre el inicio, las alturas de cruce
elegidas y la meta.

Para minimizarla, se mueve solo cuando es obligado: se mantiene la altura
actual y en cada borde se lleva al rango permitido. Por inducción, la
forma más barata de estar a altura `h` tras el borde `i` cuesta el total
voraz hasta ahí más `|h − altura voraz|`, así que la elección voraz nunca
es peor. `O(n)`.

Detalles a tener en cuenta:

- los rectángulos que se tocan en menos de dos unidades, o solo por una
  esquina, no dejan paso alguno;
- los rectángulos pueden extenderse por debajo de cero;
- con un solo rectángulo la respuesta es la distancia de `(1, 1)` a la
  meta, y 0 para un rectángulo de 2×2.

Las respuestas se compararon con una solución escrita aparte en 400
cadenas aleatorias y en todas las pruebas.

## Notas por lenguaje

- Go y Java leen la entrada con lectores de bytes escritos a mano.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1202_greedy.cpp](1202_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.234 s | 132 KB |
| [1202_greedy.go](1202_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.046 s | 1088 KB |
| [1202_greedy.java](1202_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.140 s | 540 KB |
| [1202_greedy.py](1202_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.328 s | 39384 KB |
| [1202_greedy.rs](1202_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.031 s | 8696 KB |
