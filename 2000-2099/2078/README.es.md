# 2078. Cotas del marcador de bolos a partir de los totales por cuadro

[Timus 2078](https://acm.timus.ru/problem.aspx?space=1&num=2078) · dificultad 275 · dp, simulation

Problema original de Alexander Krasnoselskikh, preparado por Oleg Dolgorukov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una partida de bolos tiene diez cuadros. En los cuadros 1 a 9 se lanza a
10 bolos hasta dos veces; derribarlos todos con el primer lanzamiento es
un pleno (el segundo se omite), y con los dos, un semipleno. Un pleno
suma al cuadro los dos lanzamientos siguientes, un semipleno el
siguiente. El último cuadro da un tercer lanzamiento tras un pleno o un
semipleno, con bolos nuevos cada vez que caen todos, y no recibe bonos.
Solo se conoce cuántos bolos cayeron en cada cuadro. Hallar el menor y
el mayor marcador posibles. Los límites son 2 segundos y 256 MB.

## Entrada

Diez números: los bolos de los cuadros 1 a 9 (de 0 a 10) y del último
cuadro (de 0 a 30).

## Salida

El menor y el mayor marcador.

## Evaluación

Se comparan los tokens exactos; los espacios no afectan.

- `2078_dp_simulation.go` (Go 1.14 x64): 14 pruebas del repositorio; 14 comparaciones adicionales de fuente exacta.

- `2078_dp_simulation.java` (Java 1.8): 14 pruebas del repositorio; 444 comparaciones adicionales de fuente exacta.

- `2078_dp_simulation.py` (PyPy 3.10 x64): 14 pruebas del repositorio.

- `2078_dp_simulation.rs` (Rust 1.75 x64): 14 pruebas del repositorio.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 2 4 8 3 8 1 9 8 7
```

Salida:

```
60 62
```

### Ejemplo 2

Entrada:

```
2 4 6 8 10 10 8 6 4 2
```

Salida:

```
60 86
```

## Solución

Los bolos en sí suman lo mismo con cualquier reparto de los cuadros en
lanzamientos; solo cambian los bonos, y estos miran a lo sumo dos
lanzamientos adelante. Así que una DP recorre los cuadros del último al
primero y guarda, para cada par (x, y) de los dos primeros lanzamientos
desde el cuadro actual, el menor y el mayor marcador de los cuadros de
ahí al final.

Para el último cuadro se prueban todas las secuencias válidas con el
total correcto: dos lanzamientos sin pleno ni semipleno, y en otro caso un
tercero con bolos nuevos (o con los que quedan tras un pleno y un
segundo lanzamiento parcial). Su par son sus dos primeros lanzamientos y
su marcador es su total.

Un cuadro con menos de 10 bolos se reparte como (r, t − r) para
cualquier r, y su par son esos dos lanzamientos. Un cuadro con 10 bolos
es un pleno, con par (10, x) para el par (x, y) del cuadro siguiente y
bono x + y, o un semipleno (r, 10 − r) con bono x. La respuesta es el
extremo sobre los pares del primer cuadro; hay a lo sumo 121 pares, así
que el trabajo es O(1).

En el primer ejemplo el primer cuadro es un pleno o un semipleno,
seguido de un cuadro de 2 bolos: como pleno suma los dos lanzamientos de
ese cuadro (2 puntos), como semipleno no suma nada si ese cuadro empieza
con 0; de ahí 60 y 62.

## Soluciones optimizadas

`2078_dp_simulation.py`. Conserva DP cronológica de cuatro deudas (0,0),(1,0),(1,1),(2,1). Desenrolla mínimos/máximos en ocho escalares, elimina listas por frame y bucle de estados. Mismas reglas de reposición final y extremos exactos; centinelas ±10000 fuera de puntajes legales 0..300. O(F) tiempo, estado constante más O(F) totales de entrada. CPython elegido es más rápido pero usa más memoria que PyPy histórico; no mezcla pares/runtimes. Conserva DP inversa didáctica.

Fuente exacto: Python 3.12 x64 Accepted #11327850: 0.078 s / 796 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 1/227; 174/227. Admisión estricta usa solo tiempo bajo 1024 KB: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. La variante anterior conservada tiene su par propio #11309738 (PyPy 3.10 x64): 0.14 s / 276 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `2078_dp_simulation.py`: 0.078 s / 796 KB; base didáctica conservada `2078_dp.py`: 0.093 s / 708 KB.

Se conserva el DP inverso claro. dp_simulation cronológico guarda los bonos pendientes de las dos próximas tiradas: solo (0,0), (1,0), (1,1), (2,1), con mínimo/máximo por estado. En un frame de dos tiradas y total t, el bono adicional es b*t+(a-b)*first; como a >= b, sus extremos están en los extremos legales de la primera tirada. Un strike consume el primer bono viejo, desplaza el segundo y añade sus dos bonos. El último frame no crea bonos; las reglas de reposición dan los extremos, y un total > 20 obliga a dos primeras tiradas de 10. Las transiciones cubren toda secuencia legal. Cuatro estados sustituyen 121 pares futuros: O(F) tiempo y memoria constante de puntuación. Cada E/S tiene Accepted propio.

- `2078_dp_simulation.go`: 0.031 s / 312 KB; base `2078_dp.go`: 0.031 s / 1144 KB; cambio respecto a la base: tiempo -0.0%, memoria -72.7%.
- `2078_dp_simulation.java`: 0.109 s / 416 KB; base `2078_dp.java`: 0.125 s / 1660 KB; cambio respecto a la base: tiempo -12.8%, memoria -74.9%.

- `2078_dp_simulation.rs`: 0.015 s / 60 KB; base `2078_dp.rs`: 0.031 s / 224 KB; cambio respecto a la base: tiempo -51.6%, memoria -73.2%.

El código sin cambios de cuatro estados obtuvo Rust 1.75 x64 Accepted #11329569: **0.015 s / 60 KB**. Ambas métricas proceden de esa misma ejecución. El único rival elegible con el mismo compilador (#10818310, 0.015 s) fija un límite de 0.031 s: la tolerancia de un tic mostrado supera el margen del 15%; el código cumple los [criterios compartidos](../../RATING_CRITERIA.md). La memoria no se compara por debajo de 1024 KB. Las cinco repeticiones dieron entre 0.015 y 0.062 s; esto no demuestra una nueva mejora algorítmica. Se conserva la versión sencilla de Rust.

## Notas por lenguaje

Todas las familias usan los [criterios compartidos](../../RATING_CRITERIA.md). Por debajo de 1024 KB solo se compara el tiempo; las muestras pequeñas del mismo compilador usan la referencia prescrita y un margen del 15%. Rust se reevaluó el 2026-11-24; las demás notas de grupos siguientes se conservan como instantáneas históricas.

- C++: base didáctica preferida `2078_dp.cpp`; fuente que cubre `2078_dp.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 42/42.

- Go: base didáctica preferida `2078_dp.go`; fuente que cubre `2078_dp_simulation.go`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Java: base didáctica preferida `2078_dp.java`; fuente que cubre `2078_dp_simulation.java`; puestos tiempo/memoria 1/1, registros de otros autores 4/4.

- Python/PyPy: base didáctica preferida `2078_dp.py`; fuente que cubre `2078_dp_simulation.py`; puestos tiempo/memoria 153/2, registros de otros autores 158/158.

- Rust: base didáctica preferida `2078_dp.rs`; fuente que cubre `2078_dp_simulation.rs`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2078_dp.cpp](2078_dp.cpp) | G++ 13.2 x64 | dp | O(1) | AC | 0.015 s | 116 KB | 11309235 |
| [2078_dp.go](2078_dp.go) | Go 1.14 x64 | dp | O(1) | AC | 0.031 s | 1144 KB | 11294529 |
| [2078_dp.java](2078_dp.java) | Java 1.8 | dp | O(1) | AC | 0.125 s | 1660 KB | 11309236 |
| [2078_dp.py](2078_dp.py) | Python 3.12 x64 | dp | O(1) | AC | 0.093 s | 708 KB | 11294532 |
| [2078_dp.rs](2078_dp.rs) | Rust 1.75 x64 | dp | O(1) | AC | 0.031 s | 224 KB | 11309237 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2078_dp_simulation.go](2078_dp_simulation.go) | Go 1.14 x64 | dp, simulation | O(F) time; O(1) score state | AC | 0.031 s | 312 KB | 11309759 |
| [2078_dp_simulation.java](2078_dp_simulation.java) | Java 1.8 | dp, simulation | O(F) time; O(1) score state | AC | 0.109 s | 416 KB | 11309301 |
| [2078_dp_simulation.py](2078_dp_simulation.py) | Python 3.12 x64 | dp, simulation | O(F) time; O(1) score state plus O(F) input | AC | 0.078 s | 796 KB | 11327850 |
| [2078_dp_simulation.rs](2078_dp_simulation.rs) | Rust 1.75 x64 | dp, simulation | O(F) time; O(1) score state | AC | 0.015 s | 60 KB | 11329569 |
