import datetime
from typing import List, Dict

class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.bookings = []  # list of (start_date, end_date)

    def is_available(self, start_date: datetime.date, end_date: datetime.date) -> bool:
        for s, e in self.bookings:
            if start_date <= e and end_date >= s:
                return False
        return True

    def book(self, start_date: datetime.date, end_date: datetime.date):
        if not self.is_available(start_date, end_date):
            raise Exception("Room not available.")
        self.bookings.append((start_date, end_date))

class Guest:
    def __init__(self, name: str, age: int, id_number: str):
        self.name = name
        self.age = age
        self.id = id_number
        self.history = []

    def book_room(self, hotel, start_date, end_date):
        room = hotel.find_available_room(start_date, end_date)
        if room:
            room.book(start_date, end_date)
            self.history.append((room.number, start_date, end_date))
        else:
            print(f"No rooms available for {self.name} from {start_date} to {end_date}")

class Hotel:
    def __init__(self, name: str, rooms: List[Room]):
        self.name = name
        self.rooms = {room.number: room}
        self.guests: Dict[str, Guest] = {}

    def add_guest(self, guest: Guest):
        self.guests[guest.id] = guest

    def find_available_room(self, start_date, end_date) -> Room:
        for room in self.rooms.values():
            if room.is_available(start_date, end_date):
                return room
        return None

    def generate_report(self, date: datetime.date):
        print(f"Report for {date} at {self.name}")
        for room in self.rooms:
            print(f"Room {room.number}:")
            for s, e in room.bookings:
                if s <= date <= e:
                    print(f"  Occupied from {s} to {e}")

# Simulation
if __name__ == "__main__":
    rooms = [Room(101, 2), Room(102, 4)]
    h = Hotel("Seaside Inn", rooms)

    guest1 = Guest("Alice", 30, "A123")
    guest2 = Guest("Bob", 45, "B456")

    h.add_guest(guest1)
    h.add_guest(guest2)

    today = datetime.datetime.now()
    next_week = today + datetime.timedelta(days=7)

    guest1.book_room(h, today, next_week)
    guest2.book_room(h, today, next_week)

    h.generate_report(today)
