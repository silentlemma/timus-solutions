# 1183. La secuencia de paréntesis correcta más corta que contiene una dada

[Timus 1183](https://acm.timus.ru/problem.aspx?space=1&num=1183) · dificultad 196 · dp

Problema original de Andrew Stankevich, del concurso regional ACM ICPC del noreste de Europa 2001–2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados hasta 100 caracteres de `(`, `)`, `[`, `]`, hay que imprimir una
secuencia correcta de paréntesis lo más corta posible que los contenga
como subsecuencia.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Los paréntesis en una línea, que puede estar vacía.

## Salida

Una secuencia correcta más corta que los contenga.

## Evaluación

Se acepta cualquier secuencia correcta que contenga los paréntesis dados
en orden y sea tan corta como la respuesta guardada.

## Ejemplos

### Ejemplo 1

Entrada:

```
([(]
```

Salida:

```
()[()]
```

## Solución

Sea `add[i][j]` el menor número de paréntesis que hay que añadir para que
el trozo `s[i..j)` sea correcto. Un paréntesis suelto necesita una
pareja. Un trozo más largo o bien tiene una pareja que encaja en sus
extremos, envolviendo el mejor arreglo del interior, o bien se parte en
dos partes que se arreglan por separado:

`add[i][j] = min(add[i+1][j−1] si s[i] y s[j−1] encajan, min sobre k de add[i][k] + add[k][j])`.

Anotando qué opción ganó se puede reconstruir la secuencia: un paréntesis
suelto se imprime con su pareja, una pareja envolvente alrededor de su
interior y una partición como sus dos mitades. `O(n³)` para `n ≤ 100`.

Detalles a tener en cuenta:

- la línea de entrada puede estar vacía, y entonces la respuesta es una
  línea vacía;
- en los empates hay que anotar igualmente una opción real, o la
  reconstrucción tomaría un trozo largo por un paréntesis suelto;
- `([)]` necesita dos paréntesis más, y tanto `()[()]` como `([])[]` son
  de las más cortas; se acepta cualquiera.

Las respuestas se compararon con una solución escrita aparte en 300
líneas aleatorias de hasta 100 paréntesis, y cada secuencia impresa pasó
el comprobador.

## Notas por lenguaje

- Python reconstruye la respuesta con una pila explícita; los demás
  lenguajes usan recursión, de a lo sumo 100 niveles.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1183_dp.cpp](1183_dp.cpp) | G++ 13.2 x64 | dp | O(n³) | AC | 0.015 s | 460 KB |
| [1183_dp.go](1183_dp.go) | Go 1.14 x64 | dp | O(n³) | AC | 0.031 s | 1232 KB |
| [1183_dp.java](1183_dp.java) | Java 1.8 | dp | O(n³) | AC | 0.078 s | 616 KB |
| [1183_dp.py](1183_dp.py) | Python 3.12 x64 | dp | O(n³) | AC | 0.078 s | 876 KB |
| [1183_dp.rs](1183_dp.rs) | Rust 1.75 x64 | dp | O(n³) | AC | 0.001 s | 308 KB |
