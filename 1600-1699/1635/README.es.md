# 1635. Mnemotecnia y palíndromos

[Timus 1635](https://acm.timus.ru/problem.aspx?space=1&num=1635) · dificultad 202 · dp

Problema original de Igor Chevdar, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Partir una cadena de letras minúsculas en la menor cantidad de
palíndromos e imprimir cuántos son y los trozos en orden. Se acepta
cualquier partición óptima.

## Entrada

Una cadena no vacía de letras latinas minúsculas, de longitud hasta 4000.

## Salida

El menor número de palíndromos y luego los trozos de una partición
óptima separados por espacios.

## Ejemplos

### Ejemplo 1

Entrada:

```
pasoib
```

Salida:

```
6
p a s o i b
```

### Ejemplo 2

Entrada:

```
zzzqxx
```

Salida:

```
3
zzz q xx
```

### Ejemplo 3

Entrada:

```
wasitacatisaw
```

Salida:

```
1
wasitacatisaw
```

## Solución

Sea dp[j] el menor número de palíndromos para el prefijo de longitud j;
entonces dp[r + 1] = min dp[l] + 1 sobre los palíndromos s[l..r], y
recordar el l del mínimo reconstruye los trozos.

C++, Go, Java y Rust enumeran los palíndromos expandiendo alrededor de
cada uno de los 2n − 1 centros de izquierda a derecha. Ese orden es
seguro: un palíndromo s[l..r] tiene su centro en l o después, mientras
que todo palíndromo que termina en l − 1 tiene el centro antes de l, así
que dp[l] ya es definitivo. `O(n²)` de tiempo en el peor caso (una sola
letra repetida) y `O(n)` de memoria.

Python no puede permitirse ocho millones de palíndromos uno a uno, así
que trabaja con conjuntos de bits. Los inicios j de los palíndromos
s[j..i] salen de los de i − 1: desplazarlos una posición hacia abajo y
quedarse con las posiciones donde está s[i], y luego añadir i mismo e
i − 1 si s[i − 1] = s[i]. Además, dp cambia a lo sumo en uno por paso
(sin su última letra, el último trozo se parte en su primera letra y un
palíndromo), así que dp[i + 1] es dp[i] − 1, dp[i] o dp[i] + 1. Con un
conjunto de bits de las posiciones para cada valor de dp, dos operaciones
«y» lo deciden, y el bit común más bajo indica el trozo.
`O(n² / 64)` operaciones de palabra.

Detalles a tener en cuenta:

- tomar primero el palíndromo más largo no es óptimo: abaab necesita dos
  trozos, a y baab, no aba, a, b (prueba 06);
- la matriz de los n² indicadores de palíndromo ocupa 16 MB en bytes; la
  expansión desde los centros no la necesita.

Un verificador acepta cualquier partición óptima; las respuestas
coinciden en el número con una implementación aceptada independiente en
100 cadenas aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1635_dp.cpp](1635_dp.cpp) | G++ 13.2 x64 | dp | O(n²) | AC | 0.015 s | 676 KB |
| [1635_dp.go](1635_dp.go) | Go 1.14 x64 | dp | O(n²) | AC | 0.046 s | 1456 KB |
| [1635_dp.java](1635_dp.java) | Java 1.8 | dp | O(n²) | AC | 0.125 s | 796 KB |
| [1635_dp.py](1635_dp.py) | Python 3.12 x64 | dp | O(n²) | AC | 0.093 s | 2064 KB |
| [1635_dp.rs](1635_dp.rs) | Rust 1.75 x64 | dp | O(n²) | AC | 0.062 s | 304 KB |
