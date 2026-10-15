# 1680. El primero que no clasifica

[Timus 1680](https://acm.timus.ru/problem.aspx?space=1&num=1680) · dificultad 223 · strings

Problema original de Dmitry Ivankov, preparado por Alexander Ipatov, del X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una semifinal envía q equipos a la final, como mucho uno por
universidad: todo equipo que quedó por debajo de otro equipo de su
misma universidad se tacha de la clasificación. Imprimir el equipo que
queda en el puesto q + 1 tras tachar.

## Entrada

El año, n (n ≤ 201) y q (3 ≤ q ≤ 12), y luego los n equipos en orden de
puestos. Un equipo se escribe como el nombre de la universidad, un
espacio, '#' y su número de 1 a 8; una universidad con un solo equipo
puede escribirse sin número. Los nombres constan de letras latinas,
espacios, '.', '-' y '&', con 36 caracteres como mucho, y dos
universidades nunca difieren solo en mayúsculas. La respuesta existe.

## Salida

El nombre de ese equipo tal como aparece en la clasificación.

## Ejemplos

### Ejemplo 1

Entrada:

```
1999 10 6
St Petersburg SU #1
Belarusian SU #1
Moscow SU #4
Southern Ural SU
Moscow SU #1
Novosibirsk SU #1
St Petersburg SU #3
Belarusian SU #3
St Petersburg IFMO #1
Ural SU #3
```

Salida:

```
Ural SU #3
```

## Solución

Se recorre la clasificación guardando el conjunto de universidades que
ya tienen un equipo en la lista. La universidad de un equipo es el
texto antes de su último '#', sin el espacio final, o la línea entera
si no hay '#'. Como dos universidades nunca difieren solo en
mayúsculas, los nombres se comparan en minúsculas. Un equipo de una
universidad ya presente se salta; si no, cuando el conjunto ya tiene q
universidades este equipo es la respuesta, y si no, su universidad
entra en el conjunto. `O(n · L)` para nombres de longitud L.

Trampas:

- la misma universidad puede aparecer con distintas mayúsculas
  («Ural SU» y «URAL SU», test 02), así que se compara sin distinguir
  mayúsculas;
- se comparan nombres completos: «Ural SU» y «Ural SU State» son
  universidades distintas (test 03);
- el equipo se imprime exactamente como viene, con su número.

Las respuestas coinciden con una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1680_strings.cpp](1680_strings.cpp) | G++ 13.2 x64 | strings | O(n · L) | AC | 0.015 s | 420 KB |
| [1680_strings.go](1680_strings.go) | Go 1.14 x64 | strings | O(n · L) | AC | 0.015 s | 1088 KB |
| [1680_strings.java](1680_strings.java) | Java 1.8 | strings | O(n · L) | AC | 0.078 s | 472 KB |
| [1680_strings.py](1680_strings.py) | Python 3.12 x64 | strings | O(n · L) | AC | 0.078 s | 456 KB |
| [1680_strings.rs](1680_strings.rs) | Rust 1.75 x64 | strings | O(n · L) | AC | 0.015 s | 432 KB |
