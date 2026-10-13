use std::collections::BTreeSet;
use std::io::{self, Read};

const BITS: u32 = 21; // the answer stays below 900 000 cells, a table of 2^21 is enough
const WORD: u32 = 64;
const SLOTS: usize = 1 << BITS;
const MIX: u64 = 0x9E37_79B9_7F4A_7C15;

/// An open-addressing set of cell numbers; 0 marks an empty slot, so numbers are stored + 1.
struct CellSet {
    table: Vec<u64>,
    len: usize,
}

impl CellSet {
    fn add(&mut self, cell: i64) {
        let key = cell as u64 + 1;
        let mut h = (key.wrapping_mul(MIX) >> (WORD - BITS)) as usize;
        while self.table[h] != 0 && self.table[h] != key {
            h = (h + 1) & (SLOTS - 1);
        }
        if self.table[h] == 0 {
            self.table[h] = key;
            self.len += 1;
        }
    }
}

/// How many steps fit on the board from cell in direction v.
fn room(s: i64, cell: &[i64], v: &[i64]) -> i64 {
    cell.iter()
        .zip(v)
        .filter(|(_, &d)| d != 0)
        .map(|(&c, &d)| if d > 0 { s - 1 - c } else { c })
        .min()
        .unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let nums: Vec<i64> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (n, s) = (nums[0] as usize, nums[1]);
    let start: Vec<i64> = nums[2..2 + n].iter().map(|c| c - 1).collect();
    // a cell is the number with digits x_i in base S
    let weight: Vec<i64> = (0..n).map(|i| s.pow(i as u32)).collect();
    // rook directions along each axis, bishop directions along all axes at once
    let mut dirs: BTreeSet<Vec<i64>> = BTreeSet::new();
    for i in 0..n {
        for sign in [1, -1] {
            let mut v = vec![0; n];
            v[i] = sign;
            dirs.insert(v);
        }
    }
    for mask in 0..1usize << n {
        // in one dimension they coincide with the rook ones
        dirs.insert(
            (0..n)
                .map(|i| if mask >> i & 1 == 1 { -1 } else { 1 })
                .collect(),
        );
    }
    let mut first: BTreeSet<Vec<i64>> = BTreeSet::new();
    for v in &dirs {
        for k in 1..=room(s, &start, v) {
            first.insert(start.iter().zip(v).map(|(c, d)| c + k * d).collect());
        }
    }
    let mut reach = CellSet {
        table: vec![0; SLOTS],
        len: 0,
    };
    for cell in &first {
        let here: i64 = cell.iter().zip(&weight).map(|(c, w)| c * w).sum();
        for v in &dirs {
            let step: i64 = v.iter().zip(&weight).map(|(d, w)| d * w).sum();
            // every cell on the ray after the first move
            for k in 1..=room(s, cell, v) {
                reach.add(here + k * step);
            }
        }
    }
    println!("{}", reach.len);
}
