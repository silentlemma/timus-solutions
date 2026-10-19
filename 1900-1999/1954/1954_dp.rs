use std::io::{self, Read};

const ALPHABET: usize = 26;
const TARGET: usize = 5;
const INF: usize = TARGET + 1;
const OUTER_SPLIT: usize = 3;
#[derive(Clone)]
struct Node {
    next: [usize; ALPHABET],
    length: isize,
    link: usize,
    diff: usize,
    series: usize,
    best: [usize; 2],
    start: [usize; 2],
}
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let text = input.trim().as_bytes();
    let n = text.len();
    let mut data = vec![0];
    data.extend_from_slice(text);
    let blank = Node {
        next: [0; ALPHABET],
        length: 0,
        link: 0,
        diff: 0,
        series: 0,
        best: [INF; 2],
        start: [0; 2],
    };
    let mut tree = vec![blank; n + 2];
    tree[0].length = -1;
    let mut best = vec![[INF; 2]; n + 1];
    let mut parent = vec![[0; 2]; n + 1];
    best[0][0] = 0;
    let (mut count, mut last) = (2, 1);
    for i in 1..=n {
        let code = (data[i] - b'a') as usize;
        let mut current = last;
        while data[(i as isize - tree[current].length - 1) as usize] != data[i] {
            current = tree[current].link;
        }
        let mut following = tree[current].next[code];
        if following == 0 {
            following = count;
            count += 1;
            tree[current].next[code] = following;
            tree[following].length = tree[current].length + 2;
            let link = if tree[following].length == 1 {
                1
            } else {
                let mut suffix = tree[current].link;
                while data[(i as isize - tree[suffix].length - 1) as usize] != data[i] {
                    suffix = tree[suffix].link;
                }
                tree[suffix].next[code]
            };
            tree[following].link = link;
            let diff = (tree[following].length - tree[link].length) as usize;
            tree[following].diff = diff;
            tree[following].series = if diff == tree[link].diff {
                tree[link].series
            } else {
                link
            };
        }
        last = following;
        let mut v = last;
        while tree[v].length > 0 {
            let base = i - tree[tree[v].series].length as usize - tree[v].diff;
            let suffix = tree[v].link;
            for p in 0..2 {
                tree[v].best[p] = best[base][p];
                tree[v].start[p] = base;
                if tree[v].diff == tree[suffix].diff && tree[suffix].best[p] < tree[v].best[p] {
                    tree[v].best[p] = tree[suffix].best[p];
                    tree[v].start[p] = tree[suffix].start[p];
                }
                if tree[v].best[p] + 1 < best[i][p ^ 1] {
                    best[i][p ^ 1] = tree[v].best[p] + 1;
                    parent[i][p ^ 1] = tree[v].start[p];
                }
            }
            v = tree[v].series;
        }
    }
    if best[n][1] > TARGET {
        println!("NO");
        return;
    }
    let mut result: Vec<&[u8]> = Vec::new();
    let (mut position, mut parity) = (n, 1);
    while position > 0 {
        let before = parent[position][parity];
        result.push(&text[before..position]);
        position = before;
        parity ^= 1;
    }
    result.reverse();
    while result.len() < TARGET {
        if let Some(index) = result.iter().position(|part| part.len() >= OUTER_SPLIT) {
            let part = result[index];
            result.splice(
                index..index + 1,
                [
                    &part[..1],
                    &part[1..part.len() - 1],
                    &part[part.len() - 1..],
                ],
            );
        } else {
            let mut next = Vec::new();
            let mut remaining = 2;
            for part in result {
                if part.len() == 2 && remaining > 0 {
                    next.push(&part[..1]);
                    next.push(&part[1..]);
                    remaining -= 1;
                } else {
                    next.push(part);
                }
            }
            result = next;
        }
    }
    let mut output = String::from("YES\n");
    for part in result {
        output.push_str(std::str::from_utf8(part).unwrap());
        output.push('\n');
    }
    print!("{}", output);
}
