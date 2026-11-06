# 1489. Puntos en un paralelepípedo

[Timus 1489](https://acm.timus.ru/problem.aspx?space=1&num=1489) · dificultad 384 · geometry

Problema original de Vladislav Isenbaev y Alexander Toropov, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una caja A × B × C (1 ≤ A, B, C ≤ 1000) se recorta como un desarrollo en
cruz: una columna de anchura A, con x entre C y C + A, que tiene de
abajo arriba caras de alturas B, C, B y C, y dos solapas C × B a los
lados de la tercera cara. En el desarrollo se marcan dos puntos
distintos con dos decimales. Hay que hallar la distancia entre ellos
una vez montada la caja, con error de 10⁻⁶.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

A, B y C, y luego los dos puntos como x y.

## Salida

La distancia.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2 2
3.00 3.00
5.00 5.00
```

Salida:

```
1.4142135623730950
```

## Solución

Se pone en el suelo la tercera cara de la columna: su esquina (C, B + C)
va al origen, y un punto (x, y) de ella a (x − C, y − B − C, 0). Las
cuatro caras laterales se levantan desde ella por aristas comunes, así que la
distancia de un punto a esa arista pasa a ser su altura:

- la solapa izquierda da (0, y − B − C, C − x), la derecha
  (A, y − B − C, x − C − A);
- la cara bajo el suelo da (x − C, 0, B + C − y), la de encima
  (x − C, B, y − 2B − C);
- la cara inferior de la columna se pliega a través de la cara bajo el
  suelo y se convierte en la tapa:
  (x − C, B − y, C).

Los puntos de una arista común reciben la misma posición desde
cualquiera de las dos caras. La respuesta es la distancia en línea
recta entre las dos posiciones. Leer las coordenadas en centésimas
hace exactas las caras. `O(1)`.

Detalles a tener en cuenta:

- la distancia es en línea recta a través de la caja, no por su
  superficie (pruebas 01, 03);
- dos puntos distintos del desarrollo pueden pegarse en un mismo punto
  de la caja, y entonces la respuesta es 0 (pruebas 02, 05);
- los extremos de la columna y de las solapas se convierten en aristas
  de la tapa o de las caras laterales (pruebas 04, 05).

## Soluciones optimizadas

La versión Go lee las coordenadas directamente como centésimas enteras y aplica las mismas fórmulas de las caras. La elección de la cara y la distancia al cuadrado son exactas. Solo la raíz cuadrada usa coma flotante. Se redondea el resultado a ocho decimales en un búfer fijo. syscall.Read y syscall.Write usan los descriptores estándar, repiten llamadas interrumpidas y completan escrituras parciales.

Las implementaciones base aceptadas [1489_geometry.cpp](1489_geometry.cpp), [1489_geometry.java](1489_geometry.java), [1489_geometry.py](1489_geometry.py), [1489_geometry.rs](1489_geometry.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1489_geometry.cpp](1489_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 208 KB | 11287173 |
| [1489_geometry.go](1489_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1120 KB | 11287175 |
| [1489_geometry.java](1489_geometry.java) \* | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1892 KB | 11287179 |
| [1489_geometry.py](1489_geometry.py) \* | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 572 KB | 11287178 |
| [1489_geometry.rs](1489_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 256 KB | 11287180 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1489_geometry_optimized.go](1489_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 284 KB | 11311209 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
