# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons
import os
import sys
sys.path.append('core')
from PMC import *
from speciation import *
from clear import *

folderout = os.path.join('..', 'archives', 'out', '')
clear(folderout)

print 'Start Canteras'

#Canteras
archivespeciation = os.path.join ('..', 'archives', 'in', 'PE', 'CANT_SCP_PROF_PM25.xlsx')
folderCant = os.path.join('..','archives', 'in', 'Emitions', 'CANT', '')
speciation(archivespeciation, folderCant)

folderout = os.path.join('..','archives', 'out',  'CANT', '')
brinding (folderout)

print 'Start BLD'

#BLD
archivespeciation = os.path.join ('..', 'archives', 'in', 'PE', 'BLD_CONVP_SCP_PROF_PM25.xlsx')
folderBLD = os.path.join('..','archives', 'in', 'Emitions', 'BLD', '')
speciation(archivespeciation, folderBLD)

folderout = os.path.join('..','archives', 'out', 'BLD', '')
brinding (folderout)

folderPMC = os.path.join('..','archives', 'in', 'PMC', 'BLD', '')
pmc(folderPMC)
testingpmc(folderout)

print 'Start CONVP'

#CONVP
archivespeciation = os.path.join ('..', 'archives', 'in', 'PE', 'BLD_CONVP_SCP_PROF_PM25.xlsx')
folderCONVP = os.path.join('..','archives', 'in', 'Emitions', 'CONVP', '')
speciation(archivespeciation, folderCONVP)

folderout = os.path.join('..','archives', 'out', 'CONVP', '')
brinding (folderout)

folderPMC = os.path.join('..','archives', 'in', 'PMC', 'CONVP', '')
pmc(folderPMC)
testingpmc(folderout)



