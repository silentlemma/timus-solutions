use std::fmt::Write;
use std::io::{self, Read};

struct Fenwick {
    linear: Vec<i64>,
    constant: Vec<i64>,
}

fn lowbit(value: usize) -> usize {
    value & value.wrapping_neg()
}

impl Fenwick {
    fn new(values: &[i64]) -> Self {
        let mut tree = Self {
            linear: vec![0; values.len()],
            constant: vec![0; values.len()],
        };
        for i in 1..values.len() {
            let difference = values[i] - values[i - 1];
            tree.linear[i] = difference;
            tree.constant[i] = difference * (i - 1) as i64;
        }
        for i in 1..values.len() {
            let ancestor = i + lowbit(i);
            if ancestor < values.len() {
                tree.linear[ancestor] += tree.linear[i];
                tree.constant[ancestor] += tree.constant[i];
            }
        }
        tree
    }

    fn suffix_add(&mut self, mut index: usize, amount: i64) {
        let weighted = amount * (index - 1) as i64;
        while index < self.linear.len() {
            self.linear[index] += amount;
            self.constant[index] += weighted;
            index += lowbit(index);
        }
    }

    fn prefix_sum(&self, index: usize) -> i64 {
        let (mut coefficient, mut offset) = (0, 0);
        let mut at = index;
        while at > 0 {
            coefficient += self.linear[at];
            offset += self.constant[at];
            at -= lowbit(at);
        }
        coefficient * index as i64 - offset
    }

    fn point(&self, mut index: usize) -> i64 {
        let mut result = 0;
        while index > 0 {
            result += self.linear[index];
            index -= lowbit(index);
        }
        result
    }

    fn values(mut self) -> Vec<i64> {
        // Undo the linear Fenwick build, then integrate the differences.
        for i in (1..self.linear.len()).rev() {
            let ancestor = i + lowbit(i);
            if ancestor < self.linear.len() {
                self.linear[ancestor] -= self.linear[i];
            }
        }
        for i in 1..self.linear.len() {
            self.linear[i] += self.linear[i - 1];
        }
        self.linear
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let q: usize = tokens.next().unwrap().parse().unwrap();
    let mut salary = vec![0_i64; n];
    salary[0] = tokens.next().unwrap().parse().unwrap();
    let mut parent = vec![0_usize; n];
    for vertex in 1..n {
        parent[vertex] = tokens.next().unwrap().parse().unwrap();
        salary[vertex] = tokens.next().unwrap().parse().unwrap();
    }
    let mut size = vec![1_usize; n];
    for vertex in (1..n).rev() {
        size[parent[vertex]] += size[vertex];
    }
    // Reserve consecutive child blocks; every parent has a smaller number.
    let mut tin = vec![1; n];
    let mut cursor = vec![2; n];
    for vertex in 1..n {
        let boss = parent[vertex];
        tin[vertex] = cursor[boss];
        cursor[boss] += size[vertex];
        cursor[vertex] = tin[vertex] + 1;
    }
    let mut initial = vec![0; n + 1];
    for vertex in 0..n {
        initial[tin[vertex]] = salary[vertex];
    }
    let mut tree = Fenwick::new(&initial);
    for _ in 0..q {
        let kind = tokens.next().unwrap();
        let vertex: usize = tokens.next().unwrap().parse().unwrap();
        let threshold: i64 = tokens.next().unwrap().parse().unwrap();
        let amount: i64 = tokens.next().unwrap().parse().unwrap();
        let left = tin[vertex];
        let length = if kind == "employee" { 1 } else { size[vertex] };
        let total = if length == 1 {
            tree.point(left)
        } else {
            tree.prefix_sum(left + length - 1) - tree.prefix_sum(left - 1)
        };
        if total < threshold * length as i64 {
            tree.suffix_add(left, amount);
            tree.suffix_add(left + length, -amount);
        }
    }
    let final_salary = tree.values();
    let mut output = String::new();
    for vertex in 0..n {
        writeln!(output, "{}", final_salary[tin[vertex]]).unwrap();
    }
    print!("{output}");
}
