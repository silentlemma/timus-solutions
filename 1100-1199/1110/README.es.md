# 1110. Todos los restos cuya potencia N-ésima da resto Y

[Timus 1110](https://acm.timus.ru/problem.aspx?space=1&num=1110) · dificultad 53 · bruteforce

Problema original de la Olimpiada Nacional Búlgara de Informática, primer día.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados `N`, `M` e `Y` (`0 < N < 999`, `1 < M < 999`, `0 < Y < 999`), halla
todos los enteros `X` de `[0, M − 1]` con `X^N mod M = Y`.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N M Y` en una línea.

## Salida

Todos esos `X` en orden creciente, separados por espacios, o `-1` si no
hay ninguno.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 6 4
```

Salida:

```
2 4
```

## Solución

Hay menos de mil candidatos, así que se prueba cada `X` y se calcula
`X^N mod M` por exponenciación rápida, reduciendo módulo `M` tras cada
multiplicación. `O(M log N)`.

Detalles a tener en cuenta:

- `Y` puede ser `M` o mayor; un resto nunca lo es, y entonces la
  respuesta es `-1`;
- `X^N` es enorme: se reduce en cada paso, y los productos quedan por
  debajo de `M²`, que cabe en 32 bits;
- con `N = 1` la respuesta es solo `Y` siempre que `Y < M`.

Las respuestas se comprobaron con la multiplicación repetida simple, `N`
multiplicaciones para cada `X`.

## Soluciones optimizadas

`1110_bruteforce_optimized.java`. Java conserva la búsqueda exhaustiva de raíces modulares por cuadrados sucesivos, pero empareja x con M-x: sus potencias son iguales si N es par y opuestas módulo M si es impar. Una exponenciación comprueba ambos residuos; trata el cero aparte y Y>=M no tiene raíces. Un arreglo booleano marca las raíces y un búfer de bytes acotado las emite en orden creciente, o -1. Con M<999 cada raíz usa como máximo tres cifras, así que bastan 4*M bytes de respuesta. Tiempo O(M log N), espacio auxiliar O(M). Conserva el análisis directo de enteros; no introduce tablas de respuestas ni otro método teórico de raíces.

Accepted exacto Java 1.8 #11327344: 0.078 s / 304 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/228, memoria 1/228. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Ambas métricas son primeras; cumple también la meta propia del lenguaje, sin asterisco. El registro optimizado documentado antes #11303558 era 0.109 s / 412 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1110_bruteforce_optimized.java`: 0.078 s / 304 KB; base didáctica conservada `1110_bruteforce.java`: 0.109 s / 1568 KB.

`1110_bruteforce_optimized.py`. Mantiene la enumeración exhaustiva mediante potencias modulares. Agrupa raíces crecientes en una salida, sin print por raíz; conserva -1 si no hay. Vacía antes de salir directamente. No cambia pruebas ni base, sin test probabilístico de raíces.

Accepted exacto CPython 3.12 #11327010: 0.062 s / 656 KB. Comparación guardada 2026-11-20 con compiladores actuales de la familia: tiempo 4/147, memoria 118/147. Por debajo de 1024 KB, admisión estricta solo por tiempo.

- `1110_bruteforce_optimized.py`: 0.062 s / 656 KB; base didáctica conservada `1110_bruteforce.py` (Python 3.12 x64): 0.078 s / 352 KB; cambio de tiempo -20.5%; cambio de memoria +86.4%.

La solución optimizada en C++ imprime cada raíz en cuanto la encuentra en
lugar de juntar las raíces en un vector: 128 KB en lugar de 196 KB, con
el mismo tiempo.

## Notas por lenguaje

- Python usa el `pow` de tres argumentos incorporado; los demás lenguajes
  llevan una pequeña función de potencia.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1110_bruteforce.cpp](1110_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(M log N) | AC | 0.015 s | 196 KB | 11279202 |
| [1110_bruteforce.go](1110_bruteforce.go) | Go 1.14 x64 | bruteforce | O(M log N) | AC | 0.015 s | 1104 KB | 11279203 |
| [1110_bruteforce.java](1110_bruteforce.java) | Java 1.8 | bruteforce | O(M log N) | AC | 0.109 s | 1568 KB | 11279205 |
| [1110_bruteforce.py](1110_bruteforce.py) | Python 3.12 x64 | bruteforce | O(M log N) | AC | 0.078 s | 352 KB | 11279204 |
| [1110_bruteforce.rs](1110_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(M log N) | AC | 0.015 s | 212 KB | 11279206 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1110_bruteforce_optimized.cpp](1110_bruteforce_optimized.cpp) | G++ 13.2 x64 | bruteforce | O(M log N) | AC | 0.015 s | 128 KB | 11303557 |
| [1110_bruteforce_optimized.java](1110_bruteforce_optimized.java) | Java 1.8 | bruteforce | O(M log N) time; O(M) auxiliary space | AC | 0.078 s | 304 KB | 11327344 |
| [1110_bruteforce_optimized.py](1110_bruteforce_optimized.py) \* | Python 3.12 x64 | bruteforce | O(M log N) | AC | 0.062 s | 656 KB | 11327010 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
