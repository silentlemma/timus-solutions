use std::io::{self, Read};

const WORD: usize = 64;

struct Polygon {
    n: usize,
    xs: Vec<i64>,
    ys: Vec<i64>,
}

impl Polygon {
    fn cross(&self, o: usize, a: usize, b: usize) -> i64 {
        let (xs, ys) = (&self.xs, &self.ys);
        (xs[a] - xs[o]) * (ys[b] - ys[o]) - (ys[a] - ys[o]) * (xs[b] - xs[o])
    }

    fn cross_point(&self, o: usize, ax: i64, ay: i64, b: usize) -> i64 {
        let (xs, ys) = (&self.xs, &self.ys);
        (ax - xs[o]) * (ys[b] - ys[o]) - (ay - ys[o]) * (xs[b] - xs[o])
    }

    /// j lies strictly inside the interior angle of the polygon at i.
    fn in_cone(&self, i: usize, j: usize) -> bool {
        let n = self.n;
        let (prv, nxt) = ((i + n - 1) % n, (i + 1) % n);
        let base = self.cross(i, nxt, prv);
        let (to_next, to_prev) = (self.cross(i, nxt, j), self.cross(i, prv, j));
        if base >= 0 {
            to_next > 0 && to_prev < 0
        } else {
            to_next > 0 || to_prev < 0
        }
    }
}

fn set(b: &mut [u64], k: usize) {
    b[k / WORD] |= 1 << (k % WORD);
}

fn has(b: &[u64], k: usize) -> bool {
    b[k / WORD] >> (k % WORD) & 1 != 0
}

fn clear(b: &mut [u64], k: usize) {
    b[k / WORD] &= !(1 << (k % WORD));
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let n = v[0] as usize;
    let mut xs: Vec<i64> = (0..n).map(|i| v[1 + 2 * i]).collect();
    let mut ys: Vec<i64> = (0..n).map(|i| v[2 + 2 * i]).collect();
    let mut rest = v[2 * n + 1..].iter().copied();
    let mut next = || rest.next().unwrap();
    let (sx1, sy1, sx2, sy2) = (next(), next(), next(), next());
    let mut orig: Vec<usize> = (0..n).collect();
    let area: i64 = (0..n).map(|i| xs[i] * ys[(i + 1) % n] - xs[(i + 1) % n] * ys[i]).sum();
    if area < 0 {
        // counterclockwise from now on
        xs.reverse();
        ys.reverse();
        orig.reverse();
    }
    let poly = Polygon { n, xs, ys };
    let words = n.div_ceil(WORD);
    let last_mask = if n % WORD != 0 { (1u64 << (n % WORD)) - 1 } else { !0 };

    // left[a][b] for a < b: the vertices strictly left of the line a -> b
    let mut pair_index = vec![0usize; n * n];
    let mut pairs = 0;
    for a in 0..n {
        for b in a + 1..n {
            pair_index[a * n + b] = pairs;
            pair_index[b * n + a] = pairs;
            pairs += 1;
        }
    }
    let mut left = vec![0u64; pairs * words];
    for a in 0..n {
        for b in a + 1..n {
            let p = pair_index[a * n + b];
            let bs = &mut left[p * words..(p + 1) * words];
            for k in 0..n {
                if poly.cross(a, b, k) > 0 {
                    set(bs, k);
                }
            }
        }
    }
    // when a comes after b: the complement of the other side, which also
    // counts the points on the line; used only where those cannot occur
    let strictly_left = |a: usize, b: usize, out: &mut [u64]| {
        let p = pair_index[a * n + b];
        let src = &left[p * words..(p + 1) * words];
        for w in 0..words {
            out[w] = if a < b { src[w] } else { !src[w] };
        }
        out[words - 1] &= last_mask;
    };
    // bit k: the vertex is strictly left of edge k -> k + 1
    let mut edge_left = vec![0u64; n * words];
    for vtx in 0..n {
        for k in 0..n {
            if poly.cross(k, (k + 1) % n, vtx) > 0 {
                set(&mut edge_left[vtx * words..(vtx + 1) * words], k);
            }
        }
    }

    // vis[a]: the vertices joined to a by an edge or a diagonal
    let mut vis = vec![0u64; n * words];
    for i in 0..n {
        let j = (i + 1) % n;
        set(&mut vis[i * words..(i + 1) * words], j);
        set(&mut vis[j * words..(j + 1) * words], i);
    }
    let mut hits = vec![0u64; words];
    for i in 0..n {
        for j in i + 2..n {
            if (j + 1) % n == i || !poly.in_cone(i, j) || !poly.in_cone(j, i) {
                continue;
            }
            let p = pair_index[i * n + j];
            let line = &left[p * words..(p + 1) * words];
            let eli = &edge_left[i * words..(i + 1) * words];
            let elj = &edge_left[j * words..(j + 1) * words];
            // edges whose ends lie on different sides of the line, and whose
            // line separates i from j; those touching i or j cannot cross
            for w in 0..words {
                let mut shifted = line[w] >> 1;
                if w + 1 < words {
                    shifted |= line[w + 1] << (WORD - 1);
                }
                hits[w] = (line[w] ^ shifted) & (eli[w] ^ elj[w]);
            }
            clear(&mut hits, n - 1); // edge n - 1 -> 0 wraps around
            if has(line, 0) != has(line, n - 1) && has(eli, n - 1) != has(elj, n - 1) {
                set(&mut hits, n - 1);
            }
            hits[words - 1] &= last_mask;
            for k in [(i + n - 1) % n, i, (j + n - 1) % n, j] {
                clear(&mut hits, k);
            }
            let mut crossing = false;
            'scan: for w in 0..words {
                let mut m = hits[w];
                while m != 0 {
                    let k = w * WORD + m.trailing_zeros() as usize;
                    m &= m - 1;
                    let (d1, d2) = (poly.cross(i, j, k), poly.cross(i, j, (k + 1) % n));
                    if (d1 > 0 && d2 < 0) || (d1 < 0 && d2 > 0) {
                        crossing = true;
                        break 'scan;
                    }
                }
            }
            if crossing {
                continue;
            }
            // no vertex may lie on the open segment
            let (xs, ys) = (&poly.xs, &poly.ys);
            let blocked = (0..n).any(|k| {
                k != i
                    && k != j
                    && poly.cross(i, j, k) == 0
                    && (xs[k] - xs[i]) * (xs[k] - xs[j]) + (ys[k] - ys[i]) * (ys[k] - ys[j]) < 0
            });
            if !blocked {
                set(&mut vis[i * words..(i + 1) * words], j);
                set(&mut vis[j * words..(j + 1) * words], i);
            }
        }
    }

    // bit k: k strictly left of the line a -> s1 (and a -> s2)
    let mut left1 = vec![0u64; n * words];
    let mut left2 = vec![0u64; n * words];
    for a in 0..n {
        for k in 0..n {
            if poly.cross_point(a, sx1, sy1, k) > 0 {
                set(&mut left1[a * words..(a + 1) * words], k);
            }
            if poly.cross_point(a, sx2, sy2, k) > 0 {
                set(&mut left2[a * words..(a + 1) * words], k);
            }
        }
    }
    // a triangle a, b, k counterclockwise whose sides are edges or diagonals,
    // with both ends of S strictly inside and no vertex inside
    let (mut right1, mut right2) = (vec![0u64; words], vec![0u64; words]);
    let (mut cand, mut ab, mut bk, mut ka) =
        (vec![0u64; words], vec![0u64; words], vec![0u64; words], vec![0u64; words]);
    let (xs, ys) = (&poly.xs, &poly.ys);
    let side = |a: usize, b: usize, px: i64, py: i64| {
        (xs[b] - xs[a]) * (py - ys[a]) - (ys[b] - ys[a]) * (px - xs[a])
    };
    for b in 0..n {
        right1.fill(0);
        right2.fill(0);
        for k in 0..n {
            if poly.cross_point(b, sx1, sy1, k) < 0 {
                set(&mut right1, k);
            }
            if poly.cross_point(b, sx2, sy2, k) < 0 {
                set(&mut right2, k);
            }
        }
        for a in 0..n {
            if a == b || !has(&vis[a * words..(a + 1) * words], b) {
                continue;
            }
            if side(a, b, sx1, sy1) <= 0 || side(a, b, sx2, sy2) <= 0 {
                continue;
            }
            for w in 0..words {
                cand[w] = vis[a * words + w]
                    & vis[b * words + w]
                    & left1[a * words + w]
                    & left2[a * words + w]
                    & right1[w]
                    & right2[w];
            }
            clear(&mut cand, a);
            clear(&mut cand, b);
            strictly_left(a, b, &mut ab);
            for w in 0..words {
                let mut m = cand[w];
                while m != 0 {
                    let k = w * WORD + m.trailing_zeros() as usize;
                    m &= m - 1;
                    strictly_left(b, k, &mut bk);
                    strictly_left(k, a, &mut ka);
                    let empty = (0..words).all(|u| {
                        let mut inside = ab[u] & bk[u] & ka[u];
                        for vtx in [a, b, k] {
                            if vtx / WORD == u {
                                inside &= !(1u64 << (vtx % WORD));
                            }
                        }
                        inside == 0
                    });
                    if empty {
                        println!("{} {} {}", orig[a] + 1, orig[b] + 1, orig[k] + 1);
                        return;
                    }
                }
            }
        }
    }
    println!("Impossible");
}
