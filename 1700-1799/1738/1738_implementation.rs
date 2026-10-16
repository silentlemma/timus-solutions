use std::collections::HashSet;
use std::io::{self, Read};

const HEX_PINS: usize = 1 << 16;
const DIGITS: usize = 4;
const NIBBLE: usize = 15;
const BITS: usize = 4;
const BASE: usize = 10;
const HEX: u32 = 16;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut pins = vec![0usize; n + 1];
    for pin in pins.iter_mut().skip(1) {
        *pin = usize::from_str_radix(it.next().unwrap(), HEX).unwrap();
    }
    // differing hex digits of two pins: nonzero nibbles of their xor
    let mut differ = vec![0usize; HEX_PINS];
    for x in 1..HEX_PINS {
        differ[x] = differ[x >> BITS] + usize::from(x & NIBBLE != 0);
    }
    let mut count = [0u64; DIGITS + 1];
    let longest = n.to_string().len();
    for i in 1..=n {
        let pin = pins[i];
        // each pair is counted from its smaller number: a digit raised in
        // place, which never repeats a number, or a digit inserted
        let (mut place, mut rest) = (1, i);
        while rest > 0 {
            for d in rest % BASE + 1..BASE {
                let j = i + (d - rest % BASE) * place;
                if j > n {
                    break;
                }
                count[differ[pin ^ pins[j]]] += 1;
            }
            place *= BASE;
            rest /= BASE;
        }
        let s = i.to_string();
        if s.len() >= longest {
            continue;
        }
        let mut near = HashSet::new();
        for p in 0..=s.len() {
            for d in '0'..='9' {
                let t = format!("{}{}{}", &s[..p], d, &s[p..]);
                if !t.starts_with('0') {
                    near.insert(t.parse::<usize>().unwrap());
                }
            }
        }
        for j in near {
            if j <= n {
                count[differ[pin ^ pins[j]]] += 1;
            }
        }
    }
    let out: Vec<String> = count[1..].iter().map(|c| c.to_string()).collect();
    println!("{}", out.join(" "));
}
