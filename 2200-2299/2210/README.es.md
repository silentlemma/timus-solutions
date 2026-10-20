# 2210. El mayor dinero tras T días de trabajar o comprar negocios

[Timus 2210](https://acm.timus.ru/problem.aspx?space=1&num=2210) · dificultad 1161 · dp

Problema original de Valentin Zuev, de la Olimpiada Académica Universitaria Escolar de Informática 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada día un jugador trabaja por 1 moneda o compra un negocio de uno de N
tipos, que cuesta Aᵢ y da Bᵢ monedas al día desde el día siguiente;
después se paga la renta de los negocios comprados antes. Para cada una
de Q duraciones T, hallar el mayor número de monedas tras T días,
empezando de cero. Los límites son 2 segundos y 256 MB.

## Entrada

N, 1 ≤ N ≤ 100, luego los pares Aᵢ, Bᵢ entre 1 y 100, luego Q,
1 ≤ Q ≤ 5 · 10⁴, y las duraciones 1 ≤ T ≤ 10⁸.

## Salida

La mayor cantidad para cada T.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
1 100
1
5
```

Salida:

```
401
```

### Ejemplo 2

Entrada:

```
2
1 1
4 10
1
8
```

Salida:

```
42
```

## Solución

Solo importan los tipos que rinden más que cualquier tipo más barato,
así que forman una lista de coste y renta crecientes que termina en el
más caro, de coste C y renta I.

Un estado es (renta, dinero). Un día se trabaja o se compra un tipo
asequible, y un estado sin más renta ni más dinero que otro se
descarta, así que cada día queda una escalera corta de estados. La DP
avanza día a día con dos salidas:

- **Solo trabajar desde ahora.** Un estado (r, m) del día d que después
  solo trabaja termina con m + (r + 1)(T − d), una recta en T. Cada
  estado añade una recta así.
- **Estados ricos.** Cuando renta y dinero son ambos al menos C, el
  dinero ya no limita nada y comprar lo antes posible nunca es peor.
  Entonces cada día restante elige por separado lo mejor entre trabajar,
  que vale 1, y comprar el tipo que más rinde en los k días que quedan,
  que vale Bk − A. Desde C + 1 días restantes siempre es el tipo
  superior, que vale Ik − C, así que tras un prefijo fijo el total es
  una cuadrática en T cuya parte en T² es igual para todos los estados
  ricos. Quitándola, queda una recta por estado rico.

Los estados no ricos siguen trabajando o comprando, y el bucle termina
cuando todos se han vuelto ricos, lo que en los peores casos lleva
unos cientos de días. Los T pequeños hasta
ese punto se responden con una tabla, y los mayores toman el mejor valor
entre las rectas de trabajo y las rectas ricas, cada grupo guardado
como envolvente convexa superior y consultado con búsqueda binaria.

En el primer ejemplo (prueba 01), las acciones óptimas son trabajar,
comprar, trabajar, comprar, trabajar. El dinero al final de cada día es
1, 0, 101, 200, 401. La trampa es comprar demasiado pronto: al empezar
sin monedas no se puede comprar el día 1, y un negocio nuevo empieza a
dar renta solo al día siguiente.

La DP guarda a lo sumo C + 2I + 1 ≤ 301 estados al día durante unos
cientos de días, y cada consulta cuesta O(log).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2210_dp.cpp](2210_dp.cpp) | G++ 13.2 x64 | dp | O(D (C + I) N + Q log D) | AC | 0.046 s | 304 KB |
| [2210_dp.go](2210_dp.go) | Go 1.14 x64 | dp | O(D (C + I) N + Q log D) | AC | 0.078 s | 2716 KB |
| [2210_dp.java](2210_dp.java) | Java 1.8 | dp | O(D (C + I) N + Q log D) | AC | 0.187 s | 8628 KB |
| [2210_dp.py](2210_dp.py) | Python 3.12 x64 | dp | O(D (C + I) N + Q log D) | AC | 0.312 s | 11044 KB |
| [2210_dp.rs](2210_dp.rs) | Rust 1.75 x64 | dp | O(D (C + I) N + Q log D) | AC | 0.046 s | 2448 KB |
