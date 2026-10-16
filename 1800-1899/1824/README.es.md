# 1824. Bombardeo de ifrits

[Timus 1824](https://acm.timus.ru/problem.aspx?space=1&num=1824) · dificultad 1063 · backtracking

Problema original de Igor Andrianov, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n ciudades, puntos del plano. Una botella lanzada sobre una ciudad
destruye todas las ciudades a distancia no mayor que r. Las botellas
solo pueden lanzarse sobre ciudades. Hallar el menor número de botellas
que destruyen todas las ciudades y las ciudades donde lanzarlas.

## Entrada

n y r (1 ≤ n ≤ 30, 1 ≤ r ≤ 1000), luego n líneas con las coordenadas
enteras de las ciudades, de 0 a 1000.

## Salida

El menor número de botellas y luego los números de las ciudades donde
lanzarlas. Se acepta cualquier elección óptima.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 50
10 10
500 500
501 501
999 999
```

Salida:

```
3
1 3 4
```

## Solución

Es un conjunto dominante mínimo del grafo que une ciudades a distancia
no mayor que r, con 30 vértices, así que el alcance de cada ciudad cabe
en una máscara de bits cover[i].

Se prueban presupuestos k = 1, 2, … y se buscan como mucho k
lanzamientos que cubran el conjunto de ciudades que quedan. Algún
lanzamiento debe alcanzar a la ciudad sin cubrir u con menos ciudades a
su alcance, así que la búsqueda solo ramifica por las ciudades al
alcance de u, primero las que dan más impactos nuevos. Tres podas la
mantienen pequeña:

- si ni siquiera k lanzamientos con la mayor ganancia actual cubren lo
  que queda, se abandona;
- se salta un candidato cuyos impactos nuevos son subconjunto de los de
  un candidato ya probado, porque su rama solo puede ser peor;
- un estado fallido (ciudades restantes, presupuesto) se recuerda y no
  se vuelve a buscar con el mismo presupuesto o uno menor.

El primer presupuesto que tiene éxito es óptimo. Hay como máximo 2^n
máscaras y n presupuestos, con O(n^2) de trabajo por estado expandido.
Una cota conservadora es O(n^3 * 2^n) de tiempo y O(2^n + n^2) de espacio.

En el ejemplo las ciudades 2 y 3 distan √2 y una botella se lleva
ambas, mientras que 1 y 4 están lejos de todo: tres botellas.

Trampas:

- una distancia exactamente r cuenta como impacto, así que se comparan
  cuadrados enteros;
- nada prohíbe dos ciudades en el mismo punto;
- elegir con avidez la ciudad que alcanza más no es óptimo.
- las coordenadas de los grupos (prueba `gen3`, modo 3 del generador)
  deben estar en [0,1000]: la semilla 11 producía y = 1006. Ahora el
  generador limita cada coordenada a ese intervalo.

Los números coinciden con un oráculo exacto e independiente que enumera
subconjuntos en 1.200 mapas aleatorios pequeños.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1824_backtracking.cpp](1824_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(n^3 * 2^n) worst case | AC | 0.031 s | 220 KB |
| [1824_backtracking.go](1824_backtracking.go) | Go 1.14 x64 | backtracking | O(n^3 * 2^n) worst case | AC | 0.031 s | 1204 KB |
| [1824_backtracking.java](1824_backtracking.java) | Java 1.8 | backtracking | O(n^3 * 2^n) worst case | AC | 0.156 s | 3944 KB |
| [1824_backtracking.py](1824_backtracking.py) | Python 3.12 x64 | backtracking | O(n^3 * 2^n) worst case | AC | 0.078 s | 656 KB |
| [1824_backtracking.rs](1824_backtracking.rs) | Rust 1.75 x64 | backtracking | O(n^3 * 2^n) worst case | AC | 0.015 s | 420 KB |
