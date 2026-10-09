# 1046. Reconstruir un polígono a partir de los vértices de los triángulos sobre sus lados

[Timus 1046](https://acm.timus.ru/problem.aspx?space=1&num=1046) · dificultad 1887 · geometry

Problema original de Dmitry Filimonenkov, del concurso universitario de programación de la Universidad Estatal de los Urales, 25 de marzo de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un polígono `A1 A2 … AN` (`3 ≤ N ≤ 50`) tiene sus vértices en sentido
horario. Sobre cada lado `Ai Ai+1` (con `AN+1 = A1`) se construye hacia
fuera un triángulo isósceles `Ai Mi Ai+1`, con `Mi Ai = Mi Ai+1` y ángulo
`αi` en `Mi`. Ningún subconjunto no vacío de los ángulos suma un múltiplo
de 360°. Dados los vértices `Mi` y los ángulos, reconstruye los vértices
del polígono.

Todos los números de la entrada son reales con como mucho dos decimales,
`|xi|, |yi| ≤ 100`. Límite de tiempo: 0,5 segundos. Límite de memoria:
64 MB.

## Entrada

`N`, luego `N` líneas con las coordenadas de `M1 … MN` y luego `N` líneas
con los ángulos `α1 … αN` en grados.

## Salida

`N` líneas con las coordenadas de `A1 … AN`, exactas hasta dos decimales.

## Evaluación

Los números se comparan con un error absoluto de 0.011: las respuestas se
imprimen con dos decimales, así que la última cifra puede diferir en uno.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 2
3 3
2 0
90
90
90
```

Salida:

```
1.00 1.00
1.00 3.00
3.00 1.00
```

### Ejemplo 2

Entrada:

```
4
-1.73 1.00
1.00 3.00
2.58 1.00
1.00 -2.41
60
90
120
45
```

Salida:

```
0.00 -0.01
0.01 2.00
2.00 2.01
2.00 -0.01
```

## Solución

Se tratan los puntos como números complejos. `Mi Ai = Mi Ai+1` con el
ángulo `αi` en `Mi` significa que `Ai+1` es `Ai` girado alrededor de `Mi`
un ángulo `αi` (en sentido antihorario para un polígono en sentido horario
con los triángulos por fuera):

```text
A[i+1] = M[i] + w[i] · (A[i] − M[i]),     w[i] = e^(i·α[i])
```

Cada paso es una aplicación `z → w·z + (1 − w)·M`. Componer los `N` pasos
en orden da `z → a·z + b` con `a = w1 · … · wN = e^(i·Σα)`, y `A1` debe
ser su punto fijo porque el recorrido vuelve a `A1`:

```text
A1 = a·A1 + b   →   A1 = b / (1 − a)
```

Los ángulos nunca suman un múltiplo de 360°, así que `a ≠ 1` y la
respuesta es única. Los demás vértices salen aplicando los pasos uno a
uno. `O(N)`.

Detalles a tener en cuenta:

- el sentido del giro: con los vértices en sentido horario y los
  triángulos por fuera, el giro de `Ai` a `Ai+1` alrededor de `Mi` es
  antihorario;
- los ángulos están en grados;
- los `Mi` de la entrada están redondeados, así que el polígono
  reconstruido se parece al original pero no coincide exactamente;
  imprime dos decimales y evita `-0.00`.

## Notas por lenguaje

- **C++**: `std::complex`; **Go**: `complex128`; **Python**: números
  complejos integrados.
- **Java**: partes real e imaginaria en variables separadas;
  `String.format` con `Locale.US` para el punto decimal.
- **Rust**: un pequeño tipo complejo con las cuatro operaciones.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1046_geometry.cpp](1046_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.031 s | 212 KB |
| [1046_geometry.go](1046_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1160 KB |
| [1046_geometry.java](1046_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.109 s | 1116 KB |
| [1046_geometry.py](1046_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.062 s | 576 KB |
| [1046_geometry.rs](1046_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.046 s | 280 KB |
