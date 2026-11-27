# 1272. Un metro que no es el de Ekaterimburgo

[Timus 1272](https://acm.timus.ru/problem.aspx?space=1&num=1272) · dificultad 144 · dsu

Problema original de Magaz Asanov (preparado por Igor Goldberg), del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad está sobre 1 ≤ N ≤ 10 000 islas unidas por 0 ≤ K ≤ 12 000
túneles y 0 ≤ M ≤ 12 000 puentes, y entre todos conectan todas las
islas. Un metro debe conectar todas las islas usando algunos de estos
enlaces, con el menor número posible de puentes. ¿Cuántos puentes
necesita?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, K y M, luego K túneles y M puentes, cada uno como dos números de
isla entre 1 y N.

## Salida

El menor número de puentes.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 4 4
1 2
2 3
4 5
6 7
1 3
2 4
5 6
6 7
```

Salida:

```
2
```

## Solución

Los túneles no cuestan nada, así que se toman todos: dividen las islas
en grupos ya conectados. Cada puente puede unir como mucho dos grupos en
uno y, como toda la red es conexa, siempre se pueden elegir puentes que
unan los grupos de uno en uno. La respuesta es el número de grupos por
túneles menos uno, contado con una estructura de unión-búsqueda sobre
los túneles; se ignoran los extremos de los puentes.
`O((N+K)log(N+1))`.

Detalles a tener en cuenta:

- los puentes no importan, solo que conectan los grupos, cosa que el
  enunciado garantiza;
- los túneles pueden repetirse o unir una isla consigo misma
  (prueba 05);
- con una sola isla, o si los túneles ya lo conectan todo, la respuesta
  es 0 (pruebas 02, 04).

Bases y rápidos nativos enlazan raíces sin rango con path halving. El límite logarítmico es amortizado aun con enlaces arbitrarios ([Tarjan–van Leeuwen, lemas 7–8](https://doi.org/10.1145/62.2160)); una operación find puede ser lineal, sin afirmar inversa de Ackermann aquí. Iᶜ bytes consumidos con prelectura acotada: O((N+K)log(N+1)+Iᶜ). Bases C++/Go/Java solo túneles, Python/Rust archivo entero; rápidos C++/Go/Rust leen puentes, Java/Python prefijo. M se cuenta por entrada consumida.

Bases C++/Go/Java N+1 padres y lector B acotado O(N+B); Python entrada completa dividida/Rust String entero O(N+I). Go rápidoN+1 uint 16, Rust/Java padres nativos y búferes O(N+B). C++ rápido fija 10001 padres independientemente de N:W=10000, O(W+B). Python rápido raíces/tamaños negativos y bloques 1024 O(N+B), sin DSU para n=1 o k=0. Versiones por flujo sin lista de puentes.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1272_dsu_optimized.py` une por tamaño con path splitting. Guarda padre antiguo next_vertex, redirige nodo al abuelo y avanza al padre antiguo; halving avanzaría al nuevo. Raíces negativas guardan tamaños. Conectividad completa garantiza components−1 sin puentes; sale al quedar un componente, o N−1 sin DSU para n=1 o k=0. Tokens por bloques 1024, DSU O(N+K·α(N)) amortizado más entrada consumida, espacioO(N+B). Sin cambio algorítmico.

Accepted histórico exacto Python 3.12 #11327776:0.078 s / 784 KB. Cohorte 2026-11-20 tiempo 3/99, memoria 2/99; bajo 1024 KB solo tiempo sin primer puesto separado. #11304489 fue otra pareja 0.109 s / 1076 KB.

- `1272_dsu_optimized.py`: 0.078 s / 784 KB; base didáctica conservada `1272_dsu.py`: 0.093 s / 3328 KB.

`1272_dsu_optimized.java` conserva enlaces sin rango y halving, sustituye StreamTokenizer por bytes fijos y no lee sufijo de puentes. DSU tiene mismo límite logarítmico amortizado; O(N+K·N) solo cota más floja por find, no otro algoritmo. EspacioO(N+B). Parejas históricas Java: base 0.140 s / 488 KB, rápido 0.109 s / 512 KB.

Frente a `1272_dsu.java`: tiempo 0.140 s → 0.109 s; memoria 488 KB → 512 KB.

La solución optimizada en C++ analiza los números a mano desde un búfer
de 4 KB en lugar de `scanf` y guarda los padres en un arreglo global
fijo de 10 001 celdas, suficiente para `N ≤ 10 000`, en lugar de un
`std::vector`. Además lee los puentes hasta el final, cosa que la
solución sencilla no hace: [1272_dsu_optimized.cpp](1272_dsu_optimized.cpp).

La solución optimizada en Go analiza los números byte a byte desde el
`bufio.Reader` en lugar de `fmt.Fscan` y guarda los padres como
`uint16`, que admite números de isla hasta 10 000, en lugar de `int`.
Además lee los puentes hasta el final, cosa que la solución sencilla no
hace: [1272_dsu_optimized.go](1272_dsu_optimized.go).

La solución optimizada en Rust analiza los números a mano desde un búfer
de 4 KB que se rellena desde la entrada estándar, en lugar de leer toda
la entrada en un `String`, así que en memoria quedan solo los padres y
el búfer: [1272_dsu_optimized.rs](1272_dsu_optimized.rs).

### Mejora medida

Ganancias siguientes son observaciones históricas. Admisión por ranking común, sin regla independiente 30% recursos o primer puesto. Se conservan bases docentes aun si fallan métricas.

- `1272_dsu_optimized.cpp`: reducción de tiempo +51.61%; reducción de
  memoria +49.12%; base: `1272_dsu.cpp`.

- `1272_dsu_optimized.go`: reducción de tiempo -106.67%; reducción de
  memoria +35.85%; base: `1272_dsu.go`.

- `1272_dsu_optimized.rs`: reducción de tiempo +0.00%; reducción de
  memoria +63.93%; base: `1272_dsu.rs`.

## Notas por lenguaje

Caché ligada a fuente: rápidos C++/Java/Python pasan tiempo ordinario; ambos Rust también; ambos Go referencia escasa exacta (base 1428 KB ambas métricas, rápido 916 KB solo tiempo). Bases C++/Java/Python fallan y quedan docentes. [Reglas comunes](../../RATING_CRITERIA.md), solo tiempo bajo 1024 KB. Java histórico 6/90 tiempo,2/90 memoria es vieja instantánea. Nueve hashes con comentario nuevo requieren Accepted exacto nuevo; Java rápido no cambia.

Se corrigió en nueve archivos “cada puente une dos componentes”: puede ser interno, pero red completa conexa garantiza suficientes puentes entre componentes. Solo líneas explicativas cambiadas; código ejecutable, bases y otros comentarios útiles intactos. Tabla conserva ID/tiempo/memoria de Accepted históricos emparejados.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1272_dsu.cpp](1272_dsu.cpp) | G++ 13.2 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.015 s | 216 KB | 11331137 |
| [1272_dsu.go](1272_dsu.go) | Go 1.14 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.031 s | 1396 KB | 11331005 |
| [1272_dsu.java](1272_dsu.java) | Java 1.8 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.109 s | 472 KB | 11331044 |
| [1272_dsu.py](1272_dsu.py) | Python 3.12 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.125 s | 3220 KB | 11331064 |
| [1272_dsu.rs](1272_dsu.rs) | Rust 1.75 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.015 s | 724 KB | 11331101 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1272_dsu_optimized.cpp](1272_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.015 s | 128 KB | 11331138 |
| [1272_dsu_optimized.go](1272_dsu_optimized.go) | Go 1.14 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.031 s | 924 KB | 11331006 |
| [1272_dsu_optimized.py](1272_dsu_optimized.py) | Python 3.12 x64 | dsu | O(N+K·α(N)+Iᶜ) amortized | AC | 0.078 s | 888 KB | 11331065 |
| [1272_dsu_optimized.rs](1272_dsu_optimized.rs) | Rust 1.75 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.062 s | 268 KB | 11331102 |
| [1272_dsu_optimized.java](1272_dsu_optimized.java) | Java 1.8 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.109 s | 512 KB | 11325012 |
