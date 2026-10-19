use std::io::{self, Read, Write};

struct Charges {
    size: usize,
    initial: Vec<i64>,
    tree: Vec<i64>,
    offsets: Vec<usize>,
    divisors: Vec<u16>,
}

impl Charges {
    fn new(initial: Vec<i64>) -> Self {
        let size = initial.len() - 1;
        let mut offsets = vec![0; size + 2];
        let mut divisor = 1;
        while divisor * divisor <= size {
            for multiple in (divisor * divisor..=size).step_by(divisor) {
                offsets[multiple + 1] += 1;
            }
            divisor += 1;
        }
        for index in 1..=size + 1 {
            offsets[index] += offsets[index - 1];
        }
        let mut divisors = vec![0; offsets[size + 1]];
        let mut cursor = offsets.clone();
        divisor = 1;
        while divisor * divisor <= size {
            for multiple in (divisor * divisor..=size).step_by(divisor) {
                divisors[cursor[multiple]] = divisor as u16;
                cursor[multiple] += 1;
            }
            divisor += 1;
        }
        Self {
            size,
            initial,
            tree: vec![0; size + 1],
            offsets,
            divisors,
        }
    }

    fn irradiate(&mut self, left: usize, right: usize, power: i64) {
        let mut index = left;
        while index <= self.size {
            self.tree[index] += power;
            index += index & index.wrapping_neg();
        }
        index = right + 1;
        while index <= self.size {
            self.tree[index] -= power;
            index += index & index.wrapping_neg();
        }
    }

    fn point(&self, mut index: usize) -> i64 {
        let mut result = 0;
        while index > 0 {
            result += self.tree[index];
            index &= index - 1;
        }
        result
    }

    fn measure(&self, index: usize) -> i64 {
        let mut result = self.initial[index];
        for at in self.offsets[index]..self.offsets[index + 1] {
            let divisor = self.divisors[at] as usize;
            let partner = index / divisor;
            result += self.point(divisor);
            if partner != divisor {
                result += self.point(partner);
            }
        }
        result
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let size: usize = words.next().unwrap().parse().unwrap();
    let mut initial = vec![0];
    for _ in 0..size {
        initial.push(words.next().unwrap().parse::<i64>().unwrap());
    }
    let mut charges = Charges::new(initial);
    let count: usize = words.next().unwrap().parse().unwrap();
    let mut output = io::BufWriter::new(io::stdout().lock());
    for _ in 0..count {
        let kind: usize = words.next().unwrap().parse().unwrap();
        if kind == 1 {
            let index = words.next().unwrap().parse().unwrap();
            writeln!(output, "{}", charges.measure(index)).unwrap();
        } else {
            let left = words.next().unwrap().parse().unwrap();
            let right = words.next().unwrap().parse().unwrap();
            let power = words.next().unwrap().parse().unwrap();
            charges.irradiate(left, right, power);
        }
    }
}
