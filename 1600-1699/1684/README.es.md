# 1684. La última palabra de Jack

[Timus 1684](https://acm.timus.ru/problem.aspx?space=1&num=1684) · dificultad 266 · strings

Problema original de Dmitry Ivankov, del X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dadas una palabra y una segunda palabra, partir la segunda en trozos
que sean cada uno un prefijo no vacío de la primera, o informar de que
no se puede.

## Entrada

Las dos palabras, una por línea, no vacías, de letras latinas
minúsculas, cada una de longitud a lo sumo 75000.

## Salida

No y, en la línea siguiente, los trozos separados por espacios, si
existe una partición; si no, Yes. Se acepta cualquier partición válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
abracadabra
abrabracada
```

Salida:

```
No
abr abracad a
```

### Ejemplo 2

Entrada:

```
abracadabra
arbadacarba
```

Salida:

```
Yes
```

## Solución

Sea z[p] la longitud del prefijo más largo de la primera palabra que
empieza en la posición p de la segunda: la función Z de
word + "#" + last los da todos en tiempo lineal. Desde un corte en p el
siguiente trozo puede acabar en cualquiera de p + 1, …, p + z[p], pues
todo prefijo más corto también encaja. Así, los cortes alcanzables
forman siempre un rango entero 0, …, reach: se recorre p desde 0
mientras p ≤ reach y se extiende reach hasta p + z[p]. Cada corte q
recién cubierto recuerda el p que lo cubrió, y seguir esos enlaces
desde el final da los trozos.

Si el recorrido se detiene antes del final de la segunda palabra, la
respuesta es Yes. `O(m + n)` para palabras de longitudes m y n.

Trampas:

- tomar siempre el prefijo más largo puede fallar: para aab y aaab el
  voraz aa deja ab, mientras que a + aab funciona (test 06);
- las palabras de la respuesta están invertidas: No significa que hay
  partición;
- la línea de salida tiene hasta 75000 trozos, conviene construirla de
  una vez.

El verificador compara el veredicto con una implementación aceptada
independiente y comprueba que los trozos son prefijos que forman la
palabra.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1684_strings.cpp](1684_strings.cpp) | G++ 13.2 x64 | strings | O(m + n) | AC | 0.031 s | 6108 KB |
| [1684_strings.go](1684_strings.go) | Go 1.14 x64 | strings | O(m + n) | AC | 0.031 s | 7368 KB |
| [1684_strings.java](1684_strings.java) | Java 1.8 | strings | O(m + n) | AC | 0.140 s | 8584 KB |
| [1684_strings.py](1684_strings.py) | Python 3.12 x64 | strings | O(m + n) | AC | 0.265 s | 7024 KB |
| [1684_strings.rs](1684_strings.rs) | Rust 1.75 x64 | strings | O(m + n) | AC | 0.062 s | 5168 KB |
