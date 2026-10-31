# 1413. Saltador marciano

[Timus 1413](https://acm.timus.ru/problem.aspx?space=1&num=1413) · dificultad 180 · simulation

Problema original de Stanislav Vasiliev, del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un vehículo se maneja con un teclado numérico: cada tecla de 1 a 9
salvo el 5 da un salto de exactamente un metro en la dirección de esa
tecla vista desde el 5 central (8 es norte, 6 este, 9 noreste, etc.),
el 5 toma una muestra del suelo y el 0 hace que el vehículo se
autodestruya. Dadas hasta 10⁶ pulsaciones, hay que imprimir dónde
termina el vehículo: en el primer 0 o, si no hay ninguno, tras la
última tecla. La respuesta es el desplazamiento al este y al norte, con
un error absoluto o relativo de como mucho 10⁻¹⁰.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

Las cifras de las teclas pulsadas.

## Salida

X e Y, el desplazamiento al este y al norte.

## Ejemplos

### Ejemplo 1

Entrada:

```
1236987412369870234567890123456789
```

Salida:

```
1.0000000000 0.0000000000
```

## Solución

Se cuenta cuántas veces se pulsó cada tecla antes del primer 0. Un
salto recto mueve un eje un metro entero y uno diagonal mueve ambos
ejes 1/√2, así que el punto final en cada eje es (suma recta) + (suma
diagonal) / √2, calculado a partir de sumas enteras. Contar evita el
redondeo en cada salto, pero la multiplicación y la suma finales en
coma flotante y la salida con diez decimales todavía redondean; el
error absoluto puede superar ligeramente 10⁻¹⁰. `O(n)`.

Detalles a tener en cuenta:

- las teclas después del primer 0 se ignoran (pruebas 01, 05, gen2);
- un salto diagonal mide un metro, no √2 (prueba 04);
- las coordenadas diagonales son irracionales, por lo que contar no
  hace exactas las coordenadas finales (prueba 04);
- leer un millón de caracteres con una llamada de entrada lenta por cada
  uno puede llevarse buena parte de los 0.5 segundos, así que las
  soluciones leen tokens enteros, líneas o toda la entrada de una vez.

## Soluciones optimizadas

La solución optimizada en Go cuenta las teclas en un búfer reutilizable
de 4 KB en lugar de leer de una vez a memoria las hasta 10⁶ pulsaciones:
{1413_simulation_optimized.go}.

La solución optimizada en Java cuenta las teclas directamente sobre los
bytes de un `BufferedInputStream` y se detiene en el primer 0, en lugar
de decodificar la entrada en líneas `String` de hasta un millón de
caracteres con `BufferedReader`: {1413_simulation_optimized.java}.

La solución optimizada en Python lee la entrada en trozos de 8 KB y
cuenta los dígitos de cada trozo con `bytes.count`, en lugar de leer de
una vez a memoria las hasta 10⁶ pulsaciones; tras el primer 0 el resto
de la entrada se lee pero no se cuenta: {1413_simulation_optimized.py}.

La solución optimizada en Rust cuenta las teclas en un búfer
reutilizable de 4 KB en lugar de leer de una vez las hasta 10⁶
pulsaciones en un vector: {1413_simulation_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1413_simulation_optimized.go`: reducción de tiempo +0.00%; reducción
  de memoria +68.46%; base: `1413_simulation.go`.

- `1413_simulation_optimized.java`: reducción de tiempo -17.20%;
  reducción de memoria +83.87%; base: `1413_simulation.java`.

- `1413_simulation_optimized.py`: reducción de tiempo +16.13%; reducción
  de memoria +82.94%; base: `1413_simulation.py`.

- `1413_simulation_optimized.rs`: reducción de tiempo +0.00%; reducción
  de memoria +88.58%; base: `1413_simulation.rs`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1413_simulation.cpp](1413_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 1832 KB | 11307301 |
| [1413_simulation.go](1413_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.015 s | 3196 KB | 11286093 |
| [1413_simulation.java](1413_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.093 s | 5804 KB | 11307330 |
| [1413_simulation.py](1413_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.093 s | 3072 KB | 11286094 |
| [1413_simulation.rs](1413_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 2136 KB | 11286097 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1413_simulation_optimized.go](1413_simulation_optimized.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.015 s | 1008 KB | 11307331 |
| [1413_simulation_optimized.java](1413_simulation_optimized.java) \* | Java 1.8 | simulation | O(n) | AC | 0.109 s | 936 KB | 11307336 |
| [1413_simulation_optimized.py](1413_simulation_optimized.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 524 KB | 11307334 |
| [1413_simulation_optimized.rs](1413_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 244 KB | 11307332 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
