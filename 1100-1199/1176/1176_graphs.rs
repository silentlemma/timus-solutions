use std::fmt::Write;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let mut read = || it.next().unwrap().parse::<usize>().unwrap();
    let (n, a) = (read(), read());
    // the channels still to lay are the missing ones; every planet has as
    // many of them going out as coming in, so they form one Euler circuit
    let mut todo = vec![Vec::new(); n + 1];
    for i in 1..=n {
        for j in 1..=n {
            if read() == 0 && i != j {
                todo[i].push(j);
            }
        }
    }
    // Hierholzer: walk until stuck, then back up and splice in side loops
    let mut next = vec![0; n + 1];
    let mut stack = vec![a];
    let mut circuit = Vec::new();
    while let Some(&v) = stack.last() {
        if next[v] < todo[v].len() {
            stack.push(todo[v][next[v]]);
            next[v] += 1;
        } else {
            circuit.push(v);
            stack.pop();
        }
    }
    circuit.reverse();
    let mut out = String::new();
    for w in circuit.windows(2) {
        writeln!(out, "{} {}", w[0], w[1]).unwrap();
    }
    print!("{}", out);
}
