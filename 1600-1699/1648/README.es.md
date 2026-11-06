# 1648. Yates

[Timus 1648](https://acm.timus.ru/problem.aspx?space=1&num=1648) · dificultad 387 · greedy

Problema original de Alexey Samsonov, del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un astillero construye a lo sumo d yates al mes. Al final del mes i
llegan aᵢ nuevos multimillonarios, cada uno quiere un yate en el acto;
quien no lo encuentra se va para siempre. Se pueden construir yates por
adelantado, pero guardar uno durante un mes cuesta un lingote de oro. Hay
que hallar el mayor número de yates que se pueden vender en n meses y el
menor gasto de almacenaje para vender tantos.

## Entrada

n y d (1 ≤ n ≤ 20000, 1 ≤ d ≤ 100000) y luego a₁ … aₙ
(0 ≤ aᵢ ≤ 100000).

## Salida

El mayor número de yates vendidos y el menor oro gastado en almacenaje.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5
6 1 7
```

Salida:

```
13 2
```

## Solución

Ventas: al final del mes i el astillero ha construido a lo sumo i · d
yates, y los compradores del mes i solo compran entonces. Atender a cada
comprador que el inventario permita es óptimo, así que el total
acumulado de ventas es Sᵢ = min(Sᵢ₋₁ + aᵢ, i · d), y Sₙ es la
respuesta. Vender lo antes posible además deja el menor inventario al
final de cada mes.

Almacenaje: con las ventas de cada mes fijadas, cada yate se construye lo
más tarde posible. Yendo del último mes hacia atrás, un mes construye lo
que vende más lo que los meses siguientes no pudieron construir, hasta d;
el resto pasa un mes antes y cuesta un lingote por cada frontera de mes
que espera. La suma de esos arrastres es el menor gasto de almacenaje.
`O(n)`.

Las ventas no superan 20000 · 100000 = 2.000.000.000 y caben en un
entero de 32 bits con signo. El almacenaje necesita 64 bits: puede llegar
a unos n² · d / 2.

Detalles a tener en cuenta:

- los compradores de un mes no se pueden atender más tarde, así que las
  ventas de un mes están limitadas por sus compradores y por lo que exista
  para entonces (prueba 03);
- los compradores agrupados al final obligan a almacenar mucho tiempo
  (pruebas 04, 05), más allá de los enteros de 32 bits (gen3).

Las respuestas coinciden con una implementación aceptada independiente
en 120 pruebas aleatorias y con una búsqueda exhaustiva en las pequeñas.

## Soluciones optimizadas

C++ y Go guardan solo el vector de ventas. La pasada hacia delante lee la demanda mensual y limita inmediatamente las ventas acumuladas por la producción acumulada. La pasada hacia atrás retrasa la producción todo lo posible y suma las existencias que cruzan cada límite mensual. Las ventas usan enteros de 32 bits y el almacenamiento total usa 64 bits. Go usa un vector fijo de ventas y entrada y salida directa de bytes.

Las implementaciones base aceptadas [1648_greedy.java](1648_greedy.java), [1648_greedy.py](1648_greedy.py), [1648_greedy.rs](1648_greedy.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1648_greedy.cpp](1648_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.031 s | 360 KB | 11288506 |
| [1648_greedy.go](1648_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.062 s | 1584 KB | 11288507 |
| [1648_greedy.java](1648_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.109 s | 688 KB | 11288509 |
| [1648_greedy.py](1648_greedy.py) \* | Python 3.12 x64 | greedy | O(n) | AC | 0.109 s | 3136 KB | 11288508 |
| [1648_greedy.rs](1648_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.015 s | 844 KB | 11288510 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1648_greedy_optimized.cpp](1648_greedy_optimized.cpp) \* | G++ 13.2 x64 | greedy | O(n) | AC | 0.031 s | 208 KB | 11310644 |
| [1648_greedy_optimized.go](1648_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 876 KB | 11311107 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
