# 2111. Un coste de reparto que no depende del orden

[Timus 2111](https://acm.timus.ru/problem.aspx?space=1&num=2111) · dificultad 74 · math

Problema original de Anna Khanova, de la Olimpiada Académica Universitaria de Informática 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n ciudades están unidas a la capital por carreteras de longitudes dᵢ, y
la ciudad i necesita dᵢ toneladas de carga. Un camión cargado una vez en
la capital visita las ciudades en cualquier orden, siempre por las
carreteras; llevar m toneladas l kilómetros cuesta m · l. Hallar el
menor coste total. Los límites son 1 segundo y 256 MB.

## Entrada

n ≤ 10⁵ y después d₁ … dₙ, cada uno hasta 10⁴.

## Salida

El menor coste.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 2 3
```

Salida:

```
36
```

## Solución

Cada visita va de la capital a una ciudad y vuelve. Con carga L a la
ida, la visita cuesta L·d y luego (L − d)·d a la vuelta, es decir
(2L − d)·d. Aquí L es d más la demanda de las ciudades aún por visitar.
Sumando sobre las visitas, cada ciudad aporta d² dos veces menos una, y
cada par de ciudades aporta 2·dᵢ·dⱼ sea cual sea la primera. Así que todo
orden cuesta (Σ dᵢ)², que llega a 10¹⁸ y necesita enteros de 64 bits.

En el ejemplo (1 + 2 + 3)² = 36.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2111_math.cpp](2111_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.078 s | 140 KB |
| [2111_math.go](2111_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.062 s | 2776 KB |
| [2111_math.java](2111_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 512 KB |
| [2111_math.py](2111_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 7368 KB |
| [2111_math.rs](2111_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.046 s | 2140 KB |
