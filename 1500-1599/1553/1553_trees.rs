use std::io::{self, Read, Write};

/// A segment tree of maxima over the places of the chains.
struct Maxima {
    width: usize,
    tree: Vec<i64>,
}

impl Maxima {
    fn add(&mut self, at: usize, v: i64) {
        let mut i = at + self.width;
        self.tree[i] += v;
        i >>= 1;
        while i > 0 {
            self.tree[i] = self.tree[2 * i].max(self.tree[2 * i + 1]);
            i >>= 1;
        }
    }

    /// The largest level at the places lo to hi.
    fn max(&self, lo: usize, hi: usize) -> i64 {
        let (mut lo, mut hi, mut best) = (lo + self.width, hi + self.width + 1, 0);
        while lo < hi {
            if lo & 1 == 1 {
                best = best.max(self.tree[lo]);
                lo += 1;
            }
            if hi & 1 == 1 {
                hi -= 1;
                best = best.max(self.tree[hi]);
            }
            lo >>= 1;
            hi >>= 1;
        }
        best
    }
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s.split_ascii_whitespace();
    let mut num = || it.next().unwrap();
    let n: usize = num().parse().unwrap();
    let mut adj = vec![Vec::new(); n + 1];
    for _ in 1..n {
        let a: usize = num().parse().unwrap();
        let b: usize = num().parse().unwrap();
        adj[a].push(b);
        adj[b].push(a);
    }
    // heavy-light decomposition: every cave's heavy child continues its chain,
    // and the chains lie consecutively in one segment tree of maxima
    let (mut parent, mut depth, mut order) =
        (vec![0usize; n + 1], vec![0usize; n + 1], vec![1usize]);
    let mut i = 0;
    while i < order.len() {
        let v = order[i];
        for &u in &adj[v] {
            if u != parent[v] {
                parent[u] = v;
                depth[u] = depth[v] + 1;
                order.push(u);
            }
        }
        i += 1;
    }
    let (mut size, mut heavy) = (vec![1usize; n + 1], vec![0usize; n + 1]);
    for &v in order[1..].iter().rev() {
        let p = parent[v];
        size[p] += size[v];
        if heavy[p] == 0 || size[v] > size[heavy[p]] {
            heavy[p] = v;
        }
    }
    let (mut head, mut index) = (vec![0usize; n + 1], vec![0usize; n + 1]);
    let mut next = 0;
    for &v in &order {
        if v == 1 || heavy[parent[v]] != v {
            let mut u = v;
            while u != 0 {
                head[u] = v;
                index[u] = next;
                next += 1;
                u = heavy[u];
            }
        }
    }
    let width = n.next_power_of_two();
    let mut maxima = Maxima {
        width,
        tree: vec![0; 2 * width],
    };
    let q: usize = num().parse().unwrap();
    let mut out = String::new();
    for _ in 0..q {
        let kind = num();
        let mut u: usize = num().parse().unwrap();
        let mut v: usize = num().parse().unwrap();
        if kind == "I" {
            maxima.add(index[u], v as i64);
            continue;
        }
        let mut best = 0;
        while head[u] != head[v] {
            if depth[head[u]] < depth[head[v]] {
                std::mem::swap(&mut u, &mut v);
            }
            best = best.max(maxima.max(index[head[u]], index[u]));
            u = parent[head[u]];
        }
        best = best.max(maxima.max(index[u].min(index[v]), index[u].max(index[v])));
        out += &format!("{}\n", best);
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
