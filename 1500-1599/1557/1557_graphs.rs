use std::io::{self, Read};

const GOLDEN: u64 = 0x9E37_79B9_7F4A_7C15;
const MIX1: u64 = 0xBF58_476D_1CE4_E5B9;
const MIX2: u64 = 0x94D0_49BB_1331_11EB;
const SHIFT1: u32 = 30;
const SHIFT2: u32 = 27;
const SHIFT3: u32 = 31;

/// A splitmix64 step: well-spread 64-bit labels from a counter.
fn mix(x: u64) -> u64 {
    let x = x.wrapping_add(GOLDEN);
    let x = (x ^ (x >> SHIFT1)).wrapping_mul(MIX1);
    let x = (x ^ (x >> SHIFT2)).wrapping_mul(MIX2);
    x ^ (x >> SHIFT3)
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text
        .split_ascii_whitespace()
        .map(|w| w.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let mut ends = Vec::with_capacity(m);
    let mut adj: Vec<Vec<(usize, usize)>> = vec![Vec::new(); n];
    for e in 0..m {
        let (u, v) = (it.next().unwrap() - 1, it.next().unwrap() - 1);
        ends.push((u, v));
        adj[u].push((v, e));
        adj[v].push((u, e));
    }
    // a spanning tree in breadth-first order
    let (mut parent, mut parent_edge) = (vec![0usize; n], vec![0usize; n]);
    let (mut seen, mut in_tree) = (vec![false; n], vec![false; m]);
    let mut order = vec![0usize];
    seen[0] = true;
    let mut i = 0;
    while i < order.len() {
        let v = order[i];
        for &(u, e) in &adj[v] {
            if !seen[u] {
                seen[u] = true;
                parent[u] = v;
                parent_edge[u] = e;
                in_tree[e] = true;
                order.push(u);
            }
        }
        i += 1;
    }
    // every other channel gets a random label; a tree channel gets the XOR
    // of the labels of the channels whose cycles pass through it, which is
    // the XOR over the subtree below it
    let (mut label, mut below) = (vec![0u64; m], vec![0u64; n]);
    for e in 0..m {
        if !in_tree[e] {
            label[e] = mix(e as u64);
            below[ends[e].0] ^= label[e];
            below[ends[e].1] ^= label[e];
        }
    }
    for &v in order.iter().skip(1).rev() {
        label[parent_edge[v]] = below[v];
        below[parent[v]] ^= below[v];
    }
    // a bridge (label 0) cuts with any other channel; two other channels cut
    // together exactly when no cycle passes through just one of them
    label.sort_unstable();
    let bridges = label.partition_point(|&x| x == 0) as i64;
    let rest = m as i64 - bridges;
    let mut total = m as i64 * (m as i64 - 1) / 2 - rest * (rest - 1) / 2;
    let mut i = bridges as usize;
    while i < m {
        let mut j = i;
        while j < m && label[j] == label[i] {
            j += 1;
        }
        total += ((j - i) * (j - i - 1) / 2) as i64;
        i = j;
    }
    println!("{}", total);
}
