# 1701. Ostap y sus socios

[Timus 1701](https://acm.timus.ru/problem.aspx?space=1&num=1701) · dificultad 641 · dsu

Problema original de Dmitry Ivankov, del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cuaderno contiene afirmaciones «el empleado i gana d más que el
empleado j». El empleado 0, Vasili, gana 0, y nadie más gana más de
10⁹ (ni menos de 0). Hallar salarios que cumplan todas las
afirmaciones, o el número de la primera afirmación que no puede
cumplirse junto con las anteriores.

## Entrada

n y m (1 ≤ n, m ≤ 50000), y luego m afirmaciones i j d
(0 ≤ i, j < n; |d| ≤ 20000).

## Salida

Possible y los n salarios, o «Impossible after i statements». Se acepta
cualquier conjunto de salarios válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 6
3 4 1200
4 1 -5500
2 3 4300
3 0 8200
0 4 -7000
2 1 0
```

Salida:

```
Possible
0
12500
12500
8200
7000
```

### Ejemplo 2

Entrada:

```
3 5
1 2 5
0 2 0
1 0 -5
1 2 5
2 2 0
```

Salida:

```
Impossible after 3 statements
```

### Ejemplo 3

Entrada:

```
3 2
1 0 871
1 2 903
```

Salida:

```
Impossible after 2 statements
```

## Solución

Se procesan las afirmaciones en orden con una unión-búsqueda con pesos.
Cada empleado guarda la diferencia entre su salario y el de su padre,
así que salary(x) = salary(root) + offset(x) tras comprimir el camino.
Cada conjunto guarda además el rango de valores que puede tomar el
salario de su raíz para que todos sus salarios queden en 0 … 10⁹. El
conjunto de Vasili empieza con el único valor 0.

Una afirmación salary(i) − salary(j) = d dentro de un conjunto debe
concordar con los desplazamientos. Entre dos conjuntos fija
salary(rⱼ) = salary(rᵢ) + shift. El rango de la raíz unida es el rango
antiguo intersecado con el de la otra raíz desplazado en −shift, y un
rango vacío significa que la afirmación lo rompe todo. Al final cada
raíz toma el menor valor de su rango y todos los salarios salen de los
desplazamientos. `O((n + m) α(n))`.

Trampas:

- una afirmación puede contradecir solo los límites, no las demás
  afirmaciones: en el tercer ejemplo la segunda deja un salario
  negativo;
- una afirmación puede comparar a un empleado consigo mismo, y entonces
  d debe ser 0 (test 05);
- el límite superior nunca actúa aquí, pues |d| ≤ 20000 y a lo sumo
  49999 enlaces mantienen toda diferencia por debajo de 10⁹, pero el
  inferior sí;
- las búsquedas de la raíz no usan recursión, porque antes de comprimir
  los conjuntos forman cadenas largas.

El verificador comprueba el 0 de Vasili, los rangos y cada afirmación,
o la línea Impossible exacta; una implementación aceptada independiente
lo pasa con las mismas pruebas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1701_dsu.cpp](1701_dsu.cpp) | G++ 13.2 x64 | dsu | O((n + m) α(n)) | AC | 0.093 s | 2784 KB |
| [1701_dsu.go](1701_dsu.go) | Go 1.14 x64 | dsu | O((n + m) α(n)) | AC | 0.125 s | 5940 KB |
| [1701_dsu.java](1701_dsu.java) | Java 1.8 | dsu | O((n + m) α(n)) | AC | 0.109 s | 6448 KB |
| [1701_dsu.py](1701_dsu.py) | Python 3.12 x64 | dsu | O((n + m) α(n)) | AC | 0.343 s | 18488 KB |
| [1701_dsu.rs](1701_dsu.rs) | Rust 1.75 x64 | dsu | O((n + m) α(n)) | AC | 0.046 s | 5124 KB |
