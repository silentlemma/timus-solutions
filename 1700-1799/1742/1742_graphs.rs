use std::io::{self, Read};

const FRESH: u8 = 0;
const WALKING: u8 = 1;
const DONE: u8 = 2;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let n = v[0];
    let mut to = vec![0usize; n + 1];
    let mut incoming = vec![0usize; n + 1];
    for i in 1..=n {
        to[i] = v[i];
        incoming[to[i]] += 1;
    }
    // follow the arrows from every new programmer to find the cycles
    let mut state = vec![FRESH; n + 1];
    let mut path = Vec::new();
    let (mut cycles, mut on_cycles, mut bare) = (0, 0, 0);
    for start in 1..=n {
        path.clear();
        let mut x = start;
        while state[x] == FRESH {
            state[x] = WALKING;
            path.push(x);
            x = to[x];
        }
        if state[x] == WALKING {
            cycles += 1;
            // a cycle nobody else points into needs a group of its own
            let mut alone = true;
            let mut u = x;
            loop {
                on_cycles += 1;
                if incoming[u] != 1 {
                    alone = false;
                }
                u = to[u];
                if u == x {
                    break;
                }
            }
            if alone {
                bare += 1;
            }
        }
        for &u in &path {
            state[u] = DONE;
        }
    }
    // fewest: every programmer nobody names starts a group, and so does
    // every bare cycle; most: a cycle goes into one group as soon as a
    // group enters it, and everyone else can stand alone
    let starts = (1..=n).filter(|&i| incoming[i] == 0).count();
    println!("{} {}", starts + bare, n - on_cycles + cycles);
}
