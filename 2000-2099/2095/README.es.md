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

`2095_math_optimized.java`. Conserva eliminación exacta por bloques de cociente, avanzando juntos ambos prefijos; si coinciden devuelve cero. Si L=1, quiet(0)=0 y basta calcular prefijo superior. El salto común seguro usa comparación entera en lugar de Math.min. Cada paso elimina floor(c/k); agrupa j=floor((c−qk)/(2q))+1 pasos mientras q no cambia. O(R^(1/3)) tiempo, O(1) estado numérico. Consume ambos límites antes de reutilizar64bytes para respuesta decimal; vacía antes de Runtime.getRuntime().halt(0). Los45150intervalos1≤L≤R≤300 coinciden con oráculo independiente paso a paso;2000grandes con padre aceptado y1000pruebas I/O del main real. Pares actual0.093 s/464 KB e histórico0.125 s/320 KB separados: más rapidez cuesta más memoria. Conserva criba didáctica y demás lenguajes.

Accepted exacto Java 1.8 #11327888: 0.093 s / 464 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 5/44, memoria 1/44. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11309305 era 0.125 s / 320 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `2095_math_optimized.java`: 0.093 s / 464 KB; base didáctica conservada `2095_math.java`: 0.125 s / 1556 KB.

Se conserva el cribado paso a paso. Antes de k, c=qk+r. Tras jrestas de q, el cociente sigue q exactamente mientras 2 qj<=r; la desigualdad superior se relaja. Aplicar r//(2 q)+1 pasos: c-=q*j,k+=j. El siguiente cociente positivo disminuye. Por inducción de c<-c-floor(c/k), antes de k:(k-1)c<=N+(k-2)(k-1)/2. ParaK=ceil(N^(1/3))+1 hay menos deKpasos iniciales y después q<=K, como muchoKbloques: O(N^(1/3))tiempo/O(1)estado. Respuesta quiet(R)-quiet(L-1). Go usa E/S nativa portátil acotada. Java aplica los mismos bloques exactos. Python calcula cada prefijo por separado y obtiene a la vez el cociente y el resto con divmod. Todas las operaciones son enteras y exactas.

- `2095_math_optimized.go`: 0.015 s / 280 KB; base `2095_math.go`: 0.031 s / 1076 KB; cambio respecto a la base: tiempo -51.6%, memoria -74.0%.

- `2095_math_optimized.py`: 0.062 s / 368 KB; base `2095_math.py`: 0.078 s / 368 KB; cambio respecto a la base: tiempo -20.5%, memoria -0.0%.

`2095_math_optimized.rs`. Conserva la criba exacta de eliminación paso a paso para cada prefijo: c pasa a c-floor(c/k), aumentando k desde dos hasta c<k. Evalúa quiet(R)-quiet(L-1), incluido quiet(0)=0. Solo requiere dos variables de bucle por prefijo: O(√R) tiempo y O(1) estado auxiliar. Rust usa el entorno de C para entrada y salida, evitando cadenas String completas decodificadas y el formato de Rust. La fuente sencilla aceptada se conserva sin cambios.

Frente a `2095_math.rs`: tiempo 0.015 s → 0.031 s; memoria 204 KB → 52 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`2095_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

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
| [2095_math_optimized.java](2095_math_optimized.java) \* | Java 1.8 | math | O(R^(1/3)) time; O(1) numeric state | AC | 0.093 s | 464 KB | 11327888 |
| [2095_math_optimized.py](2095_math_optimized.py) | Python 3.12 x64 | math | O(R^(1/3)) time; O(1) numeric state | AC | 0.062 s | 368 KB | 11309302 |
| [2095_math_optimized.rs](2095_math_optimized.rs) \* | Rust 1.75 x64 | math | O(√R) | AC | 0.031 s | 52 KB | 11325120 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
