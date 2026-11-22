# 1495. Un-dos, un-dos 2

[Timus 1495](https://acm.timus.ru/problem.aspx?space=1&num=1495) · dificultad 340 · bfs

Problema original de Igor Chevdar, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que hallar el menor número escrito solo con las cifras 1 y 2 que sea
divisible entre N (1 ≤ N ≤ 10⁶). Si no existe o tiene más de 30 cifras,
se escribe «Impossible».

Límite de tiempo: 2 segundos. Límite de memoria: 256 MB.

## Entrada

N.

## Salida

El número, o «Impossible».

## Ejemplos

### Ejemplo 1

Entrada:

```
5
```

Salida:

```
Impossible
```

### Ejemplo 2

Entrada:

```
8
```

Salida:

```
112
```

## Solución

Para lo que puede seguir a un prefijo solo importa su resto módulo N,
así que se busca en anchura sobre los restos. Se parte de los números 1
y 2, y desde un número con resto r se va a r·10 + 1 y luego a
r·10 + 2. Los números más cortos se alcanzan antes, y dentro de una
misma longitud la cola sigue el orden numérico, así que el primer
número que llega a un resto es el menor con ese resto; cualquier otro
posterior, y todas sus prolongaciones, serían mayores. Cada uno de los
N restos se guarda una vez con su última cifra y su padre, y la
respuesta se reconstruye por los padres en cuanto aparece el resto 0.
Los números dejan de crecer a las 30 cifras. `O(N)`.

Detalles a tener en cuenta:

- un número de unos y doses nunca acaba en 0 ni en 5, así que los
  múltiplos de 5 son imposibles (pruebas 01, 07, 09);
- la respuesta puede tener exactamente 30 cifras, como para 999999, y
  eso aún se admite (prueba 05);
- r·10 + d queda por debajo de 10⁷, pero la respuesta completa puede superar
  el rango de los enteros de 64 bits; se reconstruye a partir de sus cifras
  (pruebas 05, 08).

## Soluciones optimizadas

`1495_bfs_optimized.py`. Conserva BFS de residuos, orden 1 luego 2 y códigos/cola de 32 bits. Expande ambas aristas: calcula (10*r+1)%N una vez; para el dígito 2 suma uno con vuelta, sin otro módulo. Capas limitan a 30 cifras y mantienen el menor largo y orden lexicográfico. Múltiplos de cinco siguen siendo imposibles exactamente. O(N) trabajo/espacio bajo la cota. PyPy usa 11808 KB frente a 11404 KB antes, con tiempo de 0.921 a 0.14 s: aumento pequeño de memoria explícito. Conserva BFS didáctico. El anterior 0.921 s / 11404 KB usaba CPython 3.12; el seleccionado usa PyPy 3.10. Cambian código e intérprete: comparación de ejecuciones emparejadas, no benchmark aislado de reescribir aristas.

Accepted exacto PyPy 3.10 #11326708: 0.14 s / 11808 KB. Comparación guardada 2026-11-20 con compiladores actuales de la familia: tiempo 1/19, memoria 1/19. Desde 1024 KB se exigen ambos criterios estrictos; pasan ambos.

- `1495_bfs_optimized.py`: 0.14 s / 11808 KB; base didáctica conservada `1495_bfs.py` (Python 3.12 x64): 0.906 s / 62744 KB; cambio de tiempo -84.5%; cambio de memoria -81.2%.

Las versiones en C++, Go y Python usan la misma búsqueda en anchura. Cada resto ocupa una entrada de 32 bits. Cero indica que aún no se ha visitado. En las demás entradas, los bits superiores guardan el predecesor más uno y el bit inferior guarda el dígito menos uno. La cola también usa entradas de 32 bits y los límites de cada nivel dan la longitud.

Las bases Accepted conservadas [1495_bfs.go](1495_bfs.go), [1495_bfs.java](1495_bfs.java), [1495_bfs.rs](1495_bfs.rs) pasan también diez primeros o 15% superior en las métricas exigidas de la comparación guardada. Se reutilizan sin duplicados; conserva las demás bases. El asterisco indica la meta propia del lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1495_bfs.cpp](1495_bfs.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.046 s | 14636 KB | 11287220 |
| [1495_bfs.go](1495_bfs.go) | Go 1.14 x64 | bfs | O(N) | AC | 0.093 s | 32440 KB | 11287221 |
| [1495_bfs.java](1495_bfs.java) \* | Java 1.8 | bfs | O(N) | AC | 0.156 s | 17324 KB | 11287225 |
| [1495_bfs.py](1495_bfs.py) | Python 3.12 x64 | bfs | O(N) | AC | 0.906 s | 62744 KB | 11287224 |
| [1495_bfs.rs](1495_bfs.rs) | Rust 1.75 x64 | bfs | O(N) | AC | 0.062 s | 26080 KB | 11287226 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1495_bfs_optimized.cpp](1495_bfs_optimized.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.015 s | 7004 KB | 11310407 |
| [1495_bfs_optimized.go](1495_bfs_optimized.go) \* | Go 1.14 x64 | bfs | O(N) | AC | 0.046 s | 8964 KB | 11310363 |
| [1495_bfs_optimized.py](1495_bfs_optimized.py) | PyPy 3.10 x64 | bfs | O(N) | AC | 0.14 s | 11808 KB | 11326708 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
