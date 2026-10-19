# 1890. Dinero de la nada

[Timus 1890](https://acm.timus.ru/problem.aspx?space=1&num=1890) · dificultad 465 · fenwick

Problema original de Dmitry Ivankov, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un árbol con raíz contiene n empleados, numerados de 0 a n − 1, con
raíz 0. Cada vértice tiene un salario entero no negativo. Hay que
procesar q actualizaciones condicionales en el orden dado:

- `employee x y z`: si el salario actual de x es estrictamente menor
  que y, aumentarlo en z;
- `department x y z`: si el salario medio actual del subárbol de x es
  estrictamente menor que y, aumentar en z cada salario de ese
  subárbol, incluido x.

Hay que obtener todos los salarios finales. El árbol no cambia.
Los límites son 1 segundo y 64 MB.

## Entrada

La primera línea contiene n, q y el salario inicial s₀ de la raíz:
1 ≤ n, q ≤ 50 000 y 0 ≤ s₀ ≤ 10⁹.

Para cada i de 1 a n − 1, la siguiente línea contiene su padre pᵢ y
su salario inicial sᵢ, con 0 ≤ pᵢ < i y 0 ≤ sᵢ ≤ 10⁹.

Las siguientes q líneas contienen las actualizaciones en el formato
anterior, con 0 ≤ x < n y 1 ≤ y, z ≤ 10⁹.

## Salida

Escribir los n salarios finales, uno por línea, en orden creciente de
número de vértice.

## Evaluación

Las salidas se comparan como secuencias de tokens enteros.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3 1
0 10
0 10
1 10
employee 2 15 1
employee 3 5 1
department 0 10 1
```

Salida:

```
2
11
12
11
```

## Solución

Ordenar el árbol en preorden. Sean tin[x] la posición de x y size[x]
el tamaño de su subárbol. El subárbol ocupa exactamente el intervalo
[tin[x], tin[x] + size[x]).

Como cada padre tiene un número menor que sus hijos, calcular los
tamaños de subárbol sumándolos a sus padres en orden decreciente de
vértice. Después procesar los vértices en orden creciente. Cada padre
reserva un bloque consecutivo de longitud size[x] para un hijo x,
después de su propia posición y de los bloques de hijos ya reservados.
Así se obtienen las posiciones de preorden en `O(n)`, sin recursión.

Mantener los salarios en este orden mediante dos árboles de Fenwick
que permiten sumar un valor en un intervalo y consultar su suma.
Para construir esta estructura, sea dᵢ la diferencia entre salarios
consecutivos, con índices desde 1, donde d₁ es el primer salario.
El primer árbol guarda dᵢ y el segundo guarda (i − 1)dᵢ. Si sus sumas
de prefijo hasta k son B₁(k) y
B₂(k), la suma de los primeros k salarios es k·B₁(k) − B₂(k). Sumar z
en un intervalo solo cambia las dos diferencias de sus extremos, por
lo que cada árbol necesita únicamente dos actualizaciones puntuales.
La suma de un intervalo es la diferencia de dos sumas de prefijo.

Para `employee`, consultar el intervalo de un solo elemento de x.
Para `department`, consultar todo su subárbol y llamar S a la suma.
La condición de la media se comprueba exactamente como S < y·size[x],
sin división ni números de coma flotante. Si se cumple la desigualdad
estricta correspondiente, sumar z en el mismo intervalo; en otro caso
no cambiar nada.

Los intervalos de preorden seleccionan exactamente los empleados
indicados. La fórmula de Fenwick devuelve la suma de salarios actual
después de todas las operaciones anteriores, por lo que tanto la
condición como el incremento coinciden con la operación requerida.
Al terminar, deshacer la construcción del primer árbol de Fenwick:
en orden decreciente de índice, restar cada entrada de su padre de
Fenwick. Las entradas pasan a contener las diferencias actuales dᵢ.
Una suma de prefijos recupera todos los salarios en tiempo lineal;
escribirlos en el orden original de vértices.

Cada consulta o incremento cuesta `O(log n)`. Construir los árboles
iniciales acumulando cada entrada en su padre de Fenwick en orden
creciente de índice. Tanto la inicialización como la recuperación
final son lineales, así que el tiempo total es `O(n + q log n)` y
la memoria es `O(n)`.

En el ejemplo, el salario del empleado 2 pasa de 10 a 11. El del
empleado 3 sigue siendo 10 porque 10 no es menor que 5. La suma de
todo el árbol es ahora 32 y la media es 8, menor que 10. La última
operación suma 1 a todos los salarios: quedan 2, 11, 12 y 11.

Trampas:

- la igualdad con el umbral no activa una actualización;
- un subárbol incluye su raíz y todos sus descendientes;
- los números originales de un subárbol no tienen por qué ser consecutivos;
- usar enteros con signo de 64 bits para salarios, sumas, diferencias
  ponderadas y productos como y·size[x]; los enteros de Python bastan;
- escribir por número de vértice, no por posición de recorrido.

## Notas por lenguaje

Usar entrada y salida con búfer. En los lenguajes con enteros de ancho
fijo, las entradas de Fenwick necesitan 64 bits; los índices del árbol
pueden seguir siendo enteros ordinarios.

Las respuestas coinciden con una simulación por fuerza bruta en 160
casos aleatorios pequeños y con una implementación aceptada
independiente en 37 casos generados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1890_fenwick.cpp](1890_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n + q log n) | AC | 0.062 s | 2728 KB |
| [1890_fenwick.go](1890_fenwick.go) | Go 1.14 x64 | fenwick | O(n + q log n) | AC | 0.046 s | 11840 KB |
| [1890_fenwick.java](1890_fenwick.java) | Java 1.8 | fenwick | O(n + q log n) | AC | 0.187 s | 6316 KB |
| [1890_fenwick.py](1890_fenwick.py) | Python 3.12 x64 | fenwick | O(n + q log n) | AC | 0.843 s | 29672 KB |
| [1890_fenwick.rs](1890_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n + q log n) | AC | 0.046 s | 7924 KB |
