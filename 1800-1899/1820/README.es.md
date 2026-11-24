# 1820. Filetes de los Urales

[Timus 1820](https://acm.timus.ru/problem.aspx?space=1&num=1820) · dificultad 25 · math

Problema original de Magaz Asanov, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que freír ambos lados de n filetes, un minuto por lado, en una
sartén que admite como mucho k filetes a la vez. Hallar el menor número
de minutos.

## Entrada

n y k (1 ≤ n, k ≤ 1000).

## Salida

El menor número de minutos.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2
```

Salida:

```
3
```

## Solución

Hay 2n lados y cada minuto se fríen como mucho k, así que hacen falta
al menos ⌈2n/k⌉ minutos; y los dos lados de un filete no pueden
freírse en el mismo minuto, así que al menos 2. La respuesta es
max(2, ⌈2n/k⌉), y se alcanza: se listan los lados como cara 1, …,
cara n, dorso 1, …, dorso n y cada minuto se fríen los k siguientes.
Con n ≥ k los dos lados de un filete distan n en la lista y nunca
coinciden en un minuto; con n < k ambos lados caben en dos minutos de
todos modos. `O(1)`.

En el ejemplo: caras 1 y 2, luego dorso 1 con cara 3, luego dorsos 2
y 3: tres minutos.

Trampas:

- freír tandas completas de k filetes durante dos minutos desperdicia
  la sartén: 3 filetes en una sartén para 2 tardan 3 minutos, no 4;
- con k ≥ 2n la cota ⌈2n/k⌉ vale 1, pero un filete sigue necesitando
  dos minutos.

## Soluciones optimizadas

`1820_math_optimized.py`. Python conserva max(2,ceil(2N/K)). Si N<=K, dos minutos son necesarios y suficientes; si no, el techo ya es al menos tres y calcula (2*N+K-1)//K sin max. Las dos caras siguen necesitando minutos distintos. Entrada binaria, una escritura directa y salida dentro de main sustituyen print/flush y limpieza normal. No introduce tablas ni otro algoritmo de planificación. Tiempo y estado auxiliar O(1) en los límites indicados; conserva las bases.

Accepted exacto Python 3.12 x64 #11327556: 0.078 s / 736 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 22/591, memoria 583/591. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11324829 (PyPy 3.10 x64) era 0.125 s / 216 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1820_math_optimized.py`: 0.078 s / 736 KB; base didáctica conservada `1820_math.py`: 0.093 s / 348 KB.

`1820_math_optimized.java`. Java conserva max(2,ceil(2N/K)), calculado exactamente como max(2,(2*N+K-1)/K). Cada filete necesita dos minutos distintos y la sartén procesa como máximo K de las 2N caras por minuto. Se conservan la justificación matemática y la base didáctica. Búferes fijos de bytes y salida decimal directa sustituyen las llamadas por carácter y el formato general. En los límites indicados, tiempo y espacio auxiliar O(1).

Accepted exacto Java 1.8 #11327469: 0.109 s / 400 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 53/779, memoria 1/779. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303779 era 0.125 s / 348 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1820_math_optimized.java`: 0.109 s / 400 KB; base didáctica conservada `1820_math.java`: 0.14 s / 1608 KB.

`1820_math_optimized.cpp`. Conserva max(2,ceil(2N/K)): cada filete necesita dos minutos distintos y caben como máximo K de las 2N caras por minuto. La conversión explícita de bytes de C sustituye el formato entero, usando intermedios de 64 bits con signo para redondear hacia arriba exactamente. Tiempo y estado auxiliar O(1).

Frente a `1820_math.cpp`: tiempo 0.031 s → 0.015 s; memoria 124 KB → 72 KB.

`1820_math_optimized.go`. Mantiene la misma cota y construcción de cocción. Flujos portátiles de bytes os.File y búferes acotados sustituyen fmt; calcula el techo con int64. Solo retiene las dos entradas y la respuesta, con O(1) tiempo y almacenamiento auxiliar fijo.

Frente a `1820_math.go`: tiempo 0.046 s → 0.031 s; memoria 1076 KB → 824 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1820_math.cpp](1820_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 124 KB | 11303517 |
| [1820_math.go](1820_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1076 KB | 11290244 |
| [1820_math.java](1820_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1608 KB | 11290247 |
| [1820_math.py](1820_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 348 KB | 11290246 |
| [1820_math.rs](1820_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB | 11303518 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1820_math_optimized.java](1820_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 400 KB | 11327469 |
| [1820_math_optimized.cpp](1820_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 72 KB | 11325061 |
| [1820_math_optimized.go](1820_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 824 KB | 11328310 |
| [1820_math_optimized.py](1820_math_optimized.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 736 KB | 11327556 |
