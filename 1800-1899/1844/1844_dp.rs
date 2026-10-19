use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let tests: usize = it.next().unwrap().parse().unwrap();
    let mut out = String::new();
    for _ in 0..tests {
        let mut num = || it.next().unwrap().parse::<usize>().unwrap();
        let (n, m, k) = (num(), num(), num());
        let mut plans: Vec<Vec<(bool, usize)>> = Vec::new();
        for length in [n, m] {
            let mut plan = Vec::with_capacity(length);
            for _ in 0..length {
                let call = it.next().unwrap() == "+";
                plan.push((call, it.next().unwrap().parse::<usize>().unwrap()));
            }
            plans.push(plan);
        }
        let (sandro, zagamius) = (&plans[0], &plans[1]);
        // cell (i, j): Sandro has done i steps and Zagamius j; it is taken
        // when both offices hold one mage, and a step is blocked exactly when
        // it leads into a taken cell. Row n + 1 is all taken: no step down.
        let mut taken = vec![vec![true; m + 1]; n + 2];
        let mut with_sandro = vec![false; k + 1];
        for i in 0..=n {
            if i > 0 {
                let (call, mage) = sandro[i - 1];
                with_sandro[mage] = call;
            }
            let mut shared = 0i32; // mages in both offices
            for j in 0..=m {
                if j > 0 && with_sandro[zagamius[j - 1].1] {
                    shared += if zagamius[j - 1].0 { 1 } else { -1 };
                }
                taken[i][j] = shared > 0;
            }
        }
        let mut reach = vec![vec![false; m + 1]; n + 1];
        reach[0][0] = true;
        let mut stuck = false;
        'rows: for i in 0..=n {
            for j in 0..=m {
                if !reach[i][j] {
                    continue;
                }
                let down = !taken[i + 1][j];
                let right = j < m && !taken[i][j + 1];
                if !down && !right && (i < n || j < m) {
                    stuck = true;
                    break 'rows;
                }
                if down {
                    reach[i + 1][j] = true;
                }
                if right {
                    reach[i][j + 1] = true;
                }
            }
        }
        out.push_str(if stuck { ":-(\n" } else { ":-)\n" });
    }
    print!("{}", out);
}
