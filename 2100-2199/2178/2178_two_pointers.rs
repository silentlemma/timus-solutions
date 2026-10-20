use std::io::{self, Read};

const MAX_VALUE: usize = 100000;
const BASE_SIZE: usize = 16;

struct Solver {
    values: Vec<i32>,
    limit: Vec<usize>,
    minimum: Vec<i32>,
    maximum: Vec<i32>,
    frequency: Vec<i32>,
}

impl Solver {
    fn mixed(&mut self, left: usize, middle: usize, right: usize, sign: i32) -> i64 {
        let (low, high, offset) = if sign == 1 {
            (&self.minimum, &self.maximum, 0)
        } else {
            (&self.maximum, &self.minimum, MAX_VALUE as i32)
        };
        let mut lower = middle;
        let mut upper = middle as i32 - 1;
        let mut threshold = upper;
        let mut current = lower;
        let mut answer = 0;
        for i in (left..middle).rev() {
            while lower < right && sign * low[lower] >= sign * low[i] {
                lower += 1;
            }
            while threshold + 1 < right as i32
                && sign * high[(threshold + 1) as usize] < sign * high[i]
            {
                threshold += 1;
            }
            let target = threshold.min(self.limit[i] as i32);
            while upper < target {
                upper += 1;
                if upper >= current as i32 {
                    let key = (sign * low[upper as usize] + upper + offset) as usize;
                    self.frequency[key] += 1;
                }
            }
            while upper > target {
                if upper >= current as i32 {
                    let key = (sign * low[upper as usize] + upper + offset) as usize;
                    self.frequency[key] -= 1;
                }
                upper -= 1;
            }
            while current < lower {
                if current as i32 <= upper {
                    let key = (sign * low[current] + current as i32 + offset) as usize;
                    self.frequency[key] -= 1;
                }
                current += 1;
            }
            answer += self.frequency[(sign * high[i] + i as i32 + offset) as usize] as i64;
        }
        for (j, &value) in low.iter().enumerate().take(right).skip(middle) {
            self.frequency[(sign * value + j as i32 + offset) as usize] = 0;
        }
        answer
    }

    fn count(&mut self, mut left: usize, mut right: usize) -> i64 {
        let mut answer = 0;
        if right - left <= BASE_SIZE {
            for i in left..right {
                let mut low = self.values[i];
                let mut high = low;
                for j in i..right.min(self.limit[i] + 1) {
                    low = low.min(self.values[j]);
                    high = high.max(self.values[j]);
                    if high - low == (j - i) as i32 {
                        answer += 1;
                    }
                }
            }
            return answer;
        }
        let middle = left + (right - left) / 2;
        answer = self.count(left, middle) + self.count(middle, right);
        while left < middle && self.limit[left] < middle {
            left += 1;
        }
        right = right.min(self.limit[middle - 1] + 1);
        if left == middle || right == middle {
            return answer;
        }
        self.minimum[middle - 1] = self.values[middle - 1];
        self.maximum[middle - 1] = self.values[middle - 1];
        for i in (left..middle - 1).rev() {
            self.minimum[i] = self.minimum[i + 1].min(self.values[i]);
            self.maximum[i] = self.maximum[i + 1].max(self.values[i]);
        }
        self.minimum[middle] = self.values[middle];
        self.maximum[middle] = self.values[middle];
        for j in middle + 1..right {
            self.minimum[j] = self.minimum[j - 1].min(self.values[j]);
            self.maximum[j] = self.maximum[j - 1].max(self.values[j]);
        }
        // Extrema in one half determine the opposite endpoint.
        for i in left..middle {
            let j = i as i32 + self.maximum[i] - self.minimum[i];
            if j >= middle as i32 && j < right as i32 {
                let j = j as usize;
                if j <= self.limit[i]
                    && self.maximum[j] < self.maximum[i]
                    && self.minimum[j] > self.minimum[i]
                {
                    answer += 1;
                }
            }
        }
        for j in middle..right {
            let i = j as i32 - self.maximum[j] + self.minimum[j];
            if i >= left as i32 && i < middle as i32 {
                let i = i as usize;
                if j <= self.limit[i]
                    && self.maximum[i] < self.maximum[j]
                    && self.minimum[i] > self.minimum[j]
                {
                    answer += 1;
                }
            }
        }
        answer + self.mixed(left, middle, right, 1) + self.mixed(left, middle, right, -1)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let values: Vec<i32> = tokens.take(n).map(|token| token.parse().unwrap()).collect();
    let mut solver = Solver {
        values,
        limit: vec![0; n],
        minimum: vec![0; n],
        maximum: vec![0; n],
        frequency: vec![0; MAX_VALUE + n + 1],
    };
    let mut next = vec![n; MAX_VALUE + 1];
    let mut end = n - 1;
    for i in (0..n).rev() {
        let value = solver.values[i] as usize;
        end = end.min(next[value] - 1);
        solver.limit[i] = end;
        next[value] = i;
    }
    println!("{}", solver.count(0, n));
}
