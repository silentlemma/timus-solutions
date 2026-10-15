# 1702. Cruce

[Timus 1702](https://acm.timus.ru/problem.aspx?space=1&num=1702) · dificultad 2314 · backtracking

Problema original de Sergey Pupyrev, del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los coches llegan a un cruce por cuatro lados, y cada lado se divide en
tres flujos: giro a la derecha, recto y giro a la izquierda. Son 12
flujos con sus propios semáforos. El flujo i tiene nᵢ coches y, en
verde, deja pasar vᵢ coches por minuto. Los semáforos cambian una vez
por minuto, y dos flujos pueden estar en verde a la vez solo si no se
cruzan ni acaban en la misma dirección. En 10 minutos, hacer lo más
pequeño posible el mayor número de coches que quede en un flujo.

## Entrada

n₁ … n₁₂ (0 ≤ nᵢ ≤ 1000), y luego v₁ … v₁₂ (1 ≤ vᵢ ≤ 1000).

## Salida

Ese máximo mínimo posible.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 0 0 14 13 0 20 0 0 0 60 7
1 1 1 1 3 1 2 1 1 1 5 1
```

Salida:

```
10
```

## Solución

Según el dibujo del enunciado, los flujos 1–3 vienen del sur, 4–6 del
este, 7–9 del norte y 10–12 del oeste, cada grupo en el orden derecha,
recto, izquierda, con circulación por la derecha. Dibujando sus
trayectorias por el cruce se obtiene el grafo de conflictos: los flujos
de un mismo lado nunca chocan, los que van a la misma dirección siempre
lo hacen, y los demás chocan cuando sus trayectorias se cruzan. Por
ejemplo, el flujo 1 solo choca con 9 y 11. Los semáforos de un minuto
forman un conjunto de flujos compatibles dos a dos, y abrir más flujos
nunca perjudica, así que solo importan los 17 conjuntos maximales.
Cada uno abre exactamente cuatro flujos.

Se busca la respuesta L por bisección. Dejar a lo sumo L coches en el
flujo i requiere ⌈(nᵢ − L) / vᵢ⌉ minutos en verde. La pregunta pasa a
ser si 10 conjuntos maximales cubren esas necesidades, lo que decide
una búsqueda con memoria. Algún minuto debe abrir el flujo con mayor
necesidad restante, así que solo se ramifica por los conjuntos que lo
contienen. Se poda cuando una necesidad supera los minutos restantes o
cuando la suma supera cuatro veces los minutos restantes. La búsqueda
es pequeña: muy por debajo de 0.1 s por entrada.

Trampas:

- un flujo que necesita más de 10 minutos hace imposible ese L de
  inmediato;
- el grafo de conflictos sale del dibujo, así que toda la dificultad es
  entender bien la numeración (y la regla de fusión con igual
  destino);
- dos flujos que se cruzan, de 100 coches a 10 por minuto, se reparten
  los 10 minutos y dejan 50 cada uno (test 06).

Las respuestas coinciden con una implementación aceptada independiente
en 310 entradas aleatorias, incluidos flujos densos que necesitan tres
o cuatro minutos cada uno.

Complejidad: `O(S^T·log C)` para S = 17 conjuntos maximales de
semáforos, T = 10 minutos y C el mayor número de coches, para la
búsqueda binaria.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1702_backtracking.cpp](1702_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(S^T·log C) | AC | 0.015 s | 280 KB |
| [1702_backtracking.go](1702_backtracking.go) | Go 1.14 x64 | backtracking | O(S^T·log C) | AC | 0.046 s | 1880 KB |
| [1702_backtracking.java](1702_backtracking.java) | Java 1.8 | backtracking | O(S^T·log C) | AC | 0.187 s | 6920 KB |
| [1702_backtracking.py](1702_backtracking.py) | Python 3.12 x64 | backtracking | O(S^T·log C) | AC | 0.125 s | 1712 KB |
| [1702_backtracking.rs](1702_backtracking.rs) | Rust 1.75 x64 | backtracking | O(S^T·log C) | AC | 0.031 s | 552 KB |
