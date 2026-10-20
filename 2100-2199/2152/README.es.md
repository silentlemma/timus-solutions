# 2152. Subir los aranceles cambiando una cifra en k paquetes

[Timus 2152](https://acm.timus.ru/problem.aspx?space=1&num=2152) · dificultad 1167 · greedy, sorting

Problema original de Ivan Sychev, del Concurso Escolar de Programación de los Urales 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un paquete paga a créditos por cada kilogramo de peso por encima de mxw
y el b por ciento de cada crédito de precio por encima de mxp. Se puede
cambiar exactamente una cifra del peso o del precio en a lo sumo k de
los n paquetes. Maximizar el arancel total e imprimirlo con los datos
nuevos de cada paquete. Se acepta cualquier conjunto óptimo de cambios.
Los límites son 1 segundo y 256 MB.

## Entrada

n y k, 1 ≤ n ≤ 2 · 10⁵, 0 ≤ k ≤ n, luego mxw, mxp, a, b con
1 ≤ mxw, mxp, a ≤ 10⁹ y 1 ≤ b ≤ 100, y luego los pesos y precios, de 1 a
10⁹.

## Salida

El mayor arancel total, y luego el peso y el precio de cada paquete.

## Evaluación

Un comprobador verifica el total con error relativo 10⁻⁹, que los
cambios sean válidos y que los datos impresos den ese total.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 2
30 500 4 30
6 1100
60 90
9 990
91 420
```

Salida:

```
3217.000000000
6 9100
60 90
9 990
91 920
```

## Solución

El arancel solo crece con el peso y el precio, así que el mejor cambio
de un paquete hace uno de los dos números lo mayor posible: convertir en
9 su primera cifra que no sea 9. Se compara la ganancia de hacerlo en el
peso con la del precio y se queda la mejor; un número de solo nueves no
puede crecer.

Los paquetes no se afectan entre sí, así que se toman las k mayores
ganancias positivas tras ordenar. Todas las cantidades se guardan como
enteros en centésimas de crédito, porque el b por ciento de un número
entero de créditos tiene a lo sumo dos decimales, así que el total es
exacto. El trabajo es O(n log n).

En el ejemplo el precio 1100 pasa a 9100 y 420 a 920, las dos mayores
ganancias.

## Notas por lenguaje

- Python se ejecuta con PyPy: con CPython 3.12 supera el límite de tiempo
  en el test 9 (1.015 s), mientras que con PyPy 3.10 se acepta en 0.281 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2152_greedy_sorting.cpp](2152_greedy_sorting.cpp) | G++ 13.2 x64 | greedy, sorting | O(n log n) | AC | 0.140 s | 16016 KB |
| [2152_greedy_sorting.go](2152_greedy_sorting.go) | Go 1.14 x64 | greedy, sorting | O(n log n) | AC | 0.140 s | 23532 KB |
| [2152_greedy_sorting.java](2152_greedy_sorting.java) | Java 1.8 | greedy, sorting | O(n log n) | AC | 0.281 s | 24904 KB |
| [2152_greedy_sorting.py](2152_greedy_sorting.py) | PyPy 3.10 x64 | greedy, sorting | O(n log n) | AC | 0.281 s | 18812 KB |
| [2152_greedy_sorting.rs](2152_greedy_sorting.rs) | Rust 1.75 x64 | greedy, sorting | O(n log n) | AC | 0.062 s | 19692 KB |
