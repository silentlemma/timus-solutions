use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|x| x.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let m = it.next().unwrap();
    let mut girls: Vec<usize> = it.by_ref().take(n).collect();
    let mut boys: Vec<usize> = it.take(m).collect();
    // with k pairs the k most sensitive girls stay dry, and the k most
    // sensitive boys walk with them
    girls.sort_unstable();
    boys.sort_unstable();
    let best = (0..=n.min(m))
        .map(|k| girls[..n - k].iter().sum::<usize>() + boys[..m - k].iter().sum::<usize>() * k)
        .min()
        .unwrap();
    println!("{}", best);
}
