# 1881. Enunciado largo

[Timus 1881](https://acm.timus.ru/problem.aspx?space=1&num=1881) · dificultad 62 · simulation

Problema original de Fedor Fominykh, del Concurso Regional Escolar de Programación de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una página tiene h líneas de w caracteres. Las palabras de una línea se
separan con un solo espacio, y una palabra que no cabe en la línea
actual empieza otra; las palabras nunca se parten. ¿Cuántas páginas
ocupa un texto de n palabras?

## Entrada

h, w y n (1 ≤ h, w ≤ 100, 1 ≤ n ≤ 10 000), luego n palabras, una por
línea, cada una de como mucho w caracteres; su longitud total es como
mucho 10 000.
Las palabras no están vacías y solo contienen letras inglesas mayúsculas
y minúsculas y los signos de puntuación `.,!?`.

## Salida

El número de páginas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5 6
To
be
or
not
to
be
```

Salida:

```
2
```

## Solución

Se llenan las líneas de forma voraz. Se guarda cuántos caracteres van
usados en la línea actual; una palabra necesita su longitud más un
espacio salvo si empieza la línea. Si no cabe, empieza una línea nueva.
Empezar la cuenta en −1 hace que la primera palabra de una línea no
necesite espacio. La respuesta es el número de líneas dividido entre h
y redondeado hacia arriba. `O(n)`.

En el ejemplo las líneas son "To be", "or", "not" y "to be": "or not" y
"not to" tienen un carácter de más. Cuatro líneas en páginas de tres
ocupan dos páginas.

Trampas:

- una palabra que llena justo el resto de la línea, espacio incluido,
  todavía cabe;
- el espacio solo va entre palabras, nunca al principio de una línea;
- el número de páginas se redondea hacia arriba.

Los recuentos coinciden con una implementación aceptada independiente
en 100 textos aleatorios.

## Soluciones optimizadas

`1881_simulation_optimized.java`. Java mantiene el ajuste voraz de palabras completas. Cuenta sus bytes directamente en el búfer compartido de entrada de 1024 bytes, incluso al cruzar recargas y llegar al EOF, sin crear cadenas por palabra. Conserva solo el ancho ocupado y el número de líneas; una palabra que no cabe inicia otra línea y las páginas son ceil(lines/height). Emite el entero mediante búferes fijos. Para B bytes de entrada, tiempo O(B) y espacio auxiliar O(1); no almacena un arreglo de palabras ni texto unido. Las comprobaciones independientes construyeron líneas reales e incluyeron ajustes exactos, palabras largas, límites del búfer y ausencia del salto de línea final.

Accepted exacto Java 1.8 #11327457: 0.109 s / 356 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 21/202, memoria 1/202. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303783 era 0.125 s / 408 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1881_simulation_optimized.java`: 0.109 s / 356 KB; base didáctica conservada `1881_simulation.java`: 0.109 s / 1336 KB.

La solución optimizada en C++ nunca guarda una palabra: lee cada palabra
carácter a carácter con `getchar` y conserva solo su longitud, que es
todo lo que necesita el reparto en líneas. Ocupa 128 KB en lugar de
404 KB, con el mismo tiempo.

Leer las palabras por líneas y usar solo sus longitudes para distribuirlas en páginas. El envío aceptado 11303784 tardó 0.093 s y usó 488 KB. La versión sencilla tardó 0.078 s y usó 656 KB. El tiempo registrado es mayor que el de la versión sencilla.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1881_simulation.cpp](1881_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 404 KB | 11291031 |
| [1881_simulation.go](1881_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.031 s | 1236 KB | 11291032 |
| [1881_simulation.java](1881_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.109 s | 1336 KB | 11291035 |
| [1881_simulation.py](1881_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 656 KB | 11291034 |
| [1881_simulation.rs](1881_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.031 s | 256 KB | 11291036 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1881_simulation_optimized.cpp](1881_simulation_optimized.cpp) \* | G++ 13.2 x64 | simulation | O(n) | AC | 0.031 s | 128 KB | 11303646 |
| [1881_simulation_optimized.java](1881_simulation_optimized.java) \* | Java 1.8 | simulation | O(B) time; O(1) auxiliary space | AC | 0.109 s | 356 KB | 11327457 |
| [1881_simulation_optimized.py](1881_simulation_optimized.py) \* | Python 3.12 x64 | simulation | O(n) | AC | 0.093 s | 488 KB | 11303784 |

\* Accepted; aún no alcanza la meta de clasificación separada: C++ requiere los diez primeros o el 15% superior tanto en tiempo como en memoria; las demás familias de lenguajes requieren el primer puesto en ambas. Esta marca es independiente de los criterios de admisión; la versión admite más optimización.
