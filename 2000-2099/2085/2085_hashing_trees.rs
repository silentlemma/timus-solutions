use std::collections::HashMap;
use std::io::{self, Read};

const SEED: u64 = 31337;
// splitmix64 constants
const GAMMA: u64 = 0x9e3779b97f4a7c15;
const MUL_A: u64 = 0xbf58476d1ce4e5b9;
const MUL_B: u64 = 0x94d049bb133111eb;
const SHIFTS: [u32; 3] = [30, 27, 31];

// splitmix64: random weights without external crates
fn next_random(state: &mut u64) -> u64 {
    *state = state.wrapping_add(GAMMA);
    let mut z = *state;
    z = (z ^ (z >> SHIFTS[0])).wrapping_mul(MUL_A);
    z = (z ^ (z >> SHIFTS[1])).wrapping_mul(MUL_B);
    z ^ (z >> SHIFTS[2])
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let mut adj = vec![Vec::new(); n];
    for _ in 0..n - 1 {
        let (u, v) = (it.next().unwrap() - 1, it.next().unwrap() - 1);
        adj[u].push(v);
        adj[v].push(u);
    }
    // every technology gets a random weight; a path uses each one exactly once
    // when (with overwhelming probability) its weights add up to the sum of all
    let mut state = SEED;
    let weight: Vec<u64> = (0..=m).map(|_| next_random(&mut state)).collect();
    let goal = weight[1..].iter().fold(0u64, |s, &w| s.wrapping_add(w));
    let mut own = vec![0u64; n];
    for v in 0..n {
        let a = it.next().unwrap();
        for _ in 0..a {
            own[v] = own[v].wrapping_add(weight[it.next().unwrap()]);
        }
    }
    // depth[v]: the weights on the path from the root to v
    let mut parent = vec![usize::MAX; n];
    let mut depth = vec![0u64; n];
    depth[0] = own[0];
    let mut order = vec![0];
    let mut k = 0;
    while k < order.len() {
        let v = order[k];
        for &u in &adj[v] {
            if u != parent[v] {
                parent[u] = v;
                depth[u] = depth[v].wrapping_add(own[u]);
                order.push(u);
            }
        }
        k += 1;
    }
    // small to large: below[v] maps depth -> a vertex of the subtree of v; two
    // vertices from different children of x (or x itself) join through x
    let mut below: Vec<Option<HashMap<u64, usize>>> = vec![None; n];
    for &x in order.iter().rev() {
        if own[x] == goal {
            println!("{} {}", x + 1, x + 1);
            return;
        }
        let mut mine = HashMap::new();
        mine.insert(depth[x], x);
        let target = goal.wrapping_add(depth[x].wrapping_mul(2)).wrapping_sub(own[x]);
        for &y in &adj[x] {
            if y == parent[x] {
                continue;
            }
            let mut other = below[y].take().unwrap();
            if other.len() > mine.len() {
                std::mem::swap(&mut mine, &mut other);
            }
            for (&d, &u) in &other {
                if let Some(&v) = mine.get(&target.wrapping_sub(d)) {
                    println!("{} {}", u + 1, v + 1);
                    return;
                }
            }
            mine.extend(other);
        }
        below[x] = Some(mine);
    }
    println!("No solution");
}
