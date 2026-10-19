# 1958. Ordenar con intercambios cíclicos según el valor

[Timus 1958](https://acm.timus.ru/problem.aspx?space=1&num=1958) · difficulty 3577 · constructive

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Olga Soboleva (prepared by Denis Dublennykh).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Ordenar una permutación p de 1…n mediante esta operación: elegir un valor
a, 1≤a≤n, localizar su posición actual k desde cero e intercambiar p[k]
con p[(k+a) mod n]. El argumento es un valor, no un índice. Usar como
máximo 10⁶ operaciones o declarar imposibilidad. Límites: 1 s, 64 MB.

## Entrada

Primero n, 1≤n≤500, seguido de n enteros que forman una permutación de 1…n.

## Salida

Si no se puede ordenar, `Impossible`. En otro caso, primero m, 0≤m≤10⁶,
y luego m líneas con los argumentos en orden. Vale cualquier secuencia
correcta, sin minimizar m. La construcción demuestra que toda entrada
legal es ordenable; el programa nunca imprime `Impossible`.

## Evaluación

Un comprobador ejecuta las operaciones impresas y acepta cualquier
secuencia dentro del límite que ordene la permutación.

## Ejemplos

```
5
1 3 5 2 4
```

```
3
4
3
3
```

## Solución

Usamos la última posición n−1 como búfer. Si contiene a<n, la operación a
intercambia con (n−1+a) mod n=a−1 y coloca a en su destino definitivo.
Repetimos hasta que el búfer contenga n; llamamos a esto vaciar.

En un vaciado, cada paso fija un valor nuevo que los siguientes no alteran:
otra operación b apunta a otro índice b−1. Así, tras como máximo n−1
llamadas aparece n en el búfer. Empezamos con un vaciado.

Ahora existe un sufijo correcto que incluye n. Si todo está ordenado,
terminamos. Si no, localizamos 1 y ejecutamos 1 hasta llevarlo al final:
son intercambios adyacentes hacia la derecha, sin vuelta circular.
Vaciamos otra vez y repetimos.

### Por qué crece el sufijo

Supongamos correctos los índices k…n−1 antes de una ronda, k>0. El valor 1
está antes del sufijo. Al llevarlo al final, cada valor del sufijo se
desplaza una posición a la izquierda: k+1 queda en k−1, k+2 en k, …,
n en n−2.

En el siguiente vaciado, la única forma de traer n al búfer es fijar n−1
en n−2. Antes, n−1 debe llegar al búfer fijando n−2; retrocediendo,
la cadena pasa necesariamente por k,k+1,…,n−1. Ningún valor ya fijado
durante ese vaciado vuelve a desplazarse. Se restaura el sufijo y además
se fija k en k−1. El sufijo correcto crece al menos una posición.

Cada ronda avanza y finalmente ordena. El vaciado inicial necesita a lo
sumo n−1 llamadas. Hay como máximo n−1 rondas, cada una con hasta n−1
movimientos de 1 y n−1 llamadas de vaciado. Por tanto:

m≤(n−1)+2(n−1)²=(n−1)(2n−1)≤498501<10⁶.

Con n=1 o entrada ya ordenada, se imprime cero. Cada argumento representa
una operación real, no una instrucción comprimida.

Tiempo O(n²), incluidas búsqueda de 1 y salida. Operaciones almacenadas:
O(n²) memoria; permutación de trabajo: O(n). No confundir a con k ni usar
índices desde uno en el módulo. a=n es una operación nula válida; el
vaciado nunca la necesita. Se exige 1…n, no una rotación circular.

## Notas por lenguaje

C++, Go y Rust guardan un vector/slice. Java 8 usa un array int primitivo
con capacidad demostrada, sin objetos por llamada. Python conserva
referencias enteras y escribe bloques de 4096 llamadas, evitando una
enorme lista de cadenas decimales. Rust solo usa la biblioteca estándar.
Bastan enteros ordinarios en versiones nativas. Se verifica CPython.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1958_constructive.cpp](1958_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.015 s | 1416 KB |
| [1958_constructive.go](1958_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.046 s | 7624 KB |
| [1958_constructive.java](1958_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.109 s | 9216 KB |
| [1958_constructive.py](1958_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.234 s | 6288 KB |
| [1958_constructive.rs](1958_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.078 s | 4964 KB |
