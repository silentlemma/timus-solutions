# 1584. Los secretos de los faraones

[Timus 1584](https://acm.timus.ru/problem.aspx?space=1&num=1584) · dificultad 1326 · matching

Problema original de Alex Gevak, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Unas estatuas forman una cuadrícula de n × m (n y m pares, hasta 20),
cada una una letra que indica su tipo, con menos de 30 tipos. Hay que
recolocarlas para que cada fila y cada columna se lea igual desde ambos
extremos, cargando el menor número posible de estatuas de un sitio a
otro, e imprimir ese número. Siempre es posible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y m, y luego n líneas de m letras.

## Salida

El menor número de traslados.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
abxa
xyyb
xyyx
abba
```

Salida:

```
2
```

## Solución

Filas y columnas simétricas significan que las cuatro imágenes especulares
de una casilla, (i, j), (i, m−1−j), (n−1−i, j) y (n−1−i, m−1−j), tienen
un mismo tipo. Así que la cuadrícula se divide en nm/4 grupos de cuatro
casillas, cada uno a llenar con un tipo, y un tipo con c estatuas llena
exactamente c/4 grupos.

Una estatua que ya está donde irá su tipo se queda; cualquier otra se
traslada al menos una vez, y llevarlas por cada ciclo de la permutación
cuesta exactamente esos traslados (un intercambio cuesta dos, como en el
ejemplo). Así que la respuesta es el número de casillas cuyo tipo
cambia. Dar el tipo k a un grupo cuesta 4 menos las estatuas de tipo k
que ya hay en él, y la mejor elección es un problema de asignación: una
columna por cada plaza de cada tipo (c/4 columnas para el tipo k), una
fila por grupo, resuelto con el método húngaro en O(G³) para
G = nm/4 ≤ 100 grupos. Los resultados se contrastaron con probar todas
las asignaciones en 200 cuadrículas pequeñas aleatorias.

Detalles a tener en cuenta:

- se cuentan los traslados de estatuas, no los intercambios: un
  intercambio son dos traslados (el ejemplo);
- un grupo puede tener dos tipos de dos en dos, y entonces cambian dos
  estatuas si recibe cualquiera de esos dos tipos (prueba 03);
- una elección voraz por grupos puede impedir un emparejamiento mejor en
  otro lugar, así que los grupos necesitan una asignación de verdad.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1584_matching.cpp](1584_matching.cpp) | G++ 13.2 x64 | matching | O((n m)^3) | AC | 0.031 s | 468 KB |
| [1584_matching.go](1584_matching.go) | Go 1.14 x64 | matching | O((n m)^3) | AC | 0.031 s | 1344 KB |
| [1584_matching.java](1584_matching.java) | Java 1.8 | matching | O((n m)^3) | AC | 0.156 s | 1784 KB |
| [1584_matching.py](1584_matching.py) | Python 3.12 x64 | matching | O((n m)^3) | AC | 0.171 s | 804 KB |
| [1584_matching.rs](1584_matching.rs) | Rust 1.75 x64 | matching | O((n m)^3) | AC | 0.031 s | 288 KB |
