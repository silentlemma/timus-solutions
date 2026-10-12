use std::io::{self, Read, Write};

// pair the children along the likes from start, two by two; on an odd
// path the last one, who likes nobody, stays free
fn pair_along(
    start: usize,
    likes: &[Option<usize>],
    seen: &mut [bool],
    partner: &mut [Option<usize>],
) {
    let mut chain = Vec::new();
    let mut v = Some(start);
    while let Some(u) = v {
        if seen[u] {
            break;
        }
        seen[u] = true;
        chain.push(u);
        v = likes[u];
    }
    for pair in chain.chunks_exact(2) {
        partner[pair[0]] = Some(pair[1]);
        partner[pair[1]] = Some(pair[0]);
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let k = it.next().unwrap();
    // children 0..k-1 are boys and k..2k-1 girls; likes[v] is the child v
    // likes; nobody is liked by two, so the likes form paths and cycles
    let mut likes = vec![None; 2 * k];
    let mut liked = vec![false; 2 * k];
    for i in 0..2 * k {
        let x = it.next().unwrap();
        if x != 0 {
            let target = if i < k { k + x - 1 } else { x - 1 };
            likes[i] = Some(target);
            liked[target] = true;
        }
    }
    let mut seen = vec![false; 2 * k];
    let mut partner = vec![None; 2 * k];
    for v in 0..2 * k {
        if !liked[v] {
            pair_along(v, &likes, &mut seen, &mut partner);
        }
    }
    for v in 0..2 * k {
        if !seen[v] {
            // what is left are cycles, always of even length
            pair_along(v, &likes, &mut seen, &mut partner);
        }
    }
    // the free children like nobody and can be paired in any way
    let mut g = k;
    for b in 0..k {
        if partner[b].is_some() {
            continue;
        }
        while partner[g].is_some() {
            g += 1;
        }
        partner[b] = Some(g);
        partner[g] = Some(b);
    }
    let words: Vec<String> = (0..k)
        .map(|i| (partner[i].unwrap() - k + 1).to_string())
        .collect();
    let mut out = words.join(" ");
    out.push('\n');
    io::stdout().write_all(out.as_bytes()).unwrap();
}
