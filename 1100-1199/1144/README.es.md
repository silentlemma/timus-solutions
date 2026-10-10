# 1144. Repartir cajas de oro entre generales lo más igualado posible

[Timus 1144](https://acm.timus.ru/problem.aspx?space=1&num=1144) · dificultad 1972 · greedy

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
momento tiene menos oro, que se encuentra con un montículo.

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
   con una tabla de sumas de subconjuntos en bitsets, una fila por caja
   para poder reconstruir el reparto. Solo se usa mientras la tabla tiene
   menos de 4 millones de bits, más o menos medio megabyte.
4. Si nada ayuda, la búsqueda termina.

Cada cambio estrecha la diferencia de dos generales sin subir al más rico
ni bajar al más pobre, así que la suma de los cuadrados de las cantidades
baja cada vez y la búsqueda termina; un tope de rondas protege el tiempo.
En pruebas aleatorias con muchas cajas por general la diferencia llega a
`1`, que es óptima cuando el total no es divisible por `M`. Con una o dos
cajas por general queda mayor, y en parte es inevitable.

Detalles a tener en cuenta:

- el límite de memoria de 4 MB impide tablas grandes de sumas de
  subconjuntos, de ahí la comprobación de tamaño antes de cada reparto
  exacto;
- cada general conserva al menos una caja: los movimientos nunca vacían
  `hi`, y un reparto que deja un lado vacío se descarta;
- la diferencia impresa debe ser la diferencia real del reparto impreso.

Las respuestas se comprobaron con el comprobador en todas las pruebas; los
cinco lenguajes imprimen repartos idénticos.

## Notas por lenguaje

- Todos los lenguajes siguen los mismos pasos en el mismo orden, así que
  sus resultados son idénticos.
- Go, Java y Rust guardan una caja como un solo entero, su valor
  desplazado 14 bits a la izquierda más su número, que se ordena igual que
  el par.
- Java lo guarda todo en arreglos primitivos, reutiliza un único búfer
  para las tablas de sumas de subconjuntos y evita las lambdas: con el
  límite de 4 MB, los números envueltos, las tablas de vida corta y la
  maquinaria que las lambdas cargan en Java 8 hacían crecer el montículo
  por encima de él.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1144_greedy.cpp](1144_greedy.cpp) | G++ 13.2 x64 | greedy | heuristic | AC | 0.046 s | 404 KB |
| [1144_greedy.go](1144_greedy.go) | Go 1.14 x64 | greedy | heuristic | AC | 0.156 s | 1944 KB |
| [1144_greedy.java](1144_greedy.java) | Java 1.8 | greedy | heuristic | AC | 0.125 s | 3648 KB |
| [1144_greedy.py](1144_greedy.py) | Python 3.12 x64 | greedy | heuristic | AC | 0.609 s | 4048 KB |
| [1144_greedy.rs](1144_greedy.rs) | Rust 1.75 x64 | greedy | heuristic | AC | 0.062 s | 608 KB |
