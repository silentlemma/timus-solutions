# 2166. El cruce de rectas más lejano del origen en distancia L1

[Timus 2166](https://acm.timus.ru/problem.aspx?space=1&num=2166) · dificultad 1868 · geometry, sorting

Problema original de Vadim Barinov, del Concurso Escolar de Programación de los Urales 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan N rectas no paralelas dos a dos, cada una por dos puntos enteros,
y cada cruce de dos rectas es una estación. Llegar a una estación (x, y)
desde el origen a lo largo de los ejes cuesta |x| + |y|. Imprimir el
mayor de esos costes sobre todas las estaciones con error relativo 10⁻⁴.
Los límites son 3 segundos y 256 MB.

## Entrada

N, 2 ≤ N ≤ 10⁵, y luego las rectas como x₁ y₁ x₂ y₂ con coordenadas de
hasta 1000 en valor absoluto.

## Salida

El mayor |x| + |y| sobre todos los cruces.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 0 1 1
1 0 1 1
1 3 2 1
```

Salida:

```
4
```

## Solución

El coste |x| + |y| es la mayor de las cuatro funciones lineales ±x ± y,
así que la respuesta es el mayor valor de una función lineal sobre todos
los cruces del arreglo, tomado en cuatro direcciones. Un hecho clásico
de los arreglos de rectas dice que el cruce extremo en cualquier
dirección lo forman dos rectas vecinas en el orden cíclico de
pendientes. Así que se ordenan las rectas por dirección con una
comparación exacta por producto vectorial y se comprueban los N cruces
de vecinas cíclicas.

Escribiendo una recta como dy · x − dx · y = c, el cruce de dos rectas es
una fracción de denominador |dx₁ dy₂ − dy₁ dx₂|, y su norma L1 es
(|dx₁ c₂ − c₁ dx₂| + |dy₁ c₂ − c₁ dy₂|) dividido entre ese denominador.
La mejor fracción se guarda de forma exacta con multiplicación cruzada
de enteros. Para imprimirla se separa el cociente entero y se redondea solo
el resto a doce decimales, llevando una unidad a la parte entera si hace
falta. Así se evita el desbordamiento al escalar todo el numerador.
El denominador es como máximo 8 · 10⁶, por lo que una respuesta positiva
es al menos 1/(8 · 10⁶) y el error relativo del redondeo es como máximo
4 · 10⁻⁶. El cero se imprime exactamente.
El tiempo es O(N log N) y la memoria O(N).

Trampa (prueba [22](tests/22.in)): seis decimales pueden superar el límite
de error relativo cerca de cero: 18/3617 se redondea a 0.004976, con error
relativo mayor que 10⁻⁴. El verificador calcula la fracción exacta a partir
de la entrada, ya que las salidas guardadas también pueden estar redondeadas.

En el ejemplo las rectas y = x y x = 1 se cortan en (1, 1), la recta por
(1, 3) y (2, 1) corta a y = x en (5/3, 5/3) y a x = 1 en (1, 3), la más
lejana, con coste 4.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2166_geometry_sorting.cpp](2166_geometry_sorting.cpp) | G++ 13.2 x64 | geometry, sorting | O(N log N) | AC | 0.078 s | 2304 KB |
| [2166_geometry_sorting.go](2166_geometry_sorting.go) | Go 1.14 x64 | geometry, sorting | O(N log N) | AC | 0.062 s | 8264 KB |
| [2166_geometry_sorting.java](2166_geometry_sorting.java) | Java 1.8 | geometry, sorting | O(N log N) | AC | 0.203 s | 9096 KB |
| [2166_geometry_sorting.py](2166_geometry_sorting.py) | Python 3.12 x64 | geometry, sorting | O(N log N) | AC | 1.078 s | 44556 KB |
| [2166_geometry_sorting.rs](2166_geometry_sorting.rs) | Rust 1.75 x64 | geometry, sorting | O(N log N) | AC | 0.062 s | 5520 KB |
