use std::collections::HashSet;
use std::io::{self, Read};

const MODULUS: usize = 1000000007;

struct Expansions<'a> {
    rules: &'a [Vec<usize>],
    width: usize,
    limit: usize,
    prefixes: Vec<Vec<u8>>,
    suffixes: Vec<Vec<u8>>,
    visited: Vec<bool>,
    parts: HashSet<Vec<u8>>,
}

impl Expansions<'_> {
    fn visit(&mut self, vertex: usize) {
        if self.visited[vertex] {
            return;
        }
        if self.rules[vertex].is_empty() {
            self.prefixes[vertex] = vec![(vertex + 1) as u8];
            self.suffixes[vertex] = self.prefixes[vertex].clone();
        } else {
            let mut prefix = Vec::new();
            let mut suffix = Vec::new();
            for index in 0..self.rules[vertex].len() {
                let child = self.rules[vertex][index];
                self.visit(child);
                let mut span = suffix.clone();
                span.extend_from_slice(&self.prefixes[child]);
                for word in span.windows(self.width) {
                    self.parts.insert(word.to_vec());
                }
                prefix.extend_from_slice(&self.prefixes[child]);
                prefix.truncate(self.limit);
                suffix.extend_from_slice(&self.suffixes[child]);
                if suffix.len() > self.limit {
                    suffix.drain(..suffix.len() - self.limit);
                }
            }
            self.prefixes[vertex] = prefix;
            self.suffixes[vertex] = suffix;
        }
        self.visited[vertex] = true;
    }
}

fn distinct_parts(rules: &[Vec<usize>], width: usize) -> usize {
    let mut expansions = Expansions {
        rules,
        width,
        limit: width - 1,
        prefixes: vec![Vec::new(); rules.len()],
        suffixes: vec![Vec::new(); rules.len()],
        visited: vec![false; rules.len()],
        parts: HashSet::new(),
    };
    for vertex in 0..rules.len() {
        expansions.visit(vertex);
    }
    expansions.parts.len() % MODULUS
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut tokens = text.split_whitespace();
    let count = tokens.next().unwrap().parse::<usize>().unwrap();
    let width = tokens.next().unwrap().parse::<usize>().unwrap();
    let mut rules = Vec::with_capacity(count);
    for _ in 0..count {
        let length = tokens.next().unwrap().parse::<i32>().unwrap();
        let rule = if length == -1 {
            Vec::new()
        } else {
            (0..length)
                .map(|_| tokens.next().unwrap().parse::<usize>().unwrap() - 1)
                .collect()
        };
        rules.push(rule);
    }
    println!("{}", distinct_parts(&rules, width));
}
