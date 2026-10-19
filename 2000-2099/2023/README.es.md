# 2023. Pasos entre tres destinos

[Timus 2023](https://acm.timus.ru/problem.aspx?space=1&num=2023) · dificultad 40 · implementation

Problema original de Alex Samsonov, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres destinos ocupan las posiciones consecutivas 0, 1 y 2 de una línea.
Cada etiqueta pertenece a un único destino según esta tabla completa:

| Posición | Etiquetas |
| --- | --- |
| 0 | Alice, Ariel, Aurora, Phil, Peter, Olaf, Phoebus, Ralph, Robin |
| 1 | Bambi, Belle, Bolt, Mulan, Mowgli, Mickey, Silver, Simba, Stitch |
| 2 | Dumbo, Genie, Jiminy, Kuzko, Kida, Kenai, Tarzan, Tiana, Winnie |
Procesa `n` etiquetas en el orden dado, empezando en la posición 0. Ir a
una posición adyacente cuesta un paso; procesar una etiqueta en su
destino no cuesta pasos. Calcula el total. El recorrido termina en el
último destino, sin obligación de volver a la posición 0. Las etiquetas
pueden repetirse. Límites: `1 ≤ n ≤ 1000`, 1 segundo, 64 MB.

## Entrada

La primera línea contiene `n`. Cada una de las siguientes `n` líneas
contiene una etiqueta de la tabla con la grafía y las mayúsculas
indicadas. Su orden es el de procesamiento. Las etiquetas solo tienen
letras y su longitud no supera siete.

## Salida

Un entero: el número total de pasos, entre 0 y `2n`, ambos incluidos.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
4
Aurora
Tiana
Ariel
Mulan
```

```
5
```

## Solución

Tras cada etiqueta basta recordar la posición actual. Las iniciales de
los tres grupos son disjuntas: `A, P, O, R` corresponden a la posición
0; `B, M, S`, a la posición 1; las demás iniciales permitidas (`D, G, J,
K, T, W`), a la posición 2. Este atajo es válido porque todas las
etiquetas de entrada pertenecen a la tabla.

Inicializa `position = 0` y `steps = 0`. Para cada etiqueta determina
`target`, suma `abs(target - position)` a `steps` y actualiza `position
= target`. Tras exactamente `n` etiquetas imprime `steps`. No se deben
ordenar ni reorganizar las etiquetas.

Para demostrarlo, considera un desplazamiento desde `p` hasta `q`. Cada
paso modifica la coordenada en una unidad, así que hacen falta al menos
`|q-p|` pasos. Caminar directamente hacia `q` alcanza esa cota. El orden
obligatorio fija cada par de destinos consecutivos, incluida la posición
inicial 0. Por tanto, sumar esas distancias exactas da el recorrido
requerido. Por inducción, después de cada etiqueta los contadores
representan su destino y la distancia exacta acumulada. No hay otro
desplazamiento después de la última etiqueta.

En el ejemplo, las posiciones son `0 → 0 → 2 → 0 → 1`; los pasos suman
`0 + 2 + 2 + 1 = 5`. El tiempo es `O(n)` porque las etiquetas tienen
longitud acotada. El recorrido usa `O(1)` contadores; estos programas
guardan la entrada, por lo que su memoria adicional total es `O(n)`. Una
lectura que procese cada etiqueta inmediatamente permitiría `O(1)`.

Trampas:

- La posición inicial es la de la izquierda, incluso antes de la primera
  etiqueta.
- Pasar entre los extremos cuesta dos pasos; permanecer en un destino
  cuesta cero.
- Respeta el orden y las repeticiones; no añadas un regreso al final.
- Conserva las grafías `Mickey`, `Kuzko` y `Phoebus`. La inicial
  identifica el destino, no un intervalo alfabético ni una casilla
  individual.

## Notas por lenguaje

Los cinco programas hacen el mismo recorrido y usan enteros ordinarios:
el máximo es 2000. C++ busca en cadenas, Go busca la inicial ASCII como
rune, Rust como byte, Java usa `indexOf` y Python pertenencia a cadenas.
La entrada con búfer basta para 1000 etiquetas; CPython no necesita un
entorno alternativo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2023_implementation.cpp](2023_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 460 KB |
| [2023_implementation.go](2023_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1160 KB |
| [2023_implementation.java](2023_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 596 KB |
| [2023_implementation.py](2023_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 388 KB |
| [2023_implementation.rs](2023_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.062 s | 248 KB |
