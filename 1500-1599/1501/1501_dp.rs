use std::io::{self, Read};

fn balance(pile: &[u8]) -> Vec<i32> {
    let mut d = vec![0i32];
    for &card in pile {
        d.push(d[d.len() - 1] + if card == b'1' { 1 } else { -1 });
    }
    d
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    // after taking i cards of the first pile and j of the second, the red and
    // the black piles differ by d1[i] + d2[j], where d = 2 * reds - taken
    let d1 = balance(it.next().unwrap().as_bytes());
    let d2 = balance(it.next().unwrap().as_bytes());
    // reach[i][j]: the state is allowed and comes from (i - 1, j) or (i, j - 1)
    let mut reach = vec![vec![false; n + 1]; n + 1];
    for i in 0..=n {
        for j in 0..=n {
            if (d1[i] + d2[j]).abs() > 1 {
                continue;
            }
            reach[i][j] =
                (i == 0 && j == 0) || (i > 0 && reach[i - 1][j]) || (j > 0 && reach[i][j - 1]);
        }
    }
    if !reach[n][n] {
        println!("Impossible");
        return;
    }
    // walk back from (n, n): a step left took a card of the second pile
    let mut moves = Vec::with_capacity(2 * n);
    let (mut i, mut j) = (n, n);
    while i > 0 || j > 0 {
        if j > 0 && reach[i][j - 1] {
            moves.push(b'2');
            j -= 1;
        } else {
            moves.push(b'1');
            i -= 1;
        }
    }
    moves.reverse();
    println!("{}", String::from_utf8(moves).unwrap());
}
