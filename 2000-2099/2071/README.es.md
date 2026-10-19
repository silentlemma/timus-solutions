# 2071. Orden de los cócteles con menos vertidos

[Timus 2071](https://acm.timus.ru/problem.aspx?space=1&num=2071) · dificultad 640 · bitmask, dp

Problema original de Mikhail Rubinchik, preparado por Nickolai Permyakov y Alexey Danilyuk, del Concurso Regional Escolar de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de n clientes pide un cóctel: un conjunto no vacío de los zumos
A, B y P. Los vasos se ponen en fila en algún orden, y un vertido llena
un tramo de vasos consecutivos con un zumo (primero manzana, luego
plátano y luego piña, así que el orden de los vertidos no es problema).
Cada vaso debe recibir exactamente los zumos de su cóctel. Ordenar los
vasos para necesitar el menor número de vertidos. Los límites son
1 segundo y 64 MB.

## Entrada

n, 1 ≤ n ≤ 10⁵, y después n líneas, cada una A, B, P, AB, AP, BP o ABP.

## Salida

El menor número de vertidos y después los números de los vasos en el
orden de la fila. Se acepta cualquier orden óptimo.

## Evaluación

Un comprobador compara el número de vertidos y recuenta los vertidos que
necesita el orden impreso.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
A
B
ABP
```

Salida:

```
3
1 3 2
```

## Solución

Con la fila fija, cada zumo necesita un vertido por cada tramo maximal de
vasos que lo contienen, así que el coste es el número de lugares donde
un zumo está en un vaso pero no en el anterior (el primer vaso cuenta
todos sus zumos). Mover un vaso junto a otro igual nunca añade tramos,
así que todos los vasos de un cóctel pueden ir juntos, y solo importa el
orden de a lo sumo siete cócteles distintos.

Se ordenan con una DP sobre subconjuntos: best[S][last] es el menor
número de vertidos para una fila hecha de los cócteles de S que termina
en last. Añadir el cóctel k cuesta los zumos de k que faltan en last, es
decir popcount(k & ~last). La respuesta es el mínimo sobre last para el
conjunto completo, y los predecesores guardados dan el orden. Con siete
cócteles son 2⁷ · 7 · 7 pasos, así que el trabajo es O(n) para leer e
imprimir.

En el ejemplo el orden B, ABP, A necesita tres vertidos: un tramo por
zumo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2071_bitmask_dp.cpp](2071_bitmask_dp.cpp) | G++ 13.2 x64 | bitmask, dp | O(n) | AC | 0.078 s | 440 KB |
| [2071_bitmask_dp.go](2071_bitmask_dp.go) | Go 1.14 x64 | bitmask, dp | O(n) | AC | 0.046 s | 7572 KB |
| [2071_bitmask_dp.java](2071_bitmask_dp.java) | Java 1.8 | bitmask, dp | O(n) | AC | 0.125 s | 8848 KB |
| [2071_bitmask_dp.py](2071_bitmask_dp.py) | Python 3.12 x64 | bitmask, dp | O(n) | AC | 0.140 s | 17408 KB |
| [2071_bitmask_dp.rs](2071_bitmask_dp.rs) | Rust 1.75 x64 | bitmask, dp | O(n) | AC | 0.062 s | 7116 KB |
