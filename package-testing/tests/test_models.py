from unittest.mock import Mock

import tests

tests.__file__

import pytest

from package.models import Alarm, Phone, PhoneBook, Sensor


class TestModelPhone:
    @pytest.fixture
    def phonebook(self):
        return PhoneBook("tepdir")

    @pytest.mark.xfail(reason="unknown for the time")
    def test_phone_book_is_not_empty(self, phonebook):
        phonebook.add(Phone(name="vicktor", phone="1222"))
        phonebook.add(Phone(name="espoir", phone="1333"))
        expected = Phone(name="vicktor", phone="1222")

        assert phonebook.lookup("vicktor").name == expected.name
        assert phonebook.lookup("vicktor").phone == expected.phone
        return None


class TestAlarmSensor:
    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        expected = False
        assert alarm.alarm_on == expected

    def test_alarm_high_value_reached_return_on(self):
        stub = Mock(Sensor)
        stub.sample_value.return_value = 22
        alarm = Alarm(stub)
        alarm.check_alarm()
        assert alarm.alarm_on == True

    def test_alarm_low_value_reached_return_on(self):
        stub = Mock(Sensor)
        stub.sample_value.return_value = 2
        alarm = Alarm(stub)
        alarm.check_alarm()
        assert alarm.alarm_on == True
