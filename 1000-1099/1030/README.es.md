# 1030. La distancia por círculo máximo entre un barco y un iceberg

[Timus 1030](https://acm.timus.ru/problem.aspx?space=1&num=1030) · dificultad 898 · geometry, parsing

Problema original de Evgeny Shtykov, del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un mensaje de radio da las coordenadas de un barco y de un iceberg sobre una
esfera perfecta de 6875 millas de diámetro. Imprime la longitud del camino
más corto sobre la esfera entre ellos, con dos decimales, y añade la línea
`DANGER!` si la distancia impresa es menor que 100.00 millas.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

El mensaje tiene siempre exactamente estas líneas (los valores cambian):

```text
Message #<n>.
Received at <HH>:<MM>:<SS>.
Current ship's coordinates are
<X1>^<X2>'<X3>" <NL o SL>
and <Y1>^<Y2>'<Y3>" <EL o WL>.
An iceberg was noticed at
<X1>^<X2>'<X3>" <NL o SL>
and <Y1>^<Y2>'<Y3>" <EL o WL>.
===
```

`X1^X2'X3"` son X1 grados, X2 minutos y X3 segundos de latitud norte (`NL`)
o sur (`SL`), de 0 a 90 grados; `Y1^Y2'Y3"` es la longitud, este (`EL`) u
oeste (`WL`), de 0 a 180 grados.

## Salida

```text
The distance to the iceberg: <s> miles.
```

con `<s>` impreso con dos decimales, seguido de la línea `DANGER!` cuando el
`<s>` impreso es menor que 100.00.

## Evaluación

La salida se compara token a token; los números pueden diferir como mucho en
0.01.

## Ejemplos

### Ejemplo 1

Entrada:

```
Message #100.
Received at 00:10:20.
Current ship's coordinates are
12^30'00" NL
and 40^10'00" WL.
An iceberg was noticed at
12^10'00" NL
and 41^00'00" WL.
===
```

Salida:

```
The distance to the iceberg: 52.78 miles.
DANGER!
```

### Ejemplo 2

Entrada:

```
Message #101.
Received at 01:11:21.
Current ship's coordinates are
55^45'20" NL
and 37^37'00" EL.
An iceberg was noticed at
59^56'30" NL
and 30^18'00" EL.
===
```

Salida:

```
The distance to the iceberg: 342.61 miles.
```

## Solución

**Lectura.** Cada coordenada son tres enteros seguidos de `NL`, `SL`, `EL`
o `WL`. Se reemplazan los caracteres `^`, `'` y `"` por espacios, se divide
el texto en tokens y, en cada token de la forma `?L` con `?` entre
`N S E W`, se toman los tres tokens anteriores como grados, minutos y
segundos. El valor es `grados + minutos / 60 + segundos / 3600`, negativo
para el sur y el oeste. Los dos primeros valores son el barco y los dos
últimos el iceberg.

**Distancia.** Para latitudes `φ1, φ2` y longitudes `λ1, λ2` en radianes, el
ángulo central `θ` entre los puntos lo da la **fórmula del haverseno**

`hav θ = sin²((φ2 - φ1) / 2) + cos φ1 · cos φ2 · sin²((λ2 - λ1) / 2)`,

así que `θ = 2 · asin(sqrt(hav θ))` y la distancia es `R · θ` con
`R = 6875 / 2`. La ley esférica de los cosenos,
`cos θ = sin φ1 sin φ2 + cos φ1 cos φ2 cos(λ2 - λ1)`, da el mismo valor pero
pierde precisión con puntos cercanos, donde `cos θ` está muy cerca de 1.

**La línea de peligro.** Depende del valor impreso: una distancia de 99.996
millas se imprime como `100.00` y no es peligrosa. Compara con 100.00 la
distancia redondeada a centésimas.

Detalles a tener en cuenta:

- longitudes a ambos lados del meridiano 180 (`179°59' E` y `179°59' W`
  están a 2 minutos);
- limita `hav θ` a 1 antes de `sqrt`/`asin`: el redondeo puede pasarlo de 1
  para puntos antípodas;
- el umbral va sobre el valor redondeado, no sobre el exacto.

## Notas por lenguaje

La misma lectura y fórmula en todos los lenguajes; Python usa una expresión
regular y Java imprime con `Locale.US`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1030_geometry.cpp](1030_geometry.cpp) | G++ 13.2 x64 | geometry | O(length of the message) | AC | 0.015 s | 352 KB |
| [1030_geometry.go](1030_geometry.go) | Go 1.14 x64 | geometry | O(length of the message) | AC | 0.046 s | 1120 KB |
| [1030_geometry.java](1030_geometry.java) | Java 1.8 | geometry | O(length of the message) | AC | 0.093 s | 988 KB |
| [1030_geometry.py](1030_geometry.py) | Python 3.12 x64 | geometry | O(length of the message) | AC | 0.062 s | 516 KB |
| [1030_geometry.rs](1030_geometry.rs) | Rust 1.75 x64 | geometry | O(length of the message) | AC | 0.015 s | 288 KB |
