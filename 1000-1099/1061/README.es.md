# 1061. La ventana más barata de búferes libres

[Timus 1061](https://acm.timus.ru/problem.aspx?space=1&num=1061) · dificultad 666 · prefix_sums

Problema original del concurso regional ACM ICPC del noreste de Europa 2000–2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` búferes (`1 ≤ N ≤ 100000`), cada uno bloqueado (`*`) o con un
valor de 0 a 9. Elige `K` búferes consecutivos (`1 ≤ K ≤ 10000`), ninguno
bloqueado, con el menor valor total, e imprime el número `L` del primero;
con totales iguales, el menor `L`. Imprime `0` si no existe tal ventana.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `K`, y luego los `N` estados, 80 caracteres por línea (la última
puede ser más corta).

## Salida

`L`, o `0`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
100 53
2165745216091853477755800393859785807207523169954341**7363*9*94664808*4777717089
09825185827659480548
```

Salida:

```
0
```

### Ejemplo 2

Entrada:

```
100 10
2165745216091853477755800393859785807207523169954341**7363*9*94664808*4777717089
09825185827659480548
```

Salida:

```
36
```

## Solución

Dos sumas prefijas sobre los búferes: el valor total y el número de
búferes bloqueados entre los `i` primeros. Una ventana `[L, L + K − 1]` es
válida cuando el número de bloqueos no cambia a lo largo de ella, y su
valor es una diferencia de las sumas de valores. Revisar las `N − K + 1`
ventanas de izquierda a derecha y cambiar la mejor solo con un valor
estrictamente menor da el menor `L` entre las más baratas. `O(N)`.

Detalles a tener en cuenta:

- `K > N`: no hay ninguna ventana, la respuesta es `0`;
- empates: se conserva la primera ventana, así que la mejor solo se
  cambia con un valor estrictamente menor;
- los estados están repartidos en líneas de 80 caracteres: se leen
  caracteres y se saltan los saltos de línea;
- los búferes bloqueados no tienen valor; solo invalidan ventanas.

## Notas por lenguaje

- **C++**, **Go**, **Java**: los estados se leen carácter a carácter tras
  los dos números.
- **Python**, **Rust**: toda la entrada se separa en palabras y se unen
  las filas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1061_prefix_sums.cpp](1061_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.015 s | 1372 KB |
| [1061_prefix_sums.go](1061_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 2700 KB |
| [1061_prefix_sums.java](1061_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.093 s | 1600 KB |
| [1061_prefix_sums.py](1061_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.109 s | 9248 KB |
| [1061_prefix_sums.rs](1061_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.015 s | 2196 KB |
