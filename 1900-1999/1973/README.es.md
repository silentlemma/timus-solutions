# 1973. Área esperada de un triángulo con vértice fijo

[Timus 1973](https://acm.timus.ru/problem.aspx?space=1&num=1973) · difficulty 4773 · geometry

Problema original de Denis Dublennykh, del Campeonato de Programación Deportiva de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Fijar el primer vértice A de un polígono convexo. Elegir B y C de forma
independiente y uniforme por área en su interior estricto. Hallar el área
no orientada esperada de ABC. Hay 3≤n≤1000 vértices en orden antihorario,
coordenadas enteras entre −10⁶ y 10⁶ inclusive y ningún trío colineal.
Límites: 1 segundo, 64 MB.

## Entrada

n seguido de n pares x,y en orden del contorno. El primero es A, que
debe mantenerse fijo; cambiar el vértice inicial cambia la pregunta.

## Salida

Un número real: el área esperada. Se acepta error absoluto o relativo
de hasta 10⁻⁶; basta cumplir uno de los dos.

## Evaluación

Un comprobador compara el número con un error de como mucho 10⁻⁶ ·
max(1, |respuesta|).

## Ejemplos

```
4
0 0
1 0
1 1
0 1
```

```
0.120370370
```

## Solución

Trasladar A al origen. Sean v₁,…,vₙ₋₁ los otros vértices. Los triángulos
Tᵢ=(0,vᵢ,vᵢ₊₁), i=1,…,n−2, de áreas positivas sᵢ, dividen el polígono
salvo fronteras de probabilidad cero. Definir área total S,
dᵢ=2sᵢ=cross(vᵢ,vᵢ₊₁), tᵢ=vᵢ+vᵢ₊₁ y D=Σdᵢ, donde
cross(x,y)=xₓyᵧ−xᵧyₓ. El centroide es cᵢ=tᵢ/3.

### Puntos en triángulos distintos

Para i<j, los rayos de Tᵢ preceden a los de Tⱼ. El ángulo total junto
al ancla es menor que π por convexidad, de modo que cross(B,C)≥0 cuando
B∈Tᵢ y C∈Tⱼ. La independencia condicional da producto cruzado esperado
cross(cᵢ,cⱼ); el área aporta la mitad. Los órdenes (i,j) y (j,i) tienen
probabilidad total 2sᵢsⱼ/S², así que su contribución conjunta es

sᵢsⱼ·cross(cᵢ,cⱼ)/S².

### Puntos en el mismo triángulo

En T=(0,u,v), escribir un punto uniforme como r((1−t)u+tv). t es uniforme
en [0,1], independiente de r con densidad 2r; E[r]=2/3. Dos puntos con
parámetros (r,t),(q,z) dan área area(T)·r·q·|t−z|. Como E|t−z|=1/3,
el área condicional esperada es (4/27)·area(T).

Multiplicar por (sᵢ/S)² y añadir los casos distintos:

E = [(4/27)Σsᵢ³ + Σᵢ<ⱼ sᵢsⱼ·cross(tᵢ,tⱼ)/9] / S².

Sustituyendo dᵢ=2sᵢ y D=2S:

E = [2Σdᵢ³ + 3Σᵢ<ⱼ dᵢdⱼ·cross(tᵢ,tⱼ)] / (27D²).

### Prefijo para evitar todas las parejas

Antes de j mantener el vector exacto P=Σᵢ<ⱼ dᵢtᵢ. Su contribución por
parejas es dⱼ·cross(P,tⱼ). Añadir 2dⱼ³+3dⱼ·cross(P,tⱼ) al numerador,
actualizar P con dⱼtⱼ y D con dⱼ. Un recorrido calcula la fórmula, con
términos finales no negativos. La partición condicional cubre todos los
pares aleatorios y demuestra tanto la fórmula como su implementación.

Tiempo `O(n)` en operaciones aritméticas, `O(n)` puntos almacenados y
`O(1)` acumuladores adicionales. Los límites fijan el tamaño de los enteros.

### Restar exactamente antes de redondear

Tras trasladar, las coordenadas llegan a 2·10⁶, dᵢ≤8·10¹² y las de tᵢ
a 4·10⁶. Una cota holgada da coordenadas de P menores que 3.2·10²² y
|cross(P,tᵢ)| menor que 2.56·10²⁹, dentro de 128 bits con signo. Calcular
esa diferencia exactamente: rayos casi paralelos provocan cancelación
de productos grandes. El numerador final puede superar 128 bits; C++
y Rust convierten términos positivos antes de cubicar o multiplicar
por dᵢ. La suma positiva no tiene cancelación. Las demás versiones
mantienen toda la fracción en enteros arbitrarios hasta la división final.

En el ejemplo d₁=d₂=1, t₁=(2,1), t₂=(1,2), cross(t₁,t₂)=3 y D=2.
Numerador 2(1+1)+3·3=13, denominador 27·4=108: el resultado es
13/108≈0.12037037037, compatible con el valor impreso.

La distribución es uniforme por área: ponderar los triángulos por área.
Conservar el primer vértice. El producto cruzado orientado esperado de
dos puntos idénticamente distribuidos es cero, no el área buscada: hace
falta condicionar el orden angular. No omitir el caso del mismo triángulo
ni sustituir 4/27 por otra fórmula. Usar enteros exactos anchos para la
resta prefija y convertir antes de cubos o D² si pueden desbordarse.

## Notas por lenguaje

Python, Go 1.14 math/big y Java 8 BigInteger mantienen toda la fracción
exacta. C++ usa prefijos __int128 y acumulación long double; Rust usa
i128 y f64. Todos imprimen doce decimales, con bibliotecas estándar
y los tipos enteros del compilador elegido.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1973_geometry.cpp](1973_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 492 KB |
| [1973_geometry.go](1973_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1676 KB |
| [1973_geometry.java](1973_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.140 s | 4604 KB |
| [1973_geometry.py](1973_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.093 s | 776 KB |
| [1973_geometry.rs](1973_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 312 KB |
