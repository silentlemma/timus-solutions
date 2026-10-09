# 1093. ¿Atraviesa un dardo en caída una diana redonda en el espacio?

[Timus 1093](https://acm.timus.ru/problem.aspx?space=1&num=1093) · dificultad 1996 · geometry

Problema original de Alexander Klepinin, del USU Open Collegiate Programming Contest, marzo de 2001, Senior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La diana es un disco de centro `C`, radio `R` y vector normal `N`. Un
dardo parte de `S` con velocidad `V` (con parte horizontal no nula) y se
mueve como `S + V·t − (g/2)·t²·ẑ` con `g = 10`. Empieza fuera de la
diana. Imprime `HIT` si el dardo pasa alguna vez estrictamente por dentro
del disco, por cualquier lado, y `MISSED` si no. Los 13 números valen
como mucho 500 en valor absoluto y tienen como mucho cuatro decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`Cx Cy Cz Nx Ny Nz R` y luego `Sx Sy Sz Vx Vy Vz`.

## Salida

`HIT` o `MISSED`.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
47 0 -72 1 0 1 4.25
0 0 0 10 0 10
```

Salida:

```
HIT
```

## Solución

Sea `D = S − C`. La distancia del dardo al plano, multiplicada por `|N|`,
es `N·(D + V t) − 5 Nz t²`, un trinomio `a t² + 2h t + c` con
`a = −5 Nz`, `h = N·V / 2` y `c = N·D`. El dardo solo puede tocar el disco
en una raíz `t ≥ 0`, y allí se comprueba si el cuadrado de la distancia
al centro menos `R²`, `Q(t) = |D + V t − 5t² ẑ|² − R²`, es negativo.

- `a ≠ 0`: hasta dos raíces `t = (−h ± √(h² − ac)) / a`; la parábola
  puede cruzar el plano dos veces, y cualquiera de los cruces puede ser
  el acierto.
- `a = 0`, `h ≠ 0` (un plano vertical): una raíz `t = −c / 2h`.
- `a = h = 0`: la trayectoria es paralela al plano o está en él. En ambos
  casos el dardo nunca atraviesa el disco desde un lado, así que falla:
  deslizarse dentro del plano de la diana no es un acierto.

`O(1)`.

Detalles a tener en cuenta:

- estrictamente dentro: un dardo justo en el borde falla, así que la
  comparación usa una pequeña tolerancia negativa;
- solo cuentan las raíces con `t ≥ 0`, y hay que probar las dos, porque el
  primer cruce puede pasar junto al disco y el segundo a través de él;
- el discriminante puede salir un poco negativo por redondeo cuando la
  cima del vuelo apenas roza el plano, así que se compara con una
  pequeña tolerancia, y una raíz un pelo por debajo de cero sigue
  contando como `t = 0`;
- `N` no está normalizado, y no importa, porque solo se usan el signo y
  las raíces de la ecuación del plano.

Las respuestas se comprobaron con un cálculo exacto con fracciones: en
una raíz del trinomio, `Q` se reduce a una forma lineal en `t`, y su signo
en `(−h ± √d) / a` se decide sin redondeos. Así se compararon cientos de
lanzamientos aleatorios apuntados a menos de una diezmilésima del borde.
Una versión anterior contaba como acierto una trayectoria contenida en el
plano que cruzaba el disco; Timus la rechazó en la prueba 56, así que
ahora esa trayectoria es un fallo.

## Notas por lenguaje

- Rust desestructura los trece números con un patrón de corte.
- Java lee los números con `Locale.US`, así que el punto decimal se acepta
  sea cual sea la configuración regional del sistema.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1093_geometry.cpp](1093_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 448 KB |
| [1093_geometry.go](1093_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB |
| [1093_geometry.java](1093_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1844 KB |
| [1093_geometry.py](1093_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 548 KB |
| [1093_geometry.rs](1093_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 228 KB |
