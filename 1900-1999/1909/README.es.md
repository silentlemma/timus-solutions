# 1909. Primer contacto sin raíces cuadradas

[Timus 1909](https://acm.timus.ru/problem.aspx?space=1&num=1909) · difficulty 3963 · geometry

Problema original de Pavel Atnashev, preparado por Daniil Ayzenshteyn, Ural Championship 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos puntos distintos A,B se mueven con la misma velocidad constante no nula v.
Su segmento de unión puede tocar una esfera sólida fija de centro C y radio
R>0. Inicialmente todo el segmento está libre. En su primer contacto con
la esfera, ambos puntos se detienen inmediatamente. Determina si el contacto
incluye un extremo, ocurre estrictamente dentro del segmento o nunca sucede.
La tangencia cuenta; un empate con contacto de extremo es una colisión.
Límites: 1 segundo y 64 MB.

## Entrada

Cuatro líneas: Cx Cy Cz R; Ax Ay Az; Bx By Bz; vx vy vz.
Los 13 valores son enteros de valor absoluto como máximo 100 000.
R>0, A≠B y v≠0. El segmento inicial completo, incluidos sus extremos,
no intersecta ni toca la esfera.

## Salida

`Crash` si hay contacto de extremo, `Warning` si el primer contacto está
estrictamente dentro del segmento, o `False alarm` si no hay contacto.
Una colisión posterior sobre las trayectorias originales no ocurre si
un contacto interior anterior ya detuvo ambos puntos.

## Evaluación

El nombre exacto distingue mayúsculas y se compara por tokens.

## Ejemplos

```
0 0 0 1
2 0 0
3 0 0
-1 0 0
```

```
Crash
```

```
0 0 0 1
2 0 0
0 2 0
-1 -1 0
```

```
Warning
```

```
0 0 0 1
2 0 0
3 -1 0
1 1 0
```

```
False alarm
```

## Solución

Traslada el centro de la esfera al origen. Usa productos escalar y vectorial:

```text
w0 = A-C, w1 = B-C, u = w1-w0, U = dot(u,u)
n = cross(u,v), j = cross(u,w0)
a = dot(n,n), b = dot(j,n), c = dot(j,j)-R²U
q(t) = at²+2bt+c
K = R²a-dot(w0,n)²
```

La distancia cuadrada del origen a la recta soporte móvil menos R² es q(t)/U.
Un primer contacto interior exige que la recta entre desde fuera: a>0,c>0,b<0
y discriminante no negativo. Si la recta ya intersecta la esfera al inicio
pero el segmento está libre, el primer contacto del segmento solo puede
ser de extremo. Un primer contacto interior en la salida posterior de la
recta implicaría una intersección anterior por continuidad. Con a=0, el
movimiento sigue la recta y el primer contacto también es de extremo.

No calcules D=b²−ac directamente en 128 bits. La identidad de Lagrange da
D=U·K: K determina su signo y detecta la raíz doble. Si a>0,c>0,b<0,K≥0,
el primer contacto de la recta ocurre en t₀=(−b−√D)/a>0. Su punto más
cercano es estrictamente interior exactamente cuando u·(w0+vt₀)<0 y
u·(w1+vt₀)>0. Entonces devuelve `Warning`: ningún extremo puede tocar
antes que la recta que lo contiene.

Para obtener el signo de x+yt₀ sin evaluar raíces, usa x=u·w, y=u·v para
cada extremo w. Si y=0, basta sign(x). Si no, escribe z=−x/y=num/den con
den>0 y calcula H=a·num+b·den. H compara z con el vértice −b/a.
Si H≥0, sign(t₀−z)=−1, salvo H=0,K=0 que produce cero. Si H<0, z está
a la izquierda del vértice y sign(t₀−z)=sign(q(z)). En z el extremo
es perpendicular a u, por lo que q(z)y²/U=E, siendo
E=||w·y−v·x||²−R²y². Su signo se calcula con enteros.
Finalmente sign(x+yt₀)=sign(y)·sign(t₀−z). La igualdad corresponde a un
extremo, así que las dos condiciones interiores deben ser estrictas.

Si no existe primer contacto interior, comprueba las dos semirrectas de los
extremos. Para w define p=w·v, V=v·v. Como el punto inicial es exterior,
hay contacto futuro exactamente si p<0 y p²≥V(w·w−R²). La igualdad es
tangencia y también cuenta. Si alguna semirrecta cumple, devuelve `Crash`;
si no, `False alarm`. Ya se descartó cualquier contacto interior anterior
que pudiera detenerlas.

El número de operaciones y el espacio auxiliar son O(1). Las componentes
trasladadas y las de u no superan 2·10⁵, y las de v no superan 10⁵.
Esto acota |H|≤1.152·10³³ y |E|≤1.728·10³³: todos los intermediarios
calculados caben en 128 bits con signo. El D completo no usado puede
superar ese rango; por eso es necesario K.

## Notas por lenguaje

C++ y Rust usan 128 bits con signo en todas las operaciones vectoriales;
convertir después de multiplicar en 64 bits sería inseguro. Go 1.14 usa
math/big, Java 8 BigInteger inmutables y Python 3.12 enteros exactos.
Los auxiliares de Go crean resultados nuevos y no mutan argumentos compartidos.
El programa no usa raíces, división, coma flotante ni tolerancias. Comprobar
primero las posibles colisiones futuras de los extremos ignoraría la parada
provocada por un contacto interior anterior.

Las respuestas coinciden con una búsqueda del primer contacto en alta
precisión en 6957 casos, entre ellos 32 exactos de tangencia, empate en
un extremo, desplazamientos de una unidad y direcciones casi paralelas;
una implementación aceptada independiente coincide en otros 48.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1909_geometry.cpp](1909_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 440 KB |
| [1909_geometry.go](1909_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1216 KB |
| [1909_geometry.java](1909_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1756 KB |
| [1909_geometry.py](1909_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 764 KB |
| [1909_geometry.rs](1909_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.062 s | 220 KB |
