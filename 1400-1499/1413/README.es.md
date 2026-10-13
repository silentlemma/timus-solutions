# 1413. Saltador marciano

[Timus 1413](https://acm.timus.ru/problem.aspx?space=1&num=1413) · dificultad 179 · simulation

Problema original de Stanislav Vasiliev, del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un vehículo se maneja con un teclado numérico: cada tecla de 1 a 9
salvo el 5 da un salto de exactamente un metro en la dirección de esa
tecla vista desde el 5 central (8 es norte, 6 este, 9 noreste, etc.),
el 5 toma una muestra del suelo y el 0 hace que el vehículo se
autodestruya. Dadas hasta 10⁶ pulsaciones, hay que imprimir dónde
termina el vehículo: en el primer 0 o, si no hay ninguno, tras la
última tecla. La respuesta es el desplazamiento al este y al norte, con
un error de como mucho 10⁻¹⁰.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

Las cifras de las teclas pulsadas.

## Salida

X e Y, el desplazamiento al este y al norte.

## Ejemplos

### Ejemplo 1

Entrada:

```
1236987412369870234567890123456789
```

Salida:

```
1.0000000000 0.0000000000
```

## Solución

Se cuenta cuántas veces se pulsó cada tecla antes del primer 0. Un
salto recto mueve un eje un metro entero y uno diagonal mueve ambos
ejes 1/√2, así que el punto final en cada eje es (suma recta) + (suma
diagonal) / √2, calculado a partir de sumas enteras con un solo
redondeo. Sumar un millón de pasos en coma flotante uno a uno también
podría valer, pero los contadores mantienen el error muy por debajo de
10⁻¹⁰. `O(n)`.

Detalles a tener en cuenta:

- las teclas después del primer 0 se ignoran (pruebas 01, 05, gen2);
- un salto diagonal mide un metro, no √2 (prueba 04);
- leer un millón de caracteres de uno en uno con llamadas de entrada
  lentas puede llevarse buena parte de los 0.5 segundos, así que la
  entrada se lee en bloques grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1413_simulation.cpp](1413_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 1640 KB |
| [1413_simulation.go](1413_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.015 s | 3196 KB |
| [1413_simulation.java](1413_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.125 s | 980 KB |
| [1413_simulation.py](1413_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.093 s | 3072 KB |
| [1413_simulation.rs](1413_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 2136 KB |
