use std::io::{self, Write};

const LETTERS: usize = 26;
const ORDER: usize = 3;
const LENGTH: usize = 1000000;

// A de Bruijn sequence: every word of ORDER letters once around the cycle.
fn gen(t: usize, p: usize, a: &mut Vec<usize>, cycle: &mut Vec<usize>) {
    if t > ORDER {
        if ORDER % p == 0 {
            cycle.extend_from_slice(&a[1..=p]);
        }
        return;
    }
    a[t] = a[t - p];
    gen(t + 1, p, a, cycle);
    for j in a[t - p] + 1..LETTERS {
        a[t] = j;
        gen(t + 1, t, a, cycle);
    }
}

fn main() {
    let mut a = vec![0; LETTERS * ORDER];
    let mut cycle = Vec::new();
    gen(1, 1, &mut a, &mut cycle);
    // repeating the cycle keeps every window of three letters a cyclic window
    // of it, so each triple, pair and letter appears almost equally often
    let mut out: Vec<u8> = (0..LENGTH)
        .map(|i| b'a' + cycle[i % cycle.len()] as u8)
        .collect();
    out.push(b'\n');
    io::stdout().write_all(&out).unwrap();
}
