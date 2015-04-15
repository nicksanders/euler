

fn num_factors(n: usize) -> usize {
    let mut cnt = 0;
    let end = (n as f32).sqrt() as usize;
    for i in (1..end + 1) {
        if n % i == 0 {
            cnt += 2;
        }
    }
    cnt
}

#[allow(dead_code)]
fn factors(n: usize) -> Vec<usize> {
    let mut f = vec![];
    let end = (n as f32).sqrt() as usize;
    for i in (1..end + 1) {
        if n % i == 0 {
            f.push(i);
            f.push(n / i);
        }
    }
    f
}

fn main() {

    let mut num = 1;
    let mut prod: usize;

    loop {
        prod = (1..num + 1).fold(0, |x, sum| sum + x);
        let t = num_factors(prod);
        if t >= 500 {
            break;
        }
        num += 1
    }

    println!("{}", prod);
}
