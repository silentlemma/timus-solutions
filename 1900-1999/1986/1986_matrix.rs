use std::collections::{BTreeMap, BTreeSet};
use std::fmt::Write;
use std::io::{self, Read};

const PERCENT: i128 = 100;
const SCALE: i128 = 1000000;
const DIGITS: usize = 6;

fn determinant(mut a: Vec<Vec<i128>>) -> i128 {
    let n = a.len();
    if n == 0 {
        return 1;
    }
    let (mut previous, mut sign) = (1, 1);
    for k in 0..n - 1 {
        let pivot_row = match (k..n).find(|&r| a[r][k] != 0) {
            Some(r) => r,
            None => return 0,
        };
        if pivot_row != k {
            a.swap(k, pivot_row);
            sign = -sign;
        }
        let pivot = a[k][k];
        for row in k + 1..n {
            for col in k + 1..n {
                a[row][col] = (a[row][col] * pivot - a[row][k] * a[k][col]) / previous;
            }
            a[row][k] = 0;
        }
        previous = pivot;
    }
    sign * a[n - 1][n - 1]
}

fn solve(input: &str) -> String {
    let mut recipes = BTreeMap::<String, BTreeMap<String, i128>>::new();
    let mut parts = BTreeSet::new();
    for line in input.lines().filter(|s| !s.trim().is_empty()) {
        let (name, body) = line.split_once(':').unwrap();
        let mut tokens = body.split_whitespace();
        let mut row = BTreeMap::new();
        while let Some(part) = tokens.next() {
            let value = tokens.next().unwrap().parse().unwrap();
            row.insert(part.to_string(), value);
            parts.insert(part.to_string());
        }
        recipes.insert(name.trim().to_string(), row);
    }
    let names: Vec<String> = recipes.keys().cloned().collect();
    let bases: Vec<String> = parts
        .into_iter()
        .filter(|p| !recipes.contains_key(p))
        .collect();
    let (n, m) = (names.len(), bases.len());
    let mut a = vec![vec![0; n]; n];
    for i in 0..n {
        for j in 0..n {
            let diagonal = if i == j { PERCENT } else { 0 };
            a[i][j] = diagonal - *recipes[&names[i]].get(&names[j]).unwrap_or(&0);
        }
    }
    let denominator = determinant(a.clone());
    let mut numerators = vec![vec![0; m]; n];
    for col in 0..n {
        for base in 0..m {
            let mut replaced = a.clone();
            for row in 0..n {
                replaced[row][col] = *recipes[&names[row]].get(&bases[base]).unwrap_or(&0);
            }
            numerators[col][base] = determinant(replaced);
        }
    }
    let mut output = String::new();
    for row in 0..n {
        let mut units: Vec<i128> = numerators[row]
            .iter()
            .map(|&v| v * PERCENT * SCALE / denominator)
            .collect();
        let largest = (0..m).max_by_key(|&b| numerators[row][b]).unwrap();
        let total: i128 = units.iter().sum();
        units[largest] += PERCENT * SCALE - total;
        write!(&mut output, "{} :", names[row]).unwrap();
        for base in 0..m {
            write!(
                &mut output,
                " {} {}.{:0width$}",
                bases[base],
                units[base] / SCALE,
                units[base] % SCALE,
                width = DIGITS
            )
            .unwrap();
        }
        output.push('\n');
    }
    output
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve(&input));
}
