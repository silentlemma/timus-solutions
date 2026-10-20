# 2150. Repartir un grafo de amistad denso en parejas y tríos

[Timus 2150](https://acm.timus.ru/problem.aspx?space=1&num=2150) · dificultad 1167 · greedy, matching

Problema original de Semyon Trifochkin, del Concurso Escolar de Programación de los Urales 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n alumnos, cada uno amigo de al menos ⌈n / 2⌉ de los demás, deben
repartirse en grupos de dos o tres en los que todos se conocen. Imprimir
un reparto o NO. Se acepta cualquier reparto válido. Los límites son 1
segundo y 256 MB.

## Entrada

n, 2 ≤ n ≤ 1000, y luego la matriz simétrica de amistad.

## Salida

NO, o YES, el número de grupos y cada grupo con su tamaño y miembros.

## Evaluación

Un comprobador verifica que los grupos cubren a cada alumno una vez y
que todos los miembros de un grupo son amigos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 1
1 0
```

Salida:

```
YES
1
2 1 2
```

### Ejemplo 2

Entrada:

```
5
0 1 0 1 1
1 0 1 0 1
0 1 0 1 1
1 0 1 0 1
1 1 1 1 0
```

Salida:

```
YES
2
3 1 2 5
2 3 4
```

## Solución

La respuesta siempre es YES: existe un emparejamiento casi perfecto, y
el alumno que sobra con n impar puede unirse a una de sus parejas.

Se toma un emparejamiento maximal voraz. Los alumnos sin pareja no son
amigos entre sí, o la pasada voraz los habría emparejado, así que todos
sus amigos están emparejados. Para dos alumnos sin pareja u y v hay una
pareja (a, b) con u amigo de a y v amigo de b, o al revés: si no, cada
pareja recibiría a lo sumo dos de las aristas de u y v, como mucho n − 2
en total, mientras que u y v tienen juntos al menos n amigos. Cambiar
(a, b) por (u, a) y (v, b) añade una pareja, así que los alumnos sin
pareja se arreglan de dos en dos.

Si n es impar queda un alumno w. Tiene al menos ⌈n / 2⌉ amigos, más que
las (n − 1) / 2 parejas, así que los dos alumnos de alguna pareja son sus
amigos, y esa pareja se convierte en un trío con w. Cada paso recorre las
parejas una vez por alumno arreglado, O(n²) en total.

En el segundo ejemplo el alumno 5 conoce a todos, así que la pareja
(1, 2) toma al alumno 5 como tercer miembro y (3, 4) sigue siendo pareja.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2150_greedy_matching.cpp](2150_greedy_matching.cpp) | G++ 13.2 x64 | greedy, matching | O(n^2) | AC | 0.031 s | 540 KB |
| [2150_greedy_matching.go](2150_greedy_matching.go) | Go 1.14 x64 | greedy, matching | O(n^2) | AC | 0.031 s | 6248 KB |
| [2150_greedy_matching.java](2150_greedy_matching.java) | Java 1.8 | greedy, matching | O(n^2) | AC | 0.156 s | 1532 KB |
| [2150_greedy_matching.py](2150_greedy_matching.py) | Python 3.12 x64 | greedy, matching | O(n^2) | AC | 0.187 s | 19168 KB |
| [2150_greedy_matching.rs](2150_greedy_matching.rs) | Rust 1.75 x64 | greedy, matching | O(n^2) | AC | 0.031 s | 3292 KB |
