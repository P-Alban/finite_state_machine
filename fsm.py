from datetime import timedelta, datetime


class StateObject(object):
    def __init__(self, extra_states):
        self.extra_states = extra_states

    def __getattribute__(self, item):
        states = super().__getattribute__('extra_states')
        return states if item == 'extra_states' else states[item]

    def __str__(self):
        return str(self.extra_states)


class FSM:
    def __init__(self, default):
        self.default = default
        self.states = {}
        self.extra_states = {}
        self.expired_states = {}

    def init_state(self, holder):
        """
        Sets the key to the default value
        Does the same as function set_default_state()
        :param holder: key
        :return:
        """
        self.set_default_state(holder)

    def set_state(self, holder, value):
        """
        Sets the state for the key
        :param holder: key
        :param value:
        :return:
        """
        self.states.update({holder: value})

    def remove_state(self, holder):
        """
        remove the state by holder
        :param holder: key
        :return:
        """
        del self.states[holder]

    def remove_extra_state(self, holder):
        """
        remove the extra state by holder
        :param holder: key
        :return:
        """
        del self.extra_states[holder]

    def set_default_state(self, holder):
        self.states[holder] = self.default

    def add_extra_state(self, holder, key, value):
        """
        Here you can add many values ​​for the key, they will be available like this:
        key.value
        :param holder: key
        :param key: key
        :param value:
        :return:
        """
        if not self.extra_states.get(holder):
            self.extra_states.update({holder: {key: value}})
        else:
            self.extra_states[holder].update({key: value})

    def get_state(self, holder):
        """
        return current state for holder
        :param holder: key
        :return:
        """
        return self.states.get(holder)

    def get_extra_state(self, holder, key):
        """
        return extra state for holder by name
        :param holder: key
        :param key:
        :return:
        """
        return self.extra_states[holder][key]

    def all_extra_states(self, holder):
        """
        return all extra state for holder
        :param holder: key
        :return:
        """
        return StateObject(self.extra_states[holder])

    def set_expired(self, holder, seconds):
        """
        Sets a value with a specified lifetime
        :param holder: value
        :param seconds: time in seconds
        :return:
        """
        self.expired_states[holder] = datetime.now() + timedelta(seconds=seconds)

    def remove_expired(self, holder):
        if self.expired_states.get(holder):
            del self.expired_states[holder]

    def check_expired(self, holder):
        """
        Returns the remaining lifetime of the object if it has not expired,
        otherwise False
        :param holder:
        :return: time or bool
        """
        now = datetime.now()
        saved_time = self.expired_states.get(holder)
        if not saved_time or now >= saved_time:
            self.remove_expired(holder)
            return False
        return saved_time - now
