# 1727. Los números mágicos de Znaika

[Timus 1727](https://acm.timus.ru/problem.aspx?space=1&num=1727) · dificultad 202 · greedy

Problema original de Ivan Burmistrov, del Concurso Regional de Programación por Equipos de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hallar un conjunto de enteros positivos distintos menores que 10⁵ cuyas
cifras sumen n en total, o imprimir −1 si no lo hay.

## Entrada

n (0 < n < 10⁵).

## Salida

El tamaño del conjunto y luego sus números, o −1. Se acepta cualquier
conjunto válido.

## Evaluación

Usar el verificador constructivo, no comparar con una única salida.
Comprobar cantidad, valores positivos menores que 100000, ausencia de
duplicados y suma decimal exacta. Las cinco fuentes nuevas superaron
13 entradas de Docker cada una y obtuvieron Accepted propio asociado a
su SHA exacto. El formato C++ superó por separado las 13 entradas.
El nuevo Python se ejecutó además con 265 entradas; un modelo separado
de prefijos/restos se verificó para los 99999 objetivos legales. No son
99999 ejecuciones de cada lenguaje. Incluir 1, 9, 45, 46 y 99999.

## Ejemplos

### Ejemplo 1

Entrada:

```
17
```

Salida:

```
3
7 12 43
```

## Solución

Sea `s(x)` la suma decimal de cifras y `L=100000`. Las bases voraces
calculan `s(i)=s(i//10)+i%10` para todo `i<L`, recorren desde `L−1` hacia
abajo y eligen un número cuando su suma cabe en el objetivo restante.
Cada valor se visita una vez: los elegidos son distintos y válidos.
Tiempo y tabla auxiliar `O(L)`; los `q` valores de salida ocupan `O(q)`.

¿Por qué termina? Cada número de `[90000,99999]` suma como máximo 45;
el bloque completo suma `9·10000+4·45·1000=270000`. Si el resto aún fuera
al menos 45 al acabar el bloque, todos sus números habrían cabido. Pero
restar 270000 del `n<100000` inicial no puede dejar un resto no negativo.
Así, el resto baja de 45 dentro del bloque y después nunca aumenta.
Al llegar a las cifras todavía libres `9,8,…,1`, representan vorazmente
cualquier resto de 0 a 45. Antes de `d`, mantener
`remainder≤d(d+1)/2`; elegir `d` si cabe conserva la cota para `d−1`.
El resto final es cero, por lo que nunca hace falta −1.

Se mantienen los cinco algoritmos sencillos. Solo C++ recibe el formato
exacto del repositorio, con Accepted y medidas propios; las otras cuatro
fuentes conservan sus bytes y se respalda el C++ original.

## Soluciones optimizadas

La nueva construcción evita la tabla completa y el recorrido largo.
Mientras el resto supere 45, elegir números consecutivos desde 99999 y
calcular sus sumas de cifras cuando hagan falta. Cada número de cinco
cifras aporta como máximo 45, así que cabe. La cota del bloque de 270000
prueba que esta fase termina antes de 90000, lejos de las cifras pequeñas.
Completar el resto con cifras distintas de 9 a 1. Las fases usan rangos
disjuntos y el invariante del resto demuestra la suma exacta. Se admite
cualquier conjunto válido; no se exige minimizar su tamaño.

Con `D` cifras por número grande y `q` valores de salida, el tiempo es
`O(qD+D)` y el espacio de salida `O(q)`; aquí `D=5`, por tanto `O(q)` tiempo.
No hay tabla previa `O(L)`. Es otra construcción, llamada `constructive`,
sin duplicar el barrido como `_optimized`. Los cinco lenguajes cumplen el
30% mediante ahorro medido de memoria frente a sus bases actuales.
Python pasa de 0,093 a 0,109 s registrados: se admite por memoria.
El cambio Rust 0,046→0,031 s es un tick y no prueba una aceleración fiable.

Ahorro medido de memoria: C++ 66.4%, Go 43.9%, Java 61.9%, Python 43.0%, Rust 76.6%.

## Notas por lenguaje

Las medidas Accepted corresponden a bytes exactos. Se comparan las
bases sencillas actuales, incluido el nuevo formato C++ aceptado.
La instantánea del 2 de noviembre de 2026 usa los filtros acordados de
compilador y otros autores: C++ busca el 15% superior o los primeros diez
puestos en ambas medidas; las demás familias, el primer puesto en ambas.
Un asterisco señala una mejora admitida que aún no alcanza esa meta.
Una muestra sin rivales ofrece cobertura formal, no demuestra superioridad.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1727_greedy.cpp](1727_greedy.cpp) | G++ 13.2 x64 | greedy | O(L) | AC | 0.015 s | 596 KB | 11308491 |
| [1727_greedy.go](1727_greedy.go) | Go 1.14 x64 | greedy | O(L) | AC | 0.031 s | 2268 KB | 11289382 |
| [1727_greedy.java](1727_greedy.java) | Java 1.8 | greedy | O(L) | AC | 0.125 s | 2196 KB | 11289385 |
| [1727_greedy.py](1727_greedy.py) | Python 3.12 x64 | greedy | O(L) | AC | 0.093 s | 1636 KB | 11289384 |
| [1727_greedy.rs](1727_greedy.rs) | Rust 1.75 x64 | greedy | O(L) | AC | 0.046 s | 1096 KB | 11289388 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1727_constructive.cpp](1727_constructive.cpp) | G++ 13.2 x64 | constructive | O(qD + D) | AC | 0.015 s | 200 KB | 11308058 |
| [1727_constructive.go](1727_constructive.go) | Go 1.14 x64 | constructive | O(qD + D) | AC | 0.031 s | 1272 KB | 11308060 |
| [1727_constructive.java](1727_constructive.java) | Java 1.8 | constructive | O(qD + D) | AC | 0.109 s | 836 KB | 11308061 |
| [1727_constructive.py](1727_constructive.py) | Python 3.12 x64 | constructive | O(qD + D) | AC | 0.109 s | 932 KB | 11308057 |
| [1727_constructive.rs](1727_constructive.rs) | Rust 1.75 x64 | constructive | O(qD + D) | AC | 0.031 s | 256 KB | 11308062 |
