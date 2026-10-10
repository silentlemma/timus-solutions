use std::io::{self, Read};

// sums closer than this count as equal
const EPS: f64 = 1e-9;

struct Exchange {
    from: usize,
    to: usize,
    rate: f64,
    fee: f64,
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input.split_ascii_whitespace();
    let mut int = || tok.next().unwrap().parse::<f64>().unwrap();
    let (n, m, s, v) = (int() as usize, int() as usize, int() as usize, int());
    let mut edges = Vec::new();
    for _ in 0..m {
        let (a, b) = (int() as usize, int() as usize);
        let (rab, cab, rba, cba) = (int(), int(), int(), int());
        edges.push(Exchange {
            from: a,
            to: b,
            rate: rab,
            fee: cab,
        });
        edges.push(Exchange {
            from: b,
            to: a,
            rate: rba,
            fee: cba,
        });
    }
    // best[c] is the most money of currency c that can be held; a pass that
    // still improves something after n passes has found a gaining cycle
    let mut best = vec![-1.0f64; n + 1];
    best[s] = v;
    let mut changed = false;
    for _ in 0..n {
        changed = false;
        for e in &edges {
            if best[e.from] - e.fee >= 0.0 {
                let got = (best[e.from] - e.fee) * e.rate;
                if got > best[e.to] + EPS {
                    best[e.to] = got;
                    changed = true;
                }
            }
        }
        if best[s] > v + EPS || !changed {
            break;
        }
    }
    let gain = best[s] > v + EPS || changed;
    println!("{}", if gain { "YES" } else { "NO" });
}
