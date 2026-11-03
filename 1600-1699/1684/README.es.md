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

## Evaluación

Se verifica que las piezas formen el texto y cada una sea prefijo del patrón; se acepta cualquier descomposición válida y se comprueba la imposibilidad.

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

## Soluciones optimizadas

El nuevo algoritmo usa función prefijo y elección voraz de la última pieza más larga, en lugar de Z y cortes alcanzables hacia delante. El diccionario contiene prefijos: extender la última pieza hacia la izquierda solo puede acortar un prefijo anterior válido, por lo que la elección es segura. Se guarda la longitud coincidente en cada extremo, se reconstruyen cortes hacia atrás y se emiten segmentos originales. Enlaces y longitudes compactos reemplazan el búfer Z combinado y las copias de salida.

- `1684_greedy_strings.cpp`: 0.015 s / 836 KB; base `1684_strings.cpp`: 0.015 s / 6084 KB; cambio respecto a la base: tiempo -0.0%, memoria -86.3%.
- `1684_greedy_strings.go`: 0.015 s / 2068 KB; base `1684_strings.go`: 0.031 s / 7368 KB; cambio respecto a la base: tiempo -51.6%, memoria -71.9%.
- `1684_greedy_strings.java`: 0.109 s / 1248 KB; base `1684_strings.java`: 0.140 s / 8584 KB; cambio respecto a la base: tiempo -22.1%, memoria -85.5%.
- `1684_greedy_strings.py`: 0.156 s / 1692 KB; base `1684_strings.py`: 0.250 s / 7360 KB; cambio respecto a la base: tiempo -37.6%, memoria -77.0%.
- `1684_greedy_strings.rs`: 0.015 s / 1288 KB; base `1684_strings.rs`: 0.031 s / 4176 KB; cambio respecto a la base: tiempo -51.6%, memoria -69.2%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1684_strings.cpp`; versión que cubre `1684_greedy_strings.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 67/67.

- Go: base didáctica preferida `1684_strings.go`; versión que cubre `1684_strings.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1684_strings.java`; versión que cubre `1684_greedy_strings.java`; puestos tiempo/memoria 1/1, registros de otros autores 6/6.

- Python/PyPy: base didáctica preferida `1684_strings.py`; versión que cubre `1684_greedy_strings.py`; puestos tiempo/memoria 6/1, registros de otros autores 30/30.

- Rust: base didáctica preferida `1684_strings.rs`; versión que cubre `1684_strings.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1684_strings.cpp](1684_strings.cpp) | G++ 13.2 x64 | strings | O(m + n) | AC | 0.015 s | 6084 KB | 11308841 |
| [1684_strings.go](1684_strings.go) | Go 1.14 x64 | strings | O(m + n) | AC | 0.031 s | 7368 KB | 11288854 |
| [1684_strings.java](1684_strings.java) | Java 1.8 | strings | O(m + n) | AC | 0.140 s | 8584 KB | 11288857 |
| [1684_strings.py](1684_strings.py) | Python 3.12 x64 | strings | O(m + n) | AC | 0.250 s | 7360 KB | 11309202 |
| [1684_strings.rs](1684_strings.rs) | Rust 1.75 x64 | strings | O(m + n) | AC | 0.031 s | 4176 KB | 11309203 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1684_greedy_strings.cpp](1684_greedy_strings.cpp) | G++ 13.2 x64 | greedy, strings | O(pattern length + text length) | AC | 0.015 s | 836 KB | 11309270 |
| [1684_greedy_strings.go](1684_greedy_strings.go) | Go 1.14 x64 | greedy, strings | O(pattern length + text length) | AC | 0.015 s | 2068 KB | 11309272 |
| [1684_greedy_strings.java](1684_greedy_strings.java) | Java 1.8 | greedy, strings | O(pattern length + text length) | AC | 0.109 s | 1248 KB | 11309271 |
| [1684_greedy_strings.py](1684_greedy_strings.py) \* | Python 3.12 x64 | greedy, strings | O(pattern length + text length) | AC | 0.156 s | 1692 KB | 11309268 |
| [1684_greedy_strings.rs](1684_greedy_strings.rs) | Rust 1.75 x64 | greedy, strings | O(pattern length + text length) | AC | 0.015 s | 1288 KB | 11309273 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
