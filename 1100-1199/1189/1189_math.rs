use std::collections::BTreeSet;
use std::io;

const BASE: i64 = 10;
const ELEVEN: i64 = 11;

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let n: i64 = line.trim().parse().unwrap();
    let mut found = BTreeSet::new();
    // strike digit d at place k from x = (a * 10 + d) * 10^k + b, b < 10^k:
    // then y = a * 10^k + b and x + y = (11a + d) * 10^k + 2b
    let mut power = 1;
    while power <= n {
        for carry in 0..2 {
            let twice = n % power + carry * power;
            if twice % 2 == 0 && twice / 2 < power {
                let (b, q) = (twice / 2, (n - twice) / power);
                let (a, d) = (q / ELEVEN, q % ELEVEN);
                let x = (a * BASE + d) * power + b;
                // x has at least two digits and starts with a nonzero digit
                if d < BASE && x >= BASE && (a > 0 || d > 0) {
                    found.insert(x);
                }
            }
        }
        power *= BASE;
    }
    let mut out = format!("{}\n", found.len());
    for x in found {
        let width = x.to_string().len() - 1;
        out += &format!("{} + {:0width$} = {}\n", x, n - x, n, width = width);
    }
    print!("{}", out);
}
