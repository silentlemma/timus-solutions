use std::collections::BTreeMap;
use std::io::{self, Read};

const MOD: u64 = 1_000_000_000;
const OPEN: usize = 1; // plugs are brackets: the two ends of one path
const CLOSE: usize = 2;
const BITS: usize = 2; // a plug state keeps two bits per plug
const MASK: usize = (1 << BITS) - 1;

fn get(code: usize, k: usize) -> usize {
    code >> (BITS * k) & MASK
}

fn with(code: usize, k: usize, v: usize) -> usize {
    (code & !(MASK << (BITS * k))) | v << (BITS * k)
}

/// The bracket matching plug k: rightwards for an opening one, leftwards otherwise.
fn partner(code: usize, k: usize) -> usize {
    let rightwards = get(code, k) == OPEN;
    let (mut depth, mut j) = (0i32, k);
    loop {
        if get(code, j) == get(code, k) {
            depth += 1;
        } else if get(code, j) != 0 {
            depth -= 1;
        }
        if depth == 0 {
            return j;
        }
        j = if rightwards { j + 1 } else { j - 1 };
    }
}

/// Run one row of cells over a plug state and return the states it can leave
/// below; plug c is the left plug of cell c, plug c + 1 its upper plug.
fn row_moves(width: usize, start: usize, last: bool) -> BTreeMap<usize, u64> {
    let mut states = BTreeMap::new();
    states.insert(start << BITS, 1u64);
    for c in 0..width {
        let mut next: BTreeMap<usize, u64> = BTreeMap::new();
        for (&p, &ways) in &states {
            let (left, up) = (get(p, c), get(p, c + 1));
            let mut put = |q: usize, down: usize, right: usize| {
                *next
                    .entry(with(with(q, c, down), c + 1, right))
                    .or_insert(0) += ways;
            };
            if left == 0 && up == 0 {
                if c + 1 < width && !last {
                    put(p, OPEN, CLOSE); // a new path turning right and down
                }
            } else if left != 0 && up != 0 {
                let mut q = p;
                if left == OPEN && up == CLOSE {
                    // closing the cycle: only at the very last cell, with nothing else open
                    if last && c == width - 1 && with(with(p, c, 0), c + 1, 0) == 0 {
                        put(p, 0, 0);
                    }
                    continue;
                }
                if left == OPEN && up == OPEN {
                    q = with(q, partner(q, c + 1), OPEN);
                } else if left == CLOSE && up == CLOSE {
                    q = with(q, partner(q, c), CLOSE);
                }
                put(q, 0, 0);
            } else {
                let plug = left + up;
                if !last {
                    put(p, plug, 0);
                }
                if c + 1 < width {
                    put(p, 0, plug);
                }
            }
        }
        states = next;
    }
    states
        .into_iter()
        .filter(|&(p, _)| get(p, width) == 0)
        .map(|(p, w)| (p, w % MOD))
        .collect()
}

fn multiply(a: &[Vec<u64>], b: &[Vec<u64>]) -> Vec<Vec<u64>> {
    let n = a.len();
    let mut c = vec![vec![0u64; n]; n];
    for i in 0..n {
        for k in 0..n {
            if a[i][k] != 0 {
                for j in 0..n {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
                }
            }
        }
    }
    c
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (width, height) = (v[0] as usize, v[1]);
    // every plug state that a row can leave behind, reached from the empty one
    let mut index: BTreeMap<usize, usize> = BTreeMap::new();
    let mut order = vec![0usize];
    index.insert(0, 0);
    let mut i = 0;
    while i < order.len() {
        for &t in row_moves(width, order[i], false).keys() {
            if !index.contains_key(&t) {
                index.insert(t, order.len());
                order.push(t);
            }
        }
        i += 1;
    }
    let size = order.len();
    let mut step = vec![vec![0u64; size]; size];
    let mut power = vec![vec![0u64; size]; size];
    for i in 0..size {
        power[i][i] = 1;
        for (t, ways) in row_moves(width, order[i], false) {
            step[i][index[&t]] = ways;
        }
    }
    // the first height - 1 rows by fast powering, then the last row that closes the cycle
    let mut e = height - 1;
    while e > 0 {
        if e & 1 == 1 {
            power = multiply(&power, &step);
        }
        step = multiply(&step, &step);
        e >>= 1;
    }
    let mut total = 0u64;
    for i in 0..size {
        if let Some(&closed) = row_moves(width, order[i], true).get(&0) {
            total = (total + power[0][i] * closed) % MOD;
        }
    }
    println!("{}", 2 * total % MOD); // every cycle can be walked in two directions
}
