use std::io::{self, Read};

const MOST: i32 = 30;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let t: usize = lines.next().unwrap().trim().parse().unwrap();
    let mut out = String::new();
    for line in lines.take(t) {
        let numbers: Vec<i32> = line.split_whitespace().filter_map(|w| w.parse().ok()).collect();
        let first_home = line.contains(" home ");
        let (x, y) = (numbers[0], numbers[1]);
        let (mut lowest, mut highest) = (-1, -1);
        for g in 0..=MOST {
            let (mut can_pass, mut can_fail) = (false, false);
            for o in 0..=MOST {
                // totals first, then goals scored at the other team's stadium, and
                // when both are equal a coin decides, so both may happen
                let ours = (x + g, if first_home { g } else { x });
                let theirs = (y + o, if first_home { y } else { o });
                can_pass |= ours >= theirs;
                can_fail |= ours <= theirs;
            }
            if can_pass && lowest == -1 {
                lowest = g;
            }
            if can_fail {
                highest = g;
            }
        }
        out.push_str(&format!("{} {}\n", lowest, highest));
    }
    print!("{}", out);
}
