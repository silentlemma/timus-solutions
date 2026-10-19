# 1983. Área de un triángulo dentro de una bola

[Timus 1983](https://acm.timus.ru/problem.aspx?space=1&num=1983) · dificultad 1546 · geometry

Problema original de Mikhail Rubinchik, del Campeonato Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres puntos no colineales de coordenadas enteras con valor absoluto como
máximo 200 definen un triángulo relleno en el espacio tridimensional.
Hallar el área de su intersección con la bola cerrada de radio 100
centrada en el origen. Se pide el área en el plano del triángulo, no un
área proyectada ni un volumen. Límites: 0,5 segundos y 64 MB.

## Entrada

Tres líneas; cada una contiene las tres coordenadas enteras de un vértice.

## Salida

Un número real no negativo: el área de intersección.

## Evaluación

Los números se comparan con error absoluto o relativo 10⁻².

## Ejemplos

Entrada:

```
0 0 0
0 2 0
2 0 0
```

Salida:

```
2.00000
```

## Solución

Sean `p,q,r` los vértices, `n=(q−p)×(r−p)`, `N=n·n>0` y `D=n·p`. El
plano tiene ecuación `n·x=D`. Si `F=10000N−D²≤0`, no corta el interior
de la bola y el área es cero. En otro caso, la sección es un disco de
radio al cuadrado `ρ²=F/N`, centrado en la proyección del origen sobre
el plano.

Tomar el vector unitario `u=(q−p)/|q−p|`, la normal unitaria `w=n/√N` y
`v=w×u`. Cada punto `x` se transforma en `(x·u,x·v)`. El centro del
disco se transforma en cero porque es paralelo a `w`. Esta base
ortonormal conserva el área y reduce el problema a un triángulo y un
disco planos.

Para cada arista orientada `p+t e`, `0≤t≤1`, usar las coordenadas
enteras tridimensionales originales. Calcular `A=e·e`, `B=p·e`,
`C=p·p−10000` y `Δ=B²−AC`. La parte interior satisface `At²+2Bt+C<0`. Si
`Δ>0`, sus extremos son dos raíces. Calcularlas de forma estable como
`s/A` y `C/s`, con `s=−B−copysign(√Δ,B)`, y ordenarlas. Dividir la
arista en las raíces estrictamente dentro de `(0,1)`. Un subsegmento es
interior exactamente cuando el parámetro de su punto medio está
estrictamente entre las raíces. Con `Δ≤0`, todos los subsegmentos de
longitud positiva son exteriores: un punto medio tangente no hace
interior toda una arista.

Para los extremos planos `a,b` de cada parte, sumar `cross(a,b)` si es
interior y `ρ²·atan2(cross(a,b),a·b)` si es exterior. Sumar con signo
sobre el contorno, tomar el valor absoluto y dividir entre dos. Las
partes interiores aportan abanicos triangulares orientados y las
exteriores sectores circulares orientados. Los abanicos sobrantes se
cancelan y la intersección se cuenta una vez. También es la integral de
contorno de un campo continuo cuyo rotacional es uno dentro del disco y
cero fuera. Dividir en todos los cruces justifica elegir triángulo o
sector para cada parte.

En el ejemplo, todo el triángulo rectángulo está dentro de la bola.
Ambos catetos miden 2 y el área es `2·2/2=2`.

Siempre hay tres aristas y como máximo dos raíces por arista: tiempo y
memoria `O(1)`. La normal, el residuo `F` y los discriminantes se
calculan como enteros antes de convertir a coma flotante. Los límites
permiten enteros de 64 bits con signo. Raíces, proyecciones y ángulos
usan doble precisión.

Trampas:

- Los tres vértices pueden estar fuera y el triángulo contener todo el disco.
- Conservar los signos hasta el valor absoluto final e incluir la arista
  de cierre.
- La tangencia del plano o de una arista no crea un tramo interior de
  longitud positiva.
- Calcular `F` y `Δ` como enteros para evitar que la cancelación cambie
  los cruces.
- Usar `atan2` para conservar la orientación del ángulo.
- Se pide el área real en el plano, no su proyección sobre un plano coordenado.

## Notas por lenguaje

Los cinco programas usan el mismo algoritmo de tamaño constante. C++,
Go, Java y Rust emplean enteros de 64 bits con signo para las decisiones
geométricas y doble precisión para áreas; Python usa enteros exactos y
aritmética flotante estándar. Java fija la configuración regional para
imprimir el punto decimal.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1983_geometry.cpp](1983_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 452 KB |
| [1983_geometry.go](1983_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1224 KB |
| [1983_geometry.java](1983_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1936 KB |
| [1983_geometry.py](1983_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 924 KB |
| [1983_geometry.rs](1983_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 260 KB |
