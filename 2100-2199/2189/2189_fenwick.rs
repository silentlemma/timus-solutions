use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

struct Occurrences {
    positions: Vec<usize>,
    owners: Vec<usize>,
    starts: Vec<usize>,
    sizes: Vec<usize>,
    counts: Vec<usize>,
    steps: Vec<usize>,
    tree: Vec<usize>,
    boundary: usize,
}

impl Occurrences {
    fn new(keys: &[u64], stride: u64, role_count: usize) -> Self {
        let size = keys.len();
        let mut result = Self {
            positions: vec![0; size],
            owners: vec![0; size],
            starts: Vec::with_capacity(role_count),
            sizes: Vec::with_capacity(role_count),
            counts: vec![0; role_count],
            steps: Vec::with_capacity(role_count),
            tree: vec![0; size],
            boundary: stride as usize,
        };
        let mut previous = 0;
        for (rank, &key) in keys.iter().enumerate() {
            let value = key / stride;
            if value != previous {
                result.starts.push(rank);
                result.sizes.push(0);
                previous = value;
            }
            let role = result.starts.len() - 1;
            result.owners[rank] = role;
            result.sizes[role] += 1;
            result.positions[rank] = (key % stride) as usize;
        }
        for &length in &result.sizes {
            let mut step = 1;
            while step * 2 <= length {
                step *= 2;
            }
            result.steps.push(step);
        }
        result
    }

    fn build(&mut self) {
        for role in 0..self.starts.len() {
            let base = self.starts[role];
            let size = self.sizes[role];
            for index in 1..=size {
                let parent = index + (index & index.wrapping_neg());
                if parent <= size {
                    self.tree[base + parent - 1] += self.tree[base + index - 1];
                }
            }
        }
    }

    fn change(&mut self, rank: usize, insert: bool) {
        let role = self.owners[rank];
        let base = self.starts[role];
        let size = self.sizes[role];
        let mut index = rank - base + 1;
        while index <= size {
            if insert {
                self.tree[base + index - 1] += 1;
            } else {
                self.tree[base + index - 1] -= 1;
            }
            index += index & index.wrapping_neg();
        }
        if insert {
            self.counts[role] += 1;
        } else {
            self.counts[role] -= 1;
        }
    }

    fn select(&self, role: usize, mut order: usize) -> usize {
        let base = self.starts[role];
        let size = self.sizes[role];
        let mut index = 0;
        let mut step = self.steps[role];
        while step > 0 {
            let next = index + step;
            if next <= size && self.tree[base + next - 1] < order {
                index = next;
                order -= self.tree[base + next - 1];
            }
            step >>= 1;
        }
        self.positions[base + index]
    }

    fn contribution(&self, rank: usize) -> u64 {
        let role = self.owners[rank];
        let base = self.starts[role];
        let mut before = 0;
        let mut index = rank - base;
        while index > 0 {
            before += self.tree[base + index - 1];
            index -= index & index.wrapping_neg();
        }
        let left = if before == 0 {
            0
        } else {
            self.select(role, before)
        };
        let right = if before == self.counts[role] {
            self.boundary
        } else {
            self.select(role, before + 1)
        };
        let position = self.positions[rank];
        (position - left) as u64 * (right - position) as u64
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let q: usize = tokens.next().unwrap().parse().unwrap();
    let stride = (n + 1) as u64;
    let mut initial_keys = Vec::with_capacity(n);
    let mut queries = Vec::with_capacity(q);
    let mut keys = Vec::with_capacity(n + q);
    for position in 1..=n {
        let value: u64 = tokens.next().unwrap().parse().unwrap();
        let key = value * stride + position as u64;
        initial_keys.push(key);
        keys.push(key);
    }
    for _ in 0..q {
        let position: usize = tokens.next().unwrap().parse().unwrap();
        let value: u64 = tokens.next().unwrap().parse().unwrap();
        let key = value * stride + position as u64;
        queries.push((position - 1, key));
        keys.push(key);
    }
    keys.sort_unstable();
    keys.dedup();
    let mut role_count = 0;
    let mut previous = 0;
    for &key in &keys {
        let role = key / stride;
        if role != previous {
            role_count += 1;
            previous = role;
        }
    }
    let mut occurrences = Occurrences::new(&keys, stride, role_count);
    let mut current = Vec::with_capacity(n);
    let total = n as u64 * (n + 1) as u64 / 2;
    let mut scores = vec![total; role_count];
    let mut last = vec![0; role_count];
    for (index, &key) in initial_keys.iter().enumerate() {
        let rank = keys.binary_search(&key).unwrap();
        let role = occurrences.owners[rank];
        let position = index + 1;
        current.push(rank);
        occurrences.tree[rank] = 1;
        occurrences.counts[role] += 1;
        scores[role] -= (position - last[role]) as u64 * (n + 1 - position) as u64;
        last[role] = position;
    }
    occurrences.build();
    let mut heap = BinaryHeap::with_capacity(role_count + 2 * q);
    for (role, &score) in scores.iter().enumerate() {
        heap.push(Reverse((score, role)));
    }
    let mut output = String::new();
    for (position, key) in queries {
        let old_rank = current[position];
        let new_rank = keys.binary_search(&key).unwrap();
        if old_rank != new_rank {
            let old_role = occurrences.owners[old_rank];
            let new_role = occurrences.owners[new_rank];
            occurrences.change(old_rank, false);
            scores[old_role] += occurrences.contribution(old_rank);
            scores[new_role] -= occurrences.contribution(new_rank);
            occurrences.change(new_rank, true);
            current[position] = new_rank;
            heap.push(Reverse((scores[old_role], old_role)));
            heap.push(Reverse((scores[new_role], new_role)));
        }
        while let Some(&Reverse((score, role))) = heap.peek() {
            if score == scores[role] {
                writeln!(output, "{score}").unwrap();
                break;
            }
            heap.pop();
        }
    }
    io::stdout().lock().write_all(output.as_bytes()).unwrap();
}
