use std::io::{self, BufWriter, Read, Write};

fn main() {
    let stdin = io::stdin();
    let mut bytes = stdin.lock().bytes().map(Result::unwrap);
    let mut next = || {
        let first = bytes.by_ref().find(|&c| c > b' ').unwrap();
        let mut value = (first - b'0') as usize;
        for c in bytes.by_ref() {
            if c <= b' ' {
                break;
            }
            value = value * 10 + (c - b'0') as usize;
        }
        value
    };
    let n = next();
    // At most(n+1)*10000<=1000010000 coins, so signed32-bit cells suffice.
    let mut diff = vec![0_i32; n + 2];
    for _ in 0..=n {
        let (a, b, amount) = (next(), next(), next() as i32);
        diff[a] += amount;
        diff[b + 1] -= amount;
    }
    let stdout = io::stdout();
    let mut output = BufWriter::new(stdout.lock());
    let mut total = 0_i32;
    for (i, delta) in diff.iter().enumerate().take(n + 1).skip(1) {
        total += delta;
        write!(output, "{}{}", total, if i < n { " " } else { "\n" }).unwrap();
    }
}
