# 1182. Dos equipos de conocidos mutuos, lo más iguales posible

[Timus 1182](https://acm.timus.ru/problem.aspx?space=1&num=1182) · dificultad 512 · graphs

Problema original de Vladimir Kotov y Roman Elizarov, del concurso regional ACM ICPC del noreste de Europa 2001–2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`2 ≤ N ≤ 100` personas dicen a quién conocen; conocerse no tiene por qué
ser mutuo. Hay que repartir a todos en dos equipos no vacíos de modo que
en cada equipo cada miembro conozca a todos los demás, con tamaños lo más
parecidos posible, o decir que no hay reparto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego, para cada persona, la lista de las personas que conoce,
terminada en 0.

## Salida

`No solution`, o dos líneas, cada una con el tamaño de un equipo y sus
miembros.

## Evaluación

Se acepta cualquier reparto en el que ambos equipos no estén vacíos,
cubran a todos, sean grupos de conocidos mutuos y difieran en tamaño lo
menos posible; el comprobador toma la mejor diferencia de la respuesta
guardada.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
3 4 5 0
1 3 5 0
2 1 4 5 0
2 3 5 0
1 2 3 4 0
```

Salida:

```
No solution
```

### Ejemplo 2

Entrada:

```
5
2 3 5 0
1 4 5 3 0
1 2 5 0
1 2 3 0
4 3 2 1 0
```

Salida:

```
3 1 3 5
2 2 4
```

## Solución

Dos personas son desconocidas salvo que cada una conozca a la otra. Los
desconocidos deben ir en equipos distintos, así que el grafo de
desconocidos debe ser bipartito, lo que comprueba un coloreado en
anchura; un ciclo impar significa `No solution`. Cada componente conexa
de ese grafo tiene dos lados, que deben ir a equipos distintos, en
cualquiera de los dos sentidos. Las personas de componentes distintas se
conocen mutuamente, así que cualquier combinación de elecciones vale.

Lo que queda es una mochila: `reach[k][s]` dice si las primeras `k`
componentes pueden dar exactamente `s` personas al primer equipo, y
recuerda el lado usado. Se toma el `s` alcanzable más cercano a `N/2` y
se recorre hacia atrás para formar los equipos. `O(N²)`.

Detalles a tener en cuenta:

- conocer es unidireccional en la entrada, así que un par cuenta como
  conocido solo si ambos se nombran;
- una componente de una sola persona puede ir a cualquier equipo, lo que
  permite igualar tamaños;
- ambos equipos quedan no vacíos por sí solos: una componente con
  desconocidos tiene los dos lados no vacíos, y la mochila reparte a las
  personas sueltas.

Las respuestas se compararon con una solución escrita aparte en 300
grupos aleatorios de hasta 41 personas, doce de ellos sin solución, y
cada reparto impreso pasó el comprobador.

## Notas por lenguaje

- Todos los lenguajes colorean el grafo de desconocidos directamente
  desde la matriz de conocidos y hacen la misma mochila.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1182_graphs.cpp](1182_graphs.cpp) | G++ 13.2 x64 | graphs | O(N²) | AC | 0.015 s | 280 KB |
| [1182_graphs.go](1182_graphs.go) | Go 1.14 x64 | graphs | O(N²) | AC | 0.031 s | 1400 KB |
| [1182_graphs.java](1182_graphs.java) | Java 1.8 | graphs | O(N²) | AC | 0.171 s | 5732 KB |
| [1182_graphs.py](1182_graphs.py) | Python 3.12 x64 | graphs | O(N²) | AC | 0.078 s | 1332 KB |
| [1182_graphs.rs](1182_graphs.rs) | Rust 1.75 x64 | graphs | O(N²) | AC | 0.046 s | 384 KB |
