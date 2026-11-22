# 2033. Elegir un modelo por frecuencia y precio mínimo

[Timus 2033](https://acm.timus.ru/problem.aspx?space=1&num=2033) · dificultad 104 · hashing

Problema original de Ilya Kuchumov, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay exactamente seis registros de compra, cada uno con persona, modelo y precio.
Elige un modelo presente en el mayor número de registros; entre los empatados,
prefiere el menor precio observado para ese modelo. Si ambos criterios empatan,
cualquier modelo óptimo sirve. Los nombres de personas pueden coincidir:
cada registro cuenta, sin deduplicar por nombre.

Las personas tienen nombres de 1–20 letras inglesas minúsculas, los modelos
1–20 letras minúsculas o dígitos. Precio entero de 1 a `1000000`.
Límites: 1 segundo y 64 MB.

## Entrada

Exactamente seis descripciones de tres líneas: persona, modelo, precio.
No se da una cantidad inicial de registros.

## Salida

Un nombre de modelo óptimo, conservando su cadena y los posibles ceros
iniciales.

## Evaluación

Un comprobador acepta cualquier modelo con el mayor número de registros
y, entre ellos, el menor precio.

## Ejemplos

```
oleg
nexus4
13000
kirill
kurtka
20000
den
nexus4
12000
nikita
htc
10000
mikhail
nexus4
14000
alexey
htc
9500
```

```
nexus4
```

## Solución

Usa una tabla hash de modelo a frecuencia y mínimo precio. Lee el nombre
de persona, pero no lo uses como clave. Al crear una entrada, comienza
con frecuencia cero y el precio actual; después incrementa la frecuencia
y actualiza el mínimo. Recorre las entradas, prefiriendo mayor
frecuencia y después menor precio. Los programas usan el menor nombre
léxico en un empate completo para obtener una salida determinista; el
problema permite todos los empatados óptimos.

Tras cualquier prefijo, cada entrada contiene exactamente el número de
registros y el mínimo precio de su modelo en ese prefijo. La
inicialización, el incremento y el mínimo conservan el invariante;
después de seis registros las puntuaciones son exactas. En el recorrido
final la respuesta es la mejor entre las entradas visitadas; comparar
los dos criterios conserva esa propiedad y termina en un óptimo global.

En el ejemplo `nexus4` aparece tres veces, mínimo 12000; `htc` dos, mínimo 9500;
`kurtka` una, 20000. La frecuencia es prioritaria, así que gana `nexus4`,
aunque un modelo minoritario sea más barato.

Para `k` registros, tiempo hash esperado `O(k)` y espacio `O(k)` con
palabras de hasta 20 caracteres. Aquí `k=6` es fijo, por lo que tiempo y
espacio reales están acotados por constantes. No se supone una entrada
de más de seis registros.

Trampas:

- Cuenta registros, no nombres de personas distintos.
- Usa el precio mínimo, no suma, media, último ni máximo.
- La frecuencia tiene prioridad sobre el precio.
- Inicializa el primer precio con su registro, sin dejar un cero por defecto.
- Los modelos numéricos siguen siendo cadenas con sus ceros iniciales.

## Soluciones optimizadas

`2033_hashing_optimized.py`. Lee tokens binarios por líneas; guarda [recuento, precio_mínimo] mutable por modelo, sin tuplas de registros ni lista de tokens de todo el archivo. Cuenta seis registros incluso con nombres repetidos, preservando ceros iniciales de modelos. Maximiza frecuencia, después minimiza precio; el orden lexicográfico solo resuelve un empate final permitido. Para I bytes, M modelos y longitud máxima de línea Lmax: O(I) tiempo esperado y O(M+Lmax) espacio auxiliar con nombres de hasta 20 caracteres. Conserva la base legible con registros y mapa.

Reutiliza el fuente histórico exacto CPython 3.12 Accepted #11307496: 0.078 s / 500 KB. En el grupo comparable guardado el 2026-11-20: tiempo 4/61, memoria 32/61. Bajo 1024 KB, admisión estricta solo por tiempo, superada. El asterisco sigue la meta separada del lenguaje. Son medidas emparejadas de este fuente, no nuevo envío ni garantía portátil. Usa finalización normal del intérprete.

- `2033_hashing_optimized.py`: 0.078 s / 500 KB; base didáctica conservada `2033_hashing.py` (Python 3.12 x64): 0.109 s / 452 KB. Ambas medidas de la base quedan explícitas aunque una aumente.

`2033_implementation.java`. Sustituye agrupación hash por recorrer hasta seis nombres en arreglos fijos. Cuenta cada compra aunque se repita la persona y guarda el precio mínimo por modelo. Preserva cadenas y ceros iniciales, usando orden lexicográfico solo para empates permitidos tras cuenta/precio. Seis registros dan O(L) trabajo de caracteres y espacio de seis nombres, sin Record ni HashMap. El nombre público es implementation porque ya no usa hash; mantiene los bytes Accepted y la versión didáctica hashing.

Frente a `2033_hashing.java`: tiempo 0.125 s → 0.109 s; memoria 628 KB → 572 KB.

La solución optimizada en C++ prescinde de la tabla hash: con solo seis
registros compara cada registro con los seis, contando los registros del
mismo modelo y tomando su precio mínimo, 36 comparaciones en total, y se
queda con el mejor registro con el mismo desempate. Los nombres se leen
con `scanf` en arreglos fijos de 21 bytes, suficientes para
20 caracteres y el cero final, en lugar de `std::string` e `iostream`:
{2033_bruteforce.cpp}.

La solución optimizada en Rust prescinde de la tabla hash: con solo seis
registros compara cada registro con los seis, contando los registros del
mismo modelo y tomando su precio mínimo, 36 comparaciones en total, y se
queda con el mejor registro con el mismo desempate. Los seis modelos
siguen siendo trozos del texto de entrada en un arreglo fijo en lugar de
copias en un `HashMap`: {2033_bruteforce.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y cumple un criterio de clasificación
o de mejora de recursos. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `2033_bruteforce.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +67.71%; base: `2033_hashing.cpp`.

- `2033_bruteforce.rs`: reducción de tiempo +0.00%; reducción de memoria
  +47.71%; base: `2033_hashing.rs`.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`2033_implementation.java`: puesto de tiempo 24/207 y de memoria 32/207 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2033_hashing.cpp](2033_hashing.cpp) | G++ 13.2 x64 | hashing | O(1) | AC | 0.015 s | 384 KB | 11293121 |
| [2033_hashing.go](2033_hashing.go) | Go 1.14 x64 | hashing | O(1) | AC | 0.031 s | 1116 KB | 11293123 |
| [2033_hashing.java](2033_hashing.java) | Java 1.8 | hashing | O(1) | AC | 0.125 s | 628 KB | 11304031 |
| [2033_hashing.py](2033_hashing.py) | Python 3.12 x64 | hashing | O(1) | AC | 0.109 s | 452 KB | 11293124 |
| [2033_hashing.rs](2033_hashing.rs) | Rust 1.75 x64 | hashing | O(1) | AC | 0.046 s | 436 KB | 11293128 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2033_bruteforce.cpp](2033_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 124 KB | 11304029 |
| [2033_bruteforce.rs](2033_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.046 s | 228 KB | 11304030 |
| [2033_implementation.java](2033_implementation.java) \* | Java 1.8 | implementation | O(L), six records | AC | 0.109 s | 572 KB | 11325123 |
| [2033_hashing_optimized.py](2033_hashing_optimized.py) \* | Python 3.12 x64 | hashing | O(I) expected time; O(M+Lmax) space | AC | 0.078 s | 500 KB | 11307496 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
