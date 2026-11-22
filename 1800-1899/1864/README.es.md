# 1864. Reunión en casa de Den

[Timus 1864](https://acm.timus.ru/problem.aspx?space=1&num=1864) · dificultad 177 · math

Problema original del folclore (preparado por Daniil Ayzenshteyn), del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n amigos fueron a casa de Den; el amigo i compró aᵢ litros de zumo, y
todos, Den incluido, bebieron lo mismo. Luego Den paga 100 rublos por
el zumo que bebió quien no lo había comprado, repartidos con justicia
entre los amigos que compraron más de lo que bebieron. ¿Cuántos rublos
recibe cada amigo, redondeando hacia abajo?

## Entrada

n (2 ≤ n ≤ 100), luego a₁, …, aₙ (0 ≤ aᵢ ≤ 100) con suma positiva.

## Salida

Los rublos de cada amigo, redondeados hacia abajo.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
10 10 10
```

Salida:

```
33 33 33
```

### Ejemplo 2

Entrada:

```
2
10 0
```

Salida:

```
100 0
```

## Solución

Con S litros en total, cada una de las n + 1 personas bebe S/(n + 1),
así que el amigo i compró para otros aᵢ − S/(n + 1) litros si eso es
positivo, y nada en otro caso. El dinero se reparte en proporción a
esas cantidades. Multiplicándolo todo por n + 1 todo queda en enteros:
eᵢ = max(0, aᵢ(n + 1) − S), y el amigo i recibe ⌊100·eᵢ / Σ e⌋. La suma
nunca es 0: los amigos compraron S entre todos y solo bebieron
nS/(n + 1). `O(n)`; Python tarda `O(n²)`.

En el primer ejemplo cada uno bebió 7,5 litros y cada amigo pagó
2,5 litros para Den, así que el dinero se reparte entre tres: 33 cada
uno tras redondear.

Trampas:

- Den también bebe, así que la parte es S/(n + 1), no S/n;
- los amigos que compraron menos de lo que bebieron no reciben nada;
- los enteros exactos evitan cualquier duda al redondear hacia abajo.

Los repartos coinciden con una implementación aceptada independiente en
doscientas reuniones aleatorias.

## Soluciones optimizadas

`1864_math_optimized.java`. Conserva normalización exacta c_i=max(0,a_i(N+1)−sum(a)), share_i=floor(100c_i/sum(c)). Analiza enteros directamente. Porcentaje 0..100 usa una a tres cifras más separador, hasta cuatro bytes por persona, y escribe una vez. Mismas contribuciones y división hacia abajo; no redondea para forzar suma 100. O(N) tiempo y O(N) espacio para contribuciones/salida. Conserva base.

Accepted exacto Java 1.8 #11327834: 0.093 s / 368 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 7/59, memoria 1/59. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11307325 era 0.125 s / 520 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1864_math_optimized.java`: 0.093 s / 368 KB; base didáctica conservada `1864_math.java`: 0.125 s / 1720 KB.

`1864_math_optimized.py`. Conserva créditos exactos max(0,(N+1)*bought[i]-total) y floor(100*credit[i]/sum(credits)). El total es positivo; antes de recortar, los créditos suman total, así que el denominador recortado es positivo. La aritmética entera evita redondeos. Tiempo O(N) calculando una sola vez el divisor común. El generador básico recalculaba sum(over) por amigo, con O(N²); ahora guarda la suma una vez. Compras, créditos y salida unida aún ocupan O(N). El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1864_math.py`: tiempo 0.093 s → 0.14 s; memoria 412 KB → 212 KB.

`1864_math_optimized.rs`. Conserva créditos exactos max(0,(N+1)*bought[i]-total) y floor(100*credit[i]/sum(credits)). El total es positivo; antes de recortar, los créditos suman total, así que el denominador recortado es positivo. La aritmética entera evita redondeos. Tiempo O(N) calculando una sola vez el divisor común. Reutiliza un arreglo fijo de100 i64 para compras y créditos, sin vectores separados ni cadenas de respuesta. Ocupa800bytes explícitos más estado constante; N<=100 y cantidades<=100 acotan productos. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1864_math.rs`: tiempo 0.031 s → 0.046 s; memoria 236 KB → 48 KB.

La solución optimizada en C++ calcula las mismas partes, pero guarda las
compras y los excedentes en dos arreglos fijos de 100 números,
suficientes porque `n ≤ 100`, en lugar de dos vectores en el montículo:
{1864_math_optimized.cpp}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1864_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +45.83%; base: `1864_math.cpp`.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1864_math_optimized.py`: puesto de tiempo 18/20 y de memoria 1/20 en esta muestra comparable.

`1864_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1864_math.cpp](1864_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 192 KB | 11304246 |
| [1864_math.go](1864_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1116 KB | 11290890 |
| [1864_math.java](1864_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1720 KB | 11290894 |
| [1864_math.py](1864_math.py) | Python 3.12 x64 | math | O(n²) | AC | 0.093 s | 412 KB | 11290893 |
| [1864_math.rs](1864_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 236 KB | 11304247 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1864_math_optimized.cpp](1864_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 104 KB | 11307321 |
| [1864_math_optimized.java](1864_math_optimized.java) \* | Java 1.8 | math | O(N) time and storage | AC | 0.093 s | 368 KB | 11327834 |
| [1864_math_optimized.py](1864_math_optimized.py) \* | PyPy 3.10 x64 | math | O(N) | AC | 0.14 s | 212 KB | 11325076 |
| [1864_math_optimized.rs](1864_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.046 s | 48 KB | 11325116 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
