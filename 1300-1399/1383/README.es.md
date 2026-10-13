# 1383. Diseños de jardín

[Timus 1383](https://acm.timus.ru/problem.aspx?space=1&num=1383) · dificultad 8198 · geometry

Problema original de Andrew Rumyantsev, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 10 000 proyectos dan cada uno una lista de puntos de coordenadas
enteras de valor absoluto a lo sumo 1000, a lo sumo 200 000 puntos en total.
Dos proyectos son iguales si uno se convierte en el otro reordenando sus
puntos y aplicando una aplicación afín que conserva la orientación: una
matriz de determinante positivo y un desplazamiento. Hay que imprimir
las clases de proyectos iguales.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego cada proyecto: su longitud M y M líneas de coordenadas.

## Salida

El número de clases, luego cada clase como lista de números de
proyecto terminada en 0.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
5
1 2
0 0
6 0
0 4
2 7
5
1 2
3 9
0 1
2 3
9 2
5
-43 -37
-73 -47
-3 3
-23 -7
-3 63
3
0 0
1 0
0 1
3
0 0
1 0
3 0
3
10 3
3 7
5 2
3
6 1
6 5
6 7
```

Salida:

```
4
4 6 0
5 7 0
1 3 0
2 0
```

## Solución

Se da a cada proyecto una clave canónica, igual para dos proyectos justo
cuando son iguales, y se agrupan los proyectos por clave. Los puntos
repetidos cuentan, así que la clave describe la lista con sus
repeticiones. Para C++, Go, Java y Rust:

- Todos los puntos iguales: la clave es solo su número.
- Todos los puntos en una recta: una aplicación afín puede estirar la
  recta y darle la vuelta, así que los extremos se llevan a 0 y 1 y se
  enumeran ordenadas las posiciones de todos los puntos. Se lee también
  desde el otro extremo y se queda la lista menor.
- Si no, se usa la envolvente convexa estricta en sentido antihorario;
  una aplicación afín de determinante positivo la lleva a la envolvente
  de la imagen en el mismo orden. Cada vértice de la envolvente, con el
  siguiente y el anterior, define un sistema de referencia: la
  aplicación que lo lleva a (0, 0), el siguiente a (1, 0) y el anterior
  a (0, 1) tiene determinante positivo. En ese sistema todas las
  coordenadas son fracciones con el mismo denominador, el producto
  cruzado de las dos aristas. Divididas entre su mcd común quedan
  únicas, así que conjuntos de puntos iguales dan listas de enteros
  iguales. Primero se compara solo la envolvente en cada sistema. Luego,
  para los sistemas en que la envolvente parece menor, se enumeran
  ordenados todos los puntos y se queda la lista menor. Así se tienen en
  cuenta las simetrías de la envolvente.

Las clases se imprimen por el tamaño de sus proyectos y luego por su
primer proyecto, como en el ejemplo. `O(S log S + Σ h²)` para S puntos
y envolventes de h vértices.

Detalles a tener en cuenta:

- la equivalencia al reflejo requiere una simetría afín que invierte
  la orientación (pruebas 04 y 13);
- una recta puede leerse en cualquier sentido (prueba 03);
- los puntos repetidos importan (pruebas 02, 03 y 06);
- una envolvente cuadrada da cuatro sistemas de envolvente igual de
  pequeña; los puntos interiores y las repeticiones siguen importando
  (prueba 05 y prueba generada 2).

Las clases se compararon en 350 lotes aleatorios de proyectos pequeños y
sus imágenes por aplicaciones enteras aleatorias de ambos signos con una
búsqueda directa que intenta llevar un triángulo de un proyecto a cada
triángulo de otro. Las pruebas se juzgan con un verificador que acepta
las clases en cualquier orden.

## Notas por lenguaje

- Java guarda los puntos, los pares en el sistema de referencia y las
  claves en arreglos de números simples, con cada par empaquetado en un
  long para ordenar sin comparador: con un objeto por punto y claves
  envueltas excedía el límite de tiempo en la prueba 8 del juez, y ahora
  tarda 1,67 s de los 2 s.
- Python encuentra los sistemas de referencia sin probarlos todos.
  Escribe la envolvente como la sucesión cíclica de lo que una
  aplicación afín conserva de cada tres aristas consecutivas, sus tres
  productos vectoriales divididos entre su mcd, y toma la menor rotación
  de esa sucesión en tiempo lineal. Si todos los puntos son vértices de
  la envolvente, esa sucesión con las repeticiones ya es la clave; si
  no, solo se usan los sistemas en las rotaciones mínimas, los de una
  envolvente simétrica filtrados además por el centroide, y en ellos se
  listan los puntos. Corre en CPython; la versión anterior, que probaba
  todos los sistemas, excedía el límite de tiempo en la prueba 8 del
  juez incluso con PyPy. `O((r + 1) S log S)` para a lo sumo r sistemas
  restantes por proyecto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1383_geometry.cpp](1383_geometry.cpp) | G++ 13.2 x64 | geometry | O(S log S + Σh²) | AC | 1.109 s | 5216 KB |
| [1383_geometry.go](1383_geometry.go) | Go 1.14 x64 | geometry | O(S log S + Σh²) | AC | 1.640 s | 7884 KB |
| [1383_geometry.java](1383_geometry.java) | Java 1.8 | geometry | O(S log S + Σh²) | AC | 1.671 s | 7768 KB |
| [1383_geometry.py](1383_geometry.py) | Python 3.12 x64 | geometry | O((r + 1) S log S) | AC | 1.125 s | 38932 KB |
| [1383_geometry.rs](1383_geometry.rs) | Rust 1.75 x64 | geometry | O(S log S + Σh²) | AC | 0.703 s | 5672 KB |
