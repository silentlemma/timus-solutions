use std::io::{self, Read};

const DIGIT: u32 = 9; // the largest digit

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut s: Vec<u8> = input.trim().bytes().collect();
    // the rightmost digit that can grow by one while the digits after it give
    // one back; the smallest such change gives the next number
    let mut after = 0u32; // the sum of the digits after position i
    for i in (0..s.len()).rev() {
        let d = (s[i] - b'0') as u32;
        if d < DIGIT && after > 0 {
            s[i] += 1;
            let mut rest = after - 1;
            // the smallest tail with this sum: the digits pushed to the right
            for j in (i + 1..s.len()).rev() {
                let put = rest.min(DIGIT);
                s[j] = b'0' + put as u8;
                rest -= put;
            }
            println!("{}", String::from_utf8(s).unwrap());
            return;
        }
        after += d;
    }
    println!("-1");
}
