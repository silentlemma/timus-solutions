use std::collections::HashMap;
use std::io::{self, Read};

const WIDTH: usize = 6;
const FULL: i64 = 100;
const CODE: usize = 3;

// percents of total that round each value down or up and add up to 100:
// round all down, then raise the ones with the largest remainders
fn shares(values: &[i64], total: i64) -> Vec<Option<i64>> {
    if total == 0 {
        return vec![None; values.len()];
    }
    let mut out: Vec<i64> = values.iter().map(|v| FULL * v / total).collect();
    let mut order: Vec<usize> = (0..values.len()).collect();
    order.sort_by_key(|&k| -(FULL * values[k] % total));
    let missing = (FULL - out.iter().sum::<i64>()) as usize;
    for &k in &order[..missing] {
        out[k] += 1;
    }
    out.into_iter().map(Some).collect()
}

fn cell(s: &str) -> String {
    format!("{:>width$}", s, width = WIDTH)
}

fn percent(p: Option<i64>) -> String {
    match p {
        Some(p) => cell(&format!("{}%", p)),
        None => cell("-"),
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let lines: Vec<&str> = input
        .split('\n')
        .map(|l| l.trim_end_matches('\r'))
        .collect();
    let survey = lines[0];
    let mut at = 1;
    // each question: its line, then the lines of its answers
    let mut questions: Vec<Vec<&str>> = Vec::new();
    let mut place = HashMap::new();
    while lines[at] != "#" {
        if lines[at].starts_with(' ') {
            questions.last_mut().unwrap().push(lines[at]);
        } else {
            place.insert(&lines[at][..CODE], questions.len());
            questions.push(vec![lines[at]]);
        }
        at += 1;
    }
    at += 1;
    let mut results = Vec::new();
    while lines[at] != "#" {
        results.push(lines[at].as_bytes());
        at += 1;
    }
    at += 1;
    let mut out = String::new();
    while at < lines.len() && lines[at] != "#" {
        let spec = lines[at];
        at += 1;
        let (p1, p2) = (place[&spec[..CODE]], place[&spec[CODE + 1..2 * CODE + 1]]);
        let (first, second) = (&questions[p1], &questions[p2]);
        let a1: Vec<u8> = first[1..].iter().map(|l| l.as_bytes()[1]).collect();
        let a2: Vec<u8> = second[1..].iter().map(|l| l.as_bytes()[1]).collect();
        let (rows, cols) = (a1.len(), a2.len());
        // the table with its totals as one more column and one more row
        let mut table = vec![vec![0i64; cols + 1]; rows + 1];
        for line in &results {
            let r = a1.iter().position(|&c| c == line[p1]).unwrap();
            let c = a2.iter().position(|&x| x == line[p2]).unwrap();
            for i in [r, rows] {
                for j in [c, cols] {
                    table[i][j] += 1;
                }
            }
        }
        let whole = |t: i64| if t > 0 { Some(FULL) } else { None };
        let by_row: Vec<Vec<Option<i64>>> = table
            .iter()
            .map(|r| {
                let mut got = shares(&r[..cols], r[cols]);
                got.push(whole(r[cols]));
                got
            })
            .collect();
        let mut by_col = vec![vec![None; cols + 1]; rows + 1];
        for j in 0..=cols {
            let part: Vec<i64> = (0..rows).map(|i| table[i][j]).collect();
            for (i, p) in shares(&part, table[rows][j]).into_iter().enumerate() {
                by_col[i][j] = p;
            }
            by_col[rows][j] = whole(table[rows][j]);
        }
        if !out.is_empty() {
            out.push('\n');
        }
        out += &format!("{} - {}\n", survey, &spec[2 * CODE + 2..]);
        for line in first.iter().chain(second.iter()) {
            out += line;
            out.push('\n');
        }
        out.push('\n');
        out += &cell("");
        let c2 = &second[0][..CODE];
        for &c in &a2 {
            out += &cell(&format!("{}:{}", c2, c as char));
        }
        out += &cell("TOTAL");
        out.push('\n');
        let c1 = &first[0][..CODE];
        for i in 0..=rows {
            let label = if i < rows {
                format!("{}:{}", c1, a1[i] as char)
            } else {
                "TOTAL".to_string()
            };
            out += &cell(&label);
            for v in &table[i] {
                out += &cell(&v.to_string());
            }
            for ps in [&by_row[i], &by_col[i]] {
                out.push('\n');
                out += &cell("");
                for &p in ps.iter() {
                    out += &percent(p);
                }
            }
            out.push('\n');
        }
    }
    print!("{}", out);
}
