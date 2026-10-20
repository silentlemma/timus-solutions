# 2180. Sumar a un subárbol hasta una profundidad y leer un vértice

[Timus 2180](https://acm.timus.ru/problem.aspx?space=1&num=2180) · dificultad 1297 · fenwick

Problema original de Vladimir Cherepanov, del Concurso Escolar de Programación de los Urales 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un árbol con raíz 1 tiene N vértices. Una actualización "+ v k x" suma x
a v y a cada descendiente como mucho k niveles por debajo, y una
consulta "? v" pide el total sumado a v hasta el momento. Los límites
son 2 segundos y 256 MB.

## Entrada

N, 2 ≤ N ≤ 10⁵, luego los padres p₂ … p_N con pᵢ < i, luego Q,
1 ≤ Q ≤ 10⁵, y Q líneas "+ v k x" con 0 ≤ k ≤ N, 1 ≤ x ≤ 10⁹, o "? v".

## Salida

La respuesta a cada consulta.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1 1 2
6
? 3
+ 1 1 5
? 2
+ 2 1 9
? 4
? 2
```

Salida:

```
0
5
9
14
```

## Solución

Con un recorrido de Euler, el subárbol de v es un intervalo de tiempos
de entrada, y la actualización llega exactamente a los vértices u de ese
intervalo con depth(u) ≤ depth(v) + k. Una consulta en u suma, por
tanto, las actualizaciones cuyo intervalo contiene entry(u) y cuyo
límite de profundidad es al menos depth(u), una pregunta bidimensional
que se responde en línea.

El Fenwick exterior recorre los tiempos de entrada y guarda cada
actualización como +x al inicio del intervalo y −x tras su final, así
que una suma de prefijo hasta entry(u) conserva justo los intervalos que
contienen u. Cada nodo exterior tiene un Fenwick interior para la
condición de profundidad. C++, Go, Java y Rust conservan todos los
vértices y comprimen los límites de profundidad de las actualizaciones
parciales en cada nodo exterior visitado al actualizar un extremo.
Una actualización suma en su límite y una consulta suma todos los
límites desde depth(u) hacia arriba, usando índices en orden inverso.

Python conserva solo los vértices consultados al menos una vez y
transforma cada subárbol en un intervalo de los tiempos de entrada
retenidos. Sus árboles interiores comprimen las profundidades de las
consultas en cada nodo exterior visitado por una consulta de prefijo.
Una actualización suma a todas las profundidades guardadas que no
superan su límite, y una consulta lee su propia profundidad mediante
un Fenwick con recorrido inverso. Ambas variantes leen todas las
operaciones para preparar las coordenadas y luego las procesan en
orden de entrada. La memoria total es O(N + Q log N).

Dos casos evitan los árboles interiores en todas las implementaciones:
k = 0 solo toca v y va a un arreglo simple; un límite que alcanza el
vértice más profundo del subárbol no necesita prueba de profundidad y
va a un Fenwick exterior ordinario.

Una trampa es usar las etiquetas como intervalos de subárboles: pueden
estar intercaladas (prueba 06), por lo que hacen falta los tiempos de
entrada de Euler. El límite de profundidad es inclusivo: también se
suma a los vértices exactamente k niveles por debajo de v (prueba 09).

En el ejemplo la primera actualización llega a 1, 2 y 3 con 5, y la
segunda a 2 y 4 con 9, así que el vértice 2 tiene 14.

Cada operación cuesta O(log² N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2180_fenwick.cpp](2180_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((N + Q) log² N) | AC | 0.609 s | 35640 KB |
| [2180_fenwick.go](2180_fenwick.go) | Go 1.14 x64 | fenwick | O((N + Q) log² N) | AC | 1.250 s | 60432 KB |
| [2180_fenwick.java](2180_fenwick.java) | Java 1.8 | fenwick | O((N + Q) log² N) | AC | 1.015 s | 53608 KB |
| [2180_fenwick.py](2180_fenwick.py) | PyPy 3.10 x64 | fenwick | O((N + Q) log² N) | AC | 0.843 s | 65728 KB |
| [2180_fenwick.rs](2180_fenwick.rs) | Rust 1.75 x64 | fenwick | O((N + Q) log² N) | AC | 0.687 s | 54696 KB |
