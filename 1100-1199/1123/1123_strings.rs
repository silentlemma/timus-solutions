use std::io::{self, Read};

// the left half with its middle digit, copied backwards onto the right half
fn mirror(digits: &[u8]) -> Vec<u8> {
    let mut out = digits.to_vec();
    let n = out.len();
    for i in 0..n / 2 {
        out[n - 1 - i] = out[i];
    }
    out
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let s = input.split_ascii_whitespace().next().unwrap().as_bytes();
    let mut best = mirror(s);
    // same length strings of digits compare like the numbers they spell
    if best.as_slice() < s {
        // add one to the left half with its middle digit; it is not all nines,
        // since all nines mirror to the largest number of this length
        let mut half = s.to_vec();
        let mut k = (s.len() + 1) / 2 - 1;
        while half[k] == b'9' {
            half[k] = b'0';
            k -= 1;
        }
        half[k] += 1;
        best = mirror(&half);
    }
    println!("{}", String::from_utf8(best).unwrap());
}
