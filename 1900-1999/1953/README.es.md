# 1953. Elipse de área máxima a partir de tres lados

[Timus 1953](https://acm.timus.ru/problem.aspx?space=1&num=1953) · difficulty 2527 · geometry

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (idea by Pavel Ageev).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dadas las longitudes de un triángulo no degenerado, hallar la elipse de
área máxima contenida en él. Una elipse contiene los puntos cuya suma
de distancias a dos focos no supera 2R. Pedir la distancia entre focos y
el semieje mayor R. La pareja es única; en un círculo coinciden los focos.
Límites: 1 segundo, 64 MB.

## Entrada

Una línea de enteros a,b,c: 1≤a≤b≤c≤1000 y c<a+b.

## Salida

Dos reales: distancia focal, después R. Error absoluto o relativo de cada
uno como máximo 10⁻⁶. Imprimir doce cifras decimales.

## Evaluación

Ambos números se comparan con error absoluto o relativo 10⁻⁶.

## Ejemplos

```
1 1 1
```

```
0.000000 0.288675
```

## Solución

La máxima es la inelipse de Steiner: centro en el baricentro y tangencia
en los puntos medios. Demostración por áreas: transformar afínmente una
elipse candidata en el disco unidad. Un triángulo que contiene ese disco
tiene área al menos 3√3. Desplazar sus lados paralelamente hacia dentro
hasta tangencia no aumenta el área. El triángulo tangente tiene inradio 1,
por lo que su área es su semiperímetro cot(A/2)+cot(B/2)+cot(C/2).
Cotangente es estrictamente convexa en (0,π/2); los semiángulos suman π/2,
y la suma es al menos 3cot(π/6)=3√3, con igualdad solo en el equilátero.
La razón área de elipse/área de triángulo es como máximo π/(3√3). La imagen
afín del incírculo equilátero alcanza la cota. Se conservan baricentros y
puntos medios, probando la descripción y el caso de igualdad.

Sean p₁,p₂,p₃ los vértices y g su baricentro. La matriz de forma es
Q=(1/6)Σ(pᵢ−g)(pᵢ−g)ᵀ: la elipse es g+Q^(1/2)u, |u|≤1. En el
equilátero Q es el inradio al cuadrado por la identidad. Una transformación
afín cambia ambos lados como Q→TQTᵀ, así que la fórmula es general.
Sus autovalores λ₊≥λ₋>0 son los semiejes al cuadrado. Para S=a²+b²+c²
y área triangular Δ, trace Q=S/18 y det Q=Δ²/27. Luego
λ₊=(S+√D)/36 y λ₊−λ₋=√D/18, con D=S²−48Δ².

Evitar calcular el área o restar flotantes casi iguales. La identidad de
Herón da el entero no negativo
D=2[(a²−b²)²+(b²−c²)²+(c²−a²)²]. Con q=√D, las respuestas son
sqrt(2q)/3 y sqrt(S+q)/6. Para un equilátero D=0 y la distancia focal
es exactamente cero sin tolerancia ni rama especial.

O(1) tiempo y espacio, operaciones enteras y tres raíces cuadradas.

R es semieje; la primera respuesta es la distancia completa entre focos,
2sqrt(λ₊−λ₋). El incírculo solo es óptimo en el equilátero. Evitar
desbordar antes de convertir a double y no calcular S²−48Δ² en flotante
cerca de un círculo. Un triángulo válido muy delgado sigue teniendo área
positiva y una elipse auténtica.

## Notas por lenguaje

C++, Go, Java y Rust calculan cuadrados y diferencias en enteros con signo
de 64 bits; Python tiene enteros arbitrarios. La cota conservadora
D<6·10¹²<2⁴³ evita desbordamiento y permite conversión exacta a binary64.
Después usar double/f64. No hay cancelación en S+q y D=0 se conserva.
Doce decimales dan error de impresión como máximo 5·10⁻¹³. Solo biblioteca
estándar; Java fija Locale.US.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1953_geometry.cpp](1953_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 452 KB |
| [1953_geometry.go](1953_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1104 KB |
| [1953_geometry.java](1953_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1840 KB |
| [1953_geometry.py](1953_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 540 KB |
| [1953_geometry.rs](1953_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 252 KB |
