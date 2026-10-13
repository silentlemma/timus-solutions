use std::io::{self, Read, Write};

const TABLE: usize = 1 << 15; // over three times the number of values: short probes
const HASH: u32 = 2654435761;
const MAX_VALUE: i64 = 1000000000;

// open addressing: a value and its first position, or position 0 for empty
struct Positions {
    keys: Vec<i64>,
    place: Vec<usize>,
}

impl Positions {
    fn slot(&self, v: i64) -> usize {
        let mut h = (v as u32).wrapping_mul(HASH) as usize % TABLE;
        while self.place[h] != 0 && self.keys[h] != v {
            h = (h + 1) % TABLE;
        }
        h
    }

    // the position of a value, or 0 when it is not there
    fn find(&self, v: i64) -> usize {
        if !(1..=MAX_VALUE).contains(&v) {
            return 0;
        }
        self.place[self.slot(v)]
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut pos = Positions {
        keys: vec![0; TABLE],
        place: vec![0; TABLE],
    };
    let mut a = Vec::with_capacity(n);
    for i in 1..=n {
        let v = it.next().unwrap();
        let h = pos.slot(v);
        if pos.place[h] == 0 {
            pos.keys[h] = v;
            pos.place[h] = i;
            a.push(v);
        }
    }
    a.sort_unstable();
    let m = a.len();
    let mut best = m.min(2);
    let mut first = a[0];
    let mut step = if m > 1 { a[1] - a[0] } else { 0 };
    // a progression is walked only from its smallest element, so every pair of
    // neighbours in a progression is visited once: O(n^2) look-ups in all
    let mut i = 0;
    while i + best < m {
        for j in i + 1..m {
            let d = a[j] - a[i];
            if a[i] + best as i64 * d > a[m - 1] {
                break; // larger differences cannot beat the best either
            }
            if pos.find(a[j] + d) == 0 || pos.find(a[i] - d) != 0 {
                continue; // no third element, or not the smallest one
            }
            let mut length = 2;
            let mut x = a[j] + d;
            while pos.find(x) != 0 {
                length += 1;
                x += d;
            }
            if length > best {
                best = length;
                first = a[i];
                step = d;
            }
        }
        i += 1;
    }
    let places: Vec<String> = (0..best)
        .map(|k| pos.find(first + k as i64 * step).to_string())
        .collect();
    let mut out = io::stdout().lock();
    writeln!(out, "{}", best).unwrap();
    writeln!(out, "{}", places.join(" ")).unwrap();
}
