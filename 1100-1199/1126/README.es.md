# 1126. El máximo de cada ventana de M lecturas consecutivas

[Timus 1126](https://acm.timus.ru/problem.aspx?space=1&num=1126) · dificultad 92 · two_pointers

Problema original de Alexander Mironenko, del sexto concurso universitario de programación de la Universidad Estatal de los Urales, 21 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados un ancho de ventana `M` (`2 ≤ M ≤ 14000`) y `N` lecturas
(`M ≤ N ≤ 25000`, cada una de 0 a 100000) terminadas en `-1`, imprime el
máximo de las lecturas `1..M`, luego de `2..M+1`, y así hasta la última
ventana completa.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`M`, luego las lecturas una por línea y luego `-1`.

## Salida

Los `N − M + 1` máximos de las ventanas, uno por línea.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
10
11
10
0
0
0
1
2
3
2
-1
```

Salida:

```
11
11
10
0
1
2
3
3
```

## Solución

Se mantiene una cola doble de índices cuyos valores decrecen del frente
al final. Una lectura nueva quita primero del final todo índice cuyo
valor no sea mayor que el suyo, porque ya no puede aumentar el máximo mientras la
nueva esté en la ventana; luego entra por el final. El frente sale cuando
queda fuera de la ventana. El frente de la cola es siempre el máximo de
la ventana actual. Cada índice entra y sale a lo sumo una vez, así que el recorrido
entero es `O(N)`; recalcular cada ventana costaría `O(N·M)`, hasta unos 156
millones de pasos.

Detalles a tener en cuenta:

- las lecturas terminan en `-1`, no se da su número;
- de varias lecturas iguales pueden quitarse del final todas salvo la más
  nueva, que sale la última de la ventana;
- con `M = N` hay una sola ventana.

Las respuestas se comprobaron con el máximo de cada ventana calculado
directamente, en todas las pruebas.

## Soluciones optimizadas

`1126_two_pointers_optimized.py`. Mantiene la deque monótona, codificando cada entrada como (value<<15)|index: con N<=25000 bastan 15 bits de índice. El orden entero compara primero valor y luego edad; una lectura igual más reciente sustituye a la antigua. Elimina la cabeza caducada y las colas dominadas, y obtiene el máximo con >>15. Cada entrada entra y sale una vez: O(N) amortizado y O(M) entradas. El lector de 4096 bytes conserva tokens parciales y escribe lotes de 512 respuestas. Las escrituras directas y os._exit(0) dentro de main evitan la limpieza normal. Conserva la base didáctica con parejas.

Accepted exacto Python 3.12 x64 #11327503: 0.093 s / 1452 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 2/54, memoria 2/54. Con 1024 KB o más la admisión estricta exige tiempo y memoria: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11326680 (Python 3.12 x64) era 0.109 s / 2152 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1126_two_pointers_optimized.py`: 0.093 s / 1452 KB; base didáctica conservada `1126_two_pointers.py`: 0.14 s / 3448 KB.

Accepted exacto CPython 3.12 #11326680: 0.109 s / 2152 KB. Comparación guardada 2026-11-20 de compiladores actuales: tiempo 6/54, memoria 4/54. Ambas métricas exigidas pasan diez primeros o 15% superior, redondeando el corte porcentual hacia arriba. El asterisco sigue la meta separada Python de primer puesto en ambas.

El envío optimizado documentado antes #11303710 (Python 3.12 x64) registró 0.125 s / 668 KB. El actual CPython 3.12 registra menor tiempo y mayor memoria. Son medidas emparejadas de ejecuciones distintas; la comparación incluye elección de intérprete y variabilidad del juez. La diferencia de 0.016 s frente al optimizado anterior es un solo tic; la selección se justifica por las clasificaciones guardadas.

Las soluciones optimizadas (C++, Java) no guardan las lecturas: cada una
entra en la cola doble junto con su índice en cuanto se lee, y el máximo de
una ventana completa se imprime enseguida. C++ lee con `getchar`; Java
analiza a mano un búfer de bytes, guarda la cola doble en un búfer circular
de `M` celdas, ya que la ventana nunca tiene más, y escribe los números a
través de un búfer de bytes. C++: 224 KB en lugar de 776 KB, con el
mismo tiempo; Java: 0.109 s en lugar de 0.156 s y 624 KB en lugar de
2332 KB.

Rust analiza los números a mano desde un búfer de 4 KB en lugar de leer
toda la entrada en una cadena, y escribe cada respuesta por una salida
con búfer en cuanto la conoce: 332 KB en lugar de 1192 KB, con el mismo
tiempo.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1126_two_pointers_parsing_implementation_optimized.go`. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios. Un búfer recargable de 8192 bytes sustituye el almacenamiento de toda la entrada, manteniendo tokens, lecturas parciales y fin de archivo.

Accepted #11328910 (Go 1.14 x64): **0.031 s / 2344 KB**. Comparación archivada: `1126_two_pointers.go` (Go 1.14 x64) — 0.062 s / 2896 KB (#11279328).

## Notas por lenguaje

- En las soluciones simples, Go y Java guardan la cola en un arreglo con
  un frente que avanza; C++, Rust y Python usan las colas dobles de su
  biblioteca.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1126_two_pointers.cpp](1126_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 776 KB | 11279323 |
| [1126_two_pointers.go](1126_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N) | AC | 0.062 s | 2896 KB | 11279328 |
| [1126_two_pointers.java](1126_two_pointers.java) | Java 1.8 | two_pointers | O(N) | AC | 0.156 s | 2332 KB | 11279331 |
| [1126_two_pointers.py](1126_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N) | AC | 0.140 s | 3448 KB | 11279329 |
| [1126_two_pointers.rs](1126_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.046 s | 1192 KB | 11279332 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1126_two_pointers_optimized.cpp](1126_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 224 KB | 11303561 |
| [1126_two_pointers_optimized.java](1126_two_pointers_optimized.java) | Java 1.8 | two_pointers | O(N) | AC | 0.109 s | 624 KB | 11303563 |
| [1126_two_pointers_optimized.py](1126_two_pointers_optimized.py) | Python 3.12 x64 | two_pointers | O(N) amortized; O(M) deque + bounded buffers | AC | 0.093 s | 1452 KB | 11327503 |
| [1126_two_pointers_optimized.rs](1126_two_pointers_optimized.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.031 s | 332 KB | 11303711 |
| [1126_two_pointers_parsing_implementation_optimized.go](1126_two_pointers_parsing_implementation_optimized.go) | Go 1.14 x64 | two_pointers, parsing, implementation | O(N) | AC | 0.031 s | 2344 KB | 11328910 |
