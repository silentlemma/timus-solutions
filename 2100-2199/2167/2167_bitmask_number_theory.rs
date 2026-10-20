use std::io::{self, Read, Write};

const BITS: usize = 20; // every number of the message is below 2^20

fn main() {
    let size = 1usize << BITS;
    // has[j][x]: some prime below 2^20 has its top j bits equal to x
    let mut has: Vec<Vec<bool>> = vec![Vec::new(); BITS + 1];
    let mut prime = vec![true; size];
    prime[0] = false;
    prime[1] = false;
    let mut i = 2;
    while i * i < size {
        if prime[i] {
            let mut j = i * i;
            while j < size {
                prime[j] = false;
                j += i;
            }
        }
        i += 1;
    }
    has[BITS] = prime;
    for level in (0..BITS).rev() {
        let row: Vec<bool> = (0..1usize << level)
            .map(|x| has[level + 1][2 * x] || has[level + 1][2 * x + 1])
            .collect();
        has[level] = row;
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|x| x.parse::<usize>().unwrap());
    let t = it.next().unwrap();
    let mut out = String::new();
    for a in it.take(t) {
        // The smallest key is the smallest a xor p over primes p below 2^20,
        // since a key below 2^20 reaches the prime 2; choose the bits of p
        // from the top, keeping the bit of a whenever some prime allows it.
        let mut prefix = 0;
        for bit in (0..BITS).rev() {
            let want = prefix * 2 + (a >> bit & 1);
            prefix = if has[BITS - bit][want] { want } else { want ^ 1 };
        }
        out.push_str(&(a ^ prefix).to_string());
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
