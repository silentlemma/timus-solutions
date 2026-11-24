# 1723. El libro de Sandro

[Timus 1723](https://acm.timus.ru/problem.aspx?space=1&num=1723) · dificultad 62 · strings

Problema original de Ivan Burmistrov (preparado por Olga Soboleva), del Concurso Regional de Programación por Equipos de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada subcadena de una palabra dada es un hechizo, y su fuerza es el
número de veces que aparece en la palabra, contando las apariciones
solapadas. Imprimir un hechizo de fuerza máxima.

## Entrada

Una palabra no vacía de a lo sumo 50 letras latinas minúsculas.

## Salida

Cualquier hechizo de fuerza máxima.

## Ejemplos

### Ejemplo 1

Entrada:

```
tebidohtebidoh
```

Salida:

```
tebidoh
```

## Solución

Cada aparición de un hechizo empieza con una aparición de su primera
letra, y apariciones distintas empiezan en lugares distintos. Así que
ningún hechizo es más fuerte que su primera letra sola, y una letra más
frecuente es un hechizo de fuerza máxima. `O(n)`.

En el ejemplo cada letra aparece dos veces, así que `t` es tan fuerte
como `tebidoh`.

Trampas:

- las apariciones pueden solaparse: `aba` aparece tres veces en
  `abababa`, pero `a` aparece cuatro;
- se acepta cualquier hechizo de fuerza máxima, así que las pruebas usan
  un comprobador.

El comprobador cuenta las apariciones de la respuesta, con solapamientos,
y las compara con las de la respuesta esperada. Una letra más frecuente
coincide con una búsqueda exhaustiva de todas las subcadenas en 300
palabras aleatorias.

## Soluciones optimizadas

`1723_strings_optimized.java`. Conserva conteo de 26 letras minúsculas y devuelve cualquiera de máxima frecuencia, también conjuro más fuerte. Palabra hasta cincuenta letras: contadores byte con signo no desbordan. Actualiza máximo durante lectura y escribe letra/salto en dos bytes. Sin guardar palabra, Scanner ni pasada final. O(N) tiempo, 26 bytes de conteo y estado constante; otro empate es válido.

Accepted exacto Java 1.8 #11327830: 0.109 s / 308 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 36/246, memoria 1/246. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303774 era 0.14 s / 348 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1723_strings_optimized.java`: 0.109 s / 308 KB; base didáctica conservada `1723_strings.java`: 0.125 s / 1556 KB.

La solución optimizada en C++ cuenta las letras a medida que las lee
con `getchar`, sin guardar la cadena: 84 KB en lugar de 352 KB.

Contar cada letra minúscula con el recuento de bytes incorporado y conservar la primera que alcanza el máximo. El envío aceptado 11302183 tardó 0.078 s y usó 392 KB. La versión sencilla tardó 0.078 s y usó 404 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1723_strings.cpp](1723_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 352 KB | 11303504 |
| [1723_strings.go](1723_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1068 KB | 11289348 |
| [1723_strings.java](1723_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 1556 KB | 11303505 |
| [1723_strings.py](1723_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 404 KB | 11289349 |
| [1723_strings.rs](1723_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 228 KB | 11289353 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1723_strings_optimized.cpp](1723_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 84 KB | 11303635 |
| [1723_strings_optimized.java](1723_strings_optimized.java) | Java 1.8 | strings | O(N) time; 26 byte counters | AC | 0.109 s | 308 KB | 11327830 |
| [1723_strings_optimized.py](1723_strings_optimized.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 392 KB | 11302183 |
