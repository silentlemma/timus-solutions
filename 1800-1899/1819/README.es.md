# 1819. Enfoque profesional

[Timus 1819](https://acm.timus.ru/problem.aspx?space=1&num=1819) · dificultad 6421 · graphs

Problema original del Tavrida NU Akai Contest, sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad tiene n cruces y k tramos de calle de doble sentido, sin dos
tramos entre el mismo par. Para cada una de q consultas (hotel, sede),
decir si hay tres caminos del hotel a la sede tales que ningún par de
ellos use el mismo tramo.

## Entrada

n y k (2 ≤ n ≤ 50000, 1 ≤ k ≤ 50000), luego k tramos como pares de
cruces distintos, luego q (1 ≤ q ≤ 50000) y q pares de cruces
distintos.

## Salida

Para cada consulta, "Yes" o "No" en su propia línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 9
1 2
1 5
1 4
1 6
2 3
3 4
3 5
4 5
4 6
9
1 2
1 3
1 5
2 4
5 6
3 6
3 4
2 6
2 3
```

Salida:

```
No
Yes
Yes
No
No
No
Yes
No
No
```

## Solución

Por el teorema de Menger la respuesta es "Yes" exactamente cuando los
dos cruces siguen conectados tras quitar cualquier conjunto de a lo
sumo dos tramos, así que la tarea es responder consultas de 3-conexidad
por aristas.

Se toma un bosque de búsqueda en profundidad. Cada tramo restante une
un cruce con uno de sus ancestros y cubre las aristas del árbol entre
ellos. Cada uno de esos tramos recibe un número aleatorio de 64 bits, y
la cobertura de una arista del árbol es el xor de los números de los
tramos que la cubren: marcar ambos extremos de cada tramo y acumular
xor hacia arriba da todas las coberturas en `O(n + k)`. El número de
tramos que cubren se acumula igual. Los cortes de a lo sumo dos tramos
son entonces:

- una arista del árbol sin cubrir, un puente;
- una arista del árbol cubierta por exactamente un tramo, junto con ese
  tramo;
- dos aristas del árbol con coberturas iguales.

Entre las aristas del árbol cubiertas al menos dos veces, las de igual
cobertura están en un mismo camino a la raíz y cortan el árbol en
trozos que los tramos que las cubren cierran en un anillo; dos cruces
quedan separados por un par así salvo que el camino entre ellos en el
árbol cruce todas las aristas de la clase o ninguna. Por eso cada
arista del árbol recibe un valor: uno aleatorio nuevo para puentes y
aristas cubiertas una vez, y para una clase de coberturas iguales
valores aleatorios con xor cero, con 0 para una arista sola en su
clase. Como cualquier segmento propio no vacío de una clase da un xor
no nulo con probabilidad abrumadora, dos cruces del mismo árbol son
3-conexos por aristas exactamente cuando sus etiquetas, los xor de
valores desde la raíz, coinciden. Cada consulta es una comparación.
`O(n + k + q)` esperado con una tabla hash para las clases.

En el ejemplo el cruce 6 solo tiene los tramos 1–6 y 4–6, y el cruce 2
solo 1–2 y 2–3, así que cada uno queda aislado por dos tramos. Según el
árbol de búsqueda, ese par es o bien dos aristas del árbol con
coberturas iguales, o bien una arista del árbol cubierta solo por el
otro tramo. Los otros cuatro cruces obtienen etiquetas iguales.

Trampas:

- los cruces de componentes distintas tienen etiqueta 0 en sus raíces,
  así que también se comparan las componentes;
- una clase cruzada por completo no separa: los extremos de una cadena
  de pares de corte están en un mismo trozo del anillo;
- 50000 vértices en un camino exigen una búsqueda en profundidad
  iterativa.

Todas las respuestas coinciden con una búsqueda por flujo máximo en
cientos de grafos pequeños aleatorios y con una implementación aceptada
independiente en grafos aleatorios, ruedas, anillos de bloques K4,
caminos y bosques de tamaño máximo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1819_graphs.cpp](1819_graphs.cpp) | G++ 13.2 x64 | graphs | O(n + k + q) | AC | 0.156 s | 5008 KB |
| [1819_graphs.go](1819_graphs.go) | Go 1.14 x64 | graphs | O(n + k + q) | AC | 0.062 s | 10436 KB |
| [1819_graphs.java](1819_graphs.java) | Java 1.8 | graphs | O(n + k + q) | AC | 0.125 s | 6744 KB |
| [1819_graphs.py](1819_graphs.py) | Python 3.12 x64 | graphs | O(n + k + q) | AC | 0.359 s | 34464 KB |
| [1819_graphs.rs](1819_graphs.rs) | Rust 1.75 x64 | graphs | O(n + k + q) | AC | 0.031 s | 9700 KB |
