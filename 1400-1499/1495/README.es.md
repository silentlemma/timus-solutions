# 1495. Un-dos, un-dos 2

[Timus 1495](https://acm.timus.ru/problem.aspx?space=1&num=1495) · dificultad 340 · bfs

Problema original de Igor Chevdar, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que hallar el menor número escrito solo con las cifras 1 y 2 que sea
divisible entre N (1 ≤ N ≤ 10⁶). Si no existe o tiene más de 30 cifras,
se escribe «Impossible».

Límite de tiempo: 2 segundos. Límite de memoria: 256 MB.

## Entrada

N.

## Salida

El número, o «Impossible».

## Ejemplos

### Ejemplo 1

Entrada:

```
5
```

Salida:

```
Impossible
```

### Ejemplo 2

Entrada:

```
8
```

Salida:

```
112
```

## Solución

Para lo que puede seguir a un prefijo solo importa su resto módulo N,
así que se busca en anchura sobre los restos. Se parte de los números 1
y 2, y desde un número con resto r se va a r·10 + 1 y luego a
r·10 + 2. Los números más cortos se alcanzan antes, y dentro de una
misma longitud la cola sigue el orden numérico, así que el primer
número que llega a un resto es el menor con ese resto; cualquier otro
posterior, y todas sus prolongaciones, serían mayores. Cada uno de los
N restos se guarda una vez con su última cifra y su padre, y la
respuesta se reconstruye por los padres en cuanto aparece el resto 0.
Los números dejan de crecer a las 30 cifras. `O(N)`.

Detalles a tener en cuenta:

- un número de unos y doses nunca acaba en 0 ni en 5, así que los
  múltiplos de 5 son imposibles (pruebas 01, 07, 09);
- la respuesta puede tener exactamente 30 cifras, como para 999999, y
  eso aún se admite (prueba 05);
- r·10 + d queda por debajo de 10⁷, pero la respuesta completa puede superar
  el rango de los enteros de 64 bits; se reconstruye a partir de sus cifras
  (pruebas 05, 08).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1495_bfs.cpp](1495_bfs.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.046 s | 14636 KB |
| [1495_bfs.go](1495_bfs.go) | Go 1.14 x64 | bfs | O(N) | AC | 0.093 s | 32440 KB |
| [1495_bfs.java](1495_bfs.java) | Java 1.8 | bfs | O(N) | AC | 0.156 s | 17324 KB |
| [1495_bfs.py](1495_bfs.py) | Python 3.12 x64 | bfs | O(N) | AC | 0.906 s | 62744 KB |
| [1495_bfs.rs](1495_bfs.rs) | Rust 1.75 x64 | bfs | O(N) | AC | 0.062 s | 26080 KB |
