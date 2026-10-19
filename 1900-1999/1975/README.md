# 1975. Counting Rotations of Marked Sphere Points

[Timus 1975](https://acm.timus.ru/problem.aspx?space=1&num=1975) · difficulty 4173 · geometry

Original problem by Denis Dublennykh, from the Ural Sport Programming Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A unit sphere centered at the origin has n marked points. Count proper
three-dimensional rotations about its center that send every mark within
Euclidean distance 10⁻⁶ of a mark. Include the identity. Rotations inducing
the same point permutation count once; reflections are excluded. Limits:
1 second and 64 MB.

## Input

The first line is n, 3≤n≤200. Each following line gives one point's x, y, z
coordinates, with at most nine digits after the decimal point. Points lie
on the unit sphere; the distance between distinct points is at least 10⁻⁵.
Retain the input coordinates when measuring residuals; normalization is
only for choosing directions and orthonormal frames.

## Output

One integer: the number of distinct attainable point permutations.

## Checking

Outputs are compared token by token.

## Examples

```
3
0 1 0
1 0 0
0 0 1
```

```
3
```

## Solution

### Enumerate well-conditioned image frames

Write ε=10⁻⁶. Choose the first unit direction a and another direction b
maximizing s=|a×b|. There are at least three separated marks, so s is
positive, even when all marks nearly lie on one axis. Use the right-handed
basis z=a, y=(a×b)/s, x=y×z. Express the original, unnormalized points in
this basis.

Try each ordered pair of distinct target marks P,Q. A rotation changes
neither angles nor orientation. Let e=ε/min|point| and η=2 asin(e/2).
The angle β between P,Q must differ from α=angle(a,b) by at most 2η.
Cheap sine and cosine bounds reject most pairs first. Their extra 10⁻¹²
slack is only a necessary-condition filter, never the acceptance distance.

The target basis defines a proper canonical rotation R₀ taking a exactly
to P and b to Q's azimuth. It need not itself meet the tolerance. A feasible
rotation is T H R₀, where T tilts P by at most η and H twists around P by θ.
If t=sin β, then |sin(θ/2)|≤e/√(st). Every source point has transverse
radius at most s. Its canonical image is therefore within
ε+rmax·e·(1+2√(s/t)) of its true target. The separation bound gives
s≥approximately 5·10⁻⁶ and t≥s−2e, making this distance below 5ε,
including nine-decimal input rounding.

Consequently the nearest mark within 5ε is exactly the required target.
Hash points into cubes of side 10ε, adding each to the 27 adjacent buckets;
one bucket lookup then finds all possible targets of each canonical image.
Reject absent or repeated targets. Store accepted permutations to avoid
counting the same rearrangement twice.

### Verify a proper rotation, not just its canonical frame

For a fixed permutation, check the actual maximum residual. For example,
the points (1,0,0), (−δ,1,0), (−1,0,0), (δ,−1,0), with δ=0.9ε, admit
the quarter-turn although the canonical frame can have error 1.8ε. A
canonical-only test would lose valid permutations. Least squares alone is
also insufficient: minimizing the sum does not minimize the largest error.

First try a scaled three-variable rotation update, then weighted
least-squares updates. Axial scaling by s keeps polar clusters numerically
conditioned. Compose updates as one normalized quaternion and reapply it
to the original points. Accept only an explicit proper rotation whose
every residual is within ε plus the stated roundoff guard.

A failed fit is not a rejection. Pair-angle inequalities may prove the
permutation impossible. A second certificate uses nonnegative weights wᵢ,
current rotated points pᵢ and targets qᵢ. Put F=Σwᵢ|pᵢ−qᵢ|²,
g=Σwᵢ pᵢ×(qᵢ−pᵢ), and
H=Σwᵢ[(pᵢ·qᵢ)I−(pᵢqᵢᵀ+qᵢpᵢᵀ)/2]. If a conservative lower bound
λ on H's smallest eigenvalue is positive, every rotation has weighted
error at least F−|g|²/λ. Reject only if this exceeds ε²Σwᵢ with conservative
roundoff allowances. Jacobi rotations and Gershgorin bounds supply λ.

### Complete search when the fast certificates do not decide

In the target frame parameterize T by its new axis direction
(u,v,1)/√(1+u²+v²). All feasible rotations occur in the box
|u|,|v|≤tan η, |θ|≤2 asin(min(1,e/√(st))). After twisting a point to
(x,y,z), set c=1/√(1+u²+v²), d=ux+vy and h=cz−c²d/(1+c).
Its tilted coordinates are (x+uh,y+vh,c(z−d)); this remains a proper rotation.

For box half-widths hu,hv,hθ, a point of norm r and transverse radius ρ
moves from its center image by at most 2r√(hu²+hv²)+ρhθ. Discard the box
if any center residual minus this bound exceeds ε plus 10⁻¹⁶. Otherwise
accept a valid center witness or split the parameter with largest scaled
half-width. A priority queue examines the smallest residual lower bound
first. There is no node cap or acceptance of an unresolved cell. Once
the motion bound is below a quarter of the witness guard, an unpruned
center must already pass. This handles the floating-point boundary without
silently increasing the geometric tolerance to the 5ε matching gate.

Every valid permutation supplies one enumerated anchor pair; the 5ε bound
recovers its exact targets and the parameter box contains its rotation.
Every accepted permutation has an explicit proper witness. Necessary
conditions and conservative box bounds discard only infeasible choices.
These facts prove completeness and soundness, subject to the stated
binary64 roundoff band.

In the example the identity and two cyclic permutations of the positive
coordinate axes are proper rotations, giving 3. The other three axis
permutations reverse orientation and must not be counted.

For total B visited search boxes, time is `O(n³+nB+B log(B+1))`, because
each of at most n(n−1) candidates costs linear work before subdivision.
With A accepted permutations and H live boxes, space is `O(n²+nA+H)`.
Subdivision is adaptive and can be exponential; the bound does not claim
uniform polynomial worst-case time for tolerance feasibility.

Do not include reflections, assume approximate symmetries form a group,
or substitute an exact frame or a least-squares failure for feasibility.
Use cross products for nearly parallel axes, raw points for distances,
and the stricter ε bound for final witnesses. Never reject just because
an optimization iteration limit was reached; continue with certified search.

## Language notes

All five programs implement the same frame enumeration and certified
refinement using their standard libraries. Python's first update uses
Rodrigues' formula; the compiled versions use a quaternion. Subsequent
updates use normalized quaternions throughout. C++ accumulates certificate
sums in long double; Go, Java and Rust use compensated sums, and Python
uses math.fsum. These improve certificate rounding without changing ε.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1975_geometry.cpp](1975_geometry.cpp) | G++ 13.2 x64 | geometry | O(n^3+n*B+B log(B+1)) | AC | 0.046 s | 1012 KB |
| [1975_geometry.go](1975_geometry.go) | Go 1.14 x64 | geometry | O(n^3+n*B+B log(B+1)) | AC | 0.031 s | 4212 KB |
| [1975_geometry.java](1975_geometry.java) | Java 1.8 | geometry | O(n^3+n*B+B log(B+1)) | AC | 0.171 s | 6952 KB |
| [1975_geometry.py](1975_geometry.py) | Python 3.12 x64 | geometry | O(n^3+n*B+B log(B+1)) | AC | 0.312 s | 3712 KB |
| [1975_geometry.rs](1975_geometry.rs) | Rust 1.75 x64 | geometry | O(n^3+n*B+B log(B+1)) | AC | 0.046 s | 1620 KB |
