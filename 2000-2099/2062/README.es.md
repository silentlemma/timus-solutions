# 2062. Acumular radiación por divisores

[Timus 2062](https://acm.timus.ru/problem.aspx?space=1&num=2062) · dificultad 296 · fenwick

Problema original de Alexey Danilyuk, preparado por Nikita Sivukhin, del Concurso Regional Escolar de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cadena tiene n partículas con cargas iniciales a[i]. Dirigir una
potencia d a la partícula k suma d a cada partícula cuyo número es
múltiplo de k. La operación `2 l r d` dirige la potencia d a cada
partícula de l a r por separado, así que una partícula alcanzada desde
varias recibe varias sumas; la operación `1 i` pregunta la carga actual
de la partícula i. Los límites son 3 segundos y 128 MB.

## Entrada

Primero n, luego las n cargas a[i], después q y las q operaciones. 1 ≤
n, q ≤ 300 000, 0 ≤ a[i], d ≤ 10⁶, 1 ≤ i ≤ n, 1 ≤ l ≤ r ≤ n.

## Salida

Las respuestas a las consultas, una por línea.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

Cada bloque de entrada va seguido de su salida.

```
3
1 2 3
2
2 1 3 5
1 2
```

```
12
```

```
6
1 2 1 4 5 6
5
2 2 4 2
1 3
1 4
2 3 5 1
1 5
```

```
3
8
6
```

En el primer experimento, irradiar `[1,3]` con potencia cinco llega a la
partícula dos desde las fuentes uno y dos. Su carga es `2+5+5=12`. Las
cargas iniciales no son por sí mismas fuentes de radiación.

En el segundo, la primera actualización deja potencia dos en las fuentes
de `[2,4]`. La partícula tres recibe solo la fuente tres: `1+2=3`. La
cuatro recibe las fuentes dos y cuatro: `4+2+2=8`. La siguiente
actualización de `[3,5]` añade uno a la fuente cinco y su carga pasa a
`5+1=6`.

## Solución

### Separar potencia dirigida y carga física

Sea `v[k]` la potencia acumulada dirigida a la fuente `k`, inicialmente
cero. Una actualización suma `d` a `v[l..r]`. La fuente alcanza la
partícula `i` exactamente cuando su índice divide `i`. Por tanto, la
carga es `a[i]+sum(v[k] : k divide i)`. La regla demuestra la igualdad
para una irradiación y la suma la conserva después de todas las
operaciones. Divisores diferentes representan fuentes diferentes: sus
ondas no cancelan ni fusionan las aportaciones.

### Sumas de intervalo mediante Fenwick

Guardamos las diferencias de `v` en un árbol Fenwick. Sumar `d` al
intervalo cerrado requiere sumar en `l` y restar en `r+1` cuando este
índice existe. El prefijo hasta `k` es exactamente `v[k]`: los dos
deltas dejan una contribución `d` solamente dentro del intervalo. Los
caminos de actualización y prefijo cubren correctamente sus rangos y
cuestan `O(log n)`. Una medición suma esos prefijos para todos los
divisores del índice y añade únicamente la carga inicial de esa
partícula. El invariante anterior demuestra así cada respuesta.

### Pares de divisores en un CSR compacto

Cada divisor pertenece al par `(d,i/d)` cuyo elemento menor cumple
`d²≤i`. Precalculamos solamente esos menores: para cada `d²≤n`
recorremos `d²,d²+d,…≤n`, exactamente los múltiplos donde `d` es divisor
pequeño. Una primera pasada cuenta entradas por partícula; sus prefijos
dan los offsets de un array plano; otra pasada rellena los segmentos. Al
medir `i` recorremos su segmento y consultamos ambos miembros de cada
par, solo una vez si coinciden. El menor identifica un par único, de
modo que todos los divisores positivos, incluidos uno y el propio
índice, aparecen exactamente una vez. Los cuadrados requieren comprobar
la igualdad para no duplicar su raíz.

Los divisores pequeños caben en 16 bits, pues
`d≤floor(sqrt(300000))=547`; también basta short con signo en Java. Hay
como máximo `n·547=164100000<2³¹` entradas, por lo que los offsets caben
en 32 bits con signo; se reserva el tamaño realmente contado. El número
exacto es `S=sum(floor(n/d)−d+1,1≤d≤floor(sqrt(n)))`. La cota armónica
da `O(n log n)` para las dos pasadas y el almacenamiento, sin listas de
enteros empaquetados en objetos por partícula.

No sumar las cargas iniciales sobre los divisores. Actualizar las
potencias dirigidas. Como el extremo derecho está incluido, el delta
negativo corresponde a `r+1`; si `r=n` queda fuera del árbol y se omite.
Usar índices desde uno: una actualización en cero no avanza. No duplicar
la raíz de un cuadrado, truncar respuestas a 32 bits, olvidar la fuente
uno ni imprimir respuestas para actualizaciones. Las mediciones
repetidas y la potencia cero son válidas.

## Notas por lenguaje

Las cargas y celdas Fenwick son enteros de 64 bits con signo. Una cota
segura, aunque holgada, es `1000000+q·n·1000000≤90000000001000000<2⁶³`:
una operación tiene a lo sumo `n` fuentes. Las diferencias pueden ser
negativas aunque las potencias reales sean no negativas. Los índices y
`d²` caben en 32 bits.

El precálculo usa `O(n log n)` tiempo y espacio. Con `u` actualizaciones
e índices medidos `i₁,…,iₘ`, el tiempo total es `O(n log n+u log
n+sum(τ(iⱼ) log n))`, donde `τ(i)` cuenta divisores. Una actualización
cuesta `O(log n)` y una medición `O(τ(i) log n)`, no tiempo constante.
Los cinco programas usan los mismos segmentos de pares. C++, Go, Java y
Rust usan arrays/vectores primitivos y entrada/salida con búfer. Python
guarda divisores de 16 bits, offsets de 32 y cargas/Fenwick de 64, lee
por líneas y escribe lotes de 1024 respuestas. La solución en Python corre en PyPy,
porque CPython es demasiado lento en las pruebas más grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2062_fenwick.cpp](2062_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n log n + q tau_max log n) | AC | 0.437 s | 10720 KB |
| [2062_fenwick.go](2062_fenwick.go) | Go 1.14 x64 | fenwick | O(n log n + q tau_max log n) | AC | 0.843 s | 42280 KB |
| [2062_fenwick.java](2062_fenwick.java) | Java 1.8 | fenwick | O(n log n + q tau_max log n) | AC | 0.703 s | 14964 KB |
| [2062_fenwick.py](2062_fenwick.py) | PyPy 3.10 x64 | fenwick | O(n log n + q tau_max log n) | AC | 1.875 s | 38992 KB |
| [2062_fenwick.rs](2062_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n log n + q tau_max log n) | AC | 0.406 s | 27256 KB |
