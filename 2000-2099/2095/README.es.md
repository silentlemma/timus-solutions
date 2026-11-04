# 2095. Contar los días que conserva una criba repetida

[Timus 2095](https://acm.timus.ru/problem.aspx?space=1&num=2095) · dificultad 277 · math

Problema original de Dmitry Ivankov, del Concurso Individual Abierto de la UrFU 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los días se numeran 1, 2, 3, … Cada segundo día es de informe; de los
que quedan, cada tercero es de informe; de los que quedan, cada cuarto,
y así para siempre. Los días que nunca se quitan son tranquilos. Contar
los días tranquilos de [l; r]. Los límites son 1 segundo y 64 MB.

## Entrada

l y r, 1 ≤ l ≤ r ≤ 10⁹.

## Salida

El número de días tranquilos de l a r.

## Evaluación

Tokens exactos. Cada fuente nueva tiene pruebas completas del entorno destino, comparaciones matemáticas independientes y Accepted propio ligado al hash; las bases conservan sus propias medidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 10
```

Salida:

```
3
```

## Solución

Sea f(n) el número de días tranquilos entre los n primeros. Las
eliminaciones siempre toman posiciones de la lista de días restantes,
así que entre los c primeros días restantes el paso k quita exactamente
⌊c / k⌋, y los días restantes entre los n primeros siguen siendo un
prefijo de la lista. Por tanto f(n) se obtiene con c ← c − ⌊c / k⌋ para
k = 2, 3, … mientras c ≥ k; cuando c < k ningún paso posterior toca el
prefijo. El número c decrece más o menos como n / k, así que el bucle
acaba tras unos 2√(n/π) pasos, unos 3.6·10⁴ para 10⁹. La respuesta es
f(r) − f(l − 1).

En el ejemplo f(10): 10 → 5 → 4 → 3, y los días tranquilos son 1, 3
y 7.

## Soluciones optimizadas

Se conserva el cribado paso a paso. Antes de k, c=qk+r. Tras jrestas de q, el cociente sigue q exactamente mientras 2 qj<=r; la desigualdad superior se relaja. Aplicar r//(2 q)+1 pasos: c-=q*j,k+=j. El siguiente cociente positivo disminuye. Por inducción de c<-c-floor(c/k), antes de k:(k-1)c<=N+(k-2)(k-1)/2. ParaK=ceil(N^(1/3))+1 hay menos deKpasos iniciales y después q<=K, como muchoKbloques: O(N^(1/3))tiempo/O(1)estado. Respuesta quiet(R)-quiet(L-1). Go usa E/S nativa portátil acotada. Java aplica los mismos bloques exactos. Python calcula cada prefijo por separado y obtiene a la vez el cociente y el resto con divmod. Todas las operaciones son enteras y exactas.

- `2095_math_optimized.go`: 0.015 s / 280 KB; base `2095_math.go`: 0.031 s / 1076 KB; cambio respecto a la base: tiempo -51.6%, memoria -74.0%.
- `2095_math_optimized.java`: 0.125 s / 320 KB; base `2095_math.java`: 0.125 s / 1556 KB; cambio respecto a la base: tiempo -0.0%, memoria -79.4%.
- `2095_math_optimized.py`: 0.062 s / 368 KB; base `2095_math.py`: 0.078 s / 368 KB; cambio respecto a la base: tiempo -20.5%, memoria -0.0%.

## Notas por lenguaje

Las instantáneas se guardaron el 1 y el 4 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `2095_math.cpp`; fuente que cubre `2095_math.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 38/38.

- Go: base didáctica preferida `2095_math.go`; fuente que cubre `2095_math_optimized.go`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Java: base didáctica preferida `2095_math.java`; fuente que cubre `2095_math_optimized.java`; puestos tiempo/memoria 2/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `2095_math.py`; fuente que cubre `2095_math_optimized.py`; puestos tiempo/memoria 1/1, registros de otros autores 60/60.

- Rust: base didáctica preferida `2095_math.rs`; fuente que cubre `2095_math.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2095_math.cpp](2095_math.cpp) | G++ 13.2 x64 | math | O(sqrt r) | AC | 0.015 s | 108 KB | 11309238 |
| [2095_math.go](2095_math.go) | Go 1.14 x64 | math | O(sqrt r) | AC | 0.031 s | 1076 KB | 11294664 |
| [2095_math.java](2095_math.java) | Java 1.8 | math | O(sqrt r) | AC | 0.125 s | 1556 KB | 11309239 |
| [2095_math.py](2095_math.py) | Python 3.12 x64 | math | O(sqrt r) | AC | 0.078 s | 368 KB | 11294665 |
| [2095_math.rs](2095_math.rs) | Rust 1.75 x64 | math | O(sqrt r) | AC | 0.015 s | 204 KB | 11309240 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2095_math_optimized.go](2095_math_optimized.go) | Go 1.14 x64 | math | O(R^(1/3)) time; O(1) numeric state | AC | 0.015 s | 280 KB | 11309760 |
| [2095_math_optimized.java](2095_math_optimized.java) \* | Java 1.8 | math | O(R^(1/3)) time; O(1) numeric state | AC | 0.125 s | 320 KB | 11309305 |
| [2095_math_optimized.py](2095_math_optimized.py) | Python 3.12 x64 | math | O(R^(1/3)) time; O(1) numeric state | AC | 0.062 s | 368 KB | 11309302 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
