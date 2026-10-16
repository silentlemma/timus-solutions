# 1755. Tarta

[Timus 1755](https://acm.timus.ru/problem.aspx?space=1&num=1755) · dificultad 829 · greedy

Problema original de Vladislav Isenbaev, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tarta tiene n gramos de bizcocho y m de chocolate. El Pequeño la corta
en dos trozos, con cualquier cantidad de cada cosa, y Karlsson se queda
el trozo que más le gusta, dejando elegir al Pequeño si empatan. Un
trozo con x gramos de bizcocho e y de chocolate vale a₁x + b₁y para el
Pequeño y a₂x + b₂y para Karlsson. Hallar un corte que dé al Pequeño lo
máximo.

## Entrada

a₁, b₁, a₂, b₂ (0 ≤ aᵢ, bᵢ ≤ 100) y luego n y m (0 ≤ n, m ≤ 1000).

## Salida

El bizcocho y el chocolate de uno de los dos trozos, con un error de a lo
sumo 10⁻⁸. Se acepta cualquier corte óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2 3 2
400 300
```

Salida:

```
300.00000000 0.00000000
```

## Solución

El Pequeño siempre acaba con un trozo que Karlsson valora en no más de
la mitad de la tarta, T/2 con T = a₂n + b₂m: si Karlsson prefiere un
trozo, se lo lleva, y si empatan ambos valen T/2 para él. Cualquier
trozo que Karlsson valore en a lo sumo T/2 puede ser del Pequeño con
solo cortarlo. Así que hay que hallar el trozo de mayor valor
a₁x + b₁y con a₂x + b₂y ≤ T/2, 0 ≤ x ≤ n y 0 ≤ y ≤ m.

Es una mochila fraccionaria con dos bienes: cada gramo de bizcocho aporta
a₁ y ocupa a₂ del espacio T/2, cada gramo de chocolate aporta b₁ y
ocupa b₂. Lo mejor es tomar primero el bien de mayor valor por espacio,
tanto como quepa, y luego el otro. Los bienes que no ocupan espacio se toman
enteros, y comparar a₁·b₂ con b₁·a₂ mantiene el orden exacto. `O(1)`.

En el ejemplo T/2 = 900. El chocolate aporta 2 por 2 de espacio y el
bizcocho 1 por 3, así que se toman los 300 gramos de chocolate, que ocupan
600, y luego 100 gramos de bizcocho: un trozo que vale 700 para el
Pequeño. El programa imprime este trozo, 100 y 300; el ejemplo imprime
el otro, 300 y 0, que es el mismo corte.

Trampas:

- la respuesta puede nombrar cualquiera de los trozos: importa el
  corte, no el trozo;
- si Karlsson no valora nada, el Pequeño puede llevarse la tarta
  entera;
- un empate no perjudica al Pequeño, así que el trozo puede ocupar el
  espacio justo.

Los cortes dan al Pequeño el mismo valor que una implementación
aceptada independiente, que prueba las esquinas de la región
permitida, en 600 tartas aleatorias, algunas con coeficientes nulos o
con gustos que coinciden.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1755_greedy.cpp](1755_greedy.cpp) | G++ 13.2 x64 | greedy | O(1) | AC | 0.015 s | 140 KB |
| [1755_greedy.go](1755_greedy.go) | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 1120 KB |
| [1755_greedy.java](1755_greedy.java) | Java 1.8 | greedy | O(1) | AC | 0.140 s | 1792 KB |
| [1755_greedy.py](1755_greedy.py) | Python 3.12 x64 | greedy | O(1) | AC | 0.078 s | 480 KB |
| [1755_greedy.rs](1755_greedy.rs) | Rust 1.75 x64 | greedy | O(1) | AC | 0.046 s | 280 KB |
