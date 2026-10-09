use std::collections::VecDeque;
use std::io::{self, Read};

const OCTET_BITS: u32 = 8;

fn address(s: &str) -> u32 {
    s.split('.')
        .fold(0, |v, part| v << OCTET_BITS | part.parse::<u32>().unwrap())
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let mut next = || it.next().unwrap();
    let n: usize = next().parse().unwrap();
    // each interface is reduced to its subnet, IP AND mask
    let mut nets: Vec<Vec<u32>> = Vec::with_capacity(n);
    for _ in 0..n {
        let k: usize = next().parse().unwrap();
        let own = (0..k)
            .map(|_| {
                let ip = address(next());
                ip & address(next())
            })
            .collect();
        nets.push(own);
    }
    let start = next().parse::<usize>().unwrap() - 1;
    let end = next().parse::<usize>().unwrap() - 1;
    let linked = |u: usize, v: usize| nets[u].iter().any(|p| nets[v].contains(p));
    let mut from = vec![usize::MAX; n];
    from[start] = start;
    let mut queue = VecDeque::from([start]);
    while let Some(u) = queue.pop_front() {
        for v in 0..n {
            if from[v] == usize::MAX && linked(u, v) {
                from[v] = u;
                queue.push_back(v);
            }
        }
    }
    if from[end] == usize::MAX {
        println!("No");
        return;
    }
    let mut path = vec![end];
    while *path.last().unwrap() != start {
        path.push(from[*path.last().unwrap()]);
    }
    let names: Vec<String> = path.iter().rev().map(|v| (v + 1).to_string()).collect();
    println!("Yes\n{}", names.join(" "));
}
