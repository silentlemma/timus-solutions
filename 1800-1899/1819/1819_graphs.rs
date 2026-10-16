use std::collections::HashMap;
use std::io::{self, Read, Write};

// splitmix64 with a fixed seed
const SEED: u64 = 2010;
const GAMMA: u64 = 0x9e3779b97f4a7c15;
const MIX1: u64 = 0xbf58476d1ce4e5b9;
const MIX2: u64 = 0x94d049bb133111eb;
const SHIFT1: u32 = 30;
const SHIFT2: u32 = 27;
const SHIFT3: u32 = 31;

struct SplitMix(u64);

impl SplitMix {
    fn next(&mut self) -> u64 {
        self.0 = self.0.wrapping_add(GAMMA);
        let mut z = self.0;
        z = (z ^ (z >> SHIFT1)).wrapping_mul(MIX1);
        z = (z ^ (z >> SHIFT2)).wrapping_mul(MIX2);
        z ^ (z >> SHIFT3)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<usize>().unwrap());
    let (n, k) = match (it.next(), it.next()) {
        (Some(n), Some(k)) => (n, k),
        _ => return,
    };
    const NONE: usize = usize::MAX;
    // half-edge h runs from ends[h] to ends[h ^ 1], and the half-edges of
    // a vertex are chained through head and nxt
    let mut ends = vec![0; 2 * k];
    let mut head = vec![NONE; n];
    let mut nxt = vec![NONE; 2 * k];
    for h in 0..2 * k {
        ends[h] = it.next().unwrap() - 1;
        nxt[h] = head[ends[h]];
        head[ends[h]] = h;
    }
    let mut comp = vec![NONE; n];
    let mut tin = vec![0; n];
    let mut parent = vec![NONE; n];
    let mut up_edge = vec![NONE; n];
    let mut order = Vec::with_capacity(n);
    let mut stack = Vec::with_capacity(n);
    let mut iter = head.clone();
    for root in 0..n {
        if comp[root] != NONE {
            continue;
        }
        comp[root] = root;
        tin[root] = order.len();
        order.push(root);
        stack.push(root);
        while let Some(&v) = stack.last() {
            let h = iter[v];
            if h == NONE {
                stack.pop();
                continue;
            }
            iter[v] = nxt[h];
            let w = ends[h ^ 1];
            if comp[w] == NONE {
                comp[w] = root;
                parent[w] = v;
                up_edge[w] = h >> 1;
                tin[w] = order.len();
                order.push(w);
                stack.push(w);
            }
        }
    }
    let mut rng = SplitMix(SEED);
    // every non-tree edge joins a vertex and its ancestor; mark it with a
    // random value at both ends, so after summing over subtrees the edge
    // above v carries the xor of the non-tree edges passing over it
    let mut cover = vec![0u64; n];
    let mut count = vec![0i64; n];
    for e in 0..k {
        let (mut a, mut b) = (ends[2 * e], ends[2 * e + 1]);
        if up_edge[a] == e || up_edge[b] == e {
            continue;
        }
        if tin[a] < tin[b] {
            std::mem::swap(&mut a, &mut b);
        }
        let r = rng.next();
        cover[a] ^= r;
        cover[b] ^= r;
        count[a] += 1;
        count[b] -= 1;
    }
    for &v in order.iter().rev() {
        let p = parent[v];
        if p != NONE {
            cover[p] ^= cover[v];
            count[p] += count[v];
        }
    }
    // a pair of edges is a cut exactly when it is a tree edge covered by
    // nothing but that non-tree edge, or two tree edges covered by the same
    // set; give tree edges values so that a path xors to zero iff it crosses no cut
    let mut value = vec![0u64; n];
    let mut first: HashMap<u64, usize> = HashMap::with_capacity(n);
    for &v in &order {
        if parent[v] == NONE {
            continue;
        }
        if count[v] < 2 {
            // a bridge or an edge with one cover: crossing it separates
            value[v] = rng.next();
            continue;
        }
        // edges with one cover set lie on a chain and cut the tree into
        // pieces closed into a ring; a path inside the ring crosses all of
        // them or none of them, so the class must xor to zero
        let rep = *first.entry(cover[v]).or_insert(v);
        if rep != v {
            value[v] = rng.next();
            value[rep] ^= value[v];
        }
    }
    let mut label = vec![0u64; n];
    for &v in &order {
        if parent[v] != NONE {
            label[v] = label[parent[v]] ^ value[v];
        }
    }
    let q = it.next().unwrap();
    let mut out = String::new();
    for _ in 0..q {
        let a = it.next().unwrap() - 1;
        let b = it.next().unwrap() - 1;
        out.push_str(if comp[a] == comp[b] && label[a] == label[b] { "Yes\n" } else { "No\n" });
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
