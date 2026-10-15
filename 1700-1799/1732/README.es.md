# 1732. Ministerio de la Verdad

[Timus 1732](https://acm.timus.ru/problem.aspx?space=1&num=1732) · dificultad 558 · strings

Problema original de Alex Samsonov (preparado por Dmitry Ivankov), del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Borrar algunas letras de un dicho, y cada letra borrada se convierte en
un espacio, de modo que se lea como otro dicho dado una vez que las
rachas de espacios se reducen a uno y se recortan los extremos. Mostrar
qué letras borrar.

## Entrada

El dicho original y el deseado, cada uno de hasta 100 000 caracteres:
palabras de letras latinas separadas por espacios simples. Los dos son
distintos.

## Salida

El dicho original con las letras borradas cambiadas por `_`, o
`I HAVE FAILED!!!` si no se puede. Se acepta cualquier respuesta
válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
Preved to Medved
Preved Me
```

Salida:

```
Preved __ Me____
```

### Ejemplo 2

Entrada:

```
this is impossible
im possible
```

Salida:

```
I HAVE FAILED!!!
```

## Solución

Cada palabra deseada debe ser un tramo de letras dentro de una palabra
original, y dos palabras deseadas dentro de la misma palabra original
necesitan al menos una letra borrada entre ellas. Los espacios del
original no se pueden quitar, así que una palabra deseada nunca abarca
dos palabras originales.

Se recorren las palabras originales en orden y se colocan las deseadas
de forma voraz: cada una en su primera aparición en la palabra actual,
al menos dos posiciones después del final de la anterior en ella. Si no
aparece en lo que queda de la palabra, se pasa a la siguiente. La
colocación más temprana deja el mayor espacio para lo que sigue, así
que si al voraz se le acaban las palabras originales, nada funciona.
Toda letra no conservada se convierte en `_`.

Buscar con un `find` de biblioteca puede ser cuadrático, por ejemplo
una palabra de 100 000 aes frente a una palabra deseada de aes que
termina en b. Por eso la búsqueda usa la función de prefijos de la
palabra deseada actual, que se reconstruye solo cuando esa palabra
cambia, y cada búsqueda empieza donde terminó la anterior, así que cada
letra original se examina una sola vez. `O(L)`.

En el primer ejemplo `Preved` se conserva entera, `to` se borra y `Me`
es el comienzo de `Medved`.

Trampas:

- `abab` no puede convertirse en `ab ab`: el espacio tiene que salir de
  una letra borrada, y por la misma razón `impossible` no da
  `im possible` en el segundo ejemplo;
- las letras distinguen mayúsculas y minúsculas;
- una palabra deseada no puede unir dos palabras originales: `to Me`
  nunca da `toMe`.

El comprobador verifica que solo letras se convirtieron en guiones bajos
y que el resultado se lee como el dicho deseado. Las respuestas
coinciden con una búsqueda exhaustiva de todos los borrados en 300
dichos cortos, y con una implementación aceptada independiente en los
largos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1732_strings.cpp](1732_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.046 s | 2676 KB |
| [1732_strings.go](1732_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.031 s | 3296 KB |
| [1732_strings.java](1732_strings.java) | Java 1.8 | strings | O(L) | AC | 0.156 s | 6484 KB |
| [1732_strings.py](1732_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.156 s | 6320 KB |
| [1732_strings.rs](1732_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.031 s | 2184 KB |
