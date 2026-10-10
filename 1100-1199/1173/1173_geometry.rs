use std::io::{self, Read};

// coordinates have at most three decimals, so in thousandths they are exact
// integers and every turn below is decided without rounding
const SCALE: f64 = 1000.0;
// a friend is given by x, y and the id
const FIELDS: usize = 3;

fn half(p: &(i64, i64, u32)) -> i32 {
    if p.1 > 0 || (p.1 == 0 && p.0 > 0) {
        0
    } else {
        1
    }
}

fn cross(p: &(i64, i64, u32), q: &(i64, i64, u32)) -> i64 {
    p.0 * q.1 - p.1 * q.0
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let tokens: Vec<&str> = input.split_ascii_whitespace().collect();
    let exact = |k: usize| (tokens[k].parse::<f64>().unwrap() * SCALE).round() as i64;
    let (hx, hy) = (exact(0), exact(1));
    let n: usize = tokens[2].parse().unwrap();
    // x, y relative to the house, then the id
    let mut friends: Vec<(i64, i64, u32)> = (0..n)
        .map(|i| {
            let k = FIELDS + FIELDS * i;
            (
                exact(k) - hx,
                exact(k + 1) - hy,
                tokens[k + 2].parse().unwrap(),
            )
        })
        .collect();
    friends.sort_by(|p, q| half(p).cmp(&half(q)).then(0.cmp(&cross(p, q))));
    // consecutive friends by angle, joined in turn, never cross; the house
    // closes the loop across one angular gap, which must be the one wider
    // than half a turn if there is one
    let mut start = 0;
    for i in 0..n {
        if cross(&friends[(i + n - 1) % n], &friends[i]) < 0 {
            start = i;
        }
    }
    let mut out = String::from("0\n");
    for k in 0..n {
        out += &format!("{}\n", friends[(start + k) % n].2);
    }
    out += "0\n";
    print!("{}", out);
}
