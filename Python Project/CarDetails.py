class Car:
    def __init__(self, color, company, cost):
        self.color = color.title()
        self.company = company.title()
        self.cost = cost
    
    def get_color(self):
        return f'Color of car is {self.color}'
    
    def get_company(self):
        return f'Company of car is {self.company}'
    
    def get_cost(self):
        return f'Cost of car is {self.cost}'

car_data = {
    "tesla_model_s": {
        "color": "black",
        "company": "Tesla",
        "cost": 70000
    },
    "ford_mustang": {
        "color": "red",
        "company": "Ford",
        "cost": 55000
    },
    "toyota_camry": {
        "color": "silver",
        "company": "Toyota",
        "cost": 35000
    }
}

def get_car_data(car_model, data):
    if car_model in data:
        car_data = data[car_model]
        print(f"Color: {car_data['color']}")
        print(f"Company: {car_data['company']}")
        print(f"Cost: {car_data['cost']}")
        print()
    else:
        print(f"Car model '{car_model}' not found in the data.")

get_car_data("ford_mustang", car_data)
get_car_data("tesla_model_s", car_data)
get_car_data("toyota_camry", car_data)

# Author : Heamnt Thapa
# Code pushed in github at 27.02.2024
