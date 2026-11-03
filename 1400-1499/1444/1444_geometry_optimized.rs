use std::io::{self, BufWriter, Read, Write};

const MAX_COORD: i64 = 1000;
const MAX_DENOMINATOR: u64 = (4 * MAX_COORD) as u64;
const SCALE: u64 = MAX_DENOMINATOR * MAX_DENOMINATOR;
const HALF_TURN: u64 = 2 * SCALE;
const FULL_TURN: u64 = 4 * SCALE;
const DISTANCE_BITS: u32 = 12;
const ID_BITS: u32 = 15;
const KEY_SHIFT: u32 = DISTANCE_BITS + ID_BITS;
const ID_MASK: u64 = (1 << ID_BITS) - 1;
const BUFFER_SIZE: usize = 4096;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input
        .split_ascii_whitespace()
        .map(|s| s.parse::<i64>().unwrap());
    let n = tokens.next().unwrap() as usize;
    let ox = tokens.next().unwrap();
    let oy = tokens.next().unwrap();
    let mut keys = Vec::with_capacity(n - 1);
    for identity in 2..=n {
        let dx = tokens.next().unwrap() - ox;
        let dy = tokens.next().unwrap() - oy;
        let distance = (dx.abs() + dy.abs()) as u64;
        let rank = if dy > 0 || (dy == 0 && dx > 0) {
            (distance as i64 - dx) as u64 * SCALE / distance
        } else {
            HALF_TURN + (distance as i64 + dx) as u64 * SCALE / distance
        };
        keys.push((rank << KEY_SHIFT) | (distance << ID_BITS) | identity as u64);
    }
    keys.sort_unstable();
    let mut start = 0;
    let mut previous = keys[keys.len() - 1] >> KEY_SHIFT;
    for (i, &key) in keys.iter().enumerate() {
        let current = key >> KEY_SHIFT;
        let gap = if current >= previous {
            current - previous
        } else {
            current + FULL_TURN - previous
        };
        if gap >= HALF_TURN {
            start = i;
        }
        previous = current;
    }
    let stdout = io::stdout();
    let mut out = BufWriter::with_capacity(BUFFER_SIZE, stdout.lock());
    writeln!(out, "{}\n1", n).unwrap();
    for &key in keys[start..].iter().chain(keys[..start].iter()) {
        writeln!(out, "{}", key & ID_MASK).unwrap();
    }
}
