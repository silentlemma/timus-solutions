use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let k = it.next().unwrap();
    let s: Vec<usize> = it.take(n).collect();
    let total: usize = s.iter().sum();
    // Every sponsor needs its own problems, and no problem holds more than k.
    let m = (*s.iter().max().unwrap()).max((total + k - 1) / k);
    // Write the sponsors one after another and deal the copies round robin:
    // a sponsor's copies are consecutive and at most m, so they land in
    // different problems, and every problem gets at most ceil(total / m) <= k.
    let mut problems = vec![Vec::new(); m];
    let mut position = 0;
    for (sponsor, &wanted) in s.iter().enumerate() {
        for _ in 0..wanted {
            problems[position % m].push(sponsor + 1);
            position += 1;
        }
    }
    let mut out = format!("{}\n", m);
    for p in &problems {
        out.push_str(&p.len().to_string());
        for x in p {
            out.push(' ');
            out.push_str(&x.to_string());
        }
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
