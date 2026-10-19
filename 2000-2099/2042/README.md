# 2042. Bounded palindromes under substring assignments

[Timus 2042](https://acm.timus.ru/problem.aspx?space=1&num=2042) · difficulty 3248 · strings, segment_tree

Original problem by Nikita Sivukhin, from the Ural FU Dandelion contest, Petrozavodsk training camp, summer 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Maintain a lowercase Latin string under substring assignments. An update
replaces every character in a given inclusive interval by the same
letter. A counting query asks how many palindrome substring occurrences
lie completely inside its interval and have length at most a fixed `k`.
Equal words at different positions are counted separately.

## Input

The first line contains the initial string and `k`, where `1≤n≤100000`
and `1≤k≤50`. The next line contains `1≤m≤100000` operations. Operation
`1 l r c` assigns the lowercase letter `c` to positions `l..r`.
Operation `2 l r` requests the count in that interval. All indices are
one-based, with `1≤l≤r≤n`. The string length and `k` never change. Time
limit: 3 seconds; memory limit: 64 MB.

## Output

Print one integer per counting query, in operation order; if there are
no counting queries, the output is empty. Answers are compared as
integer tokens. This counts pairs of endpoints, not distinct palindrome
values. Each answer is at most `nk≤5000000`.

## Checking

Outputs are compared token by token.

## Examples

```
abacaba 4
3
2 1 3
1 1 3 c
2 1 4
```

```
4
10
```

Initially the first three letters form `aba`. Its three single letters
and its length-three palindrome give `4` occurrences. After assigning
`c` to positions `1..3`, the first four letters are `cccc`. All its
`4+3+2+1=10` substrings have length at most `4` and are palindromes.

## Solution

### A bounded count for each center

Use zero-based indices below. Put `O=(k+1)//2` and `E=k//2`. Let
`odd[i]` be the palindrome radius at character `i`, including the center
and capped at `O`. Let `even[i]` be the radius at the gap immediately
before `i`, capped at `E`. Radius `d` represents `d` different positive
lengths of that parity. Thus `p[i]=odd[i]+even[i]` counts all allowed
occurrences assigned to center index `i`.

Compute these radii with Manacher's algorithm. Its mirror initialization
remains valid with a cap: a mirrored radius below the cap is exact until
the known right boundary, while reaching the cap already gives the
largest allowed answer. Successful new comparisons advance the right
boundary, so each odd or even pass is linear.

Maintain two lazy segment trees: one supports character assignment and
extraction of a short consecutive window; the other supports assignment
and sums of `p`. It also replaces a short consecutive range by
explicitly computed values in one traversal. Replacing its elements by
separate point updates would introduce an unnecessary logarithm.

### Repair only the boundaries of an assignment

Assign characters in `[l,r]` first. A radius can change only when its
largest permitted window intersects that interval. All affected center
indices therefore lie in `A=[l-O+1,r+E]`, clipped to the string. For
centers in `I=[l+E,r-O+1]`, both largest windows lie entirely inside the
assigned interval. Every corresponding substring is constant, so set
`p=k` on this interior.

The rest of `A` consists of at most two short boundary pieces, each of
at most `k-1` centers. If `I` is empty, repair the whole clipped `A`
once; the two nominal pieces can overlap. To repair centers `[u,v]`,
extract characters `[u-E,v+O-1]`, clipped globally, compute their capped
radii and replace exactly those centers. This window contains every
possible allowed palindrome for these centers, so truncation at its
edges cannot remove a valid radius. Its length is `O(k)`, even when the
update itself is long.

### Count inside a query interval

If `r-l+1<k`, extract the whole query and sum its local capped radii.
Otherwise centers in `[l+E,r-O+1]` have all their permitted windows
inside the query; sum their stored `p` values. Remaining centers are
`l..l+E-1` and `r-O+2..r`.

For the left piece, extract the first `k-1` query characters and sum
radii only at its first `E` centers. For the right piece, extract the
last `k-1` characters and sum only its last `O-1` centers. Those windows
contain all relevant palindromes and naturally enforce the query
boundaries. The interior and two pieces partition all center indices,
and each occurrence has one center and parity. Hence the sum counts each
requested occurrence exactly once and includes no occurrence outside the
interval. For `k=1` both pieces are empty and only single letters
remain.

### Bounds and implementation details

After a correct initial build, the assignment argument restores every
changed center and preserves every other center. Induction over
operations gives correct stored values, and the query partition proves
every returned answer. A short window and a bulk replacement cost
`O(k+log n)`; a long constant interior needs only a lazy assignment.
Total time is `O(n+m(k+log n))` and storage is `O(n)`.

Python uses a different invariant: `s[i]` and `e[i]` count allowed
palindromes starting and ending at position `i`. Its intervals below are
half-open. A scan keeps a machine-word mask whose bit `d` represents a
palindrome of length `d+1` ending at the current position. Shift the
previous mask by two, insert the length-one and length-two candidates,
and intersect with the mask of matching letter positions. The latter
mask has bit `d` set exactly when the character `d` positions back
matches. Thus each longer candidate survives exactly when its inner
substring is a palindrome and its outer letters agree. Discard lengths
above `k`; a small population-count table gives `e[i]`. Per-letter
histories advance by the distance since that letter last appeared.
Scanning the reversed window gives `s[i]`.

Uniform windows have endpoint counts `min(k,t)`, where `t` is the number
of characters available toward the corresponding edge. Short windows
with two or three maximal constant runs also admit direct counts,
starting with the counts inside each run. A two-run window has no
palindrome using both letters. With three runs, a palindrome using
different letters must contain the whole middle run and equally many
letters from matching outer runs; add exactly the extensions that fit
both outer runs and the length bound. Other windows use the mask scan.
Bounded exact caches reuse short byte strings and their immutable
endpoint counts or query totals, so a cache hit changes no result.

For a query shorter than `k-1`, every substring already satisfies the
length bound. Count the substrings inside each constant run by its
triangular number, then expand symmetrically around each whole run. Any
palindrome using different letters has exactly one such central run, so
this counts every occurrence once. If the expansion work exceeds a
linear budget, discard the partial total and use the mask scan instead.
This keeps the short-query calculation linear.

Characters and endpoint counts live in bytearrays split into fixed-size
blocks, with a lazy segment tree over block sums. The starting and
ending sums occupy separate fields of one integer; each field can hold
the full possible sum, so additions cannot carry between them. A paint
tags whole blocks with their new letter and provisionally sets both
endpoint counts to `k`. Materialize a tagged block before reading its
characters or partially editing it. Counts equal `k` wherever all
allowed lengths fit inside the painted run; repair the remaining
affected counts in `O(k)` windows at its edges, merging the windows when
they overlap. Any changed palindrome must meet the paint and has length
at most `k`, so these windows contain every needed character and all
other counts remain valid. Recompute sums only for the repaired blocks.

For a query `[l,r)` of length at least `k-1`, return
`sum(e[0:r])-sum(s[0:l])` using two tree prefix sums. Every allowed
palindrome starting before `l` also ends before `r`, since its length is
at most `k`. Subtraction therefore cancels exactly the occurrences
outside the query on the left; the remainder lies wholly inside. A
whole-string query uses the stored total directly.

Paints are deferred until a query needs the endpoint structure. Before
its first use, apply the pending paints to the characters and build the
counts only once. Later batches can omit a paint fully covered by later
paints: only the final characters matter to the next unresolved query. A
backward scan records coverage from long paints only; ignoring shorter
paints can miss a redundant write but cannot remove one that is still
needed. Larger batches of short paints write the characters in order,
trimming prefixes and suffixes already equal to the new letter. An
actual change on `[l,r)` can affect ending counts only in `[l,r+k-1)`
and starting counts only in `[l-k+1,r)`, clipped globally. Sort and
merge nearby affected intervals, extend each by the needed `k-1` context
characters, and recompute each merged region once from the final string.
This is exact even for overlapping paints because all repairs see the
final characters. Other batches use the individual boundary repairs.
Paints after the last query need no processing.

Some queries need no repairs at all. Besides the most recent painted
interval, Python tracks one interval known to be uniform, joining
overlapping or adjacent paints of the same letter or keeping a new paint
or a surviving uniform piece. These choices preserve the guarantee that
every character in the tracked interval is equal. A query contained in
either known uniform interval has answer `dL-d(d-1)/2`, where `L` is its
length and `d=min(k,L)`: sum `L-j+1` occurrences for each length `j`
from one to `d`. For `k=1`, every query has this answer regardless of
characters. Such queries leave pending paints deferred.

The Python bound also includes work outside the tree. Let `B` be its
fixed block width, which is at least `k`. A single paint can write
`O(n/B)` block markers and repair `O(B+k)` characters; tree paths cost
`O(log n)`. Maintaining the covered-interval union when filtering a
batch can likewise visit `O(n/B+1)` pieces under the fixed thresholds.
Sorting affected intervals adds at most `O(m log m)` over all batches. A
conservative total bound is `O(n+m(n/B+B+k+log n+log m))` time. Stored
characters, counts and trees use `O(n)` space; buffered input, pending
paints and answers bring total storage to `O(n+m)`. These costs differ
from the center-based bound above.

Keep the even center before `i`, not after it. Clip global windows,
merge overlapping repair pieces, and distinguish a radius from a
substring length. Count occurrences, including every single letter.
Handle `k>n` and empty output. Restore a block's lazy value before a
partial edit. Do not perform `k` independent tree point updates when one
bulk replacement suffices.

## Language notes

C++, Go and Rust use flat arrays and logarithmic tree recursion. Rust
uses saturating arithmetic for clipped left bounds and empty interiors.
Go 1.14 uses buffered output and its own integer parser. Java 8 reuses
short-window, radius and replacement buffers to limit allocations.
Python uses endpoint masks, a lazy block tree and deferred boundary
repairs. Counts fit signed 32 bits; Rust stores sums in unsigned 32-bit
integers. All versions convert input indices once.

The current Python solution runs under PyPy and was Accepted on Timus
with PyPy 3.10 x64 in 2.39 s, using 26 300 KB, within the 3 s limit.
Earlier versions exceeded the time limit on judge test 9 under CPython
and tests 14 and 17 under PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2042_strings_segment_tree.cpp](2042_strings_segment_tree.cpp) | G++ 13.2 x64 | strings, segment_tree | O(n+m(k+log n)) | AC | 0.781 s | 2980 KB |
| [2042_strings_segment_tree.go](2042_strings_segment_tree.go) | Go 1.14 x64 | strings, segment_tree | O(n+m(k+log n)) | AC | 0.921 s | 16428 KB |
| [2042_strings_segment_tree.java](2042_strings_segment_tree.java) | Java 1.8 | strings, segment_tree | O(n+m(k+log n)) | AC | 0.890 s | 8844 KB |
| [2042_strings_segment_tree.py](2042_strings_segment_tree.py) | PyPy 3.10 x64 | strings, segment_tree | O(n+m(n/B+B+k+log n+log m)) | AC | 2.390 s | 26300 KB |
| [2042_strings_segment_tree.rs](2042_strings_segment_tree.rs) | Rust 1.75 x64 | strings, segment_tree | O(n+m(k+log n)) | AC | 0.640 s | 5788 KB |
