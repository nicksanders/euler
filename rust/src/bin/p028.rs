
fn main() {

    let mut num = 1;
    let mut diag1 = 1;
    let mut diag2 = 0;
    let mut step = 2;

    for _ in (0..500) {
        for s in (1..5) {
            num += step;
            if s % 2 == 0 {
                diag1 += num;
            } else {
                diag2 += num;
            }
        }
        step += 2;
    }

    println!("{}", diag1 + diag2);

}
