use std::fmt::Write as FormatWrite;
use std::io::{self, Read, Write};

#[derive(Clone, Copy)]
struct Query {
    u: usize,
    v: usize,
    cut: usize,
    index: usize,
}

#[derive(Clone, Copy)]
struct Fraction {
    numerator: u64,
    denominator: u64,
}

impl Fraction {
    fn append(self, output: &mut String) {
        write!(output, "{}", self.numerator / self.denominator).unwrap();
        let mut remainder = self.numerator % self.denominator;
        if remainder != 0 {
            output.push('.');
            while remainder != 0 {
                remainder *= 10;
                output.push((b'0' + (remainder / self.denominator) as u8) as char);
                remainder %= self.denominator;
            }
        }
        output.push('\n');
    }
}

fn solve(next: &[usize], length: usize, cut: usize) -> Fraction {
    let mut best = Fraction {
        numerator: 0,
        denominator: 1,
    };
    let mut denominator = 1;
    let mut position = cut;
    let remaining = (length - cut) as u64;
    loop {
        position = next[position];
        let numerator = (position - cut) as u64;
        if numerator * best.denominator > best.numerator * denominator {
            best = Fraction {
                numerator,
                denominator,
            };
        }
        if position == length {
            break;
        }
        position += 1;
        denominator *= 2;
        // An answer is at least 1/2, so at most 18 mismatches need consideration.
        // Even the whole remaining word cannot improve the current answer.
        if remaining * best.denominator <= best.numerator * denominator {
            break;
        }
    }
    best
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let query_count: usize = tokens.next().unwrap().parse().unwrap();
    let mut words = Vec::with_capacity(count);
    let mut maximum_length = 0;
    for _ in 0..count {
        let word: Vec<u8> = tokens.next().unwrap().bytes().rev().collect();
        maximum_length = maximum_length.max(word.len());
        words.push(word);
    }
    let mut queries = Vec::with_capacity(query_count);
    for index in 0..query_count {
        let first = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        let second = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        let cut = tokens.next().unwrap().parse().unwrap();
        queries.push(Query {
            u: first.min(second),
            v: first.max(second),
            cut,
            index,
        });
    }
    queries.sort_unstable_by_key(|query| (query.u, query.v));
    let mut answers = vec![
        Fraction {
            numerator: 0,
            denominator: 1,
        };
        query_count
    ];
    let mut next = vec![0; maximum_length + 1];
    let mut begin = 0;
    while begin < query_count {
        let mut end = begin + 1;
        let u = queries[begin].u;
        let v = queries[begin].v;
        while end < query_count && queries[end].u == u && queries[end].v == v {
            end += 1;
        }
        let length = words[u].len().min(words[v].len());
        if u != v {
            // Reuse one mismatch table for every query of this word pair.
            next[length] = length;
            for i in (0..length).rev() {
                next[i] = if words[u][i] == words[v][i] {
                    next[i + 1]
                } else {
                    i
                };
            }
        }
        for query in &queries[begin..end] {
            answers[query.index] = if u == v {
                Fraction {
                    numerator: (length - query.cut) as u64,
                    denominator: 1,
                }
            } else {
                solve(&next, length, query.cut)
            };
        }
        begin = end;
    }
    let mut output = String::new();
    for answer in answers {
        answer.append(&mut output);
    }
    io::stdout().write_all(output.as_bytes()).unwrap();
}
