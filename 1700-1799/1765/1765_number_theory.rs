use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let (n, k) = (words.next().unwrap(), words.next().unwrap());
    let mut broken = vec![false; n];
    for _ in 0..k {
        broken[words.next().unwrap() - 1] = true;
    }
    let mut primes = Vec::new();
    let mut m = n;
    let mut d = 2;
    while d * d <= m {
        if m % d == 0 {
            primes.push(d);
            while m % d == 0 {
                m /= d;
            }
        }
        d += 1;
    }
    if m > 1 {
        primes.push(m);
    }
    // a balanced set of tips is a union of disjoint regular p-gons and q-gons,
    // and blades n / (p q) apart form a p by q grid whose rows are the q-gons
    // and whose columns are the p-gons
    let p = primes[0];
    let q = if primes.len() > 1 { primes[1] } else { 1 };
    let classes = n / (p * q);
    let mut remove = Vec::new();
    for base in 0..classes {
        let (mut bad_row, mut bad_col) = (vec![false; p], vec![false; q]);
        let (mut rows, mut cols) = (0, 0);
        for t in 0..p * q {
            if !broken[base + t * classes] {
                continue;
            }
            if !bad_row[t % p] {
                rows += 1;
            }
            if !bad_col[t % q] {
                cols += 1;
            }
            bad_row[t % p] = true;
            bad_col[t % q] = true;
        }
        if rows == 0 {
            continue;
        }
        // a row and a column always share a cell, so the kept blades are
        // either all clean rows or all clean columns, whichever hold more, and
        // with one prime the rows are single blades that never balance
        let by_rows = q > 1 && (p - rows) * q >= (q - cols) * p;
        for t in 0..p * q {
            let c = base + t * classes;
            let dropped = if by_rows { bad_row[t % p] } else { bad_col[t % q] };
            if dropped && !broken[c] {
                remove.push(c + 1);
            }
        }
    }
    if remove.len() + k == n {
        println!("-1");
        return;
    }
    let names: Vec<String> = remove.iter().map(|x| x.to_string()).collect();
    println!("{}\n{}", remove.len(), names.join(" "));
}
