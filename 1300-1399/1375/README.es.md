# 1375. Inconformismo

[Timus 1375](https://acm.timus.ru/problem.aspx?space=1&num=1375) · dificultad 541 · number_theory

Problema original de Den Raskovalov, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados un primo p ≤ 10⁶ y 0 ≤ k ≤ p − 1, hay que imprimir cualesquiera x
e y de 0 a p − 1 con x² + y² ≡ k (mod p), o `NO SOLUTION` si no los
hay.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

k y p.

## Salida

x e y, o `NO SOLUTION`.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 3
```

Salida:

```
0 2
```

## Solución

Para un primo impar p, los cuadrados toman (p + 1) / 2 valores
distintos módulo p, y lo mismo los valores k − x². Dos conjuntos de
(p + 1) / 2 valores entre p tienen que cortarse, así que algún x² y algún
y² suman k: siempre hay respuesta, y `NO SOLUTION` no aparece nunca.
Para p = 2 todo k es 0² + 0² o 1² + 0².

Para hallarla, se guarda una raíz de cada cuadrado: para y de 0 a p − 1
se anota y como raíz de y² mod p. Luego se prueba x = 0, 1, 2, … hasta
que k − x² mod p tenga raíz. Alrededor de la mitad de los valores son
cuadrados, así que esto acaba casi enseguida. `O(p)`.

Detalles a tener en cuenta:

- k = 0 tiene la respuesta 0 0 (prueba 07);
- k − x² debe tomarse módulo p como número no negativo;
- y² se acerca a 10¹², más de lo que cabe en 32 bits.

La respuesta se comprobó para todo k y todo primo menor que 300, y las
pruebas se juzgan con un verificador que acepta cualquier par.

## Notas por lenguaje

- Las cinco soluciones guardan la tabla de raíces en un arreglo de p
  números.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1375_number_theory.cpp](1375_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(p) | AC | 0.031 s | 3656 KB |
| [1375_number_theory.go](1375_number_theory.go) | Go 1.14 x64 | number_theory | O(p) | AC | 0.062 s | 9624 KB |
| [1375_number_theory.java](1375_number_theory.java) | Java 1.8 | number_theory | O(p) | AC | 0.156 s | 5172 KB |
| [1375_number_theory.py](1375_number_theory.py) | Python 3.12 x64 | number_theory | O(p) | AC | 0.359 s | 23992 KB |
| [1375_number_theory.rs](1375_number_theory.rs) | Rust 1.75 x64 | number_theory | O(p) | AC | 0.046 s | 7892 KB |
