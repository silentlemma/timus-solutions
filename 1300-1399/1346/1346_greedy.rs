use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let data: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let count = (data[1] - data[0] + 1) as usize;
    let f = &data[2..2 + count];
    let (mut pieces, mut i) = (0, 0);
    while i < count {
        // stretch this piece while it stays monotone; its way up or down is
        // fixed by its first step that is not flat
        pieces += 1;
        let (mut way, mut j) = (0, i);
        while j + 1 < count {
            let step = (f[j + 1] - f[j]).signum();
            if step != 0 && way != 0 && step != way {
                break;
            }
            if way == 0 {
                way = step;
            }
            j += 1;
        }
        i = j + 1;
    }
    println!("{}", pieces);
}
