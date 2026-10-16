use std::io::{self, Read};

// counts are capped here: two ways already make the answer ambiguous
const MANY: u32 = 2;

// whether digit c of the paper may be bit b
fn fits(c: u8, b: usize) -> bool {
    c == b'?' || (c - b'0') as usize == b
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let k = words.next().unwrap().as_bytes();
    let x = words.next().unwrap().as_bytes();
    let n = k.len();
    // the Gray code of k has digit x(i) = k(i) xor k(i - 1), with a 0 before
    // the first digit; ways[b][i] counts the readings of the first i + 1
    // digits that end with k(i) = b
    let mut ways = [vec![0u32; n], vec![0u32; n]];
    let mut w = [1u32, 0];
    for i in 0..n {
        let mut next = [0u32; 2];
        for cur in 0..2 {
            if !fits(k[i], cur) {
                continue;
            }
            for prev in 0..2 {
                if fits(x[i], prev ^ cur) {
                    next[cur] = MANY.min(next[cur] + w[prev]);
                }
            }
        }
        w = next;
        ways[0][i] = w[0];
        ways[1][i] = w[1];
    }
    if w[0] + w[1] == 0 {
        println!("Impossible");
        return;
    }
    if w[0] + w[1] > 1 {
        println!("Ambiguity");
        return;
    }
    // walk back along the single reading: exactly one earlier digit of k
    // with a reading of its own leads on to the next one
    let mut bits = vec![b'0'; n];
    let mut code = vec![b'0'; n];
    let mut cur = if w[1] > 0 { 1 } else { 0 };
    bits[n - 1] = b'0' + cur as u8;
    for i in (1..n).rev() {
        for prev in 0..2 {
            if ways[prev][i - 1] > 0 && fits(x[i], prev ^ cur) {
                bits[i - 1] = b'0' + prev as u8;
                code[i] = b'0' + (prev ^ cur) as u8;
            }
        }
        cur = (bits[i - 1] - b'0') as usize;
    }
    code[0] = bits[0];
    println!("{}\n{}", String::from_utf8(bits).unwrap(), String::from_utf8(code).unwrap());
}
