# 2100. Contar los invitados y evitar el trece

[Timus 2100](https://acm.timus.ru/problem.aspx?space=1&num=2100) · dificultad 29 · implementation

Problema original de Alexey Danilyuk, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una pareja invita a n amigos; una respuesta `name+one` significa que el
amigo viene con su pareja. Todos se sientan a una mesa con los novios, y
si se sentaran exactamente 13, se añade un maniquí. Cada asiento cuesta
100 dólares. Imprimir el coste de la cena. Los límites son 1 segundo y
64 MB.

## Entrada

n ≤ 20 y después las n respuestas, cada una un nombre de letras latinas,
quizá con `+one`.

## Salida

El coste en dólares.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
Ted+one
Robin
Barney
```

Salida:

```
600
```

### Ejemplo 2

Entrada:

```
6
Alice+one
Bob+one
carl
Debora+one
Enrique+one
FRED+one
```

Salida:

```
1400
```

## Solución

Se empieza por los dos anfitriones, se suma 2 por cada respuesta que
termina en `+one` y 1 por las demás, se convierte 13 en 14 y se
multiplica por 100.

En el segundo ejemplo se sentarían 2 + 5 · 2 + 1 = 13 personas, así que
se les une un maniquí: 1400.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2100_implementation.cpp](2100_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 404 KB |
| [2100_implementation.go](2100_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1076 KB |
| [2100_implementation.java](2100_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.156 s | 1596 KB |
| [2100_implementation.py](2100_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 420 KB |
| [2100_implementation.rs](2100_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 236 KB |
