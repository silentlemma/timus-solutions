# 1698. País Cuadrado 5

[Timus 1698](https://acm.timus.ru/problem.aspx?space=1&num=1698) · dificultad 640 · number_theory

Problema original de Alex Samsonov, del Ural SU Contest en el campus de invierno de Petrozavodsk, febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Contar los enteros positivos de a lo sumo n cifras, sin ceros a la
izquierda, cuyo cuadrado termina en el propio número, como 76² = 5776.

## Entrada

n (1 ≤ n ≤ 2000).

## Salida

La cantidad.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
3
```

## Solución

Un número x de d cifras sirve cuando x² ≡ x (mod 10ᵈ), es decir, cuando
x(x − 1) es divisible por 2ᵈ y por 5ᵈ. Como x y x − 1 son coprimos,
cada potencia de primo divide a uno de ellos, lo que da cuatro restos
módulo 10ᵈ: 0, 1 y los dos mixtos. Los restos mixtos son las últimas d
cifras de dos números 10-ádicos infinitos, …890625 y …109376. Sus
cifras, salvo la última, suman 9 posición a posición, porque los dos
números suman 1 (mod 10ᵈ).

Así, para cada longitud d los candidatos son 1 (solo con d = 1) y los
dos finales de longitud d, que cuentan cuando su cifra inicial, la
d-ésima cifra del número infinito, no es 0. Escribiendo el que termina
en 5 como x = Σ xᵢ 10ⁱ, la cifra d de x² es la suma de xᵢ·xⱼ con
i + j = d más el acarreo de abajo. Una cifra nueva c entra en esa suma
como 2·5·c, múltiplo de 10, así que c debe ser (los demás productos +
acarreo) mod 10, y el siguiente acarreo sale enseguida. El que termina
en 6 tiene ahí la cifra 9 − c, que cuenta cuando c ≠ 9. `O(n²)`
productos de cifras, sin enteros grandes.

Trampas:

- el 1 cuenta (1² = 1), pero el 0 no es positivo;
- los finales con cero inicial, como 0625 para d = 4, no cuentan
  (test 04);
- los dos números infinitos están ligados: uno es 1 menos el otro, así
  que la misma cifra decide por ambos.

Las respuestas coinciden con una implementación aceptada independiente
para todos los n probados hasta 2000.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1698_number_theory.cpp](1698_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n²) | AC | 0.015 s | 204 KB |
| [1698_number_theory.go](1698_number_theory.go) | Go 1.14 x64 | number_theory | O(n²) | AC | 0.031 s | 1168 KB |
| [1698_number_theory.java](1698_number_theory.java) | Java 1.8 | number_theory | O(n²) | AC | 0.125 s | 1600 KB |
| [1698_number_theory.py](1698_number_theory.py) | Python 3.12 x64 | number_theory | O(n²) | AC | 0.296 s | 436 KB |
| [1698_number_theory.rs](1698_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n²) | AC | 0.015 s | 236 KB |
