# 1919. Un parche rectangular de una pared cilíndrica

[Timus 1919](https://acm.timus.ru/problem.aspx?space=1&num=1919) · difficulty 2080 · geometry

Problema original de Dmitry Ivankov, de la subregión oriental del NEERC 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un hueco rectangular tiene lados w,h. Para cada cilindro, decidir si se
puede recortar una sola pieza conexa de su pared lateral, aplanarla sin
estirar y girarla para cubrir el hueco completo. El recorte puede seguir
una espiral alrededor del cilindro; las bases no aportan material.
El cilindro se describe por su altura H y su circunferencia L, no diámetro.
Límites: 1 segundo y 64 MB.

## Entrada

Primero w,h y después n. Cada una de las siguientes n líneas contiene
H,L para un cilindro, en ese orden. Todas las longitudes son enteras
de 1 a 1 000 000; 1≤n≤1000.

## Salida

Para cada cilindro y en orden, escribir `Block the hole` si sirve,
o `Too small` en caso contrario. La igualdad está permitida: el parche
puede tocar los extremos o la costura cortada.

## Evaluación

Se comparan tokens separados por espacios, respetando mayúsculas.
Cada frase se escribe en una línea propia.

## Ejemplos

```
314 314
4
314 314
314 313
600 500
234 3456
```

```
Block the hole
Too small
Block the hole
Too small
```

## Solución

Desenrollamos el cilindro en un plano de período horizontal L dentro
de una franja vertical de altura H. El rectángulo debe caber en altura
y cada sección horizontal debe medir como máximo L: de lo contrario,
dos puntos interiores a distancia L corresponderían al mismo material.
A la inversa, si ninguna sección supera L, la proyección periódica no
identifica puntos interiores y permite recortar el rectángulo conexo.
Una pieza mayor que cubra el hueco puede recortarse hasta ese rectángulo.

La proyección horizontal completa puede superar L: alturas diferentes
usan vueltas distintas. Un hueco 1×1000 puede cubrirse con H=11,L=100,
aunque una lámina plana de 100×11 no serviría.

Sea θ∈[0,π/2] el ángulo del lado w con la horizontal, c=cos θ,s=sin θ.
La altura es Y=w s+h c. Por simetría y convexidad, la sección horizontal
máxima pasa por el centro y mide min(w/c,h/s); un denominador cero
representa una cota infinita. Por tanto, la condición de circunferencia es

```text
w ≤ L cos θ  O  h ≤ L sin θ.
```

Cada rama permite un intervalo cerrado que toca 0 o π/2.
Como Y''=−Y<0, Y es cóncava y su mínimo en cada intervalo está en un
extremo. Basta revisar posiciones alineadas y las posiciones donde
una restricción de sección se cumple con igualdad.

Probamos (A,B)=(w,h) y (h,w). La rama A≤L cos θ solo existe si A≤L.
El extremo alineado sirve si B≤H. En el otro extremo cos θ=A/L,
y la altura requerida es

```text
A (B + sqrt(L²−A²)) / L.
```

Con T=HL−AB, después de los controles anteriores, ese extremo sirve
exactamente si T≥0 y T²≥A²(L²−A²). Es obligatorio comprobar el signo
antes de elevar al cuadrado. Todas las comparaciones enteras incluyen
la igualdad. Si sirve cualquiera de los dos órdenes, la respuesta es
afirmativa. El argumento de los extremos demuestra que al rechazar
ambas ramas no queda ninguna rotación factible.

O(n) operaciones enteras acotadas y O(1) espacio geométrico auxiliar.
Las versiones que almacenan toda la entrada o salida usan O(n) memoria total.

Se pueden intercambiar los lados del hueco, pero no H y L.
L ya es la circunferencia. El área no basta: 3×11 falla para H=7,L=5.
Exigir que quepa todo el rectángulo envolvente pierde los recortes
espirales. Conservar el signo de T y aceptar igualdad, incluso A=L
cuando el radical es cero.

## Notas por lenguaje

HL,AB,A²,L² caben en 64 bits, pero los productos finales alcanzan 10²⁴.
C++ convierte a `__int128` antes de multiplicar; Rust usa `u128` y
comprueba antes de restar. Go 1.14 obtiene ambas palabras con
`math/bits.Mul64`, comparando primero la alta y después la baja.
Java 8 usa `BigInteger` para los productos finales y Python enteros
de precisión arbitraria. Ningún programa calcula ángulos, raíces
ni tolerancias en punto flotante.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1919_geometry.cpp](1919_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 432 KB |
| [1919_geometry.go](1919_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1112 KB |
| [1919_geometry.java](1919_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.109 s | 960 KB |
| [1919_geometry.py](1919_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.078 s | 616 KB |
| [1919_geometry.rs](1919_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 260 KB |
