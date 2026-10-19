use std::collections::HashMap;
use std::fmt::Write;
use std::io::{self, Read};

const FACES: usize = 6;

// grid steps from start to every crystal
fn spread(near: &[Vec<usize>], start: usize) -> Vec<i64> {
    let mut steps = vec![-1i64; near.len()];
    steps[start] = 0;
    let mut queue = vec![start];
    let mut i = 0;
    while i < queue.len() {
        let v = queue[i];
        i += 1;
        for &w in &near[v] {
            if steps[w] < 0 {
                steps[w] = steps[v] + 1;
                queue.push(w);
            }
        }
    }
    steps
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<i64>().unwrap());
    let side = it.next().unwrap() as f64;
    let n = it.next().unwrap();
    let count = (n * n * n) as usize;
    // crystals with the same rune touch: the crystals and their contacts
    // form the n x n x n grid, whatever the turns of the crystals
    let mut near: Vec<Vec<usize>> = vec![Vec::new(); count];
    let mut first: HashMap<i64, usize> = HashMap::with_capacity(FACES * count);
    for c in 0..count {
        for _ in 0..FACES {
            let rune = it.next().unwrap();
            if rune == 0 {
                continue;
            }
            if let Some(&other) = first.get(&rune) {
                near[c].push(other);
                near[other].push(c);
            } else {
                first.insert(rune, c);
            }
        }
    }
    // a corner touches the fewest crystals; the three corners n - 1 steps
    // away lie along the edges from it, and the steps to a corner and to
    // one of them give the coordinate along that edge
    let corner = (0..count).min_by_key(|&c| near[c].len()).unwrap();
    let origin = spread(&near, corner);
    let axes: Vec<Vec<i64>> = (0..count)
        .filter(|&c| origin[c] == n - 1 && near[c].len() == near[corner].len())
        .map(|c| spread(&near, c))
        .collect();
    let m = it.next().unwrap();
    let mut out = String::new();
    for _ in 0..m {
        let a = it.next().unwrap() as usize - 1;
        let b = it.next().unwrap() as usize - 1;
        let square: i64 = axes
            .iter()
            .map(|far| {
                let x = (origin[a] - far[a] + n - 1) / 2;
                let y = (origin[b] - far[b] + n - 1) / 2;
                (x - y) * (x - y)
            })
            .sum();
        writeln!(out, "{:.7}", side * (square as f64).sqrt()).unwrap();
    }
    print!("{}", out);
}
