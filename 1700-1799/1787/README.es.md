# 1787. Giro hacia MEGA

[Timus 1787](https://acm.timus.ru/problem.aspx?space=1&num=1787) · dificultad 25 · simulation

Problema original de Bulat Zaynullin, del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un semáforo deja girar k coches por minuto. Durante el minuto i llegan
aᵢ coches nuevos al giro, que al principio estaba vacío. ¿Cuántos
coches esperan al cabo de n minutos?

## Entrada

k y n (1 ≤ k, n ≤ 100), luego a₁, …, aₙ (0 ≤ aᵢ ≤ 100).

## Salida

El número de coches que esperan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
6 7 2
```

Salida:

```
0
```

### Ejemplo 2

Entrada:

```
5 3
20 0 0
```

Salida:

```
5
```

## Solución

Se sigue el atasco minuto a minuto: se suman los coches nuevos, se
restan k, y si el resultado baja de cero el atasco simplemente está
vacío. `O(n)`.

En el primer ejemplo el atasco es 1, luego 3, luego 0, porque en el
último minuto solo hay 5 coches ante el semáforo. En el segundo es 15,
10, 5.

Trampas:

- el atasco no puede ser negativo: un minuto tranquilo no guarda
  capacidad para después, así que sumar todos los aᵢ y restar n·k es
  incorrecto;
- por la misma razón importa el orden: el primer ejemplo al revés,
  2 7 6, deja 3 coches en lugar de 0.

Las respuestas coinciden con una implementación aceptada independiente
en 150 casos aleatorios con cualquier número de coches y con números
cercanos a k.

## Soluciones optimizadas

`1787_simulation_optimized.java`. Java conserva la recurrencia de tráfico: añade las llegadas del minuto, resta la capacidad y limita la espera inferiormente a cero. Solo retiene ese contador; no guarda las llegadas ni acumula capacidad sin usar. Un búfer fijo de entrada de 256 bytes y salida decimal directa sustituyen Scanner y el formato general. Tiempo O(N), espacio auxiliar O(1). Los límites de minutos y llegadas garantizan que el contador cabe en int.

Accepted exacto Java 1.8 #11327468: 0.109 s / 316 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 65/755, memoria 5/755. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303638 era 0.125 s / 364 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1787_simulation_optimized.java`: 0.109 s / 316 KB; base didáctica conservada `1787_simulation.java`: 0.125 s / 1680 KB.

Las soluciones optimizadas (C++, Java) llevan la misma cuenta de la
cola. C++ lee y escribe con `scanf` y `printf` en lugar de `iostream`:
124 KB en lugar de 392 KB, con el mismo tiempo.

Consumir los recuentos de coches del iterador y guardar solo el número actual de coches en espera. El envío aceptado 11324248 tardó 0.125 s y usó 244 KB. La versión sencilla tardó 0.078 s y usó 420 KB. El tiempo registrado es mayor que el de la versión sencilla.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1787_parsing_optimized.go`. Se usa conversión directa por tipos con un búfer recargable de 256 bytes y salida compacta con escrituras completas. Los negativos se acumulan con signo, incluido el mínimo entero, sin reflexión de entrada ni despacho genérico de salida. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios. Los dígitos completos se convierten dentro del bloque, manteniendo local el cursor hasta un límite. La acumulación negativa admite el mínimo con signo y evita una rama o llamada por dígito, conservando EOF y signos opcionales.

Accepted #11329124 (Go 1.14 x64): **0.015 s / 796 KB**. Comparación archivada: `1787_simulation.go` (Go 1.14 x64) — 0.031 s / 1076 KB (#11289817).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1787_simulation.cpp](1787_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 392 KB | 11303509 |
| [1787_simulation.go](1787_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.031 s | 1076 KB | 11289817 |
| [1787_simulation.java](1787_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.125 s | 1680 KB | 11289820 |
| [1787_simulation.py](1787_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 420 KB | 11289819 |
| [1787_simulation.rs](1787_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.046 s | 248 KB | 11303511 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1787_simulation_optimized.cpp](1787_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 124 KB | 11303637 |
| [1787_simulation_optimized.java](1787_simulation_optimized.java) | Java 1.8 | simulation | O(N) time; O(1) auxiliary space | AC | 0.109 s | 316 KB | 11327468 |
| [1787_simulation_optimized.py](1787_simulation_optimized.py) \* | PyPy 3.10 x64 | simulation | O(n) | AC | 0.125 s | 244 KB | 11324248 |
| [1787_parsing_optimized.go](1787_parsing_optimized.go) | Go 1.14 x64 | parsing | O(n) | AC | 0.015 s | 796 KB | 11329124 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
