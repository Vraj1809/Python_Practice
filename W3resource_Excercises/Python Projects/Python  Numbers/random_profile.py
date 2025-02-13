import random

fname = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria','Adam','Sturt','Nikolson','Tom','Harry','Ruskin','Thor','Rocky','Ravid','David','Harris','Eion','Elon','Mark','Will','Chris']

lname = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin','Potter','Jukerberg','Smith','Nebula','Downy','Downy Jr']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

class Name:
    def __init__(self, num = 1):
        self.num = num
        
    def first_name(self):
        
        for i in range(self.num):
            firstName = random.choice(fname)
            print(firstName)
            
    def last_name(self):
        
        for i in range(self.num):
            lastName = random.choice(lname)
            print(lastName)
            
    def full_name(self):
        
        for i in range(self.num):
            firstName = random.choice(fname)
            lastName = random.choice(lname)
            print(firstName, " ", lastName)
            
    def full_description(self):
        
        for i in range(self.num):
            firstName = random.choice(fname)
            lastName = random.choice(lname)
            phone = f'+91-{random.randint(800, 999)}{random.randint(800, 999)}{random.randint(1000,9999)}'
            streetno = random.randint(100, 999)
            streetname = random.choice(street_names) + " St."
            city = random.choice(fake_cities)
            state = random.choice(states)
            pin_code = random.randint(10000, 99999)
        
            address = f'{streetno} {streetname}, {city} {state} {pin_code}'
            email = firstName.lower() + lastName.lower() + '@bogusemail.com'
            print(f'{firstName} {lastName} \n {address}- Us\n{phone}\n{email}')
            print('-'*30)
        
        print('*'*30)