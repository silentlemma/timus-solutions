# 1840. Víctima de la publicidad

[Timus 1840](https://acm.timus.ru/problem.aspx?space=1&num=1840) · dificultad 6779 · geometry

Problema original de Pavel Egorov, del XV Campeonato Abierto de los Urales de Programación Competitiva, abril de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un patinador debe recorrer n segmentos orientados en orden, uniendo los
vecinos con arcos de circunferencia para que el camino sea suave; donde
no cabe un arco entre dos vecinos, puede alargar uno de ellos. La
velocidad es como mucho 10, la aceleración a lo largo del camino como
mucho 1, y en un arco de radio R la velocidad es como mucho √R
(aceleración centrípeta v²/R ≤ 1). Partiendo y terminando en reposo,
hallar el menor tiempo del recorrido.

## Entrada

n (1 ≤ n ≤ 1000), luego n segmentos con las coordenadas del inicio y
del final, enteros de valor absoluto hasta 1000. Dos vecinos nunca
apuntan en el mismo sentido, y siempre existe un camino suave.

## Salida

El menor tiempo, con error absoluto o relativo de como mucho 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
0 0 4 0
```

Salida:

```
4.0000000000
```

### Ejemplo 2

Entrada:

```
2
-2 4 0 4
4 0 4 -2
```

Salida:

```
7.1415926536
```

## Solución

El camino. Sean dos vecinos: uno termina en B yendo según u, el
siguiente empieza en A yendo según v. Si las rectas no son paralelas,
se cortan en un punto X que queda t más allá de B y back antes de A.
Un arco tangente a ambas rectas las toca a distancias iguales de X, así
que al alargar como mucho un segmento la distancia con signo es
d = min(t, back), y el segmento con más holgura se alarga en la diferencia.
Con ángulo de giro φ el radio es
|d|·(1 + cos φ)/sin φ y, si d > 0, el arco gira φ. Si d < 0,
el arco da la vuelta larga, girando 2π − φ. La distancia
0 es una esquina, un arco de radio 0 donde el patinador debe parar. Los
vecinos opuestos se unen con media circunferencia a través del hueco
entre sus rectas, tras alargar uno de ellos para alinearlos.

El recorrido. El camino es ahora una cadena de piezas: segmentos con
tope de velocidad 10 y arcos con tope min(10, √R). Con aceleración y
frenada de como mucho 1, la velocidad donde se unen dos piezas es la
menor entre lo que se puede alcanzar desde el inicio, barriendo hacia
delante con v² creciendo 2·longitud y limitado por cada pieza, y
aquello desde lo que todavía se puede frenar antes del final, barriendo
hacia atrás igual. Cada pieza se recorre lo más rápido acelerando,
manteniendo el tope si hay sitio, y frenando. `O(n)`.

En el segundo ejemplo las rectas y = 4 y x = 4 se cortan 4 más allá del
primer segmento y 4 antes del segundo, lo que da un cuarto de
circunferencia de radio 4 y tope 2. El patinador acelera hasta 2 en 2
metros, recorre el arco de longitud 2π a velocidad 2 en π segundos y
frena en los últimos 2 metros: 2 + π + 2.

Trampas:

- las rectas casi paralelas pueden dar arcos y alargamientos enormes, así que
  los tiempos pueden ser enormes; la respuesta sigue siendo una suma de
  fórmulas cerradas cortas;
- el tope de una pieza limita la velocidad en sus dos extremos;
- la vuelta larga aparece cuando X queda detrás de B según u o más allá
  de A según v.

Las respuestas coinciden con una implementación aceptada independiente
en quinientos caminos aleatorios y en las pruebas grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1840_geometry.cpp](1840_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 308 KB |
| [1840_geometry.go](1840_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1396 KB |
| [1840_geometry.java](1840_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.125 s | 1132 KB |
| [1840_geometry.py](1840_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.093 s | 1728 KB |
| [1840_geometry.rs](1840_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.046 s | 376 KB |
