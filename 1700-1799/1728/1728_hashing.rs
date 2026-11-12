use std::collections::HashSet;
use std::io::{self, Read};

const LYOSHA: &str = "Efremov";
const VADIK: &str = "Kantorov";
const FULL_TEAM: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let (mut full, mut pairs) = (HashSet::new(), HashSet::new());
    for _ in 0..n {
        let size: usize = tokens.next().unwrap().parse().unwrap();
        for _ in 0..size {
            let name = tokens.next().unwrap();
            if name != LYOSHA && name != VADIK {
                if size == FULL_TEAM {
                    full.insert(name);
                } else {
                    pairs.insert(name);
                }
            }
        }
    }
    let lyosha: i32 = tokens.next().unwrap().parse().unwrap();
    let vadik: i32 = tokens.next().unwrap().parse().unwrap();
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let (mut best, mut chosen) = (-1, "");
    for _ in 0..m {
        let name = tokens.next().unwrap();
        let rating: i32 = tokens.next().unwrap().parse().unwrap();
        let mut strength = vadik + rating;
        if !full.contains(name) {
            strength += lyosha;
        } else if pairs.contains(name) {
            continue;
        }
        if strength > best {
            best = strength;
            chosen = name;
        }
    }
    if best < 0 {
        println!("Fail");
    } else {
        println!("Win\n{}", chosen);
    }
}
