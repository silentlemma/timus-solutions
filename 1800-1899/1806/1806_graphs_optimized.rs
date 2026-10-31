use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read};
use std::io::{BufWriter, Write};

const DIGITS: usize = 10;
const HASH_MULTIPLIER: u64 = 11400714819323198485;
// slots hold index + 1; multiplicative hashing takes high bits of the wrapped product.
fn slot(value: i64, number: &[i64], table: &[u32], bits: u32) -> usize {
    let mut s = ((value as u64).wrapping_mul(HASH_MULTIPLIER) >> (u64::BITS - bits)) as usize;
    while table[s] != 0 && number[table[s] as usize - 1] != value {
        s = (s + 1) & (table.len() - 1);
    }
    s
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let cost: Vec<i32> = (0..DIGITS)
        .map(|_| it.next().unwrap().parse().unwrap())
        .collect();
    let mut place = vec![1i64; DIGITS];
    for p in (0..DIGITS - 1).rev() {
        place[p] = place[p + 1] * DIGITS as i64;
    }
    let number: Vec<i64> = (0..n)
        .map(|_| it.next().unwrap().parse().unwrap())
        .collect();

    let capacity = (2 * n).next_power_of_two();
    let bits = capacity.trailing_zeros();
    let mut table = vec![0u32; capacity];
    for (i, &v) in number.iter().enumerate() {
        let s = slot(v, &number, &table, bits);
        table[s] = i as u32 + 1;
    }

    // at most 49999 edges of cost <= 10000 keep distances within i32.
    let mut best = vec![-1i32; n];
    let mut before = vec![u32::MAX; n];
    let mut heap = BinaryHeap::new();
    best[0] = 0;
    heap.push(Reverse((0i32, 0u32)));
    while let Some(Reverse((d, u))) = heap.pop() {
        let u = u as usize;
        if d != best[u] {
            continue;
        }
        if u == n - 1 {
            break;
        }
        let value = number[u];
        // the fixed ten-digit scratch array avoids a heap allocation for every vertex.
        let mut digit = [0i64; DIGITS];
        for p in 0..DIGITS {
            digit[p] = value / place[p] % DIGITS as i64;
        }
        // neighbours with the first change at digit p share a prefix of p
        for p in 0..DIGITS {
            let low = value - digit[p] * place[p];
            let changes = (0..DIGITS as i64)
                .filter(|&o| o != digit[p])
                .map(|o| low + o * place[p]);
            let swaps = (p + 1..DIGITS)
                .filter(|&q| digit[q] != digit[p])
                .map(|q| value + (digit[q] - digit[p]) * (place[p] - place[q]));
            for next in changes.chain(swaps) {
                let entry = table[slot(next, &number, &table, bits)];
                if entry != 0 {
                    let v = entry as usize - 1;
                    let time = d + cost[p];
                    if best[v] < 0 || time < best[v] {
                        best[v] = time;
                        before[v] = u as u32;
                        heap.push(Reverse((time, v as u32)));
                    }
                }
            }
        }
    }

    let mut out = BufWriter::new(io::stdout().lock());
    if best[n - 1] < 0 {
        writeln!(out, "-1").unwrap();
        return;
    }
    let mut path = vec![n - 1];
    while *path.last().unwrap() != 0 {
        path.push(before[*path.last().unwrap()] as usize);
    }
    writeln!(out, "{}\n{}", best[n - 1], path.len()).unwrap();
    for (i, v) in path.iter().rev().enumerate() {
        if i > 0 {
            write!(out, " ").unwrap();
        }
        write!(out, "{}", v + 1).unwrap();
    }
    writeln!(out).unwrap();
}
