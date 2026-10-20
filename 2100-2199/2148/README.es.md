# 2148. Rebotar un disparo en un tanque redondo entre dos jugadores equidistantes

[Timus 2148](https://acm.timus.ru/problem.aspx?space=1&num=2148) · dificultad 500 · geometry

Problema original de Kirill Meshcheryakov, del Concurso Escolar de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tanque redondo tiene centro C y radio r. Dos jugadores A y B están
fuera de él a la misma distancia de C. Hallar un punto del borde del
tanque en el que un disparo desde A rebote hacia B, con el ángulo de
incidencia igual al de reflexión y sin ninguna parte del camino dentro
del tanque; un disparo rasante por una tangente no cuenta. Imprimir
"No way" si no existe. Los límites son 0.5 segundos y 256 MB.

## Entrada

El centro y el radio, luego A y luego B, todos enteros con valor
absoluto a lo sumo 3000.

## Salida

El punto, o "No way".

## Evaluación

Un comprobador verifica la distancia al centro y los dos ángulos con
precisión 10⁻⁶ y que ambos disparos queden fuera del tanque.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 7 3
0 0
8 0
```

Salida:

```
4.000000 4.000000
```

### Ejemplo 2

Entrada:

```
0 0 2
-5 0
-3 4
```

Salida:

```
-1.788854 0.894427
```

## Solución

Como |A − C| = |B − C|, la figura es simétrica respecto a la bisectriz
del ángulo ACB, y el punto de esa bisectriz P = C + r · w / |w|, con
w = A + B − 2C, refleja A hacia B: la normal en P es la propia
bisectriz. El camino A → P queda fuera del tanque exactamente cuando A
está estrictamente más allá de la tangente en P, es decir,
(A − C) · w > r · |w|; por simetría lo mismo vale entonces para B. Con
igualdad el disparo roza la tangente, y w = 0 significa que A y B están
enfrentados, lo que hace 0 el lado izquierdo.

Si la condición falla, tampoco hay otro punto: los puntos del borde
visibles desde A forman un arco alrededor de la dirección de A, los
visibles desde B otro alrededor de la de B, y cuando el punto de la
bisectriz no está estrictamente dentro de ambos arcos, estos no se
solapan en absoluto.

La prueba usa solo enteros, elevando al cuadrado ambos lados cuando el
izquierdo es positivo; los valores quedan muy por debajo de 64 bits. Las
coordenadas de P se imprimen con nueve decimales.

En el primer ejemplo w = (0, −14) apunta hacia abajo desde C = (4, 7),
así que P = (4, 4).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2148_geometry.cpp](2148_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 144 KB |
| [2148_geometry.go](2148_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1136 KB |
| [2148_geometry.java](2148_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1800 KB |
| [2148_geometry.py](2148_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 524 KB |
| [2148_geometry.rs](2148_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 260 KB |
