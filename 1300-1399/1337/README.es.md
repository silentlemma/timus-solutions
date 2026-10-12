# 1337. Burocracia

[Timus 1337](https://acm.timus.ru/problem.aspx?space=1&num=1337) · dificultad 1532 · graphs

Problema original de Anatoly Uglov y Evgeny Krokhalev, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 100 funcionarios emiten cada uno un tipo de documento y atienden un
día de una semana de L ≤ 100 días; varios funcionarios pueden atender el
mismo día. Conseguir un documento lleva el día entero, así que se
consigue como mucho un documento por día, y solo se da a quien ya tiene
cierto conjunto de otros documentos. Hoy es el día K de la semana, y hoy
también se puede usar. Dados los documentos que ya se tienen y los que
se quieren, hay que hallar el menor número de días después de hoy para
conseguirlos todos, y los documentos en el orden en que se obtienen, o
imprimir `No Solution`. Si hay varios órdenes igual de rápidos, vale
cualquiera.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y L; el día de atención de cada funcionario; N listas de los
documentos que necesita cada uno, cada una terminada en 0; K; la lista
de documentos que se tienen, terminada en 0; la lista de documentos
deseados, terminada en 0.

## Salida

El número de días y luego los documentos en el orden en que se
obtienen, o `No Solution`.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 7
1 2
0
1 0
1
1 0
2 0
```

Salida:

```
1
2
```

## Solución

Primero se busca lo que hay que conseguir: los documentos deseados que
no se tienen y, detrás de cada uno, los papeles que necesita y tampoco
se tienen, y así sucesivamente. Un papel que ya se tiene corta la
búsqueda, porque lo que necesitaba ya no importa. Si estos documentos se
necesitan unos a otros en un ciclo, ninguno del ciclo puede ser el
primero, y la respuesta es `No Solution`; un orden topológico lo
detecta.

Se numeran los días desde hoy, que es el día 0. Un plan es un orden de
los documentos: cada uno se consigue el primer día libre de su
funcionario que llega después de sus papeles. En un día en que se puede
conseguir algún documento, conseguirlo nunca perjudica, porque adelantar
a ese día su obtención posterior solo libera un día. Así que la única
elección es cuál de los documentos listos para el primer día útil
tomar, y todos son de funcionarios de ese día de la semana. Si dos
funcionarios nunca comparten día, el plan es forzado; si no, tomar el
documento con la cadena de espera más larga detrás es una buena
apuesta, pero no siempre acierta (prueba 11).

La respuesta se halla con ramificación y poda sobre esa elección:

- la regla de la cadena más larga da un primer plan y se vuelve a
  ejecutar desde cada nodo de la búsqueda para mejorar el mejor plan;
- un nodo se poda con una cota inferior: el día más temprano de cada
  documento restante sale de sus papeles, y para cada día de la semana
  los k documentos que no pueden ir antes del día r ocupan k de esos
  días desde r, y al último aún le queda su cadena de espera más corta;
- un conjunto de documentos en mano al que ya se llegó el mismo día o
  antes no se vuelve a explorar.

En el peor caso la búsqueda es exponencial. En casos aleatorios con 100
funcionarios que comparten una semana de pocos días suele terminar en
una fracción de segundo, pero algunos casos raros tardan mucho más. Los
resultados se contrastaron con una programación dinámica sobre todos
los subconjuntos de documentos por conseguir, en 1000 casos aleatorios
de hasta 14 documentos con días compartidos.

Detalles a tener en cuenta:

- varios funcionarios pueden atender el mismo día y solo se consigue un
  documento, así que el orden importa (prueba 09);
- hoy es el día 0 y se puede usar: un documento cuyo funcionario atiende
  hoy cuesta 0 días (prueba 04);
- si todo lo deseado ya está en mano, la respuesta es 0 y una línea
  vacía (pruebas 02 y 06);
- un ciclo entre los papeles necesarios puede romperlo un papel que ya
  se tiene (prueba 07), y solo un ciclo entre los documentos aún por
  conseguir hace imposible la tarea (prueba 03).

Complejidad: `O(2^N·N)` para N documentos por conseguir, ya que ningún
conjunto de documentos en mano se explora dos veces.

## Notas por lenguaje

- El conjunto de documentos en mano es un entero en Python, dos palabras
  de 64 bits en C++, Go y Rust y una lista de dos long en Java, y sirve
  de clave de un mapa.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1337_graphs.cpp](1337_graphs.cpp) | G++ 13.2 x64 | graphs | O(2^N·N) | AC | 0.015 s | 300 KB |
| [1337_graphs.go](1337_graphs.go) | Go 1.14 x64 | graphs | O(2^N·N) | AC | 0.031 s | 1780 KB |
| [1337_graphs.java](1337_graphs.java) | Java 1.8 | graphs | O(2^N·N) | AC | 0.187 s | 4100 KB |
| [1337_graphs.py](1337_graphs.py) | Python 3.12 x64 | graphs | O(2^N·N) | AC | 0.109 s | 1216 KB |
| [1337_graphs.rs](1337_graphs.rs) | Rust 1.75 x64 | graphs | O(2^N·N) | AC | 0.046 s | 580 KB |
