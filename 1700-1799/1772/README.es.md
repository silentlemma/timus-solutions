# 1772. Pistas de esquí para robots

[Timus 1772](https://acm.timus.ru/problem.aspx?space=1&num=1772) · dificultad 738 · segment_tree

Problema original de Alex Samsonov, del XIV Campeonato de los Urales de Programación Competitiva, 10 de abril de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n pistas paralelas van de la salida a la meta, y un esquiador sale por
la pista s. En el recorrido encuentra en orden k robots caídos, cada uno
cortando las pistas de l a r; entre ellos puede moverse de lado, una
pista por segundo. Ningún robot corta todas las pistas. Hallar el menor
número de segundos de pasos laterales para superarlos a todos.

## Entrada

n, s y k (2 ≤ n ≤ 10⁵, 1 ≤ s ≤ n, 0 ≤ k ≤ 10⁵) y luego los k tramos
cortados l y r (1 ≤ l ≤ r ≤ n) en el orden en que se encuentran.

## Salida

El menor número de segundos.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3 2
2 5
1 4
```

Salida:

```
6
```

## Solución

Sea f(x) el menor tiempo para estar en la pista x tras los robots ya
encontrados, libre para seguir. Al principio f(x) = |x − s|, y f nunca
cambia más de 1 entre pistas vecinas, porque un paso más corrige la
diferencia. Un robot en las pistas de l a r no cambia f fuera de ellas,
y dentro pone f(x) = min(f(l − 1) + (x − l + 1), f(r + 1) + (r + 1 − x)):
el esquiador pasa por la pista l − 1 o r + 1 y luego vuelve a entrar.
Rodear más lejos nunca ayuda, pues allí f ya es mínima por la regla del
paso.

Así cada robot asigna a un tramo de pistas una función de la forma
min(a + x, b − x), y f(x) la da el último robot que cubre x, o la
salida si no hay ninguno. Un árbol de segmentos guarda en cada nodo el
último robot cuyo tramo cubre el nodo entero; el último robot sobre una
pista es el mayor de ellos en su camino a la raíz. Cada robot necesita
dos consultas y una asignación, y la respuesta es el menor f sobre
todas las pistas al final. `O((n + k) log n)`.

En el ejemplo f empieza como 2 1 0 1 2. El robot de las pistas 2 a 5
deja la pista 1 en 2 y pone el resto en 3 4 5 6; el robot de las pistas
1 a 4 deja la pista 5 en 6 y pone el resto en 10 9 8 7, así que la
respuesta es 6.

Trampas:

- un robot que toca un borde solo se puede rodear por un lado;
- el total puede llegar a unos 10¹⁰ cuando los robots obligan a ir de
  borde a borde, más de 32 bits;
- las pistas dentro de un tramo cortado vuelven a servir justo después
  de él.

Las respuestas coinciden con una programación dinámica pista a pista
sobre todos los movimientos en 400 casos aleatorios de hasta 9 pistas y
con una implementación aceptada independiente en 48 casos con hasta 10⁵
pistas y robots. La solución en Python corre en PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1772_segment_tree.cpp](1772_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O((n + k) log n) | AC | 0.156 s | 2372 KB |
| [1772_segment_tree.go](1772_segment_tree.go) | Go 1.14 x64 | segment_tree | O((n + k) log n) | AC | 0.203 s | 8136 KB |
| [1772_segment_tree.java](1772_segment_tree.java) | Java 1.8 | segment_tree | O((n + k) log n) | AC | 0.140 s | 3184 KB |
| [1772_segment_tree.py](1772_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O((n + k) log n) | AC | 0.359 s | 19444 KB |
| [1772_segment_tree.rs](1772_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O((n + k) log n) | AC | 0.031 s | 6500 KB |
