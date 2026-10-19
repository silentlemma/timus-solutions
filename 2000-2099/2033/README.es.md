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

## Notas por lenguaje

C++ usa `unordered_map`, Go `map`, Rust y Java `HashMap` y Python `dict`.
Go copia el valor de la tabla, lo cambia y lo guarda otra vez. Rust y los demás
inicializan el mínimo con el primer precio. Frecuencias hasta seis y precios
caben en enteros ordinarios con signo. Java lee las tres líneas indicadas;
los otros programas separan por blancos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2033_hashing.cpp](2033_hashing.cpp) | G++ 13.2 x64 | hashing | O(1) | AC | 0.015 s | 384 KB |
| [2033_hashing.go](2033_hashing.go) | Go 1.14 x64 | hashing | O(1) | AC | 0.031 s | 1116 KB |
| [2033_hashing.java](2033_hashing.java) | Java 1.8 | hashing | O(1) | AC | 0.109 s | 612 KB |
| [2033_hashing.py](2033_hashing.py) | Python 3.12 x64 | hashing | O(1) | AC | 0.109 s | 452 KB |
| [2033_hashing.rs](2033_hashing.rs) | Rust 1.75 x64 | hashing | O(1) | AC | 0.046 s | 436 KB |
