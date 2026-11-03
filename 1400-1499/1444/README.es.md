# 1444. Alimentar al elefpótamo

[Timus 1444](https://acm.timus.ru/problem.aspx?space=1&num=1444) · dificultad 262 · geometry

Problema original de Ekaterina Vasilyeva (idea y texto) y Alexander Mironenko, Alexey Lakhtin y Den Raskovalov (programación), del Décimo Campeonato Universitario de Programación por Equipos de los Urales, 24–25 de marzo de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N calabazas (3 ≤ N ≤ 30000) están en puntos enteros distintos con
coordenadas de −1000 a 1000, no todas en una recta. Un elefpótamo empieza
en la calabaza 1 y se la come; tras cada calabaza se le puede mandar en
línea recta hacia cualquier calabaza restante. El animal se detiene para
siempre en cuanto pisa sus propias huellas, así que el recorrido nunca
debe tocarse a sí mismo. Hay que hallar el mayor número K de calabazas
que puede comer y el orden del recorrido, empezando por la 1.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego las coordenadas de las calabazas 1 a N.

## Salida

K y luego los números de las calabazas en el orden en que se comen, uno
por línea. Se acepta cualquier recorrido válido.

## Evaluación

Se acepta cualquier recorrido máximo desde el primer punto, con índices distintos y sin cruces ni contactos propios.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
10 10
0 10
10 0
```

Salida:

```
4
1
3
2
4
```

## Solución

Siempre se pueden comer las N calabazas. Las demás se ordenan por el
ángulo de la dirección desde la calabaza 1 y, en un mismo rayo, por la
distancia, las cercanas primero; las comparaciones usan productos
vectoriales enteros, así que son exactas. Recorrerlas en ese orden barre
alrededor de la calabaza 1 como un abanico: cada paso avanza más lejos
por el mismo rayo o pasa a la dirección siguiente, de modo que el
recorrido está en cada momento dentro de un sector estrecho y nunca
vuelve atrás.

El único peligro es el comienzo del círculo. Si dos direcciones vecinas
distan media vuelta o más, el paso entre ellas podría pasar por la
calabaza 1 o cortar pasos anteriores, así que el círculo se corta justo
después de ese hueco; solo puede haber uno, porque no todas las
calabazas están en una recta. Sin un hueco así, se corta entre dos grupos
consecutivos de rayos distintos, empezando por la calabaza más cercana
del siguiente grupo. No se debe dividir un grupo entre ambos lados del
corte: volver a sus calabazas más cercanas tocaría el segmento inicial.
El corte predeterminado de las soluciones, al comienzo de la ordenación
angular, ya cumple esta regla.
`O(N log N)`.

Detalles a tener en cuenta:

- varias calabazas en un mismo rayo se comen de la más cercana a la más
  lejana (pruebas 03, 06, gen2);
- mantener unido cada grupo de un rayo al elegir el corte, incluso si
  todos los huecos angulares son menores de media vuelta (prueba 06);
- un hueco de exactamente media vuelta, con calabazas a ambos lados de
  la calabaza 1 sobre una recta (pruebas 03, 09);
- la calabaza 1 en una esquina deja un hueco de más de media vuelta
  (pruebas 04, gen3, gen4).

## Soluciones optimizadas

Se ordenan claves enteras exactas de dirección, evitando productos cruzados repetidos. Un parámetro racional basado en la longitud Manhattan es monótono alrededor del origen. La cota de coordenadas garantiza una separación mínima entre fracciones distintas, por lo que escalar y truncar no fusiona direcciones. La clave incluye rango angular, distancia cuadrada e índice; los puntos del mismo rayo siguen de cerca a lejos. El hueco angular determina el mismo corte cíclico de la prueba simple, sin ángulos de coma flotante.

- `1444_geometry_optimized.cpp`: 0.015 s / 320 KB; base `1444_geometry.cpp`: 0.062 s / 444 KB; cambio respecto a la base: tiempo -75.8%, memoria -27.9%.
- `1444_geometry_optimized.go`: 0.031 s / 1188 KB; base `1444_geometry.go`: 0.078 s / 2336 KB; cambio respecto a la base: tiempo -60.3%, memoria -49.1%.
- `1444_geometry_optimized.java`: 0.093 s / 736 KB; base `1444_geometry.java`: 0.187 s / 6232 KB; cambio respecto a la base: tiempo -50.3%, memoria -88.2%.
- `1444_geometry_optimized.py`: 0.171 s / 3976 KB; base `1444_geometry.py`: 0.453 s / 11600 KB; cambio respecto a la base: tiempo -62.3%, memoria -65.7%.
- `1444_geometry_optimized.rs`: 0.046 s / 1244 KB; base `1444_geometry.rs`: 0.031 s / 2104 KB; cambio respecto a la base: tiempo +48.4%, memoria -40.9%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1444_geometry.cpp`; versión que cubre `1444_geometry_optimized.cpp`; puestos tiempo/memoria 1/10, registros de otros autores 352/352.

- Go: base didáctica preferida `1444_geometry.go`; versión que cubre `1444_geometry_optimized.go`; puestos tiempo/memoria 1/1, registros de otros autores 4/4.

- Java: base didáctica preferida `1444_geometry.java`; versión que cubre `1444_geometry_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 6/6.

- Python/PyPy: base didáctica preferida `1444_geometry.py`; versión que cubre `1444_geometry_optimized.py`; puestos tiempo/memoria 13/1, registros de otros autores 59/59.

- Rust: base didáctica preferida `1444_geometry.rs`; versión que cubre `1444_geometry_optimized.rs`; puestos tiempo/memoria 1/2, registros de otros autores 1/1.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1444_geometry.cpp](1444_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.062 s | 444 KB | 11286284 |
| [1444_geometry.go](1444_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.078 s | 2336 KB | 11286286 |
| [1444_geometry.java](1444_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.187 s | 6232 KB | 11286290 |
| [1444_geometry.py](1444_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.453 s | 11600 KB | 11286289 |
| [1444_geometry.rs](1444_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 2104 KB | 11286291 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1444_geometry_optimized.cpp](1444_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 320 KB | 11309261 |
| [1444_geometry_optimized.go](1444_geometry_optimized.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1188 KB | 11309263 |
| [1444_geometry_optimized.java](1444_geometry_optimized.java) | Java 1.8 | geometry | O(N log N) | AC | 0.093 s | 736 KB | 11309262 |
| [1444_geometry_optimized.py](1444_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(N log N) | AC | 0.171 s | 3976 KB | 11309260 |
| [1444_geometry_optimized.rs](1444_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.046 s | 1244 KB | 11309264 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
