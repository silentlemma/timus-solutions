# 1887. Tarjeta de viajero frecuente

[Timus 1887](https://acm.timus.ru/problem.aspx?space=1&num=1887) · dificultad 1070 · probability

Problema original de Eugene Kurpilyanskiy, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número de tarjeta tiene n cifras aleatorias x₁, …, xₙ, cada una
uniforme de 0 a 9, y una cifra de control
((∏ (aᵢxᵢ² + bᵢxᵢ + cᵢ)) mod 11) mod 10. Se generan tarjetas hasta que
diez de ellas tengan cifras de control distintas dos a dos. ¿Cuál es el
número esperado de tarjetas generadas? Hay que escribir −1 si alguna
cifra de control no puede aparecer nunca.

## Entrada

n (2 ≤ n ≤ 25) y luego las líneas a₁ … aₙ, b₁ … bₙ y c₁ … cₙ (todas de 0
a 9).

## Salida

El número esperado de tarjetas con error de como mucho 10⁻⁶, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
13
0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1
```

Salida:

```
29.2896825397
```

### Ejemplo 2

Entrada:

```
13
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
```

Salida:

```
-1
```

## Solución

Primero se halla la distribución de la cifra de control. El producto se
toma módulo 11, así que una programación dinámica sobre los 11 restos
lo sigue factor a factor: cada cifra xᵢ multiplica el resto por
aᵢxᵢ² + bᵢxᵢ + cᵢ con probabilidad 1/10. El resto r da la cifra de
control r mod 10, así que los restos 0 y 10 dan ambos 0. Si alguna
cifra tiene probabilidad 0, se escribe −1; la dinámica solo suma
términos positivos, así que ese cero es exacto.

Después se reúnen las diez cifras, y cada tarjeta muestra la cifra d
con probabilidad p_d. Sea E(S) el número esperado de tarjetas que faltan
cuando ya se han visto las cifras de S. Una tarjeta o muestra una cifra
nueva d, con probabilidad p_d, o se repite, así que
E(S) = (1 + Σ_{d∉S} p_d·E(S ∪ {d})) / Σ_{d∉S} p_d sobre los 2¹⁰
conjuntos, del completo hacia abajo. El denominador se suma sobre las
cifras que faltan en vez de tomarse como 1 menos las vistas, para que
una probabilidad pequeña conserve su precisión. La respuesta es E(∅).
`O(n·10·11 + 2¹⁰·10)`.

En el primer ejemplo cada factor es xᵢ + 1, de 1 a 10, así que el
producto es un resto no nulo uniforme y cada cifra de control tiene
probabilidad 1/10. La respuesta es la clásica
10·(1 + 1/2 + … + 1/10) ≈ 29.2897.

Trampas:

- la cifra de control es (producto mod 11) mod 10, así que un producto
  de 10 da la cifra 0, igual que el propio 0;
- un solo factor siempre nulo hace que todas las cifras de control sean
  0;
- los productos de cuadrados solo dan restos cuadráticos módulo 11, así
  que algunas entradas hacen imposibles ciertas cifras y piden −1.

Los valores esperados coinciden con la inclusión-exclusión exacta sobre
todos los conjuntos de cifras y con una implementación aceptada
independiente en 48 entradas aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1887_probability.cpp](1887_probability.cpp) | G++ 13.2 x64 | probability | O(n + 2^10 * 10) | AC | 0.015 s | 220 KB |
| [1887_probability.go](1887_probability.go) | Go 1.14 x64 | probability | O(n + 2^10 * 10) | AC | 0.031 s | 1228 KB |
| [1887_probability.java](1887_probability.java) | Java 1.8 | probability | O(n + 2^10 * 10) | AC | 0.156 s | 1880 KB |
| [1887_probability.py](1887_probability.py) | Python 3.12 x64 | probability | O(n + 2^10 * 10) | AC | 0.078 s | 636 KB |
| [1887_probability.rs](1887_probability.rs) | Rust 1.75 x64 | probability | O(n + 2^10 * 10) | AC | 0.046 s | 272 KB |
