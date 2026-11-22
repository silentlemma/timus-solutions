# 1642. Laberinto unidimensional

[Timus 1642](https://acm.timus.ru/problem.aspx?space=1&num=1642) · dificultad 96 · implementation

Problema original de Daniil Ayzenshteyn, del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una persona está en el 0 de una recta con obstáculos y una salida en x.
Camina en la dirección elegida, sale en cuanto llega a la salida y da la
vuelta en cada obstáculo. Para las dos direcciones iniciales, hacia
delante (creciente) y hacia atrás, hay que hallar la distancia recorrida
antes de salir, o decir que la salida es inalcanzable.

## Entrada

n y x (0 ≤ n ≤ 100), y luego n coordenadas distintas de obstáculos.
Todas las coordenadas son no nulas, de valor absoluto hasta 1000, y no
hay obstáculo en la salida. En cualquier dirección el camino encuentra
la salida o un obstáculo.

## Salida

Dos distancias, primero hacia delante, o `Impossible`.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 -2
-10 -4 2
```

Salida:

```
6 2
```

### Ejemplo 2

Entrada:

```
3 -2
10 -1 2
```

Salida:

```
Impossible
```

## Solución

Solo importan los obstáculos más cercanos: left, el mayor por debajo de
0 (o −∞ si no existe), y right, el menor por encima de 0 (o +∞ si no existe).
La salida es alcanzable exactamente cuando
left < x < right; si no, `Impossible`. En las dos direcciones el camino
es entonces directo o con un rodeo:

- x > 0: hacia delante x; hacia atrás hasta left y vuelta,
  2 · |left| + x;
- x < 0: hacia delante hasta right y vuelta, 2 · right + |x|; hacia
  atrás |x|.

El obstáculo necesario para el rodeo existe por la promesa del
enunciado. `O(n)`.

Detalles a tener en cuenta:

- un obstáculo entre el inicio y la salida bloquea las dos direcciones,
  así que una sola respuesta vale para ambas (el segundo ejemplo, la
  prueba 06);
- puede no haber ningún obstáculo del lado de la salida.

Las respuestas coinciden con una implementación aceptada independiente
en 300 rectas aleatorias.

## Soluciones optimizadas

`1642_implementation_optimized.py`. Conserva paredes más cercanas y distancias. Pared estrictamente entre cero y salida impide escapar, permitiendo terminar inmediatamente. Si no, ruta con un giro usa pared opuesta más cercana, garantizada por contrato. Lee/split entrada acotada completa, os.write y os._exit(0). O(N) tiempo, O(I) tokens y estado geométrico constante; a diferencia anterior no analiza en streaming acotado.

Accepted exacto Python 3.12 x64 #11327790: 0.078 s / 744 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 20/243, memoria 225/243. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11325697 era 0.156 s / 252 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1642_implementation_optimized.py`: 0.078 s / 744 KB; base didáctica conservada `1642_implementation.py`: 0.093 s / 504 KB.

`1642_implementation_optimized.java`. Java conserva el obstáculo más próximo a cada lado de cero y las mismas dos distancias. Un obstáculo estrictamente entre cero y la salida impide escapar definitivamente, así que imprime Impossible y retorna. En otro caso, para x>0 las distancias son x y x-2*left; para x<0, 2*right-x y -x. El obstáculo prometido en el lado contrario hace finito el desvío. El análisis de bytes con signo y la salida directa sustituyen Scanner y la concatenación. Tiempo máximo O(N), espacio auxiliar O(1), sin guardar una lista de obstáculos.

Accepted exacto Java 1.8 #11327458: 0.093 s / 416 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 4/83, memoria 6/83. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303629 era 0.125 s / 436 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1642_implementation_optimized.java`: 0.093 s / 416 KB; base didáctica conservada `1642_implementation.java`: 0.14 s / 1688 KB.

`1642_implementation_optimized.cpp`. Conserva la barrera más cercana a cada lado en una pasada y aplica las mismas fórmulas de accesibilidad y distancias. El análisis y la impresión manual de bytes de C sustituyen la conversión entera con formato, con intermedios de 64 bits con signo. Sin lista de obstáculos: O(n) tiempo y O(1) estado de trabajo explícito.

Frente a `1642_implementation.cpp`: tiempo 0.031 s → 0.015 s; memoria 124 KB → 72 KB.

`1642_implementation_optimized.rs`. Actualiza ambos límites de barrera al leer cada obstáculo, en vez de reunir la entrada y recorrer dos veces su vector. Las fórmulas de distancia no cambian. La entrada/salida numérica de C y dos límites dan O(n) tiempo y O(1) espacio auxiliar.

Frente a `1642_implementation.rs`: tiempo 0.031 s → 0.015 s; memoria 228 KB → 48 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1642_implementation.cpp](1642_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.031 s | 124 KB | 11303497 |
| [1642_implementation.go](1642_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1076 KB | 11288477 |
| [1642_implementation.java](1642_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1688 KB | 11288479 |
| [1642_implementation.py](1642_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 504 KB | 11288478 |
| [1642_implementation.rs](1642_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 228 KB | 11303498 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1642_implementation_optimized.java](1642_implementation_optimized.java) \* | Java 1.8 | implementation | O(N) time; O(1) auxiliary space | AC | 0.093 s | 416 KB | 11327458 |
| [1642_implementation_optimized.cpp](1642_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 72 KB | 11325060 |
| [1642_implementation_optimized.rs](1642_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 48 KB | 11324980 |
| [1642_implementation_optimized.py](1642_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N) time; O(I) token storage | AC | 0.078 s | 744 KB | 11327790 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
