# 1851. Prácticas en GOV

[Timus 1851](https://acm.timus.ru/problem.aspx?space=1&num=1851) · dificultad 1708 · flow

Problema original de Mikhail Rubinchik, del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La distancia de un patrón p a una cadena s es la suma de las distancias
de Hamming de p a todas las subcadenas de s de longitud |p|. Algunos
caracteres de s y de p están borrados; restaurarlos para que esa
distancia sea la menor posible.

## Entrada

La cadena s y el patrón p, ambos no vacíos, de como mucho 1000
caracteres de "0", "1" y "?", con |p| ≤ |s|; "?" marca un carácter
borrado.

## Salida

La menor distancia, y luego s y p con cada "?" cambiado por "0" o "1".
Se acepta cualquier restauración óptima.

## Ejemplos

### Ejemplo 1

Entrada:

```
00?
1?
```

Salida:

```
2
000
10
```

## Solución

El carácter p[i] se compara con s[j] una vez en cada ventana que los
junta, lo que ocurre exactamente cuando 0 ≤ j − i ≤ |s| − |p|, y cada
par así cuesta 1 si los caracteres difieren. Como cada carácter es 0 o
1, es un problema de corte: cada carácter borrado va a un grafo, los 1
del lado de la fuente y los 0 del lado del sumidero.

- Un par de caracteres conocidos suma su coste directamente.
- Un par de un carácter borrado y un 1 conocido cuesta 1 si el borrado
  pasa a ser 0: un arco de capacidad 1 desde la fuente hasta él; un 0
  conocido da un arco de capacidad 1 hacia el sumidero. Todos esos arcos
  de un carácter se juntan en uno, y si un carácter tiene de los dos
  tipos, el menor se paga de todos modos y se resta de ambos.
- Un par de dos caracteres borrados cuesta 1 si se separan: una arista
  no dirigida de capacidad 1.

El coste de una restauración es la parte fija más la capacidad del
corte que define, así que la respuesta es la parte fija más un flujo
máximo, aquí con el algoritmo de Dinic, y el lado de la fuente en la red
residual tras la última búsqueda da la restauración. Hay como mucho
2000 caracteres borrados y |p|·(|s| − |p| + 1) ≤ 250 500 pares.

En el ejemplo p[0] = 1 se encuentra con s[0] = 0 y s[1] = 0, lo que
cuesta 2 pase lo que pase. p[1] se encuentra con s[1] = 0 y con s[2]:
restaurar ambos caracteres borrados como 0 no cuesta nada más, así que
la respuesta es 2.

Trampas:

- p[i] solo se encuentra con s[i] … s[i + |s| − |p|], no con todos los
  caracteres de s;
- un arco desde la fuente y otro hacia el sumidero en un mismo nodo se
  compensan antes del flujo, y el flujo queda pequeño;
- cualquier corte mínimo es válido, así que la salida se comprueba
  recalculando la distancia.

Las restauraciones pasan un verificador que recalcula la distancia y la
compara con el óptimo, hallado probando todas las restauraciones en
trescientos casos cortos y con una implementación aceptada independiente
en los largos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1851_flow.cpp](1851_flow.cpp) | G++ 13.2 x64 | flow | O(V^2 E) | AC | 0.031 s | 7004 KB |
| [1851_flow.go](1851_flow.go) | Go 1.14 x64 | flow | O(V^2 E) | AC | 0.031 s | 26920 KB |
| [1851_flow.java](1851_flow.java) | Java 1.8 | flow | O(V^2 E) | AC | 0.125 s | 6448 KB |
| [1851_flow.py](1851_flow.py) | Python 3.12 x64 | flow | O(V^2 E) | AC | 0.640 s | 31084 KB |
| [1851_flow.rs](1851_flow.rs) | Rust 1.75 x64 | flow | O(V^2 E) | AC | 0.046 s | 13644 KB |
