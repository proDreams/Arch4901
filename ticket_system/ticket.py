import datetime
import decimal


class Ticket:
    _id: int
    _departure_zone: int
    _arrival_zone: int
    _route_number: int
    _departure_time: datetime
    _arrival_time: datetime
    _buyer_id: int
    _is_used: bool
    _price: decimal
    _place: str


class User:
    _id: int
    _name: str
    _tickets: [Ticket]
    _login: str
    _password_hash_code: int
    _account_id: int


class Account:
    _user_account_id: int
    _balance: decimal
