use std::io::{self, Read};

const HALF: usize = 10; // categories are split into a low and a high half of the mask

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let (k, n, m) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
    // by_category[u][c]: the crossings next to u along roads of category c
    let mut by_category = vec![vec![0u32; k]; n];
    for _ in 0..m {
        let (a, b, c) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
        by_category[a][c] |= 1 << b;
        by_category[b][c] |= 1 << a;
    }
    let low_size = k.min(HALF);
    let high_size = k - low_size;
    let table = |u: usize, offset: usize, size: usize| {
        let mut out = vec![0u32; 1 << size];
        for s in 1..1usize << size {
            out[s] = out[s & (s - 1)] | by_category[u][offset + s.trailing_zeros() as usize];
        }
        out
    };
    let low: Vec<Vec<u32>> = (0..n).map(|u| table(u, 0, low_size)).collect();
    let high: Vec<Vec<u32>> = (0..n).map(|u| table(u, low_size, high_size)).collect();
    let low_mask = (1usize << low_size) - 1;
    // whether the roads of the categories in s lead from crossing 0 to 1
    let connects = |s: usize| {
        let (lo, hi) = (s & low_mask, s >> low_size);
        let (mut reach, mut todo) = (1u32, 1u32);
        while todo != 0 {
            let u = todo.trailing_zeros() as usize;
            todo &= todo - 1;
            let fresh = (low[u][lo] | high[u][hi]) & !reach;
            reach |= fresh;
            todo |= fresh;
            if reach & 2 != 0 {
                return true;
            }
        }
        false
    };
    // fewer permits first
    for size in 1..=k as u32 {
        for s in 0..1usize << k {
            if s.count_ones() == size && connects(s) {
                let chosen: Vec<String> = (0..k)
                    .filter(|c| s >> c & 1 == 1)
                    .map(|c| c.to_string())
                    .collect();
                println!("{}\n{}", size, chosen.join(" "));
                return;
            }
        }
    }
}
