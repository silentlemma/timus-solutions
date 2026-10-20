# 2186. La menor rotación que apunta suficientes rayos a un círculo

[Timus 2186](https://acm.timus.ru/problem.aspx?space=1&num=2186) · dificultad 2681 · geometry, sorting

Problema original de Artyom Kutuzov, del Concurso Escolar de Programación de los Urales 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n rayos salen del origen en direcciones distintas (xᵢ, yᵢ), y un círculo
de radio r con centro (a, b) está apartado del origen. Los rayos giran
juntos en sentido antihorario un ángulo α, y luego se hacen k disparos,
cada uno desde un rayo elegido de forma uniforme e independiente; un
disparo acierta si su rayo toca el círculo, borde incluido. Para cada
una de q probabilidades pᵢ, hallar el menor α en [0, 360) que acierta
con probabilidad al menos pᵢ, o −1. Se aceptan respuestas con error
10⁻³. Los límites son 2 segundos y 256 MB.

## Entrada

n, k y q, 1 ≤ n ≤ 10⁵, 1 ≤ k ≤ 10, 1 ≤ q ≤ 10⁵, luego las n direcciones
con coordenadas hasta 10⁹, luego a, b y r, y luego los pᵢ con a lo sumo
cinco decimales.

## Salida

El ángulo en grados para cada consulta, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 2 5
5 -5
3 0
-3 -2
-3 -1
-3 0
-4 -1
4 2 2
0.3 0.5 0.75 0.8 0.9
```

Salida:

```
0.0000000000
45.0000000000
165.9637565321
180.0000000000
-1
```

## Solución

Si c rayos tocan el círculo, la probabilidad de acierto es
1 − ((n − c) / n)ᵏ, que crece con c, así que cada consulta pide la menor
rotación con al menos cierto número c de rayos que aciertan.

Desde el origen el círculo se ve como un arco de direcciones de la
tangente inferior a la superior, de ancho 2 · asin(r / √(a² + b²)). Al
crecer α, los rayos entran en ese arco por la tangente inferior. Así que
la cuenta solo sube en α = 0 o cuando algún rayo llega a la tangente
inferior, y entonces aciertan los rayos cuyas direcciones están dentro
del ancho del arco a partir de él. Con los rayos ordenados por ángulo,
una ventana de dos punteros sobre la lista duplicada da esa cuenta para
cada rayo, y el menor α por cuenta, hecho monótono con un mínimo de
sufijo, responde todas las cuentas.

Las direcciones justo sobre una tangente deciden si un rayo acierta, así
que cuando el punto flotante queda cerca de un empate la prueba se rehace
con enteros: el borde de la ventana compara el ángulo entre dos rayos
con el ancho del arco mediante productos escalar y vectorial, y un rayo
en la tangente inferior con α = 0 cuenta de inmediato salvo que esté
estrictamente dentro, en cuyo caso necesita una vuelta completa.

Las probabilidades tienen cinco decimales, así que cada cuenta c recibe
un nivel ⌊10⁵ · (1 − ((n − c) / n)ᵏ)⌋, calculado en punto flotante y
confirmado con enteros cerca de un punto de la malla, y una consulta p
se convierte en una búsqueda binaria del primer nivel de al menos 10⁵ p.

En el ejemplo k = 2 y n = 6. El rayo (3, 0) toca el círculo con α = 0,
lo que ya da 1 − (5/6)² ≥ 0.3, mientras que 0.9 necesitaría cinco de
los seis rayos, que el arco nunca contiene a la vez.

La ordenación y la ventana cuestan O(n log n), y las consultas
O(q log n).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2186_geometry_sorting.cpp](2186_geometry_sorting.cpp) | G++ 13.2 x64 | geometry, sorting | O((n + q) log n) | AC | 0.328 s | 3380 KB |
| [2186_geometry_sorting.go](2186_geometry_sorting.go) | Go 1.14 x64 | geometry, sorting | O((n + q) log n) | AC | 0.453 s | 16064 KB |
| [2186_geometry_sorting.java](2186_geometry_sorting.java) | Java 1.8 | geometry, sorting | O((n + q) log n) | AC | 0.515 s | 19788 KB |
| [2186_geometry_sorting.py](2186_geometry_sorting.py) | Python 3.12 x64 | geometry, sorting | O((n + q) log n) | AC | 1.015 s | 54488 KB |
| [2186_geometry_sorting.rs](2186_geometry_sorting.rs) | Rust 1.75 x64 | geometry, sorting | O((n + q) log n) | AC | 0.109 s | 16212 KB |
