from xattr import remove


class Bus:

    def __init__(self, speed, max_seats, max_speed, passengers, are_free_seats, seats):

        self.speed = speed
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = passengers
        self.are_free_seats = are_free_seats
        self.seats = seats


    def __str__(self):
        return (f'Speed: {self.speed}\n'
                f'Max seats: {self.max_seats}\n'
                f'Max speed: {self.max_speed}\n'
                f'Passengers list {self.passengers}\n'
                f'Are there free seats: {self.are_free_seats}\n'
                f'Seats: {self.seats}')


    def embarking(self, new_passengers):
        free_seats_count = self.max_seats - len(self.passengers)
        if free_seats_count >= len(new_passengers):
            for passenger in new_passengers:
                self.passengers.append(passenger)
            counter = len(new_passengers)
            free_seats = [key for key, value in self.seats.items() if value == False]
            key_index_counter = 0
            while counter > 0:
                free_seat_key = free_seats[key_index_counter]
                self.seats[free_seat_key] = True
                key_index_counter += 1
                counter -= 1
        else:
            raise ValueError('There arent enough free seats')
        if len(self.passengers) == self.max_seats:
            self.are_free_seats = False


    def disembarking(self, passengers_list):
        not_found_passengers = []
        deleted_passengers = []
        occupied_seats = [key for key, value in self.seats.items() if value == True]
        key_index_counter = 0
        for passenger in passengers_list:
            if passenger in self.passengers:
                self.passengers.remove(passenger)
                deleted_passengers.append(passenger)
                occupied_seat_index = occupied_seats[key_index_counter]
                self.seats[occupied_seat_index] = False
                key_index_counter += 1
            else:
                not_found_passengers.append(passenger)
        if len(deleted_passengers) > 0:
            print(f'Deleted passengers: {', '.join(deleted_passengers)}')
        if len(not_found_passengers) > 0:
            print(f'Not found passengers: {', '.join(not_found_passengers)}. These passengers could not be removed')


    def speed_change(self, value, change):
        if change == 0:
            if self.speed - value >= 0:
                self.speed -= value
            else:
                self.speed = 0
        elif change == 1:
            if self.speed + value <= self.max_speed:
                self.speed += value
            else:
                self.speed = self.max_speed


    def __contains__(self, passenger_name):
        return passenger_name in self.passengers


    def __iadd__(self, other):
        free_seats_count = self.max_seats - len(self.passengers)
        if free_seats_count >= 1:
            self.passengers.append(other)
            free_seats = [key for key, value in self.seats.items() if value == False]
            free_seat_key = free_seats[0]
            self.seats[free_seat_key] = True
        else:
            raise ValueError('There arent enough free seats')
        if len(self.passengers) == self.max_seats:
            self.are_free_seats = False
        return self


    def __isub__(self, other):
        not_found_passenger = ''
        deleted_passenger = ''
        occupied_seats = [key for key, value in self.seats.items() if value == True]
        if other in self.passengers:
            self.passengers.remove(other)
            deleted_passenger = other
            occupied_seat_index = occupied_seats[0]
            self.seats[occupied_seat_index] = False
        else:
            not_found_passenger = other
        if len(deleted_passenger) > 0:
            print(f'Deleted passenger: {deleted_passenger}')
        if len(not_found_passenger) > 0:
            print(f'Not found passenger: {not_found_passenger}. These passengers could not be removed')
        return self


neoplan_speed = 100
neoplan_max_seats = 25
neoplan_max_speed = 120
neoplan_passangers = ['Ivanov', 'Petrov', 'Sidorov']
neoplan_are_free_seats = True
neoplan_seats = {
    1: True,
    2: True,
    3: True,
    4: False,
    5: False,
    6: False,
    7: False,
    8: False,
    9: False,
    10: False,
    11: False,
    12: False,
    13: False,
    14: False,
    15: False,
    16: False,
    17: False,
    18: False,
    19: False,
    20: False,
    21: False,
    22: False,
    23: False,
    24: False,
    25: False
}
neoplan = Bus(speed=neoplan_speed, max_seats=neoplan_max_seats, max_speed=neoplan_max_speed, passengers=neoplan_passangers, are_free_seats=neoplan_are_free_seats, seats=neoplan_seats)
print(neoplan)
neoplan_new_passengers = ['Smith', 'Swan']
neoplan.embarking(new_passengers=neoplan_new_passengers)
print(neoplan)

neoplan.disembarking(passengers_list=neoplan_new_passengers)
print(neoplan)

neoplan.speed_change(value=20, change=0)
print(neoplan)

neoplan.speed_change(value=60, change=1)
print(neoplan)

print('Ivanov' in neoplan)
new_passenger = 'Masharo'
neoplan += new_passenger
print(neoplan)

neoplan -= new_passenger
print(neoplan)