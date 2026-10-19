# 2008. Tres saltos balísticos

[Timus 2008](https://acm.timus.ru/problem.aspx?space=1&num=2008) · dificultad 1038 · math

Problema original de Olga Karpova. (Prepared by Alexey Kungurtsev), del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una partícula empieza en una de dos manos, sin conocer cuál. Salta a la
otra mano, vuelve a la inicial y después salta a un punto que representa
la cabeza. Cada salto puede elegir una nueva velocidad inicial de módulo
no mayor que `v`. Solo actúa gravedad hacia abajo `g=9.8`, con velocidad
horizontal constante. Decidir si alguna mano inicial permite los tres
saltos. Los tres puntos fijos y distintos están en un plano vertical,
con eje y hacia arriba.

## Entrada

Entero `v`, seguido de tres parejas de coordenadas en orden cabeza, mano
izquierda y mano derecha. Velocidad y coordenadas son enteros no
negativos de hasta 10000, en metros y metros por segundo. Tiempo 0,5
segundos, memoria 64 MB.

## Salida

Imprimir exactamente `Yes` si es posible y `No` en caso contrario. Se
compara el único token exactamente.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
10
0 5
0 0
10 0
```

```
Yes
```

```
10
10 5
0 0
10 0
```

```
Yes
```

```
5
0 5
0 0
10 0
```

```
No
```

Velocidad 10 permite ambos saltos entre manos separadas por 10. El
primer ejemplo termina desde la izquierda, el segundo desde la derecha.
En el tercero, velocidad 5 no basta ni para cruzar entre manos.

## Solución

Se requieren las dos direcciones entre manos independientemente de la
inicial. El salto final puede salir de cualquiera. Exigir
`izquierda→derecha` y `derecha→izquierda`, junto con `izquierda→cabeza`
o `derecha→cabeza`. El desplazamiento vertical hace que la
alcanzabilidad sea direccional.

Para un salto, sean `dx,dy` los desplazamientos, `t>0` su duración y
`r=sqrt(dx²+dy²)>0`. Las componentes iniciales necesarias son `ux=dx/t`
y `uy=dy/t+g t/2`, con módulo cuadrado

`u²(t)=r²/t²+g dy+g²t²/4`.

La suma del primer y último término alcanza mínimo `g r` cuando
`t²=2r/g`. Así, el mínimo módulo cuadrado inicial es `g(r+dy)`, no
negativo y alcanzable en tiempo positivo para puntos distintos. Un salto
vertical descendente puede necesitar velocidad inicial cero: la caída
libre es válida.

Un salto es posible exactamente si `v²≥(49/5)(r+dy)`. Sea `T=5v²−49dy`.
Equivale a `T≥49r`, y por tanto a `T≥0` y `T²≥49²(dx²+dy²)`. Son
comparaciones enteras exactas. Comprobar el signo antes de elevar al
cuadrado; la igualdad es alcanzable y no necesita tolerancias.

Ambas direcciones entre manos son necesarias. Si cumplen y una mano
alcanza la cabeza, elegirla como inicial, realizar ida y vuelta y luego
el salto final. Toda secuencia válida exige esas mismas direcciones, por
lo que el criterio completo es necesario y suficiente.

Tiempo `O(1)` y memoria `O(1)` para tres puntos fijos. Bastan enteros
con signo de 64 bits: `|T|≤500490000`, por tanto
`T²≤250490240100000000<2^63`, y `49²(dx²+dy²)≤480200000000`. La
multiplicación debe ser de 64 bits desde el principio.

## Notas por lenguaje

Leer primero la cabeza y después las manos. Comprobar ambas direcciones
entre manos y permitir cualquiera para el último salto. Usar
desplazamientos con signo aunque las coordenadas no sean negativas.
Mantener `g=49/5` exactamente, sin redondear a 10 ni calcular raíces en
el programa. Incluir `v=0`, `dy` negativo, trayectorias verticales e
igualdad. C++, Go, Java y Rust usan enteros con signo de 64 bits; los
enteros Python son exactos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2008_math.cpp](2008_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 384 KB |
| [2008_math.go](2008_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1092 KB |
| [2008_math.java](2008_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 440 KB |
| [2008_math.py](2008_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 516 KB |
| [2008_math.rs](2008_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.062 s | 228 KB |
