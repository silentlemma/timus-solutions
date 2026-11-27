# 1306. Mediana de una sucesión

[Timus 1306](https://acm.timus.ru/problem.aspx?space=1&num=1306) · dificultad 145 · sorting

Problema original del Segundo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 3–4 de abril de 1998.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que hallar la mediana de 1 ≤ N ≤ 250 000 enteros de 0 a 2³¹ − 1: el
elemento central de la sucesión ordenada si N es impar, y la media de
los dos centrales si N es par. Se imprime con un decimal.

Límite de tiempo: 1 segundo. Límite de memoria: 1 MB. El enunciado
admite C, C++ y Pascal; el formulario de envío ofrece además Rust.

## Entrada

N y luego los N números, uno por línea.

## Salida

La mediana con un decimal.

## Comprobación

Comparación exacta (`judging: exact` en `tests/tests.json`): una línea
con la mediana exacta, un decimal (`.0` o `.5`) y salto de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
12
1
9
4
2
7
```

Salida:

```
5.5
```

## Solución

La sucesión entera ocupa 250 000 · 4 bytes, alrededor de 1 MB, que es
todo el límite de memoria. Pero solo importa la mitad menor: la mediana
es el mayor, o la media de los dos mayores, de los ⌊N/2⌋ + 1 números más
pequeños.

Así que un montículo de máximo guarda los ⌊N/2⌋ + 1 números más
pequeños vistos hasta ahora, unos 500 KB. Cada número nuevo entra
mientras el montículo no está lleno, o sustituye a la cima si es menor
que ella. Al final:

- con N impar la cima es la mediana;
- con N par la cima y, tras sacarla, la nueva cima son los dos
  elementos centrales.

El trabajo del montículo es `O(N log N)` en el peor caso; incluyendo
I bytes de entrada es `O(I+N log N)`. Guarda `⌊N/2⌋+1` elementos activos.
Ambos C++ reservan un array fijo de 125001 elementos (500004 bytes para
enteros de 32 bits): espacio asignado `O(C+B)`, con capacidad máxima C
y búferes acotados B, sin reducirse para cada N pequeño. Rust reserva
solo `⌊N/2⌋+1` elementos i32, pero retiene la línea más larga H:
`O(N/2+H+B)`. Con líneas de ancho acotado el espacio variable es `O(N)`.
Las sumas se calculan en un tipo más ancho.

Detalles a tener en cuenta:

- la suma de dos números cerca de 2³¹ − 1 puede desbordar un entero de
  32 bits con signo (prueba 04), pero cabe en uno sin signo; el código usa 64 bits;
- la media es entera o termina en .5, así que se imprime exacta, sin
  coma flotante (pruebas 01 y 08);
- aquí los flujos de C++ gastan demasiada memoria, así que el programa
  lee con `scanf`.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

La solución optimizada en C++ analiza los números a mano desde un búfer
de 4 KB en lugar de `scanf`. Construye de una vez el montículo con los
primeros ⌊N/2⌋ + 1 números mediante `std::make_heap`, en tiempo lineal,
en lugar de insertarlos uno a uno, y reemplaza la cima con un solo
hundimiento en lugar de `pop_heap` seguido de `push_heap`:
{1306_sorting_optimized.cpp}.

### Mejora medida

Los porcentajes comparan los Accepted guardados; no son umbrales de
admisión. Véanse los [criterios](../../RATING_CRITERIA.md): top-10/top-15%,
sustituidos con 1–10 rivales de la misma versión por la referencia
seleccionada y tolerancia del 15% o un tick. Con menos de 1024 KB se
compara solo tiempo. Se conservan versiones sencillas útiles. C++ rápido
cumple su criterio temporal guardado y Rust básico la comparación temporal
de su grupo pequeño. Identidad del fuente y métricas se verifican aparte.

Solo se corrigieron comentarios en C++ y Rust sencillos. Se preservan
los algoritmos y los demás comentarios útiles.

- `1306_sorting_optimized.cpp`: reducción de tiempo +84.73%; reducción
  de memoria +8.97%; base: `1306_sorting.cpp`.

## Notas por lenguaje

- El enunciado solo admite C, C++ y Pascal, pero el formulario de envío
  de Timus ofrece además Rust 1.75, así que hay soluciones en C++ y Rust;
  Go, Python y Java no se pueden enviar.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1306_sorting.cpp](1306_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N) | AC | 0.218 s | 608 KB | 11331139 |
| [1306_sorting.rs](1306_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N) | AC | 0.031 s | 704 KB | 11331103 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1306_sorting_optimized.cpp](1306_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(N log N) | AC | 0.031 s | 568 KB | 11304527 |
