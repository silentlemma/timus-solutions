# 1299. Psilonianos

[Timus 1299](https://acm.timus.ru/problem.aspx?space=1&num=1299) · dificultad 1525 · implementation

Problema original de Pavel Egorov, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que simular una decisión de un robot de combate. Tiene energía E y
munición W, uno de cuatro comportamientos, y ve M enemigos con energía
media MP, el más peligroso en un ángulo a. Responde con una orden:

- `LEFT X`, `RIGHT X`, `FRONT X`, `BACKWARD X` con X = min(100, E);
- `FIRE P` con P = min(20, W);
- `STOP`.

Los comportamientos:

- guardia (G): sin enemigos, `STOP`; si |a| < 5, dispara; si no, gira
  hacia el objetivo, a la izquierda si a ≥ 5 y a la derecha si a ≤ −5;
- defensa (D): si 20 · M ≥ W, retrocede disparando; si no, actúa como
  guardia;
- ataque (A), con N robots propios de energía media NP: si
  N · NP > 3 · M · MP, avanza disparando; si no, retrocede disparando;
- patrulla (P), con la desviación d respecto al siguiente punto de la
  ruta: con enemigos, defensa; si no, se dirige al punto con el frente
  o con la parte trasera, lo que pida el giro menor, y gira si ese
  ángulo pasa de 20 o se mueve en caso contrario.

Retroceder disparando significa moverse hacia atrás cuando no hay
enemigos o el objetivo está desviado al menos 5 grados, y disparar en
otro caso. Avanzar disparando es igual con `FRONT` y 10 grados.

Los ángulos van de −179 a 180; los demás números, de 0 a 1000.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

E y W; la letra del comportamiento; M, MP y a; para un ataque además N
y NP, para una patrulla además d.

## Salida

Una orden.

## Ejemplos

### Ejemplo 1

Entrada:

```
100 100
P
0 0 0
-100
```

Salida:

```
LEFT 100
```

### Ejemplo 2

Entrada:

```
10 1000
A
1 10 30
100 1000
```

Salida:

```
FRONT 10
```

### Ejemplo 3

Entrada:

```
10 1000
G
1 10 4
```

Salida:

```
FIRE 20
```

## Solución

Las reglas se aplican tal como se enumeran, solo con enteros. Tres
puntos del enunciado necesitan una interpretación:

- Los ángulos positivos quedan a la izquierda. La guardia gira a la
  izquierda para a ≥ 5, y el primer ejemplo coincide: el punto está 100
  grados a la derecha, así que la parte trasera está 80 grados a la
  izquierda, y el robot gira `LEFT`.
- «Desviado al menos 5 (o 10) grados» al retroceder o avanzar se lee
  como |a| ≥ 5 (o 10), el mismo ángulo absoluto que usa la guardia. El
  robot solo dispara cuando apunta.
- En la patrulla la parte trasera apunta según d − 180 (o d + 180 si
  d ≤ 0). Cuando frente y parte trasera necesitan el mismo giro, en
  d = ±90, se mantiene el frente, así que d = 90 da `LEFT` (prueba 19).

`O(1)`.

Detalles a tener en cuenta:

- los umbrales son exactos: con a = 5 ya gira (prueba 05), y con una
  desviación de 20 todavía avanza (pruebas 13 y 16);
- con el triple exacto de la fuerza enemiga se retrocede en ataque:
  la condición es estricta (prueba 10);
- las cantidades se limitan a lo que tiene el robot: `FIRE 5` con 5
  unidades restantes (prueba 10), `BACKWARD 0` sin energía (prueba 16);
- una patrulla que encuentra un enemigo sigue las reglas de defensa, no
  la ruta (prueba 18).

Las respuestas se compararon con una implementación independiente de la
misma interpretación en 400 entradas aleatorias, con ángulos cerca de
cada umbral.

## Notas por lenguaje

- Todos los lenguajes escriben las reglas como pequeñas funciones que
  se llaman entre sí: la patrulla llama a la defensa, y esta a la
  guardia o a la retirada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1299_implementation.cpp](1299_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 200 KB |
| [1299_implementation.go](1299_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1100 KB |
| [1299_implementation.java](1299_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1684 KB |
| [1299_implementation.py](1299_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 676 KB |
| [1299_implementation.rs](1299_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 236 KB |
