use std::io::{self, Read, Write};

const LOG: usize = 17; // 2^17 > 100000 cells

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let mut number = || -> usize { words.next().unwrap().parse().unwrap() };
    let (h, w) = (number(), number());
    let cells = h * w;
    let mut words = text.split_ascii_whitespace().skip(2);
    let mut open = vec![false; cells];
    for r in 0..h {
        for (c, &ch) in words.next().unwrap().as_bytes().iter().enumerate() {
            open[r * w + c] = ch == b'#';
        }
    }
    // the open cells form a tree; root it at the first open cell and keep, for
    // every cell, its parent, depth, the direction of the step from the parent
    // (as the index offset) and the number of turns from the root
    let root = open.iter().position(|&x| x).unwrap();
    let mut parent = vec![usize::MAX; cells];
    let mut depth = vec![0usize; cells];
    let mut step = vec![0i64; cells];
    let mut turns = vec![0i64; cells];
    parent[root] = root;
    let mut order = vec![root];
    let mut k = 0;
    while k < order.len() {
        let v = order[k];
        k += 1;
        let (r, c) = (v / w, v % w);
        let moves = [
            (r > 0, v.wrapping_sub(w)),
            (r + 1 < h, v + w),
            (c > 0, v.wrapping_sub(1)),
            (c + 1 < w, v + 1),
        ];
        for &(fits, u) in &moves {
            if fits && open[u] && parent[u] == usize::MAX {
                parent[u] = v;
                depth[u] = depth[v] + 1;
                step[u] = u as i64 - v as i64;
                turns[u] = turns[v] + (v != root && step[v] != step[u]) as i64;
                order.push(u);
            }
        }
    }
    // closed cells point at themselves, which keeps the jump table in range
    for v in 0..cells {
        if parent[v] == usize::MAX {
            parent[v] = v;
        }
    }
    let mut up = vec![parent.clone()];
    for b in 1..LOG {
        let next: Vec<usize> = (0..cells).map(|v| up[b - 1][up[b - 1][v]]).collect();
        up.push(next);
    }
    let q: usize = words.next().unwrap().parse().unwrap();
    let mut out = String::new();
    for _ in 0..q {
        let mut pos = || -> usize { words.next().unwrap().parse::<usize>().unwrap() - 1 };
        let (r1, c1, r2, c2) = (pos(), pos(), pos(), pos());
        let (mut a, mut b) = (r1 * w + c1, r2 * w + c2);
        if depth[a] < depth[b] {
            std::mem::swap(&mut a, &mut b);
        }
        let mut answer = 0;
        if a != b {
            let (mut a1, mut b1) = (a, b);
            let mut below = false;
            if depth[a] > depth[b] {
                // lift a to just below b's depth: if it then hangs from b, b is
                // an ancestor and only the way down from b counts
                let (mut k, mut bit) = (depth[a] - depth[b] - 1, 0);
                while k > 0 {
                    if k & 1 == 1 {
                        a1 = up[bit][a1];
                    }
                    k >>= 1;
                    bit += 1;
                }
                below = parent[a1] == b;
                if !below {
                    a1 = parent[a1];
                }
            }
            if below {
                answer = turns[a] - turns[a1];
            } else {
                for bit in (0..LOG).rev() {
                    if up[bit][a1] != up[bit][b1] {
                        a1 = up[bit][a1];
                        b1 = up[bit][b1];
                    }
                }
                // a1 and b1 are the children of the meeting cell on the two
                // sides; the path turns there unless it goes straight through
                let straight = step[a1] == -step[b1];
                answer = turns[a] - turns[a1] + turns[b] - turns[b1] + (!straight) as i64;
            }
        }
        out.push_str(&answer.to_string());
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
