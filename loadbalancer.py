#!/usr/bin/env python

import requests
import json
import unicodedata
from subprocess import Popen, PIPE
import time
import networkx as nx
from sys import exit

# Method To Get REST Data In JSON Format
def getResponse(url,choice):
response = requests.get(url)

	if(response.ok):
		jData = json.loads(response.content)
		if(choice=="deviceInfo"):
			deviceInformation(jData)
		elif(choice=="findSwitchLinks"):
			findSwitchLinks(jData,switch[h2])
		elif(choice=="linkTX"):
			linkTX(jData,portKey)

	else:
		response.raise_for_status()
    
# Parses JSON Data To Find Switch Connected To H4
def deviceInformation(data):
	global switch
	global deviceMAC
	global hostPorts
	switchDPID = ""
	for i in data:
		if(i['ipv4']):
			ip = i['ipv4'][0].encode('ascii','ignore')
			mac = i['mac'][0].encode('ascii','ignore')
			deviceMAC[ip] = mac
			for j in i['attachmentPoint']:
				for key in j:
					temp = key.encode('ascii','ignore')
					if(temp=="switchDPID"):
						switchDPID = j[key].encode('ascii','ignore')
						switch[ip] = switchDPID
					elif(temp=="port"):
						portNumber = j[key]
						switchShort = switchDPID.split(":")[7]
						hostPorts[ip+ "::" + switchShort] = str(portNumber)
 
 # Finding Switch Links
 def findSwitchLinks(data,s):
 def findSwitchLinks(data,s):
	global switchLinks
	global linkPorts
	global G

	links=[]
	for i in data:
		src = i['src-switch'].encode('ascii','ignore')
		dst = i['dst-switch'].encode('ascii','ignore')

		srcPort = str(i['src-port'])
		dstPort = str(i['dst-port'])

		srcTemp = src.split(":")[7]
		dstTemp = dst.split(":")[7]

		G.add_edge(int(srcTemp,16), int(dstTemp,16))

		tempSrcToDst = srcTemp + "::" + dstTemp
		tempDstToSrc = dstTemp + "::" + srcTemp

		portSrcToDst = str(srcPort) + "::" + str(dstPort)
		portDstToSrc = str(dstPort) + "::" + str(srcPort)

		linkPorts[tempSrcToDst] = portSrcToDst
		linkPorts[tempDstToSrc] = portDstToSrc

		if (src==s):
			links.append(dst)
		elif (dst==s):
			links.append(src)
		else:
			continue

	switchID = s.split(":")[7]
	switchLinks[switchID]=links
  
  # Finds a Path to A Switch
  def findSwitchRoute():
  
  # Computes Link TX
  def linxTX(data,key):
  
  # Method To Compute Link Cost
  def getLinkCost():
  
  def systemCommand(cmd):
  
  def flowRule():
  
  def addFlow():
  
# Method To Perform Load Balancing
def loadbalance():
linkURL = "http://localhost:8080/wm/topology/links/json"
	getResponse(linkURL,"findSwitchLinks")

	findSwitchRoute()
	getLinkCost()
	addFlow()

# Main
