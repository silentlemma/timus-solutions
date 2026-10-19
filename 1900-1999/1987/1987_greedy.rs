use std::fmt::Write;
use std::io::{self, Read};

fn locate(left: &[i32], right: &[i32], queries: &[i32]) -> Vec<i32> {
    let mut stack: Vec<usize> = Vec::with_capacity(left.len());
    let mut answers = Vec::with_capacity(queries.len());
    let mut index = 0;
    for &point in queries {
        while index < left.len() && left[index] <= point {
            while stack.last().map_or(false, |&i| right[i] < left[index]) {
                stack.pop();
            }
            stack.push(index);
            index += 1;
        }
        while stack.last().map_or(false, |&i| right[i] < point) {
            stack.pop();
        }
        answers.push(stack.last().map_or(-1, |&i| (i + 1) as i32));
    }
    answers
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut left = Vec::with_capacity(n);
    let mut right = Vec::with_capacity(n);
    for _ in 0..n {
        left.push(tokens.next().unwrap().parse().unwrap());
        right.push(tokens.next().unwrap().parse().unwrap());
    }
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let queries: Vec<i32> = (0..m)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let mut output = String::new();
    for answer in locate(&left, &right, &queries) {
        writeln!(&mut output, "{}", answer).unwrap();
    }
    print!("{}", output);
}
