use std::io::{self, Read};

const SEATS: u32 = 36;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut tokens = text.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut east = vec![0u32; n - 1];
    let mut west = vec![0u32; n - 1];
    for i in 0..n {
        for j in 0..n {
            let people: u32 = tokens.next().unwrap().parse().unwrap();
            if people == 0 {
                continue;
            }
            let load = if i < j { &mut east } else { &mut west };
            for leg in i.min(j)..i.max(j) {
                load[leg] += people;
            }
        }
    }
    let peak = east.into_iter().chain(west).max().unwrap();
    println!("{}", (peak + SEATS - 1) / SEATS);
}
