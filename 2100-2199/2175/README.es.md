# 2175. Número de máximos de prefijo cuando los elementos solo crecen

[Timus 2175](https://acm.timus.ru/problem.aspx?space=1&num=2175) · dificultad 1006 · fenwick

Problema original de Ignat Nigmatullin, del Concurso Escolar de Programación de los Urales 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La escalera de un arreglo empieza con su primer elemento y toma una y
otra vez el primer elemento posterior estrictamente mayor que el último
tomado, así que está formada por los máximos de prefijo estrictos. Cada
una de las Q actualizaciones suma una cantidad no negativa a un
elemento; imprimir la longitud de la escalera tras cada una. Los límites
son 2 segundos y 256 MB.

## Entrada

N, 1 ≤ N ≤ 10⁵, el arreglo, 0 ≤ aᵢ ≤ 10⁹, y luego Q, 1 ≤ Q ≤ 10⁵, y las
actualizaciones p, x con 0 ≤ x ≤ 10⁹.

## Salida

La longitud de la escalera tras cada actualización.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1 2 5 1 7
3
1 3
2 3
4 6
```

Salida:

```
3
3
3
```

## Solución

La escalera se guarda como una lista enlazada de posiciones. Cuando aₚ
crece:

- Si p no está en la escalera, entra exactamente cuando su valor nuevo
  supera a todos los elementos anteriores. El mayor elemento anterior, el
  primero entre iguales, está en la escalera, y p se enlaza justo
  después de él.
- Si p está ahora en la escalera, los siguientes elementos de la
  escalera que no superan el valor nuevo salen uno tras otro, hasta uno
  mayor o el final.

Los valores solo crecen, así que cada salida la paga una inserción
anterior, y hay a lo sumo N + Q inserciones. El máximo de un prefijo sale
de un árbol de Fenwick de máximos sobre las posiciones; al crecer un
valor se actualizan sus nodos, y la subida se detiene en el primer nodo
que ya guarda un valor mayor, porque todos los nodos siguientes también
lo contienen. El trabajo es O((N + Q) log N).

En el ejemplo la primera actualización deja el arreglo 4 2 5 1 7, y la
escalera 4, 5, 7 tiene tres elementos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2175_fenwick.cpp](2175_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((N + Q) log N) | AC | 0.078 s | 1404 KB |
| [2175_fenwick.go](2175_fenwick.go) | Go 1.14 x64 | fenwick | O((N + Q) log N) | AC | 0.046 s | 11164 KB |
| [2175_fenwick.java](2175_fenwick.java) | Java 1.8 | fenwick | O((N + Q) log N) | AC | 0.125 s | 8376 KB |
| [2175_fenwick.py](2175_fenwick.py) | Python 3.12 x64 | fenwick | O((N + Q) log N) | AC | 0.625 s | 36632 KB |
| [2175_fenwick.rs](2175_fenwick.rs) | Rust 1.75 x64 | fenwick | O((N + Q) log N) | AC | 0.031 s | 7376 KB |
