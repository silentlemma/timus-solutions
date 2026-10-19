# 2041. Un orden con límites vecinos estrictos

[Timus 2041](https://acm.timus.ru/problem.aspx?space=1&num=2041) · difficulty 2106 · greedy, dsu

Problema original de Oleg Merkurev, del concurso Dandelion de la UrFU, campamento de Petrozavodsk, verano de 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `n` objetos numerados, con volumen interior `a_i` y exterior `b_i`.
Ordene todos los objetos para que cada pareja consecutiva `u,v` cumpla
la desigualdad estricta `b_u>a_v`. Solo importan las parejas
consecutivas. Determine si existe tal orden y construya uno cuando sea
posible.

## Entrada

La primera línea contiene `2≤n≤100000`. Las siguientes `n` líneas
contienen `a_i,b_i`, con `1≤a_i≤b_i≤1000000`. Se permite que ambos
volúmenes sean iguales. Los índices originales son `1..n`. Límite de
tiempo: 1 segundo. Memoria: 64 MB.

## Salida

Imprima `No` si no existe ningún orden. En otro caso imprima `Yes` y una
permutación de los `n` índices. Se admite cualquier permutación válida.

## Evaluación

El comprobador acepta cualquier permutación completa que cumpla todas
las desigualdades estrictas consecutivas. Verifica rango, unicidad y
cantidad de elementos. Para `No` cuenta de forma independiente los
objetos puntuales y los intervalos que cruzan estrictamente un volumen,
según el criterio de abajo. No exige reproducir una permutación esperada
concreta.

## Ejemplos

```
3
1 5
2 2
6 7
```

```
Yes
3 1 2
```

```
3
2 2
2 2
3 4
```

```
No
```

En el primer ejemplo, `3,1,2` cumple `7>1` y `5>2`. Los programas pueden
devolver `3,2,1`, también válido. En el segundo, entre los dos objetos
`(2,2)` habría que elevar el volumen exterior por encima de `2`; `(3,4)`
no puede seguir a `(2,2)` y no permite esa transición.

## Solución

### Elegir el mayor volumen interior admisible

Sea `B` el volumen exterior del último objeto elegido; inicialmente
`B=max(b_i)+1`. Elija el objeto no usado con mayor `a_i<B` y, en caso de
empate, mayor `b_i`. Añada su índice original, cambie `B` a su `b_i` y
elimínelo. Si ambos volúmenes empatan, el índice es indiferente; las
implementaciones eligen el mayor. Si faltan objetos pero ninguno es
admisible, imprima `No`.

El desempate exterior es necesario: para `(2,2),(2,3)` debe ir primero
el segundo objeto. Elegir primero el punto produciría un bloqueo
incorrecto.

### Por qué un bloqueo demuestra imposibilidad

Llame intervalo a un objeto con `a<b` y punto en `x` al objeto `(x,x)`.
Todo intervalo no usado permanece admisible. Si un intervalo admisible
`v` no se elige, el objeto elegido `u` tiene `a_u≥a_v`. Si la
desigualdad es estricta, `b_u≥a_u>a_v`. En caso de igualdad, el
desempate da `b_u≥b_v>a_v`. Por tanto, `v` sigue siendo admisible. Al
principio todos lo son; por inducción, cuando el algoritmo se bloquea
solo quedan puntos.

Fije un volumen `x`. Sea `K(x)` el número de puntos en `x` y `T(x)` el
número de intervalos con `a<x<b`. Cualquier orden válido requiere
`K(x)≤T(x)+1`. Entre dos apariciones consecutivas del punto `x`, el
volumen exterior debe pasar por primera vez de un valor no mayor que `x`
a otro mayor que `x`. El primer objeto que lo consigue tiene `b>x` y,
por la arista precedente, `a<x`. Así, cada uno de los `K(x)-1` huecos
disjuntos necesita un intervalo cruzante distinto.

Suponga que el algoritmo se bloquea y queda un punto `x`. Mientras
`B>x`, ese punto es admisible, así que el objeto elegido tiene volumen
interior al menos `x`. Tal fase no puede reducir `B` por debajo de `x` y
solo termina al consumir un punto en `x`, dejando `B=x`. Ningún
intervalo cruzante se elige durante esa fase, pues su volumen interior
es menor que `x`. Cada intervalo cruzante se consume con `B≤x` e inicia
una nueva fase `B>x`. Al bloquearse, `B≤x` y todos los intervalos ya se
usaron por el invariante. Hay una fase inicial y `T(x)` fases
posteriores, cada una terminada por un punto en `x`. Se consumieron
exactamente `T(x)+1` puntos, pero queda alguno: `K(x)>T(x)+1`. Se viola
una condición necesaria de cualquier orden.

Un recorrido completo es válido por construcción; un recorrido bloqueado
aporta una prueba de imposibilidad. Esto demuestra también la
suficiencia de las desigualdades por separado para cada `x`. No deben
convertirse en un emparejamiento global entre todas las clases de puntos
e intervalos: un solo intervalo puede ayudar a varios volúmenes en el
mismo orden.

### Predecesor con eliminaciones

Ordene crecientemente las ternas `(a,b,índice)` en posiciones `1..n` y
reserve `0` como centinela. Una búsqueda del primer `a≥B` da la cantidad
`c` de posiciones con `a<B`. Se necesita la mayor posición todavía
disponible no mayor que `c`; el orden de las ternas aplica ambas
prioridades.

Use una unión de conjuntos disjuntos con división del camino a la mitad,
unión por rango y el mínimo `best` guardado en cada raíz. Al principio
cada posición es un conjunto. Eliminar una posición disponible `p` une
su componente con la de `p-1`. Las componentes son intervalos contiguos
`[l,r]`: todas las posiciones `(l,r]` están eliminadas y `l` sigue
disponible o es el centinela. Así, `best[find(c)]` es exactamente el
predecesor requerido. El identificador de la raíz puede corresponder a
una posición eliminada: hay que consultar el mínimo guardado, no la raíz
misma. Un resultado `0` significa que no existe candidato. Las búsquedas
son iterativas.

La ordenación y `n` búsquedas binarias cuestan `O(n log n)`; las
operaciones equilibradas de conjuntos añaden `O(n α(n))`. El tiempo
total es `O(n log n)` y el espacio, incluida la respuesta, `O(n)`. Un
árbol de Fenwick sobre las posiciones disponibles es otra implementación
de predecesores en `O(n log n)`.

La desigualdad entre vecinos es estricta aunque la entrada permita
`a=b`. El empate interior se resuelve primero con el volumen exterior y
después con el índice. La raíz del conjunto no es necesariamente el
predecesor: hay que leer su mínimo guardado. El suministro de intervalos
se comprueba por cada volumen puntual, pues un intervalo puede ayudar a
varias clases. Una salida válida puede diferir del ejemplo.

## Notas por lenguaje

C++, Go y Rust guardan directamente ternas y arreglos de conjuntos. Go
usa ordenación compatible con 1.14 y entrada/salida con búfer; Rust,
búsqueda binaria iterativa y salida con búfer. Java 8 usa un búfer de
bytes, arreglos de ternas, rangos de un byte y StringBuilder. Python lee
pares línea a línea y usa ternas ordenadas, `bisect_left` y bytearray
para los rangos; la división iterativa de caminos evita límites de
recursión. Todas las versiones conservan índices originales desde uno y
excluyen la igualdad `a=B` mediante la búsqueda estricta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2041_greedy_dsu.cpp](2041_greedy_dsu.cpp) | G++ 13.2 x64 | greedy, dsu | O(n log n) | AC | 0.062 s | 2392 KB |
| [2041_greedy_dsu.go](2041_greedy_dsu.go) | Go 1.14 x64 | greedy, dsu | O(n log n) | AC | 0.218 s | 8064 KB |
| [2041_greedy_dsu.java](2041_greedy_dsu.java) | Java 1.8 | greedy, dsu | O(n log n) | AC | 0.218 s | 9700 KB |
| [2041_greedy_dsu.py](2041_greedy_dsu.py) | Python 3.12 x64 | greedy, dsu | O(n log n) | AC | 0.656 s | 32656 KB |
| [2041_greedy_dsu.rs](2041_greedy_dsu.rs) | Rust 1.75 x64 | greedy, dsu | O(n log n) | AC | 0.046 s | 5876 KB |
