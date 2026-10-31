use std::io::{self, BufRead};

const MEDAL_KINDS: usize = 3;
const MEDALS: [&str; MEDAL_KINDS] = ["gold", "silver", "bronze"];
const PER_MEDAL: usize = 4;
const PRIZE: usize = 5;

fn main() {
    let input = io::stdin();
    let mut input = input.lock();
    let mut line = String::new();
    let mut teams = Vec::new();
    // each name and forecast occupies its own line; retain only medallists.
    for medal in MEDALS {
        for _ in 0..PER_MEDAL {
            line.clear();
            input.read_line(&mut line).unwrap();
            teams.push((line.trim().to_owned(), medal));
        }
    }
    line.clear();
    input.read_line(&mut line).unwrap();
    let n: usize = line.trim().parse().unwrap();
    let (mut best, mut winners) = (0, 0);
    for _ in 0..n {
        line.clear();
        input.read_line(&mut line).unwrap();
        let k: usize = line.trim().parse().unwrap();
        let mut right = 0;
        for _ in 0..k {
            line.clear();
            input.read_line(&mut line).unwrap();
            let mut words = line.split_ascii_whitespace();
            let team = words.next().unwrap();
            words.next();
            let kind = words.next().unwrap();
            if teams
                .iter()
                .any(|(name, medal)| name == team && *medal == kind)
            {
                right += 1;
            }
        }
        if right > best {
            best = right;
            winners = 1;
        } else if right == best {
            winners += 1;
        }
    }
    println!("{}", PRIZE * winners);
}
