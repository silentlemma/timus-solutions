# 2049. Construir transferencias mediante divisiones inversas

[Timus 2049](https://acm.timus.ru/problem.aspx?space=1&num=2049) · difficulty 3271 · constructive

Problema original de Daniil Ayzenshteyn, preparado por Egor Shchelkonogov, del Campeonato de Programación Deportiva de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n recipientes con una unidad cada uno. La acción a → b vierte de a
en b exactamente lo que b contiene en ese momento, así que (x, y) pasa a
(x − y, 2y); solo se permite si x ≥ y. Con a lo sumo 3n acciones, lograr
que el recipiente 1 tenga exactamente k unidades; los demás pueden
terminar con cualquier cantidad. Los límites son 1 segundo y 64 MB.

## Entrada

Dos enteros n y k, 1 ≤ k ≤ n ≤ 100 000.

## Salida

Imprimir `-1` si es imposible. Si no, imprimir el número de acciones M,
0 ≤ M ≤ 3n, y después M líneas con los pares a b de recipientes
distintos.

## Evaluación

Un comprobador ejecuta las acciones y verifica que cada una está
permitida y que el recipiente 1 termina con k unidades; se acepta
cualquier secuencia válida, y `-1` solo si es imposible.

## Ejemplos

```
5 3
```

```
4
2 1
4 3
3 1
1 5
```

```
5 5
```

```
-1
```

El primero produce
`[1,1,1,1,1]→[2,0,1,1,1]→[2,0,2,0,1]→[4,0,0,0,1]→[3,0,0,0,2]` y deja
tres en el primero. El segundo exigiría concentrar las cinco unidades;
el invariante siguiente lo impide.

## Solución

### Existencia

Si `k` es potencia de dos, incluido uno, existe respuesta. En otro caso,
existe exactamente cuando `n≥k+1+(k mod 2)`.

La parte impar del máximo común divisor de todos los volúmenes es
invariante. Para cualquier potencia impar de primo `q`, todos los
valores posteriores a `(x,y)→(x-y,2y)` son divisibles por `q` si y solo
si lo eran antes, pues dos es invertible módulo `q`. El máximo común
divisor inicial es uno. Por tanto, con `n=k`, concentrar todo exige que
`k` sea potencia de dos.

Si `k>1` es impar, considerar la primera vez que el primer recipiente
alcanza `k`. No puede ser receptor, porque duplicar produce un par. Como
donante, antes tenía `k+y` y el receptor `y≥1`: se necesita masa total
al menos `k+2`. Esto prueba todos los casos excluidos; la construcción
prueba suficiencia.

### Construcción inversa

Usar `N=k` recipientes si es potencia de dos, o `N=k+1+(k mod 2)` en
otro caso. Los no usados permanecen en uno. Empezar en el estado
**final** deseado: `[k,0,…]` o `[k,N-k,0,…]`. En el segundo, el extra es
uno o dos y la parte impar del máximo común divisor es uno.

Una acción inversa toma `2h>0` del recipiente `b` y mueve su mitad a
otro `a`: `(x,2h)→(x+h,h)`. Guardar el par directo original `(a,b)`. Se
puede deshacer legalmente, pues `x+h≥h`. Al terminar invertir el
**orden** de los pares, conservando sus direcciones.

Mantener recipientes vacíos, recipientes positivos pares y grupos de
impares por volumen.

1. Si hay al menos dos pares, dividir cualquiera entre su recipiente y
   uno vacío.
2. Si el único par es múltiplo de cuatro, dividirlo igualmente.
3. En otro caso es `2h` con `h` impar. Elegir volumen impar `a≠h` y
   mantener **esos mismos dos recipientes**. Aplicar acciones inversas
   intercambiando sus roles par/impar hasta que el par sea múltiplo de
   cuatro; dividirlo en la siguiente iteración.
4. Si ningún impar difiere de `h`, la parte impar del máximo común
   divisor sería `h`, luego `h=1`. Solo queda un dos y los demás
   positivos son unos; dividir ese último dos.

Siempre hay vacío cuando hace falta: con masa `N` y algún volumen mayor
que uno hay menos de `N` positivos. Una división ordinaria conserva un
par salvo en el último paso; las acciones de pareja también lo
conservan.

En la pareja fija `(2h,a)`, la mitad y el impar evolucionan como
`(h,a)→((h+a)/2,h)` mientras la nueva mitad siga impar. La diferencia no
nula `D=a-h` pasa a `-D/2`. Tras exactamente `t=ν2(|D|)` pasos la mitad
es par y el volumen completo múltiplo de cuatro. Cada tramo termina y la
división siguiente aumenta el número de positivos. Finalmente hay `N`
positivos y masa `N`: todos son uno. Invertir las acciones guardadas da
la solución directa manteniendo la identidad del primer recipiente.

### Cota de acciones

La prueba combina una cota analítica y una **verificación finita
exhaustiva** pequeña, incluida abajo y en [tests/gen.py](tests/gen.py).

Definir `L(v)=floor(log2(v))` para positivos, `F=sum L(v)` y `P`
cantidad de recipientes positivos. Cobrar cada paso o grupo por
`2ΔF+3ΔP`.

Una división `2h→h,h` cuesta uno, con `ΔP=1` y `ΔF=L(h)-1≥-1`,
cumpliendo la cota.

Agrupar los `t` pasos de pareja con la división inmediatamente
posterior. Cuestan `t+1` y tienen `ΔP=1`. Escribir `a-h=2^t d`, con `d`
impar con signo, `ε=(-1)^t` y `T=2h+a`. Al terminar hay `b,b,c`, donde
`b=(T-εd)/3` es par positivo y `c=T-2b` impar positivo. Se obtiene
resolviendo `h_next=(T-h)/2`, cuyo punto fijo es `T/3`.

Basta `ΔF≥floor((t-1)/2)` para concluir `t+1≤2ΔF+3`.

Con `t=1`, `b=(h+a)/2,c=h`. Si `q=L(max(h,a))`, entonces `b≥max(h,a)/2`
y `ΔF=2L(b)-L(a)-1≥q-3`. Esto basta para `q≥3`; en otro caso ambos
valores son menores que ocho.

Para `t≥2`, sean `u=min(h,a),v=max(h,a),p=L(u),q=L(v)`. Los promedios
mantienen `b,c≥u`. Además `b,c≥v/4`: si `a≥h`, para `t` par se tiene
`b≥(a+3h)/4,c≥a/3` y para `t≥3` impar, `c≥(a+3h)/4,b≥a/3`; si `h>a`,
ambos son al menos `h/2`. Por ello `ΔF≥3max(p,q-2)-p-q-1≥q-5`. Como
`|a-h|≥2^t`, resulta `q≥t`. Para `t≥8` esto ya prueba la desigualdad.
Para `2≤t≤7` también basta `q≥5+floor((t-1)/2)`. En los casos restantes
`q≤7` y ambos impares son menores que 256.

Todos los casos restantes, incluidos los pequeños con `t=1`, quedan
cubiertos por estos 16256 pares ordenados distintos de impares positivos
menores que 256:

```python
L = lambda x: x.bit_length() - 1
for h in range(1, 256, 2):
    for a in range(1, 256, 2):
        if a == h:
            continue
        D = a - h
        t = (abs(D) & -abs(D)).bit_length() - 1
        d = D // (1 << t)
        T = 2 * h + a
        b = (T - (-1) ** t * d) // 3
        c = T - 2 * b
        delta = 2 * L(b) + L(c) - L(2 * h) - L(a)
        assert t + 1 <= 2 * delta + 3
```

Todas las aserciones se cumplen, completando la desigualdad de fase.
Sumando divisiones sueltas y fases completas, el estado final tiene
`F=0,P=N`: `M≤2(0-F_initial)+3(N-P_initial)≤3N≤3n`. No se usa ningún
corte empírico sobre `n` ni sobre el número de acciones.

### Implementación y complejidad

Guardar listas doblemente enlazadas en arreglos. Los positivos pares
comparten una lista; los impares pertenecen a la lista de su volumen
actual. Otra lista contiene los grupos impares no vacíos. Para encontrar
un volumen distinto de `h` basta el primer grupo o el siguiente.
Eliminar ambas pertenencias antiguas antes de modificar volúmenes y
volver a insertarlas después. Los enlaces de un recipiente se reutilizan
entre listas pares e impares.

Cada operación de lista es constante y no recorre conjuntos dispersos.
Tiempo y espacio: `O(N+M)=O(n)`.

## Notas por lenguaje

El receptor se duplica y la cantidad transferida no es arbitraria.
Conservar la identidad del primero. Invertir el orden, no la dirección
de cada par. Mantener la pareja fija dentro del tramo para aplicar la
prueba. Solo las divisiones usan vacíos. Cero acciones es correcto con
`k=1`.

Todos los puertos usan arreglos compactos y búferes de pares separados.
Python usa `array` sin signo y salida por bloques; Java, arreglos
primitivos y un búfer de bytes reutilizable. C++, Go y Rust escriben con
búfer.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2049_constructive.cpp](2049_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.031 s | 5052 KB |
| [2049_constructive.go](2049_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.046 s | 14800 KB |
| [2049_constructive.java](2049_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 7888 KB |
| [2049_constructive.py](2049_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.593 s | 5608 KB |
| [2049_constructive.rs](2049_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.015 s | 9200 KB |
