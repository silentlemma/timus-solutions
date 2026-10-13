# 1369. Carrera de cucarachas

[Timus 1369](https://acm.timus.ru/problem.aspx?space=1&num=1369) · dificultad 10221 · geometry

Problema original de Den Raskovalov, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En el plano hay M cucarachas (1 ≤ M ≤ 100 000) y N dulces (0 ≤ N ≤ 10 000), con
coordenadas reales entre −10 000 y 10 000; dos cucarachas cualesquiera, y
dos dulces cualesquiera, están a 0,001 o más. Para cada dulce imprime los
números de las cucarachas más cercanas, en orden creciente.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

M y las cucarachas, luego N y los dulces, un punto por línea.

## Salida

N líneas, las cucarachas más cercanas a cada dulce.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
1 0
0 1
1 2
2
0 0
0 2
```

Salida:

```
1
3 4
```

## Solución

Las implementaciones usan una tolerancia que el enunciado no menciona:
una cucaracha cuenta si su distancia al cuadrado es menor que la mínima
más 2⁻²⁴. Las coordenadas pueden tener más de 20 cifras tras el punto,
y double puede perder distinciones cerca de este límite. Las comparaciones
exactas usan enteros escalados por 10³⁰, truncando después de 30 decimales.

C++, Go, Java y Rust unen las cucarachas en un grafo: la triangulación de
Delaunay, construida por divide y vencerás sobre quad-edges, más los vecinos de
cada cucaracha en el orden por x y en el orden por y. Las pruebas de
orientación y de círculo se calculan en double con una cota de su error
de redondeo, y se recalculan exactas cuando el resultado cae dentro de
esa cota. Si todas las cucarachas están en una recta, el grafo es el
camino a lo largo de ella.

Para un dulce, un recorrido empieza en la más cercana entre la respuesta
anterior y hasta 1 024 cucarachas repartidas en el orden por x, y
pasa a un vecino más cercano mientras lo haya: primero en double, luego
exacto. Sobre una triangulación de Delaunay ese recorrido termina en la
cucaracha más cercana. Una búsqueda por el grafo desde ahí reúne todas
las cucarachas dentro de la tolerancia, expandiendo solo esos vértices.
W cuenta los vértices y las entradas de las listas de adyacencia examinados,
y K las cucarachas indicadas por consulta (máximos entre consultas).

Detalles a tener en cuenta:

- la tolerancia 2⁻²⁴ en las distancias al cuadrado: la prueba 06 tiene
  diferencias de distancias al cuadrado menores y mayores que ella;
- puede haber doce cucarachas igual de cercanas (prueba 04);
- cucarachas en una recta degeneran la triangulación (prueba 05);
- N puede ser 0 (prueba 03).

Las respuestas coinciden con una fuerza bruta exacta en todas las pruebas
pequeñas y en muestras de las grandes. Una implementación independiente
aceptada coincide en todo salvo cinco líneas de las pruebas generadas de
anillos y circunferencia, donde la fuerza bruta da la razón a las
soluciones de aquí.

## Notas por lenguaje

- C++ y Rust guardan las coordenadas en enteros de 128 bits y los
  productos en un entero de 512 bits de dieciséis dígitos de 32 bits. Go
  también guarda las coordenadas en 128 bits y las amplía solo para los
  pasos exactos, con arreglos de aristas de 32 bits: una primera versión
  con coordenadas de 512 bits usó 88 MB en la prueba 9 del juez.
- Java compara primero las distancias en double y de forma exacta solo
  cuando la diferencia cae dentro del error de redondeo, y multiplica
  solo los dígitos usados: sin eso tardaba más de 2 s en la prueba 9 del
  juez.
- Python se ejecuta con PyPy y no construye la triangulación: busca las
  cucarachas más cercanas en un árbol k-d de cajas envolventes guardado
  en arreglos planos, girado según el eje principal de una nube
  alargada. Cuando las cucarachas están cerca de una circunferencia, se
  ordenan por ángulo, y un nodo se acota con su intervalo angular y su
  menor distancia al centro; también se pueden recorrer directamente
  ventanas angulares estrechas o toda la circunferencia. Los double
  deciden todo salvo los posibles empates, que se comparan de forma exacta. Versiones anteriores con
  triangulación tardaban algo más de 2 s en la prueba 15 del juez o
  usaban 70 MB en la prueba 9. V cuenta los nodos del árbol y puntos
  examinados por consulta (máximo entre consultas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1369_geometry.cpp](1369_geometry.cpp) | G++ 13.2 x64 | geometry | O(M log M + N · (W + K log K)) | AC | 0.812 s | 33540 KB |
| [1369_geometry.go](1369_geometry.go) | Go 1.14 x64 | geometry | O(M log M + N · (W + K log K)) | AC | 1.328 s | 40448 KB |
| [1369_geometry.java](1369_geometry.java) | Java 1.8 | geometry | O(M log M + N · (W + K log K)) | AC | 1.781 s | 53152 KB |
| [1369_geometry.py](1369_geometry.py) | PyPy 3.10 x64 | geometry | O(M log² M + N · (log M + V + K log K)) | AC | 1.687 s | 46264 KB |
| [1369_geometry.rs](1369_geometry.rs) | Rust 1.75 x64 | geometry | O(M log M + N · (W + K log K)) | AC | 0.656 s | 39668 KB |
