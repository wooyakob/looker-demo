import json
import csv

input_path = "/Users/wooyakob/Desktop/looker-demo/data-conversion/exported-support-tickets.json"
output_path = "/Users/wooyakob/Desktop/looker-demo/datasets/exported-support-tickets.csv"

with open(input_path, "r", encoding="utf-8") as infile:
    tickets = json.load(infile)

# Define the CSV columns (headers)
fields = [
    "ID", "Customer", "Contact", "Role", "Product", "Purchased",
    "First Response Time", "Resolution Time", "Satisfaction", "Feedback",
    "User", "Agent"
]

with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    
    for ticket in tickets:
        row = {
            "ID": ticket.get("ID", "No ID"),
            "Customer": ticket.get("Customer", "Unknown Customer"),
            "Contact": ticket.get("Contact", "Unknown Contact"),
            "Role": ticket.get("Role", "Unknown Role"),
            "Product": ticket.get("Product", "No Product"),
            "Purchased": ticket.get("Purchased", "No Purchase Date"),
            "First Response Time": ticket.get("First Response Time", "No Response Time"),
            "Resolution Time": ticket.get("Resolution Time", "No Resolution Time"),
            "Satisfaction": ticket.get("Satisfaction", "No Satisfaction"),
            "Feedback": ticket.get("Feedback", ""),
            "User": ticket.get("User", ""),
            "Agent": ticket.get("Agent", "")
        }
        writer.writerow(row)

print(f"CSV file created at: {output_path}")