# 1994. Exclusiones aleatorias óptimas entre pérdidas nocturnas

[Timus 1994](https://acm.timus.ru/problem.aspx?space=1&num=1994) · dificultad 1050 · dp, probability, combinatorics

Problema original de Denis Dublennykh, preparado por Eugene Kurpilyansky.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

De `n` miembros activos, `k` son hostiles y el resto ordinarios. Cada
noche cada hostil puede eliminar un ordinario; las asignaciones
maximizan las pérdidas, por lo que desaparece el menor de ambos grupos.
Cada día siguiente se elige un número positivo de exclusiones; las
identidades se escogen uniformemente al azar. Los excluidos no actúan ni
cuentan al final. Optimice los números diarios para maximizar la
esperanza de ordinarios activos cuando cesen las pérdidas o no quede
ninguno.

El momento inicial es nocturno: la primera pérdida sucede antes de la
primera exclusión. No se eligen identidades. `1≤k≤min(n,20)`, `n≤200`.
Tiempo: 1 segundo; memoria: 64 MB.

## Entrada

Dos enteros `n k`.

## Salida

Un real: la esperanza óptima de población ordinaria restante, no una
probabilidad.

## Evaluación

Los números se comparan con error absoluto o relativo 10⁻⁶.

## Ejemplos

Entrada:

```
4 1
```

Salida:

```
0.6666666667
```

La primera noche convierte `(4,1)` en un día con tres miembros y un
hostil. Excluir uno salva a dos ordinarios con probabilidad `1/3`; en
otro caso la noche elimina al último. La esperanza es `2/3`.

## Solución

### Programación dinámica diurna

Sea `V(N,K)` el óptimo al comenzar el día, antes de excluir. Bases:
`V(N,0)=N`, `V(N,N)=0`. Los conteos bastan aunque las identidades estén
ocultas: si sobreviven ordinarios a una noche, sus muertes revelan el
número hostil restante. Si todos desaparecen, el resultado ya es cero y
no hay decisión futura.

Pruebe conservar `t<N` miembros. El subconjunto es uniforme y su número
hostil `j` tiene distribución hipergeométrica. Con `j=0`, el valor es
`t`; con `t≤2j`, la noche elimina a todos los ordinarios; de otro modo
el día siguiente tiene `t−j` miembros y `j` hostiles.

`P(j)=C(K,j)·C(N−K,t−j)/C(N,t)`

`V(N,K)=max[1≤t<N] Σ[max(0,t−(N−K))≤j≤min(K,⌊(t−1)/2⌋)] P(j)·V(t−j,j)`

El término `j=0` usa `V(t,0)=t`; los omitidos valen cero. Conservar cero
también vale cero y puede omitirse. Calcule por `N` creciente, pues
`t−j<N`, con combinaciones de Pascal. La implementación suma primero el
numerador ponderado y divide una vez por el denominador común `C(N,t)`.

La respuesta inicial es cero si `n≤2k`, o `V(n−k,k)` tras la primera
noche obligatoria. Una mayoría hostil en un estado diurno no implica
cero: `V(2,1)=1/2` al poder excluir al hostil. Tampoco basta excluir
uno: en el día `(5,2)`, conservar tres da `0.6`, pero conservar cuatro
solo `4/15`.

La retención uniforme da la probabilidad indicada y cada composición
tiene el resultado nocturno descrito. Los estados menores ya contienen
la esperanza futura óptima, de modo que condicionar y promediar obtiene
el valor de cada acción permitida. Maximizar sobre todos los tamaños
positivos elige la mejor. La inducción por población demuestra la tabla;
aplicar la noche inicial produce la respuesta. Aleatorizar el número
elegido no supera el máximo de sus valores.

Con `M=n−k`, tiempo `O(M²k²)` y memoria `O(M²+Mk)`. Se omite la tabla si
la primera noche da cero; la entrada máxima requiere unos pocos millones
de términos.

Las combinaciones hasta 200 son menores que `10⁶⁰`, los numeradores
menores que `10⁶²`, sin desbordamiento double. Todas las sumas son no
negativas. Con redondeo estándar, Pascal tiene error relativo
`γ₂₀₀<2.3·10⁻¹⁴`; dos coeficientes, hasta 21 términos y una división dan
una cota conservadora por acción inferior a `10⁻¹³`, aparte del error
previo. Los pesos no negativos suman como máximo uno y el máximo es
1-Lipschitz. En menos de 200 transiciones el error absoluto es menor que
`200((1+10⁻¹³)²⁰⁰−1)<5·10⁻⁹`. Los términos positivos no subdesbordan.
Doce decimales añaden como máximo `5·10⁻¹³`.

## Notas por lenguaje

Las cinco versiones usan la misma DP y double. Java fija la
configuración de salida y Go es compatible con 1.14. Python saca el
denominador del bucle interior. Distinga día y primera noche, admita
exclusiones en grupo y use el límite inferior `max(0,t−(N−K))` si se
conserva más gente que ordinarios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1994_dp_probability.cpp](1994_dp_probability.cpp) | G++ 13.2 x64 | dp, probability | O((n-k)^2 k^2) | AC | 0.015 s | 616 KB |
| [1994_dp_probability.go](1994_dp_probability.go) | Go 1.14 x64 | dp, probability | O((n-k)^2 k^2) | AC | 0.015 s | 1340 KB |
| [1994_dp_probability.java](1994_dp_probability.java) | Java 1.8 | dp, probability | O((n-k)^2 k^2) | AC | 0.125 s | 1968 KB |
| [1994_dp_probability.py](1994_dp_probability.py) | Python 3.12 x64 | dp, probability | O((n-k)^2 k^2) | AC | 0.718 s | 1124 KB |
| [1994_dp_probability.rs](1994_dp_probability.rs) | Rust 1.75 x64 | dp, probability | O((n-k)^2 k^2) | AC | 0.046 s | 428 KB |
