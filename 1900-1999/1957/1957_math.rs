use std::collections::BTreeMap;
use std::fmt::Write;
use std::io::{self, Read};

const TEAM_COUNT: usize = 4;
const WIN_POINTS: i32 = 3;
const OUTCOME_COUNT: usize = 3;
const ORDER_COUNT: usize = 24;

struct Game {
    a: usize,
    b: usize,
    c: i64,
    d: i64,
}
#[derive(Clone)]
struct Row {
    coefficients: Vec<i64>,
    bound: i64,
}

fn gcd(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn simplify(rows: Vec<Row>) -> Option<Vec<Row>> {
    let mut unique: BTreeMap<Vec<i64>, i64> = BTreeMap::new();
    for row in rows {
        let mut divisor = 0;
        for &value in &row.coefficients {
            divisor = gcd(divisor, value);
        }
        if divisor == 0 {
            if row.bound < 0 {
                return None;
            }
            continue;
        }
        let coefficients = row.coefficients.iter().map(|&x| x / divisor).collect();
        let bound = row.bound.div_euclid(divisor);
        unique
            .entry(coefficients)
            .and_modify(|b| *b = (*b).min(bound))
            .or_insert(bound);
    }
    Some(
        unique
            .into_iter()
            .map(|(coefficients, bound)| Row {
                coefficients,
                bound,
            })
            .collect(),
    )
}

fn integer_feasible(input: Vec<Row>) -> bool {
    let Some(mut rows) = simplify(input) else {
        return false;
    };
    while !rows.is_empty() {
        let dimension = rows[0].coefficients.len();
        let mut choice = None;
        for i in 0..dimension {
            let (mut positive, mut negative) = (0, 0);
            let (mut unit_upper, mut unit_lower) = (true, true);
            for row in &rows {
                let value = row.coefficients[i];
                if value > 0 {
                    positive += 1;
                    unit_upper = unit_upper && value == 1;
                }
                if value < 0 {
                    negative += 1;
                    unit_lower = unit_lower && value == -1;
                }
            }
            let candidate = (positive * negative, i);
            if (unit_upper || unit_lower) && choice.map_or(true, |best| candidate < best) {
                choice = Some(candidate);
            }
        }
        let column = choice.unwrap().1;
        let mut projected = Vec::new();
        for row in &rows {
            if row.coefficients[column] == 0 {
                let mut copy = row.clone();
                copy.coefficients.remove(column);
                projected.push(copy);
            }
        }
        for lower in rows.iter().filter(|r| r.coefficients[column] < 0) {
            for upper in rows.iter().filter(|r| r.coefficients[column] > 0) {
                let coefficients = (0..dimension)
                    .filter(|&i| i != column)
                    .map(|i| {
                        upper.coefficients[column] * lower.coefficients[i]
                            - lower.coefficients[column] * upper.coefficients[i]
                    })
                    .collect();
                let bound = upper.coefficients[column] * lower.bound
                    - lower.coefficients[column] * upper.bound;
                projected.push(Row {
                    coefficients,
                    bound,
                });
            }
        }
        let Some(next) = simplify(projected) else {
            return false;
        };
        rows = next;
    }
    true
}

fn next_order(order: &mut [usize; TEAM_COUNT]) -> bool {
    let mut i = TEAM_COUNT - 1;
    while i > 0 && order[i - 1] >= order[i] {
        i -= 1;
    }
    if i == 0 {
        return false;
    }
    let mut j = TEAM_COUNT - 1;
    while order[j] <= order[i - 1] {
        j -= 1;
    }
    order.swap(i - 1, j);
    order[i..].reverse();
    true
}

fn possible_orders(matches: &[Game]) -> Vec<[usize; TEAM_COUNT]> {
    let mut initial_points = [0; TEAM_COUNT];
    let mut initial_difference = [0_i64; TEAM_COUNT];
    let mut played = [[false; TEAM_COUNT]; TEAM_COUNT];
    for m in matches {
        played[m.a][m.b] = true;
        initial_difference[m.a] += m.c - m.d;
        initial_difference[m.b] += m.d - m.c;
        if m.c == m.d {
            initial_points[m.a] += 1;
            initial_points[m.b] += 1;
        } else {
            initial_points[if m.c > m.d { m.a } else { m.b }] += WIN_POINTS;
        }
    }
    let mut remaining = Vec::new();
    for (a, row) in played.iter().enumerate() {
        for (b, &done) in row.iter().enumerate().skip(a + 1) {
            if !done {
                remaining.push((a, b));
            }
        }
    }
    let mut orders = Vec::new();
    let mut order = std::array::from_fn(|i| i);
    loop {
        orders.push(order);
        if !next_order(&mut order) {
            break;
        }
    }
    let mut found = [false; ORDER_COUNT];
    let mut found_count = 0;
    let pattern_count = OUTCOME_COUNT.pow(remaining.len() as u32);
    for pattern in 0..pattern_count {
        if found_count == ORDER_COUNT {
            break;
        }
        let mut code = pattern;
        let mut points = initial_points;
        let mut difference = initial_difference;
        let mut edges = Vec::new();
        for &(a, b) in &remaining {
            let outcome = code % OUTCOME_COUNT;
            code /= OUTCOME_COUNT;
            if outcome == 0 {
                points[a] += 1;
                points[b] += 1;
            } else {
                let (winner, loser) = if outcome == 1 { (a, b) } else { (b, a) };
                points[winner] += WIN_POINTS;
                difference[winner] += 1;
                difference[loser] -= 1;
                edges.push((winner, loser));
            }
        }
        for (index, order) in orders.iter().enumerate() {
            if found[index] || order.windows(2).any(|w| points[w[0]] < points[w[1]]) {
                continue;
            }
            let mut rows = Vec::new();
            for column in 0..edges.len() {
                let mut coefficients = vec![0; edges.len()];
                coefficients[column] = -1;
                rows.push(Row {
                    coefficients,
                    bound: 0,
                });
            }
            for pair in order.windows(2) {
                let (a, b) = (pair[0], pair[1]);
                if points[a] != points[b] {
                    continue;
                }
                let coefficients = edges
                    .iter()
                    .map(|&(winner, loser)| {
                        i64::from(winner == b) - i64::from(loser == b) - i64::from(winner == a)
                            + i64::from(loser == a)
                    })
                    .collect();
                rows.push(Row {
                    coefficients,
                    bound: difference[a] - difference[b],
                });
            }
            if integer_feasible(rows) {
                found[index] = true;
                found_count += 1;
            }
        }
    }
    orders
        .into_iter()
        .enumerate()
        .filter_map(|(i, o)| if found[i] { Some(o) } else { None })
        .collect()
}

fn take<T: std::str::FromStr>(words: &mut std::str::SplitWhitespace<'_>) -> T {
    words.next().unwrap().parse().ok().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = take(&mut words);
    let matches: Vec<Game> = (0..n)
        .map(|_| Game {
            a: take::<usize>(&mut words) - 1,
            b: take::<usize>(&mut words) - 1,
            c: take(&mut words),
            d: take(&mut words),
        })
        .collect();
    let orders = possible_orders(&matches);
    let mut output = String::new();
    writeln!(output, "{}", orders.len()).unwrap();
    for order in orders {
        for (i, team) in order.iter().enumerate() {
            if i > 0 {
                output.push(' ');
            }
            write!(output, "{}", team + 1).unwrap();
        }
        output.push('\n');
    }
    print!("{output}");
}
