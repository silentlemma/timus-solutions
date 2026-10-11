use std::io::{self, Read};

// a brick and everything it carries: its ends, the total weight (lengths)
// and twice its moment about 0, R^2 - L^2 per brick
#[derive(Clone, Copy)]
struct Brick {
    left: i64,
    right: i64,
    weight: i64,
    moment: i64,
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let layers = it.next().unwrap();
    let mut above: Vec<Brick> = Vec::new();
    for _ in 0..layers {
        let k = it.next().unwrap();
        let mut bricks: Vec<Brick> = (0..k)
            .map(|_| {
                let (left, right) = (it.next().unwrap(), it.next().unwrap());
                Brick {
                    left,
                    right,
                    weight: right - left,
                    moment: right * right - left * left,
                }
            })
            .collect();
        // each brick above rests on the one brick below that it overlaps, and
        // the centre of all it carries must lie strictly inside the overlap, a test
        // that the doubled moment keeps in whole numbers
        let mut j = 0;
        for a in &above {
            while j < bricks.len() && bricks[j].right <= a.left {
                j += 1;
            }
            if j == bricks.len() || bricks[j].left >= a.right {
                println!("No");
                return;
            }
            let lo = a.left.max(bricks[j].left);
            let hi = a.right.min(bricks[j].right);
            if !(2 * lo * a.weight < a.moment && a.moment < 2 * hi * a.weight) {
                println!("No");
                return;
            }
            bricks[j].weight += a.weight;
            bricks[j].moment += a.moment;
        }
        above = bricks;
    }
    println!("Yes");
}
