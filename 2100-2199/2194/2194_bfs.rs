use std::collections::VecDeque;
use std::io::{self, Read};

const FACES: usize = 6; // a six lets the player roll again in the same turn

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut jump = vec![0usize; n + 1];
    for i in 2..n {
        jump[i] = it.next().unwrap();
    }
    // land[i]: where the token rests after arriving at i and following snakes
    let mut land = vec![0usize; n + 1];
    for i in 1..=n {
        land[i] = if jump[i] > 0 { land[i - jump[i]] } else { i };
    }

    // turns holds the fewest turns begun when the token is about to roll at a
    // cell, and a six keeps the turn going at weight 0 while other rolls cost 1
    let infinity = n + 1;
    let mut turns = vec![infinity; n + 1];
    turns[1] = 1;
    let mut queue = VecDeque::from(vec![1usize]);
    let mut best = infinity;
    while let Some(cell) = queue.pop_front() {
        let current = turns[cell];
        if current >= best {
            continue;
        }
        for face in 1..=FACES {
            let target = land[(cell + face).min(n)];
            if target == n {
                best = best.min(current);
                continue;
            }
            let cost = if face == FACES { current } else { current + 1 };
            if cost < turns[target] {
                turns[target] = cost;
                if face == FACES {
                    queue.push_front(target);
                } else {
                    queue.push_back(target);
                }
            }
        }
    }
    if best < infinity {
        println!("{}", best);
    } else {
        println!("-1");
    }
}
