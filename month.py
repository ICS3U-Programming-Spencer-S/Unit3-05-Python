#!/usr/bin/env python3

# Created by: Spencer Scarlett
# Created on: Oct 13, 2022
# This program checks what month you inputted


def main():
    # user input for month
    months = input("Enter a number that represents a month (1 = January): ")
    print("")

    # Checks the case for the correct month
    match months:
        case "1":
            print("1 = January!")
        case "2":
            print("2 = February!")
        case "3":
            print("3 = March")
        case "4":
            print("4 = April")
        case "5":
            print("5 = May")
        case "6":
            print("6 = June!")
        case "7":
            print("7 = July!")
        case "8":
            print("8 = August")
        case "9":
            print("9 = September")
        case "10":
            print("10 = October")
        case "11":
            print("11 = November")
        case "12":
            print("12 = December")
        # Checker to make sure the code marks if something incorrect is inputted
        case _:
            print("Invalid input, using numbers from 1-12")


if __name__ == "__main__":
    main()
