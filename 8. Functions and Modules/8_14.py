def make_car(manufacturer, model_name, **make_car):
    make_car['Manufacturer'] = manufacturer 
    make_car['Model Name'] = model_name
    return make_car

car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)
car2 = make_car('dodge', 'carger', color='red', tow_package=False)
print(car2)
car3 = make_car('honda', 'accord', color='gray', tow_package=True)
print(car3)