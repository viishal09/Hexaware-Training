def generate_order_confirmation_email(customer_name, order_number, delivery_address, expected_delivery_date):
    email_body = (f"Dear {customer_name},\n\nOrder Number: "
                  f"{order_number}\nDelivery Address: {delivery_address}\nExpected Delivery Date: "
                  f"{expected_delivery_date}\n\nThank you for choosing our courier service!")

    return email_body


# Example usage
customer_name = "Vishal"
order_number = "TN123456"
delivery_address = "123 Main St, Mumbai, MH-12345"
expected_delivery_date = "2023-12-31"

order_confirmation_email = generate_order_confirmation_email(customer_name, order_number, delivery_address,
                                                             expected_delivery_date)
print("Order Confirmation Email:\n", order_confirmation_email)
