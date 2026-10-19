# 1932. Parejas según la distancia entre cuatro dígitos

[Timus 1932](https://acm.timus.ru/problem.aspx?space=1&num=1932) · difficulty 963 · combinatorics

Original problem from Open Ural FU Championship 2012 | by Victor Vinogradov (prepared by Egor Shchelkonogov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados identificadores hexadecimales distintos de cuatro caracteres,
contar parejas sin orden que difieran exactamente en una, dos, tres
y cuatro posiciones. Los ceros iniciales ocupan posiciones reales.
Límites: 1 segundo, 64 MB.

## Entrada

Primero n, 2≤n≤65536, seguido de n cadenas distintas de longitud cuatro.
Símbolos 0..9 y letras minúsculas a..f. El identificador 0000 es válido.

## Salida

Cuatro enteros, por cantidad creciente de posiciones diferentes.
Cada pareja sin orden pertenece exactamente a una de las cuatro clases.

## Evaluación

Comparación exacta de cuatro tokens enteros.

## Ejemplos

```
3
dead
beef
f00d
```

```
0 0 2 1
```

## Solución

Para k=1,2,3, sea S_k la suma de cantidades de parejas que coinciden
en cada subconjunto elegido de k posiciones. Cuenta con multiplicidad:
una pareja con r posiciones iguales aporta C(r,k), una por subconjunto
válido. No hay coincidencia en las cuatro posiciones porque las cadenas
son distintas. Si d_j cuenta parejas con j diferencias, entonces
S_3=d_1, S_2=3d_1+d_2 y S_1=3d_1+2d_2+d_3. Se obtiene
d_1=S_3, d_2=S_2−3d_1, d_3=S_1−3d_1−2d_2, y finalmente
d_4=n(n−1)/2−d_1−d_2−d_3. Estas identidades prueban la inversión.

Calcular las estadísticas en línea. Cada subconjunto de posiciones
tiene una tabla de frecuencias de dígitos proyectados. Al llegar un
identificador, sumar la frecuencia anterior de su clave al S_k pertinente
y después incrementarla. Cada pareja coincidente se cuenta una vez,
al llegar su elemento posterior, produciendo las estadísticas exactas.

Usar cuatro tablas de tamaño 16 para posiciones sueltas, seis de tamaño 256
para parejas y cuatro de tamaño 4096 para tríos: 17 984 contadores.
Las tablas separadas distinguen subconjuntos diferentes. Interpretar el
identificador como entero, pero extraer siempre cuatro grupos de cuatro
bits; así se conservan las posiciones de ceros iniciales. Empaquetar
los dígitos seleccionados en el orden original.

O(14n+17984) tiempo y 17 984 frecuencias más entrada almacenada. Con
cuatro dígitos y alfabeto 16 fijos: O(n) tiempo, O(1) espacio de frecuencias
de trabajo y O(n) espacio total con los búferes de estos programas.

Son diferencias de dígitos, no de bits: 0000 y 000f difieren en una posición.
No compartir tablas entre subconjuntos diferentes. S_k lleva multiplicidad
binomial, no cuenta simplemente parejas con al menos k coincidencias.
La unicidad es necesaria para S_3=d_1. Sumar la frecuencia anterior antes
de incrementarla. Ordenar las respuestas por distancias 1,2,3,4 y conservar
la anchura fija al interpretar ceros iniciales.

## Notas por lenguaje

Usar totales con signo de 64 bits y promover ANTES de n(n−1). Para
n=65536, el producto 4 294 901 760 supera 32 bits antes de dividir;
el total de parejas es 2 147 450 880. Contadores de frecuencia de 32 bits
bastan: máximos 4096,256,16 para una, dos y tres posiciones. C++, Go,
Java y Rust usan acumuladores anchos; Python enteros exactos. Java
lee cantidad decimal y códigos hexadecimales con búfer. C++ cambia
solo la entrada a hexadecimal después de leer n; la salida sigue decimal.
Python utiliza CPython.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1932_combinatorics.cpp](1932_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.046 s | 720 KB |
| [1932_combinatorics.go](1932_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.046 s | 3184 KB |
| [1932_combinatorics.java](1932_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.140 s | 4948 KB |
| [1932_combinatorics.py](1932_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.359 s | 4844 KB |
| [1932_combinatorics.rs](1932_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.046 s | 1332 KB |
