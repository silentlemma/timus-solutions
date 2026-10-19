use std::io::{self, Read};
use std::str::SplitWhitespace;

const MAX_PEOPLE: usize = 400;
const WORD_BITS: usize = 64;
const WORDS: usize = (MAX_PEOPLE + WORD_BITS - 1) / WORD_BITS;
type Claims = [u64; WORDS];

fn solve(locations: &[&str], claims: &[Claims]) -> Vec<usize> {
    let n = locations.len();
    let mut graph = vec![Vec::new(); n];
    for i in 0..n {
        for j in 0..i {
            if locations[i] != locations[j]
                && claims[i].iter().zip(&claims[j]).any(|(a, b)| a & b != 0)
            {
                graph[i].push(j);
                graph[j].push(i);
            }
        }
    }
    let mut color = vec![None; n];
    let mut answer = Vec::new();
    for start in 0..n {
        if color[start].is_some() {
            continue;
        }
        color[start] = Some(0);
        let mut sides = [Vec::new(), Vec::new()];
        let mut pending = vec![start];
        let mut at = 0;
        while at < pending.len() {
            let vertex = pending[at];
            let side = color[vertex].unwrap();
            sides[side].push(vertex);
            for &target in &graph[vertex] {
                if color[target].is_none() {
                    color[target] = Some(side ^ 1);
                    pending.push(target);
                }
            }
            at += 1;
        }
        let chosen = usize::from(sides[1].len() < sides[0].len());
        answer.extend_from_slice(&sides[chosen]);
    }
    if answer.is_empty() {
        answer.push(0);
    }
    answer
}

fn run(tokens: &mut SplitWhitespace<'_>) -> String {
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut locations = Vec::with_capacity(n);
    let mut claims = vec![[0u64; WORDS]; n];
    for (i, mask) in claims.iter_mut().enumerate() {
        locations.push(tokens.next().unwrap());
        mask[i / WORD_BITS] |= 1u64 << (i % WORD_BITS);
        let count: usize = tokens.next().unwrap().parse().unwrap();
        for _ in 0..count {
            let person = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
            mask[person / WORD_BITS] |= 1u64 << (person % WORD_BITS);
        }
    }
    let answer = solve(&locations, &claims);
    let ids: Vec<String> = answer.iter().map(|v| (v + 1).to_string()).collect();
    format!("{}\n{}\n", answer.len(), ids.join(" "))
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", run(&mut input.split_whitespace()));
}
