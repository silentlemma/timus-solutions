# 1663. El hobbit, o Historia de una ida y de una vuelta 2

[Timus 1663](https://acm.timus.ru/problem.aspx?space=1&num=1663) · dificultad 3186 · dp

Problema original de Alexander Ipatov, del Ural SU Contest en el campus de invierno de Petrozavodsk, enero de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un viaje sale de la ciudad 1, pasa exactamente una vez por cada una de
las N ciudades y vuelve a la ciudad 1. Entrar en la ciudad A desde la
ciudad B cuesta P_A · ⌊1000 / P_B⌋, donde P es la población. Hay que
imprimir una ruta de coste mínimo, empezando en la ciudad 1; vale
cualquiera de coste mínimo.

## Entrada

N (2 ≤ N ≤ 1000) y luego las poblaciones P₁ … P_N (1 ≤ Pᵢ ≤ 1000).

## Salida

Las N ciudades en el orden de la ruta.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
10 3 5 4
```

Salida:

```
1 4 2 3
```

## Solución

Sea q_B = ⌊1000 / P_B⌋, de modo que un paso de B a A cuesta q_B · P_A.
Se ordenan las ciudades por población: en ese orden P solo crece y q solo
decrece. Con costes de esta forma de producto, alguna ruta de coste
mínimo es piramidal: sube de la ciudad más pequeña a la más grande por
una sucesión creciente de ciudades y baja de vuelta por las demás.

Así que cada ciudad, en el orden ordenado, va al camino de subida o al de
bajada. Tras las primeras m ciudades, uno de los dos caminos acaba en la
ciudad m y solo importa el extremo j del otro. up[j] es el menor coste
cuando el camino de subida acaba en m, y down[j] cuando acaba el de
bajada. Añadir la ciudad m + 1 al camino que ya acaba en m mantiene j y
suma lo mismo a todas las entradas, así que se guarda como un
desplazamiento común por arreglo; añadirla al otro camino da la única
entrada nueva, para j = m, que es un mínimo sobre todos los j. La última
ciudad cierra ambos caminos. Cada paso recuerda qué j dio las entradas
nuevas, y recorriendo hacia atrás desde el mejor estado final se asigna
cada ciudad a un camino. `O(N²)`.

Detalles a tener en cuenta:

- la ruta debe empezar en la ciudad 1, que no tiene por qué ser la más
  pequeña, así que el ciclo hallado se rota;
- los peajes son divisiones enteras, así que muchas ciudades comparten
  el mismo q (prueba 06 y las ciudades grandes de gen4);
- con dos ciudades solo hay una ruta.

La forma piramidal se confirmó con una búsqueda exhaustiva de todas las
rutas en 400 entradas aleatorias de hasta 9 ciudades, y los costes de las
rutas coinciden con una implementación aceptada independiente en 60
entradas aleatorias de hasta 1000 ciudades. Un comprobador compara los
costes de las rutas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1663_dp.cpp](1663_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 268 KB |
| [1663_dp.go](1663_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.031 s | 1284 KB |
| [1663_dp.java](1663_dp.java) | Java 1.8 | dp | O(N^2) | AC | 0.156 s | 2872 KB |
| [1663_dp.py](1663_dp.py) | Python 3.12 x64 | dp | O(N^2) | AC | 0.281 s | 1332 KB |
| [1663_dp.rs](1663_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.046 s | 400 KB |
