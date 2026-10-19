use std::io::{self, Read};
use std::str::SplitWhitespace;

const STREETS: &[&str] = &["preflop", "flop", "turn", "river"];

struct Game {
    stack: Vec<i32>,
    bet: Vec<i32>,
    folded: Vec<bool>,
    pending: Vec<bool>,
    dealer: usize,
    cursor: usize,
    street: usize,
    current_bet: i32,
}

impl Game {
    fn reset_pending(&mut self) {
        for i in 0..self.stack.len() {
            self.pending[i] = !self.folded[i] && self.stack[i] > 0;
        }
    }

    fn act(&mut self, player: usize, paid: i32, fold: bool) {
        self.stack[player] -= paid;
        self.bet[player] += paid;
        if fold {
            self.folded[player] = true;
        }
        if self.bet[player] > self.current_bet {
            self.current_bet = self.bet[player];
            self.reset_pending();
        }
        self.pending[player] = false;
        self.cursor = (player + 1) % self.stack.len();
    }

    fn deal(&mut self) {
        self.street += 1;
        self.current_bet = 0;
        self.bet.fill(0);
        self.reset_pending();
        self.cursor = (self.dealer + 1) % self.stack.len();
    }

    fn next_player(&self) -> Option<usize> {
        (0..self.stack.len())
            .map(|offset| (self.cursor + offset) % self.stack.len())
            .find(|&player| self.pending[player] && !self.folded[player] && self.stack[player] > 0)
    }
}

fn number<T: std::str::FromStr>(tokens: &mut SplitWhitespace<'_>) -> T {
    tokens.next().unwrap().parse().ok().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let small_blind: i32 = number(&mut tokens);
    let big_blind: i32 = number(&mut tokens);
    let ante: i32 = number(&mut tokens);
    let count: usize = number(&mut tokens);
    let dealer = number::<usize>(&mut tokens) - 1;
    let bot = number::<usize>(&mut tokens) - 1;
    let target_name = tokens.next().unwrap();
    let target = STREETS
        .iter()
        .position(|&name| name == target_name)
        .unwrap();
    let mut names = Vec::with_capacity(count);
    let mut game = Game {
        stack: vec![0; count],
        bet: vec![0; count],
        folded: vec![false; count],
        pending: vec![false; count],
        dealer,
        cursor: 0,
        street: 0,
        current_bet: big_blind,
    };
    for i in 0..count {
        names.push(tokens.next().unwrap());
        let initial: i32 = number(&mut tokens);
        game.stack[i] = initial - initial.min(ante);
    }
    let small = if count == 2 {
        dealer
    } else {
        (dealer + 1) % count
    };
    let big = (small + 1) % count;
    game.bet[small] = game.stack[small].min(small_blind);
    game.stack[small] -= game.bet[small];
    game.bet[big] = game.stack[big].min(big_blind);
    game.stack[big] -= game.bet[big];
    game.cursor = (big + 1) % count;
    game.reset_pending();

    let known: usize = number(&mut tokens);
    for _ in 0..known {
        let name = tokens.next().unwrap();
        let kind = tokens.next().unwrap();
        if name == "dealing" {
            game.deal();
            continue;
        }
        let player = names
            .iter()
            .position(|&candidate| candidate == name)
            .unwrap();
        let paid = match kind {
            "calls" | "bets" => number(&mut tokens),
            "raises" => {
                let _: i32 = number(&mut tokens);
                tokens.next();
                number::<i32>(&mut tokens) - game.bet[player]
            }
            _ => 0,
        };
        game.act(player, paid, kind == "folds");
    }
    let final_stack: Vec<i32> = (0..count).map(|_| number(&mut tokens)).collect();
    let mut answer = Vec::new();
    loop {
        let player = match game.next_player() {
            Some(player) => player,
            None => {
                game.deal();
                answer.push(format!("dealing {}", STREETS[game.street]));
                continue;
            }
        };
        if player == bot && game.street == target && game.stack == final_stack {
            break;
        }
        let mut paid = game.stack[player] - final_stack[player];
        // Before the next street, only the bot can spend beyond the current bet.
        if game.street != target && player != bot {
            paid = paid.min(game.current_bet - game.bet[player]);
        }
        let fold = paid == 0 && game.bet[player] < game.current_bet;
        let action = if paid == 0 {
            format!(
                "{} {}",
                names[player],
                if fold { "folds" } else { "checks" }
            )
        } else if game.current_bet == 0 {
            format!("{} bets {}", names[player], paid)
        } else if game.bet[player] + paid > game.current_bet {
            let total = game.bet[player] + paid;
            format!(
                "{} raises {} to {}",
                names[player],
                total - game.current_bet,
                total
            )
        } else {
            format!("{} calls {}", names[player], paid)
        };
        answer.push(action);
        game.act(player, paid, fold);
    }
    let mut output = format!("{}\n", answer.len());
    for action in answer {
        output.push_str(&action);
        output.push('\n');
    }
    print!("{}", output);
}
