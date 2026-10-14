# 1565. El duelo a tres

[Timus 1565](https://acm.timus.ru/problem.aspx?space=1&num=1565) · dificultad 1780 · games

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

Mientras viven los tres, el turno de A termina esa fase en el acto:
A nunca falla y mata al más fuerte de B y C. Sean h la puntería del
oponente más fuerte y l la del más débil, con h > l. El fuerte siempre
dispara a A. Matar al otro oponente deja el siguiente turno a A y no
mejora la supervivencia. El débil compara disparar a A con esperar.
Si sigue A, la diferencia tiene el signo de (1 − h)(1 − l) − h; si
sigue el fuerte, tiene el signo de (1 − h)²(1 − l) − h. Dispara a A
cuando la expresión correspondiente es no negativa y al aire en otro
caso. Con l = 0 todas las acciones dan el mismo resultado y el desempate elige A.

Se leen los decimales exactamente con una escala común S: h = H/S y
l = L/S. Las comparaciones usan productos enteros:
(S − H)(S − L) ≥ H·S y (S − H)²(S − L) ≥ H·S². Así se conservan los
empates exactos sin confundir una preferencia estricta muy pequeña con
un empate. Con estas decisiones, la misma recursión mezcla aciertos y
fallos hasta el turno de A, como mucho dos disparos después. La fórmula
del duelo se evalúa mediante la razón entre la puntería menor y la mayor,
para evitar dividir por cero si ambas se redondean a cero en coma
flotante; solo las probabilidades usan coma flotante.

Aquí d es el número de cifras decimales de entrada.

Detalles a tener en cuenta:

- una tolerancia fija puede convertir una preferencia estricta en un
  empate y cambiar mucho las probabilidades ajenas;
- disparar al aire puede ser lo mejor: en el ejemplo, mientras viven
  los tres, C siempre dispara al aire y deja que A y B disparen primero;
- B o C pueden no acertar nunca o no fallar nunca, y A dispara primero a
  un B o C perfecto (pruebas 02–05);
- el siguiente tirador tras un acierto se salta al muerto, lo que decide
  quién abre el duelo que queda.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1565_games.cpp](1565_games.cpp) | G++ 13.2 x64 | games | O(d²) | AC | 0.015 s | 392 KB |
| [1565_games.go](1565_games.go) | Go 1.14 x64 | games | O(d²) | AC | 0.015 s | 1216 KB |
| [1565_games.java](1565_games.java) | Java 1.8 | games | O(d²) | AC | 0.109 s | 1856 KB |
| [1565_games.py](1565_games.py) | Python 3.12 x64 | games | O(d²) | AC | 0.078 s | 828 KB |
| [1565_games.rs](1565_games.rs) | Rust 1.75 x64 | games | O(d²) | AC | 0.015 s | 252 KB |
