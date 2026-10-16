# 1751. Teoría de la improbabilidad

[Timus 1751](https://acm.timus.ru/problem.aspx?space=1&num=1751) · dificultad 3372 · graphs

Problema original de Damir Akhmetzyanov, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una teoría tiene n hipótesis, algunas basadas en otras, quizá en
ciclos. La hipótesis i es admisible con probabilidad pᵢ, de forma
independiente, y comprobarla cuesta tᵢ segundos, una comprobación cada
vez. Una hipótesis es verdadera cuando ella y todo aquello en lo que se
basa, directa o indirectamente, son admisibles. Hallar el tiempo
esperado para saber qué hipótesis son verdaderas, comprobando en el
mejor orden.

## Entrada

n (1 ≤ n ≤ 500) y luego, para cada hipótesis, tᵢ (1 ≤ tᵢ ≤ 1000), pᵢ
(0.0001 ≤ pᵢ ≤ 0.9999), kᵢ y las kᵢ hipótesis en que se basa
directamente.

## Salida

El tiempo esperado, con un error de a lo sumo 10⁻³.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
5 0.3 1 2
6 0.99 0
2 0.2 1 4
2 0.2 0
```

Salida:

```
13.350
```

### Ejemplo 2

Entrada:

```
3
1 0.5 1 2
2 0.5 1 3
3 0.5 1 1
```

Salida:

```
2.750
```

## Solución

Las hipótesis de un mismo ciclo de dependencias se apoyan unas en
otras, así que son todas verdaderas o todas falsas. El método de Tarjan
divide las hipótesis en esos grupos y da cada grupo después de todos
los grupos en que se basa.

Un grupo solo necesita comprobarse si todos los grupos en que se basa
resultaron totalmente admisibles; cualquier fallo por debajo ya lo hace
falso. Dentro de un grupo las comprobaciones paran en el primer fallo,
y el orden más barato es por tᵢ / (1 − pᵢ), de menor a mayor:
intercambiar dos vecinos en mal orden solo puede bajar el tiempo
esperado. Así el grupo g cuesta E_g = t₁ + p₁t₂ + p₁p₂t₃ + … en ese
orden y es totalmente admisible con probabilidad q_g = Πpᵢ. La
respuesta es la suma sobre los grupos de E_g por el producto de q_h
sobre todos los grupos h en que se basa g. Ese conjunto se construye
como un conjunto de bits, cada grupo tomando los conjuntos de los
grupos a los que apunta, en el orden que da el método de Tarjan.
`O(n² + n·m / 64)` para m dependencias; las operaciones con enteros
de varias palabras en Python dan `O(n³)`.

En el primer ejemplo 2 y 4 se comprueban siempre, por 6 y 2 segundos,
1 solo si 2 se cumple, 0,99 · 5, y 3 solo si 4 se cumple, 0,2 · 2: 13,35
en total.

Trampas:

- comprobar un grupo antes que los de debajo puede gastar tiempo que un
  fallo de abajo habría ahorrado;
- un grupo verdadero debe comprobarse entero;
- los productos sobre muchos grupos pueden ser diminutos, lo que aquí
  no hace daño.

Las respuestas coinciden con la mejor estrategia adaptativa hallada por
búsqueda sobre todo lo conocido hasta el momento, en 200 teorías
aleatorias de hasta 6 hipótesis, y con una implementación aceptada
independiente en las pruebas grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1751_graphs.cpp](1751_graphs.cpp) | G++ 13.2 x64 | graphs | O(n^2 + n*m/64) | AC | 0.156 s | 1008 KB |
| [1751_graphs.go](1751_graphs.go) | Go 1.14 x64 | graphs | O(n^2 + n*m/64) | AC | 0.125 s | 4328 KB |
| [1751_graphs.java](1751_graphs.java) | Java 1.8 | graphs | O(n^2 + n*m/64) | AC | 0.484 s | 8164 KB |
| [1751_graphs.py](1751_graphs.py) | Python 3.12 x64 | graphs | O(n^3) | AC | 0.234 s | 20332 KB |
| [1751_graphs.rs](1751_graphs.rs) | Rust 1.75 x64 | graphs | O(n^2 + n*m/64) | AC | 0.046 s | 3436 KB |
