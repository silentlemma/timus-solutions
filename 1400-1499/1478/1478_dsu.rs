use std::collections::HashMap;
use std::io::{self, Read, Write};

const INDEX_BITS: u32 = 10; // edges are packed as length, then both indices
const INDEX_MASK: i64 = (1 << INDEX_BITS) - 1;
const WORD_BITS: usize = 64;

/// Counts are bit sets: bit k says that k bases are possible; res |= a << k.
fn or_shifted(res: &mut [u64], a: &[u64], k: usize) {
    let (words, bits) = (k / WORD_BITS, k % WORD_BITS);
    for i in (words..res.len()).rev() {
        let mut v = a[i - words] << bits;
        if bits > 0 && i > words {
            v |= a[i - words - 1] >> (WORD_BITS - bits);
        }
        res[i] |= v;
    }
}

fn find(parent: &mut [usize], mut x: usize) -> usize {
    while parent[x] != x {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    x
}

fn solve(xs: &[i64], ys: &[i64]) -> String {
    let n = xs.len();
    let dist = |a: usize, b: usize| (xs[a] - xs[b]).pow(2) + (ys[a] - ys[b]).pow(2);
    let mut edges = Vec::with_capacity(n * n / 2);
    for i in 0..n {
        for j in i + 1..n {
            edges.push(dist(i, j) << (2 * INDEX_BITS) | (i as i64) << INDEX_BITS | j as i64);
        }
    }
    edges.sort_unstable();

    // the single-linkage tree: nodes 0 .. n-1 are the objects, then each
    // component formed after a group of equal distances is a new node
    let mut kids: Vec<Vec<usize>> = vec![Vec::new(); n];
    let mut width = vec![0i64; n];
    let mut out: Vec<Option<i64>> = vec![None; n];
    let mut parent: Vec<usize> = (0..n).collect();
    let mut members: Vec<Vec<usize>> = (0..n).map(|i| vec![i]).collect();
    let mut comp_width = vec![0i64; n];
    let mut comp_node: Vec<usize> = (0..n).collect();
    let mut e = 0;
    while e < edges.len() {
        let w = edges[e] >> (2 * INDEX_BITS);
        let mut grown: HashMap<usize, Vec<usize>> = HashMap::new(); // root -> swallowed nodes
        while e < edges.len() && edges[e] >> (2 * INDEX_BITS) == w {
            let a = (edges[e] >> INDEX_BITS & INDEX_MASK) as usize;
            let b = (edges[e] & INDEX_MASK) as usize;
            e += 1;
            let (ra, rb) = (find(&mut parent, a), find(&mut parent, b));
            if ra == rb {
                continue;
            }
            let mut far = comp_width[ra].max(comp_width[rb]);
            for &p in &members[ra] {
                for &q in &members[rb] {
                    far = far.max(dist(p, q));
                }
            }
            parent[rb] = ra;
            let moved = std::mem::take(&mut members[rb]);
            members[ra].extend(moved);
            comp_width[ra] = far;
            let mut swallowed = grown.remove(&ra).unwrap_or_else(|| vec![comp_node[ra]]);
            match grown.remove(&rb) {
                Some(more) => swallowed.extend(more),
                None => swallowed.push(comp_node[rb]),
            }
            grown.insert(ra, swallowed);
        }
        for (root, swallowed) in grown {
            for &c in &swallowed {
                out[c] = Some(w);
            }
            comp_node[root] = kids.len();
            kids.push(swallowed);
            width.push(comp_width[root]);
            out.push(None);
        }
    }

    // a node can be a base when it is narrower than its distance to the rest
    let size = (n + WORD_BITS) / WORD_BITS;
    let mut all: Vec<Vec<u64>> = Vec::with_capacity(kids.len());
    for v in 0..kids.len() {
        let mut mask = vec![0u64; size];
        if out[v].map_or(true, |o| width[v] < o) {
            mask[0] |= 1 << 1;
        }
        if !kids[v].is_empty() {
            let mut total = vec![0u64; size];
            total[0] = 1;
            for &c in &kids[v] {
                let mut combined = vec![0u64; size];
                for k in 1..=n {
                    if all[c][k / WORD_BITS] >> (k % WORD_BITS) & 1 == 1 {
                        or_shifted(&mut combined, &total, k);
                    }
                }
                total = combined;
            }
            for i in 0..size {
                mask[i] |= total[i];
            }
        }
        all.push(mask);
    }
    let root = all.last().unwrap();
    (1..=n)
        .map(|k| {
            if root[k / WORD_BITS] >> (k % WORD_BITS) & 1 == 1 {
                '1'
            } else {
                '0'
            }
        })
        .collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let mut out = String::new();
    while let Some(n) = it.next() {
        if n == 0 {
            break;
        }
        let mut xs = Vec::new();
        let mut ys = Vec::new();
        for _ in 0..n {
            xs.push(it.next().unwrap());
            ys.push(it.next().unwrap());
        }
        out.push_str(&solve(&xs, &ys));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
