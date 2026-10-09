# 1043. El rectángulo entero que encierra un arco de circunferencia

[Timus 1043](https://acm.timus.ru/problem.aspx?space=1&num=1043) · dificultad 1626 · geometry

Problema original de Alexander Mironenko, del V Campeonato por Equipos de Programación de la Universidad Estatal de los Urales, octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arco de circunferencia se da por sus dos extremos `A`, `B` y otro
punto `C` del arco; los tres tienen coordenadas enteras de valor absoluto
como mucho 1000 y no están alineados. El centro de la circunferencia y
todo el arco están en el cuadrado `[-1000, 1000]^2`. Halla el área mínima
de un rectángulo de lados paralelos a los ejes y vértices enteros que
cubra el arco.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Tres líneas con las coordenadas de `A`, `B` y `C`.

## Salida

El área mínima.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
476 612
487 615
478 616
```

Salida:

```
66
```

### Ejemplo 2

Entrada:

```
-5 0
5 0
0 5
```

Salida:

```
50
```

## Solución

La caja que encierra el arco está formada por sus extremos y por aquellos
de los cuatro puntos extremos de la circunferencia (`centro ± r` en cada
eje) que están en el arco. Después, los límites inferiores se redondean
hacia abajo y los superiores hacia arriba.

Un punto de la circunferencia está en el arco exactamente cuando es `A`,
`B`, o está del mismo lado de la recta `AB` que `C`. Así que la prueba es
el signo de un producto vectorial.

La dificultad es la precisión. Un extremo como `centro_x + r` puede ser
exactamente entero, o fallar por `10^-8`; entonces `ceil` en coma
flotante da fácilmente una respuesta errónea. Las soluciones trabajan de
forma exacta con enteros:

- el centro es `(ux / d, uy / d)` con enteros `ux`, `uy`, `d > 0` (regla
  de Cramer), y `r · d = sqrt(rho2)` con `rho2` entero;
- `ceil(centro_x + r)` es el menor entero `k` con `k·d − ux ≥ 0` y
  `(k·d − ux)^2 ≥ rho2`; una estimación en coma flotante da el punto de
  partida, y las comparaciones exactas lo mueven un paso o dos; `floor` es
  simétrico;
- el lado de un punto extremo, multiplicado por `d`, tiene la forma
  `alpha − gamma · sqrt(rho2)` con enteros `alpha`, `gamma`, y su signo se
  obtiene comparando `alpha^2` con `gamma^2 · rho2` (tras mirar los signos
  de `alpha` y `gamma`).

Los números llegan a unos `10^28`, lo que exige enteros de 128 bits.
`O(1)`.

Detalles a tener en cuenta:

- un extremo exactamente sobre una línea de la cuadrícula no debe alejar
  el borde una unidad más, y uno que la pasa apenas sí debe;
- un extremo que coincide con un extremo del arco da lado 0: ya está
  contado como extremo;
- el centro puede estar en un semientero, así que los extremos enteros no
  exigen un centro entero (pruebas 13 y 14).

## Notas por lenguaje

- **C++**: `__int128`; **Rust**: `i128`.
- **Go**: `math/big`; **Java**: `BigInteger`; **Python**: enteros
  integrados, con `math.isqrt` para el punto de partida.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1043_geometry.cpp](1043_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 400 KB |
| [1043_geometry.go](1043_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1216 KB |
| [1043_geometry.java](1043_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1724 KB |
| [1043_geometry.py](1043_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 828 KB |
| [1043_geometry.rs](1043_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 220 KB |
