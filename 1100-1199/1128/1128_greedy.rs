use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = tok.next().unwrap();
    let enemies: Vec<Vec<usize>> = (0..n)
        .map(|_| {
            let k = tok.next().unwrap();
            (0..k).map(|_| tok.next().unwrap() - 1).collect()
        })
        .collect();
    let mut side = vec![0u8; n];
    let mut work: Vec<usize> = (0..n).collect();
    // a child with two or more enemies on its side has at most one on the
    // other, so moving it removes at least one pair of enemies sharing a
    // group; the moves stop after at most as many steps as there are pairs
    while let Some(v) = work.pop() {
        let same = enemies[v].iter().filter(|&&u| side[u] == side[v]).count();
        if same >= 2 {
            side[v] ^= 1;
            work.extend(&enemies[v]);
            work.push(v);
        }
    }
    let (group, other): (Vec<usize>, Vec<usize>) = (1..=n).partition(|&v| side[v - 1] == side[0]);
    let small = if group.len() <= other.len() {
        group
    } else {
        other
    };
    let list: Vec<String> = small.iter().map(|v| v.to_string()).collect();
    println!("{}\n{}", small.len(), list.join(" "));
}
