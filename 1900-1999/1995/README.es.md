# 1995. Peso total mínimo para una cantidad seleccionada

[Timus 1995](https://acm.timus.ru/problem.aspx?space=1&num=1995) · dificultad 614 · greedy, constructive

Problema original de Denis Dublennykh, preparado por Oleg Dolgorukov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Construya `n` pesos enteros positivos. El primero se descarta siempre.
En cada posición posterior `i`, numerada desde cero, cuente los pesos
estrictamente menores entre los `i` anteriores. Se conserva el actual
exactamente cuando esa cantidad alcanza al menos el `p` por ciento de
`i`. Se cuentan todos los anteriores, también los descartados y el
primero; los iguales no son menores.

Minimice el peso total con exactamente `k` objetos conservados y dé
cualquier secuencia óptima. `1≤k<n≤100000`, `1≤p≤100`; se garantiza
viabilidad. Tiempo: 1 segundo; memoria: 64 MB.

## Entrada

Primera línea `n k`, segunda `p`.

## Salida

El total mínimo en la primera línea, seguido en la segunda por `n` pesos
positivos en orden. Se admite cualquier óptimo.

## Evaluación

Un comprobador verifica la cantidad y la suma de los pesos, compara el
total con el óptimo y simula cada decisión; se acepta cualquier
secuencia óptima.

## Ejemplos

Entrada:

```
3 1
50
```

Salida:

```
4
1 2 1
```

Se conserva el 2 y se descarta el último 1. El programa puede producir
`1 1 2`, también de total 4 y uno conservado. No es posible menos que
`n+k=4`: cada peso vale al menos 1 y cada conservado al menos 2.

## Solución

### Construcción

Sea `D=n−k`. Coloque primero `D` unos descartados y luego construya los
`k` conservados en orden no decreciente. En la posición `i=D..n−1` hacen
falta `q=ceil(p·i/100)` anteriores menores. En un prefijo ordenado, el
mínimo entero viable es su elemento `q` más uno:

`a[i]=a[(p·i−1)//100]+1`, inicialmente `a[0..D−1]=1`.

El índice es `q−1` y pertenece a `0..i−1`, pues `i≥1` y `1≤p≤100`. Nunca
disminuye al avanzar `i`; por inducción, el prefijo permanece ordenado y
sus primeros `q` valores son estrictamente menores que el nuevo. Así se
conservan exactamente los últimos `k`.

### Optimalidad

Reduzca a 1 todos los descartados de cualquier solución viable. Siguen
descartados y reducir otros pesos no disminuye el conteo menor de un
conservado sin modificar. El total no aumenta.

Intercambie un conservado `x≥2` con el 1 descartado inmediatamente
posterior. Si antes había `i` anteriores y `L` menores, `100L≥pi`;
después hay `i+1` anteriores y `L+1` menores. Sigue siendo conservado
porque `100≥p`. El 1 se descarta y los multiconjuntos previos de
posiciones posteriores no cambian. Repitiendo se llevan todos los unos
descartados al inicio: existe un óptimo de esta forma.

Compare la secuencia voraz `a` con cualquier cola viable `b`. Si cada
valor anterior de `a` es como máximo el correspondiente de `b`, también
lo es su estadístico de orden `q`. La viabilidad de `b[i]` obliga a que
su elemento prefijo `q` sea como máximo `b[i]−1`. El voraz toma su
propio elemento más uno, por tanto no supera `b[i]`. La inducción
demuestra mínimo coordenada a coordenada y suma mínima, sin suponer
ordenada la cola competidora.

## Notas por lenguaje

Una consulta directa por elemento: `O(n)` operaciones aritméticas y
memoria `O(n)`, más el texto de salida. Cada peso es como máximo
`i+1≤n`. El total llega a `n(n+1)/2=5000050000` con `n=100000`, `k=n−1`,
`p=100`: use acumuladores de 64 bits. `p·i` cabe en 32 bits; Python usa
enteros sin ese límite.

No incluya el elemento actual en el denominador, ni cuente solo
conservados, ni considere iguales como menores, ni cambie `≥` por `>`.
Contar pesos menores necesita un árbol solo en el comprobador; la
construcción misma es lineal. Los intercambios justifican la forma óptima; la
implementación no los ejecuta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1995_greedy_constructive.cpp](1995_greedy_constructive.cpp) | G++ 13.2 x64 | greedy, constructive | O(n) | AC | 0.015 s | 816 KB |
| [1995_greedy_constructive.go](1995_greedy_constructive.go) | Go 1.14 x64 | greedy, constructive | O(n) | AC | 0.046 s | 2740 KB |
| [1995_greedy_constructive.java](1995_greedy_constructive.java) | Java 1.8 | greedy, constructive | O(n) | AC | 0.093 s | 6100 KB |
| [1995_greedy_constructive.py](1995_greedy_constructive.py) | Python 3.12 x64 | greedy, constructive | O(n) | AC | 0.093 s | 10976 KB |
| [1995_greedy_constructive.rs](1995_greedy_constructive.rs) | Rust 1.75 x64 | greedy, constructive | O(n) | AC | 0.031 s | 2220 KB |
