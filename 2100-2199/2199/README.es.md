# 2199. Dos días de un rango cuyos cambios suman lo más cerca de cero

[Timus 2199](https://acm.timus.ru/problem.aspx?space=1&num=2199) · dificultad 1265 · sqrt_decomposition, sorting

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arreglo d de N enteros recibe Q consultas de rango [l, r]: dar dos
posiciones distintas i, j del rango con el menor |dᵢ + dⱼ|, cualquiera
si hay varias mejores. Los límites son 3 segundos y 256 MB.

## Entrada

N y Q, 2 ≤ N, Q ≤ 30 000, luego d con |dᵢ| ≤ 10⁹, y luego las
consultas.

## Salida

Dos posiciones por consulta.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 4
17 11 -1 -4 20 -24
1 2
3 4
2 3
1 6
```

Salida:

```
1 2
3 4
2 3
5 6
```

## Solución

Se ordenan los elementos por valor absoluto. El mejor par de cualquier
conjunto son dos vecinos en ese orden: si para a y b hay un elemento c
entre ellos con |a| ≤ |c| ≤ |b|, cambiar b por c o a por c nunca aumenta
|a + b|, porque c tiene el signo de a o el de b. Así un conjunto solo
necesita, para cada elemento, su predecesor y su sucesor en ese orden.

Las consultas se responden fuera de línea, agrupadas por el bloque de
su extremo izquierdo, al estilo del algoritmo de Mo sin borrados. Dentro
de un bloque las consultas se ordenan por extremo derecho, y la parte
del rango a la derecha del bloque solo crece, guardando sus elementos en
un bitset sobre los rangos de valor absoluto, de modo que un elemento
nuevo halla sus dos vecinos con operaciones de bits y actualiza el mejor
par. Los pocos días entre el extremo izquierdo y el borde del bloque se
añaden encima para cada consulta y luego se quitan, con sus propios
pares preparados una vez por bloque.

Dos cotas baratas recortan casi todo el trabajo. El menor |dᵢ + dⱼ| de
todo el arreglo se conoce de antemano, y una consulta que contiene un
par que lo alcanza se responde al instante con una tabla de prefijos. Y
un elemento cuyo mejor compañero en todo el arreglo no puede mejorar la
respuesta actual nunca necesita insertarse.

La versión en Python evita las búsquedas en el bitset. Insertar los
elementos uno a uno en el orden por valor absoluto equivale a borrarlos
del orden completo al revés, así que una lista enlazada sobre ese orden,
borrada desde el final, da a cada elemento sus vecinos en el momento en
que llega. Para los pocos días a la izquierda del bloque, una consulta
necesita, para cada uno de esos días x, el elemento llegado y más
cercano a −x. Al llegar, y pasa a ser el más cercano exactamente para
los valores −x entre los puntos medios hacia sus vecinos en el orden
por valor, y estos intervalos también se hallan borrando desde el
final. Los intervalos se aplican en orden de llegada a un árbol sobre
grupos de 16 de esos días, gana el último, y una consulta lee el
compañero guardado de cada uno de sus días.

En el ejemplo todo el arreglo da |20 − 24| = 4 en los días 5 y 6.

Con bloques de unos N / √Q días esto cuesta O((N + Q)√N) pasos de
bitset.

## Notas por lenguaje

- Python se ejecuta con PyPy: con CPython 3.12 supera el límite de tiempo
  en el test 4 (3.031 s), mientras que con PyPy 3.10 se acepta en 1.125 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2199_sqrt_decomposition_sorting.cpp](2199_sqrt_decomposition_sorting.cpp) | G++ 13.2 x64 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 0.656 s | 3472 KB |
| [2199_sqrt_decomposition_sorting.go](2199_sqrt_decomposition_sorting.go) | Go 1.14 x64 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 1.234 s | 12004 KB |
| [2199_sqrt_decomposition_sorting.java](2199_sqrt_decomposition_sorting.java) | Java 1.8 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 1.812 s | 11324 KB |
| [2199_sqrt_decomposition_sorting.py](2199_sqrt_decomposition_sorting.py) | PyPy 3.10 x64 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 1.125 s | 17704 KB |
| [2199_sqrt_decomposition_sorting.rs](2199_sqrt_decomposition_sorting.rs) | Rust 1.75 x64 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 0.703 s | 7536 KB |
