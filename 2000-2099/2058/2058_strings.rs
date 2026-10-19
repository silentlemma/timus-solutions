use std::fmt::Write;
use std::io::{self, Read};

fn lookup(first: &[usize], next: &[usize], label: &[usize], node: usize, code: usize) -> usize {
    let mut child = first[node];
    while child != 0 && label[child] != code {
        child = next[child];
    }
    child
}

fn solve(word: &[u8]) -> String {
    let n = word.len();
    let infinity = n as i32 + 1;
    let mut data = vec![0; n + 1];
    data[1..].copy_from_slice(word);
    let mut length = vec![0i32; n + 2];
    let mut link = vec![0usize; n + 2];
    let mut difference = vec![0i32; n + 2];
    let mut series = vec![0usize; n + 2];
    let mut cache_odd = vec![infinity; n + 2];
    let mut cache_even = vec![infinity; n + 2];
    let mut odd = vec![infinity; n + 1];
    let mut even = vec![infinity; n + 1];
    let mut first = vec![0usize; n + 2];
    let mut next = vec![0usize; n + 2];
    let mut label = vec![0usize; n + 2];
    length[0] = -1;
    even[0] = 0;
    let mut nodes = 2;
    let mut last = 1;
    let mut output = String::new();
    for end in 1..=n {
        let letter = data[end];
        let code = (letter - b'a') as usize;
        let mut node = last;
        while data[(end as i32 - length[node] - 1) as usize] != letter {
            node = link[node];
        }
        let mut found = lookup(&first, &next, &label, node, code);
        if found == 0 {
            found = nodes;
            nodes += 1;
            length[found] = length[node] + 2;
            let mut suffix = 1;
            if length[found] != 1 {
                let mut candidate = link[node];
                while data[(end as i32 - length[candidate] - 1) as usize] != letter {
                    candidate = link[candidate];
                }
                suffix = lookup(&first, &next, &label, candidate, code);
            }
            link[found] = suffix;
            difference[found] = length[found] - length[suffix];
            series[found] = if difference[found] == difference[suffix] {
                series[suffix]
            } else {
                suffix
            };
            next[found] = first[node];
            first[node] = found;
            label[found] = code;
        }
        last = found;
        node = last;
        while length[node] > 0 {
            let suffix = link[node];
            let before = end - length[series[node]] as usize - difference[node] as usize;
            cache_odd[node] = odd[before];
            cache_even[node] = even[before];
            if difference[node] == difference[suffix] {
                cache_odd[node] = cache_odd[node].min(cache_odd[suffix]);
                cache_even[node] = cache_even[node].min(cache_even[suffix]);
            }
            odd[end] = odd[end].min(cache_even[node] + 1);
            even[end] = even[end].min(cache_odd[node] + 1);
            node = series[node];
        }
        let a = if odd[end] < infinity { odd[end] } else { -1 };
        let b = if even[end] < infinity { even[end] } else { -2 };
        writeln!(output, "{} {}", a, b).unwrap();
    }
    output
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve(input.trim().as_bytes()));
}
