# Problem 11 — read lines as if they came from a microcontroller
# Write a single file, e.g. 011_serial.py. Graded functions use only the
# stdlib. The optional lab at the bottom uses the pyserial package.
#
# Serial here means a stream of text over a cable (usually USB). The
# microcontroller prints one line at a time. Your laptop reads each line
# and turns it into numbers. You do not need a board for the graded
# functions.
#
#
# What you will need
#
# Packages for the graded functions: none.
# Package for the optional lab: pyserial (the import name is serial).
#
# Ideas to have in place before you start:
# - readline() returns the next line of text, or an empty string when there
#   is nothing left.
# - A line may end with a newline character. Strip that before you parse.
# - Bad or empty input should not crash the parser; return None and skip.
#
# Tools to look up if you do not know them yet:
# - str.strip and str.split
# - float(...) to turn a piece of text into a number; it raises ValueError
#   if the text is not a number
# - try / except, if you want to catch a bad number (also used in 007)
# - a loop that calls readline until the result is ""
#
# You do not need: NumPy, classes, or a real serial port for the asserts.
# Do not open /dev/tty or COM ports in the graded functions.
#
# Line format (exactly three fields, separated by commas):
#   name,value,unit
# Spaces around fields are allowed and must be stripped.
# value must be a number (int or float as text).
#
# 1. parse_serial_line(line)
#    If the line is a valid reading, return a dict with keys
#    "name" (str), "value" (float), "unit" (str).
#    Return None if the line is empty, is only whitespace, does not have
#    exactly three comma-separated fields, or the middle field is not a
#    number.
#
# 2. parse_serial_stream(text)
#    text is a whole block that may contain many lines (newline-separated).
#    Parse each line. Return a list of the dicts that parsed successfully,
#    in order. Skip lines that parse as None.
#
# 3. readings_from_readline(source)
#    source is any object with a readline method (a file, or a fake port).
#    Call readline until it returns "" (empty string).
#    Parse each line with parse_serial_line. Return the successful dicts
#    in order. If readline returns a bytes object, decode it as UTF-8
#    before parsing (real serial libraries often give bytes).
#
#
# Examples
#
# parse_serial_line("temp,21.5,C")     ->  {"name": "temp", "value": 21.5, "unit": "C"}
# parse_serial_line(" dist , 0.4 , m ") ->  {"name": "dist", "value": 0.4, "unit": "m"}
# parse_serial_line("")                ->  None
# parse_serial_line("temp,xx,C")       ->  None
# parse_serial_line("only-one-field")  ->  None
#
# parse_serial_stream("temp,21.5,C\nbad\ndist,0.4,m\n") ->
#   [{"name": "temp", "value": 21.5, "unit": "C"},
#    {"name": "dist", "value": 0.4, "unit": "m"}]
#
#
# How you know you are done
#
# Put this at the bottom of the same file and run
#   python 011_serial.py
# All of it should print ok and not raise.
# Then, if you have a board, fill in the optional lab comments.
#

# ----- EXERCISE -----
# Write your code below.
#


# ----- ASSERTION ------
#

assert parse_serial_line("temp,21.5,C") == {"name": "temp", "value": 21.5, "unit": "C"}
assert parse_serial_line(" dist , 0.4 , m ") == {"name": "dist", "value": 0.4, "unit": "m"}
assert parse_serial_line("battery,12,V") == {"name": "battery", "value": 12.0, "unit": "V"}
assert parse_serial_line("") is None
assert parse_serial_line("   ") is None
assert parse_serial_line("temp,xx,C") is None
assert parse_serial_line("only-one-field") is None
assert parse_serial_line("a,1,b,c") is None
assert parse_serial_line("temp,21.5") is None

stream = parse_serial_stream("temp,21.5,C\nbad\ndist,0.4,m\n\n")
assert stream == [
    {"name": "temp", "value": 21.5, "unit": "C"},
    {"name": "dist", "value": 0.4, "unit": "m"},
]
assert parse_serial_stream("") == []
assert parse_serial_stream("nope\nstill-nope") == []


class FakePort:
    def __init__(self, chunks):
        self._chunks = list(chunks)
        self._i = 0

    def readline(self):
        if self._i >= len(self._chunks):
            return ""
        chunk = self._chunks[self._i]
        self._i += 1
        return chunk


port = FakePort(["temp,21.5,C\n", "skip-me\n", "dist,0.4,m\n"])
assert readings_from_readline(port) == [
    {"name": "temp", "value": 21.5, "unit": "C"},
    {"name": "dist", "value": 0.4, "unit": "m"},
]

port_bytes = FakePort([b"imu,0.2,rad\n", b""])
assert readings_from_readline(port_bytes) == [
    {"name": "imu", "value": 0.2, "unit": "rad"},
]

empty_port = FakePort([])
assert readings_from_readline(empty_port) == []

print("ok")

# ----- OPTIONAL LAB (not graded by the asserts) -----
#
# 1. In a virtual environment, install pyserial.
#    YOUR_COMMAND_HERE:
#
# 2. On your microcontroller, upload a sketch that prints one line per
#    reading in the format name,value,unit (for example temp,21.5,C) and
#    ends each line with a newline.
#
# 3. Find the port name your operating system gave the board
#    (something like /dev/ttyACM0 or COM3). Record it:
#    PORT:
#
# 4. Write a short script that opens that port, reads 10 successful
#    readings with readings_from_readline or a loop of parse_serial_line,
#    and prints them. You will need to look up serial.Serial in the
#    pyserial docs (port, baudrate). Baudrate is the agreed speed in
#    symbols per second; 115200 is a common choice.
#    Paste the script below only if you want a record. Do not commit
#    port names that are machine-specific if they will confuse someone else.
#
#    YOUR_SCRIPT_HERE:
#
# 5. Unplug the board and run the script again. What error do you get?
#    OBSERVATION:
#
