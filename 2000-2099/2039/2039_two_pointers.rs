use std::io::{self, Read};

fn solve(grid: &[Vec<u8>], k: usize) -> i64 {
    let (n, m) = (grid.len(), grid[0].len());
    if k > n.min(m) {
        return 0;
    }
    let mut columns = vec![vec![b'0'; n]; m];
    for (r, row) in grid.iter().enumerate() {
        for (c, &value) in row.iter().enumerate() {
            columns[c][r] = value;
        }
    }
    let mut answer = 0i64;
    for diagonal in 1 - n as isize..m as isize {
        let r0 = (-diagonal).max(0) as usize;
        let c0 = diagonal.max(0) as usize;
        let (mut start, mut pr, mut pc, mut br, mut bc) =
            (0usize, None::<usize>, None::<usize>, 0usize, 0usize);
        for at in 0..(n - r0).min(m - c0) {
            let (r, c) = (r0 + at, c0 + at);
            loop {
                let (rs, cs) = (r0 + start, c0 + start);
                let last = grid[r][cs..c]
                    .iter()
                    .rposition(|&x| x == b'0')
                    .map(|x| x + cs);
                let valid =
                    last.is_none() || pr.is_none() || grid[r][cs..c] == grid[pr.unwrap()][cs..c];
                if valid {
                    let (mut nrp, mut ncp) = (pr, pc);
                    if let Some(last) = last {
                        nrp = Some(r);
                        if pr.is_none() {
                            ncp = Some(last);
                        }
                    }
                    let last_row = columns[c][rs..=r]
                        .iter()
                        .rposition(|&x| x == b'0')
                        .map(|x| x + rs);
                    let valid = last_row.is_none()
                        || nrp.is_none()
                        || columns[c][rs..=r] == columns[ncp.unwrap()][rs..=r];
                    if valid {
                        if let Some(last_row) = last_row {
                            nrp = Some(last_row);
                            ncp = Some(c);
                        }
                        let length = at - start + 1;
                        let (nr, nc) = if pr.is_some() {
                            (
                                br + usize::from(grid[r][ncp.unwrap()] == b'1'),
                                bc + usize::from(columns[c][nrp.unwrap()] == b'1'),
                            )
                        } else if nrp.is_none() {
                            (length, length)
                        } else if last.is_some() {
                            (
                                length - 1,
                                grid[r][cs..=c].iter().filter(|&&x| x == b'1').count(),
                            )
                        } else {
                            (
                                columns[c][rs..=r].iter().filter(|&&x| x == b'1').count(),
                                length - 1,
                            )
                        };
                        if nr <= k && nc <= k {
                            pr = nrp;
                            pc = ncp;
                            br = nr;
                            bc = nc;
                            break;
                        }
                    }
                }
                let old_size = at - start;
                if pr.is_none() || pr == Some(rs) || pc == Some(cs) {
                    pr = None;
                    pc = None;
                    br = old_size - 1;
                    bc = old_size - 1;
                } else {
                    br -= usize::from(grid[rs][pc.unwrap()] == b'1');
                    bc -= usize::from(grid[pr.unwrap()][cs] == b'1');
                }
                start += 1;
            }
            let bound = at - start + 1;
            if bound >= k && (pr.is_none() || pr.unwrap() < r + 1 - k || pc.unwrap() < c + 1 - k) {
                answer += 1;
            }
            if bound > k && br == k && bc == k && pr.is_some() {
                let (pr, pc) = (pr.unwrap(), pc.unwrap());
                let first_r = r0
                    + start
                    + columns[pc][r0 + start..=r]
                        .iter()
                        .position(|&x| x == b'1')
                        .unwrap();
                let first_c = c0
                    + start
                    + grid[pr][c0 + start..=c]
                        .iter()
                        .position(|&x| x == b'1')
                        .unwrap();
                let high = (at - k)
                    .min(first_r - r0)
                    .min(first_c - c0)
                    .min(pr - r0)
                    .min(pc - c0);
                if high >= start {
                    answer += (high - start + 1) as i64;
                }
            }
        }
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let _m: usize = tokens.next().unwrap().parse().unwrap();
    let k: usize = tokens.next().unwrap().parse().unwrap();
    let grid: Vec<Vec<u8>> = (0..n)
        .map(|_| tokens.next().unwrap().as_bytes().to_vec())
        .collect();
    println!("{}", solve(&grid, k));
}
