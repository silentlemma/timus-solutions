# 2031. Una fila que gira hasta enteros consecutivos

[Timus 2031](https://acm.timus.ru/problem.aspx?space=1&num=2031) · dificultad 88 · bruteforce

Problema original de Nikita Sivukhin, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Construye una fila de `n` números decimales que, al girar toda la fila
180 grados, produzca un segmento creciente de enteros positivos
consecutivos. Cada número impreso debe tener exactamente dos cifras: los
de una cifra llevan cero inicial. El giro invierte tanto el orden de los
números como las cifras dentro de cada uno. `0`, `1`, `8` quedan
iguales; `6` y `9` se intercambian. Las demás cifras quedan ilegibles.

Límite de entrada: `1 ≤ n ≤ 99`. Tiempo: 1 segundo. Memoria: 64 MB.

## Entrada

Un entero `n`, la cantidad de palabras numéricas en la fila.

## Salida

Cualquier fila válida de `n` números de dos cifras separados por
espacios. Si no existe, imprime exactamente `Glupenky Pierre`. Los
valores girados deben ser positivos, por lo que `00` no vale. Conserva
los ceros iniciales de las demás palabras.

## Evaluación

Un comprobador gira la fila impresa y verifica que se obtiene una serie
de enteros positivos consecutivos, cada uno con dos dígitos legibles; la
imposibilidad solo se acepta si no existe tal serie. Se acepta cualquier
fila válida.

## Ejemplos

```
2
```

```
11 01
```

```
99
```

```
Glupenky Pierre
```

## Solución

Solo las cifras 0, 1, 6, 8 y 9 se leen al revés, así que tras el giro
solo pueden aparecer los números del 1 al 99 formados por ellas. Se
recorren 1 … 99, se cuenta la racha actual de números legibles
consecutivos y se para cuando llega a n en algún número r. Entonces se
imprimen r, r − 1, …, r − n + 1 al revés: de cada número, primero la
cifra de las unidades girada y luego la de las decenas girada, así que
la fila girada lee la racha en orden creciente. Si ninguna racha es lo
bastante larga, la respuesta es `Glupenky Pierre`. `O(100 + n)`.

Los números legibles son 1, 6, 8, 9, 10, 11, 16, 18, 19, 60, 61, 66, 68,
69, 80, 81, 86, 88, 89, 90, 91, 96, 98, 99; las rachas más largas, 8–11
y 88–91, tienen cuatro números, así que solo n ≤ 4 tiene respuesta.

Detalles a tener en cuenta:

- al girar, el 6 y el 9 se intercambian;
- se conserva el cero inicial: 01 al revés es 10;
- 00 se convertiría en 0, que no es positivo.

## Soluciones optimizadas

La solución optimizada en C++ lee `n` con `getchar` e imprime las cifras
una a una con `putchar`, sin `iostream` y sin construir una cadena:
88 KB en lugar de 368 KB, con el mismo tiempo.

## Notas por lenguaje

- Los números girados se construyen con caracteres, así que el cero
  inicial se conserva.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2031_bruteforce.cpp](2031_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(100+n) | AC | 0.015 s | 368 KB | 11303664 |
| [2031_bruteforce.go](2031_bruteforce.go) | Go 1.14 x64 | bruteforce | O(100+n) | AC | 0.031 s | 1152 KB | 11303665 |
| [2031_bruteforce.java](2031_bruteforce.java) | Java 1.8 | bruteforce | O(100+n) | AC | 0.093 s | 440 KB | 11303530 |
| [2031_bruteforce.py](2031_bruteforce.py) | Python 3.12 x64 | bruteforce | O(100+n) | AC | 0.078 s | 420 KB | 11303666 |
| [2031_bruteforce.rs](2031_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(100+n) | AC | 0.015 s | 204 KB | 11303667 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2031_bruteforce_optimized.cpp](2031_bruteforce_optimized.cpp) | G++ 13.2 x64 | bruteforce | O(100+n) | AC | 0.015 s | 88 KB | 11303668 |
