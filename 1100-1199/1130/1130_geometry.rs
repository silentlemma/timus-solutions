use std::io::{self, Read};

// among three vectors no longer than L, some sum or difference of two of them
// is no longer than L, so they can be merged into one
const KEEP: usize = 3;

struct Forest {
    x: Vec<i64>,
    y: Vec<i64>,
    parent: Vec<Option<usize>>,
    rel: Vec<i64>,
}

impl Forest {
    fn add(&mut self, x: i64, y: i64) -> usize {
        self.x.push(x);
        self.y.push(y);
        self.parent.push(None);
        self.rel.push(1);
        self.x.len() - 1
    }

    fn join(&mut self, a: usize, b: usize, s: i64) -> usize {
        let node = self.add(self.x[a] + s * self.x[b], self.y[a] + s * self.y[b]);
        self.parent[a] = Some(node);
        self.parent[b] = Some(node);
        self.rel[b] = s;
        node
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = tok.next().unwrap() as usize;
    let length = tok.next().unwrap();
    // nodes 0..n-1 are the input vectors, later nodes are merged pairs
    let mut f = Forest {
        x: Vec::new(),
        y: Vec::new(),
        parent: Vec::new(),
        rel: Vec::new(),
    };
    for _ in 0..n {
        let (x, y) = (tok.next().unwrap(), tok.next().unwrap());
        f.add(x, y);
    }
    let mut active: Vec<usize> = Vec::new();
    for i in 0..n {
        active.push(i);
        if active.len() < KEEP {
            continue;
        }
        let mut choice = None;
        'search: for p in 0..KEEP {
            for q in p + 1..KEEP {
                for s in [-1, 1] {
                    let (a, b) = (active[p], active[q]);
                    let dx = f.x[a] + s * f.x[b];
                    let dy = f.y[a] + s * f.y[b];
                    if dx * dx + dy * dy <= length * length {
                        choice = Some((p, q, s));
                        break 'search;
                    }
                }
            }
        }
        let (p, q, s) = choice.unwrap();
        let mut next: Vec<usize> = (0..KEEP)
            .filter(|&r| r != p && r != q)
            .map(|r| active[r])
            .collect();
        next.push(f.join(active[p], active[q], s));
        active = next;
    }
    // two vectors no longer than L: a sign making their dot product
    // non-positive keeps the sum within sqrt(2) L
    if let [a, b] = active[..] {
        let s = if f.x[a] * f.x[b] + f.y[a] * f.y[b] > 0 {
            -1
        } else {
            1
        };
        f.join(a, b, s);
    }
    let mut sign = vec![1i64; f.x.len()];
    for k in (0..f.x.len()).rev() {
        if let Some(p) = f.parent[k] {
            sign[k] = sign[p] * f.rel[k];
        }
    }
    let out: String = (0..n)
        .map(|i| if sign[i] > 0 { '+' } else { '-' })
        .collect();
    println!("YES\n{}", out);
}
