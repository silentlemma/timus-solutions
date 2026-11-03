# 1551. Torneo de sumo

[Timus 1551](https://acm.timus.ru/problem.aspx?space=1&num=1551) · dificultad 257 · math, sorting

Problema original de Sergey Pupyrev, del XI Campeonato Universitario por Equipos de Programación de los Urales, Ekaterimburgo, 21 de abril de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un torneo por eliminación tiene 2ᴺ luchadores (1 ≤ N ≤ 10) y N rondas;
cada luchador representa una prefectura. Los organizadores eligen el
cuadro inicial. Hay que hallar el mayor K tal que algún cuadro garantiza,
sean cuales sean los resultados, al menos K rondas en las que no se
enfrentan dos luchadores de la misma prefectura.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego 2ᴺ líneas con el nombre de un luchador y su prefectura.
Ambos campos contienen entre 1 y 30 letras latinas.

## Salida

K.

## Evaluación

Comparar un token entero. Python pasó 168 distribuciones contra frecuencias hash independientes: mayúsculas, campos de 30 letras, grupos distintos/iguales y hasta 1024 luchadores.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
Homasho Ishikawa
Tamakasuga Tokyo
Futeno Tochigi
Takekaze Tokyo
Kasugao Yamaguchi
Kotoshogiku Ishikawa
Kotomitsuki Tokyo
Miyabiyama Shizuoka
```

Salida:

```
1
```

## Solución

En la ronda r el cuadro empareja bloques de 2^(r−1) luchadores, y como
de un bloque puede salir cualquiera, la ronda r es segura exactamente
cuando las dos mitades de cada bloque de 2^r no comparten prefectura.

Tomemos la prefectura mayor, con c luchadores, y hagamos que siempre
ganen contra luchadores de otras prefecturas. Solo los encuentros entre
ellos eliminan a sus integrantes, y cada ronda insegura puede reducir
su número como mucho a la mitad. Pasar de c a uno requiere al menos
⌈log₂ c⌉ rondas inseguras, por lo que K ≤ N − ⌈log₂ c⌉.

La cota se alcanza: con k = ⌈log₂ c⌉ para el mayor c, se ordenan los
luchadores por prefectura y se reparten por turnos en los 2ᵏ bloques de
los k niveles superiores. Una prefectura tiene como mucho 2ᵏ luchadores,
así que caen en bloques distintos; dentro de un bloque todos son de
prefecturas distintas, así que las primeras N − k rondas son seguras.
La respuesta es por tanto N − ⌈log₂ c⌉. Se cuentan los luchadores por
prefectura, se toma el máximo y se incrementa k desde cero hasta que
2ᵏ ≥ c; se imprime N − k. Un oráculo exhaustivo de cuadros y resultados
coincidió en las 29 distribuciones de multiplicidades para N ≤ 3 y en
1200 entradas aleatorias. `O(2ᴺ log 2ᴺ)` para contar.

Detalles a tener en cuenta:

- una sola prefectura no deja ninguna ronda segura (pruebas 02, 04);
- c = 4 necesita solo dos rondas inseguras, c = 5 tres (pruebas 06, 07);
- las prefecturas se comparan tal como están escritas, así que Tokyo y
  tokyo son distintas (prueba 08).
- los nombres no afectan al recuento; ambos campos deben contener
  1–30 letras latinas, sin sufijos numéricos (pruebas 04–07).

## Soluciones optimizadas

La respuesta sigue dependiendo de la mayor frecuencia c: `N−ceil(log2 c)`. C++/Java compactos descartan nombres de luchadores al leer y actualizan la frecuencia máxima; C++ mantiene map ordenado, Java un hash map y entrada de bytes acotada. Python guarda solo prefecturas, las ordena y toma la racha igual más larga: cada nombre forma exactamente un bloque de su frecuencia. Se eliminan Counter, tokens de luchadores y entradas de hash separadas. Python cambia hashing lineal esperado por ordenación `O(M log M)`, `M=2^N`, para ahorrar memoria medida; no afirma acelerar. Compara cadenas completas sensibles a mayúsculas, sin huellas probabilísticas. `bit_length(c−1)` da el techo exacto del logaritmo. Se conservan todas las bases, incluida Counter.

- `1551_math_optimized.cpp`: 0.015 s / 308 KB; base `1551_math.cpp`: 0.015 s / 544 KB; cambio respecto a la base: tiempo -0.0%, memoria -43.4%.
- `1551_math_optimized.java`: 0.093 s / 568 KB; base `1551_math.java`: 0.156 s / 3280 KB; cambio respecto a la base: tiempo -40.4%, memoria -82.7%.
- `1551_math_sorting.py`: 0.093 s / 464 KB; base `1551_math.py`: 0.062 s / 696 KB; cambio respecto a la base: tiempo +50.0%, memoria -33.3%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1551_math.cpp`; fuente que cubre `1551_math_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 47/47.

- Go: base didáctica preferida `1551_math.go`; fuente que cubre `1551_math.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1551_math.java`; fuente que cubre `1551_math_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 4/4.

- Python/PyPy: base didáctica preferida `1551_math.py`; fuente que cubre `1551_math_sorting.py`; puestos tiempo/memoria 61/4, registros de otros autores 139/139.

- Rust: base didáctica preferida `1551_math.rs`; fuente que cubre `1551_math.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1551_math.cpp](1551_math.cpp) | G++ 13.2 x64 | math | O(M log M) | AC | 0.015 s | 544 KB | 11287591 |
| [1551_math.go](1551_math.go) | Go 1.14 x64 | math | O(M) expected frequency work, M=2^N | AC | 0.031 s | 1276 KB | 11287592 |
| [1551_math.java](1551_math.java) | Java 1.8 | math | O(M) expected frequency work, M=2^N | AC | 0.156 s | 3280 KB | 11287596 |
| [1551_math.py](1551_math.py) | Python 3.12 x64 | math | O(M) expected frequency work, M=2^N | AC | 0.062 s | 696 KB | 11287594 |
| [1551_math.rs](1551_math.rs) | Rust 1.75 x64 | math | O(M) expected frequency work, M=2^N | AC | 0.046 s | 576 KB | 11287598 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1551_math_optimized.cpp](1551_math_optimized.cpp) | G++ 13.2 x64 | math | O(M log M) | AC | 0.015 s | 308 KB | 11309254 |
| [1551_math_optimized.java](1551_math_optimized.java) | Java 1.8 | math | O(M) expected frequency work, M=2^N | AC | 0.093 s | 568 KB | 11309256 |
| [1551_math_sorting.py](1551_math_sorting.py) \* | Python 3.12 x64 | math, sorting | O(M log M) time; O(M) strings | AC | 0.093 s | 464 KB | 11309558 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
