# 1447. Red de trasladores

[Timus 1447](https://acm.timus.ru/problem.aspx?space=1&num=1447) · dificultad 972 · graphs

Problema original de Den Raskovalov (autor) y Stanislav Vasiliev (texto), del Décimo Campeonato Universitario de Programación por Equipos de los Urales, 24–25 de marzo de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una empresa tiene N sucursales (1 ≤ N ≤ 1000) y M enlaces posibles por
traslador (1 ≤ M ≤ 500000), cada uno entre dos sucursales distintas y
con una longitud y un coste, enteros de 1 a 10⁶; ningún par de
sucursales tiene dos enlaces. La red debe conectar todas las sucursales
sin enlaces sobrantes, es decir, ser un árbol generador, y alguno
existe. La empresa paga por metro, así que Lucius Malfoy quiere el árbol
con la menor razón entre coste total y longitud total. Hay que imprimir
esa razón con precisión 10⁻⁸.

Límite de tiempo: 4 segundos. Límite de memoria: 64 MB.

## Entrada

N, M y luego M líneas con dos sucursales, la longitud y el coste de un
enlace.

## Salida

El menor coste medio por metro.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
3
1 2 50 60
1 3 100 100
2 3 100 100
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
3
3
1 2 1000 3000
1 3 1 5
2 3 1000 1997
```

Salida:

```
2
```

## Solución

Un árbol T tiene razón como mucho λ justo cuando la suma de c − λ d en
sus aristas es como mucho 0, así que la pregunta «¿hay un árbol con
razón menor que λ?» es un árbol generador mínimo con pesos c − λ d. El
método de Dinkelbach lo convierte en una iteración rápida: se toma un
árbol cualquiera, λ pasa a ser su razón, se busca el árbol mínimo para
los pesos c − λ d y, si su peso es negativo, su propia razón es menor y
se convierte en el nuevo λ; cuando el peso mínimo es 0, ningún árbol
mejora λ. La razón baja deprisa y en la práctica bastan unas pocas
rondas.

Guardar λ como fracción p / q lo hace todo exacto: los pesos c q − d p
son enteros que caben en 64 bits, así que la condición de parada no
depende del redondeo. Con hasta 500000 aristas sobre 1000 sucursales el
grafo es casi completo, así que cada árbol se construye con el algoritmo
de Prim sobre una matriz N × N en `O(N²)`, y cada ronda cuesta `O(N²)`.

Detalles a tener en cuenta:

- el árbol más barato no es el de mejor razón (ejemplo 2);
- si la red ya es un árbol, no hay elección (pruebas 05, gen4);
- las razones pueden ser diminutas, así que hace falta precisión
  absoluta y no unas pocas cifras significativas (pruebas 04, 07).

## Notas por lenguaje

- Python lee los enlaces línea a línea en filas de `array`: medio millón
  de enlaces partidos en una sola lista de palabras ocupan más de 64 MB.
  En el juez tarda 2,25 s y 9 MB, dentro del límite de 4 segundos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1447_graphs.cpp](1447_graphs.cpp) | G++ 13.2 x64 | graphs | O(N^2) per round | AC | 0.078 s | 7656 KB |
| [1447_graphs.go](1447_graphs.go) | Go 1.14 x64 | graphs | O(N^2) per round | AC | 0.140 s | 17924 KB |
| [1447_graphs.java](1447_graphs.java) | Java 1.8 | graphs | O(N^2) per round | AC | 0.281 s | 9224 KB |
| [1447_graphs.py](1447_graphs.py) | Python 3.12 x64 | graphs | O(N^2) per round | AC | 2.250 s | 9136 KB |
| [1447_graphs.rs](1447_graphs.rs) | Rust 1.75 x64 | graphs | O(N^2) per round | AC | 0.093 s | 33148 KB |
