# 1913. Dos repetidores para conectar tres terminales

[Timus 1913](https://acm.timus.ru/problem.aspx?space=1&num=1913) · difficulty 1863 · geometry

Problema original de Alexey Samsonov (preparado por Denis Mukhametianov), de la subregión oriental del NEERC 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay dos fuentes G₁,G₂ y un receptor C en el plano. Colocar dos repetidores.
Una fuente transmite solamente a un repetidor situado a distancia ≤R;
un repetidor transmite al otro o a C a distancia ≤R. Ambas fuentes deben
alcanzar C mediante estas transmisiones dirigidas. No existen conexiones
directas fuente–C ni fuente–fuente. Encontrar cualquier colocación válida
o declarar que es imposible. Los repetidores pueden coincidir entre sí
y con los terminales. Límites: 1 segundo, 64 MB.

## Entrada

Un entero R, 1≤R≤10 000, seguido de las coordenadas enteras de C,G₁,G₂,
en ese orden. Cada coordenada está en [−10 000,10 000], y los tres
terminales son distintos entre sí.

## Salida

Escribir `Death` si no hay solución. En otro caso escribir
`Now we have enough power` y dos líneas con las coordenadas de los
repetidores. Se admite cualquier solución con error absoluto o relativo
de coordenadas no mayor que 10⁻⁵.

## Evaluación

El comprobador verifica la frase, cuatro coordenadas
finitas y la accesibilidad de C desde cada fuente en el grafo dirigido
permitido. Las aristas admiten solo 10⁻⁷ de error absoluto de redondeo.
`Death` debe coincidir con la factibilidad esperada.

## Ejemplos

```
1
0 0
2 1
2 -1
```

```
Now we have enough power
1 0
2 0
```

```
1000
0 0
2 1
2 -1
```

```
Now we have enough power
2 -1
0 0
```

```
1
0 0
5 0
0 5
```

```
Death
```

## Solución

Probar primero caminos independientes. Si |C−G₁|≤2R y |C−G₂|≤2R,
colocar cada repetidor en el punto medio entre C y una fuente. No hace
falta que los repetidores se comuniquen entre sí, incluso con las fuentes
en lados opuestos de C.

En otro caso una colocación válida tiene un repetidor cercano a C y
otro conectado al primero. Ambas fuentes usan el repetidor lejano, o
cada una usa uno. Estas tres posibilidades se unifican eligiendo un
terminal T de C,G₁,G₂ y un punto H a distancia ≤R de los otros dos
y ≤2R de T. El segundo repetidor es el punto medio entre H y T.
Si T=C, H recoge ambas fuentes; si T es una fuente, H conecta C y la otra.

Comprobar las tres intersecciones de discos cerrados con radios R,R,2R,
rotando el radio mayor. Bastan como candidatos los centros y las
intersecciones de cada par de circunferencias. Si la frontera común
cambia de circunferencia, el cambio es uno de esos vértices. Si no
cambia, la intersección es un disco contenido y sirve su centro.
Las tangencias también se incluyen.

### Decisiones exactas

Para centros P,Q y radios a,b, sean u=Q−P, d=u·u>0,
A=d+a²−b² y F=4a²d−A². Si F<0 no se cortan. En otro caso
los puntos son P+(Au±√F·rot90(u))/(2d), con rot90(x,y)=(−y,x).
Para el tercer centro S y radio c, definir w=P−S y
T=d(c²−a²−w·w)−A(w·u). La pertenencia equivale exactamente
a T≥B√F, donde B=±w·rot90(u) con el signo del candidato.

Con B=0 o F=0 basta T≥0. Con B>0 exigir T≥0 y T²≥B²F.
Con B<0 aceptar T≥0 o T²≤B²F. Se conserva el signo antes de elevar
al cuadrado; todas las decisiones son enteras, sin epsilon. Solo se
calculan coordenadas decimales después de aceptar el candidato.
Imprimir 12 decimales y el punto medio entre H y T.

### Corrección

Si ambos repetidores llegan a C, las desigualdades triangulares implican
las dos cotas 2R del primer caso. Si solo uno llega a C, el otro debe
conectarse a él. Cuando ambas fuentes usan el lejano, este está en los
discos de T=C. Si usan repetidores distintos, el cercano pertenece a los
discos de T igual a la fuente lejana. Si ambas usan el cercano, el caso
independiente ya funciona. Por tanto se cubren todas las redes factibles.
Recíprocamente, el punto medio divide una distancia ≤2R en dos enlaces
permitidos y H toca los otros dos terminales: toda construcción es válida.
Los candidatos completos y las comparaciones exactas justifican `Death`.

Tiempo y memoria adicional `O(1)`: solo hay tres terminales y un número
constante de asignaciones y candidatos.

En el primer ejemplo H=(2,0) recoge las fuentes y (1,0) conecta C.
El segundo permite coincidencias con terminales. En el tercero una fuente
está a más de 3R de C, fuera del alcance de dos repetidores.

No exigir enlace entre repetidores independientes ni permitir enlaces
directos fuente–C. Las coincidencias son válidas. Incluir los tres radios
ampliados, tangencias internas/externas, B y T negativos, y evitar
desbordamiento de 64 bits al comparar cuadrados.

## Notas por lenguaje

Las distancias al cuadrado no superan 8·10⁸. La cota |T|≤1.76·10¹⁸ cabe
en 64 bits con signo; T²≤3.0976·10³⁶ es una cota superior conservadora.
C++ y Rust comparan los cuadrados en 128 bits; Go y Java usan enteros grandes
para esa comparación; Python usa enteros de precisión arbitraria. Double
basta para imprimir coordenadas, pero no decide la existencia.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1913_geometry.cpp](1913_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 464 KB |
| [1913_geometry.go](1913_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1188 KB |
| [1913_geometry.java](1913_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1124 KB |
| [1913_geometry.py](1913_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 872 KB |
| [1913_geometry.rs](1913_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 272 KB |
