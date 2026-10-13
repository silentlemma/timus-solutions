use std::io::{self, Read, Write};

// bridgeless cubic maps with the whole border built, found by a search
const BLOCKS: &[&[&str]] = &[
    &[
        r"O-O-O-O", r"|\|/ /|", r"O O O-O", r"|\   \|", r"O-O O O", r"|/ /|\|", r"O-O-O-O",
    ],
    &[
        r"O-O-O-O", r"|\ \|/|", r"O-O O O", r"| |  /|", r"O-O-O-O", r"|     |", r"O-O O-O",
        r"|/| |\|", r"O-O-O-O",
    ],
    &[
        r"O-O-O-O", r"|\|/ /|", r"O O O-O", r"|\   \|", r"O-O-O O", r"|   |\|", r"O-O O O",
        r"|/|/ \|", r"O O O O", r"|/ /|\|", r"O-O-O-O",
    ],
    &[
        r"O-O-O-O", r"|\ \|/|", r"O O O O", r"|\|\ /|", r"O O O-O", r"|\|   |", r"O-O O-O",
        r"|   |\|", r"O-O-O O", r"| |  \|", r"O-O O O", r"|/ /|\|", r"O-O-O-O",
    ],
    &[
        r"O-O-O-O-O-O",
        r"|\ \|  \|/|",
        r"O-O O-O O O",
        r"| |  /|  /|",
        r"O-O O O O-O",
        r"|/ /| |\ \|",
        r"O-O-O-O-O-O",
    ],
    &[
        r"O-O-O-O-O-O",
        r"|\ \ \ \|/|",
        r"O-O-O O O O",
        r"|    \|\ /|",
        r"O-O-O-O O O",
        r"| | |  / /|",
        r"O-O O O O-O",
        r"|/ /| |\ \|",
        r"O-O-O-O-O-O",
    ],
    &[
        r"O-O-O-O-O-O",
        r"|\|  \| |/|",
        r"O-O O O-O O",
        r"|  /|\   /|",
        r"O-O-O O O-O",
        r"|  / /|/  |",
        r"O O-O O O-O",
        r"|\ \ \|/ \|",
        r"O-O O O O O",
        r"|/ /|  /|\|",
        r"O-O-O-O-O-O",
    ],
    &[
        r"O-O-O-O-O-O",
        r"|\| |  \|/|",
        r"O-O O O O O",
        r"|  /|/|\ /|",
        r"O-O-O O-O O",
        r"|     |  /|",
        r"O-O-O O O-O",
        r"| | |\|\| |",
        r"O-O O O O-O",
        r"|  \|\ \  |",
        r"O-O O O O-O",
        r"|/| | |\ \|",
        r"O-O-O-O-O-O",
    ],
    &[
        r"O-O-O-O-O-O-O-O",
        r"|\ \ \| | |/ /|",
        r"O-O O O O O O-O",
        r"|/ /| | |\ \ \|",
        r"O-O-O-O-O-O-O-O",
    ],
    &[
        r"O-O-O-O-O-O-O-O-O-O",
        r"|\ \ \|  \| |/ / /|",
        r"O-O O O O-O O O O-O",
        r"|/ /| | |\  | |\ \|",
        r"O-O-O-O-O-O-O-O-O-O",
    ],
    &[
        r"O-O-O-O-O-O-O-O-O-O-O-O",
        r"|\ \ \ \|/ /  | | |/ /|",
        r"O-O O O O O-O O-O O O-O",
        r"|/ /| |\  | |\ \ \ \ \|",
        r"O-O-O-O-O-O-O-O-O-O-O-O",
    ],
    &[
        r"O-O-O-O-O-O-O-O-O-O-O-O-O-O",
        r"|\ \| |/   \ \|/ /  |/ / /|",
        r"O-O O O O-O-O O O O-O O O-O",
        r"|/ / / /| | |  /| |\  |\ \|",
        r"O-O-O-O-O-O-O-O-O-O-O-O-O-O",
    ],
];
const MIN_SIDE: usize = 3;
const FLAT: usize = 3; // a strip this high needs at least FLAT_STEP columns
const FLAT_STEP: usize = 8;
const FLAT_TOP: usize = 14;
const STEP: usize = 4;
const WIDE_TOP: usize = 6;
const TALL_TOP: usize = 7;
const NO_WORLD: &str = "Imaginary world";

fn split(mut n: usize, step: usize, top: usize) -> Vec<usize> {
    let mut parts = Vec::new();
    while n > top {
        parts.push(step);
        n -= step;
    }
    parts.push(n);
    parts
}

fn shape(w: usize, h: usize) -> &'static [&'static str] {
    BLOCKS
        .iter()
        .find(|b| b[0].len() / 2 + 1 == w && b.len() / 2 + 1 == h)
        .unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (mut w, mut h) = (v[0], v[1]);
    if w * h % 2 == 1 || w.min(h) < MIN_SIDE {
        println!("{}", NO_WORLD);
        return;
    }
    let turned = w % 2 == 1; // then h is even: build the turned map
    if turned {
        std::mem::swap(&mut w, &mut h);
    }
    let (widths, heights) = if h == FLAT {
        if w < FLAT_STEP {
            println!("{}", NO_WORLD);
            return;
        }
        (split(w, FLAT_STEP, FLAT_TOP), vec![FLAT])
    } else {
        (split(w, STEP, WIDE_TOP), split(h, STEP, TALL_TOP))
    };
    let mut grid = vec![vec![b' '; 2 * w - 1]; 2 * h - 1];
    let mut top = 0;
    for (j, &bh) in heights.iter().enumerate() {
        let mut left = 0;
        for (i, &bw) in widths.iter().enumerate() {
            let (y, x) = (2 * top, 2 * left);
            for (r, row) in shape(bw, bh).iter().enumerate() {
                grid[y + r][x..x + row.len()].copy_from_slice(row.as_bytes());
            }
            if i > 0 {
                // two vertical bridges at the seam, in the lowest two rows,
                // give way to two horizontal ones
                let z = 2 * (top + bh - 2);
                grid[z + 1][x - 2] = b' ';
                grid[z + 1][x] = b' ';
                grid[z][x - 1] = b'-';
                grid[z + 2][x - 1] = b'-';
            }
            left += bw;
        }
        if j > 0 {
            // the same exchange across a horizontal seam, in the last two columns
            let (y, x) = (2 * top, 2 * (w - 2));
            grid[y - 2][x + 1] = b' ';
            grid[y][x + 1] = b' ';
            grid[y - 1][x] = b'|';
            grid[y - 1][x + 2] = b'|';
        }
        top += bh;
    }
    if turned {
        let flipped: Vec<Vec<u8>> = (0..grid[0].len())
            .map(|c| {
                grid.iter()
                    .map(|row| match row[c] {
                        b'-' => b'|',
                        b'|' => b'-',
                        ch => ch,
                    })
                    .collect()
            })
            .collect();
        grid = flipped;
    }
    let mut out = Vec::new();
    for row in &grid {
        out.extend_from_slice(row);
        out.push(b'\n');
    }
    io::stdout().write_all(&out).unwrap();
}
