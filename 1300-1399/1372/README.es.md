# 1372. Estrella de la Muerte

[Timus 1372](https://acm.timus.ru/problem.aspx?space=1&num=1372) · dificultad 5382 · geometry

Problema original con idea de Alexander Mironenko, preparado por Pavel Egorov, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una estación esférica de radio R tiene N ≤ 9 motores encendidos sin
remedio, cada uno en un mástil de altura h en una longitud y latitud
dadas, y todos empujan con el mismo empuje F en una dirección dada,
escrita también como longitud y latitud. Un motor más, en un mástil
igual, puede ponerse en cualquier sitio, apuntar a cualquier lado y
tener cualquier empuje. Hay que elegirlo para que la estación deje de
acelerar su giro, con el menor empuje, e imprimir su lugar, su dirección
y su empuje con 8 decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

R, la masa de la estación y h, luego F y N, luego N líneas: la longitud
y latitud de un motor y de su dirección.

## Salida

La longitud y latitud del motor nuevo, las de su dirección, y su
empuje. Se acepta cualquier respuesta con el menor empuje.

## Ejemplos

### Ejemplo 1

Entrada:

```
100.3 1000000.45 15.5
156.5 1
0.0 0.0 90.0 0.0
```

Salida:

```
0.00 0.00 270.00 0.00 156.50
```

## Solución

Los motores aceleran el giro con su momento total T = Σ pᵢ × F dᵢ,
donde pᵢ es el vector de posición del motor, de longitud R + h, y dᵢ la
dirección unitaria de su empuje. La masa no importa. El motor nuevo debe
aportar −T.

Una fuerza f en un punto p da el momento p × f, y |p × f| ≤ |p| · |f|.
Así que el empuje es al menos |T| / (R + h), y vale justo eso cuando p es
perpendicular a T y f = p × T / |p|²; entonces p × f = −T. Sirve
cualquier punto del círculo máximo perpendicular a T. Las soluciones
toman el eje de coordenadas menos alineado con T, le quitan su parte a
lo largo de T y usan el resultado como dirección de colocación. Longitud
y latitud se recuperan con atan2 y asin. `O(N)`.

Detalles a tener en cuenta:

- sin momento total no hay nada que hacer: empuje 0 (pruebas 02 y 04);
- una longitud apenas menor que 360 se imprime como `360.00000000`, así
  que se lleva de vuelta a 0 (prueba 09);
- la masa de la entrada es un señuelo;
- en los polos la longitud es arbitraria (prueba 03).

Las pruebas se juzgan con un verificador que recalcula el momento que
queda y el menor empuje; 400 estaciones aleatorias lo pasaron, muchas
con motores en los polos o a lo largo de los ejes.

## Notas por lenguaje

- Las cinco soluciones usan los mismos vectores; Java lee e imprime con
  `Locale.US`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1372_geometry.cpp](1372_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 172 KB |
| [1372_geometry.go](1372_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1096 KB |
| [1372_geometry.java](1372_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.125 s | 2064 KB |
| [1372_geometry.py](1372_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.078 s | 876 KB |
| [1372_geometry.rs](1372_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 300 KB |
