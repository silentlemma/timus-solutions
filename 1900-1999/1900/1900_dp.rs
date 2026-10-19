use std::io::{self, Read};

const INF: i32 = 1_000_000_000;

struct Layer<'a> {
    cost: &'a [Vec<i32>],
    previous: &'a [i32],
    current: &'a mut [i32],
    parent: &'a mut [usize],
}

impl Layer<'_> {
    fn fill(&mut self, left: usize, right: usize, first: usize, last: usize) {
        if left > right {
            return;
        }
        let middle = (left + right) / 2;
        let (mut best, mut split) = (INF, first);
        for cut in first..=last.min(middle - 1) {
            let value = self.previous[cut] + self.cost[cut + 1][middle];
            if value < best {
                best = value;
                split = cut;
            }
        }
        self.current[middle] = best;
        self.parent[middle] = split;
        self.fill(left, middle - 1, first, split);
        self.fill(middle + 1, right, split, last);
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input
        .split_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let n = tokens.next().unwrap();
    let k = tokens.next().unwrap();
    let width = n + 1;
    let mut weights = vec![vec![0; width]; width];
    let mut cost = vec![vec![0; width]; width];
    for left in 1..n {
        for right in left + 1..=n {
            weights[left][right] = tokens.next().unwrap() as i32;
        }
    }
    for left in (1..n).rev() {
        let mut prefix = 0;
        for right in left + 1..=n {
            prefix += weights[left][right];
            cost[left][right] = cost[left + 1][right] + prefix;
        }
    }
    let groups = k + 1;
    let mut previous = vec![INF; width];
    let mut parents = vec![vec![0; width]; groups + 1];
    for end in 1..=n - groups + 1 {
        previous[end] = cost[1][end];
    }
    for group in 2..=groups {
        let mut current = vec![INF; width];
        let end = n - groups + group;
        let mut layer = Layer {
            cost: &cost,
            previous: &previous,
            current: &mut current,
            parent: &mut parents[group],
        };
        layer.fill(group, end, group - 1, end - 1);
        previous = current;
    }
    let (mut end, mut cuts) = (n, Vec::with_capacity(k));
    for group in (2..=groups).rev() {
        end = parents[group][end];
        cuts.push(end);
    }
    cuts.reverse();
    println!("{}", cost[1][n] - previous[n]);
    println!(
        "{}",
        cuts.iter()
            .map(|x| x.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
}
