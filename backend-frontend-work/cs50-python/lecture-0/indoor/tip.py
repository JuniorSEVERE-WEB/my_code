def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    dSansSignDollar = d.replace("$", "")
    return float(dSansSignDollar)


def percent_to_float(p):
    # TODO
    PSansPercent = p.replace("%", "")
    pConverted = float(PSansPercent) / 100
    return pConverted


main()