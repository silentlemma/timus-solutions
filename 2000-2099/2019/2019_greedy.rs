use std::io::{self, Read};
use std::str::SplitWhitespace;

const CASE_BIT: u8 = 32;

fn solve(n: usize, word: &[u8]) -> Option<Vec<usize>> {
    let mut answer = vec![0; n];
    let mut pending: Vec<(u8, usize)> = Vec::with_capacity(word.len());
    let (mut upper, mut lower) = (0, 0);
    for &code in word {
        let is_upper = code.is_ascii_uppercase();
        let index = if is_upper {
            upper += 1;
            upper - 1
        } else {
            lower += 1;
            lower - 1
        };
        if pending
            .last()
            .is_some_and(|&(letter, _)| letter ^ code == CASE_BIT)
        {
            let (_, previous) = pending.pop().unwrap();
            if is_upper {
                answer[index] = previous;
            } else {
                answer[previous] = index;
            }
        } else {
            pending.push((code, index));
        }
    }
    if pending.is_empty() {
        Some(answer)
    } else {
        None
    }
}

fn run(tokens: &mut SplitWhitespace<'_>) -> String {
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let word = tokens.next().unwrap().as_bytes();
    match solve(n, word) {
        None => "Impossible\n".to_string(),
        Some(answer) => {
            let ids: Vec<String> = answer.iter().map(|v| (v + 1).to_string()).collect();
            ids.join(" ") + "\n"
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", run(&mut input.split_whitespace()));
}
