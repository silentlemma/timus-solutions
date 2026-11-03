# 1680. El primero que no clasifica

[Timus 1680](https://acm.timus.ru/problem.aspx?space=1&num=1680) · dificultad 224 · strings

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

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

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

## Soluciones optimizadas

Se conserva la primera selección por universidad, ignorando mayúsculas en su identidad y manteniendo la escritura original del equipo. Al completar el cupo ya no se almacenan claves de universidades nuevas. Procesar los registros en flujo elimina la lista de todas las líneas y copias. La versión PyPy conserva Unicode para no cambiar la conversión de mayúsculas ni la codificación de salida al ahorrar memoria.

- `1680_strings_optimized.cpp`: 0.001 s / 100 KB; base `1680_strings.cpp`: 0.001 s / 400 KB; cambio respecto a la base: tiempo -0.0%, memoria -75.0%.
- `1680_strings_optimized.py`: 0.125 s / 244 KB; base `1680_strings.py`: 0.078 s / 364 KB; cambio respecto a la base: tiempo +60.3%, memoria -33.0%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1680_strings.cpp`; versión que cubre `1680_strings_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 47/47.

- Go: base didáctica preferida `1680_strings.go`; versión que cubre `1680_strings.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1680_strings.java`; versión que cubre `1680_strings.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1680_strings.py`; versión que cubre `1680_strings_optimized.py`; puestos tiempo/memoria 11/1, registros de otros autores 12/12.

- Rust: base didáctica preferida `1680_strings.rs`; versión que cubre `1680_strings.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1680_strings.cpp](1680_strings.cpp) | G++ 13.2 x64 | strings | O(n · L) | AC | 0.001 s | 400 KB | 11308838 |
| [1680_strings.go](1680_strings.go) | Go 1.14 x64 | strings | O(n · L) | AC | 0.015 s | 1088 KB | 11288810 |
| [1680_strings.java](1680_strings.java) | Java 1.8 | strings | O(n · L) | AC | 0.078 s | 472 KB | 11288813 |
| [1680_strings.py](1680_strings.py) | Python 3.12 x64 | strings | O(n · L) | AC | 0.078 s | 364 KB | 11308839 |
| [1680_strings.rs](1680_strings.rs) | Rust 1.75 x64 | strings | O(n · L) | AC | 0.015 s | 432 KB | 11288816 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1680_strings_optimized.cpp](1680_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(input size) | AC | 0.001 s | 100 KB | 11308250 |
| [1680_strings_optimized.py](1680_strings_optimized.py) \* | PyPy 3.10 x64 | strings | O(input size) | AC | 0.125 s | 244 KB | 11309387 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
