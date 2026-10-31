# 1987. El intervalo contenedor más corto en una familia laminar

[Timus 1987](https://acm.timus.ru/problem.aspx?space=1&num=1987) · dificultad 168 · greedy

Problema original de Mikhail Rubinchik, idea de Nikita Pervukhin, del Campeonato Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados `n` intervalos cerrados distintos, cada pareja es disjunta o uno
contiene al otro. Para cada uno de `m` puntos, encontrar el intervalo
más corto que lo contiene. Mostrar su índice original desde 1, o −1 si
no existe.

`1≤n,m≤10⁵`, `1≤aᵢ<bᵢ≤10⁹`, `1≤cⱼ≤10⁹`. Los intervalos están ordenados
por extremo izquierdo no decreciente; en empates, por longitud
decreciente. Las consultas también son no decrecientes. Límites: 1
segundo y 64 MB.

## Entrada

Leer `n`, los `n` pares `aᵢ bᵢ`, después `m` y los `m` puntos. Los
índices de salida corresponden al orden original de los intervalos.

## Salida

Una línea por consulta con el índice del intervalo contenedor más corto, o −1.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

Entrada:

```
3
2 10
2 3
5 7
11
1
2
3
4
5
6
7
8
9
10
11
```

Salida:

```
-1
2
2
1
3
3
3
1
1
1
-1
```

## Solución

Recorrer las consultas de izquierda a derecha avanzando un puntero por
los intervalos ya ordenados. Mantener una pila de índices que forma una
cadena desde intervalos exteriores hasta interiores.

Para una consulta `c`, procesar todos los intervalos pendientes cuyo
inicio `a≤c`. Antes de apilar uno, retirar los que terminan
estrictamente antes de `a`: ya terminaron y son disjuntos del nuevo. Si
queda una cima, contiene el nuevo intervalo. Ambos se encuentran en `a`;
la condición laminar excluye un cruce parcial y el orden de entrada
impide que un exterior llegue después del interior. Con inicios iguales,
el exterior aparece primero. Apilar conserva la cadena.

Tras procesar todos los inicios como máximo `c`, retirar intervalos cuyo
extremo derecho sea estrictamente menor que `c`. Todos los restantes
contienen el punto: su inicio ya llegó y su final no pasó. La cima es el
más interior y, por tanto, el más corto. Con pila vacía, responder −1.

Un intervalo descartado nunca sirve después: terminó antes de una
coordenada ya alcanzada y las consultas no retroceden. Uno no procesado
empieza a la derecha de `c`. Todos los intervalos procesados que aún
cubren el punto permanecen en la cadena, así que la cima es óptima entre
todos. Intervalos anidados distintos tienen longitudes estrictamente
diferentes y la respuesta más corta es única.

En el ejemplo, los puntos 2 y 3 corresponden al intervalo 2; el punto 4
vuelve al exterior 1. Los puntos 5–7 corresponden al intervalo 3 y 8–10
vuelven al 1. Los puntos 1 y 11 no están cubiertos. Esto produce las
once líneas indicadas.

Cada intervalo entra una vez como máximo y sale una vez como máximo
entre ambos bucles de limpieza. El puntero solo avanza: tiempo total
`O(n+m)`. La pila necesita `O(n)` memoria auxiliar. Los programas
completos almacenan entrada o respuestas, por lo que su almacenamiento
total es `O(n+m)`. No hace falta ordenar, usar recursión, montículos ni
búsqueda binaria.

Trampas:

- Ambos controles de caducidad usan `<` estricto: el extremo derecho
  está incluido.
- Procesar todos los intervalos que empiezan en el punto antes de responder.
- Con inicios iguales, conservar el orden exterior antes que interior.
- Mostrar el índice original desde 1, no la profundidad de la pila.
- Retirar hijos terminados antes de volver a un antecesor.
- El algoritmo lineal depende de las garantías de estructura laminar y orden.

## Soluciones optimizadas

La solución optimizada en Go lee toda la entrada de golpe y analiza los
dígitos a mano en lugar de llamar a `fmt.Fscan` para cada uno de hasta
300 002 números; el barrido es el mismo: {1987_greedy_optimized.go}.

La solución optimizada en Python responde cada consulta en cuanto la lee
y guarda la pila dentro del arreglo de extremos izquierdos: una vez
apilado un intervalo, su extremo izquierdo ya no hace falta, así que esa
celda guarda el índice del intervalo que queda debajo en la pila. Los
extremos son `array("i")` de casillas con signo de 4 bytes, donde caben
coordenadas de hasta 10⁹, en lugar de listas de objetos enteros; la
entrada se lee en trozos de 4 KB en lugar de toda de golpe y las
respuestas se escriben en lotes de 1024: {1987_greedy_optimized.py}.

La solución optimizada en Rust responde cada consulta en cuanto la lee y
guarda la pila dentro del vector de extremos izquierdos: una vez apilado
un intervalo, su extremo izquierdo ya no hace falta, así que esa celda
guarda el índice del intervalo que queda debajo en la pila. Solo quedan
los dos vectores de extremos de `i32`, donde caben coordenadas de hasta
10⁹ e índices de hasta 10⁵. Los números se analizan a mano desde un
búfer de 4 KB en lugar de leer toda la entrada en un `String`, y las
respuestas pasan por un `BufWriter`: {1987_greedy_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1987_greedy_optimized.go`: reducción de tiempo +81.87%; reducción de
  memoria -55.43%; base: `1987_greedy.go`.

- `1987_greedy_optimized.py`: reducción de tiempo -33.69%; reducción de
  memoria +91.98%; base: `1987_greedy.py`.

- `1987_greedy_optimized.rs`: reducción de tiempo +51.61%; reducción de
  memoria +81.68%; base: `1987_greedy.rs`.

## Notas por lenguaje

Los cinco programas realizan el mismo barrido. Coordenadas e índices
caben en enteros de 32 bits con signo. C++ y Rust usan vectores, Java
arreglos primitivos y Go slices. Go lee con `fmt.Fscan` y Java con
`StreamTokenizer`. Python almacena los extremos, consume las consultas
mediante un iterador de tokens y acumula las respuestas.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1987_greedy.cpp](1987_greedy.cpp) | G++ 13.2 x64 | greedy | O(n+m) | AC | 0.031 s | 1288 KB | 11292362 |
| [1987_greedy.go](1987_greedy.go) | Go 1.14 x64 | greedy | O(n+m) | AC | 0.171 s | 6776 KB | 11307320 |
| [1987_greedy.java](1987_greedy.java) | Java 1.8 | greedy | O(n+m) | AC | 0.140 s | 5492 KB | 11307231 |
| [1987_greedy.py](1987_greedy.py) | Python 3.12 x64 | greedy | O(n+m) | AC | 0.187 s | 24900 KB | 11292364 |
| [1987_greedy.rs](1987_greedy.rs) | Rust 1.75 x64 | greedy | O(n+m) | AC | 0.031 s | 5328 KB | 11292367 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1987_greedy_optimized.go](1987_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(n+m) | AC | 0.031 s | 10532 KB | 11307365 |
| [1987_greedy_optimized.py](1987_greedy_optimized.py) \* | Python 3.12 x64 | greedy | O(n+m) | AC | 0.250 s | 1996 KB | 11307366 |
| [1987_greedy_optimized.rs](1987_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(n+m) | AC | 0.015 s | 976 KB | 11307324 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
