use std::io::{self, Read, Write};

// Marks everything reachable from root that is not marked yet; returns how
// many vertices it marked.
fn search(root: usize, start: &[usize], edges: &[u32], seen: &mut [bool]) -> usize {
    let mut queue = vec![root];
    seen[root] = true;
    let mut head = 0;
    while head < queue.len() {
        let u = queue[head];
        head += 1;
        for &v in &edges[start[u]..start[u + 1]] {
            let v = v as usize;
            if !seen[v] {
                seen[v] = true;
                queue.push(v);
            }
        }
    }
    queue.len()
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let mut numbers = input
        .split(|c| !c.is_ascii_digit())
        .filter(|t| !t.is_empty())
        .map(|t| t.iter().fold(0usize, |v, &c| v * 10 + (c - b'0') as usize));
    let n = numbers.next().unwrap();
    let mut start = vec![0; n + 1];
    let mut edges: Vec<u32> = Vec::new();
    for i in 0..n {
        for v in numbers.by_ref() {
            if v == 0 {
                break;
            }
            edges.push((v - 1) as u32);
        }
        start[i + 1] = edges.len();
    }
    // the reverse graph in the same compact form, built by counting
    let mut rstart = vec![0; n + 1];
    let mut redges = vec![0u32; edges.len()];
    for &v in &edges {
        rstart[v as usize + 1] += 1;
    }
    for i in 0..n {
        rstart[i + 1] += rstart[i];
    }
    let mut fill = rstart[..n].to_vec();
    for u in 0..n {
        for &v in &edges[start[u]..start[u + 1]] {
            let v = v as usize;
            redges[fill[v]] = u as u32;
            fill[v] += 1;
        }
    }

    // nobody outside the marked set can reach the root of the last search,
    // so that root lies in a strongly connected component with no way in
    let mut seen = vec![false; n];
    let mut root = 0;
    for u in 0..n {
        if !seen[u] {
            root = u;
            search(u, &start, &edges, &mut seen);
        }
    }
    let mut out = String::new();
    if search(root, &start, &edges, &mut vec![false; n]) == n {
        let mut backward = vec![false; n];
        search(root, &rstart, &redges, &mut backward);
        for u in 0..n {
            if backward[u] {
                out += &format!("{} ", u + 1);
            }
        }
    }
    out += "0\n";
    io::stdout().write_all(out.as_bytes()).unwrap();
}
