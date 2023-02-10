import argparse

from modem import GsmModem

parser = argparse.ArgumentParser()
parser.add_argument("command", help="Send AT command",
                    type=str)
args = parser.parse_args()

at_command = GsmModem(args.command)

# print(at_command)
