use std::io::{self, Read, Write};

const CORNERS: usize = 4;

fn find(parent: &mut [usize], mut x: usize) -> usize {
    while parent[x] != x {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    x
}

fn union(parent: &mut [usize], a: usize, b: usize) {
    let (a, b) = (find(parent, a), find(parent, b));
    if a != b {
        parent[a] = b;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut pic: Vec<&[u8]> = input
        .split('\n')
        .map(|l| l.trim_end_matches('\r').as_bytes())
        .collect();
    while pic.last().map_or(false, |l| l.is_empty()) {
        pic.pop();
    }
    let h = pic.len();
    let w = pic.iter().map(|l| l.len()).max().unwrap_or(0);
    // walls run along the middle lines of the cells, so the four quarters
    // around a corner of the grid always meet: the corners are the places
    // an agent can be, and a cell joins some of its four corners
    let side = w + 1;
    let mut parent: Vec<usize> = (0..(h + 1) * side).collect();
    let p = &mut parent;
    let mut secrets = Vec::new();
    for (r, row) in pic.iter().enumerate() {
        let (top, bottom) = (r * side, (r + 1) * side);
        for (c, &ch) in row.iter().enumerate() {
            match ch {
                b'.' => {
                    union(p, top + c, top + c + 1);
                    union(p, top + c, bottom + c);
                    union(p, top + c, bottom + c + 1);
                }
                b'-' => {
                    // keeps the upper and the lower pair apart
                    union(p, top + c, top + c + 1);
                    union(p, bottom + c, bottom + c + 1);
                }
                b'|' => {
                    // keeps the left and the right pair apart
                    union(p, top + c, bottom + c);
                    union(p, top + c + 1, bottom + c + 1);
                }
                b'#' => secrets.push((r, std::cmp::Reverse(c), top + c)),
                _ => {}
            }
        }
    }
    // numbered from the top, and from the right within a row
    secrets.sort();
    // an agent may not pass through a secret, so two secrets are joined when
    // some corner of one shares a region with some corner of the other
    let regions: Vec<[usize; CORNERS]> = secrets
        .iter()
        .map(|&(_, _, v)| {
            [
                find(p, v),
                find(p, v + 1),
                find(p, v + side),
                find(p, v + side + 1),
            ]
        })
        .collect();
    let mut out = String::new();
    for a in &regions {
        for b in &regions {
            let shared = a.iter().any(|x| b.contains(x));
            out.push(if shared { '1' } else { '0' });
        }
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
