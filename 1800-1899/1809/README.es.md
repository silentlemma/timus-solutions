# 1809. Chapáev y las patatas

[Timus 1809](https://acm.timus.ru/problem.aspx?space=1&num=1809) · dificultad 598 · implementation

Problema original de Dmitry Ivankov, de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuatro patatas están en celdas distintas de un tablero de 20 × 20. Una
patata puede disparar a otra si comparten fila o columna sin ninguna
patata entre ellas. Mover el menor número de patatas a celdas libres
para que cada patata pueda disparar exactamente a otra.

## Entrada

Cuatro líneas con las coordenadas x e y de las patatas, de 1 a 20.

## Salida

Las nuevas coordenadas en el mismo orden. Se acepta cualquier
respuesta óptima.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 1
2 2
4 4
4 3
```

Salida:

```
1 2
2 2
4 4
4 3
```

## Solución

Se busca una disposición donde la relación «puede disparar» divida las
cuatro patatas en dos parejas. Se comprueba la disposición tal cual. Si
no, se prueba a mover una patata a cada una de las 400 celdas. Si no,
dos movimientos siempre bastan. Si las dos patatas que se quedan se
ven entre sí, las otras dos pueden formar su propia pareja en una fila
y columnas que las fijas no usan. Si no, cada patata movida puede ir
junto a una de las fijas. Así que, para cada elección de las dos que se
mueven, basta probar las celdas junto a las fijas y esa pareja aparte.
Una prueba de estrés con 20000 disposiciones aleatorias nunca dejó
vacío este paso. `O(1)`.

En el ejemplo la segunda pareja, (4, 4) y (4, 3), ya está bien, y mover
la primera patata a (1, 2) la empareja con (2, 2).

Trampas:

- una patata entre otras dos bloquea el disparo, así que cuatro en una
  línea no forman parejas;
- una patata no puede ver a más de una, así que una pareja no debe
  compartir línea con la otra;
- las patatas movidas deben caer en celdas libres del tablero.

El verificador comprueba la disposición y compara el número de patatas
movidas con el de la respuesta esperada. Todas las soluciones lo
superan en disposiciones aleatorias, esquinas abarrotadas, una sola
línea y disposiciones casi válidas, frente a una implementación
aceptada independiente que prueba todos los pares de celdas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1809_implementation.cpp](1809_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 204 KB |
| [1809_implementation.go](1809_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1124 KB |
| [1809_implementation.java](1809_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1820 KB |
| [1809_implementation.py](1809_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.125 s | 876 KB |
| [1809_implementation.rs](1809_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.031 s | 244 KB |
