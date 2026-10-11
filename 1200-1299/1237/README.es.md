# 1237. Comprobar si un plan de evacuación es óptimo

[Timus 1237](https://acm.timus.ru/problem.aspx?space=1&num=1237) · dificultad 985 · graphs

Problema original de Vladimir Kotov, del concurso regional ACM ICPC del noreste de Europa 2002–2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N edificios (N ≤ 100) tienen B_i trabajadores cada uno, y M refugios
(M ≤ 100) admiten como mucho C_j personas cada uno. Ir del edificio i al
refugio j lleva `|X_i − P_j| + |Y_i − Q_j| + 1`. Un plan dice cuántos
trabajadores E_ij de cada edificio van a cada refugio; envía a todos y
respeta las capacidades. Hay que decidir si el plan tiene el menor
tiempo total y, si no, mostrar cualquier plan válido con un total menor.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M; los edificios como `X Y B`; los refugios como `P Q C`; y luego las
N filas del plan.

## Salida

`OPTIMAL`, o `SUBOPTIMAL` seguido de un plan mejor con el mismo formato.

## Evaluación

Se acepta cualquier plan mejor. El verificador compara la primera
palabra con la respuesta esperada y comprueba que el plan envía a todos
los trabajadores de cada edificio, cabe en cada refugio y tiene un
tiempo total menor que el dado.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4
-3 3 5
-2 -2 6
2 2 5
-1 1 3
1 1 4
-2 -2 7
0 -1 3
3 1 1 0
0 0 6 0
0 3 0 2
```

Salida:

```
SUBOPTIMAL
3 0 1 1
0 0 6 0
0 4 0 1
```

### Ejemplo 2

Entrada:

```
3 4
-3 3 5
-2 -2 6
2 2 5
-1 1 3
1 1 4
-2 -2 7
0 -1 3
3 0 1 1
0 0 6 0
0 4 0 1
```

Salida:

```
OPTIMAL
```

## Solución

El plan es un flujo, y un flujo tiene el menor coste justo cuando su
grafo residual no tiene ningún ciclo de coste negativo. Aquí ese grafo
se puede construir solo con los refugios más un nodo extra para el sitio
libre:

- **j → k** pasa un trabajador de algún edificio i del refugio j al k, lo
  que requiere `E_ij > 0` y cuesta `D_ik − D_ij`; la arista toma el
  edificio más barato;
- **j → libre**, coste 0, existe cuando el refugio j tiene una plaza
  libre;
- **libre → k**, coste 0, deja que el refugio k acabe con un trabajador
  menos.

Un ciclo solo por refugios mueve una cadena de trabajadores y conserva la
ocupación de cada refugio; un ciclo por el nodo libre ocupa una plaza
libre en un extremo y vacía una en el otro. Bellman–Ford desde todos los
nodos a la vez o se estabiliza en como mucho M + 1 rondas (`OPTIMAL`), o
aún cambia una distancia en la última ronda; entonces seguir a los
predecesores M + 1 veces lleva a un ciclo negativo, y mover un trabajador
por cada una de sus aristas entre refugios da un plan válido más barato.
`O(N·M² + M³)`.

Detalles a tener en cuenta:

- si se deja fuera del grafo el sitio libre del plan dado se pierden
  mejoras como la de la prueba 05, donde un trabajador solo tiene que
  pasar a un refugio vacío más cercano;
- un ciclo simple sale de cada refugio una sola vez, así que cada
  movimiento toma un trabajador que de verdad está allí.

Los veredictos se compararon con un flujo de coste mínimo exacto en 399
ciudades pequeñas aleatorias, y cada plan mejor pasó por el verificador.

## Notas por lenguaje

- Python relaja todas las aristas que entran en un nodo de una vez con
  `map`, y busca el edificio de cada arista solo para las aristas del
  ciclo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1237_graphs.cpp](1237_graphs.cpp) | G++ 13.2 x64 | graphs | O(N·M² + M³) | AC | 0.031 s | 372 KB |
| [1237_graphs.go](1237_graphs.go) | Go 1.14 x64 | graphs | O(N·M² + M³) | AC | 0.031 s | 1516 KB |
| [1237_graphs.java](1237_graphs.java) | Java 1.8 | graphs | O(N·M² + M³) | AC | 0.125 s | 952 KB |
| [1237_graphs.py](1237_graphs.py) | Python 3.12 x64 | graphs | O(N·M² + M³) | AC | 0.187 s | 1744 KB |
| [1237_graphs.rs](1237_graphs.rs) | Rust 1.75 x64 | graphs | O(N·M² + M³) | AC | 0.031 s | 564 KB |
