# 2022. Un Proyectil por una Abertura en una Pared Gruesa

[Timus 2022](https://acm.timus.ru/problem.aspx?space=1&num=2022) · dificultad 3527 · geometry

Problema original de Nick Burlakov, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un punto de lanzamiento despega del suelo en `(0,0)` con velocidad
`(vx,vy)` y gravedad `g=10` hacia abajo. Una pared ocupa `L≤X≤L+l`; su
abertura tiene suelo a altura `h` y techo a altura `h+d`. Mientras el
punto siga en el aire y delante de la pared puede soltar un proyectil
puntual con velocidad inicial **absoluta** `(ux,uy)`. Ambos cuerpos solo
reciben gravedad. Encuentre cualquier instante para atravesar toda la
abertura sin tocar suelo ni techo.

Los ocho enteros `L,h,l,d,vx,vy,ux,uy` están entre 1 y 1 000. Las distancias
son metros y las velocidades metros por segundo; el eje x apunta a la pared.
El tiempo comienza al despegar. El instante dado debe seguir despejado al
adelantarlo o retrasarlo `ε=10⁻⁶` segundos. Se garantiza una respuesta robusta
si existe alguna factible. Límites: 1 segundo y 64 MB.

## Entrada

Primera línea: `L h l d`. Segunda: `vx vy ux uy`.

## Salida

Imprima cualquier instante válido con error absoluto o relativo máximo
`10⁻⁶`, cumpliendo la robustez. Si no existe, imprima `-1`.

## Evaluación

Un comprobador verifica que el proyectil atraviesa toda la abertura para
cualquier momento de lanzamiento a menos de 10⁻⁶ de la respuesta, y que
`-1` solo se imprime si ningún momento sirve; se acepta cualquier
momento así.

## Ejemplos

```
4 2 2 4
1 1 5 10
```

```
0.1
```

```
30 15 5 5
10 10 20 10
```

```
-1
```

## Solución

Al soltar en `t`, el punto está en `(vx t,vy t−5t²)`. Para alcanzar la
coordenada `X`, el proyectil vuela durante `τ=(X−vx t)/ux`, dando altura
`Y(t,X)=vy t−5t²+uy τ−5τ²`. El dominio de lanzamiento es
`0<t<T=min(2vy/10,L/vx)`. La velocidad absoluta no recibe la velocidad
del punto móvil.

Para `t` fijo, la altura es una cuadrática cóncava en `X`, cuyo mínimo
en la pared está en una cara. Exija `Y(t,L)>h` y `Y(t,L+l)>h`.
Multiplicando por `ux²>0` queda `ux²(Y(t,X)−H)=−At²+Bt+C`, con
`A=5(ux²+vx²)`, `B=vy ux²−uy vx ux+10X vx` y
`C=uy X ux−5X²−H ux²`. Cada condición de suelo vale entre las dos raíces
reales, en intervalo abierto; una raíz doble solo toca el suelo.
Interseque ambos intervalos con `(0,T)` para obtener un intervalo abierto `I`.

El techo requiere el máximo, que puede estar **dentro** de la pared.
El vértice del proyectil está en `X*=vx t+ux uy/10`. La altura máxima es:

- `Y(t,L)` si `X*≤L`;
- `vy t−5t²+uy²/20` si `L≤X*≤L+l`;
- `Y(t,L+l)` si `X*≥L+l`.

Los cambios de rama ocurren en `(10L−ux uy)/(10vx)` y
`(10(L+l)−ux uy)/(10vx)`. En cada rama resuelva dónde su cuadrática es
**al menos** `h+d` e interseque el intervalo cerrado de raíces con la rama
y con `I`. Una tangencia puede dejar un único instante prohibido.

Todas las partes prohibidas forman un intervalo por la concavidad conjunta
de `Y(t,X)`: términos lineales menos `5t²` y menos `5((X−vx t)/ux)²`.
Una combinación convexa de los puntos maximizadores de dos tiempos sigue
en el intervalo fijo de la pared. La concavidad conjunta hace que el máximo
del tiempo combinado sea al menos la misma mezcla de ambos máximos.
Así `F(t)=max_X Y(t,X)` es cóncava y `F(t)≥h+d` es un intervalo o punto.
Tome los extremos prohibidos menor y mayor y reste este conjunto **cerrado**
de `I`: quedan como máximo dos componentes abiertas factibles.

Elija el punto medio de la componente más ancha. Una anchura mayor que
`2ε` deja más de `ε` hasta ambas fronteras, incluida una tangencia aislada.
La garantía asegura tal componente cuando hay solución. No una las dos
componentes factibles atravesando la zona prohibida. Solo hay un número
constante de cuadráticas: tiempo y espacio auxiliar `O(1)`.

Para raíces estables de `−At²+Bt+C=0`, calcule `D=B²+4AC` como entero
exacto. Si `D>0`, use `q=(B+copysign(sqrt(D),B))/2` y raíces `q/A`, `−C/q`,
evitando restar valores casi iguales. Trate `D=0` aparte. Las cotas son
`A≤10⁷`, `|B|≤1.02·10⁹`, `|C|≤2.02·10⁹`, `|D|≤1.1212·10¹⁸`;
bastan intermedios enteros con signo de 64 bits. Conserve la precisión
de ida y vuelta del valor elegido al imprimir.

En el primer ejemplo, `t=0.1` da alturas de cara 4.808 y 4.888 y vértice
interior 5.05, estrictamente entre 2 y 6. En el segundo, la altura máxima
del punto móvil más el ascenso adicional del proyectil solo suman 10,
por debajo del suelo de altura 15; no hay solución.

Trampas:

- `h` es el suelo; el techo está en `h+d`.
- Comprobar el vértice interior para el techo, no solo las caras.
- Conservar un punto prohibido de anchura cero en una tangencia exacta.
- Calcular productos en 64 bits antes de convertir a punto flotante.
- Usar el centro de una sola componente con el margen completo ±ε.

## Notas por lenguaje

C++, Go, Java y Rust usan coeficientes y discriminantes con signo de 64 bits;
Python usa enteros arbitrarios. Las cinco versiones calculan raíces binary64
con la fórmula estable y conservan el valor al imprimir. No necesitan malla
temporal, simulación por pasos ni búsqueda iterativa.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2022_geometry.cpp](2022_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 452 KB |
| [2022_geometry.go](2022_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1108 KB |
| [2022_geometry.java](2022_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 648 KB |
| [2022_geometry.py](2022_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 816 KB |
| [2022_geometry.rs](2022_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 256 KB |
