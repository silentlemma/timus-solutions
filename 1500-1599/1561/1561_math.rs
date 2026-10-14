use std::io::{self, Read};

const DAYS: [&str; 7] = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
];
const WEEK: i64 = DAYS.len() as i64;

fn day_of(word: &str) -> Option<usize> {
    DAYS.iter().position(|&d| d == word)
}

fn inverse(x: i64) -> i64 {
    (1..WEEK).find(|&y| x * y % WEEK == 1).unwrap_or(0)
}

/// A row of an echelon basis over the residues modulo 7, with a 1 at its
/// first non-zero place.
struct Row {
    pivot: usize,
    coefficients: Vec<i64>,
    right: i64,
}

/// Subtracts basis rows until no pivot of the basis stays non-zero.
fn reduce(basis: &[Row], v: &mut [i64], mut value: i64) -> i64 {
    for row in basis {
        let c = v[row.pivot];
        if c == 0 {
            continue;
        }
        // the row is shorter if sorts appeared after it
        for i in row.pivot..row.coefficients.len() {
            v[i] = (v[i] - c * row.coefficients[i]).rem_euclid(WEEK);
        }
        value = (value - c * row.right).rem_euclid(WEEK);
    }
    value
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut sorts = 0;
    let mut basis: Vec<Row> = Vec::new();
    let mut crazy = false;
    let mut out = String::new();
    for _ in 0..n {
        let kind = words.next().unwrap();
        if kind == "Add" {
            sorts += 1;
            continue;
        }
        // the numbers of the query up to its first weekday
        let mut v: Vec<i64> = Vec::new();
        let mut word = words.next().unwrap();
        while day_of(word).is_none() {
            v.push(word.parse::<i64>().unwrap() % WEEK);
            word = words.next().unwrap();
        }
        if v.len() < sorts {
            v.resize(sorts, 0);
        }
        let start = day_of(word).unwrap() as i64;
        if kind == "Learn" {
            let finish = day_of(words.next().unwrap()).unwrap() as i64;
            if crazy {
                continue;
            }
            let value = reduce(&basis, &mut v, (finish - start).rem_euclid(WEEK));
            match v.iter().position(|&c| c != 0) {
                None => crazy = value != 0,
                Some(pivot) => {
                    let scale = inverse(v[pivot]);
                    let coefficients = v.iter().map(|&c| c * scale % WEEK).collect();
                    let at = basis.partition_point(|r| r.pivot < pivot);
                    let right = value * scale % WEEK;
                    basis.insert(
                        at,
                        Row {
                            pivot,
                            coefficients,
                            right,
                        },
                    );
                }
            }
        } else if crazy {
            out.push_str("Already crazy\n");
        } else {
            let value = reduce(&basis, &mut v, 0);
            if v.iter().any(|&c| c != 0) {
                out.push_str("Don't know\n");
            } else {
                out.push_str(DAYS[(start - value).rem_euclid(WEEK) as usize]);
                out.push('\n');
            }
        }
    }
    print!("{}", out);
}
