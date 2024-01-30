#!/usr/bin/python3
"""This Class Define Locked Object."""


class LockedClass:
    """
    This Class Restricts The Istantiation Of New Attributes In LockedClass,
    Allowing Only 'first_name' Attributes To Be Created.
    """

    __slots__ = ["first_name"]
