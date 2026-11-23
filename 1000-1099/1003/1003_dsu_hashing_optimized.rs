use std::collections::HashMap;
use std::io::{self, Read, Write};

const END_OF_INPUT: i64 = -1;

/// Disjoint sets of prefix positions; `parity[x]` is the parity of the number
/// of ones between x and its parent.
struct Dsu {
    parent: Vec<usize>,
    parity: Vec<u8>,
    rank: Vec<u8>,
}

impl Dsu {
    fn add(&mut self) -> usize {
        self.parent.push(self.parent.len());
        self.parity.push(0);
        self.rank.push(0);
        self.parent.len() - 1
    }

    fn find(&mut self, x: usize) -> (usize, u8) {
        let mut path = Vec::new();
        let mut root = x;
        while self.parent[root] != root {
            path.push(root);
            root = self.parent[root];
        }
        let mut acc = 0;
        for &node in path.iter().rev() {
            acc ^= self.parity[node];
            self.parity[node] = acc;
            self.parent[node] = root;
        }
        (root, if path.is_empty() { 0 } else { self.parity[x] })
    }

    /// Records that x and y differ by parity w; false on a contradiction.
    fn union(&mut self, x: usize, y: usize, w: u8) -> bool {
        let (mut rx, px) = self.find(x);
        let (mut ry, py) = self.find(y);
        if rx == ry {
            return px ^ py == w;
        }
        if self.rank[rx] < self.rank[ry] {
            std::mem::swap(&mut rx, &mut ry);
        }
        self.parent[ry] = rx;
        self.parity[ry] = px ^ py ^ w;
        if self.rank[rx] == self.rank[ry] {
            self.rank[rx] += 1;
        }
        true
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let mut out = String::new();
    loop {
        let length: i64 = parse_integer(tokens.next().unwrap());
        if length == END_OF_INPUT {
            break;
        }
        let q: usize = parse_integer(tokens.next().unwrap());
        let mut dsu = Dsu {
            parent: Vec::new(),
            parity: Vec::new(),
            rank: Vec::new(),
        };
        let mut ids: HashMap<i64, usize> = HashMap::new();
        let mut answer = q;
        for i in 0..q {
            let l: i64 = parse_integer(tokens.next().unwrap());
            let r: i64 = parse_integer(tokens.next().unwrap());
            let w = u8::from(tokens.next().unwrap() == "odd");
            if answer != q {
                continue;
            }
            // ones in [l, r] = prefix(r) - prefix(l - 1)
            let a = *ids.entry(l - 1).or_insert_with(|| dsu.add());
            let b = *ids.entry(r).or_insert_with(|| dsu.add());
            if !dsu.union(a, b, w) {
                answer = i;
            }
        }
        out.push_str(&format!("{}\n", answer));
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.
fn parse_integer<T>(word: &str) -> T
where
    T: From<u8> + std::ops::Add<Output = T> + std::ops::Sub<Output = T> + std::ops::Mul<Output = T>,
{
    let digits = word.as_bytes();
    let negative = digits[0] == b'-';
    let start = usize::from(negative || digits[0] == b'+');
    let mut value = T::from(0);
    for &byte in &digits[start..] {
        let digit = T::from(byte - b'0');
        let scaled = value * T::from(10);
        value = if negative {
            scaled - digit
        } else {
            scaled + digit
        };
    }
    value
}
