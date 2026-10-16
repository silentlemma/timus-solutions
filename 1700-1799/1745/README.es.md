# 1745. Otra respuesta más

[Timus 1745](https://acm.timus.ru/problem.aspx?space=1&num=1745) · dificultad 817 · dp

Problema original de Damir Akhmetzyanov, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dadas n palabras de paréntesis, unir algunas, cada una a lo sumo una
vez y en cualquier orden, en la secuencia de paréntesis correcta más
larga.

## Entrada

n (1 ≤ n ≤ 1000) y luego las palabras; su longitud total es a lo sumo
10 000.

## Salida

La longitud l y el número k de palabras usadas, y luego los k números
de palabra en orden. Se acepta cualquier respuesta más larga.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
(
(((
(
))
```

Salida:

```
4 3
1 3 4
```

### Ejemplo 2

Entrada:

```
3
()
(()
)
```

Salida:

```
6 3
2 3 1
```

## Solución

Se describe cada palabra por el cambio de profundidad que causa y la
profundidad mínima que alcanza desde su inicio. En una respuesta
óptima, las palabras que no bajan la profundidad pueden ir primero, las
que menos se hunden antes: adelantar una de ellas solo sube la
profundidad para todas las que siguen. Las palabras que bajan la
profundidad van al final; al invertirlas e intercambiar los paréntesis,
se obtiene el mismo caso, que pone primero aquellas cuyo final queda
más alto sobre su punto más bajo. Así hay una respuesta óptima que toma
las palabras elegidas en este único orden fijo.

Luego es una mochila sobre el orden fijo: para cada profundidad d, el
prefijo más largo construido hasta ahora que termina en la profundidad
d. Una palabra puede seguir a la profundidad d si d más su profundidad
mínima no baja de cero, y lleva a la profundidad d más su cambio. La
respuesta es el valor en la profundidad 0, y una tabla de qué palabras
se tomaron recupera el orden. La profundidad nunca pasa de la longitud
total L. `O(n·L)`, unos 10⁷ pasos.

En el primer ejemplo `(`, `(` y `))` dan `(())` de longitud 4; `(((`
necesitaría tres paréntesis de cierre más.

Trampas:

- la respuesta vacía está permitida: `0 0` y una línea vacía;
- una palabra como `)(` necesita una profundidad de 1 antes de ella y
  conserva la profundidad;
- el orden dentro de cada mitad importa: una palabra que se hunde mucho
  debe ir mientras la profundidad aún es alta.

El comprobador verifica la secuencia, que los números de palabra sean
distintos y la longitud. Las longitudes coinciden con una búsqueda
sobre todas las elecciones ordenadas de palabras en 400 conjuntos
aleatorios de hasta 6 palabras, y con una implementación aceptada
independiente en las pruebas grandes. La solución en Python corre en
PyPy, ya que sus 10⁷ pasos tardan aquí unos 0,5 s con CPython.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1745_dp.cpp](1745_dp.cpp) | G++ 13.2 x64 | dp | O(n·L) | AC | 0.031 s | 10276 KB |
| [1745_dp.go](1745_dp.go) | Go 1.14 x64 | dp | O(n·L) | AC | 0.031 s | 8588 KB |
| [1745_dp.java](1745_dp.java) | Java 1.8 | dp | O(n·L) | AC | 0.140 s | 12788 KB |
| [1745_dp.py](1745_dp.py) | PyPy 3.10 x64 | dp | O(n·L) | AC | 0.250 s | 23664 KB |
| [1745_dp.rs](1745_dp.rs) | Rust 1.75 x64 | dp | O(n·L) | AC | 0.046 s | 10488 KB |
