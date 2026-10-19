# 1858. Cubo mágico

[Timus 1858](https://acm.timus.ru/problem.aspx?space=1&num=1858) · dificultad 3556 · bfs

Problema original de Mikhail Rubinchik (preparado por Denis Mukhametianov), del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cubo de lado n·l se construyó con n³ cristales cúbicos de lado l. Dos
caras en contacto llevan la misma runa, una cara exterior no lleva
ninguna, y cada runa aparece exactamente en dos caras. Los cristales se
dan por separado, cada uno en un giro desconocido, como las runas de sus
seis caras. Para varios pares de cristales hallar la distancia entre
sus centros en el cubo montado.

## Entrada

l y n (1 ≤ l ≤ 100, 2 ≤ n ≤ 30), luego n³ líneas de seis runas de 0 a
10⁹ (0 si no hay runa), luego m (1 ≤ m ≤ 10 000) y m pares de números
de cristales.

## Salida

La distancia de cada par, con error absoluto o relativo de como mucho
10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2
0 8 73 0 0 16
0 9 0 73 0 1000
0 146 4 0 16 0
0 15 0 4 1000 0
146 0 1 0 6 0
15 0 0 1 2 0
8 0 17 0 0 6
9 0 0 17 0 2
2
1 5
2 8
```

Salida:

```
1.4142135
1
```

## Solución

Los giros de los cristales no importan en absoluto. Uniendo cada dos
cristales que comparten una runa se obtiene el grafo de la rejilla del
cubo, n × n × n, y en un grafo de rejilla la distancia mínima entre dos
celdas es la suma de las diferencias absolutas de sus coordenadas. Eso
basta para recuperar las coordenadas.

Un cristal con el menor número de vecinos es una esquina c; sea el
origen. Una búsqueda en anchura desde ella da a cada cristal su
x + y + z. Las demás esquinas están a n − 1, 2(n − 1) o 3(n − 1) pasos,
así que las esquinas a exactamente n − 1 pasos de c son sus tres vecinas
por las aristas del cubo, digamos en (n − 1, 0, 0), (0, n − 1, 0) y
(0, 0, n − 1). Una búsqueda desde la primera da (n − 1 − x) + y + z, de
modo que x = (d(c, v) − d(cₓ, v) + n − 1)/2, y lo mismo para y y z.
Cuatro búsquedas sobre n³ ≤ 27 000 cristales los colocan todos, salvo
una simetría del cubo que conserva las distancias. Cada respuesta es
l·√(Δx² + Δy² + Δz²). `O(n³ + m)`.

En el ejemplo el cubo tiene lado 2. El cristal 1 comparte runas con los
cristales 2, 3 y 7, y el cristal 5 no comparte ninguna con él pero
tienen dos vecinos comunes, así que están en una diagonal de una cara:
√2. Los cristales 2 y 8 comparten la runa 9, así que se tocan: 1.

Trampas:

- los giros de los cristales solo distraen: lo único que cuenta es el
  grafo de contactos;
- para n = 2 todo cristal es una esquina y las esquinas junto a c son
  sus vecinos directos, que la misma regla encuentra;
- las runas llegan a 10⁹, así que hace falta una tabla hash, no un
  arreglo.

Las distancias coinciden con una implementación aceptada independiente
en sesenta cubos pequeños y en cubos de lado 30 con diez mil preguntas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1858_bfs.cpp](1858_bfs.cpp) | G++ 13.2 x64 | bfs | O(n^3 + m) | AC | 0.156 s | 6512 KB |
| [1858_bfs.go](1858_bfs.go) | Go 1.14 x64 | bfs | O(n^3 + m) | AC | 0.062 s | 17504 KB |
| [1858_bfs.java](1858_bfs.java) | Java 1.8 | bfs | O(n^3 + m) | AC | 0.281 s | 15404 KB |
| [1858_bfs.py](1858_bfs.py) | Python 3.12 x64 | bfs | O(n^3 + m) | AC | 0.250 s | 21964 KB |
| [1858_bfs.rs](1858_bfs.rs) | Rust 1.75 x64 | bfs | O(n^3 + m) | AC | 0.031 s | 11632 KB |
