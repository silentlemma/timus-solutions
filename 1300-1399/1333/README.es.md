# 1333. Bombardeo con genios 2

[Timus 1333](https://acm.timus.ru/problem.aspx?space=1&num=1333) · dificultad 219 · geometry

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hasta 10 bombas caen sobre el cuadrado unidad 0 ≤ x, y ≤ 1. Cada una
alcanza un disco de centro (x, y) y radio r, todos entre 0 y 1. Hay que
imprimir la parte del cuadrado alcanzada por al menos una bomba, en
porcentaje, con un error de un punto como mucho.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas con x, y y r.

## Salida

El porcentaje del cuadrado alcanzado.

## Comprobación

Imprimir porcentaje, no fracción. El enunciado pide un punto
porcentual; el verificador local usa
`|actual−expected|≤0.01·max(1,|expected|)` en esas unidades, separado de
la cota universal de cuadratura. Cada candidato pasó 12 entradas del
repositorio y 206 entradas completas extra en Docker, y obtuvo Accepted
propio de SHA exacto. El oráculo independiente acota todas las secciones
de cada celda con rectángulos adaptativos inferiores/superiores y usa
áreas analíticas de círculos enteros/medios/cuartos, sin reutilizar la
malla candidata. El máximo error frente a los extremos fue menor que
0,004001 puntos en ese conjunto; no es una garantía empírica universal.
Incluir vacío, radio cero, recortes, anidamientos, repeticiones, discos
casi tangentes, radios diminutos y ambos ejemplos.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
0.5 0.5 0.5
```

Salida:

```
78.539816
```

### Ejemplo 2

Entrada:

```
2
0.2 0.2 0.5
0.8 0.8 0.5
```

Salida:

```
80.74292
```

## Solución

Para x fijo, el disco `(cx,cy,r)` aporta el intervalo vertical
`cy±sqrt(r²−(x−cx)²)` si `|x−cx|<r`, recortado a `[0,1]`. Ordenarlos por
su extremo inferior y añadir solo la parte más allá del mayor extremo
ya cubierto calcula su unión f(x), contando solapes/repeticiones una
vez. Radio cero no aporta área. La respuesta es `100∫₀¹ f(x)dx`.
Las cinco bases usan S=20000 franjas y puntos medios:
`area≈Σ f((k+1/2)/S)/S`. Tiempo `O(SN log N)`, espacio O(N) más entrada
y salida. Se conservan exactamente los bytes de las cinco fuentes.

Hay una cota determinista. El intervalo de un disco crece por inclusión
hasta su centro y luego decrece; su variación de diferencia simétrica
suma como máximo 4r. Recortar no la aumenta. El cambio de una unión
está contenido en la unión de los cambios individuales: variación total
de f como máximo `4Σr`. En una franja de ancho h, el error integral del
punto medio es como máximo h/2 por la variación local, pues cada cambio
izquierdo/derecho afecta como máximo media franja. Sumando,
`|area−midpoint|≤2Σr/S`. Con N≤10,r≤1,S=20000, la cota en aritmética real
es 0,1 puntos porcentuales, dentro del punto permitido.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1333_geometry_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones optimizadas

`1333_geometry_optimized.rs`. Conserva 20.000 franjas de punto medio y misma aproximación por unión de intervalos recortados. Cachea radios cuadrados, usa arrays fijos para diez bombas/intervalos e inserción ordenada, sin vectores ni cuadrados repetidos. O(S(1+B²)+I) para S franjas, B<=10 e input I; inserción no mejora asintóticamente la ordenación base. O(B+T) espacio con token numérico máximo T. Salida C conserva seis decimales y la misma malla.

Frente a `1333_geometry.rs`: tiempo 0.046 s → 0.031 s; memoria 268 KB → 132 KB.

El mismo algoritmo usa S=4096: cota
`100·20/4096=0,48828125` puntos porcentuales, menor que 1. Cubre recortes,
solapes, discos estrechos y tangencias; un buen muestreo aleatorio no
justificaría por sí solo reducir franjas. Imprimir seis decimales añade
como máximo 0,0000005 puntos de redondeo decimal. Usar double y comprobar
el radicando al cuadrado antes de la raíz; si no es positivo, no aporta.

Precalcular radios cuadrados. C++/Go/Java reutilizan arrays acotados y
ordenación por inserción sin objetos/reflexión por franja: `O(SN²)`
tiempo, O(N) espacio. Python conserva ordenación, `O(SN log N)` tiempo,
O(N) espacio. Es mejora de implementación del mismo algoritmo y lleva
`_optimized`. C++ se admite por 39,3% menos memoria; 0,031→0,015s es un
tick, no evidencia fiable de velocidad. Go mejora 67,4% tiempo/81,2%
memoria, Java 50,3%/90,9%. Python ahorra 30,1% de tiempo (0,156→0,109s)
pero usa 11,9% MÁS memoria (504→564KB); se admite solo por tiempo y queda
con asterisco. Rust mantiene el tiempo y solo reduce 1,5% memoria
(268→264KB), por lo que no se añade; su base ya cubre formalmente una
muestra vacía de rivales.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1333_geometry.cpp](1333_geometry.cpp) | G++ 13.2 x64 | geometry | O(SN log N), S=20000 | AC | 0.031 s | 224 KB | 11285016 |
| [1333_geometry.go](1333_geometry.go) | Go 1.14 x64 | geometry | O(SN log N), S=20000 | AC | 0.046 s | 5944 KB | 11285017 |
| [1333_geometry.java](1333_geometry.java) | Java 1.8 | geometry | O(SN log N), S=20000 | AC | 0.187 s | 6560 KB | 11285019 |
| [1333_geometry.py](1333_geometry.py) | Python 3.12 x64 | geometry | O(SN log N), S=20000 | AC | 0.156 s | 504 KB | 11285018 |
| [1333_geometry.rs](1333_geometry.rs) | Rust 1.75 x64 | geometry | O(SN log N), S=20000 | AC | 0.046 s | 268 KB | 11285021 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1333_geometry_optimized.cpp](1333_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(SN^2), S=4096 | AC | 0.015 s | 136 KB | 11308499 |
| [1333_geometry_optimized.go](1333_geometry_optimized.go) | Go 1.14 x64 | geometry | O(SN^2), S=4096 | AC | 0.015 s | 1116 KB | 11308504 |
| [1333_geometry_optimized.java](1333_geometry_optimized.java) | Java 1.8 | geometry | O(SN^2), S=4096 | AC | 0.093 s | 600 KB | 11308510 |
| [1333_geometry_optimized.py](1333_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(SN log N), S=4096 | AC | 0.109 s | 564 KB | 11308516 |
| [1333_geometry_optimized.rs](1333_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(S(1+B²)+I) time; O(B+T) space | AC | 0.031 s | 132 KB | 11325547 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
