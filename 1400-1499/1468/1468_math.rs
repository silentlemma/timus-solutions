use std::io::{self, Read};

const DIGITS: &[u8] = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

fn whole(mut x: usize, k: usize) -> String {
    let mut out = Vec::new();
    loop {
        out.push(DIGITS[x % k]);
        x /= k;
        if x == 0 {
            break;
        }
    }
    out.reverse();
    String::from_utf8(out).unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let mut out = String::new();
    loop {
        let (a, b) = (it.next().unwrap(), it.next().unwrap());
        if a == 0 && b == 0 {
            break;
        }
        let k = it.next().unwrap();
        let mut text = whole(a / b, k);
        let mut rest = a % b;
        if rest != 0 {
            // long division; a remainder seen before starts the period
            let mut seen = vec![usize::MAX; b];
            let mut frac: Vec<u8> = Vec::new();
            while rest != 0 && seen[rest] == usize::MAX {
                seen[rest] = frac.len();
                rest *= k;
                frac.push(DIGITS[rest / b]);
                rest %= b;
            }
            let mut frac = String::from_utf8(frac).unwrap();
            if rest != 0 {
                frac.insert(seen[rest], '(');
                frac.push(')');
            }
            text.push('.');
            text.push_str(&frac);
        }
        out.push_str(&text);
        out.push('\n');
    }
    print!("{}", out);
}
