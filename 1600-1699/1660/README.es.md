# 1660. La isla de la mala suerte

[Timus 1660](https://acm.timus.ru/problem.aspx?space=1&num=1660) · dificultad 6373 · geometry

Problema original de Alexander Kokovin (preparado por Alexander Ipatov), del Ural SU Contest en el campus de invierno de Petrozavodsk, enero de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay dibujada una circunferencia de radio R y, dentro, otra de radio r
cuyo centro está a distancia d. Quien juega primero dibuja una
circunferencia tangente a la grande por dentro y a la pequeña por fuera.
Después, por turnos, cada nueva circunferencia debe ser tangente a las
dos dadas y a la dibujada justo antes, sin cortar ninguna otra (sí puede
tocar la primera). Cuando un paso admite dos opciones, decide quien jugó
primero. Cuando ya no cabe ninguna, se mide la distancia entre la primera
y la última. Hay que hallar la menor distancia que se puede conseguir.

## Entrada

Enteros R, r y d, con 0 < r < R − d, d ≥ 0, todos a lo sumo 100.

## Salida

La distancia, con al menos 5 cifras tras el punto decimal.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 1 0
```

Salida:

```
0.00000
```

## Solución

Las circunferencias forman una cadena de Steiner. Invertir el plano
respecto de un punto límite de las dos circunferencias dadas (uno de los
dos puntos que son inversos entre sí respecto de ambas a la vez) las
vuelve concéntricas. El punto límite dentro de la circunferencia pequeña
es

p = 2·d·R² / (b + √(b² − 4·d²·R²)), con b = R² + d² − r²,

medido desde el centro grande hacia el pequeño; con d = 0 es el centro
común, así que no hace falta un caso especial. La inversión conserva
tangencias y cortes, y en el dibujo concéntrico todas las circunferencias
de la cadena tienen el mismo radio w y la misma distancia m al centro,
así que cada nueva es la anterior girada el mismo ángulo
α = 2·asin(w / m). Por eso la cadena tiene siempre n = ⌊2π / α⌋
circunferencias, y la última queda a (n − 1)·α de la primera, empiece
donde empiece.

Solo queda elegir dónde empieza la primera (el otro sentido es solo su
imagen especular). Al deshacer la inversión de la primera y la última se
obtiene su distancia |c₁ − c₂| − r₁ − r₂ en función del ángulo inicial.
El mejor inicio siempre es simétrico: la primera y la última son imágenes
especulares respecto de la recta que une los dos centros, con el hueco a
uno de sus dos lados. Se comprobó en las 166 650 entradas válidas frente
a un barrido de 20 000 ángulos iniciales refinado con búsqueda ternaria;
coinciden con un margen de 10⁻¹⁰. En la práctica gana el hueco del lado
estrecho del anillo; la solución simplemente toma el menor de los dos.
`O(1)`.

Detalles a tener en cuenta:

- cuando la cadena cierra exactamente la respuesta es 0, así que el
  conteo necesita un pequeño margen contra el redondeo (pruebas 01 y 05);
- si solo caben dos circunferencias, la última toca la primera
  (prueba 06);
- escrito así, el punto límite no necesita restar números casi iguales,
  lo que mantiene la precisión en anillos finos (pruebas 02–04).

Las respuestas coinciden con una implementación aceptada independiente en
las 166 650 entradas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1660_geometry.cpp](1660_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 156 KB |
| [1660_geometry.go](1660_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1128 KB |
| [1660_geometry.java](1660_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1812 KB |
| [1660_geometry.py](1660_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 584 KB |
| [1660_geometry.rs](1660_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 264 KB |
