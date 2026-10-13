use std::collections::HashMap;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    // a team that submitted more than once is the spammer; the teams are
    // printed in the order of their first submission
    let mut count: HashMap<&str, usize> = HashMap::new();
    let mut order = Vec::new();
    for team in it.take(n) {
        let c = count.entry(team).or_insert(0);
        if *c == 0 {
            order.push(team);
        }
        *c += 1;
    }
    for team in order {
        if count[team] > 1 {
            println!("{}", team);
        }
    }
}
