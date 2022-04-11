import csv
import copy
import requests
import os
import json
import statsapi
import pandas as pd
from flask import Flask

people_2017 = statsapi.get('sports_players',{'season':2017})['people']
people_2018 = statsapi.get('sports_players',{'season':2018})['people']
people_2019 = statsapi.get('sports_players',{'season':2019})['people']
people_2020 = statsapi.get('sports_players',{'season':2020})['people']
people_2021 = statsapi.get('sports_players',{'season':2021})['people']


roster_2017 = []
roster_2018 = []
roster_2019 = []
roster_2020 = []
roster_2021 = []


for x in people_2017:
    roster_2017.append((x.get('fullName'),'2017 ' + x.get('currentTeam')['name']))
for x in people_2018:
    roster_2018.append((x.get('fullName'),'2018 ' + x.get('currentTeam')['name']))
for x in people_2019:
    roster_2019.append((x.get('fullName'),'2019 ' + x.get('currentTeam')['name']))
for x in people_2020:
    roster_2020.append((x.get('fullName'),'2020 ' + x.get('currentTeam')['name']))
for x in people_2021:
    roster_2021.append((x.get('fullName'),'2021 ' + x.get('currentTeam')['name']))

full_roster = roster_2017 + roster_2018 + roster_2019 + roster_2020 + roster_2021


class Node:
	def __init__(self, key):
		self.key = key
		self.connectedTo = []
		self.searched = False
		self.parent = None

	def addNeighbor(self, other):
		self.connectedTo.append(other)
		other.connectedTo.append(self)

	def __str__(self):
		return str(self.key) + " connectedTo: " + str([x.key for x in self.connectedTo])
class PlayerGraph:
	def __init__(self):
		self.allNodes = {}
		self.nodeCount = 0

	def addNode(self, key):
		self.nodeCount+=1
		newNode = Node(key)
		self.allNodes[key] = newNode
		return newNode

	def addEdge(self, f, t):
		if f not in self.allNodes:
			self.addNode(f)
		if t not in self.allNodes:
			self.addNode(t)
		self.allNodes[f].addNeighbor(self.allNodes[t])

	def getNode(self, item):
		try:
			return self.allNodes[item]
		except KeyError:
			return None

	def __iter__(self):
		return iter(self.allNodes.values())
class Queue(object):
	def __init__(self):
		self.items = []

	def __str__(self):
		return str(self.items)

	def show(self):
		return self.items

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.insert(0,item)

	def pop(self):
		return self.items.pop()

	def length(self):
		return len(self.items)


	def getNode(self, item):
		try:
			return self.allNodes[item]
		except KeyError:
			return None

	def __iter__(self):
		return iter(self.allNodes.values())


filesNames = full_roster
g = PlayerGraph()

for fileName in filesNames:
    playerCount = len(fileName)-1
    for i in range(playerCount):
        g.addEdge(fileName[i+1].strip().upper(), fileName[0].strip().capitalize())

def search(playerA, playerB):
    startNode = g.getNode(playerA)
    if not startNode:
        print(f"{playerA} not in graph")
        return
    endNode = g.getNode(playerB)
    if not endNode:
        print(f"{playerB} not in graph")
        return
    Q = Queue()
    startNode.searched = True
    Q.push(startNode)

    while not Q.isEmpty():
        current = Q.pop()
        if current.key == endNode.key:
            break
        for neighbor in current.connectedTo:
            if not neighbor.searched:
                neighbor.searched = True
                neighbor.parent = current
                Q.push(neighbor)
    current = endNode
    aNumber = 0
    while current.parent is not None:
        if current.key.isupper():
            print(f" played on the {current.key} with")
            aNumber += 1
        else:
            print(f"{current.key}")
        current = current.parent
    print(startNode.key)
    print("\n")
    print("{}-number of {} is {}".format(playerA, playerB, aNumber))

#playerA = input("Enter Player A: ").strip().capitalize()
#playerB = input("Enter Player B: ").strip().capitalize()
#print("\n")
#search(playerA, playerB)

if __name__ == "__main__":
	user_input = None
	while True:
		if not user_input:
			user_input = input('Input any key, or "exit" to quit: ')
		if user_input == "exit":
			print("Bye!")
			break
		else:
			playerA = input("Enter Player A: ").strip().capitalize()
			playerB = input("Enter Player B: ").strip().capitalize()
			search(playerA, playerB)
			g = PlayerGraph()

			for fileName in filesNames:
				playerCount = len(fileName)-1
				for i in range(playerCount):
					g.addEdge(fileName[i+1].strip().upper(), fileName[0].strip().capitalize())
			user_input = None

#