use std::collections::HashMap;
use std::io::{self, Read};

const CYCLE_CUT: usize = 3; // a cycle on s vertices has path(s - 1) + path(s - 3) sets

struct Counter {
    enemy: Vec<u64>,
    path: Vec<u64>, // independent sets of a path on s vertices
    memo: HashMap<u64, u64>,
}

impl Counter {
    fn count(&mut self, mask: u64) -> u64 {
        if mask == 0 {
            return 1;
        }
        if let Some(&v) = self.memo.get(&mask) {
            return v;
        }
        // split into connected parts, which multiply
        let low = mask & mask.wrapping_neg();
        let (mut part, mut frontier) = (low, low);
        while frontier != 0 {
            let bit = frontier & frontier.wrapping_neg();
            frontier ^= bit;
            let grow = self.enemy[bit.trailing_zeros() as usize] & mask & !part;
            part |= grow;
            frontier |= grow;
        }
        let result = if part != mask {
            self.count(part) * self.count(mask & !part)
        } else {
            let size = mask.count_ones() as usize;
            let (mut pivot, mut most, mut least) = (0, 0, size);
            let mut rest = mask;
            while rest != 0 {
                let v = rest.trailing_zeros() as usize;
                let degree = (self.enemy[v] & mask).count_ones() as usize;
                least = least.min(degree);
                if degree >= most {
                    pivot = v;
                    most = degree;
                }
                rest &= rest - 1;
            }
            if least + 1 == size {
                (size + 1) as u64 // all pairs are enemies: nobody or one robot
            } else if most <= 2 {
                if least <= 1 {
                    self.path[size]
                } else {
                    self.path[size - 1] + self.path[size - CYCLE_CUT]
                }
            } else {
                // branch on a vertex of most enemies: leave it out, or take it
                // and drop all its enemies
                let bit = 1u64 << pivot;
                self.count(mask & !bit) + self.count(mask & !(self.enemy[pivot] | bit))
            }
        };
        self.memo.insert(mask, result);
        result
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut enemy = vec![0u64; n];
    for (i, row) in words.take(n).enumerate() {
        for (j, c) in row.bytes().enumerate() {
            if i != j && c == b'0' {
                enemy[i] |= 1 << j;
            }
        }
    }
    // a working group is a clique of friends, that is an independent set of
    // the graph of non-friends; every group plus the empty one is a day, so
    // the day of rusting is the number of independent sets, empty included
    let mut path = vec![1u64, 2];
    for s in 2..=n {
        let next = path[s - 1] + path[s - 2];
        path.push(next);
    }
    let mut counter = Counter { enemy, path, memo: HashMap::new() };
    println!("{}", counter.count((1u64 << n) - 1));
}
