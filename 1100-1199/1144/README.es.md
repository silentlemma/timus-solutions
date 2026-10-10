# 1144. Repartir cajas de oro entre generales lo más igualado posible

[Timus 1144](https://acm.timus.ru/problem.aspx?space=1&num=1144) · dificultad 1947 · greedy

Problema original de HNT.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 10000` cajas con valores de 1 a 1000 se reparten entre `M ≤ N`,
`M ≤ 1000` generales; cada caja va entera a un general. Haz que la
diferencia entre el general más rico y el más pobre sea lo menor posible.
La respuesta se acepta si la diferencia es como mucho un `K` dado. Imprime
la diferencia y luego las cajas de cada general.

Límite de tiempo: 1 segundo. Límite de memoria: 4 MB.

## Entrada

`N`, `M` y `K`, y luego los `N` valores.

## Salida

La diferencia y luego `M` líneas con los números de caja de cada general.

## Evaluación

Se acepta cualquier reparto con diferencia como mucho `K`. El comprobador
verifica que cada caja se da exactamente una vez, que la diferencia
impresa es la real y que no supera `K`. En las pruebas grandes, `K` es la
diferencia que alcanza esta búsqueda; donde vale `1` también es la mejor
posible, porque el total no es divisible por `M`.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 3 4
12 95 16 37 59 50 47 3 41 95
```

Salida:

```
4
1 2 7
3 4 8 10
5 6 9
```

## Solución

Dividir números en `M` grupos de sumas iguales es NP-difícil, así que esto
es una heurística: un buen comienzo y una búsqueda local que para en
cuanto la diferencia es como mucho `K`.

El comienzo es la regla clásica de «primero los mayores»: se toman las
cajas de la más valiosa hacia abajo y cada una va al general que de
momento tiene menos oro, que se encuentra con un montículo (Java recorre
todos los generales en su lugar).

Después, mientras la diferencia sea mayor que `K`, se repite con el
general más rico `hi` y el más pobre `lo`, de diferencia `d`:

1. **Mover o intercambiar.** Mover una caja de valor `v` de `hi` a `lo`
   deja la diferencia del par en `|d − 2v|`; intercambiar la caja `a` de
   `hi` con la caja `b` de `lo` la deja en `|d − 2(a − b)|`. Cada general
   guarda sus cajas ordenadas, así que una búsqueda binaria encuentra la
   caja más cercana a `d/2` y, para cada valor distinto `a`, la caja `b`
   más cercana a `a − d/2`. Se hace el mejor cambio si estrecha el par.
2. Si entre `hi` y `lo` no hay ninguno, se prueba lo mismo entre `hi` y
   cada otro general, empezando por los más pobres, y entre cada general,
   empezando por los más ricos, y `lo`.
3. **Reparto exacto.** Si ningún movimiento ni intercambio sirve, se
   juntan las cajas de dos generales y se reparten lo más igualado posible
   con una tabla de sumas de subconjuntos en bitsets, una fila por prefijo
   (incluido el vacío) para reconstruir el reparto. Los datos de bits deben
   caber en 4 millones de bits, más o menos medio megabyte.
4. Si nada ayuda, la búsqueda termina.

Cada cambio estrecha la diferencia de dos generales sin subir al más rico
ni bajar al más pobre, así que la suma de los cuadrados de las cantidades
baja cada vez y la búsqueda termina; un tope de rondas protege el tiempo.
En pruebas aleatorias con muchas cajas por general la diferencia llega a
`1`, que es óptima cuando el total no es divisible por `M`. Con una o dos
cajas por general queda mayor, y en parte es inevitable.

Si la primera etapa deja una diferencia mayor que `K`, se intenta una
búsqueda exacta en profundidad con presupuesto, desde grupos vacíos.
Las cajas se procesan por valor decreciente, desempatando por número,
y los generales se prueban por número. Para el total `T`, cada suma final
está en `[L, U]`, con `L = max(1, ceil((T - (M-1)K)/M))` y
`U = floor((T + (M-1)K)/M)`, porque difiere de cualquier otra como mucho
en `K`. Esto ajusta los límites `[ceil(T/M)-K, floor(T/M)+K]`.

Con sumas parciales `s` y oro restante `A`, se ajustan los límites a
`low = max(L, max(s)-K)` y `high = min(U, min(s)+A+K)`.
Se poda si una suma supera `high`, el déficit hasta `low` supera `A`,
la capacidad total hasta `high` es menor que `A`, o quedan más generales
vacíos que cajas. En cada nivel se prueba solo el primer general con cada
suma distinta, incluido cero. Los generales son intercambiables, así que
esta simetría es segura; la comprobación de grupos vacíos y los valores
positivos garantizan grupos finales no vacíos. Se usan marcos explícitos sin recursión. Se termina con el primer
reparto dentro de `K`. Los topes son `B = SEARCH_NODES = 100000` candidatos
y `W = SEARCH_WORK = 1000000`, contando `M` unidades por candidato.
Si se agota cualquiera, se conserva el reparto de la primera etapa. El método
completo sigue siendo heurístico para entradas grandes arbitrarias.

Detalles a tener en cuenta:

- el límite de memoria de 4 MB impide tablas grandes de sumas de
  subconjuntos, de ahí la comprobación de tamaño antes de cada reparto
  exacto;
- cada general conserva al menos una caja: los movimientos nunca vacían
  `hi`, y un reparto que deja un lado vacío se descarta;
- la diferencia impresa debe ser la diferencia real del reparto impreso.

Las respuestas se comprobaron con el comprobador en todas las pruebas; los
cinco lenguajes imprimen repartos idénticos.

En la tabla de complejidad, `R = 20000` limita las rondas locales y
`P = SPLIT_BITS = 4000000` limita los bits de las tablas de subconjuntos.

## Notas por lenguaje

- Todos los lenguajes toman las mismas decisiones y desempatan igual,
  así que sus resultados son idénticos.
- Go, Java y Rust guardan una caja como un solo entero, su valor
  desplazado 14 bits a la izquierda más su número, que se ordena igual que
  el par.
- Java lo guarda todo en arreglos primitivos, reutiliza un único búfer
  para las tablas de sumas de subconjuntos y evita las lambdas: con el
  límite de 4 MB, los números envueltos, las tablas de vida corta y la
  maquinaria que las lambdas cargan en Java 8 hacían crecer el montículo
  por encima de él.
- Python descarta los tokens de entrada y el orden inicial tras usarlos
  para mantenerse dentro de los 4 MB.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1144_greedy.cpp](1144_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N + R·M·(N log N + P) + min(B·M, W)) | AC | 0.046 s | 404 KB |
| [1144_greedy.go](1144_greedy.go) | Go 1.14 x64 | greedy | O(N log N + R·M·(N log N + P) + min(B·M, W)) | AC | 0.109 s | 1948 KB |
| [1144_greedy.java](1144_greedy.java) | Java 1.8 | greedy | O(N² + R·M·(N log N + P) + min(B·M, W)) | AC | 0.156 s | 3628 KB |
| [1144_greedy.py](1144_greedy.py) | Python 3.12 x64 | greedy | O(N log N + R·M·(N log N + P) + min(B·M, W)) | AC | 0.671 s | 3512 KB |
| [1144_greedy.rs](1144_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N + R·M·(N log N + P) + min(B·M, W)) | AC | 0.046 s | 740 KB |
