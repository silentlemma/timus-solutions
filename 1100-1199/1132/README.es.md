# 1132. Todas las raíces cuadradas de a módulo un primo n, hasta 100000 consultas

[Timus 1132](https://acm.timus.ru/problem.aspx?space=1&num=1132) · dificultad 545 · number_theory

Problema original de Mikhail Medvedev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para hasta `K ≤ 100000` consultas `a, n` con `n ≤ 32767` primo y
`1 ≤ a ≤ 32767` no divisible por `n`, imprime en orden creciente todos los
`x` de `1` a `n − 1` con `x² ≡ a (mod n)`, o `No root` si no hay ninguno.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`K` y luego `K` líneas con `a` y `n`.

## Salida

Una línea por consulta: las raíces separadas por espacios, o `No root`.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
4 17
3 7
2 7
14 31
10007 20011
```

Salida:

```
2 15
No root
3 4
13 18
5382 14629
```

## Solución

Se reduce `a` módulo `n`. Para `n = 2` la única raíz es `1`. Para un
primo impar, el criterio de Euler decide si hay raíz: `a^((n−1)/2)` vale
`1` para un residuo cuadrático y `n − 1` en otro caso. Si existe una raíz
`r`, la otra es `n − r`, y son distintas porque `n` es impar y `a` no es
cero.

La raíz misma sale del algoritmo de Tonelli–Shanks. Se escribe
`n − 1 = q·2^s` con `q` impar y se toma cualquier no residuo `z`. Se
empieza con `r = a^((q+1)/2)`, `t = a^q` y `c = z^q`; entonces siempre se
cumple `r² = a·t`. Mientras `t ≠ 1`, se busca el menor `i` con
`t^(2^i) = 1`, se toma `b = c^(2^(s−i−1))` y se actualiza `r ← r·b`,
`t ← t·b²`, `c ← b²`, `s ← i`. Cada paso baja el orden de `t`, así que en
como mucho `s` pasos `t = 1` y `r² = a`. El menor no residuo de cada
primo se busca una vez y se guarda. Para `n ≡ 3 (mod 4)` el bucle no se
ejecuta y `r = a^((n+1)/4)`. `O(log² n)` por consulta.

Detalles a tener en cuenta:

- `a` puede ser mayor que `n`, así que primero se reduce;
- `n = 2` tiene una sola raíz, `1`, y el criterio de Euler no se aplica;
- las dos raíces se imprimen empezando por la menor;
- con hasta 100000 consultas, la entrada y la salida van con búfer.

Las respuestas se compararon en todas las pruebas con una tabla de todos
los cuadrados módulo cada primo que aparece.

El C++ didáctico ordena las consultas por primo y construye una tabla de cuadrados por grupo. Para un primo impar p, las raíces son x y p − x, así que probar de 1 a floor(p/2) encuentra la menor. Dos cuadrados consecutivos difieren en 2x − 1. Cada residuo se obtiene con una suma y a lo sumo una resta de p. Un cero en la tabla indica que el residuo no nulo carece de raíz. Con p = 2 las raíces coinciden y se imprime 1 una vez. Los índices restauran el orden de entrada. Tiempo O(K log K + Σp), sumando los primos distintos, y espacio O(K + P), con P el mayor primo de entrada.

## Soluciones optimizadas

Los nuevos C++/Go/Rust mantienen Tonelli–Shanks. Para p≡3 mod4 calculan a^((p+1)/4) y verifican, sin prueba Euler aparte. Para p≡5 mod8 prueban a^((p+3)/8), multiplican por2^((p−1)/4) si hace falta y verifican; guardan esa corrección. En otros primos, p−1=q2^s con q impar: una potencia b=a^((q−1)/2) da r=ab, t=rb y r²=at. Orden2^s de t significa sin raíz; las correcciones habituales reducen los demás órdenes. Sus potencias de dos usan cuadrados repetidos. Una entrada uint16 por módulo guarda el c=z^q inicial, nunca el c modificado. Productos<32767² caben en uint32. Entrada/salida por búferes fijos (Rust usa caracteres C), sin guardar todas las consultas/respuestas. Cada consulta O(log²P), clases especiales O(log P), más búsqueda única de no residuo por primo necesario. Probar Z_p bases cuesta O((Z_p+1)log p). Para K consultas y Z = Σ(Z_p+1) sobre esos primos, el tiempo con la inicialización es O(P + K log² P + Z log P). Espacio O(P), P=32768, más búferes fijos. Se conservan bases sencillas; Java/Python reutilizan las admitidas.

El envío aceptado en Rust 1.75 x64 tarda 0.062 s frente a 0.015 s de la base y usa 108 KB frente a 4068 KB.

Las implementaciones base aceptadas [1132_number_theory.java](1132_number_theory.java), [1132_number_theory.py](1132_number_theory.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Los originales guardan un no residuo por primo. C++, Go y Rust optimizados guardan la potencia inicial o la corrección de su rama. La rama p≡3 mod4 calcula la raíz directamente.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1132_number_theory.cpp](1132_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K log² n) | AC | 0.203 s | 2196 KB | 11279382 |
| [1132_number_theory.go](1132_number_theory.go) | Go 1.14 x64 | number_theory | O(K log² n) | AC | 0.093 s | 1668 KB | 11279383 |
| [1132_number_theory.java](1132_number_theory.java) \* | Java 1.8 | number_theory | O(K log² n) | AC | 0.281 s | 5908 KB | 11279386 |
| [1132_number_theory.py](1132_number_theory.py) \* | Python 3.12 x64 | number_theory | O(K log² n) | AC | 0.468 s | 19404 KB | 11279385 |
| [1132_number_theory.rs](1132_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K log² n) | AC | 0.015 s | 4068 KB | 11279388 |
| [1132_math.cpp](1132_math.cpp) | G++ 13.2 x64 | math | O(K log K + Σp) | AC | 0.171 s | 6056 KB | 11315928 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1132_number_theory_optimized.cpp](1132_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(P + K log² P + Z log P) | AC | 0.031 s | 140 KB | 11315759 |
| [1132_number_theory_optimized.go](1132_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(P + K log² P + Z log P) | AC | 0.015 s | 992 KB | 11315760 |
| [1132_number_theory_optimized.rs](1132_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(P + K log² P + Z log P) | AC | 0.062 s | 108 KB | 11315763 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
