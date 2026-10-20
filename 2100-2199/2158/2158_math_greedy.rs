use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

const MAX_GEOMETRIC: usize = 30;
const SEED_LIMIT: usize = MAX_GEOMETRIC + 2;
const MAJORITY_SIZE: usize = 2 * (2 * MAX_GEOMETRIC + 1);

fn is_arithmetic(values: &[i64]) -> bool {
    (2..values.len()).all(|i| values[i] - values[i - 1] == values[1] - values[0])
}

fn is_geometric(values: &[i64]) -> bool {
    if values.is_empty() {
        return false;
    }
    if values[0] == 0 {
        return values[values.len() - 1] == 0;
    }
    (2..values.len()).all(|i| values[i] * values[0] == values[i - 1] * values[1])
}

fn insert(values: &mut Vec<i64>, value: i64) {
    let index = values.partition_point(|&item| item <= value);
    values.insert(index, value);
}

fn extract(values: &[i64], start: i64, step: i64) -> Option<(Vec<i64>, Vec<i64>)> {
    let mut arithmetic = Vec::with_capacity(values.len());
    let mut geometric = Vec::with_capacity(MAX_GEOMETRIC + 2);
    let mut expected = start;
    for &value in values {
        if value == expected {
            arithmetic.push(value);
            expected += step;
        } else {
            geometric.push(value);
            if geometric.len() > MAX_GEOMETRIC {
                return None;
            }
        }
    }
    // Three distinct geometric terms cannot form an arithmetic progression.
    for removed in 0..=2 {
        if !arithmetic.is_empty() && is_geometric(&geometric) {
            return Some((arithmetic, geometric));
        }
        if removed == 2 || arithmetic.len() <= 1 {
            break;
        }
        insert(&mut geometric, arithmetic.pop().unwrap());
    }
    None
}

fn solve(mut values: Vec<i64>) -> Option<(Vec<i64>, Vec<i64>)> {
    values.sort_unstable();
    let mut distinct = 0;
    let mut repeated = Vec::new();
    for (i, &value) in values.iter().enumerate() {
        if i == 0 || value != values[i - 1] {
            distinct += 1;
        } else if i == 1 || value != values[i - 2] {
            repeated.push(value);
        }
    }
    if distinct == 1 {
        return Some((values[..1].to_vec(), values[1..].to_vec()));
    }
    if distinct == 2 {
        let cut = values.partition_point(|&value| value == values[0]);
        return Some((values[..cut].to_vec(), values[cut..].to_vec()));
    }
    if repeated.len() == 1 {
        let constant = repeated[0];
        let copies = values.iter().filter(|&&value| value == constant).count();
        let other: Vec<i64> = values
            .iter()
            .copied()
            .filter(|&value| value != constant)
            .collect();
        for moved in 0..2 {
            let mut rest = other.clone();
            if moved != 0 {
                insert(&mut rest, constant);
            }
            let equal = vec![constant; copies - moved];
            if is_geometric(&rest) {
                return Some((equal, rest));
            }
            if is_arithmetic(&rest) {
                return Some((rest, equal));
            }
        }
    }
    if values.len() <= MAX_GEOMETRIC + 1 {
        for (i, &value) in values.iter().enumerate() {
            let mut rest = values[..i].to_vec();
            rest.extend_from_slice(&values[i + 1..]);
            if is_geometric(&rest) {
                return Some((vec![value], rest));
            }
        }
    }
    if values.len() >= MAJORITY_SIZE {
        let mut gaps: Vec<i64> = values.windows(2).map(|pair| pair[1] - pair[0]).collect();
        gaps.sort_unstable();
        let step = gaps[gaps.len() / 2];
        if step != 0 {
            for &start in &values[..=MAX_GEOMETRIC] {
                if let Some(answer) = extract(&values, start, step) {
                    return Some(answer);
                }
            }
        }
    } else {
        let limit = values.len().min(SEED_LIMIT);
        for i in 0..limit {
            for j in i + 1..limit {
                let step = values[j] - values[i];
                if step != 0 {
                    if let Some(answer) = extract(&values, values[i], step) {
                        return Some(answer);
                    }
                }
            }
        }
    }
    None
}

fn append_values(output: &mut String, values: &[i64]) {
    for (i, value) in values.iter().enumerate() {
        if i > 0 {
            output.push(' ');
        }
        write!(output, "{value}").unwrap();
    }
    output.push('\n');
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let values = input
        .split_whitespace()
        .skip(1)
        .map(|token| token.parse::<i64>().unwrap())
        .collect();
    let mut output = String::new();
    if let Some((arithmetic, geometric)) = solve(values) {
        writeln!(output, "{}", arithmetic.len()).unwrap();
        append_values(&mut output, &arithmetic);
        append_values(&mut output, &geometric);
    } else {
        output.push_str("-1\n");
    }
    io::stdout().lock().write_all(output.as_bytes()).unwrap();
}
