# 1472. Ejército marciano

[Timus 1472](https://acm.timus.ru/problem.aspx?space=1&num=1472) · dificultad 1037 · dp

Problema original de Alexander Ipatov, del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N militares (2 ≤ N ≤ 100000) forman un árbol: el militar i > 1 depende
del mando K_i < i, y el enlace cuesta C_i (0 ≤ C_i ≤ 1000) por megabyte.
Cada militar tiene una fiabilidad real A_i: la del general (el número 1)
es 1, la de los soldados rasos (quienes no tienen subordinados) es 0 y
las demás son desconocidas. El tráfico facturado en el enlace del
militar i es cualquier cantidad de al menos max(0, A_K_i − A_i), elegida
por los propios militares. Hay que hallar la factura más pequeña que el
proveedor puede asegurarse, con exactamente dos cifras tras el punto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego N − 1 líneas K_i C_i para i = 2 … N.

## Salida

La cantidad asegurada.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
1 10
2 5
2 3
3 1
3 2
3 3
```

Salida:

```
8.00
```

## Solución

Los militares facturan el mínimo y eligen las fiabilidades desconocidas
para minimizar Σ C_i·max(0, A_K_i − A_i). Recortar cada A al intervalo
[0, 1] nunca hace crecer un término. Ahora se corta en cada nivel t
entre 0 y 1: los militares con A ≥ t incluyen al general y a ningún
soldado raso, y los enlaces desde ellos hacia militares por debajo de t
forman un corte que separa al general de todos los soldados rasos. La
factura es la integral de los precios de esos cortes sobre t, así que
nunca es menor que el corte más barato, y poner A = 1 por encima de ese
corte y 0 por debajo la alcanza. La respuesta es el corte más barato de
este tipo, siempre un número entero.

En un árbol es un mínimo de abajo arriba: cut(v), la forma más barata de
separar v de todos los soldados rasos por debajo, es la suma sobre sus
subordinados u de min(C_u, cut(u)), donde un soldado raso no se puede
separar de sí mismo y solo ofrece su propio enlace. Los mandos tienen
números menores que sus subordinados, así que una pasada de N hasta 2
termina cada militar antes que su mando. La respuesta es cut(1). `O(N)`.

Detalles a tener en cuenta:

- las fiabilidades son reales, pero el óptimo es entero y se escribe con
  «.00» (todas las pruebas);
- un enlace barato muy abajo puede ganar a uno caro más arriba, y los
  enlaces de precio 0 hacen gratis toda una rama (pruebas 03, 04);
- un soldado raso solo ofrece el enlace con su mando (prueba 02);
- una cadena de 100000 militares es demasiado profunda para la
  recursión, que la numeración permite evitar (gen2).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1472_dp.cpp](1472_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.109 s | 1760 KB |
| [1472_dp.go](1472_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.093 s | 5536 KB |
| [1472_dp.java](1472_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 2120 KB |
| [1472_dp.py](1472_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.109 s | 20020 KB |
| [1472_dp.rs](1472_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 6288 KB |
