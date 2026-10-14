# 1598. Ataque a DSA

[Timus 1598](https://acm.timus.ru/problem.aspx?space=1&num=1598) · dificultad 3852 · math

Problema original preparado por Vladimir Yakovlev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una clave pública DSA (q, p, g, y) tiene un primo q de N bits
(3 ≤ N ≤ 36), un primo p de L bits (L ≤ 60) con q divisor de p − 1, g de
orden q módulo p e y = gˣ mod p para un secreto 0 < x < q. Dados la clave
y un hash H, hay que imprimir cualquier firma válida (r, s): 0 < r, s < q
y, con w = s⁻¹, u₁ = H·w y u₂ = r·w módulo q,
((g^u₁·y^u₂) mod p) mod q = r.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, L, q, p, g, y y H.

## Salida

r y s.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 6 5 41 10 16 2
```

Salida:

```
3 3
```

## Solución

El hash está fijado, así que los trucos habituales que falsifican una
firma para algún mensaje no sirven: la solución halla la clave secreta.
Como g tiene orden q, x es el logaritmo discreto de y en un grupo de
como mucho 2³⁶ elementos, y el método paso de bebé, paso de gigante lo
halla en unos √q ≈ 2,6·10⁵ pasos: se guardan gʲ para j < m = ⌈√q⌉ en una
tabla hash, y luego se multiplica y por g⁻ᵐ = g^(q − m) hasta que el valor
aparece en la tabla; si es gʲ tras i pasos, x = i·m + j.

Con x conocido, la firma se construye como dice el enunciado, con
k = 1, 2, … hasta que r = (gᵏ mod p) mod q y s = k⁻¹(H + x·r) mod q sean
ambos no nulos. q es primo, así que k⁻¹ = k^(q − 2) mod q. La
comprobación se cumple: u₁ + x·u₂ = (H + x·r)·w = k, así que
g^u₁·y^u₂ = gᵏ. En total `O(√q)` de tiempo y memoria.

Las pruebas usan un verificador que comprueba la firma como el
enunciado. Aceptó la salida en claves hechas exactamente como se
describe, de todos los tamaños desde diminutos hasta N = 36, L = 60.

Detalles a tener en cuenta:

- p tiene hasta 60 bits, así que los productos necesitan 128 bits: C++ y
  Rust usan enteros de 128 bits, Go usa bits.Mul64 con bits.Rem64, y
  Java 8, que no tiene ninguno de los dos, multiplica de dos en dos bits
  para que cada suma quede por debajo de 2⁶³;
- k = 1 puede dar r = g mod q = 0 (así ocurre en el ejemplo), así que k
  tiene que seguir avanzando;
- H tiene N bits y puede ser mayor que q; se usa módulo q.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1598_math.cpp](1598_math.cpp) | G++ 13.2 x64 | math | O(√q) | AC | 0.109 s | 12456 KB |
| [1598_math.go](1598_math.go) | Go 1.14 x64 | math | O(√q) | AC | 0.093 s | 20784 KB |
| [1598_math.java](1598_math.java) | Java 1.8 | math | O(√q) | AC | 0.312 s | 9832 KB |
| [1598_math.py](1598_math.py) | Python 3.12 x64 | math | O(√q) | AC | 0.265 s | 26936 KB |
| [1598_math.rs](1598_math.rs) | Rust 1.75 x64 | math | O(√q) | AC | 0.046 s | 17656 KB |
