# 1962. Asientos circulares con vecinos obligatorios

[Timus 1962](https://acm.timus.ru/problem.aspx?space=1&num=1962) · difficulty 797 · graphs

Original problem from Open Ural FU Personal Contest 2013 | author not listed on Timus.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sentar en círculo a n personas distintas, numeradas de 1 a n. La silla
de la persona 1 está fija. Para cada i entre 1 y m, k_i debe ocupar una
de las dos sillas vecinas de i. Contar las disposiciones módulo
1 000 000 007. Las rotaciones son iguales y los reflejos son distintos.
Con dos personas, ambos lados tienen el mismo vecino. Límites: 1 segundo,
64 MB.

## Entrada

n,m con 2≤n≤100 y 0≤m≤n; después m enteros k_i, uno por línea,
con 1≤k_i≤n y k_i≠i. Las personas que imponen requisitos son exactamente
el prefijo 1,…,m; no se reciben pares arbitrarios de etiquetas.

## Salida

Un entero: cantidad de disposiciones válidas con la primera silla fija,
módulo 1 000 000 007.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
6 6
2
1
1
5
6
5
```

```
4
```

```
4 3
2
3
1
```

```
0
```

## Solución

El primer ejemplo fuerza los caminos 2–1–3 y 4–5–6. Sus dos bloques
tienen un único orden circular y cada camino permite dos orientaciones:
1!·2²=4. El segundo exige un triángulo entre 1,2,3; no se puede insertar
a la persona 4 conservando todas sus adyacencias, de modo que resulta cero.

Convertir cada requisito en una arista no dirigida. Los requisitos mutuos
producen una sola arista. Si un vértice alcanza más de dos vecinos
distintos, devolver cero. En caso contrario, cada componente es un camino,
un vértice aislado o un ciclo. Recorrerla con una pila explícita, contando
vértices y suma de grados. Es un ciclo cuando la suma de grados es el
doble del número de vértices.

Un ciclo que no incluye a todas las personas impide la solución: sus
vértices ya necesitan ambos vecinos dentro del ciclo y no permiten unir
a nadie más. Si abarca los n vértices, quedan exactamente sus dos
orientaciones, con las rotaciones fijadas por la persona 1.

Sin ciclos, contraer cada camino, incluidos los vértices aislados, a un
bloque. Sean C el número de bloques y P el número de caminos de al menos
dos vértices. Hay (C−1)! órdenes circulares de los bloques distintos.
Cada camino no trivial permite dos orientaciones, cada aislado solo una;
la respuesta es (C−1)!·2^P módulo el valor indicado.

Para n≥3 existe una biyección. Las aristas de un camino obligan a que
sus personas ocupen sillas consecutivas, por lo que toda disposición
produce un orden circular de bloques orientados. Expandir cualquier orden
así satisface los requisitos. Tanto si la persona 1 es extremo, interior
o aislada, existe exactamente una rotación de la expansión que la coloca
en su silla fija. No se multiplica por la longitud de su bloque.

Tratar n=2 aparte: la única disposición siempre sirve, y las dos
orientaciones de su camino describen la misma disposición. Reducir
módulo después de cada multiplicación del factorial y de la potencia.

Tiempo `O(n+m)` y espacio `O(n+m)`. Antes de cada inserción válida las
listas de adyacencia tienen como máximo dos elementos, así que buscar
duplicados cuesta tiempo constante. Si surge grado tres, se termina.

Deduplicar los requisitos mutuos e incluir los aislados entre los bloques.
Un ciclo completo da dos, uno propio da cero. No dividir entre dos por
reflejos ni multiplicar por la longitud del bloque de la persona fija.
Sin requisitos hay (n−1)! posibilidades; un camino completo da dos para
n≥3. Marcar al introducir en la pila. Los productos modulares necesitan
64 bits: un paso del factorial puede superar el entero de 32 bits.

## Notas por lenguaje

C++ usa int64_t, Go 1.14 int64, Java 8 long y Rust 1.75 u64 en productos
modulares. Todos emplean listas de adyacencia y pila explícita. Python
3.12 usa enteros y pow modular, sin recursión.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1962_graphs.cpp](1962_graphs.cpp) | G++ 13.2 x64 | graphs | O(n+m) | AC | 0.015 s | 440 KB |
| [1962_graphs.go](1962_graphs.go) | Go 1.14 x64 | graphs | O(n+m) | AC | 0.031 s | 1088 KB |
| [1962_graphs.java](1962_graphs.java) | Java 1.8 | graphs | O(n+m) | AC | 0.125 s | 1724 KB |
| [1962_graphs.py](1962_graphs.py) | Python 3.12 x64 | graphs | O(n+m) | AC | 0.093 s | 656 KB |
| [1962_graphs.rs](1962_graphs.rs) | Rust 1.75 x64 | graphs | O(n+m) | AC | 0.046 s | 236 KB |
