# 1360. Disputa filosófica

[Timus 1360](https://acm.timus.ru/problem.aspx?space=1&num=1360) · dificultad 1284 · math

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

Así que se toma s₀ = asin(x₀) + 2πk con k = ⌈1/ε⌉ + 1, con lo que
sin(s₀) = x₀ y s₀ > 2π/ε. A menos de π de t₀ = s₀² hay un t con
cos(t) = y₀ exacto: t = acos(y₀) + 2πj para el entero j más cercano. Su
raíz se aparta de s₀ unos |t − t₀| / (2s₀) ≤ π / (2s₀) < ε/4, así que x
se desvía menos de ε/4 e y nada en absoluto. La respuesta nunca es
`FAIL`. `O(1)`.

Detalles a tener en cuenta:

- con ε = 10⁻⁴ la respuesta ronda 4·10⁹, bien dentro de [0, 10¹²], así
  que t debe imprimirse con cifras suficientes: seis decimales mueven
  cos(t) a lo sumo 10⁻⁶;
- el círculo puede ser mayor que el cuadrado (prueba 05);
- conviene ajustar x₀ e y₀ a [−1, 1] antes de asin y acos.

La distancia de la curva al centro se comprobó en 307 puntos, incluidas
las cuatro esquinas y el centro con ε = 10⁻⁴; nunca pasó de 0,25·ε. Las
pruebas se juzgan con un verificador que recalcula el punto de la curva
en el t impreso.

## Notas por lenguaje

- Las cinco soluciones usan la misma fórmula; Java imprime con
  `Locale.US` para que el separador decimal sea un punto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1360_math.cpp](1360_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 164 KB |
| [1360_math.go](1360_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1088 KB |
| [1360_math.java](1360_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1920 KB |
| [1360_math.py](1360_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 368 KB |
| [1360_math.rs](1360_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 264 KB |
