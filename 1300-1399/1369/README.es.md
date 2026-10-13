# 1369. Carrera de cucarachas

[Timus 1369](https://acm.timus.ru/problem.aspx?space=1&num=1369) · dificultad 11966 · geometry

Problema original de Den Raskovalov, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En el plano hay M cucarachas (M ≤ 100 000) y N dulces (N ≤ 10 000), con
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

«Más cercana» tiene una tolerancia que el enunciado no menciona: una
cucaracha cuenta si su distancia al cuadrado es menor que la mínima más
2⁻²⁴. Las coordenadas pueden tener más de 20 cifras tras el punto, así
que un double no distingue tales distancias. Por eso cada coordenada se
guarda también exacta, como entero: el decimal por 10³⁰, y toda
comparación final se hace con esos enteros.

Las cucarachas se unen en un grafo: la triangulación de Delaunay,
construida por divide y vencerás sobre quad-edges, más los vecinos de
cada cucaracha en el orden por x y en el orden por y. Las pruebas de
orientación y de círculo se calculan en double con una cota de su error
de redondeo, y se recalculan exactas cuando el resultado cae dentro de
esa cota. Si todas las cucarachas están en una recta, el grafo es el
camino a lo largo de ella.

Para un dulce, un recorrido empieza en la más cercana de 1 024
cucarachas repartidas en el orden por x (o en la respuesta anterior) y
pasa a un vecino más cercano mientras lo haya: primero en double, luego
exacto. Sobre una triangulación de Delaunay ese recorrido termina en la
cucaracha más cercana. Una búsqueda por el grafo desde ahí reúne todas
las cucarachas dentro de la tolerancia, pasando solo por ellas.
`O(M log M + N · W)` para recorridos de W pasos.

Detalles a tener en cuenta:

- la tolerancia 2⁻²⁴ en las distancias al cuadrado: la prueba 06 tiene
  distancias iguales dentro de ella y justo fuera;
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
- Python se ejecuta con PyPy y guarda cada coordenada exacta como dos
  mitades de 64 bits en arreglos, o como una sola palabra de máquina
  cuando los valores caben. Triangula con un barrido y no añade los
  vecinos por y, lo que no cambió ninguna respuesta en las pruebas de
  aquí. En la prueba 15 del juez tarda algo más de 2 s, así que se
  mantiene marcada TLE: pasa todas las pruebas de aquí, pero no se
  afirma que quepa en el tiempo en cada prueba del juez. Versiones
  anteriores usaban 70 MB en la prueba 9, o recorrían toda la
  envolvente tras cada giro de una de sus aristas, lo que es cuadrático
  en una circunferencia.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1369_geometry.cpp](1369_geometry.cpp) | G++ 13.2 x64 | geometry | O(M log M + N · W) | AC | 0.812 s | 33540 KB |
| [1369_geometry.go](1369_geometry.go) | Go 1.14 x64 | geometry | O(M log M + N · W) | AC | 1.328 s | 40448 KB |
| [1369_geometry.java](1369_geometry.java) | Java 1.8 | geometry | O(M log M + N · W) | AC | 1.781 s | 53152 KB |
| [1369_geometry.py](1369_geometry.py) | PyPy 3.10 x64 | geometry | O(M log M + N · W) | TLE (test 15) | 2.031 s | 29864 KB |
| [1369_geometry.rs](1369_geometry.rs) | Rust 1.75 x64 | geometry | O(M log M + N · W) | AC | 0.656 s | 39668 KB |
