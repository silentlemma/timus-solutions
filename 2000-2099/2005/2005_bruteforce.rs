use std::io::{self, Read};

const POINTS: usize = 5;
// point k has index k - 1: start 0, middle points FIRST_MIDDLE..LAST_MIDDLE, finish END
const FIRST_MIDDLE: usize = 1;
const POINT_3: usize = 2;
const LAST_MIDDLE: usize = 3;
const END: usize = 4;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let numbers: Vec<i32> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let d = |i: usize, j: usize| numbers[i * POINTS + j];
    // points 2, 3 and 4 (indices 1, 2, 3) come in any order, except that 3
    // may not be the last of them
    let mut best = -1;
    let mut route = [0; POINTS];
    for a in FIRST_MIDDLE..=LAST_MIDDLE {
        for b in FIRST_MIDDLE..=LAST_MIDDLE {
            for c in FIRST_MIDDLE..=LAST_MIDDLE {
                if a == b || a == c || b == c || c == POINT_3 {
                    continue;
                }
                let cost = d(0, a) + d(a, b) + d(b, c) + d(c, END);
                if best < 0 || cost < best {
                    best = cost;
                    route = [0, a, b, c, END];
                }
            }
        }
    }
    println!("{}", best);
    let points: Vec<String> = route.iter().map(|p| (p + 1).to_string()).collect();
    println!("{}", points.join(" "));
}
