use std::io::{self, Read};

struct ProductWindow {
    bound: u64,
    product: u64,
    left: usize,
}

impl ProductWindow {
    fn new(bound: u64) -> Self {
        Self {
            bound,
            product: 1,
            left: 0,
        }
    }

    fn advance(&mut self, values: &[u64], index: usize) {
        let value = values[index];
        if value > self.bound {
            self.left = index + 1;
            self.product = 1;
            return;
        }
        // Divide before multiplying to keep the product within the bound.
        while self.product > self.bound / value {
            self.product /= values[self.left];
            self.left += 1;
        }
        self.product *= value;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let lower: u64 = tokens.next().unwrap().parse().unwrap();
    let upper: u64 = tokens.next().unwrap().parse().unwrap();
    let values: Vec<u64> = tokens.map(|token| token.parse().unwrap()).collect();

    let unreachable = n + 1;
    let mut dp = vec![unreachable; n + 1];
    dp[0] = 0;
    let mut queue = vec![0; n + 1];
    let mut head = 0;
    let mut tail = 0;
    let mut next_cut = 0;
    let mut large = ProductWindow::new(upper);
    let mut small = ProductWindow::new(lower - 1);
    for i in 0..n {
        large.advance(&values, i);
        small.advance(&values, i);
        // Eligible cuts form a moving interval, so a minimum deque is enough.
        while next_cut < small.left && next_cut <= i {
            if dp[next_cut] != unreachable {
                while head < tail && dp[queue[tail - 1]] >= dp[next_cut] {
                    tail -= 1;
                }
                queue[tail] = next_cut;
                tail += 1;
            }
            next_cut += 1;
        }
        while head < tail && queue[head] < large.left {
            head += 1;
        }
        if head < tail {
            dp[i + 1] = dp[queue[head]] + 1;
        }
    }
    if dp[n] == unreachable {
        println!("-1");
    } else {
        println!("{}", dp[n]);
    }
}
