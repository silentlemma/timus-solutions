# 1320. Descomposición de un grafo

[Timus 1320](https://acm.timus.ru/problem.aspx?space=1&num=1320) · dificultad 283 · dsu

Problema original con idea de Alexander Petrov, preparado por Alexander Petrov y Leonid Volkov, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo simple tiene un número par de aristas, de 2 a 1050, con
vértices numerados de 1 a 1000. Hay que decidir si sus aristas se
pueden repartir en pares de aristas adyacentes, es decir, con un
vértice común.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

Las aristas, cada una como un par de números de vértice, hasta el final
de la entrada. No hay lazos ni aristas repetidas.

## Salida

1 si ese reparto existe, si no 0.

## Evaluación

Tokens exactos. Cada fuente nueva tiene pruebas completas del entorno destino, comparaciones matemáticas independientes y Accepted propio ligado al hash; las bases conservan sus propias medidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2
2 3
3 1
1 10
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
1 2
2 3
3 1
4 10
```

Salida:

```
0
```

## Solución

Dos aristas adyacentes siempre están en la misma componente conexa, así
que cada componente necesita un número par de aristas. Eso también
basta: un grafo conexo con un número par de aristas siempre se puede
repartir. Se toma un árbol de búsqueda en profundidad y se tratan los
vértices desde los más profundos hacia arriba. En un vértice v, las
aristas libres en v, salvo la que va al padre, se emparejan entre sí;
si sobra una, se empareja con la arista al padre, y si no, la arista al
padre queda libre para el padre. Ningún vértice salvo la raíz deja
aristas libres por debajo, y en la raíz las aristas libres se emparejan
entre sí, lo que es posible porque el total es par.

Así que la respuesta solo necesita el número de aristas de cada
componente. Una unión de conjuntos disjuntos sobre los vértices lo
guarda en cada raíz: al unir dos componentes se suman sus cuentas, y
cada arista suma uno. Al final se comprueba que cada raíz tenga una
cuenta par. Aquí V es el rango de vértices y M el número de aristas.
Las raíces se unen sin equilibrar por rango o tamaño, por lo que la
división de caminos a la mitad da una cota total segura de
`O(V + M log V)`, incluidas la inicialización y la comprobación final
de las raíces.

Detalles a tener en cuenta:

- el grafo entero siempre tiene un número par de aristas, pero una
  componente puede no tenerlo: un triángulo y una arista aparte dan 0
  (prueba 02, y también dos triángulos separados en la prueba 06);
- no se da el número de aristas, la entrada simplemente termina;
- dos triángulos con un vértice común forman una sola componente de
  seis aristas y se pueden repartir (prueba 07).

La regla se comparó con una búsqueda sobre todos los emparejamientos en
487 grafos aleatorios de hasta 14 aristas.

## Soluciones optimizadas

Se conservan los DSU claros. Emparejar aristas es posible si y solo si cada componente tiene cantidad par. Java guarda enlaces positivos y paridad raíz 0/-1 en un array short inicializado a cero. Una arista interna invierte paridad; unir toma XOR de ambas y 1. Acortar caminos conserva componentes; etiquetas 1..1000 caben en short. El búfer de entrada estándar de 512 bytes se rellena incluso dentro de una etiqueta de cuatro dígitos, acepta espacios válidos yEOF y escribe bytes. Python codifica tamaño y paridad en raíz negativa-(2*size+parity), une por tamaño y mantiene componentes impares. Cada fuente compara con su base actual. Java: O((V+M)log V)amortizado/O(V)memoria; Python: O((V+M)alpha(V)), O(V+M)incluidos tokens.

PyPy también desactiva JIT para reducir memoria de caché de código; puede aumentar el tiempo.

- `1320_dsu_optimized.java`: 0.093 s / 408 KB; base `1320_dsu.java`: 0.109 s / 420 KB; cambio respecto a la base: tiempo -14.7%, memoria -2.9%.
- `1320_dsu_optimized.py`: 0.156 s / 436 KB; base `1320_dsu.py`: 0.093 s / 656 KB; cambio respecto a la base: tiempo +67.7%, memoria -33.5%.

## Notas por lenguaje

Las instantáneas se guardaron el 1 y el 4 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1320_dsu.cpp`; fuente que cubre `1320_dsu.cpp`; puestos tiempo/memoria 1/2, registros de otros autores 100/100.

- Go: base didáctica preferida `1320_dsu.go`; fuente que cubre `1320_dsu.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1320_dsu.java`; fuente que cubre `1320_dsu_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 5/5.

- Python/PyPy: base didáctica preferida `1320_dsu.py`; fuente que cubre `1320_dsu_optimized.py`; puestos tiempo/memoria 34/1, registros de otros autores 34/34.

- Rust: base didáctica preferida `1320_dsu.rs`; fuente que cubre `1320_dsu.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1320_dsu.cpp](1320_dsu.cpp) | G++ 13.2 x64 | dsu | O(V + M log V) | AC | 0.015 s | 184 KB | 11284943 |
| [1320_dsu.go](1320_dsu.go) | Go 1.14 x64 | dsu | O(V + M log V) | AC | 0.015 s | 1112 KB | 11284944 |
| [1320_dsu.java](1320_dsu.java) | Java 1.8 | dsu | O(V + M log V) | AC | 0.109 s | 420 KB | 11284946 |
| [1320_dsu.py](1320_dsu.py) | Python 3.12 x64 | dsu | O(V + M log V) | AC | 0.093 s | 656 KB | 11284945 |
| [1320_dsu.rs](1320_dsu.rs) | Rust 1.75 x64 | dsu | O(V + M log V) | AC | 0.015 s | 264 KB | 11284947 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1320_dsu_optimized.java](1320_dsu_optimized.java) | Java 1.8 | dsu | O((V+M) log V) amortized; O(V) storage | AC | 0.093 s | 408 KB | 11310097 |
| [1320_dsu_optimized.py](1320_dsu_optimized.py) \* | PyPy 3.10 x64 | dsu | O((V+M) alpha(V)) amortized; O(V+L) space, L=max line tokens | AC | 0.156 s | 436 KB | 11309751 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
