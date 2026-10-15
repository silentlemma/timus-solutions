# 1721. Las dos caras de la misma moneda

[Timus 1721](https://acm.timus.ru/problem.aspx?space=1&num=1721) · dificultad 581 · matching

Problema original de Pavel Atnashev, de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada problema lo preparan dos personas: una escribe el enunciado, la
otra prepara las pruebas, y sus rangos difieren exactamente en 2. Cada
persona escribe enunciados, prepara pruebas o sabe hacer ambas cosas, y
participa en a lo sumo un problema. Hallar el mayor número de problemas
y quién prepara cada uno.

## Entrada

n (2 ≤ n ≤ 1000) y luego n líneas: un nombre de hasta 20 letras
latinas, la especialidad `statements`, `testdata` o `anything` y el
rango, un entero de 3 a 1000. Todos los nombres son distintos.

## Salida

El mayor número de problemas y luego, para cada problema, el nombre de
quien escribe el enunciado y el de quien prepara las pruebas. Se acepta
cualquier plan óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
Poll anything 8
Tejat statements 6
Mebsuta testdata 6
Propus testdata 4
Alzir anything 7
Mekbuda anything 3
Dirah testdata 9
```

Salida:

```
3
Poll Mebsuta
Tejat Propus
Alzir Dirah
```

## Solución

Se unen dos personas con una arista cuando sus rangos difieren
exactamente en 2 y una puede escribir el enunciado mientras la otra
prepara las pruebas. Un plan es un conjunto de aristas sin personas en
común, así que la tarea es un emparejamiento máximo.

El grafo es bipartito. A lo largo de una arista ⌊rank/2⌋ cambia
exactamente en 1, así que su paridad se invierte: las personas con
⌊rank/2⌋ par forman un lado y las de impar el otro. Construir el grafo
y aplicar Hopcroft–Karp cuesta `O(n² + E √n)`, donde E llega a 250 000 cuando
500 personas tienen rango 3 y 500 rango 5. En cada pareja se asignan
roles válidos; si ambas saben hacer las dos tareas, vale cualquier orden.

En el ejemplo Poll (8) y Mebsuta (6), Tejat (6) y Propus (4), y Alzir
(7) y Dirah (9) forman tres problemas. Mekbuda (3) no tiene a nadie de
rango 1 o 5 y queda fuera.

Trampas:

- los rangos deben diferir exactamente en 2, no en a lo sumo 2;
- dos especialistas `statements`, o dos especialistas `testdata`, nunca forman
  un problema, aunque sus rangos difieran en 2;
- la división en dos lados permite a Hopcroft–Karp buscar caminos de
  aumento sin tratar ciclos impares;
- la solución en Python recorre los caminos de aumento con una pila
  explícita, pues un camino puede pasar por cientos de personas.

El comprobador compara el número con el óptimo y verifica que cada
pareja pueda preparar un problema y que nadie participe dos veces. Los
números coinciden con una búsqueda exhaustiva de todos los planes en
300 conjuntos aleatorios de hasta 8 personas, y con una implementación
aceptada independiente en 60 conjuntos aleatorios de 1000.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1721_matching.cpp](1721_matching.cpp) | G++ 13.2 x64 | matching | O(n² + E √n) | AC | 0.015 s | 924 KB |
| [1721_matching.go](1721_matching.go) | Go 1.14 x64 | matching | O(n² + E √n) | AC | 0.031 s | 4476 KB |
| [1721_matching.java](1721_matching.java) | Java 1.8 | matching | O(n² + E √n) | AC | 0.156 s | 6132 KB |
| [1721_matching.py](1721_matching.py) | Python 3.12 x64 | matching | O(n² + E √n) | AC | 0.171 s | 2840 KB |
| [1721_matching.rs](1721_matching.rs) | Rust 1.75 x64 | matching | O(n² + E √n) | AC | 0.031 s | 1800 KB |
