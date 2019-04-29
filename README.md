# ProPublica

## Description

This project for INST 326 uses the [ProPublica Congress API] to get House of
Representatives members for a given state, and then retrieves the bills that
they have introduced. The *propublica* module contains classes for interacting
with the ProPublica API and for modeling states, representatives, and bills.

The supplied program *md.py* uses the *propublica* module to fetch all the
representatives for the state of Maryland, and prints out the bills that they
have introduced. The idea is that it could be used to get a sense of what
activities your representative is up to. It also highlights which members have
not been active at all.

## Install

You will need Python3 to use this project. It depends on the *requests* and
*pytest* modules which can be installed with:

    pip3 install -r requirements.txt

You will also need to get a ProPublica API [key] and store it in a file in this
directory called *key.txt*.

## Run

A sample program `md.py` will use the propublica module to go through all the
House members from Maryland and print out the bills that they have introduced.
You can run it like this:

    python md.py

## Test

You can run some unit tests for the propublica module using [pytest]:

    pytest test.py

[ProPublica Congress API]: https://www.propublica.org/datastore/api/propublica-congress-api
[key]: https://www.propublica.org/datastore/api/propublica-congress-api
