# 1820. Filetes de los Urales

[Timus 1820](https://acm.timus.ru/problem.aspx?space=1&num=1820) · dificultad 25 · math

Problema original de Magaz Asanov, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que freír ambos lados de n filetes, un minuto por lado, en una
sartén que admite como mucho k filetes a la vez. Hallar el menor número
de minutos.

## Entrada

n y k (1 ≤ n, k ≤ 1000).

## Salida

El menor número de minutos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2
```

Salida:

```
3
```

## Solución

Hay 2n lados y cada minuto se fríen como mucho k, así que hacen falta
al menos ⌈2n/k⌉ minutos; y los dos lados de un filete no pueden
freírse en el mismo minuto, así que al menos 2. La respuesta es
max(2, ⌈2n/k⌉), y se alcanza: se listan los lados como cara 1, …,
cara n, dorso 1, …, dorso n y cada minuto se fríen los k siguientes.
Con n ≥ k los dos lados de un filete distan n en la lista y nunca
coinciden en un minuto; con n < k ambos lados caben en dos minutos de
todos modos. `O(1)`.

En el ejemplo: caras 1 y 2, luego dorso 1 con cara 3, luego dorsos 2
y 3: tres minutos.

Trampas:

- freír tandas completas de k filetes durante dos minutos desperdicia
  la sartén: 3 filetes en una sartén para 2 tardan 3 minutos, no 4;
- con k ≥ 2n la cota ⌈2n/k⌉ vale 1, pero un filete sigue necesitando
  dos minutos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1820_math.cpp](1820_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1820_math.go](1820_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1076 KB |
| [1820_math.java](1820_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1608 KB |
| [1820_math.py](1820_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 348 KB |
| [1820_math.rs](1820_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 232 KB |
