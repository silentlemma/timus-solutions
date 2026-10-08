use std::io::{self, Read, Write};

// Undo at most one change: the sum of the positions (from 1) of the ones of a
// sent word is divisible by n + 1.
fn restore(mut s: Vec<u8>, n: usize) -> Vec<u8> {
    let modulus = (n + 1) as i64;
    let w: i64 = (1..)
        .zip(&s)
        .filter(|&(_, &c)| c == b'1')
        .map(|(i, _)| i)
        .sum();
    if s.len() == n {
        // a raised zero at position p adds exactly p to the weight
        let p = (w % modulus) as usize;
        if p != 0 {
            s[p - 1] = b'0';
        }
        return s;
    }
    // ones_after: ones to the right of the changed place; they shift by one
    let mut ones_after = 0;
    if s.len() + 1 == n {
        for i in (0..=s.len()).rev() {
            for d in 0..2 {
                if (w + ones_after + d * (i as i64 + 1)) % modulus == 0 {
                    s.insert(i, b'0' + d as u8);
                    return s;
                }
            }
            if i > 0 && s[i - 1] == b'1' {
                ones_after += 1;
            }
        }
    } else {
        for i in (0..s.len()).rev() {
            let d = (s[i] - b'0') as i64;
            if (w - ones_after - d * (i as i64 + 1)) % modulus == 0 {
                s.remove(i);
                return s;
            }
            ones_after += d;
        }
    }
    s
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut out = Vec::new();
    for word in tokens {
        out.extend(restore(word.as_bytes().to_vec(), n));
        out.push(b'\n');
    }
    io::stdout().write_all(&out).unwrap();
}
