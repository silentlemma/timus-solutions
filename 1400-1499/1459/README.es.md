# 1459. El viaje del arquero

[Timus 1459](https://acm.timus.ru/problem.aspx?space=1&num=1459) · dificultad 1672 · dp

Problema original de Alexander Ipatov, preparado por Vladimir Yakovlev, del concurso de la Universidad Estatal de los Urales en el campus de invierno de Petrozavodsk, enero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arquero es una pieza de ajedrez que avanza una casilla hacia
delante, atrás, izquierda o derecha. Está en la casilla (1, 1) de un
tablero N × M (2 ≤ N ≤ 5, 2 ≤ M ≤ 10⁹) y debe visitar cada casilla
exactamente una vez y volver al inicio. Hay que contar cuántos
recorridos así hay, módulo 10⁹.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M.

## Salida

El número de recorridos módulo 10⁹.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
```

Salida:

```
2
```

## Solución

Un recorrido es un ciclo hamiltoniano de la cuadrícula recorrido en uno
de los dos sentidos, así que la respuesta es el doble del número de
ciclos. Los ciclos se cuentan fila a fila, con filas de anchura N ≤ 5,
mediante una DP de enchufes: entre dos filas, un estado guarda qué
aristas verticales cruzan el borde y cómo se emparejan sus extremos en
caminos, escrito como paréntesis. Dentro de una fila las casillas se
procesan de una en una con un enchufe horizontal adicional; una casilla
sin enchufes empieza un camino nuevo, una con un enchufe lo continúa
hacia abajo o a la derecha, y una con dos une dos caminos, corrigiendo
el paréntesis del extremo lejano cuando se encuentran dos de apertura o
dos de cierre. Unir los dos extremos de un mismo camino cierra un ciclo,
lo que solo se permite en la última casilla y sin otros enchufes, porque
el ciclo debe cubrirlo todo.

Para anchura 5 solo hay 20 estados, así que una fila se
convierte en una pequeña matriz de transición. Las primeras M − 1 filas
son su potencia, calculada elevando al cuadrado repetidamente, desde el
estado vacío, y la última fila, que no puede sacar enchufes hacia abajo
pero puede cerrar el ciclo, se aplica al final. `O(S³ log M)` con S
estados.

Detalles a tener en cuenta:

- con un número impar de casillas no hay recorridos (pruebas 03, 08,
  12);
- dos filas tienen exactamente un ciclo sea cual sea su longitud
  (pruebas 01, 07);
- la cuenta módulo 10⁹ en los productos de matrices necesita valores
  intermedios de 64 bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1459_dp.cpp](1459_dp.cpp) | G++ 13.2 x64 | dp | O(S^3 log M) | AC | 0.015 s | 224 KB |
| [1459_dp.go](1459_dp.go) | Go 1.14 x64 | dp | O(S^3 log M) | AC | 0.031 s | 1372 KB |
| [1459_dp.java](1459_dp.java) | Java 1.8 | dp | O(S^3 log M) | AC | 0.156 s | 4236 KB |
| [1459_dp.py](1459_dp.py) | Python 3.12 x64 | dp | O(S^3 log M) | AC | 0.156 s | 856 KB |
| [1459_dp.rs](1459_dp.rs) | Rust 1.75 x64 | dp | O(S^3 log M) | AC | 0.031 s | 260 KB |
