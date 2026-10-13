use std::io::{self, Read};

fn gcd(a: i128, b: i128) -> i128 {
    let (mut a, mut b) = (a.abs(), b.abs());
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

/// An exact fraction p / q with q > 0, kept in lowest terms.
#[derive(Clone, Copy)]
struct Frac {
    p: i128,
    q: i128,
}

impl Frac {
    fn new(p: i128, q: i128) -> Frac {
        let g = gcd(p, q);
        if g > 1 {
            Frac { p: p / g, q: q / g }
        } else {
            Frac { p, q }
        }
    }

    fn add(self, o: Frac) -> Frac {
        Frac::new(self.p * o.q + o.p * self.q, self.q * o.q)
    }

    fn scale(self, times: i128, over: i128) -> Frac {
        Frac::new(self.p * times, self.q * over)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let k: usize = input.trim().parse().unwrap();
    let mut comb = vec![vec![0i128; k + 2]; k + 2];
    for m in 0..=k + 1 {
        comb[m][0] = 1;
        for j in 1..=m {
            comb[m][j] = comb[m - 1][j - 1] + comb[m - 1][j];
        }
    }
    // Bernoulli numbers with B1 = +1/2: the sum of C(m + 1, j) B_j over
    // j <= m equals m + 1, which gives B_m from the earlier ones
    let mut bern: Vec<Frac> = Vec::new();
    for m in 0..=k {
        let mut rest = Frac::new(0, 1);
        for j in 0..m {
            rest = rest.add(bern[j].scale(comb[m + 1][j], 1));
        }
        let size = (m + 1) as i128;
        let left = Frac::new(size, 1).add(Frac::new(-rest.p, rest.q));
        bern.push(left.scale(1, size));
    }
    // Faulhaber: the coefficient of N^(k + 1 - j) is C(k + 1, j) B_j / (k + 1)
    let mut parts: Vec<String> = (0..=k)
        .map(|j| {
            let c = bern[j].scale(comb[k + 1][j], (k + 1) as i128);
            format!("{}/{}", c.p, c.q)
        })
        .collect();
    parts.push("0/1".to_string());
    println!("{}", parts.join(" "));
}
