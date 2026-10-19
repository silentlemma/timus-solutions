# 2048. Clasificar años por sus viernes trece

[Timus 2048](https://acm.timus.ru/problem.aspx?space=1&num=2048) · difficulty 900 · implementation

Problema original de Alexander Ipatov, preparado por Oleg Dolgorukov, del Campeonato de Programación Deportiva de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada año de A a B del calendario gregoriano, contar los meses cuyo
día 13 cae en viernes, y para cada k de 0 a 12 indicar cuántos años
tienen exactamente k meses así. Un año es bisiesto si es divisible por
400, o por 4 pero no por 100; entonces febrero tiene 29 días. Los
límites son 1 segundo y 64 MB.

## Entrada

Dos enteros A y B, 1919 ≤ A ≤ B ≤ 10⁹.

## Salida

Trece líneas `k: count` para k = 0, …, 12 en orden creciente, incluidas
las de cero.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
2015 2016
```

```
0: 0
1: 1
2: 0
3: 1
4: 0
5: 0
6: 0
7: 0
8: 0
9: 0
10: 0
11: 0
12: 0
```

En 2015 coinciden el 13 de febrero, marzo y noviembre, por lo que un año
pertenece al grupo tres. En 2016 solo coincide el 13 de mayo, aportando
un año al grupo uno. Los demás grupos son cero y también se imprimen sus
etiquetas.

## Solución

### Construir un período

Numerar los días desde lunes cero hasta domingo seis. El 1 de enero del
año 1 es lunes en el calendario gregoriano proléptico. Mantener el día
semanal `w` del primero del mes: el trece corresponde a `(w+12) mod 7` y
coincide si vale cuatro, viernes. Después avanzar `w` por la longitud
real del mes, módulo siete.

Simular `1..400` y guardar en `type[y-1]` la cantidad del año `y`.
Reunir esos cuatrocientos tipos en un histograma `cycle` de trece
grupos. Añadir el día de febrero solo con la regla completa de
bisiestos.

El patrón de bisiestos se repite cada 400 años. Hay
`400/4-400/100+400/400=97` bisiestos y `400*365+97=146097=7*20871` días
por período. Por tanto, su día semanal inicial también se repite.
Iguales longitudes de meses e iguales días iniciales prueban que los
tipos anuales tienen período 400.

### Histogramas de prefijos

Sea `F(t)` el histograma de `1..t`. Escribir `t=400q+r`, `0≤r<400`.
Comenzar con `q*cycle` y añadir uno al grupo de cada uno de los primeros
`r` tipos guardados. La respuesta es `F(B)-F(A-1)` componente a
componente.

### Corrección

La recurrencia mensual empieza en un día conocido y avanza exactamente
la longitud real de cada mes. Por inducción obtiene correctamente cada
día trece y los tipos del período inicial. La duración de cuatrocientos
años y la repetición de bisiestos prueban que esos tipos se repiten.

Los años `1..t` se dividen en `q` períodos completos disjuntos y un
prefijo de `r` años. Cada período aporta `cycle` y el resto exactamente
sus primeros `r` tipos; así se calcula `F(t)`. Restar lo contado hasta
`A-1` de lo contado hasta `B` deja precisamente el intervalo inclusivo
en cada grupo.

Con `C=400`, el tiempo es `O(C*12+C+13)` y el espacio auxiliar
`O(C+13)`. Ambos son constantes respecto a la amplitud del intervalo de
entrada. No se recorren los años `A..B` uno por uno.

## Notas por lenguaje

- El trece está doce días después del primero, no trece.
- El arreglo comienza en el año uno: el índice es `(year-1) mod 400`.
- Restar `F(A-1)` también cuando los extremos coinciden.
- Ser divisible por cuatro no basta: 2100 es ordinario; 2000 y 2400 son
  bisiestos.
- Imprimir grupos nulos y contar años en vez de meses.

Los cinco puertos construyen el calendario una vez y lo reutilizan en
ambos prefijos. Los compilados usan contadores de 64 bits; Python usa
enteros. Los solucionadores no requieren biblioteca de fechas ni
distribución fijada de antemano.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2048_implementation.cpp](2048_implementation.cpp) | G++ 13.2 x64 | implementation | O(C*12+C+13) | AC | 0.015 s | 400 KB |
| [2048_implementation.go](2048_implementation.go) | Go 1.14 x64 | implementation | O(C*12+C+13) | AC | 0.031 s | 1120 KB |
| [2048_implementation.java](2048_implementation.java) | Java 1.8 | implementation | O(C*12+C+13) | AC | 0.093 s | 492 KB |
| [2048_implementation.py](2048_implementation.py) | Python 3.12 x64 | implementation | O(C*12+C+13) | AC | 0.078 s | 640 KB |
| [2048_implementation.rs](2048_implementation.rs) | Rust 1.75 x64 | implementation | O(C*12+C+13) | AC | 0.031 s | 240 KB |
