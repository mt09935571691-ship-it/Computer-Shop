# 🖥️ Computer Shop Order System

A simple **Python-based computer shop ordering system** that allows users to browse a product menu, place an order, enter quantities, and receive a calculated receipt.

This project was created as a practical Python project to practice **dictionaries, functions, loops, user input, conditionals, and basic error handling**.

---

## ✨ Features

* 👤 Customer name input
* 🛒 Display available computer products
* 📦 Order multiple products at once
* 🔢 Enter a quantity for each product
* 💰 Automatic subtotal and total calculation
* 🧾 Generate a simple receipt
* ⚠️ Detect unavailable products
* ⚠️ Check whether the number of quantities matches the number of products
* 🔄 Store ordered products and quantities using a dictionary

---

## 🛍️ Available Products

| Product        | Price |
| -------------- | ----: |
| 🖱️ Mouse      |   $25 |
| ⌨️ Keyboard    |   $40 |
| 🎧 Headset     |   $35 |
| 🖱️ Mousepad   |   $15 |
| 📷 Webcam      |   $50 |
| 💾 Flash       |   $12 |
| 🎮 Gamepad     |   $45 |
| 🎙️ Microphone |   $60 |

---

## 🚀 How It Works

When the program starts, it asks for the customer's name:

```text
Enter you name:
Matin

Wellcome to our shop Matin
```

Then the available products are displayed:

```text
======= ORDER MENU =======

Mouse      25
Keyboard   40
Headset    35
Mousepad   15
Webcam     50
Flash      12
Gamepad    45
Microphone 60
```

The user can enter multiple products:

```text
Enter your order:
mouse keyboard headset
```

Then enter the corresponding quantities:

```text
Enter quantities:
2 1 3
```

The program calculates the price of each item and generates a receipt:

```text
====== RECEIPT ======

Mouse  x2 $25
Keyboard x1 $40
Headset x3 $35
-------------------------
Total: $175
```

---

## 🧠 Python Concepts Used

This project helped me practice several important Python concepts:

* **Dictionaries**
* **Functions**
* **`for` loops**
* **`if / else` statements**
* **`input()`**
* **String methods**

  * `.lower()`
  * `.split()`
  * `.title()`
* **Formatted strings (f-strings)**
* **Dictionary `.items()`**
* **Lists**
* **Basic validation**
* **Returning values from functions**

---

## 📂 Project Structure

```text
Computer-Shop/
│
├── Shop.py
└── README.md
```

---

## ▶️ How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Go into the project folder:

```bash
cd Computer-Shop
```

Run the program:

```bash
python Shop.py
```

---

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ] Add product categories
* [ ] Add a shopping cart
* [ ] Allow users to remove products from their order
* [ ] Add discounts
* [ ] Add tax calculation
* [ ] Improve input validation
* [ ] Save orders to a file
* [ ] Add an inventory system
* [ ] Add a graphical user interface (GUI)
* [ ] Add product IDs
* [ ] Add order history

---

## 🎯 Project Goal

The main goal of this project is to turn basic Python knowledge into a small, practical application.

It is part of my journey toward building larger Python projects and eventually moving into **Artificial Intelligence and Machine Learning with Python**.

---

## 🛠️ Built With

**Python 🐍**

---

## 📜 License

This project is created for learning and educational purposes.
