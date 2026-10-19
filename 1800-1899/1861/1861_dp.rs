use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let text = words.next().unwrap().as_bytes();
    let name = words.next().unwrap().as_bytes();
    let (n, m) = (text.len(), name.len());
    // the name can be written from position j on when each of its letters
    // lands on that letter or on a "?"
    let fits: Vec<bool> = (0..=n - m)
        .map(|j| (0..m).all(|i| text[j + i] == b'?' || text[j + i] == name[i]))
        .collect();
    // two copies d < m apart agree exactly when d is a period of the name:
    // copies far apart never meet, and a set of copies agrees as soon as
    // each copy agrees with the next one, which covers what lies between
    let mut border = vec![0usize; m];
    let mut k = 0;
    for i in 1..m {
        while k > 0 && name[k] != name[i] {
            k = border[k - 1];
        }
        if name[k] == name[i] {
            k += 1;
        }
        border[i] = k;
    }
    let mut periods = Vec::new();
    let mut k = border[m - 1];
    while k > 0 {
        periods.push(m - k);
        k = border[k - 1];
    }
    // best[j]: the most copies with the last one at j; before[j]: the most
    // with the last one before j
    let mut best = vec![0usize; n - m + 1];
    let mut before = vec![0usize; n - m + 2];
    for j in 0..=n - m {
        if fits[j] {
            let mut previous = if j >= m { before[j - m + 1] } else { 0 };
            for &d in &periods {
                if d <= j {
                    previous = previous.max(best[j - d]);
                }
            }
            best[j] = previous + 1;
        }
        before[j + 1] = before[j].max(best[j]);
    }
    println!("{}", before[n - m + 1]);
}
