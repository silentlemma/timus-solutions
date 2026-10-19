# 2035. Dividir un total bajo dos cotas superiores

[Timus 2035](https://acm.timus.ru/problem.aspx?space=1&num=2035) · dificultad 78 · math

Problema original de Kirill Borozdin, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados enteros `X,Y,C`, con `0 ≤ X,Y,C ≤ 1000000000`, encuentra cualquier
pareja entera `A,B` tal que `0 ≤ A ≤ X`, `0 ≤ B ≤ Y` y `A+B=C`.
Límites: 0,5 segundos y 64 MB.

## Entrada

Una línea `X Y C`, una sola instancia sin cantidad inicial de pruebas.

## Salida

Cualquier pareja válida `A B` o la palabra exacta `Impossible` si no existe.
La pareja `0 0` es válida cuando `C=0`.

## Evaluación

Un comprobador verifica ambos límites y la suma; `Impossible` solo se
acepta si no existe ninguna pareja. Se acepta cualquier pareja válida.

## Ejemplos

```
2 7 5
```

```
2 3
```

```
9 15 100
```

```
Impossible
```

## Solución

Elige `A=min(X,C)` y `B=C-A`. Si `B≤Y`, imprime la pareja; de lo
contrario, `Impossible`. El primer sumando es no negativo y no supera
`X` ni `C`; por ello `B≥0` y la suma es `C` por construcción. Comprobar
`B≤Y` completa las cotas.

Para demostrar completitud, cualquier primer sumando válido no supera ni `X`
ni `C`, luego no supera nuestra elección. Su segundo sumando será al menos
nuestro `B`. Minimizamos el segundo sumando necesario: si incluso este mínimo
excede `Y`, toda pareja falla. Así también se justifica la imposibilidad.

Equivalentemente, todas las soluciones corresponden a
`max(0,C-Y) ≤ A ≤ min(X,C)` y `B=C-A`. Bajo las cotas no negativas, el
intervalo no está vacío exactamente cuando `C≤X+Y`.

En el primer ejemplo `A=2` da `B=3` dentro de su cota; `0 5` y `1 4` también
sirven. En el segundo, la suma máxima `9+15=24` no alcanza `100`.
Tiempo y espacio de trabajo `O(1)`: comparación, resta y comprobación.

Trampas:

- Las cotas son no negativas e inclusivas.
- Tomar `A=X` sin limitarlo por `C` puede dejar `B` negativo.
- Los sumandos cero y la pareja cero son legítimos.
- Se acepta cualquier pareja válida, no solo el ejemplo.
- Respeta exactamente la escritura de `Impossible`.

## Notas por lenguaje

C++ y Java usan 64 bits con signo, Go `int64`, Rust `u64` y Python
enteros exactos. La resta de Rust es segura porque `A≤C`. Incluso
`X+Y≤2000000000` cabe en 32 bits con signo; los tipos anchos simplemente
mantienen sencilla la aritmética. Todos distinguen la pareja cero válida
de la ausencia de solución.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2035_math.cpp](2035_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 400 KB |
| [2035_math.go](2035_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1088 KB |
| [2035_math.java](2035_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 488 KB |
| [2035_math.py](2035_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 436 KB |
| [2035_math.rs](2035_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB |
