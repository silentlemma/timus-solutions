use std::io::{self, Read};

const REACH: i32 = 5;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let (h, w) = (tok.next().unwrap(), tok.next().unwrap());
    let grid: Vec<Vec<i32>> = (0..h)
        .map(|_| tok.by_ref().take(w as usize).collect())
        .collect();
    // the cells at each distance 1..5, as offsets around a crossing
    let mut rings = vec![Vec::new(); REACH as usize + 1];
    for dr in -REACH..=REACH {
        for dc in -REACH..=REACH {
            let d = dr.abs() + dc.abs();
            if (1..=REACH).contains(&d) {
                rings[d as usize].push((dr, dc));
            }
        }
    }
    let mut out = String::new();
    for r in 0..h {
        let row: Vec<String> = (0..w)
            .map(|c| {
                if grid[r as usize][c as usize] != 0 {
                    return -1;
                }
                let mut found = 0;
                for ring in &rings[1..] {
                    for &(dr, dc) in ring {
                        let (rr, cc) = (r + dr, c + dc);
                        // each type counts once however many branches share it
                        if rr >= 0 && rr < h && cc >= 0 && cc < w {
                            found |= grid[rr as usize][cc as usize];
                        }
                    }
                    if found != 0 {
                        break;
                    }
                }
                found
            })
            .map(|v| v.to_string())
            .collect();
        out.push_str(&row.join(" "));
        out.push('\n');
    }
    print!("{}", out);
}
