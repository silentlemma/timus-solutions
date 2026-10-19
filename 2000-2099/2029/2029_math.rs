use std::io::{self, Read};

fn solve(state: &str) -> u64 {
    const PEG_SUM: usize = 3;
    let mut source = 0;
    let mut answer = 0_u64;
    for (disk, &letter) in state.as_bytes().iter().enumerate().rev() {
        let target = (letter - b'A') as usize;
        if target != source {
            answer += 1_u64 << disk;
            source = PEG_SUM - source - target;
        }
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let _count: usize = tokens.next().unwrap().parse().unwrap();
    let state = tokens.next().unwrap();
    println!("{}", solve(state));
}
