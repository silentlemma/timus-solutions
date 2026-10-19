# 2074. Agrupar problemas por las rutas de sus temas

[Timus 2074](https://acm.timus.ru/problem.aspx?space=1&num=2074) · dificultad 975 · implementation, sorting

Problema original de Mikhail Rubinchik.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un clasificador de temas es un árbol escrito como lista: cada encabezado
es un identificador como `2.2.1.` seguido del nombre del tema, y después
vienen una o más líneas con los números de los problemas de ese tema.
Para cada problema mencionado, imprimir los temas a los que pertenece,
cada uno descrito por los nombres de su camino desde la raíz unidos con
puntos. Los problemas con exactamente el mismo conjunto de temas se
imprimen en una línea. Los límites son 2 segundos y 256 MB.

## Entrada

El clasificador, como en el ejemplo. Hay a lo sumo 20 temas y a lo sumo
20 números de problema distintos, de 1000 a 9999. Un nombre de tema
tiene de 1 a 20 letras minúsculas y espacios simples. Los
identificadores siguen un orden en profundidad, así que un encabezado
con k números es hijo del último encabezado con k − 1 números.

## Salida

Líneas "números : temas": los problemas del grupo en orden creciente
separados por ", ", luego " : ", y después las descripciones de sus
temas en orden lexicográfico separadas por ", ". Las líneas mismas van
en orden lexicográfico.

## Ejemplos

### Ejemplo 1

Entrada:

```
1. graphs
1022
1065
2. geometry
1020
2.1. idea
1130
2.2. technique
1111 1065
1265
2.2.1. convex hull
1271
3. dynamic programming
1244
```

Salida:

```
1020 : geometry
1022 : graphs
1065 : geometry.technique, graphs
1111, 1265 : geometry.technique
1130 : geometry.idea
1244 : dynamic programming
1271 : geometry.technique.convex hull
```

## Solución

La entrada se lee línea a línea. Una línea cuya primera palabra termina
en punto es un encabezado; el número de puntos es su profundidad, así
que la pila de nombres se corta a depth − 1 elementos y se apila el
nombre nuevo. La descripción del tema actual es la pila unida con
puntos. Cualquier otra línea contiene números de problema, y a cada uno
se le añade la descripción actual a su conjunto. Un problema pertenece
solo a los temas que lo listan, no a sus ancestros: en el ejemplo 1065
está solo en graphs y geometry.technique.

Después el conjunto ordenado de cada problema se une en una clave, los
problemas con claves iguales se agrupan, y cada grupo da una línea con
sus números ordenados y la clave. Las líneas se ordenan como cadenas
normales, donde el espacio va antes del punto y el punto antes de las
letras. Con a lo sumo 20 temas y problemas el trabajo es mínimo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2074_implementation_sorting.cpp](2074_implementation_sorting.cpp) | G++ 13.2 x64 | implementation, sorting | O(1) | AC | 0.031 s | 808 KB |
| [2074_implementation_sorting.go](2074_implementation_sorting.go) | Go 1.14 x64 | implementation, sorting | O(1) | AC | 0.046 s | 1368 KB |
| [2074_implementation_sorting.java](2074_implementation_sorting.java) | Java 1.8 | implementation, sorting | O(1) | AC | 0.171 s | 4960 KB |
| [2074_implementation_sorting.py](2074_implementation_sorting.py) | Python 3.12 x64 | implementation, sorting | O(1) | AC | 0.109 s | 792 KB |
| [2074_implementation_sorting.rs](2074_implementation_sorting.rs) | Rust 1.75 x64 | implementation, sorting | O(1) | AC | 0.062 s | 796 KB |
