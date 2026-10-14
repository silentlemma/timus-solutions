use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text
        .split_ascii_whitespace()
        .map(|w| w.parse::<i64>().unwrap());
    let total = it.next().unwrap() as usize + 2;
    let pts: Vec<(i64, i64)> = (0..total)
        .map(|_| (it.next().unwrap(), it.next().unwrap()))
        .collect();
    // always run to the farthest point not visited yet: the point before had
    // this one as its farthest, so it was at least as far as the next one,
    // which makes every turn acute
    let mut seen = vec![false; total];
    let mut at = 0;
    seen[0] = true;
    let mut path = vec![1];
    for _ in 1..total {
        let (cx, cy) = pts[at];
        let far = (0..total)
            .filter(|&j| !seen[j])
            .max_by_key(|&j| (pts[j].0 - cx).pow(2) + (pts[j].1 - cy).pow(2))
            .unwrap();
        seen[far] = true;
        at = far;
        path.push(far + 1);
    }
    let line: Vec<String> = path.iter().map(|p| p.to_string()).collect();
    println!("YES\n{}", line.join(" "));
}
