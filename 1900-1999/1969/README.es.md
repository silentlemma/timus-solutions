# 1969. Reconstrucción de horarios repetidos

[Timus 1969](https://acm.timus.ru/problem.aspx?space=1&num=1969) · difficulty 2811 · constructive

Problema original del Concurso Individual Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tranvías idénticos se mueven a velocidad constante entre los extremos A y B,
girando sin detenerse. Cada uno sale de A, completa el mismo número entero
positivo k de viajes de ida y vuelta y termina en A. Un observador está
estrictamente entre ambos extremos. Los tiempos a desde A al observador y
b desde allí a B son enteros positivos en segundos, comunes a todos.

El primero sale en D. Las salidas son distintas y crecientes; todas ocurren
estrictamente antes de que el primero vuelva a A por primera vez. Todos los
viajes terminan como máximo a las 23:59:59 del mismo día. Dados D y todos los
instantes distintos observados, ordenados, reconstruir cualquier horario
compatible. Límites: 1 segundo, 64 MB.

## Entrada

La primera línea contiene D con formato HH:MM:SS. Cada línea restante hasta
EOF contiene un paso observado con el mismo formato. No hay línea de cantidad.
El número n es par, 2≤n≤5000. Los pasos son distintos, crecientes, no pasan
de 23:59:58 y el primero es posterior a D. Se garantiza una solución.

## Salida

Una línea por tranvía, en orden de salida: todas las visitas a extremos,
desde A, alternando B y A, hasta el regreso final a A. Hay 2k+1 horas
HH:MM:SS por línea. Todos comparten k y la duración a+b de cada sentido.
Se acepta cualquier horario válido.

## Evaluación

Un comprobador simula el horario impreso y verifica las condiciones del
enunciado y el multiconjunto exacto de pasos; se acepta cualquier
horario válido.

## Ejemplos

```
08:00:00
08:07:30
08:38:30
08:44:49
08:51:32
08:53:30
09:15:49
09:22:32
09:24:30
09:30:49
09:37:32
10:01:49
10:08:32
```

```
08:00:00 08:23:00 08:46:00 09:09:00 09:32:00
08:37:19 09:00:19 09:23:19 09:46:19 10:09:19
08:44:02 09:07:02 09:30:02 09:53:02 10:16:02
```

## Solución

Convertir las horas a segundos. Sea T la secuencia ordenada, P=2(a+b) el
período completo y τ=P/2 la duración en un sentido.

### Enumerar el primer paso de regreso

La primera observación pertenece al primer tranvía en su salida hacia B,
por lo que a=T[0]−D es conocido. Su primer regreso pasa en D+P−a. Si es
T[j], entonces P=T[j]−D+a. Antes solo hay primeros pasos de ida: ningún
tranvía posterior puede regresar antes. Así j≤R≤n/2, donde R es el número
de tranvías. Probar j=1,…,n/2 inclusive. Rechazar P impar o P≤2a, que
implicaría b≤0.

### Obtener k sin otra búsqueda

Si d es la última salida, la última observación es d+kP−a y D≤d<D+P.
Por tanto,

k=floor((T[n−1]−D+a)/P).

Rechazar k=0 o n no divisible por 2k; en otro caso R=n/(2k). La desigualdad
estricta de la ventana es esencial para esta identidad.

### Reconstrucción voraz

Para cada P, recorrer T y saltar lo ya usado. El menor t sin usar debe ser
el primer paso de ida de un tranvía restante, pues todos sus otros pasos
son posteriores. Su salida está forzada a t−a y debe ser menor que D+P.
Necesita exactamente los pasos

t+rP y t+(P−2a)+rP, para r=0,…,k−1.

Exigir que existan y estén libres; después marcarlos. Rechazar por ausencia,
colisión, salida inválida o cantidad incorrecta de tranvías. Aceptar cuando
todas las observaciones se reparten entre R tranvías completos. Un conjunto
o arreglo permite consultas rápidas; marcas con número de generación evitan
limpiar todo el arreglo del día para cada candidato.

### Corrección y coste

El P real aparece en el rango probado y la fórmula determina su k real.
Tras retirar tranvías completos, el menor paso restante fuerza la siguiente
salida real; por inducción ese candidato no falla. Todo candidato exitoso
asigna cada observación exactamente a un trayecto físico, cumple las reglas
de extremos y a,b>0. La llegada final es T[n−1]+a, dentro del día por la
garantía de entrada. Luego cualquier respuesta devuelta es válida.

Como máximo n/2 candidatos examinan o marcan O(n) instantes cada uno. Con
S=86400, tiempo `O(n²+S)` y memoria `O(n+S)`; bastan enteros de 32 bits.

En el ejemplo a=450 segundos, P=2760, τ=1380, k=2 y R=3. Las salidas son
08:00:00, 08:37:19 y 08:44:02. Sumar τ repetidamente produce cinco visitas
por línea. Alternar desplazamientos de 450 y 930 segundos reproduce las
doce observaciones de entrada.

Leer hasta EOF sin cantidad inicial. Distintos períodos y valores de k
pueden explicar la misma entrada: no comparar respuestas por tokens.
Incluir el índice n/2. La última salida es estrictamente menor que D+P.
Reiniciar lógicamente las marcas y verificar límites antes de indexar.
Las visitas a extremos de tranvías distintos pueden coincidir; los pasos
observados no pueden hacerlo.

## Notas por lenguaje

Las cinco versiones comparten la reconstrucción. Python usa un conjunto
para presencia y una lista para generaciones; C++, Go, Java 8 y Rust usan
arreglos. Java añade directamente campos de dos dígitos, evitando llamadas
repetidas al formateador general. Cada tranvía conserva su propia línea.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1969_constructive.cpp](1969_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2+86400) | AC | 0.015 s | 804 KB |
| [1969_constructive.go](1969_constructive.go) | Go 1.14 x64 | constructive | O(n^2+86400) | AC | 0.046 s | 2752 KB |
| [1969_constructive.java](1969_constructive.java) | Java 1.8 | constructive | O(n^2+86400) | AC | 0.187 s | 5808 KB |
| [1969_constructive.py](1969_constructive.py) | Python 3.12 x64 | constructive | O(n^2+86400) | AC | 0.093 s | 2540 KB |
| [1969_constructive.rs](1969_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2+86400) | AC | 0.015 s | 716 KB |
