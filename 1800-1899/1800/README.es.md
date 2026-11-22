# 1800. La ley de Murphy

[Timus 1800](https://acm.timus.ru/problem.aspx?space=1&num=1800) · dificultad 169 · math

Problema original de Alex Samsonov, de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tostada, un segmento delgado de longitud l, cae desde la altura h
con la mantequilla hacia abajo, sostenida horizontal. Cae libremente
(g = 9,81 m/s²) y gira alrededor de su centro a ω revoluciones por
minuto en un plano vertical. ¿Qué lado toca primero el suelo? Se
garantiza que no lo toca estando vertical.

## Entrada

l y h en centímetros y ω en revoluciones por minuto, enteros de 1 a
1000.

## Salida

"butter" o "bread".

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 400 15
```

Salida:

```
butter
```

### Ejemplo 2

Entrada:

```
10 500 15
```

Salida:

```
bread
```

## Solución

Se convierten las longitudes a metros y ω a radianes por segundo.
Tras t segundos el centro está a h − g·t²/2 y la tostada ha girado
ω·t, así que su extremo inferior está a
gap(t) = h − g·t²/2 − (l/2)·|sin ωt|. La respuesta solo depende del
cuarto de vuelta en que gap llega a cero por primera vez: en los
cuartos 0 y 3 de una vuelta la mantequilla mira hacia abajo, en el 1 y
el 2 el pan. Así que se recorren los cuartos en orden.

En un cuarto par |sin ωt| crece, el extremo inferior baja más rápido
que el centro y gap solo decrece: la tostada toca en él exactamente
cuando gap ≤ 0 al final del cuarto. En un cuarto impar el extremo sube
respecto al centro, y gap puede bajar, luego subir y luego bajar de
nuevo. Su derivada ahí es cóncava, pues la tercera derivada es
(l/2)·ω³·cos ≤ 0. Se halla el pico de la derivada por bisección sobre
la segunda derivada. Si la derivada en el pico es positiva, una
segunda bisección encuentra dónde se vuelve positiva, el mínimo local
de gap. El cuarto contiene el primer contacto si ese mínimo o el valor
al final es como mucho cero. El centro llega al suelo en
aproximadamente 1,5 segundos, así que hay como mucho un centenar de
cuartos. `O(ω)`.

En el primer ejemplo la tostada gira un cuarto de vuelta por segundo y
cae tras unos 0,9 s, a unos 81°: mantequilla. Desde 5 m cae justo
pasados los 90°: pan.

Trampas:

- el extremo de la tostada puede tocar antes de que el centro haya
  caído mucho: una tostada larga sostenida baja toca en el primer
  cuarto (pruebas 05 y 06, ambas butter);
- en un cuarto impar gap no es monótona, así que su valor al final del
  cuarto puede perder un contacto;
- las unidades: centímetros a metros, revoluciones por minuto a
  radianes por segundo;
- los generadores usados por gen1, gen3 y gen4 también deben respetar la
  garantía de contacto no vertical. Con centímetros enteros y velocidad r
  en rpm, el primer contacto es vertical exactamente cuando
  (2h − l)·r² = 981·15²·n² para un entero positivo impar n. Se rechazan
  estos casos mediante aritmética entera exacta; no tienen un lado de
  salida especificado.

Las respuestas coinciden con un oráculo independiente que subdivide
intervalos de tiempo en 3000 entradas aleatorias (1500 pequeñas), 64
entradas límite, las nueve pruebas guardadas y los cinco casos de
generador configurados.

## Soluciones optimizadas

`1800_math_optimized.java`. Conserva búsqueda de contacto por cuartos y añade rama exacta si halfLength·omega²≤g. El extremo inferior desciende estrictamente: en cuartos impares la derivada es como máximo (−g·pi/2+halfLength·omega²)/omega<0; en pares es negativa directamente. Las raíces dan los primeros extremos vertical/horizontal no positivos; corrige índices evaluando alturas y toma el cuarto anterior. En los otros casos conserva búsqueda aceptada de altura/derivada y60bisecciones, sin reducir precisión. Rama rápida constante salvo correcciones del índice; alternativa O(Q·60), estado O(1). Lee tres datos con64bytes; escribe y vacía todo antes de Runtime.getRuntime().halt(0). Coinciden200000comparaciones con cálculo aceptado anterior,70212de rama rápida. Par actual0.093 s/512 KB más rápido pero con más memoria que histórico0.125 s/376 KB; no mezcla métricas. Conserva base de recorrido completo.

Accepted exacto Java 1.8 #11327885: 0.093 s / 512 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 5/32, memoria 6/32. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11307242 era 0.125 s / 376 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1800_math_optimized.java`: 0.093 s / 512 KB; base didáctica conservada `1800_math.java`: 0.109 s / 1576 KB.

`1800_math_optimized.py` se reutiliza byte por byte, sin otro archivo ni un algoritmo nuevo. Su Accepted de fuente exacto en CPython 3.12 #11327037 mide 0.078 s / 1008 KB. En el grupo guardado de compiladores actuales de la familia Python, 2026-11-20: puesto temporal 2/255, memoria 252/255. Al usar menos de 1024 KB, el criterio estricto de diez primeros o 15% superior usa solo tiempo; el asterisco conserva la meta de clasificación propia del lenguaje. El mismo archivo tiene también el Accepted anterior en PyPy 3.10 #11325886, 0.125 s / 412 KB. Son pares medidos en ejecuciones distintas: se elige el tiempo y puesto de CPython, mientras PyPy usa menos memoria. Las observaciones anteriores sobre ahorro de memoria en esta sección se refieren a esa medición PyPy, no a la fila CPython. Todos los fuentes didácticos siguen intactos.

`1800_math_optimized.py`. Conserva búsqueda por separación/pendiente/curvatura y60bisecciones. Extremo no toca antes de t₀=sqrt(2·max(0,h−l/2)/g), pues distancia vertical al centro≤l/2. Empieza un cuarto antes de floor(t₀/quarter), con margen de redondeo, saltando anteriores. Contacto ocurre como máximo en próximo extremo vertical; quedan cuartos próximos, con mínimos interiores/paridad absoluta butter/bread intactos. Sin importar control JIT PyPy. O(Q·60) para Q cuartos restantes, estado constante; conserva barrido completo sencillo.

Frente a `1800_math.py`: tiempo 0.093 s → 0.125 s; memoria 592 KB → 412 KB.

`1800_math_optimized.rs`. Mantiene búsqueda de contacto por cuartos de giro, con separación, pendiente y curvatura y mínimos interiores impares. Reduce bisecciones de 100 a 60: extremos positivos de esos intervalos difieren a lo sumo por factor dos, por lo que 60 pasos alcanzan resolución f64. Lee tres enteros acotados sin vector y emite butter/bread igual. O(Q·60) tiempo para Q cuartos, O(1) espacio; conserva versión didáctica de 100 pasos.

Frente a `1800_math.rs`: tiempo 0.046 s → 0.031 s; memoria 236 KB → 60 KB.

La solución optimizada en C++ lee los tres números con `scanf` e imprime
el lado con `puts` en lugar de usar `iostream`, cuyo entorno de
ejecución aquí sobra; el cálculo en coma flotante es exactamente el
mismo: {1800_math_optimized.cpp}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1800_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +73.12%; base: `1800_math.cpp`.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1800_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1800_math.cpp](1800_math.cpp) | G++ 13.2 x64 | math | O(omega) | AC | 0.015 s | 372 KB | 11304236 |
| [1800_math.go](1800_math.go) | Go 1.14 x64 | math | O(omega) | AC | 0.031 s | 1084 KB | 11289935 |
| [1800_math.java](1800_math.java) | Java 1.8 | math | O(omega) | AC | 0.109 s | 1576 KB | 11304238 |
| [1800_math.py](1800_math.py) | Python 3.12 x64 | math | O(omega) | AC | 0.093 s | 592 KB | 11289938 |
| [1800_math.rs](1800_math.rs) | Rust 1.75 x64 | math | O(omega) | AC | 0.046 s | 236 KB | 11304241 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1800_math_optimized.cpp](1800_math_optimized.cpp) | G++ 13.2 x64 | math | O(omega) | AC | 0.015 s | 100 KB | 11307243 |
| [1800_math_optimized.java](1800_math_optimized.java) \* | Java 1.8 | math | O(Q·60) fallback; O(1) state | AC | 0.093 s | 512 KB | 11327885 |
| [1800_math_optimized.rs](1800_math_optimized.rs) \* | Rust 1.75 x64 | math | O(Q·60) time; O(1) space | AC | 0.031 s | 60 KB | 11325533 |
| [1800_math_optimized.py](1800_math_optimized.py) \* | Python 3.12 x64 | math | O(Q·60) time; O(1) auxiliary state | AC | 0.078 s | 1008 KB | 11327037 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
