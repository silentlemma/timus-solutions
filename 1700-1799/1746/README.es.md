# 1746. Hipertorre

[Timus 1746](https://acm.timus.ru/problem.aspx?space=1&num=1746) · dificultad 1630 · matrix

Problema original de Petr Lezhankin, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las celdas de una rejilla de n dimensiones tienen coordenadas enteras de
0 a m − 1. Una hipertorre se mueve de una celda a cualquier celda que
difiera exactamente en una coordenada. Para q celdas dadas, contar las
rutas de exactamente d movimientos entre cada dos de ellas, módulo p.

## Entrada

n, m, d, p y q (1 ≤ n ≤ 50, 2 ≤ m ≤ 10⁵, 0 ≤ d ≤ 10⁹,
1 ≤ p ≤ 10⁹, 2 ≤ q ≤ 50) y luego las q celdas.

## Salida

Una tabla q × q: el número de rutas de la celda i a la celda j, módulo
p.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 8 4 10000000 4
3 5
0 5
3 7
0 0
```

Salida:

```
896 720 720 560
720 896 560 720
720 560 896 560
560 720 560 896
```

### Ejemplo 2

Entrada:

```
3 3 4 10000000 3
0 2 2
1 1 1
1 2 2
```

Salida:

```
90 36 45
36 90 54
45 54 90
```

## Solución

Se fija la celda destino. De la celda actual solo importa h, el número
de coordenadas en que difiere del destino. Un movimiento desde h o bien
corrige una de esas h coordenadas (h formas, a h − 1), o bien la cambia
a otro valor erróneo (h(m − 2) formas, h se mantiene), o bien estropea
una de las n − h correctas ((n − h)(m − 1) formas, a h + 1). Estos
números forman una matriz (n + 1) × (n + 1), y su potencia d-ésima,
calculada por cuadrados repetidos módulo p, da en la fila h, columna 0,
el número de rutas desde una celda a distancia h hasta el destino. Cada
respuesta solo necesita el número de coordenadas en que difieren las
dos celdas. `O(n³ log d + q²n)`.

En el primer ejemplo las celdas 1 y 2 difieren en una coordenada y
tienen 720 rutas, las celdas 1 y 4 en dos y tienen 560.

Trampas:

- p no tiene por qué ser primo, así que la potencia de la matriz se
  calcula directamente, sin dividir;
- con p = 1 todo es 0, incluidas las rutas de longitud 0;
- los productos llegan a 10¹⁸ antes del resto, así que hace falta
  aritmética de 64 bits.

Las tablas coinciden con un conteo paso a paso sobre toda la rejilla en
150 casos pequeños aleatorios, y con una implementación aceptada
independiente en las pruebas grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1746_matrix.cpp](1746_matrix.cpp) | G++ 13.2 x64 | matrix | O(n³ log d + q²n) | AC | 0.062 s | 532 KB |
| [1746_matrix.go](1746_matrix.go) | Go 1.14 x64 | matrix | O(n³ log d + q²n) | AC | 0.078 s | 2228 KB |
| [1746_matrix.java](1746_matrix.java) | Java 1.8 | matrix | O(n³ log d + q²n) | AC | 0.218 s | 4628 KB |
| [1746_matrix.py](1746_matrix.py) | Python 3.12 x64 | matrix | O(n³ log d + q²n) | AC | 0.625 s | 1084 KB |
| [1746_matrix.rs](1746_matrix.rs) | Rust 1.75 x64 | matrix | O(n³ log d + q²n) | AC | 0.062 s | 332 KB |
