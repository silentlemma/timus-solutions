# 1582. Casas de apuestas

[Timus 1582](https://acm.timus.ru/problem.aspx?space=1&num=1582) · dificultad 123 · math

Problema original de Sergey Pupyrev, preparado por Vladimir Yakovlev, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un partido tiene tres resultados con las mejores cuotas k₁, k₂ y k₃
(0.01 … 100): una apuesta de x al resultado correcto paga k·x, y una
errada no paga nada. Hay que repartir apuestas por un total de 1000
libras entre los tres resultados para recuperar lo máximo en el peor
caso, e imprimir esa cantidad redondeada al entero más cercano.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

k₁, k₂ y k₃.

## Salida

El pago garantizado, redondeado.

## Ejemplos

### Ejemplo 1

Entrada:

```
3.5 3.5 3.5
```

Salida:

```
1167
```

### Ejemplo 2

Entrada:

```
1.25 10.0 5.75
```

Salida:

```
931
```

## Solución

Se apuesta xᵢ al resultado i, con x₁ + x₂ + x₃ = 1000; el resultado i
paga kᵢ·xᵢ. Si los tres pagos difieren, pasar un poco de dinero del
resultado mejor pagado al peor pagado sube el mínimo, así que en el
mejor reparto todos los pagos son iguales a cierto P. Entonces
xᵢ = P / kᵢ, y el total da

P = 1000 / (1/k₁ + 1/k₂ + 1/k₃).

Los tres términos se suman uno tras otro en doble precisión, y el pago
se redondea con la mitad hacia arriba como ⌊P + 0.5⌋. `O(1)`.

Detalles a tener en cuenta:

- con cuotas mayores que 3, el pago garantizado supera lo apostado, como
  en el primer ejemplo;
- una mitad exacta redondea hacia arriba: las cuotas 2, 10 y 25 dan
  1562.5 y la respuesta 1563, mientras que `printf("%.0f")` redondearía
  al par e imprimiría 1562 (prueba 08);
- el `sum` de Python suma los números en coma flotante con precisión
  extra desde la versión 3.12, así que la solución en Python suma los
  tres términos uno a uno, como las demás.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1582_math.cpp](1582_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 152 KB |
| [1582_math.go](1582_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1068 KB |
| [1582_math.java](1582_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1724 KB |
| [1582_math.py](1582_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 404 KB |
| [1582_math.rs](1582_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 252 KB |
