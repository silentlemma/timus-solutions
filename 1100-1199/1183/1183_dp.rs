use std::io;

fn pair(a: u8, b: u8) -> bool {
    (a == b'(' && b == b')') || (a == b'[' && b == b']')
}

// how[i][j] says how s[i..j] is best made regular: 0 pads a lone bracket,
// -1 wraps a pair, k splits at k
fn build(s: &[u8], how: &[Vec<i32>], i: usize, j: usize, out: &mut String) {
    if i == j {
        return;
    }
    let way = how[i][j];
    if way == 0 {
        out.push_str(if s[i] == b'(' || s[i] == b')' {
            "()"
        } else {
            "[]"
        });
    } else if way < 0 {
        out.push(s[i] as char);
        build(s, how, i + 1, j - 1, out);
        out.push(s[j - 1] as char);
    } else {
        build(s, how, i, way as usize, out);
        build(s, how, way as usize, j, out);
    }
}

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let s = line.trim().as_bytes();
    let n = s.len();
    // add[i][j]: fewest brackets to add so that s[i..j] becomes regular
    let mut add = vec![vec![0; n + 1]; n + 1];
    let mut how = vec![vec![0i32; n + 1]; n + 1];
    for length in 1..=n {
        for i in 0..=n - length {
            let j = i + length;
            if length == 1 {
                add[i][j] = 1;
                continue;
            }
            let (mut best, mut way) = (add[i][i + 1] + add[i + 1][j], (i + 1) as i32);
            if pair(s[i], s[j - 1]) && add[i + 1][j - 1] < best {
                best = add[i + 1][j - 1];
                way = -1;
            }
            for k in i + 2..j {
                if add[i][k] + add[k][j] < best {
                    best = add[i][k] + add[k][j];
                    way = k as i32;
                }
            }
            add[i][j] = best;
            how[i][j] = way;
        }
    }
    let mut out = String::new();
    build(s, &how, 0, n, &mut out);
    println!("{}", out);
}
