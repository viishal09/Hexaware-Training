from ServiceProvider import ServiceProvider
from Customer import Customer
class mainModule:
    def print_main_menu(self):
        print("===== TechShop Main Menu =====")
        print("1. Manage Customers")
        print("2. Manage Products")
        print("3. Manage Orders")
        print("4. Exit")

    def manage_customers_menu(self):
        print("===== Manage Customers Menu =====")
        print("1. Add New Customer")
        print("2. View Customer Details")
        print("3. Update Customer Information")
        print("4. Calculate Total Orders")
        print("5. Back to Main Menu")

    def manage_products_menu(self):
        print("===== Manage Products Menu =====")
        print("1. Add New Product")
        print("2. View Product Details")
        print("3. Update Product Information")
        print("4. Back to Main Menu")

    def manage_orders_menu(self):
        print("===== Manage Orders Menu =====")
        print("1. Place New Order")
        print("2. View Order Details")
        print("3. Update Order Status")
        print("4. Back to Main Menu")

    def main_menu(self):
        sp = ServiceProvider()
        mm = mainModule()
        while True:
            mm.print_main_menu()
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                mm.manage_customers_menu()
                ch = input("Enter your choice (1-4): ")
                if ch == "1":
                    sp.New_Customer()
                elif ch == "2":
                    cust_id = list(input("enter customer ID"))
                    sp.Customer_Details(cust_id)
                elif ch == "3":
                    sp.UpdateCustomerInfo()
                elif ch == "4":
                    cust_id = int(input("enter customer ID"))
                    print(sp.Get_Total_Orders(cust_id))
                elif ch == "5":
                    mm.print_main_menu()

                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

            elif choice == "2":
                mm.manage_products_menu()
                ch = input("Enter your choice (1-4): ")
                if ch == "1":
                    sp.New_Product()
                elif ch == "2":
                    product_id = int(input("enter product ID"))
                    print(sp.View_Product_Details(product_id))
                elif ch == "3":
                    sp.UpdateProductInfo()
                elif ch == "4":
                    mm.print_main_menu()
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

            elif choice == "3":
                mm.manage_orders_menu()
                ch = input("Enter your choice (1-4): ")
                if ch == "1":
                    sp.place_new_order()
                elif ch == "2":
                    order_id = int(input("enter order ID"))
                    sp.view_order_details(order_id)
                elif ch == "3":
                    order_id = int(input("enter order ID"))
                    status = input("enter new status")
                    sp.update_order_status(order_id,status)
                elif ch == "4":
                    mm.print_main_menu()

                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

            elif choice == "4":
                print("Exiting TechShop. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    mainModule().main_menu()
