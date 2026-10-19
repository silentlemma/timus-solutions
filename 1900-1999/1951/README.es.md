# 1951. Contar raíces complejas compatibles

[Timus 1951](https://acm.timus.ru/problem.aspx?space=1&num=1951) · difficulty 1789 · number_theory

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Olga Soboleva).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Contar los complejos x que satisfacen xⁿ=A=a+bi y xᵐ=C=c+di a la vez,
con i²=−1. Los cuatro coeficientes son enteros, ambos lados derechos son
no nulos y los exponentes positivos. Límites: 1 segundo y 64 MB.

## Entrada

Primera línea a,b,n; segunda c,d,m.
−10¹⁸≤a,b,c,d≤10¹⁸ inclusive, 1≤n,m≤100.
Al menos uno de a,b y al menos uno de c,d es no nulo.

## Salida

Un entero: la cantidad de raíces complejas comunes.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
0 1 2
1 0 2
```

```
0
```

```
1 0 2
1 0 4
```

```
2
```

## Solución

Sea g=gcd(n,m), p=n/g, q=m/g, con gcd(p,q)=1. La respuesta es g si
A^q=C^p y cero si no. La necesidad sale de elevar las ecuaciones a q y p.
Para suficiencia, elegir enteros u,v con up+vq=1 y poner Y=A^u C^v.
Las potencias negativas existen porque A,C no son cero. La compatibilidad
da Y^p=A e Y^q=C. Toda raíz de x^g=Y satisface ambas ecuaciones y toda
raíz común cumple x^g=A^u C^v. Un Y complejo no nulo tiene exactamente
g raíces g-ésimas distintas, demostrando el recuento.

Comparar exactamente las potencias gaussianas mediante residuos. Cribar
primos hasta L=10000 y tomar los primeros K=510 no menores que 5000.
Hay 560 en ese intervalo; la lista elegida va de 5003 a 9521. Normalizar
ambas coordenadas, usar exponenciación binaria y compararlas para cada
módulo. Una diferencia da cero raíces; si coinciden todas, devolver g.

Es determinista. Cada coordenada de Z^e tiene valor absoluto como máximo
(|Re Z|+|Im Z|)^e. La suma de valores absolutos de entrada es
≤2·10¹⁸<2⁶¹ y p,q≤100. Cada diferencia D entre coordenadas de A^q y C^p
cumple |D|<2·(2·10¹⁸)^100<2⁶¹⁰¹. Cada primo elegido supera
4096=2¹²; su producto P>2^(510·12)=2⁶¹²⁰>|D|. Residuos iguales hacen
que todos los primos distintos dividan D, luego P divide D. Solo cero
cumple eso con |D|<P. Aplicarlo a ambas coordenadas prueba igualdad exacta,
sin estimar probabilidades de colisión.

La multiplicación modular de pares es (r₁r₂−i₁i₂, r₁i₂+i₁r₂), reduciendo
los resultados. Es un homomorfismo de anillos; el anillo gaussiano residual
no necesita ser un cuerpo, pues no hay divisiones ni inversos modulares.

O(L log log L + K log E) tiempo y O(L) espacio, E=max(n,m), L=10000,
K=510. Construir la criba una vez. Con L,K fijos por los límites, la
comparación tarda O(log E) y usa almacenamiento fijo.

Reducir exponentes por g: Aᵐ=Cⁿ puede valer sin raíces comunes. Importan
ambas coordenadas, fase y signos. Módulos o ángulos flotantes no prueban
igualdad. Pocos primos no bastan; la cota completa del producto es esencial.
No suponer que el anillo residual gaussiano es un cuerpo ni olvidar la
garantía de valores no nulos.

## Notas por lenguaje

Leer coeficientes con signo de 64 bits en versiones nativas. Antes de
multiplicar, normalizar restos negativos a 0..prime−1. Los valores
intermedios normalizados tienen módulo <2·9999²<2³¹−1; aun así las
versiones usan 64 bits. No multiplicar coeficientes originales de 10¹⁸.
Solo biblioteca estándar. Python/C++/Go/Java conservan una lista de módulos;
Rust la construye una vez y la pasa a la comparación.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1951_number_theory.cpp](1951_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log max(n,m)) | AC | 0.015 s | 412 KB |
| [1951_number_theory.go](1951_number_theory.go) | Go 1.14 x64 | number_theory | O(log max(n,m)) | AC | 0.046 s | 1096 KB |
| [1951_number_theory.java](1951_number_theory.java) | Java 1.8 | number_theory | O(log max(n,m)) | AC | 0.156 s | 708 KB |
| [1951_number_theory.py](1951_number_theory.py) | Python 3.12 x64 | number_theory | O(log max(n,m)) | AC | 0.093 s | 688 KB |
| [1951_number_theory.rs](1951_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log max(n,m)) | AC | 0.046 s | 244 KB |
