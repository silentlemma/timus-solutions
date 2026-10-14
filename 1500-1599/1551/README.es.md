# 1551. Torneo de sumo

[Timus 1551](https://acm.timus.ru/problem.aspx?space=1&num=1551) · dificultad 257 · math

Problema original de Sergey Pupyrev, del XI Campeonato Universitario por Equipos de Programación de los Urales, Ekaterimburgo, 21 de abril de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un torneo por eliminación tiene 2ᴺ luchadores (1 ≤ N ≤ 10) y N rondas;
cada luchador representa una prefectura. Los organizadores eligen el
cuadro inicial. Hay que hallar el mayor K tal que algún cuadro garantiza,
sean cuales sean los resultados, al menos K rondas en las que no se
enfrentan dos luchadores de la misma prefectura.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego 2ᴺ líneas con el nombre de un luchador y su prefectura.
Ambos campos contienen entre 1 y 30 letras latinas.

## Salida

K.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
Homasho Ishikawa
Tamakasuga Tokyo
Futeno Tochigi
Takekaze Tokyo
Kasugao Yamaguchi
Kotoshogiku Ishikawa
Kotomitsuki Tokyo
Miyabiyama Shizuoka
```

Salida:

```
1
```

## Solución

En la ronda r el cuadro empareja bloques de 2^(r−1) luchadores, y como
de un bloque puede salir cualquiera, la ronda r es segura exactamente
cuando las dos mitades de cada bloque de 2^r no comparten prefectura.

Tomemos la prefectura mayor, con c luchadores, y hagamos que siempre
ganen contra luchadores de otras prefecturas. Solo los encuentros entre
ellos eliminan a sus integrantes, y cada ronda insegura puede reducir
su número como mucho a la mitad. Pasar de c a uno requiere al menos
⌈log₂ c⌉ rondas inseguras, por lo que K ≤ N − ⌈log₂ c⌉.

La cota se alcanza: con k = ⌈log₂ c⌉ para el mayor c, se ordenan los
luchadores por prefectura y se reparten por turnos en los 2ᵏ bloques de
los k niveles superiores. Una prefectura tiene como mucho 2ᵏ luchadores,
así que caen en bloques distintos; dentro de un bloque todos son de
prefecturas distintas, así que las primeras N − k rondas son seguras.
La respuesta es por tanto N − ⌈log₂ c⌉. Se cuentan los luchadores por
prefectura, se toma el máximo y se incrementa k desde cero hasta que
2ᵏ ≥ c; se imprime N − k. Un oráculo exhaustivo de cuadros y resultados
coincidió en las 29 distribuciones de multiplicidades para N ≤ 3 y en
1200 entradas aleatorias. `O(2ᴺ log 2ᴺ)` para contar.

Detalles a tener en cuenta:

- una sola prefectura no deja ninguna ronda segura (pruebas 02, 04);
- c = 4 necesita solo dos rondas inseguras, c = 5 tres (pruebas 06, 07);
- las prefecturas se comparan tal como están escritas, así que Tokyo y
  tokyo son distintas (prueba 08).
- los nombres no afectan al recuento; ambos campos deben contener
  1–30 letras latinas, sin sufijos numéricos (pruebas 04–07).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1551_math.cpp](1551_math.cpp) | G++ 13.2 x64 | math | O(2^N log 2^N) | AC | 0.015 s | 544 KB |
| [1551_math.go](1551_math.go) | Go 1.14 x64 | math | O(2^N log 2^N) | AC | 0.031 s | 1276 KB |
| [1551_math.java](1551_math.java) | Java 1.8 | math | O(2^N log 2^N) | AC | 0.156 s | 3280 KB |
| [1551_math.py](1551_math.py) | Python 3.12 x64 | math | O(2^N log 2^N) | AC | 0.062 s | 696 KB |
| [1551_math.rs](1551_math.rs) | Rust 1.75 x64 | math | O(2^N log 2^N) | AC | 0.046 s | 576 KB |
