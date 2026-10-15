use std::collections::HashSet;
use std::io::{self, Read};

const LYOSHA: &str = "Efremov";
const VADIK: &str = "Kantorov";

fn team(names: &[&str]) -> Vec<String> {
    let mut sorted: Vec<String> = names.iter().map(|s| s.to_string()).collect();
    sorted.sort();
    sorted
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut played = HashSet::new();
    for _ in 0..n {
        let size: usize = it.next().unwrap().parse().unwrap();
        let names: Vec<&str> = (0..size).map(|_| it.next().unwrap()).collect();
        played.insert(team(&names));
    }
    let mut number = || -> i32 { it.next().unwrap().parse().unwrap() };
    let (lyosha, vadik, m) = (number(), number(), number());
    let mut best = -1;
    let mut chosen = String::new();
    for _ in 0..m {
        let name = it.next().unwrap();
        let rating: i32 = it.next().unwrap().parse().unwrap();
        // Lyosha stays away from a team that has played before, and the
        // pair left over must then be new, or the team is out
        let strength = if !played.contains(&team(&[LYOSHA, VADIK, name])) {
            lyosha + vadik + rating
        } else if !played.contains(&team(&[VADIK, name])) {
            vadik + rating
        } else {
            continue;
        };
        if strength > best {
            best = strength;
            chosen = name.to_string();
        }
    }
    if best < 0 {
        println!("Fail");
    } else {
        println!("Win\n{}", chosen);
    }
}
