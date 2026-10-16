use std::collections::HashMap;
use std::io::{self, Read};

struct Search {
    cover: Vec<u32>,
    failed: HashMap<u32, u32>,
    drops: Vec<usize>,
}

impl Search {
    // pick at most budget cities covering the set left, appending to drops
    fn run(&mut self, left: u32, budget: u32) -> bool {
        if left == 0 {
            return true;
        }
        if budget == 0 || self.failed.get(&left).map_or(false, |&f| f >= budget) {
            return false;
        }
        let n = self.cover.len();
        let gain: Vec<u32> = self.cover.iter().map(|&c| (c & left).count_ones()).collect();
        let best = *gain.iter().max().unwrap();
        if left.count_ones() > budget * best {
            self.failed.insert(left, budget);
            return false;
        }
        // the uncovered city with the fewest cities able to hit it
        let u = (0..n)
            .filter(|&v| left >> v & 1 == 1)
            .min_by_key(|&v| self.cover[v].count_ones())
            .unwrap();
        let mut options: Vec<usize> = (0..n).filter(|&v| self.cover[u] >> v & 1 == 1).collect();
        options.sort_by_key(|&v| std::cmp::Reverse(gain[v]));
        let mut tried: Vec<u32> = Vec::new();
        for v in options {
            let hit = self.cover[v] & left;
            // skip a drop that hits only part of what a tried one hits
            if tried.iter().any(|&t| hit & !t == 0) {
                continue;
            }
            tried.push(hit);
            self.drops.push(v);
            if self.run(left & !hit, budget - 1) {
                return true;
            }
            self.drops.pop();
        }
        self.failed.insert(left, budget);
        false
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    if v.is_empty() {
        return;
    }
    let (n, r) = (v[0] as usize, v[1]);
    let coords = &v[2..];
    let city = |i: usize| (coords[2 * i], coords[2 * i + 1]);
    // cover[i]: the cities a bottle dropped on city i destroys
    let cover: Vec<u32> = (0..n)
        .map(|i| {
            let (xi, yi) = city(i);
            (0..n)
                .filter(|&j| {
                    let (xj, yj) = city(j);
                    (xi - xj).pow(2) + (yi - yj).pow(2) <= r * r
                })
                .fold(0, |mask, j| mask | 1 << j)
        })
        .collect();
    let mut search = Search { cover, failed: HashMap::new(), drops: Vec::new() };
    let everything = ((1u64 << n) - 1) as u32;
    let mut budget = 1;
    while !search.run(everything, budget) {
        budget += 1;
    }
    let parts: Vec<String> = search.drops.iter().map(|d| (d + 1).to_string()).collect();
    println!("{}\n{}", parts.len(), parts.join(" "));
}
