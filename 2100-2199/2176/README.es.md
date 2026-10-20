# 2176. Sumas de números distintos cuya forma en base 3 se esconde en la binaria

[Timus 2176](https://acm.timus.ru/problem.aspx?space=1&num=2176) · dificultad 1043 · dp, meet_in_middle

Problema original de Konstantin Rychkov, del Concurso Escolar de Programación de los Urales 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número es bonito cuando su notación en base 3 es una subcadena de su
notación binaria, como 12 = 110₃ = 1100₂. Para cada uno de N números
xᵢ, decir si es suma de números bonitos distintos. Los límites son
1 segundo y 256 MB.

## Entrada

N, 1 ≤ N ≤ 1000, y luego x₁ … x_N con 1 ≤ xᵢ ≤ 10⁹.

## Salida

YES o NO para cada número.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
1 2 3 8 9 10
```

Salida:

```
YES
NO
NO
NO
YES
YES
```

### Ejemplo 2

Entrada:

```
4
854789369 694089367 789789379 795089367
```

Salida:

```
NO
YES
NO
YES
```

## Solución

Una cadena binaria solo tiene los dígitos 0 y 1, así que un número
bonito no tiene el dígito 2 en base 3. Esos números hasta 10⁹ tienen a
lo sumo 19 dígitos ternarios, así que hay menos de 2¹⁹, y se generan
añadiendo 0 o 1 a un prefijo ternario mientras los mismos dígitos,
leídos como patrón binario, se buscan en la forma binaria. Solo 40 son
bonitos, y el mayor es 133991292.

La pregunta es entonces una suma de subconjuntos sobre 40 números fijos,
divididos en dos partes.

- Los 31 menores suman 48106098, así que un bitset de ese tamaño marca
  todas las sumas de números pequeños distintos; cada número desplaza el
  bitset y se combina con OR.
- Los 9 restantes dan solo 2⁹ sumas de subconjuntos, que se listan y
  ordenan.

Para una consulta x se prueban las sumas h de la parte grande con
x − 48106098 ≤ h ≤ x, y la respuesta es YES si algún x − h está marcado
en el bitset.

En el primer ejemplo 9 = 100₃ = 1001₂ y 10 = 101₃ = 1010₂ son bonitos,
mientras que 2 y 3 no lo son ni se pueden formar con 1.

Construir el bitset cuesta 31 pasadas sobre 48 millones de bits, y cada
consulta prueba a lo sumo 512 sumas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2176_dp_meet_in_middle.cpp](2176_dp_meet_in_middle.cpp) | G++ 13.2 x64 | dp, meet_in_middle | O(S / w + N · 2^9) | AC | 0.046 s | 5616 KB |
| [2176_dp_meet_in_middle.go](2176_dp_meet_in_middle.go) | Go 1.14 x64 | dp, meet_in_middle | O(S / w + N · 2^9) | AC | 0.046 s | 7528 KB |
| [2176_dp_meet_in_middle.java](2176_dp_meet_in_middle.java) | Java 1.8 | dp, meet_in_middle | O(S / w + N · 2^9) | AC | 0.125 s | 6340 KB |
| [2176_dp_meet_in_middle.py](2176_dp_meet_in_middle.py) | Python 3.12 x64 | dp, meet_in_middle | O(S / w + N · 2^9) | AC | 0.562 s | 18964 KB |
| [2176_dp_meet_in_middle.rs](2176_dp_meet_in_middle.rs) | Rust 1.75 x64 | dp, meet_in_middle | O(S / w + N · 2^9) | AC | 0.046 s | 5772 KB |
