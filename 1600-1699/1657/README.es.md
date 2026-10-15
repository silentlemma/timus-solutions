# 1657. Serpiente cubo

[Timus 1657](https://acm.timus.ru/problem.aspx?space=1&num=1657) · dificultad 1522 · backtracking

Problema original de Stanislav Vasilyev (preparado por Sergey Pupyrev), del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una serpiente rompecabezas es una cuerda de 27 cubitos. En un cubito
recto (`F`) la cuerda atraviesa caras opuestas y en uno de giro (`T`)
caras contiguas; los cubitos de los extremos cuentan como rectos. Hay que
plegar la serpiente en un cubo de 3 × 3 × 3 e imprimir la posición de
cada cubito respecto al anterior, o decir que no se puede.

## Entrada

27 letras `F` y `T`.

## Salida

26 letras de `RLFBUD` (derecha, izquierda, delante, detrás, arriba,
abajo), o `IMPOSSIBLE`. Se acepta cualquier plegado válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
FFTTTFTTFTTTFTFTTTTFTFTFTFF
```

Salida:

```
UURDFFRBBUFLLDDRBRFFLLUURR
```

### Ejemplo 2

Entrada:

```
FFTFTFTFTTTTFFFTTTFTTFTTTFF
```

Salida:

```
IMPOSSIBLE
```

## Solución

Plegar es recorrer las 27 casillas del cubo: tras un cubito recto el
siguiente paso mantiene la dirección y tras uno de giro toma una de las
cuatro direcciones transversales. Una búsqueda en profundidad las prueba
por turno, sin entrar en casillas ocupadas, y abandona una rama en
cuanto las casillas libres se parten en más de un trozo, porque el resto
de la serpiente no podría recorrerlas todas.

Dos observaciones hacen la búsqueda lo bastante pequeña para Python. Las
casillas se colorean como un tablero, 14 de un color y 13 del otro, y la
serpiente alterna colores, así que debe empezar en el color mayor: una
esquina o el centro de una cara. Y las simetrías del cubo hacen iguales
todas las esquinas y todos los primeros pasos desde una esquina,
mientras que desde el centro de una cara solo hay dos clases de paso,
hacia el centro del cubo o a lo largo de la cara. Así la búsqueda empieza
con solo tres primeros movimientos.

Detalles a tener en cuenta:

- la primera y la última letra son `F` por garantía de la entrada; el
  código no las consulta;
- una serpiente toda recta es una barra de 27 y nunca se pliega
  (prueba 03);
- hay muchos plegados, así que un verificador reproduce los movimientos.

Las respuestas coinciden con una implementación aceptada independiente
en Yes o No, y pasan el verificador, en 120 serpientes, incluidas
aleatorias y serpientes de plegados aleatorios con un cubito cambiado.

Complejidad: `O(C * 4^C)` para C = 27 celdas, con a lo sumo cuatro
direcciones tras cada cubo de giro.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1657_backtracking.cpp](1657_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(C * 4^C) | AC | 0.046 s | 372 KB |
| [1657_backtracking.go](1657_backtracking.go) | Go 1.14 x64 | backtracking | O(C * 4^C) | AC | 0.046 s | 5852 KB |
| [1657_backtracking.java](1657_backtracking.java) | Java 1.8 | backtracking | O(C * 4^C) | AC | 0.125 s | 6092 KB |
| [1657_backtracking.py](1657_backtracking.py) | Python 3.12 x64 | backtracking | O(C * 4^C) | AC | 0.796 s | 776 KB |
| [1657_backtracking.rs](1657_backtracking.rs) | Rust 1.75 x64 | backtracking | O(C * 4^C) | AC | 0.062 s | 220 KB |
