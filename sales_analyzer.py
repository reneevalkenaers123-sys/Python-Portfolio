import csv

while True:
    print("\n--- SALES ANALYZER ---")
    print("1. Total Sales")
    print("2. Sports Products")
    print("3. Best Product")
    print("4. Stop")

    choice = input("Choose option: ")

    if choice == "1":
        total_sales = 0

        with open("sales_data.csv", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                total_sales += int(row["Sales"])

        print("Total Sales =", total_sales)

    elif choice == "2":
        with open("sales_data.csv", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Category"] == "Sports":
                    print(row["Product"], row["Sales"])

    elif choice == "3":
        highest_sales = 0
        best_product = ""

        with open("sales_data.csv", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                sales = int(row["Sales"])

                if sales > highest_sales:
                    highest_sales = sales
                    best_product = row["Product"]

        print("Best Product =", best_product)
        print("Highest Sales =", highest_sales)

    elif choice == "4":
        print("Program stopped.")
        break

    else:
        print("Invalid choice.")
