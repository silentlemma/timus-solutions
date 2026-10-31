use std::io::{self, Write};

const LETTERS: usize = 26;
const ORDER: usize = 3;
const LENGTH: usize = 1000000;

// a de bruijn sequence: every word of order letters once around the cycle.
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
    // one cycle has 26^3 letters; stream it instead of retaining a million-byte output.
    let block: Vec<u8> = cycle.iter().map(|&v| b'a' + v as u8).collect();
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    let mut remaining = LENGTH;
    while remaining >= block.len() {
        out.write_all(&block).unwrap();
        remaining -= block.len();
    }
    out.write_all(&block[..remaining]).unwrap();
    out.write_all(b"\n").unwrap();
}
