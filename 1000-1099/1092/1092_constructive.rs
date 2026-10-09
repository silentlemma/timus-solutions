use std::fmt::Write as _;
use std::io::{self, Read};

fn parities(a: &[Vec<bool>]) -> (Vec<usize>, Vec<usize>) {
    let n = a.len();
    let rows = (0..n)
        .filter(|&i| (0..n).filter(|&j| a[i][j]).count() % 2 == 1)
        .collect();
    let cols = (0..n)
        .filter(|&j| (0..n).filter(|&i| a[i][j]).count() % 2 == 1)
        .collect();
    (rows, cols)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n = 2 * it.next().unwrap().parse::<usize>().unwrap() + 1;
    let mut a: Vec<Vec<bool>> = (0..n)
        .map(|_| it.next().unwrap().bytes().map(|c| c == b'+').collect())
        .collect();
    let mut ops: Vec<Vec<usize>> = Vec::new();
    let mut flip = |a: &mut Vec<Vec<bool>>, perm: &Vec<usize>| {
        ops.push(perm.clone());
        for (r, &c) in perm.iter().enumerate() {
            a[r][c] = !a[r][c];
        }
    };
    // two transversals that differ in two rows flip the corners of a
    // rectangle, which keeps every row and column parity; one transversal
    // flips all the parities at once
    let (mut rows, mut cols) = parities(&a);
    if rows.len() == n || cols.len() == n {
        flip(&mut a, &(0..n).collect());
        (rows, cols) = parities(&a);
    }
    // the target keeps the parities with max(|rows|, |cols|) plus signs,
    // and the unmatched lines come in pairs and share line 0
    let mut t = vec![vec![false; n]; n];
    let paired = rows.len().min(cols.len());
    for k in 0..paired {
        t[rows[k]][cols[k]] = true;
    }
    for &r in &rows[paired..] {
        t[r][0] = !t[r][0];
    }
    for &c in &cols[paired..] {
        t[0][c] = !t[0][c];
    }
    let last = n - 1;
    for i in 0..last {
        for j in 0..last {
            if a[i][j] == t[i][j] {
                continue;
            }
            let mut rest = (0..n).filter(|&c| c != j && c != last);
            let mut perm: Vec<usize> = (0..n)
                .map(|r| {
                    if r == i {
                        j
                    } else if r == last {
                        last
                    } else {
                        rest.next().unwrap()
                    }
                })
                .collect();
            flip(&mut a, &perm);
            perm.swap(i, last);
            flip(&mut a, &perm);
        }
    }
    let mut out = String::from("There is solution:\n");
    for perm in &ops {
        let line: Vec<String> = perm.iter().map(|c| (c + 1).to_string()).collect();
        writeln!(out, "{}", line.join(" ")).unwrap();
    }
    print!("{}", out);
}
