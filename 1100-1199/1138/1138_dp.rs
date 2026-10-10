use std::io::{self, Read};

// a raise must be a whole number of percent of this base
const PERCENT: usize = 100;

fn gcd(a: usize, b: usize) -> usize {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, s) = (tok.next().unwrap(), tok.next().unwrap());
    if s > n {
        println!("0");
        return;
    }
    // jobs[a] is the longest run of jobs from salary s ending at salary a; a
    // raise from a is a whole percent exactly when it is a multiple of
    // a / gcd(a, 100)
    let mut jobs = vec![0; n + 1];
    jobs[s] = 1;
    let mut best = 1;
    for a in s..=n {
        if jobs[a] == 0 {
            continue;
        }
        best = best.max(jobs[a]);
        let step = a / gcd(a, PERCENT);
        for b in (a + step..=n).step_by(step) {
            jobs[b] = jobs[b].max(jobs[a] + 1);
        }
    }
    println!("{}", best);
}
