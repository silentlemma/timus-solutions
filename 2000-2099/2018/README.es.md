# 2018. Contar Secuencias con Rachas Limitadas

[Timus 2018](https://acm.timus.ru/problem.aspx?space=1&num=2018) · dificultad 102 · dp, prefix_sums

Problema original de Olga Soboleva, preparado por Alex Samsonov, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuente las secuencias de longitud `n` formadas por 1 y 2. Una racha de unos
puede tener como máximo `a` posiciones y una de doses, como máximo `b`.
Dos secuencias son distintas si difieren en alguna posición. El resultado
se pide módulo `1 000 000 007`.

Las restricciones son `1 ≤ a,b ≤ 300` y `max(a,b)+1 ≤ n ≤ 50 000`.
Límites: 2 segundos y 64 MB.

## Entrada

La única línea contiene `n a b`.

## Salida

Imprima el número de secuencias válidas módulo `1 000 000 007`.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3 2 1
```

```
4
```

## Solución

Sean `A_i` y `B_i` los prefijos válidos de longitud `i` que terminan en 1 y
en 2. Introduzca `A_0 = B_0 = 1` como fronteras artificiales: cada una
representa el prefijo vacío anterior a la primera racha del otro símbolo.
Para una longitud positiva, separe la última racha maximal:

- `A_i = sum(B_(i−r), 1 ≤ r ≤ min(a,i))`.
- `B_i = sum(A_(i−r), 1 ≤ r ≤ min(b,i))`.

El prefijo restante está vacío o acaba en el símbolo contrario. A la inversa,
añadir una racha de longitud permitida a ese prefijo produce una secuencia
válida. La última racha es única, por lo que no hay omisiones ni duplicados.
Como los símbolos finales son distintos, el resultado es
`(A_n + B_n) mod 1 000 000 007`.

Para evitar sumar hasta 300 términos de nuevo en cada paso, mantenga
`S_A = sum(B_j, max(0,i−a) ≤ j < i)` y
`S_B = sum(A_j, max(0,i−b) ≤ j < i)` antes de procesar `i`, inicialmente uno.
Son precisamente `A_i` y `B_i`: guarde ambos antes de modificar las sumas.
Para la siguiente longitud, añada `B_i` a `S_A` y reste `B_(i−a)` si `i ≥ a`;
añada `A_i` a `S_B` y reste `A_(i−b)` si `i ≥ b`. Reduzca módulo el módulo
indicado y normalice las restas a residuos no negativos. Se desplazan
exactamente los extremos de las ventanas, conservando el invariante;
por inducción se calcula la recurrencia correcta.

Los términos que caducan pertenecen al pasado reciente. Guarde `B` en un
búfer circular de tamaño `a+1` y `A` en otro de tamaño `b+1`. Lea
primero los términos que caducan y después escriba los nuevos. Un valor
sobrescrito ya quedó fuera de su ventana; la casilla adicional separa el
nuevo término del que caduca ahora. El tamaño para `A` depende de **b**,
pues alimenta las secuencias acabadas en 2. Tiempo `O(n)` y espacio
`O(a+b)`, hasta 602 contadores.

En el ejemplo son válidas `112`, `121`, `211`, `212`. La pareja `22` viola
`b=1`, y `111` supera `a=2`, de modo que el resultado es cuatro.

Trampas:

- El prefijo vacío artificial aparece una vez en cada recurrencia y
  caduca normalmente.
- Obtener ambos valores de las ventanas antiguas antes de actualizarlas.
- Restar ya cuando `i=a` o `i=b`, usando el tipo de terminación opuesto.
- Usar enteros amplios: la suma con el módulo añadido puede acercarse a
  tres módulos.
- Normalizar las restas y no contar los dos estados vacíos como
  soluciones reales.

## Notas por lenguaje

Todas las versiones emplean dos búferes circulares y sumas móviles. C++,
Go y Java usan contadores con signo de 64 bits; Rust usa `u64`; Python
usa enteros y un resto no negativo. No hacen falta recursión ni una
tabla grande.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2018_dp_prefix_sums.cpp](2018_dp_prefix_sums.cpp) | G++ 13.2 x64 | dp, prefix_sums | O(n) | AC | 0.015 s | 388 KB |
| [2018_dp_prefix_sums.go](2018_dp_prefix_sums.go) | Go 1.14 x64 | dp, prefix_sums | O(n) | AC | 0.031 s | 1088 KB |
| [2018_dp_prefix_sums.java](2018_dp_prefix_sums.java) | Java 1.8 | dp, prefix_sums | O(n) | AC | 0.125 s | 404 KB |
| [2018_dp_prefix_sums.py](2018_dp_prefix_sums.py) | Python 3.12 x64 | dp, prefix_sums | O(n) | AC | 0.125 s | 452 KB |
| [2018_dp_prefix_sums.rs](2018_dp_prefix_sums.rs) | Rust 1.75 x64 | dp, prefix_sums | O(n) | AC | 0.015 s | 216 KB |
