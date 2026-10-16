# 1757. Lingotes de oro

[Timus 1757](https://acm.timus.ru/problem.aspx?space=1&num=1757) · dificultad 2312 · binary_search

Problema original de Vassily Burnin, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n lingotes; el lingote i pesa mᵢ gramos y tiene ley pᵢ, los gramos
de oro por kilogramo de aleación. Se puede tomar cualquier parte de
cualquier lingote. Fundir un lingote de m gramos y ley p, o informar de
que no se puede.

## Entrada

n, m y p (1 ≤ n ≤ 1000, 1 ≤ m ≤ 10⁶, 0 ≤ p ≤ 1000) y luego mᵢ y pᵢ de
cada lingote (1 ≤ mᵢ ≤ 1000, 0 ≤ pᵢ ≤ 1000).

## Salida

`NO`, o `YES` y los gramos xᵢ tomados de cada lingote, con
|Σxᵢ − m| < 10⁻⁶ y |Σxᵢpᵢ/1000 − mp/1000| < 10⁻⁶. Se acepta cualquier
elección válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 150 750
100 1000
150 585
100 750
100 0
```

Salida:

```
YES
75.000000000
0.000000000
50.000000000
25.000000000
```

### Ejemplo 2

Entrada:

```
1 100 1000
200 0
```

Salida:

```
NO
```

## Solución

Se colocan los lingotes en fila del más pobre al más rico, M gramos en
total, y se mira una ventana de m gramos que empieza en s. Su contenido
de oro G(s), en miligramos, nunca baja al mover s a la derecha, pues la
ventana suelta metal más
pobre y recoge más rico, y cambia de forma continua. Cualquier elección
de m gramos tiene al menos tanto oro como la ventana en s = 0 y a lo
sumo tanto como la ventana en s = M − m. Así que el lingote se puede
fundir justo cuando M ≥ m y G(0) ≤ m·p ≤ G(M − m), ambos extremos
calculados exactamente.

En ese caso una búsqueda binaria sobre s encuentra dónde G(s) = m·p, y
las partes son las intersecciones de la ventana con los lingotes:
lingotes enteros dentro y a lo sumo dos cortados en los extremos. G(s)
recorre los lingotes, o busca en sumas prefijas en Python. Con K = 100
mitades, el total es `O(n log n + K·n)`, `O(n log n + K log n)` en
Python, u `O(n log² n + K·n)` en Go por su ordenación estable.
Tener pocos lingotes cortados mantiene además el redondeo de las partes
impresas muy por debajo de 10⁻⁶.

En el primer ejemplo los lingotes en orden tienen ley 0, 585, 750 y
1000. La ventana en s = 0 tiene 100 gramos de ley 0 y 50 de ley 585,
29,25 gramos de oro; en el extremo opuesto tiene 50 de ley 750 y 100 de
ley 1000, 137,5. El encargo necesita 112,5, así que la ventana se
detiene en medio: unos 30,12 gramos del lingote de 585, todo el de 750
y unos 19,88 del de 1000. Es otra respuesta válida distinta de la del
ejemplo.

Trampas:

- un encargo más pesado que todo el almacén es imposible con cualquier
  ley;
- la decisión de sí o no exige extremos exactos: G(0) y G(M − m)
  son sumas enteras representables exactamente en double;
- mezclar muchos lingotes en fracciones puede dar decimales largos;
  1000 partes redondeadas a diez decimales suman como mucho 5·10⁻⁸ de
  error de redondeo.

Las respuestas coinciden con una implementación aceptada independiente
en qué encargos son posibles, en 500 almacenes aleatorios, muchos con
la ley justo en el límite o un poco más allá, y cada respuesta pasa un
verificador de las dos condiciones y de los pesos de los lingotes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1757_binary_search.cpp](1757_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n log n + K n), K = 100 | AC | 0.015 s | 228 KB |
| [1757_binary_search.go](1757_binary_search.go) | Go 1.14 x64 | binary_search | O(n log² n + K n), K = 100 | AC | 0.031 s | 1196 KB |
| [1757_binary_search.java](1757_binary_search.java) | Java 1.8 | binary_search | O(n log n + K n), K = 100 | AC | 0.171 s | 3280 KB |
| [1757_binary_search.py](1757_binary_search.py) | Python 3.12 x64 | binary_search | O(n log n + K log n), K = 100 | AC | 0.078 s | 684 KB |
| [1757_binary_search.rs](1757_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n log n + K n), K = 100 | AC | 0.046 s | 268 KB |
