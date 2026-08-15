import numpy as np
sales = np.array([
    [120, 150, 100, 180],
    [200, 175, 220, 190],
    [90,  120, 110, 100],
    [250, 230, 210, 280],
    [160, 140, 180, 170],
    [80,  95,  70,  85],
    [210, 190, 200, 220]
])
products = ["Laptop", "Phone", "Tablet", "Monitor"]


#🟢 Level 1 — sales Analysis
'''Total sales for each employee
Average sales for each employee
Highest sale made by each employee
Lowest sale made by each employee'''

print(sales.sum(axis=1))
#output: [550 785 420 970 650 330 820]

print(sales.mean(axis=1))
#output: [137.5  196.25 105.   242.5  162.5   82.5  205.  ]

print(sales.max(axis=1))
#output: [180 220 120 280 180  95 220]

print(sales.min(axis=1))
#output: [100 175  90 210 140  70 190]


#1🟡 Level 2 — Product Analysis
'''Total sales for each product
Average sales for each product
Highest sale for each product
Lowest sale for each product'''

print(sales.sum(axis=0))
#output: [1110 1100 1090 1225]

print(sales.mean(axis=0))
#output: [158.57142857 157.14285714 155.71428571 175.]

print(sales.max(axis=0))
#output: [250 230 220 280]

print(sales.min(axis=0))
#output: [80 95 70 85]


#🟠 Level 3 — Find Top Performers
'''Employees whose average sales are above 180
Employees whose average sales are below 120
Count employees whose average is above 180
Find the employee with the highest average'''

avg= sales.mean(axis= 1)
print(sales[avg > 180])
#output:  [210 190 200 220]]

avg= sales.mean(axis= 1)
print(sales[avg<120])
#output:  [ 80  95  70  85]]

avg= sales.mean(axis= 1)
print(np.count_nonzero(avg>180))
#output: 3

avg= sales.mean(axis= 1)
index= np.argmax(avg)
print(sales[index])
#output: [250 230 210 280]


#🔵 Level 4 — Product Filtering
'''Find all employees who sold more than 200 Laptops.'''

sold_more= sales[:,0]
print(sales[sold_more>200])
#output:  [210 190 200 220]]

#🔥 Level 5 — Broadcasting
'''Total commission earned by each employee
Total commission earned from each product
Employee with the highest total commission'''

commission = np.array([0.10, 0.08, 0.12, 0.07])
commission_amount = sales * commission
print(commission_amount.sum(axis=1))
#output: [48.6  73.7  38.8  88.2  60.7  29.95 75.6 ]

commission = np.array([0.10, 0.08, 0.12, 0.07])
commission_amount = sales * commission
print(commission_amount.sum(axis=0))
#output: [111.    88.   130.8   85.75]

commission = np.array([0.10, 0.08, 0.12, 0.07])
commission_amount = sales * commission
print(commission_amount.max(axis=1))
#output: [12.6 26.4 13.2 25.2 21.6  8.4 24. ]

