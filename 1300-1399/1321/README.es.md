# 1321. Indicador de piso

[Timus 1321](https://acm.timus.ru/problem.aspx?space=1&num=1321) · dificultad 1353 · math

Problema original con idea de Leonid Volkov, preparado por Pavel Egorov y Igor Goldberg, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un edificio tiene los pisos 1 a N, con 4 < N < 10⁹⁹⁹. El indicador del
ascensor tiene una posición por cada cifra de N, cada una con hasta
siete segmentos, y muestra el número del piso sin ceros a la izquierda.
Un segmento que no se enciende en ningún piso del edificio no está
instalado. Un segmento averiado está siempre encendido o siempre
apagado.

Un técnico puede subir al ascensor en cualquier piso y viajar comparando el
indicador con los números de piso hasta encontrar todos los segmentos
averiados o comprobar que no hay ninguno. Hay que imprimir el menor
número de tramos entre pisos que necesita el viaje.

Las cifras son así: el 0 enciende todos menos el segmento central, el 1
los dos de la derecha, el 6 tiene el segmento superior y el 9 el
inferior, y el 7 es el superior y los dos de la derecha.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

El menor número de tramos.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
```

Salida:

```
8
```

## Solución

Un segmento se comprueba donde deba estar encendido y donde deba estar
apagado; un viaje de L a R pasa por todos los pisos intermedios, así
que se busca el intervalo [L, R] más corto en el que cada segmento
instalado deba estar encendido en algún piso y apagado en otro. Una
posición todavía sin usar, como las decenas en los pisos 1 a 9, está en
blanco: todos sus segmentos están apagados.

Sea D la cantidad de cifras de N. Para D ≥ 2, la posición más alta tiene
que cambiar durante el viaje, así que el intervalo cruza un múltiplo de
10^(D−1). Si cruza solo uno, las posiciones bajas pasan de 9 a 0. La
posición justo debajo de la más alta es la que menos cambia; su serie se
puede extender hacia atrás desde 9 y hacia delante desde 0. Solo la cifra
2 deja apagado el segmento inferior derecho, y solo 5 y 6 dejan apagado
el superior derecho, así que las series válidas más cortas son 6, 7, 8, 9, 0, 1, 2
y 9, 0, 1, 2, 3, 4, 5. Cada una cuesta cinco bloques de 10^(D−2) pisos
más uno. Si después del cruce no se llega a 2, hace falta la serie
2, …, 9, 0, que cuesta siete bloques más uno. Un solo cruce solo sirve
para la posición más alta cuando su cifra es 1: el blanco y el 1
difieren justo en los dos segmentos instalados allí. Llegar a la cifra 2
después del cruce exige que N empiece por 12 o más.

Con una cifra inicial de 2 o más, la posición más alta necesita al
menos tres estados. Blanco, 1, 2 basta cuando N empieza por 2 o 3. A
partir de 4 también está instalado el segmento superior izquierdo, y las
series más cortas son de blanco a 4 o de 1 a 5. Una serie de k estados
cuesta (k − 2) · 10^(D−1) + 1 tramos, y sus bloques intermedios muestran
todas las cifras bajas. Los edificios de una cifra necesitan los pisos
1 a 5. En resumen:

- N < 10: 4;
- N empieza por 1 y la segunda cifra es 2 o más: 5 · 10^(D−2) + 1;
- N empieza por 10 u 11: 7 · 10^(D−2) + 1;
- N empieza por 2 o 3: 10^(D−1) + 1;
- N empieza por 4 o más: 3 · 10^(D−1) + 1.

Las respuestas de varias cifras son una cifra, luego ceros y luego 1.

Detalles a tener en cuenta:

- N tiene hasta 999 cifras, así que se lee como cadena (pruebas 14 a
  16);
- con 10 u 11 pisos el viaje no llega al piso 12 y tiene que empezar en
  el piso 2 (pruebas 01 y 05);
- para N de dos cifras la respuesta no tiene ceros: 8 para 10 y 6 para
  12 (pruebas 01 y 04).

La fórmula se comparó con una ventana deslizante sobre todos los pisos
para cada N hasta 399 y para 60 N aleatorios hasta 30 000.

## Notas por lenguaje

- Python calcula el número con sus enteros grandes; los demás lenguajes
  construyen la respuesta como texto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1321_math.cpp](1321_math.cpp) | G++ 13.2 x64 | math | O(D) | AC | 0.015 s | 380 KB |
| [1321_math.go](1321_math.go) | Go 1.14 x64 | math | O(D) | AC | 0.031 s | 1100 KB |
| [1321_math.java](1321_math.java) | Java 1.8 | math | O(D) | AC | 0.125 s | 1584 KB |
| [1321_math.py](1321_math.py) | Python 3.12 x64 | math | O(D²) | AC | 0.093 s | 432 KB |
| [1321_math.rs](1321_math.rs) | Rust 1.75 x64 | math | O(D) | AC | 0.046 s | 220 KB |
