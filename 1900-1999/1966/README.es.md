# 1966. Conectividad por segmentos que se cruzan

[Timus 1966](https://acm.timus.ru/problem.aspx?space=1&num=1966) · difficulty 682 · dsu, geometry

Problema original del Concurso Individual Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n puntos marcados y m segmentos rectos cerrados que unen pares de
ellos. Se permite recorrer cada segmento en ambos sentidos y cambiar
de segmento en cualquier punto común, aunque no esté marcado. También
se puede visitar una marca interior a un segmento. Determinar si todas
las marcas son alcanzables desde la marca inicial. No hace falta su
índice: equivale a que todas pertenezcan a una red geométrica conexa.
Límites: 1 segundo, 64 MB.

## Entrada

n,m con 1≤m<n≤200. Después n pares enteros distintos x,y, cada coordenada
de valor absoluto como máximo 30 000. Las m líneas siguientes contienen
dos índices distintos entre 1 y n, los extremos de cada segmento. Se
permiten segmentos repetidos y extremos en orden inverso.

## Salida

`YES` si todas las marcas son alcanzables por los segmentos; si no, `NO`.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
4 2
0 0
1 0
1 1
0 1
1 3
4 2
```

```
YES
```

```
4 3
0 0
1 0
1 1
0 1
1 2
2 1
3 4
```

```
NO
```

```
3 2
0 0
1 0
1 1
1 3
3 2
```

```
YES
```

## Solución

En el primer ejemplo las diagonales del cuadrado se cruzan en el centro,
permitiendo llegar a los cuatro extremos aunque el grafo de extremos
tenga dos componentes. En el segundo se repite el primer segmento al
revés; no une los lados inferior y superior, por lo que resulta NO. En
el tercero dos segmentos forman una cadena por un extremo común y se
alcanzan las tres marcas.

Mantener una estructura de conjuntos disjuntos sobre las n marcas.
Unir los extremos de cada segmento. Por cada par de segmentos cerrados
que se intersecten, unir un extremo de uno con un extremo del otro.
Por cada marca contenida en un segmento, unirla con un extremo de este.
Devolver YES exactamente cuando todas las marcas tengan el mismo representante.

Cada unión corresponde a un recorrido real: por un segmento, cambiando
en un punto común o desde una marca interior a un extremo. A la inversa,
todo recorrido permitido sigue una secuencia de segmentos y cambia solo
en intersecciones. Los extremos de cada segmento ya están unidos, todo
cambio posible está representado y las marcas interiores están añadidas.
Así se representa toda conexión geométrica. Una marca fuera de todos
los segmentos queda aislada, como debe ser. Esto prueba el criterio.

Usar predicados enteros exactos. Definir
cross(a,b,c)=(b_x−a_x)(c_y−a_y)−(b_y−a_y)(c_x−a_x).
Un punto pertenece al segmento cerrado si este valor es cero y ambas
coordenadas están en los intervalos inclusivos de sus extremos.

Dos segmentos cerrados se cortan si sus intervalos de x e y se solapan
y los extremos de cada uno están a lados opuestos de la recta del otro,
permitiendo cero. La caja descarta segmentos colineales separados; los
signos no estrictos incluyen extremos comunes, uniones en T y solapamientos.

Tiempo `O((nm+m²)·α(n))` y espacio `O(n+m)` con compresión de caminos
y unión por tamaño. Hay nm pruebas punto/segmento y m(m−1)/2 pares de
segmentos. α es la función inversa de Ackermann de los conjuntos disjuntos.

Un grafo solo de extremos omite cruces y marcas interiores. Ni m=n−1
garantiza conexión, especialmente con duplicados. Los contactos cuentan,
pero colinealidad no implica solapamiento. Usar coordenadas de 64 bits
con signo antes de multiplicar: un producto vectorial puede superar
32 bits. No multiplicar dos productos vectoriales ni siquiera en 64 bits:
magnitudes de 3,6·10⁹ dan 1,296·10¹⁹, fuera de rango. Comparar signos
directamente; no hace falta epsilon.

## Notas por lenguaje

C++ usa int64_t, Go 1.14 int64, Java 8 long y Rust 1.75 i64 en geometría.
Python 3.12 usa enteros exactos. Todos comparan signos directamente,
comprimen caminos iterativamente y unen por tamaño de componente. No
hacen falta recursión, construcción de un grafo plano ni flotantes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1966_dsu_geometry.cpp](1966_dsu_geometry.cpp) | G++ 13.2 x64 | dsu, geometry | O((n*m+m*m)*alpha(n)) | AC | 0.015 s | 412 KB |
| [1966_dsu_geometry.go](1966_dsu_geometry.go) | Go 1.14 x64 | dsu, geometry | O((n*m+m*m)*alpha(n)) | AC | 0.031 s | 1116 KB |
| [1966_dsu_geometry.java](1966_dsu_geometry.java) | Java 1.8 | dsu, geometry | O((n*m+m*m)*alpha(n)) | AC | 0.140 s | 2260 KB |
| [1966_dsu_geometry.py](1966_dsu_geometry.py) | Python 3.12 x64 | dsu, geometry | O((n*m+m*m)*alpha(n)) | AC | 0.140 s | 784 KB |
| [1966_dsu_geometry.rs](1966_dsu_geometry.rs) | Rust 1.75 x64 | dsu, geometry | O((n*m+m*m)*alpha(n)) | AC | 0.046 s | 224 KB |
