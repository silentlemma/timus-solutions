# 2026. Maximizar una suma alternada de letras

[Timus 2026](https://acm.timus.ru/problem.aspx?space=1&num=2026) · dificultad 594 · greedy

Problema original de Alexey Danilyuk, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sustituye cada `?` por una letra inglesa minúscula, conservando las
letras ya fijadas. El resultado debe tener al menos `k` letras
distintas. El valor de una letra es su posición alfabética, de `a = 1` a
`z = 26`. La calidad es la suma en posiciones impares menos la suma en
posiciones pares, numerando desde uno. Imprime cualquier solución de
calidad máxima o indica que no se puede cumplir el número de letras
distintas.

Límites: longitud `1 ≤ n ≤ 100000`, `1 ≤ k ≤ 26`, 1 segundo, 64 MB. La
calidad puede ser negativa.

## Entrada

La primera línea es el patrón de minúsculas e interrogantes; la segunda
contiene `k`.

## Salida

Imprime una cadena completa óptima, o `-1` si es imposible. Se imprime
la cadena, no su calidad. Una cadena válida de calidad −1 también debe
imprimirse.

## Evaluación

Un comprobador verifica las letras, las posiciones fijas y el número de
letras distintas y compara la calidad con el óptimo; se acepta cualquier
compleción óptima.

## Ejemplos

```
??
1
```

```
za
```

```
??
3
```

```
-1
```

```
aza
1
```

```
aza
```

```
aza
3
```

```
-1
```

## Solución

Sean `F` las letras ya fijadas y `P`, `M` los huecos positivos y
negativos. Con índices desde cero, los pares son positivos. Faltan `r =
max(0, k-|F|)` letras distintas. Como `k ≤ 26`, hay al menos `r` letras
ausentes. La factibilidad equivale a `P+M ≥ r`: cada nueva letra
necesita un hueco diferente, y suficientes huecos permiten colocarlas.

Sin exigir diversidad, rellena los huecos positivos con `z` y los
negativos con `a`. Esta base tiene calidad máxima sin restricciones.
Reemplazar por un valor `c` pierde `26-c` en un positivo o `c-1` en un
negativo; todas las pérdidas son no negativas.

Ordena los valores ausentes de menor a mayor. Para representar `x` letras nuevas
en positivos, la menor pérdida usa los `x` valores ausentes mayores; para `y` en
negativos, los `y` menores. Precalcula sus costes prefijos `high[x]` y `low[y]`.
Prueba `max(0,r-M) ≤ x ≤ min(r,P)`, con `y = r-x`, minimizando `high[x]+low[y]`.

Rellena la base y coloca los `x` valores mayores en distintos huecos positivos,
y los `y` menores en distintos negativos. Los dos conjuntos son disjuntos porque
suman `r` elementos, como máximo el número de letras ausentes. Los demás huecos
mantienen la base. Cualquier empate entre valores de `x` sirve.

Para demostrarlo, toma cualquier solución válida y elige `r` tipos
ausentes de `F`, con un hueco representante de cada uno. Sean `x`
positivos e `y` negativos. Su coste no supera la pérdida total, porque
los demás costes son no negativos. Los positivos cuestan al menos
`high[x]` y los negativos al menos `low[y]`. Toda solución pierde al
menos el mínimo enumerado. Ambas cotas se alcanzan simultáneamente: los
`x` mayores y los `y` menores ausentes son disjuntos. Nuestra
construcción alcanza la cota e introduce `r` tipos, así que es
globalmente óptima. La base puede añadir más tipos; se exige al menos
`k`, no exactamente `k`.

En el primer ejemplo `za` tiene calidad `26-1 = 25`, el máximo sin
restricciones; se permiten dos letras con `k = 1`. En el segundo, dos
posiciones no admiten tres tipos. En el tercero solo cabe la cadena
fija, de calidad `1-26+1 = -24`. En el cuarto esa cadena contiene solo
dos tipos y resulta imposible.

Con alfabeto `σ = 26`, tiempo y espacio son `O(n + σ)`, es decir, `O(n)`.
Se guardan índices de huecos y la respuesta; los prefijos tienen longitud `σ+1`.
Otra opción es la DP del verificador: omitir cada letra ausente o representarla
en un signo disponible, manteniendo los dos números de representantes.

Trampas:

- Cuenta solo letras fijas en `F`: las `a` y `z` de la base pueden
  sobrescribirse.
- Conserva las posiciones fijas y distingue los signos de los índices
  desde cero.
- No exijas exactamente `k` tipos ni una cadena óptima concreta.
- Con `r = 0`, usa la base; una calidad fija negativa puede ser válida.
- `ab` con `k = 2` es viable con calidad −1: la salida es `ab`, no `-1`.

## Notas por lenguaje

Bastan enteros ordinarios. C++, Go y Rust usan vectores o slices para
los índices; Java usa arrays enteros. Go y Rust procesan bytes ASCII,
Python caracteres. La lectura con búfer admite 100000 caracteres; Go usa
`fmt.Fscan`, sin el límite predeterminado de Scanner. CPython no
necesita un entorno alternativo.

## Soluciones optimizadas

La versión en C++ cuenta primero las posiciones libres de cada paridad. Una vez elegida la distribución voraz, una segunda pasada rellena el mismo búfer de caracteres y toma las letras que faltan del extremo correspondiente del alfabeto. El tiempo es O(n + σ), el búfer de entrada y salida ocupa O(n) y el espacio adicional es O(σ). Las métricas corresponden al envío 11316965.

La versión en Rust también cuenta las posiciones libres por paridad y completa el búfer de entrada en el mismo sitio. El tiempo es O(n + σ) y usa O(σ) espacio adicional aparte del búfer. Las métricas corresponden al envío 11317093.

La versión en Java cuenta los huecos por paridad y completa un solo búfer de bytes en el mismo sitio. El envío 11317096 usó 628 KB en vez de 2448 KB y tardó 0.125 s en vez de 0.109 s.

La versión en Python también cuenta las posiciones libres por paridad y rellena un arreglo de bytes sin copiarlo. El tiempo es O(n + σ) y usa O(σ) espacio adicional aparte del búfer. Las métricas corresponden al envío 11317086.

La versión en Go también cuenta las posiciones libres por paridad y completa el búfer de entrada en el mismo sitio. El tiempo es O(n + σ) y usa O(σ) espacio adicional aparte del búfer. Las métricas corresponden al envío 11317080.

**Envíos de las versiones sencillas en Timus**

Java 1.8 №11317029.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2026_greedy.cpp](2026_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 1008 KB | 11322047 |
| [2026_greedy.go](2026_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 6072 KB | 11322049 |
| [2026_greedy.java](2026_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.109 s | 2448 KB | 11317029 |
| [2026_greedy.py](2026_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.109 s | 5432 KB | 11322050 |
| [2026_greedy.rs](2026_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.031 s | 2088 KB | 11322051 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2026_greedy_optimized.cpp](2026_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n + σ) | AC | 0.015 s | 204 KB | 11316965 |
| [2026_greedy_optimized.go](2026_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(n + σ) | AC | 0.031 s | 1172 KB | 11317080 |
| [2026_greedy_optimized.py](2026_greedy_optimized.py) | Python 3.12 x64 | greedy | O(n + σ) | AC | 0.093 s | 800 KB | 11317086 |
| [2026_greedy_optimized.rs](2026_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(n + σ) | AC | 0.046 s | 456 KB | 11317093 |
| [2026_greedy_optimized.java](2026_greedy_optimized.java) | Java 1.8 | greedy | O(n + σ) | AC | 0.125 s | 628 KB | 11317096 |

\* Aceptada. Aún queda por alcanzar el objetivo de clasificación de Go. Aceptada. Aún queda por alcanzar el objetivo de clasificación de Rust.
