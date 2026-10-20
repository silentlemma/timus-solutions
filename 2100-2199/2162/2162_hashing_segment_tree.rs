use std::collections::HashMap;
use std::io::{self, Read};

const LABEL_BASE: u64 = 1_000_000_001;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let length: usize = tokens.next().unwrap().parse().unwrap();
    let values: Vec<u64> = tokens.map(|token| token.parse().unwrap()).collect();
    let mut tree = vec![0; 2 * length];
    tree[length..].copy_from_slice(&values);
    for index in (1..length).rev() {
        tree[index] = tree[2 * index].max(tree[2 * index + 1]);
    }

    let mut good_until = vec![length; length];
    for offset in 0..2 {
        let mut next_edge = HashMap::with_capacity(length / 2);
        let mut limit = length;
        if length < 2 + offset {
            continue;
        }
        for start in (0..=length - 2 - offset).rev().step_by(2) {
            let mut first = values[start];
            let mut second = values[start + 1];
            if first == 0 || second == 0 || first == second {
                limit = start;
            } else {
                if first > second {
                    std::mem::swap(&mut first, &mut second);
                }
                let key = first * LABEL_BASE + second;
                if let Some(next) = next_edge.insert(key, start) {
                    limit = limit.min(next);
                }
            }
            good_until[start] = limit;
        }
    }

    let mut answer = 0;
    for start in 0..length.saturating_sub(1) {
        let vertices = values[start];
        let edges = values[start + 1];
        if vertices == 0 || edges > ((length - start - 2) / 2) as u64 {
            continue;
        }
        if edges == 0 {
            answer += 1;
            continue;
        }
        let end = start + 2 + 2 * edges as usize;
        if end > good_until[start + 2] {
            continue;
        }
        let mut left = length + start + 2;
        let mut right = length + end;
        let mut largest = 0;
        while left < right {
            if left % 2 == 1 {
                largest = largest.max(tree[left]);
                left += 1;
            }
            if right % 2 == 1 {
                right -= 1;
                largest = largest.max(tree[right]);
            }
            left /= 2;
            right /= 2;
        }
        if largest <= vertices {
            answer += 1;
        }
    }
    println!("{}", answer);
}
