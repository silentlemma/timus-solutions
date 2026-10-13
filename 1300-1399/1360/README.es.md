# 1360. Disputa filosófica

[Timus 1360](https://acm.timus.ru/problem.aspx?space=1&num=1360) · dificultad 1272 · math

Problema original con idea de Den Raskovalov, preparado por Stanislav Vasiliev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Al crecer t, el punto x = sin(√t), y = cos(t) recorre el cuadrado
[−1, 1]². Dado un punto grueso, un círculo de radio ε ≥ 10⁻⁴ con centro
(x₀, y₀) dentro del cuadrado, hay que imprimir cualquier t en
[0, 10¹²] en el que la curva esté dentro del círculo, o `FAIL` si no
existe.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

x₀ e y₀ en la primera línea, ε en la segunda.

## Salida

Un momento t, o `FAIL`.

## Ejemplos

### Ejemplo 1

Entrada:

```
0.744 0.554
0.01
```

Salida:

```
5.3
```

## Solución

Las dos coordenadas cambian a velocidades muy distintas. Sea s = √t, de
modo que x = sin(s) e y = cos(s²). Cerca de un s grande, un cambio δ en s
mueve x a lo sumo δ, pero mueve t = s² unos 2sδ, que supera un período
entero del coseno en cuanto s es bastante grande.

Primero se usa r = min(ε, 1): un punto dentro de este círculo menor
también está dentro del original. Si el radio positivo desborda al
leerlo, se conserva el infinito positivo antes de aplicar este límite.

Así que se toma s₀ = asin(x₀) + 2πk con k = ⌈1/r⌉ + 1, con lo que
sin(s₀) = x₀ y s₀ ≥ 2π/r + 3π/2. A menos de π de t₀ = s₀² hay un t con
cos(t) = y₀ exacto: t = acos(y₀) + 2πj para el entero j más cercano. Su
raíz se aparta de s₀ a lo sumo π / (√(s₀² − π) + s₀) < r/4, así que x
se desvía menos de r/4 e y nada en absoluto. La respuesta nunca es
`FAIL`. Se usa j = floor((t₀ − acos(y₀)) / (2π) + 0.5), y se redondea
el resultado a millonésimas enteras con floor(t·10⁶ + 0.5) antes de
imprimir seis decimales, con los mismos pasos de redondeo en todos los
lenguajes. Tiempo y espacio: `O(1)`.

Detalles a tener en cuenta:

- con ε = 10⁻⁴ la respuesta ronda 4·10⁹, bien dentro de [0, 10¹²], así
  que t debe imprimirse con cifras suficientes: seis decimales mueven
  cos(t) a lo sumo 10⁻⁶;
- el círculo puede ser mayor que el cuadrado (prueba 05);
- ε no tiene cota superior y puede desbordar un double (prueba 13); se
  conserva el infinito positivo del análisis y se limita el radio de
  trabajo a 1;
- conviene ajustar x₀ e y₀ a [−1, 1] antes de asin y acos.

Las respuestas impresas se comprobaron en 1317 puntos, incluidas las
cuatro esquinas y el centro con ε = 10⁻⁴ y radios fuera del rango de
double; la distancia nunca pasó de 0,251·ε. Las pruebas se juzgan con un
verificador que recalcula el punto de la curva en el t impreso.

## Notas por lenguaje

- Las cinco soluciones usan la misma fórmula; Java imprime con
  `Locale.US` para que el separador decimal sea un punto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1360_math.cpp](1360_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 156 KB |
| [1360_math.go](1360_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1112 KB |
| [1360_math.java](1360_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1920 KB |
| [1360_math.py](1360_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 476 KB |
| [1360_math.rs](1360_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 248 KB |
