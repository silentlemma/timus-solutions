# 1367. Alto secreto

[Timus 1367](https://acm.timus.ru/problem.aspx?space=1&num=1367) · dificultad 2992 · dsu

Problema original de Pavel Egorov, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una foto de a lo sumo 1000 × 1000 celdas muestra tabiques: `-` es un
tabique horizontal por la mitad de su celda, `|` uno vertical, `+` una
cruz de ambos, y `.` es terreno libre. Un secreto `#` es una cruz con un
objeto en el centro al que se llega desde cualquiera de los cuatro
lados. Los agentes van a cualquier parte salvo a través de tabiques y
nunca salen de la foto. Dos de los a lo sumo 100 secretos están unidos
si un agente puede ir de uno a otro. Hay que imprimir la matriz de
adyacencia, con los secretos numerados de arriba abajo y, dentro de una
fila, de derecha a izquierda.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

H líneas de W caracteres.

## Salida

La matriz de 0 y 1, una fila por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
+------+
|#+-+--|
-++#|..|
##..|#.|
-+--+--+
```

Salida:

```
10100
01010
10100
01011
00011
```

## Solución

Cada tabique va por una línea media de su celda, así que los cuatro
cuartos de celda alrededor de un vértice de la cuadrícula siempre se
tocan: los sitios donde puede estar un agente son los vértices de la
cuadrícula, (H + 1) × (W + 1). Cada celda une algunos de sus cuatro
vértices:

- `.` une los cuatro;
- `-` une los dos de arriba y los dos de abajo;
- `|` une los dos de la izquierda y los dos de la derecha;
- `+` y `#` no unen ninguno.

Una estructura de conjuntos disjuntos sobre los vértices da las zonas
libres. Un secreto toca las zonas de sus cuatro vértices. El ejemplo
muestra que la relación no es transitiva: el secreto 4 está unido al 2 y
al 5, pero el 2 y el 5 no. Así que un agente no puede atravesar un
secreto de un lado a otro, y dos secretos están unidos justo cuando
algún vértice de uno está en la misma zona que algún vértice del otro.
`O(H · W · α + K²)` para K secretos.

Detalles a tener en cuenta:

- dentro de una fila el orden es de derecha a izquierda, cosa que solo
  aclara el ejemplo;
- un tabique que acaba en el borde de una celda no toca a uno que cruza
  la mitad de la celda siguiente: por el hueco pasan los agentes
  (prueba 02), y una cruz lo cierra (prueba 03);
- un secreto también es una cruz, así que corta el paso entre sus
  vecinos (prueba 07);
- cada secreto está unido a sí mismo;
- sin secretos la salida está vacía (prueba 09).

Los seis dibujos pequeños del enunciado son las pruebas 02 a 07, y el
modelo de vértices se comparó en 1 500 fotos aleatorias de hasta 7 × 7
con una búsqueda sobre los cuatro cuartos de cada celda.

## Notas por lenguaje

- Python necesita PyPy en las fotos más grandes: unos 0,25 s allí,
  frente a más de un segundo con CPython.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1367_dsu.cpp](1367_dsu.cpp) | G++ 13.2 x64 | dsu | O(H·W·α + K²) | AC | 0.140 s | 4976 KB |
| [1367_dsu.go](1367_dsu.go) | Go 1.14 x64 | dsu | O(H·W·α + K²) | AC | 0.062 s | 10736 KB |
| [1367_dsu.java](1367_dsu.java) | Java 1.8 | dsu | O(H·W·α + K²) | AC | 0.140 s | 6380 KB |
| [1367_dsu.py](1367_dsu.py) | PyPy 3.10 x64 | dsu | O(H·W·α + K²) | AC | 0.453 s | 14008 KB |
| [1367_dsu.rs](1367_dsu.rs) | Rust 1.75 x64 | dsu | O(H·W·α + K²) | AC | 0.015 s | 9948 KB |
