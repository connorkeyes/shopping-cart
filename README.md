# shopping-cart

This is a project created for the fictional "Paddy's Pub". This program scans products from a Google Sheet, prints a receipt, and saves it onto your local directory as well as emailing it to you.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/connorkeyes/shopping-cart) under your own control, then clone your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd shopping-cart
```

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

```sh
conda create -n shopping-env python=3.8
conda activate shopping-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
pip install sendgrid
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify the sales tax rate of your location:

    TAX_RATE = 0.10

## Usage

Run the shopping cart script:

```py
python shopping_cart.py
```

Receipts will save in the "receipts" folder of your root directory.