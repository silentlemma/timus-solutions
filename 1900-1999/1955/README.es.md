# 1955. Segmento visible más largo de un polígono simple

[Timus 1955](https://acm.timus.ru/problem.aspx?space=1&num=1955) · difficulty 3071 · geometry

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Egor Shchelkonogov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hallar la mayor distancia entre dos puntos de un polígono simple cuyo
segmento completo queda dentro o sobre la frontera. Puede ser no convexo;
no hay autocruces ni autocontactos. Los extremos pueden estar dentro de
aristas. Límites: 1 segundo, 64 MB.

## Entrada

Primero n, 3≤n≤200. Después n pares enteros x,y en orden horario o
antihorario, −1000≤x,y≤1000. Se permiten aristas consecutivas colineales;
las no adyacentes no se cruzan ni tocan.

## Salida

Un real: máxima longitud, error absoluto o relativo ≤10⁻⁶. Doce decimales.

## Evaluación

La respuesta se compara con error absoluto o relativo 10⁻⁶.

## Ejemplos

```
4
0 0
0 1
1 1
1 0
```

```
1.414214
```

## Solución

### Por qué bastan rectas de pares de vértices

Tomar un segmento cerrado máximo y extenderlo hasta la frontera. Sin
vértices sobre él, ambos extremos están dentro de aristas. Mover ligeramente
un extremo en ambos sentidos de su arista sigue siendo factible; la distancia
al cuadrado es estrictamente convexa y no tiene máximo local. Si el único
vértice es un extremo, mover el otro igual. Una recta colineal con frontera
no es excepción: por maximalidad contiene toda la arista y otro vértice.

Si el único vértice v está dentro del segmento, girar ligeramente la recta
en ambos sentidos alrededor de v. Los extremos quedan en sus aristas fijas
y persiste factibilidad local. Cada mitad mide h/|sin(θ−α)|, h>0 la distancia
perpendicular a la recta de su arista. En el intervalo angular abierto es
una cosecante positiva de segunda derivada estrictamente positiva. La suma
es estrictamente convexa y no puede tener máximo local. Una dirección sobre
un rayo de frontera ya incluye otro vértice. Por tanto existe un máximo
que contiene dos vértices del polígono.

Enumerar la recta completa de cada par, intersectarla con el polígono
cerrado y tomar la componente conexa más larga. Los resultados son factibles
y alguno es óptimo. No limitarse a la distancia de los vértices elegidos:
el segmento puede extenderse hasta interiores de otras dos aristas.

### Intersección con una recta

Parametrizar P+tD, D=Q−P. Alturas enteras exactas h(V)=cross(D,V−P).
Para A→B, si difieren (h(A)>0),(h(B)>0), añadir
t=cross(A−P,B−A)/cross(D,B−A). Ordenar eventos y emparejar consecutivos.
En −∞ se está fuera del polígono acotado; la regla semiabierta trata los
vértices consistentemente. Eventos tangentes duplicados crean intervalos
cero o dos que se tocan. Añadir cada arista con ambas alturas cero como
intervalo cerrado, con t=dot(V−P,D)/dot(D,D). Ordenar todos los intervalos
y fusionar solapamientos Y contactos. La mayor amplitud por |D| da el
segmento de esa recta. Los intervalos de frontera preservan aristas colineales.

### Aceleraciones exactas

La máxima distancia cuadrada U entre vértices acota cualquier pareja de
puntos: también es el diámetro de su envolvente convexa. Si el par más
lejano es visible, devolver sqrt(U). Cada arista y cada par visible confirmado
dan una cota inferior entera factible L.

Para caja de ancho w, alto h y d²=dot(D,D), un segmento paralelo a D tiene
cuadrado ≤w²d²/dx² si dx≠0 y ≤h²d²/dy² si dy≠0. Rechazar si alguna cota
es estrictamente menor que L mediante multiplicación cruzada entera. Una
componente cero simplemente no rechaza con su prueba. Normalizar D por gcd
y signo y eliminar rectas repetidas con (nx,ny,cross((nx,ny),P)).

Python además rechaza un par al detectar una arista que cruza transversalmente
el interior de su segmento, con signos y rangos enteros del numerador y
denominador. Los dos vértices de contacto de un máximo son visibles entre
sí, así que es seguro. Marcar la recta vista solo después de hallar un par
visible: un par invisible no debe ocultar otra componente de la misma recta.
Actualizar alturas por incrementos enteros de aristas permite salir pronto.
Las versiones nativas pueden examinar componentes incluso de pares invisibles.

### Cotas numéricas

Signos, colinealidad, gcd y podas usan enteros. Numeradores y denominadores
de parámetros tienen módulo ≤8·10⁶, convertibles exactamente a binary64.
Racionales distintos se separan relativamente al menos 1/(8·10⁶)²>10⁻¹⁴,
mucho más que el redondeo; fracciones iguales redondean igual. No hace
falta epsilon al ordenar ni unir contactos. |t|<2829, error del cociente
≤2⁻⁴² y de resta ≤2⁻⁴⁰. Con |D|<2829, productos y raíz final, el error
absoluto de longitud queda <10⁻⁸; maximizar conserva la cota. Productos
enteros de poda ≤3,2·10¹³ caben en 64 bits con signo.

O(n³ log n) tiempo: O(n²) rectas, O(n) eventos por recta y ordenación.
O(n²) espacio para deduplicación, O(n) trabajo por recta. Diámetro O(n²).
Las podas solo mejoran estos límites.

El diámetro no convexo puede salir del polígono, y extremos óptimos no
tienen por qué ser vértices. Conservar frontera cerrada, unir contactos,
usar regla semiabierta coherente y no multiplicar podas en 32 bits. Ambos
sentidos de recorrido funcionan. No descartar una recta entera por un par
invisible antes de probar otra pareja.

## Notas por lenguaje

Programas completos, solo biblioteca estándar. Enteros nativos de 64 bits
con signo y binary64 únicamente para cocientes y longitudes; Python usa
enteros arbitrarios. Java evalúa flotantes estrictamente y reutiliza arrays.
Empaqueta nx,ny+2000,c+4000000 en campos disjuntos de bits: rangos
[0,2000],[0,4000],[0,8000000] caben en los campos elegidos de 12/23 bits,
y todo en signed long. Otras versiones conservan una terna de enteros.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1955_geometry.cpp](1955_geometry.cpp) | G++ 13.2 x64 | geometry | O(n^3 log n) | AC | 0.062 s | 992 KB |
| [1955_geometry.go](1955_geometry.go) | Go 1.14 x64 | geometry | O(n^3 log n) | AC | 0.234 s | 9272 KB |
| [1955_geometry.java](1955_geometry.java) | Java 1.8 | geometry | O(n^3 log n) | AC | 0.359 s | 8124 KB |
| [1955_geometry.py](1955_geometry.py) | Python 3.12 x64 | geometry | O(n^3 log n) | AC | 0.703 s | 1104 KB |
| [1955_geometry.rs](1955_geometry.rs) | Rust 1.75 x64 | geometry | O(n^3 log n) | AC | 0.062 s | 2096 KB |
