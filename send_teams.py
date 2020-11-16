#! /usr/bin/env python
import pymsteams
import argparse
import socket

parser = argparse.ArgumentParser(description='beacon info')
parser.add_argument('-w', '--webhook_url')
parser.add_argument('--teamserver')
parser.add_argument('--text')

args = parser.parse_args()

myTeamsMessage = pymsteams.connectorcard(args.webhook_url)
myTeamsMessage.text(f"New Event on {args.teamserver}: \n\n{args.text}")
myTeamsMessage.send()