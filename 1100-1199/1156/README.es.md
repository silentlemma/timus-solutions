# 1156. Repartir 2N problemas en dos rondas separando los problemas parecidos

[Timus 1156](https://acm.timus.ru/problem.aspx?space=1&num=1156) · dificultad 327 · graphs

Problema original de Evgeny Bryzgalov, del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda en inglés.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que repartir `2N` problemas, `N ≤ 50`, en dos rondas de `N`
problemas. `M ≤ 100` pares de problemas son parecidos y no pueden estar en
la misma ronda. Imprime las dos rondas, o `IMPOSSIBLE`.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `M`, y luego `M` pares de problemas parecidos.

## Salida

Dos líneas con los `N` problemas de cada ronda, o `IMPOSSIBLE`.

## Evaluación

Se acepta cualquier reparto válido. El comprobador verifica que las dos
líneas tienen `N` problemas cada una y juntas todos los problemas de 1 a
`2N`, que ningún par parecido comparte ronda y que `IMPOSSIBLE` solo se
imprime cuando no existe reparto.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
1 3
2 1
4 3
```

Salida:

```
1 4
2 3
```

## Solución

Se unen con aristas los problemas parecidos. Dentro de una componente
conexa, la ronda de un problema decide las de todos los demás: los
vecinos se alternan. Así que cada componente debe poder colorearse con
dos colores, y un ciclo impar hace imposible el reparto. Una componente
con clases de tamaños `a` y `b` da a la primera ronda `a` o `b`
problemas, y los problemas sin pareja son componentes de tamaño `(1, 0)`.

Falta elegir, para cada componente, qué clase va a la primera ronda para
que esta tenga exactamente `N` problemas. Es una suma de subconjuntos
sobre las componentes: `reach[k]` guarda los tamaños que pueden dar las
primeras `k` componentes, y un recorrido hacia atrás desde `N` recupera la
elección. Hay como mucho `2N = 100` componentes y tamaños hasta `N`, así
que la tabla es diminuta.

Detalles a tener en cuenta:

- colorear no basta: los tamaños de las clases deben sumar `N`;
- un problema parecido a sí mismo hace imposible el reparto;
- un par puede darse dos veces;
- los problemas de cada ronda pueden imprimirse en cualquier orden; aquí
  van en orden creciente.

Las respuestas se comprobaron con el comprobador en todas las pruebas, y
la posibilidad del reparto se comparó con probar todas las elecciones de
`N` problemas en 200 entradas aleatorias de hasta 14 problemas.

## Notas por lenguaje

- Todos los lenguajes colorean con una búsqueda en profundidad con pila
  explícita y llenan la misma tabla de sumas de subconjuntos; Python
  guarda cada fila como un conjunto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1156_graphs.cpp](1156_graphs.cpp) | G++ 13.2 x64 | graphs | O(N·(N + M)) | AC | 0.001 s | 224 KB |
| [1156_graphs.go](1156_graphs.go) | Go 1.14 x64 | graphs | O(N·(N + M)) | AC | 0.015 s | 1136 KB |
| [1156_graphs.java](1156_graphs.java) | Java 1.8 | graphs | O(N·(N + M)) | AC | 0.093 s | 616 KB |
| [1156_graphs.py](1156_graphs.py) | Python 3.12 x64 | graphs | O(N·(N + M)) | AC | 0.078 s | 892 KB |
| [1156_graphs.rs](1156_graphs.rs) | Rust 1.75 x64 | graphs | O(N·(N + M)) | AC | 0.015 s | 244 KB |
