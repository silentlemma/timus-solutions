# 1713. Subcadenas clave

[Timus 1713](https://acm.timus.ru/problem.aspx?space=1&num=1713) · dificultad 633 · strings

Problema original de Dmitry Ivankov (idea de Alexander Mironenko), de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una clave de un comando es una subcadena suya que no es subcadena de
ningún otro comando. Para cada uno de los n comandos, hallar una clave
más corta.

## Entrada

n (2 ≤ n ≤ 1000) y luego n comandos: de 1 a 100 letras latinas
minúsculas. Ningún comando es subcadena de otro.

## Salida

Una clave más corta de cada comando, en el orden de entrada. Se acepta
cualquier clave más corta.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
abcm
acm
bcd
```

Salida:

```
ab
ac
d
```

## Solución

Una subcadena que empieza en la posición p de un comando está en otro
comando justo cuando es prefijo de algún sufijo de ese otro comando.
Así que en p la clave más corta tiene una letra más que el prefijo
común más largo con algún sufijo de otro comando, si cabe antes del
final del comando.

Se ordenan todos los sufijos de todos los comandos, a lo sumo 10⁵. En
el orden, el prefijo común de dos sufijos es el mínimo de los prefijos
comunes de los vecinos entre ellos. Por eso el mayor prefijo común con
un sufijo de otro comando se alcanza en el sufijo así más cercano por
arriba o por abajo. Dos barridos lo hallan. Al bajar, el valor en curso
vuelve a empezar en el prefijo común con el vecino cuando este es de
otro comando, y si no toma el mínimo con él. Al subir es igual. El
mejor inicio de cada comando da su clave. `O(L log L · ℓ)` para L
letras en total y comandos de longitud ℓ.

Trampas:

- el comando entero siempre es una clave, pues ningún comando está
  dentro de otro, así que cada comando tiene respuesta;
- una subcadena que se repite dentro de su propio comando puede seguir siendo
  clave: solo cuentan los otros comandos;
- se acepta cualquier clave más corta, así que las pruebas usan un
  comprobador.

El comprobador verifica que cada clave esté en su comando, en ningún
otro, y tenga la longitud mínima. Las longitudes coinciden con una
implementación aceptada independiente en 200 conjuntos pequeños
aleatorios y en otros grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1713_strings.cpp](1713_strings.cpp) | G++ 13.2 x64 | strings | O(L log L · ℓ) | AC | 0.062 s | 1940 KB |
| [1713_strings.go](1713_strings.go) | Go 1.14 x64 | strings | O(L log L · ℓ) | AC | 0.109 s | 11560 KB |
| [1713_strings.java](1713_strings.java) | Java 1.8 | strings | O(L log L · ℓ) | AC | 0.265 s | 20316 KB |
| [1713_strings.py](1713_strings.py) | Python 3.12 x64 | strings | O(L log L · ℓ) | AC | 0.593 s | 20308 KB |
| [1713_strings.rs](1713_strings.rs) | Rust 1.75 x64 | strings | O(L log L · ℓ) | AC | 0.062 s | 5640 KB |
