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

## Notas por lenguaje

- Todos los lenguajes comparan las subcadenas desplazadas con una sola
  llamada de biblioteca.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1238_dp.cpp](1238_dp.cpp) | G++ 13.2 x64 | dp | O(n³ log n) | AC | 0.031 s | 460 KB |
| [1238_dp.go](1238_dp.go) | Go 1.14 x64 | dp | O(n³ log n) | AC | 0.031 s | 1264 KB |
| [1238_dp.java](1238_dp.java) | Java 1.8 | dp | O(n³ log n) | AC | 0.125 s | 1108 KB |
| [1238_dp.py](1238_dp.py) | Python 3.12 x64 | dp | O(n³ log n) | AC | 0.125 s | 696 KB |
| [1238_dp.rs](1238_dp.rs) | Rust 1.75 x64 | dp | O(n³ log n) | AC | 0.046 s | 316 KB |
