# 1673. Admisión al examen

[Timus 1673](https://acm.timus.ru/problem.aspx?space=1&num=1673) · dificultad 1220 · number_theory

Problema original de Igor Chevdar, del Ural SU Contest en el campus de verano de Petrozavodsk, agosto de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N profesores dan N² prácticas: el profesor t da las prácticas t, N + t,
2N + t, …. El estudiante j de los N asiste exactamente a las prácticas
cuyo número es múltiplo de j, y un estudiante es admitido al examen si
asistió al menos a una práctica de cada profesor. Fueron admitidos
exactamente K estudiantes; hay que imprimir el menor N posible, o 0 si
no hay ninguno.

## Entrada

K (1 ≤ K ≤ 2·10⁹).

## Salida

El menor N, o 0.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
```

Salida:

```
15
```

### Ejemplo 2

Entrada:

```
3
```

Salida:

```
0
```

## Solución

El profesor t da las prácticas cuyo número deja resto t módulo N. El
estudiante j asiste a j, 2j, …, Nj, que recorren todos los múltiplos de
gcd(j, N) módulo N; eso son todos los restos exactamente cuando
gcd(j, N) = 1. Así que K = φ(N), la función de Euler, y hay que hallar
el menor N con φ(N) = K.

Con N = p₁^e₁ ⋯ p_r^e_r, φ(N) = ∏ (pᵢ − 1) pᵢ^(eᵢ − 1). Cada pᵢ − 1
divide a K, así que solo vale la pena probar los primos d + 1 para los
divisores d de K. Un K ≤ 2·10⁹ tiene a lo sumo 1536 divisores; cada
d + 1 se prueba con Miller–Rabin en las bases 2, 3, 5, 7, exacto por
debajo de 3,2·10⁹.

Una búsqueda con memoria toma los primos candidatos en orden creciente:
least(rest, i) es el menor producto de potencias de primos desde el
i-ésimo cuya función de Euler vale rest. Para cada primo p desde i con
(p − 1) | rest prueba p¹, p², … mientras las potencias dividan lo que
queda, recurre sobre el resto con los primos posteriores y se queda con
el menor producto. Cada estado es un divisor de K y un índice de primo,
y la respuesta es least(K, 0). Para D divisores y P primos candidatos
son a lo sumo `O(D · P²)` pasos, muchos menos en la práctica.

Detalles a tener en cuenta:

- K = 1 da N = 1: con un profesor y una práctica, el único estudiante es
  admitido (prueba 03);
- un K impar mayor que 1 nunca es valor de φ (prueba 02), y algunos pares
  tampoco, el menor es 14 (prueba 08);
- la respuesta puede pasar de 2³¹: φ(2 500 015 625) = 2·10⁹ (prueba 06).

Las respuestas coinciden con el menor N de una criba de la función de
Euler para todo K hasta 300 y uno de cada siete K hasta 3000, y con una
implementación aceptada independiente para K grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1673_number_theory.cpp](1673_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(D P^2) | AC | 0.062 s | 1848 KB |
| [1673_number_theory.go](1673_number_theory.go) | Go 1.14 x64 | number_theory | O(D P^2) | AC | 0.078 s | 5620 KB |
| [1673_number_theory.java](1673_number_theory.java) | Java 1.8 | number_theory | O(D P^2) | AC | 0.203 s | 8080 KB |
| [1673_number_theory.py](1673_number_theory.py) | Python 3.12 x64 | number_theory | O(D P^2) | AC | 0.375 s | 5048 KB |
| [1673_number_theory.rs](1673_number_theory.rs) | Rust 1.75 x64 | number_theory | O(D P^2) | AC | 0.046 s | 3292 KB |
