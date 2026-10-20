use std::collections::VecDeque;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let rows: usize = tokens.next().unwrap().parse().unwrap();
    let width: i64 = tokens.next().unwrap().parse().unwrap();
    let height: usize = tokens.next().unwrap().parse().unwrap();
    let santa_width: i64 = tokens.next().unwrap().parse().unwrap();
    let mut left: VecDeque<(usize, i64)> = VecDeque::new();
    let mut right: VecDeque<(usize, i64)> = VecDeque::new();
    let mut best = 0;

    for index in 0..rows {
        let left_value: i64 = tokens.next().unwrap().parse().unwrap();
        let right_value: i64 = tokens.next().unwrap().parse().unwrap();
        let first = index.saturating_sub(height);
        while let Some(&(position, _)) = left.front() {
            if position >= first {
                break;
            }
            left.pop_front();
        }
        while let Some(&(position, _)) = right.front() {
            if position >= first {
                break;
            }
            right.pop_front();
        }
        while let Some(&(_, value)) = left.back() {
            if value > left_value {
                break;
            }
            left.pop_back();
        }
        while let Some(&(_, value)) = right.back() {
            if value > right_value {
                break;
            }
            right.pop_back();
        }
        left.push_back((index, left_value));
        right.push_back((index, right_value));
        best = best.max(left.front().unwrap().1 + right.front().unwrap().1);
    }

    println!("{}", (width - santa_width + 1 - best).max(0));
}
