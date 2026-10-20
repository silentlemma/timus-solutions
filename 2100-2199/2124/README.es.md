# 2124. Orden del subgrupo generado por un rango con multiplicación por rangos

[Timus 2124](https://acm.timus.ru/problem.aspx?space=1&num=2124) · dificultad 1303 · number_theory, segment_tree

Problema original de Alexey Danilyuk, del concurso t.me/umnik_team, campamento de Petrozavodsk, verano de 2018.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se trabaja en el grupo multiplicativo módulo un primo p. Un arreglo de n
restos recibe q consultas: multiplicar cada elemento de [l, r] por x, o
imprimir el orden del subgrupo generado por los elementos de [l, r]. Los
límites son 4 segundos y 256 MB.

## Entrada

p, n y q, 2 ≤ p < 10⁹ primo, 1 ≤ n, q ≤ 10⁵, el arreglo, 1 ≤ aᵢ < p, y
las consultas "1 l r x" y "2 l r", con 1 ≤ l ≤ r ≤ n y 1 ≤ x < p.

## Salida

La respuesta a cada consulta del segundo tipo.

## Ejemplos

### Ejemplo 1

Entrada:

```
17 3 7
10 16 2
2 2 3
2 1 2
2 2 2
1 1 2 3
2 1 1
2 3 3
2 1 3
```

Salida:

```
8
16
2
4
8
16
```

## Solución

El grupo es cíclico de orden m = p − 1. Para un generador g, el elemento
gᵉ genera el subgrupo de índice gcd(e, m), y un conjunto genera el
subgrupo cuyo índice es el mcd de los índices de sus elementos; el orden
es m dividido por ese índice. El índice de un elemento a es m / ord(a),
y ord(a) sale de los factores primos de m: se empieza en m y se divide
por un primo q mientras a elevado al orden actual entre q siga siendo 1.
No hace falta ningún logaritmo discreto.

Una multiplicación por rango cambia muchos elementos, así que se guardan
los cocientes bᵢ = aᵢ / aᵢ₋₁ (b₁ = a₁). Multiplicar [l, r] por x
multiplica b_l por x y b_{r+1} por x⁻¹, dos cambios puntuales. Los
elementos a_l, a_{l+1}, …, a_r generan el mismo subgrupo que a_l,
b_{l+1}, …, b_r, porque cada conjunto se escribe a partir del otro. Así:

- un árbol de segmentos guarda el mcd de los índices de los cocientes y
  da el mcd sobre b_{l+1} … b_r;
- un árbol de Fenwick guarda los multiplicadores de los cambios en los
  extremos; su producto prefijo por el a_l original da el a_l actual.

Una consulta calcula el índice de a_l, toma el mcd con el árbol e
imprime m dividido por él. En C++, Go, Java y Rust, cada cambio o consulta
usa O(log n) operaciones de árboles y O(log² p) operaciones modulares para
órdenes e inversos. La factorización por división cuesta O(sqrt p), y los
índices iniciales de los cocientes cuestan O(n log² p). Los inversos salen
del pequeño teorema de Fermat.

La rama alternativa de Python calcula los índices de forma diferida y
guarda en cada nodo la proyección del mcd sobre el divisor comprobado.
Una consulta puede visitar O(n) nodos, por lo que no tiene la cota por
consulta de las otras versiones. Entre invalidaciones, el divisor guardado
crece por divisibilidad como máximo O(log p) veces. Cada cambio invalida
O(log n) nodos, y una proyección no guardada cuesta O(log² p), lo que da
la cota total amortizada conservadora de la tabla.
S representa el coste de buscar una raíz primitiva y construir las tablas
de logaritmos en Python; en la rama alternativa, S = 0.

Trampa: el test 11 cubre una potencia de primo (p = 257), y el test 13 cubre
ocho factores primos distintos; ambos casos importan al elegir la rama de
Python. Esto no garantiza consultas diferidas logarítmicas: con
p = 999999503, n = 100000 y todos los valores iguales a 1, la primera
consulta `2 1 100000` imprime correctamente 1, pero realiza O(n) trabajo
diferido del árbol.

En el ejemplo p = 17 y m = 16. El elemento 16 = −1 tiene orden 2, y 10 y
16 juntos generan un subgrupo de orden 16, el grupo entero.

## Notas por lenguaje

- Python usa logaritmos discretos si cada componente de orden potencia de
  primo cabe en una tabla o se divide en dos dígitos cuyas tablas tienen
  como máximo min(65536, n + q) entradas. Los componentes coprimos pueden
  compartir una tabla, y el teorema chino del resto combina sus logaritmos.
  La multiplicación por rango se convierte en suma de exponentes, con un
  árbol de segmentos para mcd y un Fenwick aditivo. En otro caso se usa la
  rama alternativa de índices de cocientes diferidos descrita arriba.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2124_number_theory_segment_tree.cpp](2124_number_theory_segment_tree.cpp) | G++ 13.2 x64 | number_theory, segment_tree | O(sqrt p + (n + q) log(n + 1) log^2 p) | AC | 1.015 s | 4244 KB |
| [2124_number_theory_segment_tree.go](2124_number_theory_segment_tree.go) | Go 1.14 x64 | number_theory, segment_tree | O(sqrt p + (n + q) log(n + 1) log^2 p) | AC | 1.156 s | 14484 KB |
| [2124_number_theory_segment_tree.java](2124_number_theory_segment_tree.java) | Java 1.8 | number_theory, segment_tree | O(sqrt p + (n + q) log(n + 1) log^2 p) | AC | 1.593 s | 7364 KB |
| [2124_number_theory_segment_tree.py](2124_number_theory_segment_tree.py) | PyPy 3.10 x64 | number_theory, segment_tree | O(sqrt p + S + (n + q log(n + 1)) log^3 p) | AC | 2.046 s | 51480 KB |
| [2124_number_theory_segment_tree.rs](2124_number_theory_segment_tree.rs) | Rust 1.75 x64 | number_theory, segment_tree | O(sqrt p + (n + q) log(n + 1) log^2 p) | AC | 0.765 s | 10952 KB |
