# 1975. Conteo de rotaciones de puntos marcados en una esfera

[Timus 1975](https://acm.timus.ru/problem.aspx?space=1&num=1975) · dificultad 4173 · geometry

Problema original de Denis Dublennykh, del Campeonato de Programación Deportiva de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una esfera unitaria centrada en el origen tiene n puntos marcados. Contar
las rotaciones propias alrededor del centro que dejan cada imagen a
distancia euclídea no mayor que 10⁻⁶ de alguna marca. La identidad cuenta.
Dos rotaciones que producen la misma permutación cuentan una sola vez;
las reflexiones se excluyen. Límites: 1 segundo y 64 MB.

Excluir reflexiones y no suponer que las simetrías aproximadas forman
un grupo. Una base exacta fallida o un ajuste cuadrático fallido no
demuestran imposibilidad. Usar productos vectoriales cerca de ejes
paralelos, coordenadas originales para distancias y ε para los testigos.
Al agotar las iteraciones rápidas, continuar con búsqueda certificada.

## Entrada

La primera línea contiene n, 3≤n≤200. Las siguientes n líneas dan las
coordenadas x, y, z de puntos de la esfera unitaria, con un máximo de
nueve cifras decimales. Dos puntos diferentes distan al menos 10⁻⁵.
Conservar las coordenadas originales al medir errores; normalizar sólo
para construir direcciones y bases ortonormales.

## Salida

Un entero: el número de permutaciones realizables por rotaciones válidas.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3
0 1 0
1 0 0
0 0 1
```

```
3
```

## Solución

### Enumerar imágenes de una pareja bien condicionada

Sea ε=10⁻⁶. Elegir la primera dirección unitaria a y otra b que maximice
s=|a×b|. Tres marcas separadas garantizan s>0, incluso cerca de un mismo
eje. Construir la base dextrógira z=a, y=(a×b)/s, x=y×z, y expresar en
ella los puntos originales sin normalizarlos.

Probar cada pareja ordenada de destinos diferentes P,Q. Si e=ε/min|point|
y η=2 asin(e/2), el ángulo destino β debe diferir del ángulo fuente α
a lo sumo en 2η. Primero se filtran diferencias de senos y cosenos.
El margen adicional 10⁻¹² pertenece sólo a estas condiciones necesarias,
nunca a la distancia de aceptación.

La base destino define una rotación propia canónica R₀ que lleva a
exactamente a P y b al azimut de Q. Toda rotación válida es T H R₀:
T inclina P como máximo η y H gira alrededor de P un ángulo θ. Con
t=sin β se cumple |sin(θ/2)|≤e/√(st). El radio transversal de cualquier
punto fuente no supera s, así que su imagen canónica dista del destino
real a lo sumo ε+rmax·e·(1+2√(s/t)). La separación mínima implica
s≥aproximadamente 5·10⁻⁶ y t≥s−2e. La cota queda por debajo de 5ε,
incluso considerando el redondeo de nueve decimales.

Por tanto, la marca más cercana dentro de 5ε es precisamente el destino
correcto: otras marcas están separadas al menos 10ε. Usar un hash espacial
de cubos de lado 10ε y añadir cada marca a las 27 cubetas vecinas.
Una consulta por imagen encuentra todos sus destinos posibles. Rechazar
destinos ausentes o repetidos y guardar las permutaciones aceptadas en
un conjunto para no contarlas dos veces.

### Verificar una rotación, no sólo la base canónica

Los puntos (1,0,0), (−δ,1,0), (−1,0,0), (δ,−1,0), con δ=0.9ε,
admiten un cuarto de vuelta, aunque la base canónica puede producir
error 1.8ε. Comprobar sólo R₀ perdería respuestas. Tampoco basta el
mínimo cuadrático: minimizar la suma no minimiza el mayor error.

Probar primero una corrección de tres parámetros y después mínimos
cuadrados ponderados. Escalar el parámetro axial por s mejora el
condicionamiento cerca de los polos. Componer las correcciones en un
cuaternión normalizado y aplicarlo siempre a los puntos originales.
Aceptar únicamente un testigo explícito propio cuyos errores individuales
no superen ε más la protección de redondeo indicada.

Una iteración fallida no demuestra imposibilidad. Las desigualdades entre
ángulos pueden excluir una permutación. Otro certificado emplea pesos
wᵢ≥0, imágenes actuales pᵢ y destinos qᵢ. Definir F=Σwᵢ|pᵢ−qᵢ|²,
g=Σwᵢ pᵢ×(qᵢ−pᵢ) y
H=Σwᵢ[(pᵢ·qᵢ)I−(pᵢqᵢᵀ+qᵢpᵢᵀ)/2]. Si λ>0 es una cota inferior
conservadora del menor autovalor de H, toda rotación tiene error ponderado
al menos F−|g|²/λ. Rechazar sólo si supera ε²Σwᵢ conservando margen
de redondeo. Rotaciones de Jacobi y cotas de Gershgorin proporcionan λ.

### Subdivisión completa para los casos restantes

En la base destino parametrizar la inclinación por la nueva dirección
del eje (u,v,1)/√(1+u²+v²). Toda solución está en
|u|,|v|≤tan η, |θ|≤2 asin(min(1,e/√(st))). Después del giro axial,
sea (x,y,z) el punto; calcular c=1/√(1+u²+v²), d=ux+vy,
h=cz−c²d/(1+c). La imagen inclinada es (x+uh,y+vh,c(z−d)), todavía
producida por una rotación propia.

Para semianchos hu,hv,hθ, un punto de norma r y radio transversal ρ
se mueve respecto de la imagen del centro como máximo
2r√(hu²+hv²)+ρhθ. Descartar la caja si algún error del centro menos
esta cota supera ε+10⁻¹⁶. Si no, verificar el centro o dividir el
parámetro con mayor semiancho escalado. La cola de prioridad visita
primero la menor cota inferior de error. No hay límite de nodos ni
aceptación de cajas sin resolver. Cuando la cota de movimiento es menor
que un cuarto de la protección de redondeo, un centro no descartado ya
debe ser un testigo válido. Así se evita confundir el radio 5ε de
emparejamiento con la tolerancia final.

Cada permutación válida aporta una pareja de imágenes enumerada; la
cota 5ε recupera todos sus destinos y la caja contiene su rotación.
Cada aceptación tiene un testigo propio explícito. Las condiciones
necesarias y las cotas conservadoras sólo eliminan elecciones imposibles.
Esto prueba completitud y corrección con la banda binary64 declarada.

En el ejemplo sirven la identidad y las dos permutaciones cíclicas
de los ejes positivos. Las otras tres invierten la orientación.
Por ello el resultado es 3.

Con B cajas visitadas en total, el tiempo es `O(n³+nB+B log(B+1))`:
cada uno de los como máximo n(n−1) candidatos usa trabajo lineal antes
de subdividir. Con A permutaciones aceptadas y H cajas vivas, el espacio
es `O(n²+nA+H)`. La subdivisión es adaptativa y puede ser exponencial;
no se afirma una cota polinómica uniforme para la factibilidad con tolerancia.

## Notas por lenguaje

Las cinco versiones usan bibliotecas estándar y la misma búsqueda
completa. Python emplea Rodrigues en la primera corrección; las versiones
compiladas emplean cuaterniones. Las correcciones siguientes siempre usan
cuaterniones normalizados. C++ acumula certificados en long double;
Go, Java y Rust usan sumas compensadas, y Python usa math.fsum. Estas
medidas reducen el redondeo sin modificar ε.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1975_geometry.cpp](1975_geometry.cpp) | G++ 13.2 x64 | geometry | O(n^3+n*B+B log(B+1)) | AC | 0.046 s | 1012 KB |
| [1975_geometry.go](1975_geometry.go) | Go 1.14 x64 | geometry | O(n^3+n*B+B log(B+1)) | AC | 0.031 s | 4212 KB |
| [1975_geometry.java](1975_geometry.java) | Java 1.8 | geometry | O(n^3+n*B+B log(B+1)) | AC | 0.171 s | 6952 KB |
| [1975_geometry.py](1975_geometry.py) | Python 3.12 x64 | geometry | O(n^3+n*B+B log(B+1)) | AC | 0.312 s | 3712 KB |
| [1975_geometry.rs](1975_geometry.rs) | Rust 1.75 x64 | geometry | O(n^3+n*B+B log(B+1)) | AC | 0.046 s | 1620 KB |
