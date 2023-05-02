.. Netbox extraction documentation master file, created by
   sphinx-quickstart on Tue May  2 11:27:11 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Netbox extraction's documentation!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Description
==================

This is a project that obtains device information from a NetBox server using GraphQL, and presents it in a REST API.

Installation
==================

To install this project, follow the steps below:

1. Clone the GitHub repository: https://github.com/jguerrero10/testGraphQL.git
2. Creates a virtual environment and installs the project dependencies:

   `python -m venv env`

   `source env/bin/activate`

   `pip install -r requirements.txt`

Use
==================

To run the application, make sure you are in the root directory of the project and run the following command:

`uvicorn main:app --reload`

This will start the application in `http://localhost:8000`.


Endpoints
==================

The application has the following endpoints:

- `/netbox`: returns a list of devices obtained from the NetBox server.
- `/payload`: creates a text file with the author's name and the current date.

Models
==================

The application uses the following models:

- `DeviceInfo`: a model representing a device with the following fields:
    - `id`: the device ID.
    - `name`: the name of the device.
    - `manufacturer`: the name of the manufacturer of the device.
    - `ipv4`: the IPv4 address of the device.
