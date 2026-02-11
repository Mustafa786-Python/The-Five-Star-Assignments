"""
Movie Ticket Booking System – Key Points

Ticket ID Structure: "MovieCode(3) + Seat(2) + Price(2) + Show(1)"

Example: AVT1215M → Movie: AVT, Seat: 12, Price: 15, Show: M

Tasks:

Extract info from Ticket ID using string slicing and convert price to integer.

Calculate total cost by summing ticket prices for group bookings.

Display details: Movie, Seat, Price (formatted), Show time.

Goal: Provide readable ticket info and total price for multiple tickets.
"""


ticket_ids = ["AVT1215M", "TLR0818E", "HPT1012A"]

total_price = 0

print(f"{"Movie Name":<10} | {"Seat No":<10} | {"Ticket Price":<15} | {"Show Time":<10} |")
print("--" * 50)

for info in ticket_ids:
    movie_code = info[0:3]
    seat_no = info[3:5]
    ticket_price = info[5:7]
    time = info[7:]

    # conversion string to integer
    ticket_price = int(ticket_price)

    total_price += ticket_price

    if time == "M":
        show_time = "Morning"
    if time == "E":
        show_time = "Evening"
    else:
        show_time = "Afternoon"

    print(f"{movie_code:<10} | {seat_no:<10} | ${ticket_price:<15} | {show_time:<10} |")

print(f"Total Cost: ${total_price}")
