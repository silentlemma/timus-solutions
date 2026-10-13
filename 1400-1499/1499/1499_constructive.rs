use std::fmt::Write as _;
use std::io::{self, Read};

/// A convex face is cut into triangles by diagonals from its first vertex,
/// as the first and the last of its sides already exist.
fn fan(face: &[usize], cuts: &mut Vec<(usize, usize)>) {
    for &w in face.iter().take(face.len().saturating_sub(1)).skip(2) {
        cuts.push((face[0], w));
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let (n, k) = (it.next().unwrap(), it.next().unwrap());
    let mut ending = vec![Vec::new(); n + 1]; // the cuts u-v with u < v, kept at v
    for _ in 0..k {
        let (a, b) = (it.next().unwrap(), it.next().unwrap());
        ending[a.max(b)].push(a.min(b));
    }
    let mut cuts = Vec::new();
    // walk the vertices in order: a cut u-v closes the face formed by u,
    // the vertices still stacked above it, and v; nearer u first
    let mut stack: Vec<usize> = Vec::new();
    for v in 1..=n {
        stack.push(v);
        let mut starts = std::mem::take(&mut ending[v]);
        starts.sort_unstable_by(|a, b| b.cmp(a));
        for u in starts {
            stack.pop();
            let start = stack.iter().rposition(|&x| x == u).unwrap();
            let mut face = stack[start..].to_vec();
            face.push(v);
            fan(&face, &mut cuts);
            stack.truncate(start + 1);
            stack.push(v);
        }
    }
    fan(&stack, &mut cuts); // the last face, closed by the side n-1
    let mut out = format!("{}\n", cuts.len());
    for (a, b) in cuts {
        writeln!(out, "{} {}", a, b).unwrap();
    }
    print!("{}", out);
}
