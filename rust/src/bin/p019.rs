
fn get_months(year: usize) -> [usize; 12] {
    if (year % 4 == 0 && year % 100 != 0) || year % 400 == 0 {
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    } else {
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    }
}

fn main() {

    let mut total = 0;
    let mut start_day = 2;
    let week_days = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6];

    for year in (1901..2001) {
        for month in get_months(year).iter() {
            if start_day == 0 {
                total += 1;
            }
            start_day = week_days[(month % 7) + start_day];
        }
    }

    println!("{}", total);

}
