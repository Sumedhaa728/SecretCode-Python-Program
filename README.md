# SecretCode-Python-Program
# Python Message Encoder & Decoder

## 📌 About the Project

This is a simple Python-based Message Encoder and Decoder that converts a given message into an encoded format and can decode it back to its original form.

The project uses basic Python concepts such as functions, loops, conditional statements, string manipulation, and the `random` module.

## ⚙️ How It Works

The program supports two operations:

### 1. Encoding

Each word in the message is encoded based on its length:

- **Words with fewer than 3 characters:** The word is simply reversed.
- **Words with 3 or more characters:**
  1. Move the first character of the word to the end.
  2. Add three randomly selected characters at the beginning.
  3. Add another three randomly selected characters at the end.

### 2. Decoding

The decoding process reverses the encoding operations:

- **Words with fewer than 3 characters:** Reverse the word to get the original word.
- **Words with 3 or more characters:**
  1. Remove the first three and last three characters.
  2. Move the last character of the remaining word to the beginning.

## 💻 Technologies Used

- Python 
- `random` module

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/KBC-Python-MiniQuiz.git
   ```

2. Navigate to the project directory:

   ```bash
   cd KBC-Python-MiniQuiz
   ```

3. Run the Python program:

   ```bash
   python message_encoder_decoder.py
   ```

## 📚 Concepts Practiced

- Python Functions
- Function Arguments and Return Values
- For Loops
- Conditional Statements (`if-elif-else`)
- String Manipulation and Slicing
- String Concatenation
- Lists
- `random.choice()`
- `split()` and `join()` methods

## 🎯 Purpose

This project was developed to practice fundamental Python programming concepts by implementing a simple message encoding and decoding mechanism.

---

**Note:** This is a basic learning project and is not intended for secure encryption or protecting sensitive information.
