# 1821. Biatlón

[Timus 1821](https://acm.timus.ru/problem.aspx?space=1&num=1821) · dificultad 178 · sorting

Problema original de Alexander Ipatov y Alexey Samsonov, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En una carrera con salida individual los esquiadores salen uno a uno,
con 30 segundos de intervalo. Un marcador muestra al esquiador con el
mejor tiempo entre los que ya han llegado. Dados los esquiadores en
orden de salida con sus tiempos de carrera, listar a todos los que
aparecieron en el marcador.

## Entrada

n (1 ≤ n ≤ 100), luego n líneas: un apellido (hasta 20 letras
inglesas, la primera mayúscula) y un tiempo "mm:ss.d". Nadie llega a la
vez que otro y no hay dos tiempos iguales.

## Salida

El número de esquiadores que lideraban al llegar, y luego sus
apellidos en orden lexicográfico, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
Zaitseva 21:38.2
Hauswald 21:21.0
Boulygina 22:04.4
Henkel 22:06.1
Wilhelm 21:11.1
Jonsson 22:05.8
```

Salida:

```
3
Hauswald
Wilhelm
Zaitseva
```

## Solución

Se trabaja en décimas de segundo. El esquiador i (desde 0) sale en
300·i y llega en 300·i más su tiempo. Se ordenan los esquiadores por
momento de llegada y se reproduce la carrera: uno entra en el marcador
cuando su tiempo mejora todos los ya registrados. Se ordenan los
apellidos reunidos y se imprimen. `O(n log n)`.

En el ejemplo las llegadas van en el orden Zaitseva (12982), Hauswald
(13110), Boulygina (13844), Wilhelm (13911), Henkel (14161), Jonsson
(14758) en décimas; el mejor tiempo baja con Zaitseva, Hauswald y
Wilhelm.

Trampas:

- el orden de llegada no es el de salida, así que se ordena por el
  momento de llegada, no por el tiempo de carrera;
- el marcador muestra el mejor tiempo hasta el momento, no al primero
  en llegar;
- la respuesta va ordenada por apellido, no en el orden en que cambió
  el marcador.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1821_sorting.cpp](1821_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 452 KB |
| [1821_sorting.go](1821_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.031 s | 1136 KB |
| [1821_sorting.java](1821_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.156 s | 3936 KB |
| [1821_sorting.py](1821_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.093 s | 460 KB |
| [1821_sorting.rs](1821_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 228 KB |
