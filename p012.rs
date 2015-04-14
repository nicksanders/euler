
fn num_divisors(n: usize) -> usize {
    let mut cnt = 0;
    for i in (1..n + 1) {
        if n % i == 0 {
            cnt += 1;
        }
    }
    cnt
}

fn main() {

    let mut num = 1;
    let mut prod: usize;

    loop {
        prod = (1..num + 1).fold(0, |x, sum| sum + x);
        let t = num_divisors(prod);
        if t >= 500 {
            break;
        }
        println!("{} {}", prod, t);
        num += 1
    }

    println!("{}", prod);
}
