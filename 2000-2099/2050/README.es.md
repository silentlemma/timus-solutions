# 2050. Hacer coincidir rectas espaciales con media vuelta acotada

[Timus 2050](https://acm.timus.ru/problem.aspx?space=1&num=2050) · difficulty 2871 · geometry

Problema original de Egor Shchelkonogov (idea by Dmitry Ivankov), del Campeonato de Programación Deportiva de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los puntos A, B definen una recta objetivo y C, D una recta origen en el
espacio. Hallar un giro alrededor de algún eje que lleve toda la recta
origen sobre la objetivo. Los límites son 1 segundo y 64 MB.

## Entrada

Cuatro líneas con las coordenadas enteras de A, B, C y D, cada una entre
−1000 y 1000; A ≠ B y C ≠ D.

## Salida

Dos puntos P y Q del eje, con coordenadas en [−2000, 2000] y separados
al menos 1, y después el ángulo en grados en [0, 360], antihorario visto
desde P hacia Q. Siempre existe un giro, aunque se admite `Impossible`
cuando no lo hay.

## Evaluación

Un comprobador gira la recta origen y acepta la respuesta si A y B están
a menos de 10⁻⁵ de su imagen; se acepta cualquier giro válido.

## Ejemplos

```
0 0 0
0 1 0
0 0 0
1 0 0
```

```
0 0 1
0 0 0
90
```

```
1 0 1
1 0 0
0 1 1
0 1 0
```

```
0 0 1
0 0 0
270
```

En el primer ejemplo la recta original es el eje x y el destino es el
eje y; el eje mostrado y un cuarto de vuelta producen esa recta. En el
segundo, ambas rectas son paralelas a z y pasan por `(0,1,0)` y
`(1,0,0)`; el giro indicado de 270 grados mueve correctamente la recta
desplazada completa. Nuestra salida puede usar otro eje y 180 grados.

## Solución

### Construcción

Normalizamos `B-A` y `D-C` para obtener direcciones unitarias `u,v`. Si
su producto escalar es negativo, sustituimos `v` por `-v`: una recta no
está orientada. Así `u·v≥0`. Sean `m=(A+C)/2,s=C-A`.

Para `w=u+v,z=u-v` definimos `H=m+z(s·w)/(2|w|²)`. El primer eje pasa
por `H` con dirección `w`, y el ángulo es 180 grados. Un segundo
candidato intercambia `w,z` y solo hace falta con direcciones no
paralelas.

La parte lineal de media vuelta es `R(x)=2e(e·x)-x`, con `e=w/|w|`;
transforma `v` en `u`. Sea `δ=s·(u+v)/(1+u·v)`. Los puntos `C-δv/2` y
`A+δu/2` tienen punto medio `H` y diferencia perpendicular a `w`. Media
vuelta los intercambia y transforma correctamente las direcciones, por
lo que hace coincidir las rectas completas. El segundo candidato usa el
mismo argumento sustituyendo `v` por `-v`. En el caso paralelo, el
primero tiene `z=0,H=m` y funciona directamente.

### Por qué el eje cabe en los límites de coordenadas

Hay que probar las cotas de la salida, no solo encontrar un eje sin
acotar. Para direcciones no paralelas tomamos `e=(u+v)/|u+v|`, `f=(u-v)/|u-v|` y
un vector unitario `g` perpendicular a ambos. Forman una base
ortonormal. Sean `t=|u-v|/|u+v|∈(0,1]` y `d=(C-A)/2`; los subíndices
indican componentes en esa base.

Los puntos más cercanos al origen de los dos ejes son `P_+=(0,m_f+t
d_e,m_g)` y `P_-=(m_e+d_f/t,0,m_g)`. Por Cauchy–Schwarz, `(m_f+t
d_e)²≤(1+t²)(m_f²+d_e²)` y `(t m_e+d_f)²≤(1+t²)(m_e²+d_f²)`. Sumando e
incluyendo la tercera componente:
`|P_+|²+t²|P_-|²≤(1+t²)(|m|²+|d|²-d_g²)≤(1+t²)(|A|²+|C|²)/2≤(1+t²)·3·1000²`.
El promedio ponderado prueba que uno de los candidatos tiene norma como
máximo `1000√3<1733`. En el caso paralelo el primer punto es la
proyección ortogonal de `m` y cumple la misma cota.

Calculamos primero `P=H-e(e·H)`. Si `|P|≤1900` elegimos ese eje; de lo
contrario, el segundo tiene norma como máximo `1000√3` por la prueba.
Imprimimos `Q=P+2e`. La separación es dos y ambas normas son menores que
1902; cada coordenada queda estrictamente dentro de 2000. Esto también
prueba que ninguna entrada legal es imposible.

Usamos doble precisión y quince decimales. El denominador se calcula
como `2|w|²`, evitando restar números próximos en `1-u·v`. La primera
dirección tiene norma al menos `√2`. Si su punto más cercano supera
1900, la estimación `|P_+|≤1000√3(1+t)` implica
`t>1900/(1000√3)-1>0,09`; la segunda dirección seleccionada también está
bien condicionada. No se calcula una intersección inestable entre rectas
casi paralelas.

Siempre hay doce coordenadas y una cantidad fija de operaciones
vectoriales: tiempo y espacio auxiliar `O(1)`. Las cinco versiones
aplican las mismas fórmulas; Java usa locale US para el punto decimal y
Python usa float de doble precisión.

Hay que girar `CD` hacia `AB` y comprobar ambos puntos destino. Las
rectas son infinitas y no orientadas; las longitudes entre extremos
pueden diferir. Un punto medio arbitrario generalmente no pertenece al
eje correcto: hace falta la corrección de `H`. Un eje geométricamente
válido puede exceder las coordenadas permitidas; por eso se considera el
segundo candidato. La separación dos evita redondear por debajo de uno.
El sentido de un ángulo arbitrario depende de mirar de `P` a `Q`; media
vuelta actúa igual en ambos sentidos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2050_geometry.cpp](2050_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 484 KB |
| [2050_geometry.go](2050_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1140 KB |
| [2050_geometry.java](2050_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1864 KB |
| [2050_geometry.py](2050_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 836 KB |
| [2050_geometry.rs](2050_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 260 KB |
