# 1774. El barbero del ejército de magos

[Timus 1774](https://acm.timus.ru/problem.aspx?space=1&num=1774) · dificultad 519 · matching

Problema original de Magaz Asanov, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n personas necesitan dos afeitados cada una, en dos minutos enteros
distintos de su estancia: la persona i llega en el minuto tᵢ y se queda
sᵢ minutos, así que valen los minutos de tᵢ a tᵢ + sᵢ − 1. En un minuto
se puede afeitar a lo sumo a k personas. Decidir si se puede afeitar a
todos y dar los dos minutos de cada uno.

## Entrada

n y k (1 ≤ n, k ≤ 100) y luego tᵢ y sᵢ de cada persona
(0 ≤ tᵢ ≤ 1000, 2 ≤ sᵢ ≤ 1000).

## Salida

`No`, o `Yes` y para cada persona dos minutos pᵢ < qᵢ. Se acepta
cualquier horario válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2
1 3
1 3
1 3
```

Salida:

```
Yes
1 2
1 3
2 3
```

### Ejemplo 2

Entrada:

```
2 1
1 3
1 3
```

Salida:

```
No
```

## Solución

Es un problema de flujo: cada persona envía 2 afeitados, cada minuto
recibe a lo sumo k, y una persona puede enviar a lo sumo un afeitado a
cada minuto de su estancia. Los minutos entre dos momentos consecutivos
de llegada o salida ven a las mismas personas, así que se agrupan en
bloques: un bloque de L minutos recibe a lo sumo k·L afeitados, y a lo
sumo min(L, 2) de una misma persona. Con a lo sumo 2n + 1 bloques la red
es pequeña, y el algoritmo de Dinic halla el flujo máximo; se puede
afeitar a todos justo cuando vale 2n.

Dentro de un bloque los afeitados se reparten por turno entre sus
minutos, los de cada persona seguidos. Así dos afeitados de una persona
en un bloque caen en minutos distintos, pues L ≥ 2 cuando envía dos
allí, y ningún minuto recibe más de k, ya que el bloque admite a lo sumo
k·L. La red tiene O(n²) aristas y lleva a lo sumo 2n afeitados, cada uno
hallado por un camino en O(n²), así que `O(n³)` en total.

En el primer ejemplo las tres personas comparten los minutos 1 a 3 con
k = 2: seis afeitados llenan los seis huecos, y repartirlos por turno da
1 2, 3 1, 2 3, es decir, cada par de minutos una vez.

Trampas:

- los dos afeitados de una persona deben ir en minutos distintos, algo
  que una simple cuenta por bloque no ve;
- el último minuto válido es tᵢ + sᵢ − 1, no tᵢ + sᵢ;
- el horario no es único, así que el verificador comprueba las ventanas
  y la carga de cada minuto.

Las respuestas coinciden con una búsqueda sobre todos los pares de
minutos en 300 casos aleatorios de hasta 5 personas y con una
implementación aceptada independiente, comprobadas en ambos sentidos,
en 100 casos de hasta 100 personas.

La versión didáctica en C++ crea un vértice para cada minuto de 0 a 1999. La fuente envía dos unidades a cada persona. Una arista de capacidad uno conecta a la persona con cada minuto de su estancia, y cada minuto envía como máximo k unidades al sumidero. Un flujo entero de 2n asigna exactamente dos minutos válidos y distintos a cada persona. Las rutas aumentantes se buscan en profundidad y añaden una unidad. Si no queda ninguna, el flujo es máximo. Los minutos elegidos se leen directamente de las aristas saturadas de persona a minuto. Para E=n+2000+Σsᵢ aristas directas, tiempo O(nE), espacio O(E).

## Soluciones optimizadas

C++, Go, Java y Rust conservan Dinic comprimido por extremos y recuperación cíclica. Cada arista residual usa tres campos de 16 bits para destino, siguiente y capacidad. Las cabeceras planas sustituyen las listas. Como hay a lo sumo 2n extremos, B≤2n−1 bloques y 301 vértices, y como máximo 2(nB+n+B+1)≤40 400 registros con dos centinelas. Los índices caben en 16 bits. Limitar la capacidad intervalo–sumidero a la demanda 2n≤200 preserva la factibilidad, pues un horario completo solo usa 2n unidades, y acota los residuos. Contar primero aristas persona/intervalo permite reservar exactamente una vez; reutilizar BFS, niveles y cursores. Recuperar los dos tiempos desde capacidades inversas elimina enlaces auxiliares y listas por persona. Una tabla de 2001 instantes evita ordenar y usar conjuntos. En un bloque de L minutos, cada persona obtiene a lo sumo min(L,2) posiciones consecutivas del reparto cíclico, así que son distintas. Con a lo sumo kL posiciones totales, cada minuto recibe como máximo k. Tiempo O(n³), memoria O(n²). Se conservan bases; Python reutiliza la admitida.

Las implementaciones base aceptadas [1774_matching.py](1774_matching.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1774_matching.cpp](1774_matching.cpp) | G++ 13.2 x64 | matching | O(n^3) | AC | 0.031 s | 580 KB | 11289698 |
| [1774_matching.go](1774_matching.go) | Go 1.14 x64 | matching | O(n^3) | AC | 0.031 s | 3476 KB | 11289701 |
| [1774_matching.java](1774_matching.java) | Java 1.8 | matching | O(n^3) | AC | 0.156 s | 3652 KB | 11289704 |
| [1774_matching.py](1774_matching.py) | Python 3.12 x64 | matching | O(n^3) | AC | 0.093 s | 4024 KB | 11289702 |
| [1774_matching.rs](1774_matching.rs) | Rust 1.75 x64 | matching | O(n^3) | AC | 0.046 s | 964 KB | 11289706 |
| [1774_flow.cpp](1774_flow.cpp) | G++ 13.2 x64 | flow | O(nE) | AC | 0.015 s | 3584 KB | 11315880 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1774_matching_optimized.cpp](1774_matching_optimized.cpp) | G++ 13.2 x64 | matching | O(n³) | AC | 0.015 s | 300 KB | 11315516 |
| [1774_matching_optimized.go](1774_matching_optimized.go) \* | Go 1.14 x64 | matching | O(n³) | AC | 0.031 s | 1020 KB | 11315517 |
| [1774_matching_optimized.java](1774_matching_optimized.java) \* | Java 1.8 | matching | O(n³) | AC | 0.093 s | 572 KB | 11315518 |
| [1774_matching_optimized.rs](1774_matching_optimized.rs) \* | Rust 1.75 x64 | matching | O(n³) | AC | 0.015 s | 312 KB | 11315519 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
