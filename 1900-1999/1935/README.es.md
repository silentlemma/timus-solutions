# 1935. Mínimo de hojas con separaciones reordenables

[Timus 1935](https://acm.timus.ru/problem.aspx?space=1&num=1935) · difficulty 80 · greedy

Original problem from Open Ural FU Championship 2012 | by Tatiana Sharypova (prepared by Oleg Dolgorukov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Colocar n objetos finos entre las hojas de un libro, en cualquier orden.
El objeto i necesita al menos a_i hojas hasta cada objeto vecino o tapa.
Un hueco compartido debe satisfacer ambos extremos. Hallar el número
mínimo total de hojas. Límites: 1 segundo, 64 MB.

## Entrada

Primero n, 1≤n≤100. Después n enteros a_i, 1≤a_i≤100.
El orden de entrada no obliga al orden de colocación.

## Salida

Un entero: la cantidad mínima suficiente de hojas.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3
5 10 3
```

```
28
```

## Solución

La respuesta es la suma de todos los requisitos más el mayor de ellos,
S + M.

No puede ser menos: tómese un objeto con el requisito mayor M. Cada
objeto a su izquierda necesita su propio hueco a la izquierda, cada
objeto a su derecha su propio hueco a la derecha, y el objeto mayor
necesita sus dos huecos. Son n + 1 huecos distintos, y juntos tienen al
menos S + M hojas.

Basta con eso: se ordenan los requisitos a₁ ≤ … ≤ aₙ y se colocan los
objetos en este orden, con a₁ hojas antes del primero, a_(i+1) hojas
entre los objetos i e i + 1, y aₙ después del último. Cada hueco tiene
lo que pide el mayor de sus vecinos, y el total es S + M. `O(n)`; el
programa no necesita ordenar.

Detalles a tener en cuenta:

- los vecinos comparten un hueco: hace falta el requisito mayor, no la
  suma;
- el orden de la entrada no importa: 100, 1, 100 necesita 301 hojas, no
  400;
- un solo objeto necesita 2a₁ hojas.

## Soluciones optimizadas

`1935_greedy_optimized.java`. Mantiene suma más máximo en una pasada y lector de 512 bytes. Solo serializa el resultado no negativo directamente en 21 bytes de cifras/salto, sin formato general de enteros. O(N) tiempo y espacio auxiliar fijo; no mezclar tiempo nuevo con memoria del registro anterior. Conserva enseñanza.

Accepted exacto Java 1.8 #11327748: 0.093 s / 344 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 5/171, memoria 4/171. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11302269 era 0.109 s / 340 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1935_greedy_optimized.java`: 0.093 s / 344 KB; base didáctica conservada `1935_greedy.java`: 0.109 s / 1720 KB.

La solución optimizada en C++ lee con `scanf` en lugar de `iostream` y
calcula la suma y el máximo mientras lee, sin guardar los requisitos:
124 KB en lugar de 428 KB.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

Conservar el algoritmo sencillo de suma más máximo y la entrada con búfer. Vaciar la salida antes de terminar directamente con os._exit(0), omitiendo la limpieza del intérprete. El envío aceptado 11324646 tardó 0.140 s y usó 200 KB. La versión sencilla tardó 0.078 s y usó 332 KB. El tiempo registrado es mayor que el de la versión sencilla.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1935_greedy.cpp](1935_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 428 KB | 11291786 |
| [1935_greedy.go](1935_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.015 s | 1092 KB | 11291790 |
| [1935_greedy.java](1935_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.109 s | 1720 KB | 11303361 |
| [1935_greedy.py](1935_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.078 s | 332 KB | 11291793 |
| [1935_greedy.rs](1935_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.015 s | 236 KB | 11291800 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1935_greedy_optimized.cpp](1935_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 124 KB | 11303651 |
| [1935_greedy_optimized.java](1935_greedy_optimized.java) \* | Java 1.8 | greedy | O(N) time; fixed buffers | AC | 0.093 s | 344 KB | 11327748 |
| [1935_greedy_optimized.py](1935_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(n) | AC | 0.140 s | 200 KB | 11324646 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
