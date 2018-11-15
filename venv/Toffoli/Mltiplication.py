'''
Script to multiply Qbits together with pauli gates specifically 3 qubit combinations
'''

import numpy as np

def tripleKron(A,B,C):
    return np.kron(A,np.kron(B,C))

px = np.array([[0, 1], [1, 0]], dtype=np.complex128)
py = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
pz = np.array([[1, 0], [0, -1]], dtype=np.complex128)
id = np.array([[1, 0], [0, 1]], dtype=np.complex128)

q1 = np.array([0,1])
q2 = np.array([0,1])
q3 = np.array([0,1])

qBit = np.kron(q1,np.kron(q2,q3))
print(qBit)

'''
Prepare the Toffoli Decomposition
'''

T1 = tripleKron(id,id,id) * 0.75
T2 = tripleKron(id,id,pz) * 0.25
T3 = tripleKron(id,px,id) * 0.25
T4 = tripleKron(id,px,pz) * -0.25
T5 = tripleKron(pz,id,id) * 0.25
T6 = tripleKron(pz,id,pz) * -0.25
T7 = tripleKron(pz,px,id) * -0.25
T8 = tripleKron(pz,px,pz) * 0.25

out1 = np.matmul(T1,qBit)
out2 = np.matmul(T2,qBit)
out3 = np.matmul(T3,qBit)
out4 = np.matmul(T4,qBit)
out5 = np.matmul(T5,qBit)
out6 = np.matmul(T6,qBit)
out7 = np.matmul(T7,qBit)
out8 = np.matmul(T8,qBit)

out = out1 + out2 + out3 + out4 + out5 + out6 + out7 + out8

print(out1)
print(out2)
print(out3)
print(out4)
print(out5)
print(out6)
print(out7)
print(out8)



