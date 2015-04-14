
fn main() {

    let mut i = 2;
    let mut n = 600851475143u64;

    while i * i < n {
        while n % i == 0 {
            n /= i;
        }
        i += 1;
    }

    println!("{}", n)

}
