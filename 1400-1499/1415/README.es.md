# 1415. Vida móvil

[Timus 1415](https://acm.timus.ru/problem.aspx?space=1&num=1415) · dificultad 7929 · geometry, simulation

Problema original de Evgeny Krokhalev, del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N estaciones base (N ≤ 100) están en puntos enteros; la estación c
tiene una distancia umbral R_c y un nombre. La potencia de la señal es
inversamente proporcional a la distancia, y el indicador del teléfono
es violeta dentro de R_c y baja un color (índigo, azul, verde,
amarillo, naranja, rojo) por cada 2 dB de potencia perdida, quedándose
en rojo más allá. Se lleva un teléfono a lo largo de una poligonal de
M ≤ 1000 segmentos. Al encenderse elige la estación más potente,
siempre desempatando por el nombre lexicográficamente menor; se queda
con ella hasta que el indicador se pone rojo, y mientras está en rojo
cambia a la estación más potente cuya señal no sea roja en cuanto
exista una. Hay que imprimir el registro del encendido, los cambios de
celda y los cambios
de color; la línea del rojo se escribe aunque el teléfono cambie en ese
mismo instante.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas X Y R nombre, luego M, luego M segmentos X1 Y1 X2 Y2.

## Salida

El registro.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0 1 Romashka
0 10 1 Lutik
10 10 2 Znaika
10 0 1 Children
2
5 5 -5 -5
-5 -5 5 5
```

Salida:

```
Power on. CELL_ID:Znaika, SIGNAL_LEVEL:GREEN
Signal changed. SIGNAL_LEVEL:YELLOW
Signal changed. SIGNAL_LEVEL:ORANGE
Signal changed. SIGNAL_LEVEL:RED
Cell changed. CELL_ID:Romashka, SIGNAL_LEVEL:YELLOW
Signal changed. SIGNAL_LEVEL:ORANGE
Signal changed. SIGNAL_LEVEL:YELLOW
Signal changed. SIGNAL_LEVEL:GREEN
Signal changed. SIGNAL_LEVEL:BLUE
Signal changed. SIGNAL_LEVEL:INDIGO
Signal changed. SIGNAL_LEVEL:VIOLET
Signal changed. SIGNAL_LEVEL:INDIGO
Signal changed. SIGNAL_LEVEL:BLUE
Signal changed. SIGNAL_LEVEL:GREEN
Signal changed. SIGNAL_LEVEL:YELLOW
Signal changed. SIGNAL_LEVEL:ORANGE
```

## Solución

La potencia es proporcional a R / d, así que la pérdida es
10·log₁₀(d / R) dB y el color cambia en las circunferencias de radio
R·10^(k/5) para k = 0..5: violeta dentro de la primera, rojo fuera de
la última, de radio 10·R.

En un segmento p(t) = s + t·(e − s), los instantes en que la distancia
a una estación iguala un radio resuelven una ecuación de segundo grado
en t. Solo importan dos clases de instantes: la estación actual cruza
cualquiera de sus seis circunferencias, y cualquier estación cruza su
circunferencia roja (solo entonces alguna estación deja de ser roja o
pasa a serlo). Se ordenan y se agrupan los que distan como máximo 10⁻⁹
en t del primer instante del grupo. Se mira el estado justo después
de cada grupo, en el punto medio hasta el siguiente instante:

- si el teléfono no estaba en rojo, se registra el color de la
  estación actual solo si ha cambiado; si ahora está en rojo, toda
  estación que no sea roja ahí es candidata;
- si el teléfono estaba en rojo, las candidatas son las estaciones del
  grupo que han dejado de ser rojas.

Entre las candidatas gana la más potente, comparando R / d en el propio
instante con una tolerancia relativa, para que las estaciones que
llegan a la vez a su circunferencia roja empaten y decida el nombre
menor. Si gana la estación actual, solo se registra el color; si no, es
un cambio de celda, su color se lee justo después del instante y antes
de su siguiente circunferencia, y los instantes se rehacen para la
nueva estación. `O(M·N²·log N)`.

Detalles a tener en cuenta:

- el teléfono se queda con una estación débil mientras no esté en rojo,
  aunque haya otra mucho más potente al lado (pruebas 04, 10);
- recuperar la estación actual desde el rojo es un cambio de color, no
  de celda (pruebas 02, 12, 17);
- varias estaciones pueden llegar a su circunferencia roja en el mismo
  instante; con potencia igual se elige el nombre menor comparando byte
  a byte (pruebas 04, 08, 09, gen3);
- el teléfono puede encenderse en rojo sin nada al alcance, y hay
  segmentos de longitud cero (pruebas 06, 07);
- un ejemplo del foro tiene sucesos separados por unos 6,3·10⁻²¹ en t;
  incluso long double de 80 bits puede redondearlos al mismo valor.

## Notas por lenguaje

- Python se ejecuta con PyPy: CPython excede el límite de 2 s en la
  prueba 20 del juez, y PyPy tarda 1,8 s, cerca del límite, aunque cada
  prueba de aquí tarda mucho menos de 0,5 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1415_geometry.cpp](1415_geometry.cpp) | G++ 13.2 x64 | geometry | O(M*N^2*log N) | AC | 0.125 s | 8800 KB |
| [1415_geometry.go](1415_geometry.go) | Go 1.14 x64 | geometry | O(M*N^2*log N) | AC | 0.140 s | 6788 KB |
| [1415_geometry.java](1415_geometry.java) | Java 1.8 | geometry | O(M*N^2*log N) | AC | 0.359 s | 44480 KB |
| [1415_geometry.py](1415_geometry.py) | PyPy 3.10 x64 | geometry | O(M*N^2*log N) | AC | 1.796 s | 46860 KB |
| [1415_geometry.rs](1415_geometry.rs) | Rust 1.75 x64 | geometry | O(M*N^2*log N) | AC | 0.093 s | 10192 KB |
