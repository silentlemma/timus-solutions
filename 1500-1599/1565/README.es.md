# 1565. El duelo a tres

[Timus 1565](https://acm.timus.ru/problem.aspx?space=1&num=1565) · dificultad 1785 · games

Problema original de Sergey Pupyrev, del XII Campeonato de Programación de la Universidad Estatal de los Urales, 6 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres duelistas A, B y C aciertan con probabilidades 1, b y c (b ≠ c), y
un acierto mata. Un sorteo justo fija el orden, y disparan por turnos en
ese orden, saltándose a los muertos, hasta que solo queda uno; cada
disparo puede ir a cualquiera de los rivales o al aire. A siempre
dispara al rival vivo más certero. B y C eligen el disparo que les da
más probabilidad de sobrevivir y, en caso de empate, disparan al rival
más fuerte. Hay que imprimir las probabilidades de sobrevivir de A, B y
C con al menos cinco cifras tras el punto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las tres punterías.

## Salida

Las tres probabilidades en una línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
1.0 0.8 0.5
```

Salida:

```
0.30000 0.17778 0.52222
```

## Solución

Cada uno de los 6 órdenes se resuelve por separado y se promedian los
resultados. Cuando alguien muere quedan dos que disparan por turnos; si
el primero en disparar acierta con p y el otro con q, el primero gana
con

p + (1 − p)(1 − q)·p + … = p / (p + q − p·q).

Mientras viven los tres, el turno de A termina esa fase en el acto, ya
que A nunca falla y mata al más fuerte de B y C. Así que desde cualquier
turno la fase dura como mucho dos disparos más, y las probabilidades
salen por recursión sobre los turnos: quien dispara compara disparar a
cada rival (acierto con su puntería, y luego el duelo que queda, que
abre el siguiente vivo; fallo, y luego el turno siguiente) con disparar
al aire (el turno siguiente), y se queda con su mejor probabilidad. Los
empates se resuelven como dice el enunciado, después por A, B, C y el
aire, con una tolerancia de 10⁻¹². Todo tarda tiempo constante. Los
resultados coinciden con un programa independiente en unas 420 entradas.

Detalles a tener en cuenta:

- disparar al aire puede ser lo mejor: en el ejemplo, mientras viven
  los tres, C siempre dispara al aire y deja que A y B disparen primero;
- B o C pueden no acertar nunca o no fallar nunca, y A dispara primero a
  un B o C perfecto (pruebas 02–05);
- el siguiente tirador tras un acierto se salta al muerto, lo que decide
  quién abre el duelo que queda.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1565_games.cpp](1565_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 204 KB |
| [1565_games.go](1565_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.015 s | 1128 KB |
| [1565_games.java](1565_games.java) | Java 1.8 | games | O(1) | AC | 0.109 s | 2012 KB |
| [1565_games.py](1565_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.078 s | 724 KB |
| [1565_games.rs](1565_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.015 s | 256 KB |
