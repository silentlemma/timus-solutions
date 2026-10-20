# 2129. Pagar una cantidad con exactamente l monedas de potencias de k

[Timus 2129](https://acm.timus.ru/problem.aspx?space=1&num=2129) · dificultad 955 · dp

Problema original de Daniil Ayzenshteyn, preparado por Oleg Merkurev, del concurso «Más vale tarde que nunca».

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las monedas valen 1, k, k², k³, … Contar, módulo 10⁹ + 7, los
multiconjuntos de exactamente l monedas que suman n. Hay hasta 100
pruebas. Los límites son 3 segundos y 128 MB.

## Entrada

t, 1 ≤ t ≤ 100, y luego t líneas n, k, l con 1 ≤ n ≤ 10¹⁸,
2 ≤ k ≤ 10¹⁸ y 1 ≤ l ≤ 100.

## Salida

La cuenta de cada prueba.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
12 3 4
7 2 5
7 2 2
```

Salida:

```
2
1
0
```

## Solución

El menor número de monedas sale de las cifras dᵢ de n en base k,
s = Σ dᵢ monedas. Toda otra forma surge de esta partiendo monedas: una
moneda de kⁱ se convierte en k monedas de kⁱ⁻¹, lo que añade k − 1
monedas. Sea xᵢ el número de monedas de kⁱ que se parten. Las cantidades
finales son dᵢ + k · xᵢ₊₁ − xᵢ, así que vectores x distintos dan
multiconjuntos distintos, y x es válido cuando ninguna cantidad es
negativa: xᵢ ≤ dᵢ + k · xᵢ₊₁. Con l monedas las particiones suman
B = (l − s) / (k − 1), que debe ser un entero no negativo, así que
B ≤ 100.

Una DP desde la cifra más alta hacia abajo guarda (particiones usadas,
particiones del nivel de arriba) con el número de formas. En cada nivel
xᵢ recorre 0 … min(dᵢ + k · xᵢ₊₁, presupuesto restante), así que para
un número fijo de usadas el nuevo valor solo depende de lo grande que
sea xᵢ₊₁; sumas prefijas sobre el nivel anterior llenan cada fila en
O(B), O(B²) por nivel. Las monedas de 1 no se pueden partir, y la
respuesta es el número de formas que usan exactamente B particiones. Con
a lo sumo 60 cifras esto es O(B² log_k n) por prueba.

En el primer ejemplo 12 = 110 en base 3, así que s = 2 y l = 4 necesita
una partición: o el 9 se convierte en tres 3, o uno de los 3 en tres 1;
son el 3 + 3 + 3 + 3 y el 9 + 1 + 1 + 1 del enunciado.

## Notas por lenguaje

- Python se ejecuta con PyPy: con CPython 3.12 supera el límite de tiempo
  en el test 18 (3.05 s), mientras que con PyPy 3.10 se acepta en 0.63 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2129_dp.cpp](2129_dp.cpp) | G++ 13.2 x64 | dp | O(t l^2 log_k n) | AC | 0.078 s | 712 KB |
| [2129_dp.go](2129_dp.go) | Go 1.14 x64 | dp | O(t l^2 log_k n) | AC | 0.171 s | 8544 KB |
| [2129_dp.java](2129_dp.java) | Java 1.8 | dp | O(t l^2 log_k n) | AC | 0.359 s | 4940 KB |
| [2129_dp.py](2129_dp.py) | PyPy 3.10 x64 | dp | O(t l^2 log_k n) | AC | 0.625 s | 9460 KB |
| [2129_dp.rs](2129_dp.rs) | Rust 1.75 x64 | dp | O(t l^2 log_k n) | AC | 0.156 s | 712 KB |
