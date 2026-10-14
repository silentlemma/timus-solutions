use std::io::{self, Read};

const MOD: u64 = 10007;
const MOST: usize = 512; // the product of the sizes is at most this

/// The length of the arrays at each depth, ending with 0 for the empty ones.
fn sizes(text: &str) -> Vec<usize> {
    let (mut open, mut dims): (Vec<usize>, Vec<usize>) = (Vec::new(), Vec::new());
    for ch in text.bytes() {
        if ch == b'[' {
            if let Some(last) = open.last_mut() {
                *last += 1;
            }
            open.push(0);
        } else if ch == b']' {
            let depth = open.len() - 1;
            if dims.len() <= depth {
                dims.resize(depth + 1, 0);
            }
            dims[depth] = open.pop().unwrap();
        }
    }
    dims
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let dims = sizes(&text);
    if dims.len() == 1 {
        println!("1");
        return;
    }
    // Stirling numbers of the second kind: ways to split m references into k objects
    let mut stirling = vec![vec![0u64; MOST + 1]; MOST + 1];
    stirling[0][0] = 1;
    for m in 1..=MOST {
        for k in 1..=m {
            stirling[m][k] = (stirling[m - 1][k - 1] + k as u64 * stirling[m - 1][k]) % MOD;
        }
    }
    // m references to empty arrays: any partition of them (Bell numbers)
    let mut ways: Vec<u64> = (0..=MOST).map(|m| stirling[m].iter().sum::<u64>() % MOD).collect();
    // the references at depth i number at most dims[0] * ... * dims[i - 1]
    let mut slots = vec![1usize];
    for &d in &dims[..dims.len() - 1] {
        slots.push(slots[slots.len() - 1] * d);
    }
    for i in (1..dims.len() - 1).rev() {
        let width = dims[i];
        // m references to arrays of this depth: k distinct arrays, whose
        // k * width elements are configured one level down
        let upper = (MOST / width).min(slots[i]);
        let mut next = vec![0u64; MOST + 1];
        for m in 1..=upper {
            let sum: u64 = (1..=m).map(|k| stirling[m][k] * ways[k * width]).sum();
            next[m] = sum % MOD;
        }
        ways = next;
    }
    println!("{}", ways[dims[0]]);
}
