use std::fmt::Write as _;
use std::io::{self, Read};

const CAP: i32 = 100; // the largest single credit

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i32>().unwrap());
    let n = it.next().unwrap() as usize;
    let rows: Vec<i32> = (0..n).map(|_| it.next().unwrap()).collect();
    let mut cols: Vec<i32> = (0..n).map(|_| it.next().unwrap()).collect();
    let top = *cols.iter().max().unwrap();
    let mut matrix = Vec::with_capacity(n);
    for &need in &rows {
        // take from the fullest columns first: lower them all towards a level
        let taken = |cols: &[i32], level: i32| -> i32 {
            cols.iter().map(|&c| (c - level).clamp(0, CAP)).sum()
        };
        if taken(&cols, 0) < need {
            println!("NO");
            return;
        }
        let (mut lo, mut hi) = (0, top);
        while lo < hi {
            // the lowest level that takes no more than needed
            let mid = (lo + hi) / 2;
            if taken(&cols, mid) <= need {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        let mut row: Vec<i32> = cols.iter().map(|&c| (c - lo).clamp(0, CAP)).collect();
        let mut extra = need - row.iter().sum::<i32>();
        for j in 0..n {
            // one more unit from columns that stand exactly at the level
            if extra > 0 && row[j] < CAP && cols[j] - row[j] == lo && lo > 0 {
                row[j] += 1;
                extra -= 1;
            }
        }
        for j in 0..n {
            cols[j] -= row[j];
        }
        matrix.push(row);
    }
    let mut out = String::from("YES\n");
    for row in &matrix {
        let line: Vec<String> = row.iter().map(|x| x.to_string()).collect();
        writeln!(out, "{}", line.join(" ")).unwrap();
    }
    print!("{}", out);
}
