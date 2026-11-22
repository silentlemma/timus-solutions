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

`1320_dsu_optimized.py`. Mantiene la paridad con DSU: cada componente debe tener un número par de aristas. Una raíz negativa codifica -(2*size+parity); compresión por mitades y unión por tamaño dan O((V+E)*alpha(V)) amortizado. Actualiza el número de componentes impares al unir raíces o cambiar la paridad interna. Lee y divide toda la entrada acotada y pasa un iterador entero a decomposable: almacenamiento O(V+I), no O(V) en flujo. No requiere pypyjit; las métricas actuales son de CPython. La escritura directa y os._exit(0) están al nivel superior después del retorno: no se supone que parent siga vivo hasta salir.

Accepted exacto Python 3.12 x64 #11327483: 0.078 s / 808 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 6/42, memoria 13/42. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11309751 (PyPy 3.10 x64) era 0.156 s / 436 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1320_dsu_optimized.py`: 0.078 s / 808 KB; base didáctica conservada `1320_dsu.py`: 0.093 s / 656 KB.

`1320_dsu_optimized.go`. Procesa aristas en DSU con reducción de camino a la mitad. Arrays fijos de 1001 padres uint16 y paridad por componente sustituyen extremos retenidos y contadores enteros. Fusiona por XOR y conmuta por cada arista, incluidos bucles y repetidas. V=1000 cabe en uint16. Sin unión por rango: cota conservadora O(EV+V), espacio O(V). Buffers acotados de entrada de 256 bytes y salida de 64 usan syscall.Read/Write de Go 1.14, reintentan EINTR/escrituras parciales y tratan EOF de cero bytes. Elimina inicialización fmt/bufio/os.File. Pruebas Linux y compilación cruzada Windows validan funcionamiento y construcción; las métricas pareadas siguientes vienen de nuestro Accepted exacto en juez Windows. Se conserva fuente didáctica legible.

Frente a `1320_dsu.go`: tiempo 0.015 s → 0.015 s; memoria 1112 KB → 336 KB.

`1320_dsu_optimized.rs`. Conserva DSU con reducción a la mitad y paridad de aristas por componente. Flujo de aristas, padres u16 y byte de paridad; XOR al unir y conmutación por arista incluso bucles. Sin balance por rango: cota conservadora O(EV+V) tiempo y O(V) espacio, V=1000. Conserva versión legible con extremos.

Frente a `1320_dsu.rs`: tiempo 0.015 s → 0.015 s; memoria 264 KB → 68 KB.

Se conservan los DSU claros. Emparejar aristas es posible si y solo si cada componente tiene cantidad par. Java guarda enlaces positivos y paridad raíz 0/-1 en un array short inicializado a cero. Una arista interna invierte paridad; unir toma XOR de ambas y 1. Acortar caminos conserva componentes; etiquetas 1..1000 caben en short. El búfer de entrada estándar de 512 bytes se rellena incluso dentro de una etiqueta de cuatro dígitos, acepta espacios válidos yEOF y escribe bytes. Python codifica tamaño y paridad en raíz negativa-(2*size+parity), une por tamaño y mantiene componentes impares. Cada fuente compara con su base actual. Java: O((V+M)log V)amortizado/O(V)memoria; Python: O((V+M)alpha(V)), O(V+M)incluidos tokens.

Mediciones históricas de revisiones anteriores: PyPy también desactiva JIT para reducir memoria de caché de código; puede aumentar el tiempo.

- `1320_dsu_optimized.java`: 0.093 s / 408 KB; base `1320_dsu.java`: 0.109 s / 420 KB; cambio respecto a la base: tiempo -14.7%, memoria -2.9%.

## Notas por lenguaje

Las instantáneas se guardaron el 1 y el 4 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1320_dsu.cpp`; fuente que cubre `1320_dsu.cpp`; puestos tiempo/memoria 1/2, registros de otros autores 100/100.

- Go: base didáctica preferida `1320_dsu.go`; fuente que cubre `1320_dsu.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1320_dsu.java`; fuente que cubre `1320_dsu_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 5/5.

Mediciones históricas de revisiones anteriores: - Python/PyPy: base didáctica preferida `1320_dsu.py`; fuente que cubre `1320_dsu_optimized.py`; puestos tiempo/memoria 34/1, registros de otros autores 34/34.

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
| [1320_dsu_optimized.py](1320_dsu_optimized.py) \* | Python 3.12 x64 | dsu | O((V+E) alpha(V)) amortized; O(V+I) storage | AC | 0.078 s | 808 KB | 11327483 |
| [1320_dsu_optimized.go](1320_dsu_optimized.go) \* | Go 1.14 x64 | dsu | O(EV+V) time; O(V) space | AC | 0.015 s | 336 KB | 11325655 |
| [1320_dsu_optimized.rs](1320_dsu_optimized.rs) \* | Rust 1.75 x64 | dsu | O(EV+V) time; O(V) space | AC | 0.015 s | 68 KB | 11325501 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
