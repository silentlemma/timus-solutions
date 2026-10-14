# 1549. Otro rompecabezas japonés

[Timus 1549](https://acm.timus.ru/problem.aspx?space=1&num=1549) · dificultad 2338 · constructive

Problema original de Stanislav Vasiliev, preparado por Vladimir Yakovlev, del XI Campeonato Universitario por Equipos de Programación de los Urales, Ekaterimburgo, 21 de abril de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay S piezas cuadradas de vía recta y T de curva (0 ≤ S, T ≤ 1000). Hay
que montar la vía cerrada más larga: un circuito de piezas en casillas
distintas de una cuadrícula, cada una unida a la siguiente por el medio
de un lado. Se escribe su longitud y las piezas en orden como F (recta),
L y R (curvas), o «Atawazu» si no se puede cerrar un circuito.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

S y T.

## Salida

El número de piezas y la cadena de F, L y R, o `Atawazu`.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 6
```

Salida:

```
10
FLLFRLLFLF
```

### Ejemplo 2

Entrada:

```
49 3
```

Salida:

```
Atawazu
```

## Solución

¿Qué cantidades de rectas f y curvas t pueden formar un circuito?

- las casillas de un circuito alternan los dos colores de un tablero de
  ajedrez, así que f + t es par;
- cada curva cambia entre movimiento horizontal y vertical, así que t es
  par, y con ello también f;
- un circuito gira 360°, así que t ≥ 4;
- sin rectas, los movimientos alternan horizontal y vertical, y cerrar
  exige un número par de cada uno, así que t es múltiplo de 4; y t = 8
  no cabe (búsqueda sobre todos los circuitos de 8 casillas).

Estas condiciones también bastan, con tres construcciones:

- el borde de una caja de 2 filas y f/2 + b + 2 casillas de ancho con b
  salientes: cada saliente sube una casilla dos casillas vecinas de la
  fila superior o inferior, añadiendo 4 curvas y gastando 2 rectas; esto
  da t = 4 + 4b, y entre las dos filas hay sitio para los salientes
  cuando f ≥ 2 o b es 0;
- para t = 6 + 4b (y entonces f ≥ 2), una caja de 3 filas con los mismos
  salientes y una esquina hundida: la casilla de la esquina se mueve en
  diagonal hacia dentro, lo que convierte dos rectas en curvas;
- sin rectas y con t ≥ 12, una escalera: L, luego LR repetido t/4 − 2
  veces, L, LR, y lo mismo otra vez.

Así que la respuesta toma el mayor f par ≤ S y el mayor t par ≤ T; solo
cuando f es 0, t baja al mayor múltiplo de 4 que sea 4 o al menos 12. El
programa coloca las casillas y lee las letras en las curvas. Todos los
S, T ≤ 120, y cualquier f o t hasta 1000 con valores pequeños del otro,
se comprobaron recorriendo la vía; una búsqueda sobre todos los
circuitos de hasta 18 casillas halló exactamente esos pares (f, t).
`O(S + T)`.

Detalles a tener en cuenta:

- ocho curvas sin rectas no cierran, cuatro sí (pruebas 04, 12);
- una recta o curva impar sobra (pruebas 01, 11);
- la vía del ejemplo es solo una de muchas; un verificador recorre la
  salida (todas las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1549_constructive.cpp](1549_constructive.cpp) | G++ 13.2 x64 | constructive | O(S + T) | AC | 0.015 s | 244 KB |
| [1549_constructive.go](1549_constructive.go) | Go 1.14 x64 | constructive | O(S + T) | AC | 0.031 s | 1308 KB |
| [1549_constructive.java](1549_constructive.java) | Java 1.8 | constructive | O(S + T) | AC | 0.125 s | 1868 KB |
| [1549_constructive.py](1549_constructive.py) | Python 3.12 x64 | constructive | O(S + T) | AC | 0.093 s | 1000 KB |
| [1549_constructive.rs](1549_constructive.rs) | Rust 1.75 x64 | constructive | O(S + T) | AC | 0.046 s | 440 KB |
