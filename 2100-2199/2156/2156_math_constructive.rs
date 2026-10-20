use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<u64>().unwrap());
    let n = it.next().unwrap() as usize;
    let a: Vec<u64> = it.take(n).collect();
    // Around the circle the rises and the falls cancel out, so the
    // conversations where the next friend is less interesting sum to the same
    // as those where the next one is more interesting; equal neighbours add 0.
    let (mut falls, mut rises, mut ties) = (Vec::new(), Vec::new(), Vec::new());
    for i in 0..n {
        let next = a[(i + 1) % n];
        if a[i] > next {
            falls.push(i + 1);
        } else if a[i] < next {
            rises.push(i + 1);
        } else {
            ties.push(i + 1);
        }
    }
    if falls.is_empty() {
        // every difference is 0: one conversation against all the others
        falls.push(ties.pop().unwrap());
    }
    rises.extend(ties);
    let mut out = String::from("YES\n");
    for part in [&falls, &rises] {
        out.push_str(&format!("{}\n", part.len()));
        let line: Vec<String> = part.iter().map(|x| x.to_string()).collect();
        out.push_str(&line.join(" "));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
