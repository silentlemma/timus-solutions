use std::io::{self, Read};

const KINDS: usize = 3;
const MAX_ANSWER: i32 = 1_000_000_000;

fn number(input: &mut impl Iterator<Item = u8>) -> i32 {
    let first = input.find(|byte| byte.is_ascii_digit()).unwrap();
    let mut value = i32::from(first - b'0');
    for byte in input.take_while(u8::is_ascii_digit) {
        value = value * 10 + i32::from(byte - b'0');
    }
    value
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map(Result::unwrap);
    let reach: [i32; KINDS] = std::array::from_fn(|_| number(&mut input));
    let fare: [i32; KINDS] = std::array::from_fn(|_| number(&mut input));
    let _stations = number(&mut input);
    let (a, b) = (number(&mut input), number(&mut input));
    let (first, last) = (a.min(b), a.max(b));
    let mut start = 0;
    for _ in 2..=first {
        start = number(&mut input);
    }
    let count = (last - first + 1) as usize;
    let mut distance = Vec::with_capacity(count);
    let mut cost = Vec::with_capacity(count);
    distance.push(start);
    cost.push(0);
    let mut from = [0; KINDS];
    for i in 1..count {
        let position = number(&mut input);
        distance.push(position);
        // A prefix costs at most the final answer. Even adding the largest fare fits i32.
        let mut best = 2 * MAX_ANSWER;
        for k in 0..KINDS {
            while position - distance[from[k]] > reach[k] {
                from[k] += 1;
            }
            if from[k] < i {
                best = best.min(cost[from[k]] + fare[k]);
            }
        }
        cost.push(best);
    }
    println!("{}", cost[count - 1]);
}
