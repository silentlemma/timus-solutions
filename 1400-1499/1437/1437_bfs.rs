use std::collections::{HashSet, VecDeque};
use std::io::{self, Read};

const CANS: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let cap: Vec<usize> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let sz: Vec<usize> = cap.iter().map(|c| c + 1).collect();
    let code = |v: &[usize; CANS]| (v[0] * sz[1] + v[1]) * sz[2] + v[2];
    // a state (x, y, z) as one number; every move leaves some can empty or full
    let mut seen = vec![false; sz[0] * sz[1] * sz[2]];
    seen[0] = true;
    let mut queue = VecDeque::from(vec![[0usize; CANS]]);
    let mut volumes = HashSet::new();
    while let Some(v) = queue.pop_front() {
        for mask in 1..1usize << CANS {
            volumes.insert(
                (0..CANS)
                    .filter(|&i| mask >> i & 1 == 1)
                    .map(|i| v[i])
                    .sum::<usize>(),
            );
        }
        for i in 0..CANS {
            for j in 0..=CANS {
                let mut w = v;
                if j == CANS {
                    w[i] = cap[i]; // fill can i from the pump up to the brim
                } else if i != j {
                    // pour i into j
                    let amount = v[i].min(cap[j] - v[j]);
                    w[i] -= amount;
                    w[j] += amount;
                }
                let k = code(&w);
                if !seen[k] {
                    seen[k] = true;
                    queue.push_back(w);
                }
            }
        }
    }
    volumes.remove(&0);
    println!("{}", volumes.len());
}
