# 2133. Contar tramos de edificios altos con cambios de altura

[Timus 2133](https://acm.timus.ru/problem.aspx?space=1&num=2133) · dificultad 2053 · fenwick

Problema original de Nikita Sivukhin, del concurso «Más vale tarde que nunca».

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n edificios en fila. Las consultas cambian la altura de un edificio
o piden, para un nivel x, el número de tramos máximos de edificios
consecutivos de al menos x pisos. Los límites son 3 segundos y 256 MB.

## Entrada

n, 1 ≤ n ≤ 10⁵, las alturas, y luego q, 1 ≤ q ≤ 10⁵, y las consultas
"1 i x" (la altura del edificio i pasa a ser x) y "2 x", con todas las
alturas y niveles entre 1 y 10⁹.

## Salida

El número de tramos de cada consulta del segundo tipo.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
3 6 5 2 6 1 4
6
2 3
1 6 4
2 3
2 5
1 4 10
2 5
```

Salida:

```
3
2
2
1
```

## Solución

En un nivel x los edificios de altura al menos x forman tramos, y cada
par de vecinos que son ambos lo bastante altos une dos de ellos. Así que
el número de tramos es el número de edificios con h ≥ x menos el número
de pares vecinos con min(hᵢ, hᵢ₊₁) ≥ x.

Primero se leen todas las consultas y se comprimen todas las alturas y
niveles que aparecen. Un árbol de Fenwick sobre los valores comprimidos
guarda +1 en la altura de cada edificio y −1 en el mínimo de cada par
vecino; la respuesta para x es la suma de todos los valores desde x
hacia arriba. Cambiar una altura mueve el +1 del edificio y el −1 de sus
a lo sumo dos pares, un número constante de actualizaciones. Todo cuesta
O((n + q) log(n + q)).

En el ejemplo, en el nivel 3 los edificios 3 6 5 | 2 | 6 | 1 | 4 forman
tres tramos: 3 6 5, 6 y 4.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2133_fenwick.cpp](2133_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((n + q) log(n + q)) | AC | 0.109 s | 3292 KB |
| [2133_fenwick.go](2133_fenwick.go) | Go 1.14 x64 | fenwick | O((n + q) log(n + q)) | AC | 0.156 s | 18028 KB |
| [2133_fenwick.java](2133_fenwick.java) | Java 1.8 | fenwick | O((n + q) log(n + q)) | AC | 0.171 s | 6748 KB |
| [2133_fenwick.py](2133_fenwick.py) | Python 3.12 x64 | fenwick | O((n + q) log(n + q)) | AC | 1.843 s | 65740 KB |
| [2133_fenwick.rs](2133_fenwick.rs) | Rust 1.75 x64 | fenwick | O((n + q) log(n + q)) | AC | 0.078 s | 10488 KB |
