import datetime

def generate_invoice_number():
    # Get the current year and month as a string in the format YYYYMM
    year_month = datetime.datetime.now().strftime("%Y%m")

    # Read the current invoice number from a file, or create a new file if it doesn't exist
    try:
        with open("invoice_number.txt", "r") as f:
            current_number = int(f.read())
    except FileNotFoundError:
        current_number = 1

    # Create the new invoice number by combining the year-month prefix, the incrementing number, and the "INV" prefix
    invoice_number = f"{year_month}{current_number:04d}"
    invoice_number = f"INV{invoice_number}"
    
    # Increment the current invoice number and write it back to the file
    if current_number == 9999:
        with open("invoice_number.txt", "w") as f:
            f.write(str(1))
    else:
        with open("invoice_number.txt", "w") as f:
            f.write(str(current_number + 1))

    return invoice_number

# Example usage
invoice_number = generate_invoice_number()
print("Invoice number:", invoice_number)