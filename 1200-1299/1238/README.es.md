# 1238. Plegar una cadena con contadores de repetición

[Timus 1238](https://acm.timus.ru/problem.aspx?space=1&num=1238) · dificultad 416 · dp

Problema original de Roman Elizarov, del concurso regional ACM ICPC del noreste de Europa 2002–2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una secuencia plegada es una letra, dos secuencias plegadas escritas una
tras otra, o `X(S)` para una secuencia plegada S y un entero X > 1, que
significa S repetida X veces. Dada una cadena de 1 a 100 letras
mayúsculas, hay que imprimir una secuencia plegada lo más corta posible
que se despliegue en ella.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La cadena.

## Salida

Una secuencia plegada mínima; sirve cualquiera.

## Evaluación

Puede haber varios plegados igual de cortos, así que el verificador
despliega la respuesta, la compara con la entrada y compara su longitud
con la longitud mínima.

## Ejemplos

### Ejemplo 1

Entrada:

```
AAAAAAAAAABABABCCD
```

Salida:

```
9(A)3(AB)CCD
```

### Ejemplo 2

Entrada:

```
NEERCYESYESYESNEERCYESYESYES
```

Salida:

```
2(NEERC3(YES))
```

## Solución

Sea `best[i][j]` la longitud del plegado más corto de `s[i..j]`. Su nivel
superior es una concatenación, y entonces se parte en dos plegados más
cortos en algún punto k, o un único `X(S)`, y entonces el tramo es el
despliegue de S repetido X veces. Eso da la PD por intervalos, por
longitud creciente:

- `best[i][j] = min(best[i][k−1] + best[k][j])` sobre los puntos de corte;
- para cada divisor p < longitud de la longitud del tramo tal que el
  tramo tenga periodo p, además `cifras(longitud/p) + 2 + best[i][i+p−1]`.

El tramo tiene periodo p justo cuando coincide consigo mismo desplazado
p: `s[i..j−p] = s[i+p..j]`. Cada intervalo recuerda su elección y el
plegado se reconstruye desde arriba. Para un intervalo de longitud L,
cada divisor propio p requiere comparar L−p caracteres en el peor caso.
La suma sobre todos los intervalos y divisores cuesta `O(n³ log n)` tiempo;
la PD usa `O(n²)` espacio, con n ≤ 100.

Detalles a tener en cuenta:

- los contadores pueden tener dos o tres cifras, y su longitud cuenta:
  `100(A)` y `A99(A)` son igual de cortos (prueba 04);
- la parte interior de una repetición también se pliega, como en
  `2(NEERC3(YES))`;
- comparar subcadenas no cuesta tiempo constante: las cadenas de letras
  iguales (prueba 04) requieren una comparación completa para cada divisor
  propio, lo que aporta el factor logarítmico en el peor caso.

La versión didáctica en Python memoriza el texto plegado más corto de cada subcadena. Parte del texto literal, prueba todos los cortes y todos los bloques cuya repetición reproduce el texto, y conserva la codificación más corta contando los dígitos y paréntesis. El resultado de la entrada ya se puede imprimir. Para N caracteres, copiar, calcular hashes y comparar cadenas cuesta O(N⁴) tiempo, y guardar las cadenas requiere O(N³) espacio en el peor caso.

## Soluciones optimizadas

Las nuevas versiones C++ y Go mantienen la DP por intervalos y precalculan el prefijo común más largo de cada par de sufijos. Un intervalo de longitud L admite período p exactamente si p divide L y LCP[left][left+p]≥L−p: comprobación O(1). Se prueban cortes y períodos, contando los dígitos decimales y los dos paréntesis de cada repetición. Tiempo O(n³) y espacio O(n²). Para n≤100, longitudes y LCP caben en bytes; decisiones con signo codifican un corte positivo, un período negativo o cero para texto literal. La salida reconstruida tiene como máximo 100 caracteres. Se conservan las bases; Java, Python y Rust reutilizan las ya admitidas en el conjunto rápido.

Las implementaciones base aceptadas [1238_dp.java](1238_dp.java), [1238_dp.py](1238_dp.py), [1238_dp.rs](1238_dp.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1238_dp_optimized.rs`. Se precalculan prefijos comunes máximos, divisores de longitudes y cifras decimales. Cada periodo usa una comparación LCP y las transiciones no crean cadenas numéricas temporales. Tiempo O(n³), espacio O(n²); reconstrucción sin cambios.

Accepted #11328694 (Rust 1.75 x64): **0.031 s / 348 KB**. Comparación archivada: `1238_dp.rs` (Rust 1.75 x64) — 0.046 s / 316 KB (#11283818).

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes comparan las subcadenas desplazadas con una sola
  llamada de biblioteca.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1238_dp.cpp](1238_dp.cpp) | G++ 13.2 x64 | dp | O(n³ log n) | AC | 0.031 s | 460 KB | 11283813 |
| [1238_dp.go](1238_dp.go) | Go 1.14 x64 | dp | O(n³ log n) | AC | 0.031 s | 1264 KB | 11283814 |
| [1238_dp.java](1238_dp.java) | Java 1.8 | dp | O(n³ log n) | AC | 0.125 s | 1108 KB | 11283817 |
| [1238_dp.py](1238_dp.py) | Python 3.12 x64 | dp | O(n³ log n) | AC | 0.125 s | 696 KB | 11283815 |
| [1238_dp.rs](1238_dp.rs) | Rust 1.75 x64 | dp | O(n³ log n) | AC | 0.046 s | 316 KB | 11283818 |
| [1238_strings.py](1238_strings.py) | Python 3.12 x64 | strings | O(N⁴) | AC | 0.203 s | 1312 KB | 11315944 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1238_dp_optimized.cpp](1238_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(n³) | AC | 0.015 s | 144 KB | 11314905 |
| [1238_dp_optimized.go](1238_dp_optimized.go) | Go 1.14 x64 | dp | O(n³) | AC | 0.031 s | 320 KB | 11314912 |
| [1238_dp_optimized.rs](1238_dp_optimized.rs) | Rust 1.75 x64 | dp | O(n³) time; O(n²) space | AC | 0.031 s | 348 KB | 11328694 |
