# 1853. Tecnologías láser

[Timus 1853](https://acm.timus.ru/problem.aspx?space=1&num=1853) · dificultad 6453 · geometry

Problema original de Denis Dublennykh, del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un emisor láser y su receptor están en el borde de un polígono convexo,
a distancia d a lo largo del borde, y el rayo va siempre recto de uno al
otro. Ambos se mueven por el borde a la misma velocidad constante y en
el mismo sentido hasta volver al punto de partida. El vidrio se enturbia
donde se cruzan dos pulsos consecutivos, así que el rayo dibuja una
curva: hallar la longitud total de todas las líneas dibujadas.

## Entrada

n (3 ≤ n ≤ 10 000) y los vértices en sentido antihorario, enteros de
valor absoluto hasta 10⁶; luego el entero d, mayor que el lado más largo
y como mucho la mitad del perímetro.

## Salida

La longitud total, con error absoluto o relativo de como mucho 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
-1 0
1 0
0 10
11
```

Salida:

```
22.3730148246
```

### Ejemplo 2

Entrada:

```
4
0 0
10 0
10 10
0 10
11
```

Salida:

```
56.1255583559
```

## Solución

Los pulsos consecutivos se cruzan en el punto donde el rayo en
movimiento toca su envolvente, así que el dibujo es la envolvente de la
familia de rayos. Se corta el movimiento en los instantes en que el
emisor o el receptor pasan por un vértice; hay como mucho 2n, y se
encuentran recorriendo el borde con ambos puntos a la vez. Entre dos de
esos instantes el emisor se mueve como A + t·u_A y el receptor como
B + t·u_B con las direcciones unitarias de sus lados, así que el vector
del rayo es D(t) = D₀ + tV con V = u_B − u_A, y M = D × V es constante.

El punto de contacto es E = A + λD, donde la recta no se desplaza de
lado: (u_A + λV) × D = 0 da λ = (u_A × D)/M, lineal en t. E′ va a lo
largo del rayo, así que su rapidez es |E′·D|/|D|, que resulta ser
|R(t)|/√Q(t) con Q = |D|² y R cuadrático. Escribir R = αQ + βQ′ + γ
convierte la integral en términos con √Q y ∫dt/√Q = asinh((Q′/2)/|M|)/√a,
donde a = |V|² y el discriminante de Q es −4M²; la forma con asinh evita
la cancelación del logaritmo habitual. R cambia de signo en sus
raíces, donde la curva tiene cúspides, así que cada tramo se corta
también allí.

Recorriendo en sentido antihorario, el emisor y el receptor siempre se
mueven hacia lados opuestos del rayo, así que el punto de contacto está
entre ellos, dentro del vidrio. `O(n)`.

Si d es exactamente la mitad del perímetro de un cuadrado, todo rayo
pasa por el centro, el dibujo es un solo punto y la respuesta es 0.

Trampas:

- los extremos del rayo pasan por los vértices en instantes distintos:
  hay que recorrerlos juntos en vez de buscar posiciones por distancias
  en coma flotante;
- M es positivo en un polígono convexo y vale cero solo cuando el rayo
  va a lo largo de un lado, y entonces no se dibuja nada;
- ln(2at + b + 2√(aQ)) puede perder precisión cuando 2at + b es
  negativo y grande; asinh evita esta cancelación.

Las respuestas coinciden con una implementación aceptada independiente
hasta 10⁻⁷ en doscientos polígonos aleatorios, entre ellos círculos de
9000 vértices, agujas finas y d en sus dos extremos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1853_geometry.cpp](1853_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.046 s | 312 KB |
| [1853_geometry.go](1853_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 2016 KB |
| [1853_geometry.java](1853_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.140 s | 6176 KB |
| [1853_geometry.py](1853_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.218 s | 4076 KB |
| [1853_geometry.rs](1853_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 776 KB |
