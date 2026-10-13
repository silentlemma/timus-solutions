# 1474. Sobre ranas

[Timus 1474](https://acm.timus.ru/problem.aspx?space=1&num=1474) · dificultad 725 · constructive

Problema original de Alexander Ipatov, del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En los montículos 0 … 2N (1 ≤ N ≤ 499) hay N ranas blancas en
0 … N − 1, el montículo N vacío y N ranas negras en N + 1 … 2N. Una
rana blanca avanza a la derecha al vecino vacío o salta a la derecha
por encima de una rana negra hasta el montículo vacío; una negra hace
lo mismo hacia la izquierda. Los movimientos van en cualquier orden.
Hay que intercambiar los colores en como mucho un millón de
movimientos, escribiendo el número de movimientos y el montículo de
salida de cada uno, o −1 si es imposible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

K y luego los K montículos de salida. Se acepta cualquier secuencia
correcta.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
3
2 0 1
```

## Solución

Las ranas solo avanzan, así que cada rana blanca adelanta exactamente
una vez a cada rana negra, y solo un salto adelanta a una rana: N²
saltos. Entre todas recorren 2N(N + 1) montículos, dos por salto y uno
por paso, así que hay 2N pasos. Por tanto, toda partida con éxito dura
N² + 2N movimientos, 249 999 para N = 499, y la respuesta nunca es −1;
el único peligro es un callejón sin salida, en el que dos ranas del
mismo color se bloquean.

Los movimientos van en tandas de 1, 2, …, N, luego N otra vez y
luego N, …, 1, alternando negras y blancas, primero las negras.
Dentro de una tanda, se salta al hueco si es posible y, si no, se
avanza un paso. Este orden evita los callejones sin salida, así que
siempre hay un movimiento; reproducirlo confirma el intercambio para
cada N de 1 a 499. `O(N²)`.

Detalles a tener en cuenta:

- el orden importa: moverse con avidez sin el esquema de tandas puede
  dejar atascadas dos ranas del mismo color una tras otra (02; el
  comprobador reproduce cada movimiento);
- −1 nunca es la respuesta (todas las pruebas);
- con N = 499 se escriben 249 999 índices de salida, que conviene
  reunir en un solo búfer (gen4).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1474_constructive.cpp](1474_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.031 s | 1536 KB |
| [1474_constructive.go](1474_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.031 s | 11672 KB |
| [1474_constructive.java](1474_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.125 s | 8428 KB |
| [1474_constructive.py](1474_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.234 s | 24648 KB |
| [1474_constructive.rs](1474_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.062 s | 14840 KB |
