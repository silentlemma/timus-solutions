use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let mut out = format!("{}\n", n * n + n / 2 + 1);
    // a chessboard: the large numbers go down on one colour and the small
    // ones up on the other, both in reading order
    let (mut big, mut small) = (n * n, 1);
    for i in 0..n {
        let row: Vec<String> = (0..n)
            .map(|j| {
                if (i + j) % 2 == 0 {
                    big -= 1;
                    (big + 1).to_string()
                } else {
                    small += 1;
                    (small - 1).to_string()
                }
            })
            .collect();
        out.push_str(&row.join(" "));
        out.push('\n');
    }
    print!("{}", out);
}
