use std::io::{self, Read, Write};

const ALPHABET_SIZE: usize = 26;

#[derive(Default)]
struct Node {
    next: [u32; ALPHABET_SIZE],
    length: i32,
    link: usize,
    diff: i32,
    series: usize,
    cache: u32,
}

fn solve(word: &[u8]) -> Vec<u32> {
    let n = word.len();
    let mut text = Vec::with_capacity(n + 1);
    text.push(0);
    text.extend_from_slice(word);
    let mut nodes = Vec::with_capacity(n + 2);
    nodes.push(Node {
        length: -1,
        ..Node::default()
    });
    nodes.push(Node::default());
    let mut dp = vec![0_u32; n + 1];
    dp[0] = 1;
    let mut last = 1;
    for i in 1..=n {
        let mut parent = last;
        let c = (text[i] - b'a') as usize;
        while text[(i as i32 - 1 - nodes[parent].length) as usize] != text[i] {
            parent = nodes[parent].link;
        }
        if nodes[parent].next[c] == 0 {
            let v = nodes.len();
            nodes[parent].next[c] = v as u32;
            let length = nodes[parent].length + 2;
            let suffix = if length == 1 {
                1
            } else {
                let mut candidate = nodes[parent].link;
                while text[(i as i32 - 1 - nodes[candidate].length) as usize] != text[i] {
                    candidate = nodes[candidate].link;
                }
                nodes[candidate].next[c] as usize
            };
            let diff = length - nodes[suffix].length;
            let series = if diff == nodes[suffix].diff {
                nodes[suffix].series
            } else {
                suffix
            };
            nodes.push(Node {
                length,
                link: suffix,
                diff,
                series,
                ..Node::default()
            });
        }
        last = nodes[parent].next[c] as usize;
        let mut value = 0_u32;
        let mut v = last;
        while nodes[v].length > 0 {
            let cut = i - nodes[nodes[v].series].length as usize - nodes[v].diff as usize;
            let suffix = nodes[v].link;
            let cached = dp[cut]
                | if nodes[v].diff == nodes[suffix].diff {
                    nodes[suffix].cache
                } else {
                    0
                };
            nodes[v].cache = cached;
            value |= cached << 1;
            v = nodes[v].series;
        }
        dp[i] = value;
    }
    dp
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let dp = solve(input.trim().as_bytes());
    let mut out = io::BufWriter::new(io::stdout().lock());
    for value in dp.iter().skip(1) {
        writeln!(&mut out, "{}", value >> 1).unwrap();
    }
}
