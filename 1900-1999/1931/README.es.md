# 1931. Quién participa en más comparaciones

[Timus 1931](https://acm.timus.ru/problem.aspx?space=1&num=1931) · difficulty 168 · simulation

Original problem from Open Ural FU Championship 2012 | by Olga Soboleva.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Personas en orden fijo tienen puntuaciones positivas distintas. Al inicio,
la persona 1 es candidata actual. Comparar cada siguiente con la actual;
reemplazarla exactamente cuando la nueva puntuación sea menor. Ambas
participan en la comparación, también cuando provoca el reemplazo.
Imprimir una persona que participe en más comparaciones; cualquier máximo
empatado sirve. Límites: 1 segundo, 64 MB.

## Entrada

Primero n, 1≤n≤100000. Luego n enteros distintos a1..an,
1≤ai≤1000000000. Los identificadores 1..n siguen el orden de entrada.

## Salida

Un identificador con máximo número de comparaciones. Para n=1 imprimir 1:
la única persona tiene cero comparaciones.

## Evaluación

Cualquier respuesta válida. checker.py exige un único entero entre 1 y n,
simula literalmente el proceso con un contador por persona y comprueba
que el elegido sea máximo. El índice guardado es solo uno de ellos;
se acepta cualquier otro ganador empatado.

## Ejemplos

```
6
2 5 3 4 1 9
```

```
1
```

## Solución

Guardar puntuación, índice y contador de la candidatura actual, además
del mayor contador e índice registrados. El contador actual empieza en
cero. Para cada nueva persona, incrementar primero el contador de la
ANTERIOR candidata y actualizar el mejor si es mayor. Después comparar
puntuaciones. Si la nueva es menor, reemplazar y fijar su contador en
1: ya participó en la comparación que la seleccionó. Si no reemplaza,
su cuenta total de por vida es exactamente 1.

La candidatura actual siempre es el mínimo del prefijo procesado y su
contador incluye todas sus comparaciones, incluidas entrada y derrota
cuando existan. Quien no llega a candidato no supera el máximo: su única
comparación tiene como pareja a alguien cuyo contador recién incrementado
ya es al menos 1. Lo mismo cubre la comparación inicial del nuevo candidato.
Cada aumento posterior ocurre durante su candidatura y se comprueba
explícitamente. Quien fue reemplazado no vuelve y su total queda fijo.
Por inducción, el resultado registrado alcanza el máximo global.
El identificador inicial 1 cubre también la ausencia de comparaciones.

O(n) tiempo y O(1) contadores de trabajo. Los programas almacenan entrada
como arreglo, vector o tokens, por lo que el espacio total es O(n).

La menor puntuación no implica más comparaciones. Contar la derrota de
la candidatura anterior ANTES del reemplazo. La nueva empieza en 1, no 0.
Devolver identificador, no cantidad. No rechazar una respuesta distinta
solo por empate: para [3,2,1,4] sirven tanto 2 como 3.

## Notas por lenguaje

Las puntuaciones caben en enteros con signo de 32 bits y las cuentas
son ≤n−1≤99999. Solo se comparan puntuaciones. Java usa lectura entera
con búfer; C++, Go y Rust guardan arreglos primitivos; Python recorre
tokens mediante un generador. El algoritmo entregado no necesita
contadores individuales, pero el comprobador independiente sí los usa.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1931_simulation.cpp](1931_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 812 KB |
| [1931_simulation.go](1931_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.093 s | 3468 KB |
| [1931_simulation.java](1931_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.109 s | 828 KB |
| [1931_simulation.py](1931_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.125 s | 8392 KB |
| [1931_simulation.rs](1931_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 2136 KB |
