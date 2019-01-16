# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

from IPython.display import HTML

import webbrowser

def lab():
    return HTML('''<img src="images/lab.jpg" width="1000 px">''')

def ibmqx():
    # generate an URL
    return webbrowser.open("https://quantumexperience.ng.bluemix.net/qx/editor", new=0)

def ibmq_qcc():
    return HTML('''<img src="images/ibmq_qcc.jpg" width="1000 px">''')

def devices():
    # generate an URL
    return webbrowser.open("https://quantumexperience.ng.bluemix.net/qx/devices", new=0)

def qiskit():
    return webbrowser.open("https://qiskit.org", new=0)

def git():
    return webbrowser.open("https://github.com/qiskit", new=0)

def elements():
    return HTML('''<img src="images/elements.jpg" width="1000 px">''')

def quantum():
    return HTML('<img src="https://66.media.tumblr.com/763756ea907e30b639da239618bbe2d3/tumblr_mlotjw0e2C1r4xjo2o1_500.gif" width="500 px" align="center">')


def model():
    return HTML('<img src="images/model.jpg" width="1000 px" align="center">')

def community():
    return HTML('<img src="images/community.jpg" width="1000 px" align="center">')

def entanglement():
    return HTML('<img src="images/entanglement.jpg" width="1000 px" align="center">')

def aqua():
    return HTML('<img src="images/aqua.jpg" width="1000 px" align="center">')

def papers():
    return HTML('<img src="images/papers.jpg" width="1000 px" align="center">')

def execution():
    return HTML('''
    <img src="images/executions-QX-complete.gif" width="1000 px" align="center">
    ''')

def thanks():
    return HTML('<img src="images/thanks.gif" width="1000 px" align="center">')

def system():
    return HTML('<img src="images/system.jpg" width="1000 px" align="center">')

def transmon():
    return HTML('<img src="images/transmon.jpg" width="1000 px" align="center">')

def kias():
    return HTML('<img src="images/kias_qiskit.jpg" width="1000 px" align="center">')

def ntu():
    return HTML('<img src="images/ntu_qiskit.jpg" width="1000 px" align="center">')

def superposition():
    return HTML('<img src="images/superposition.gif" align="center">')

def entangled():
    return HTML('<img src="images/entenglemant.gif" align="center">')

def interference():
    return HTML('<img src="images/interference.gif" align="center">')

def algorithm():
    return HTML('<img src="images/algorithm.jpg" align="center">')

def bit_vs_qubit():
    return HTML('<img src="images/bit_vs_qubit.jpg" align="center">')

def qrac():
    return HTML('<img src="images/qrac.png" align="center">')

def other_qracs():
    return HTML('<img src="images/other_qracs.png" align="center">')

print("Hello Taiwan, Hello NTU, Hello IBM QuaNTUm ... ")
