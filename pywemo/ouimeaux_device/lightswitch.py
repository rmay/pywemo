"""Representation of a WeMo Motion device."""
from .switch import Switch


class LightSwitch(Switch):
    """Representation of a WeMo Motion device."""

    def __repr__(self):
        """Return a string representation of the device."""
        return '<"LightSwitch", "{name}", "{state}">'.format(name=self.name, state=self.get_friendly_state())


    @property
    def device_type(self):
        """Return what kind of WeMo this device is."""
        return "LightSwitch"
