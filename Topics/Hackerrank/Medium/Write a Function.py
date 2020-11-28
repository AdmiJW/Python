
def is_leap( year: int ) -> bool:
    # Proposition:
    # A year is leap -> (year not evenly divide by 100 OR can evenly divide 400) AND divisible by 4
    return (year % 100 or not year % 400) and not year % 4


if __name__ == '__main__':
    print( is_leap( int(input() ) ) )