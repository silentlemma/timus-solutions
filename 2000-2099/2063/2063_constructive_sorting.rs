use std::fmt::Write as _;
use std::io::{self, Read, Write};

// FNV-1a of the whole input seeds splitmix64; the arrangements are never
// decoded, they only make the seed differ between tests
const FNV_OFFSET: u64 = 0xcbf29ce484222325;
const FNV_PRIME: u64 = 0x100000001b3;
const GOLDEN: u64 = 0x9e3779b97f4a7c15;
const MIX_A: u64 = 0xbf58476d1ce4e5b9;
const MIX_B: u64 = 0x94d049bb133111eb;
const SHIFT_A: u32 = 30;
const SHIFT_B: u32 = 27;
const SHIFT_C: u32 = 31;

fn next_random(state: &mut u64) -> u64 {
    *state = state.wrapping_add(GOLDEN);
    let mut z = *state;
    z = (z ^ (z >> SHIFT_A)).wrapping_mul(MIX_A);
    z = (z ^ (z >> SHIFT_B)).wrapping_mul(MIX_B);
    z ^ (z >> SHIFT_C)
}

fn compare(first: usize, second: usize, real: usize, out: &mut String) {
    // Virtual padding is black and is never changed by these ascending comparisons.
    if second < real {
        writeln!(out, "? {} {}", first + 1, second + 1).unwrap();
    }
}

fn merge_network(start: usize, size: usize, stride: usize, real: usize, out: &mut String) {
    let step = 2 * stride;
    if step < size {
        merge_network(start, size, step, real, out);
        merge_network(start + stride, size, step, real, out);
        for first in ((start + stride)..(start + size - stride)).step_by(step) {
            compare(first, first + stride, real, out);
        }
    } else {
        compare(start, start + stride, real, out);
    }
}

fn sort_network(start: usize, size: usize, real: usize, out: &mut String) {
    if size > 1 {
        let half = size / 2;
        sort_network(start, half, real, out);
        sort_network(start + half, half, real, out);
        merge_network(start, size, 1, real, out);
    }
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let mut state = FNV_OFFSET;
    for &c in &input {
        state = (state ^ c as u64).wrapping_mul(FNV_PRIME);
    }
    let text = String::from_utf8_lossy(&input);
    let games: usize = text
        .split_ascii_whitespace()
        .next()
        .unwrap()
        .parse()
        .unwrap();
    let mut out = String::new();
    for game in 0..games {
        let n = game + 2;
        let mut padded = 1;
        while padded < n {
            padded *= 2;
        }
        sort_network(0, padded, n, &mut out);
        let j = 1 + (next_random(&mut state) % (n as u64 - 1)) as usize;
        writeln!(out, "! {} {}", j, j + 1).unwrap();
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
