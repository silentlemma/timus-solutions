# 1696. Salario para robots

[Timus 1696](https://acm.timus.ru/problem.aspx?space=1&num=1696) · dificultad 860 · dp

Problema original de Igor Chevdar, del Ural SU Contest en el campus de invierno de Petrozavodsk, febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n robots de rangos 1..n cobran cada mes un salario de 1 a k. Un pago
está prohibido si hay robots a, b, c cuyos rangos bajan de a a c
mientras sus salarios suben de a a c, y ningún pago puede repetirse.
Los meses se numeran 1..p dentro de cada año. ¿En qué mes se quedará el
contable sin pagos posibles?

## Entrada

n, k, p (1 ≤ n ≤ 1000; 1 ≤ k ≤ 200; 2 ≤ p ≤ 10⁹).

## Salida

El número de ese mes dentro de su año.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3 20
```

Salida:

```
7
```

## Solución

Escribiendo los salarios por orden de rango, el patrón prohibido es una
subsucesión estrictamente decreciente de longitud tres. Si hay C pagos
permitidos, el contable se oxida en el mes C + 1 contando desde el
principio, así que la respuesta es (C mod p) + 1.

Se cuentan las sucesiones rango a rango. El estado es a, el mayor
salario hasta ahora, y b, el mayor salario que viene detrás de uno
mayor (0 si no hay). Un salario nuevo z está permitido exactamente
cuando z ≥ b, pues z < b cerraría un trío decreciente. Si z < a, el
estado pasa a (a, z); si no, a (z, b). Ambos pasos son sumas prefijas:
el nuevo (a, c) reúne todos los antiguos (a, b) con b ≤ c a lo largo
de una fila, y el nuevo (z, b) todos los antiguos (a, b) con a ≤ z a lo
largo de una columna. En total `O(n · k²)` módulo p.

Trampas:

- el mes es (C mod p) + 1, así que un recuento múltiplo de p da el mes
  1 (test 10);
- los salarios iguales nunca forman un trío prohibido, solo los
  estrictamente decrecientes;
- los recuentos se guardan módulo p desde el principio, pues C es
  astronómicamente grande.

La solución en Python se envía con PyPy: una ejecución local de
CPython tarda unos 3 s con n = 1000 y k = 200, más que el límite de
2 s.

Las respuestas coinciden con un recuento sobre todas las sucesiones de
salarios para n ≤ 6 y k ≤ 5 y con una implementación aceptada
independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1696_dp.cpp](1696_dp.cpp) | G++ 13.2 x64 | dp | O(n · k²) | AC | 0.703 s | 452 KB |
| [1696_dp.go](1696_dp.go) | Go 1.14 x64 | dp | O(n · k²) | AC | 1.015 s | 7568 KB |
| [1696_dp.java](1696_dp.java) | Java 1.8 | dp | O(n · k²) | AC | 1.093 s | 2240 KB |
| [1696_dp.py](1696_dp.py) | PyPy 3.10 x64 | dp | O(n · k²) | AC | 1.203 s | 13612 KB |
| [1696_dp.rs](1696_dp.rs) | Rust 1.75 x64 | dp | O(n · k²) | AC | 0.359 s | 964 KB |
