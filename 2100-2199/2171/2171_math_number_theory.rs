use std::io::{self, Read};

struct Solution {
    limit: i64,
    starts: Vec<i64>,
    steps: Vec<i64>,
}

impl Solution {
    fn count(&self, index: usize, first: i64, period: i64, sign: i64) -> i64 {
        let mut answer = 0;
        for i in index..self.starts.len() {
            let start = self.starts[i];
            let step = self.steps[i];
            let mut next_first = first;
            let mut next_period = period;
            if period == 0 {
                // A zero period represents a single remaining number.
                if first < start || (first - start) % step != 0 {
                    continue;
                }
            } else {
                let mut gcd = period;
                let mut remainder = step;
                let mut coefficient = 1;
                let mut next_coefficient = 0;
                while remainder != 0 {
                    let quotient = gcd / remainder;
                    (gcd, remainder) = (remainder, gcd - quotient * remainder);
                    (coefficient, next_coefficient) =
                        (next_coefficient, coefficient - quotient * next_coefficient);
                }
                let difference = start - first;
                if difference % gcd != 0 {
                    continue;
                }
                let modulus = step / gcd;
                let offset = (difference / gcd * coefficient).rem_euclid(modulus);
                next_period = period * modulus;
                next_first = first + period * offset;
                if next_first < start {
                    next_first +=
                        (start - next_first + next_period - 1) / next_period * next_period;
                }
                if next_first > self.limit {
                    continue;
                }
                if next_period > self.limit - next_first {
                    next_period = 0;
                }
            }
            let size = if next_period == 0 {
                1
            } else {
                (self.limit - next_first) / next_period + 1
            };
            answer += sign * size;
            answer += self.count(i + 1, next_first, next_period, -sign);
        }
        answer
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let limit = tokens.next().unwrap().parse().unwrap();
    let size: usize = tokens.next().unwrap().parse().unwrap();
    let mut starts = Vec::with_capacity(size);
    let mut steps = Vec::with_capacity(size);
    for _ in 0..size {
        starts.push(tokens.next().unwrap().parse().unwrap());
        steps.push(tokens.next().unwrap().parse().unwrap());
    }
    let solution = Solution {
        limit,
        starts,
        steps,
    };
    println!("{}", solution.count(0, 1, 1, 1));
}
