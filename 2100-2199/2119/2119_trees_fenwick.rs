use std::io::{self, Read, Write};

const LINE_BYTES: usize = 20; // enough for any answer and its newline

fn num(t: &[u8]) -> i64 {
    t.iter().fold(0, |x, &c| x * 10 + (c - b'0') as i64)
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let tokens: Vec<&[u8]> =
        input.split(|c| c.is_ascii_whitespace()).filter(|t| !t.is_empty()).collect();
    let mut at = 0;
    let mut next = || -> &[u8] {
        at += 1;
        tokens[at - 1]
    };
    let n = num(next()) as usize;
    let mut head = vec![usize::MAX; n + 1];
    let mut nxt = vec![0usize; 2 * n];
    let mut to = vec![0usize; 2 * n];
    let mut wt = vec![0i64; 2 * n];
    for i in 0..n - 1 {
        let (u, v, w) = (num(next()) as usize, num(next()) as usize, num(next()));
        let e = 2 * i;
        to[e] = v;
        wt[e] = w;
        nxt[e] = head[u];
        head[u] = e;
        to[e + 1] = u;
        wt[e + 1] = w;
        nxt[e + 1] = head[v];
        head[v] = e + 1;
    }

    let mut tin = vec![0usize; n + 1];
    let mut parent = vec![1usize; n + 1];
    let mut depth = vec![0i64; n + 1];
    let mut order = Vec::with_capacity(n);
    let mut stack = vec![1usize];
    while let Some(v) = stack.pop() {
        tin[v] = order.len();
        order.push(v);
        let mut e = head[v];
        while e != usize::MAX {
            let u = to[e];
            if u != parent[v] {
                parent[u] = v;
                depth[u] = depth[v] + wt[e];
                stack.push(u);
            }
            e = nxt[e];
        }
    }

    // The LCA of u != v is the parent with the smallest preorder number among
    // the vertices in the preorder range (tin[u], tin[v]].
    let mut lg = vec![0usize; n + 1];
    for i in 2..=n {
        lg[i] = lg[i / 2] + 1;
    }
    let mut table: Vec<Vec<u32>> = vec![order.iter().map(|&v| tin[parent[v]] as u32).collect()];
    for k in 1..=lg[n] {
        let prev = &table[k - 1];
        let half = 1 << (k - 1);
        let row: Vec<u32> = (0..n + 1 - (1 << k)).map(|i| prev[i].min(prev[i + half])).collect();
        table.push(row);
    }
    let dist = |u: usize, v: usize| -> i64 {
        if u == v {
            return 0;
        }
        let lo = tin[u].min(tin[v]) + 1;
        let hi = tin[u].max(tin[v]);
        let k = lg[hi - lo + 1];
        let x = table[k][lo].min(table[k][hi + 1 - (1 << k)]) as usize;
        depth[u] + depth[v] - 2 * depth[order[x]]
    };

    let mut fen = vec![0i32; n + 1];
    let top = 1usize << lg[n];
    let q = num(next()) as usize;
    let mut total = 0i32;
    let mut doubled = 0i64; // the sum of distances around the marked vertices in preorder
    let mut out = String::with_capacity(q * LINE_BYTES);
    for _ in 0..q {
        let adding = next()[0] == b'+';
        let v = num(next()) as usize;
        let p = tin[v];
        if !adding {
            let mut i = p + 1;
            while i <= n {
                fen[i] -= 1;
                i += i & i.wrapping_neg();
            }
            total -= 1;
        }
        if total > 0 {
            let mut before = 0;
            let mut i = p;
            while i > 0 {
                before += fen[i];
                i -= i & i.wrapping_neg();
            }
            let kth = |mut k: i32| -> usize {
                let mut pos = 0;
                let mut step = top;
                while step > 0 {
                    if pos + step <= n && fen[pos + step] < k {
                        pos += step;
                        k -= fen[pos];
                    }
                    step >>= 1;
                }
                order[pos]
            };
            let a = kth(if before > 0 { before } else { total });
            let b = kth(if before < total { before + 1 } else { 1 });
            let change = dist(a, v) + dist(v, b) - dist(a, b);
            doubled += if adding { change } else { -change };
        }
        if adding {
            let mut i = p + 1;
            while i <= n {
                fen[i] += 1;
                i += i & i.wrapping_neg();
            }
            total += 1;
        }
        out.push_str(&(doubled / 2).to_string());
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
