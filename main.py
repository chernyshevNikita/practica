import numpy as np
import matplotlib.pyplot as plt
# системы скольжения
k = 24
Bvector = np.array([[1 / (2 ** 0.5), 0, -1 / (2 ** 0.5)],[0, 1 / (2 ** 0.5), -1 / (2 ** 0.5)],[1 / (2 ** 0.5), -1 / (2 ** 0.5), 0],[1 / (2 ** 0.5), 1 / (2 ** 0.5), 0],[1 / (2 ** 0.5), 0, 1 / (2 ** 0.5)],[0, 1 / (2 ** 0.5), -1 / (2 ** 0.5)],[1 / (2 ** 0.5), 1 / (2 ** 0.5), 0],[0, 1 / (2 ** 0.5), 1 / (2 ** 0.5)],[0, 1 / (2 ** 0.5), -1 / (2 ** 0.5)],[1 / (2 ** 0.5), 0, 1 / (2 ** 0.5)],[1 / (2 ** 0.5), -1 / (2 ** 0.5), 0],[0, 1 / (2 ** 0.5), 1 / (2 ** 0.5)],[-1 / (2 ** 0.5), 0, 1 / (2 ** 0.5)],[0, -1 / (2 ** 0.5), 1 / (2 ** 0.5)],[-1 / (2 ** 0.5), 1 / (2 ** 0.5), 0],[-1 / (2 ** 0.5), -1 / (2 ** 0.5), 0],[-1 / (2 ** 0.5), 0, -1 / (2 ** 0.5)],[0, -1 / (2 ** 0.5), 1 / (2 ** 0.5)],[-1 / (2 ** 0.5), -1 / (2 ** 0.5), 0],[0, -1 / (2 ** 0.5), -1 / (2 ** 0.5)],[-1 / (2 ** 0.5), 0, 1 / (2 ** 0.5)],[-1 / (2 ** 0.5), 0, -1 / (2 ** 0.5)],[-1 / (2 ** 0.5), 1 / (2 ** 0.5), 0],[0, -1 / (2 ** 0.5), -1 / (2 ** 0.5)]])
Nvector = np.array([[1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[-1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[-1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[-1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), -1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), -1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), -1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), -1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), -1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), -1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[-1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[-1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[-1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), -1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), -1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), -1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), -1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), -1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), -1 / (3 ** 0.5)]])



Epsi = np.zeros((3,3))
SigmaP = np.zeros((3, 3))
Sigm = np.zeros((3,3))

# Nach
GradSkorosti = np.zeros(k)
T = np.zeros(k + 1)

Tkrit = 17.5*10**6
YskorostSdviga0 = 0.001
deltT = 1
m = 86
E11 = 0.001
E21 = -0.0005
E = np.array([[E11, 0, 0], [0, E21, 0], [0, 0, E21]])
def S(D):
    return
P = np.zeros((3, 3, 3, 3))
P[0, 0, 0, 0] = P[1, 1, 1, 1] = P[2, 2, 2, 2] = 168.4*10**9
P[0, 0, 1, 1] = P[1, 1, 0, 0] = P[2, 2, 0, 0] = P[0, 0, 2, 2] = P[1, 1, 2, 2] = P[2, 2, 1, 1] = 121.4*10**9
P[0, 1, 0, 1] = P[1, 0, 0, 1] = P[1, 0, 1, 0] = P[0, 1, 1, 0] = P[0, 2, 0, 2] = P[2, 0, 0, 2] = P[2, 0, 2, 0] = P[0, 2, 2, 0] = P[2, 1, 2, 1] = P[2, 1, 1, 2] = P[1, 2, 1, 2] = P[1, 2, 2, 1] = 75.4*10**9
EP = 0
deltE = E
IntSigm = [0]
IntE = [0]
i = 0
while IntE[i] <= 0.01:
    SigmaP = np.tensordot(P, deltE, axes=2)
    Sigm = Sigm + SigmaP*0.01
    IntSigm.append(((2 / 3) * (np.tensordot(Sigm, Sigm, axes=2))) ** (1 / 2))
    EP = 0
    for p in range(1, k):
        T[p] = np.tensordot(np.tensordot(Bvector[p],Nvector[p],axes=0),Sigm)
        #print(T[p])
        if Tkrit >= T[p]:
            GradSkorosti = 0
        if Tkrit < T[p]:
            GradSkorosti = YskorostSdviga0 * ((T[p] / Tkrit) ** (1/m))
        EP += GradSkorosti*np.tensordot(Bvector[p],Nvector[p],axes=0)
    deltE = E-EP
    Epsi = Epsi + E * 0.01
    IntE.append(((2 / 3) * (np.tensordot(Epsi, Epsi, axes=2))) ** (1 / 2))
    i+=1
print(Sigm)
with open("IntSigm.txt", "a") as file:
    file.write(f"\n {IntSigm} ")
with open("IntE.txt", "a") as file:
    file.write(f"\n {IntE} ")


fig, ax = plt.subplots()
ax.set_title('График')
ax.plot(IntE,IntSigm )
plt.show()