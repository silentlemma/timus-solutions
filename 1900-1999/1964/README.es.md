# 1964. Intersección común mínima

[Timus 1964](https://acm.timus.ru/problem.aspx?space=1&num=1964) · difficulty 172 · math

Original problem from Open Ural FU Personal Contest 2013 | by Alexander Ipatov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un universo contiene n elementos distintos y hay k subconjuntos. Solo
se conoce una cota inferior a_i para el tamaño del subconjunto i:
contiene al menos a_i elementos. Hallar el menor número posible de
elementos presentes en todos los k subconjuntos. Los solapamientos son
arbitrarios. Límites: 1 segundo, 64 MB.

## Entrada

Primera línea n,k, con 1≤n≤10⁹ y 2≤k≤20. La segunda da k enteros a_i,
cada uno entre 1 y n, ambos inclusive.

## Salida

Un entero: tamaño mínimo de la intersección de los k conjuntos.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
1000000000 2
800000000 800000000
```

```
600000000
```

```
1000000000 2
500000000 500000000
```

```
0
```

## Solución

En el primer ejemplo cada conjunto puede omitir como máximo 200 000 000
elementos. Incluso con omisiones disjuntas solo se cubren 400 000 000 de
los mil millones: los 600 000 000 restantes son comunes. Las omisiones
disjuntas alcanzan esa cota. En el segundo, los conjuntos pueden ser
mitades distintas del universo y no tener ningún elemento común.

Usar los complementos. Sea b_i=n−a_i: como máximo b_i elementos pueden
faltar del conjunto i. Un elemento está fuera de la intersección si falta
en algún conjunto. La unión de los complementos tiene tamaño a lo sumo
min(n,Σb_i), por lo que la intersección tiene tamaño al menos

max(0,n−Σb_i) = max(0,Σa_i−(k−1)n).

La cota se alcanza. Numerar cíclicamente los elementos 0,…,n−1 y dar
a cada complemento los siguientes b_i números consecutivos, volviendo
a cero al pasar n−1. Como b_i<n, cada complemento tiene exactamente
b_i elementos distintos y el conjunto original exactamente a_i. Estos
tamaños exactos satisfacen también las cotas inferiores.

Si Σb_i<n, los complementos son disjuntos y su unión tiene Σb_i
elementos. Si Σb_i≥n, el recorrido consecutivo visita los n elementos
y la unión es el universo. Se alcanza min(n,Σb_i) en ambos casos,
y por tanto la intersección alcanza la cota inferior.

No hace falta construir conjuntos en el programa: empezar con n,
restar cada n−a_i y reemplazar el resultado negativo por cero.

Tiempo `O(k)` y espacio `O(k)` en estas implementaciones, que guardan
los k valores de entrada. El acumulador usa `O(1)` espacio adicional.

Las cotas son inferiores, no probabilidades ni sucesos independientes.
No basta el conjunto más pequeño ni sumar intersecciones por pares.
Limitar a cero el resultado negativo. La respuesta es como máximo n,
pero las sumas intermedias pueden acercarse a 20·10⁹ y las restas caer
por debajo de −2³¹: usar enteros de 64 bits con signo. Si todos los
a_i=n, la respuesta es n.

## Notas por lenguaje

C++ usa int64_t, Go 1.14 int64, Java 8 long y Rust 1.75 i64. Rust no
debe usar un acumulador sin signo porque puede ser negativo. Python 3.12
usa enteros exactos. Todas las versiones leen las k cotas una sola vez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1964_math.cpp](1964_math.cpp) | G++ 13.2 x64 | math | O(k) | AC | 0.031 s | 408 KB |
| [1964_math.go](1964_math.go) | Go 1.14 x64 | math | O(k) | AC | 0.031 s | 1120 KB |
| [1964_math.java](1964_math.java) | Java 1.8 | math | O(k) | AC | 0.125 s | 1648 KB |
| [1964_math.py](1964_math.py) | Python 3.12 x64 | math | O(k) | AC | 0.078 s | 476 KB |
| [1964_math.rs](1964_math.rs) | Rust 1.75 x64 | math | O(k) | AC | 0.031 s | 236 KB |
