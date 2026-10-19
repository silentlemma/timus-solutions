# 1911. Energía mínima para dejar pasar una barrera

[Timus 1911](https://acm.timus.ru/problem.aspx?space=1&num=1911) · difficulty 4162 · math

Problema original de Denis Dublennykh, NEERC 2012, Eastern subregional contest.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un carro de longitud l avanza por un pasillo a velocidad v. Una barrera
de grosor L lo sigue a velocidad V>v; inicialmente su frente queda a D
de la parte trasera del carro. Elige exactamente un desvío de los disponibles.
El carro mantiene v hasta entrar por completo y entonces desacelera
uniformemente a razón b≥a. Aumentar a hasta b cuesta s(b−a) una vez por
ese desvío. Cuando la barrera alcanza el carro, un escudo puede mantenerla
pegada a su parte trasera pagando k por segundo. No hace falta escudo cuando
el carro está totalmente dentro. Toda la barrera debe pasar la salida
antes de que el frente del carro vuelva al pasillo. Se permite parar,
esperar y continuar a pie. Minimiza la energía total. Límites: 1 segundo, 64 MB.

## Entrada

Ocho enteros v,l,V,L,D,a,k,s. Los seis primeros están estrictamente entre
0 y 100 000, v<V, y 0≤k,s≤10 000. Después n, 1≤n≤1000, y n pares xᵢ,yᵢ,
distancias a entrada y salida desde el frente inicial del carro. Cumplen
0<xᵢ, xᵢ+l<yᵢ, yᵢ<xᵢ₊₁ para desvíos consecutivos, y yᵢ<100 000.
Longitudes en metros, velocidades en m/s y desaceleración en m/s²;
k es energía por segundo y s energía por unidad de desaceleración extra.

## Salida

Una energía mínima con error absoluto o relativo como máximo 10⁻⁵.

## Evaluación

Un token numérico finito, con tolerancia absoluta/relativa 10⁻⁵.

## Ejemplos

```
1 1 2 1 1 100 1 1234
1
100 102
```

```
100.000
```

## Solución

Evalúa cada desvío (x,y). La entrada completa sucede en τ=(x+l)/v;
sin escudo, la barrera alcanza la parte trasera en t_c=D/(V−v).
El coste inevitable del escudo es k·max(0,τ−t_c). Suéltala inmediatamente
al quedar oculto: retenerla más tiempo cuesta energía y retrasa su paso.

La separación restante al entrar es g=max(D−(V−v)τ,0). El frente de la
barrera está en x−g y su parte trasera en x−g−L; necesita
T=(y−x+L+g)/V para despejar la salida. Al frente del carro le queda
d=y−x−l>0 de recorrido completamente dentro del desvío.

Con desaceleración b, el desplazamiento antes de parar es vt−bt²/2.
Mientras se alcanza la salida en movimiento, aumentar b eleva el tiempo
desde d/v hasta 2d/v. El umbral para detenerse es b_stop=v²/(2d),
y detenerse permite esperar más. La desaceleración mínima necesaria es
cero si T≤d/v, b_stop si T≥2d/v, y 2(vT−d)/T² en el intervalo intermedio.
Esta última fórmula resuelve d=vT−bT²/2; los límites aseguran velocidad
no negativa al llegar. La desaceleración natural puede bastar, de modo
que el coste extra es s·max(0,b_required−a).

El tiempo de escudo hasta la entrada completa es obligatorio; como los
precios son no negativos, la menor desaceleración suficiente es óptima.
El mínimo de los costes totales de todos los desvíos da el óptimo global:
los desvíos ignorados no cambian la velocidad en el pasillo principal.

Evita restar cantidades flotantes próximas antes de multiplicarlas por
los precios. Escribe T=N/(vV) y calcula expresiones racionales exactas:

```text
W = V-v
H = (x+l)W-Dv
N = v(y-x+L)+max(0,-H)
shield cost = k*max(0,H)/(vW)

if N >= 2dV:  Bnum = v²,                 Bden = 2d
elif N <= dV: Bnum = 0,                  Bden = 1
else:         Bnum = 2v²V(N-dV),          Bden = N²

extra = max(0, Bnum-a*Bden)
branch cost = shield cost + s*extra/Bden
```

Las comparaciones y la resta en `extra` son enteras. Solo los dos cocientes
finales no negativos se convierten a coma flotante, preservando los ceros
exactos. N≤3·10¹⁰, los productos de frenado son menores que 10²⁶ y los
numeradores de energía menores que 10³⁰: caben en 128 bits con signo.
Todos los denominadores son positivos.

Tiempo O(n), espacio O(n) para los desvíos y O(1) adicional. En el ejemplo
la desaceleración natural ya detiene el carro; solo se pagan 100 segundos
de escudo.

## Notas por lenguaje

C++ y Rust usan enteros con signo de 128 bits. Go 1.14 y Java 8 usan
64 bits para términos acotados y math/big o BigInteger para productos
grandes. Go convierte un cociente exacto big.Rat; Java convierte los
numeradores y denominadores positivos por separado. Python 3.12 usa enteros
exactos. C++ calcula los cocientes finales en long double y los demás
en doble precisión; todos imprimen doce decimales. Incluye precios cero,
umbrales exactos y velocidades v,V muy próximas.

Las respuestas coinciden con una simulación paso a paso del movimiento
con 90 dígitos, que busca el frenado por bisección en lugar de usar la
fórmula, en 628 casos; 28 de ellos se construyen alrededor de umbrales
exactos y precios nulos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1911_math.cpp](1911_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.031 s | 528 KB |
| [1911_math.go](1911_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1472 KB |
| [1911_math.java](1911_math.java) | Java 1.8 | math | O(n) | AC | 0.140 s | 3760 KB |
| [1911_math.py](1911_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 612 KB |
| [1911_math.rs](1911_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.046 s | 324 KB |
