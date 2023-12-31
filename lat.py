import numpy as np
import matplotlib.pyplot as plt
k = 24
Bvector = np.array([[1 / (2 ** 0.5), 0, -1 / (2 ** 0.5)],[0, 1 / (2 ** 0.5), -1 / (2 ** 0.5)],[1 / (2 ** 0.5), -1 / (2 ** 0.5), 0],[1 / (2 ** 0.5), 1 / (2 ** 0.5), 0],[1 / (2 ** 0.5), 0, 1 / (2 ** 0.5)],[0, 1 / (2 ** 0.5), -1 / (2 ** 0.5)],[1 / (2 ** 0.5), 1 / (2 ** 0.5), 0],[0, 1 / (2 ** 0.5), 1 / (2 ** 0.5)],[0, 1 / (2 ** 0.5), -1 / (2 ** 0.5)],[1 / (2 ** 0.5), 0, 1 / (2 ** 0.5)],[1 / (2 ** 0.5), -1 / (2 ** 0.5), 0],[0, 1 / (2 ** 0.5), 1 / (2 ** 0.5)],[-1 / (2 ** 0.5), 0, 1 / (2 ** 0.5)],[0, -1 / (2 ** 0.5), 1 / (2 ** 0.5)],[-1 / (2 ** 0.5), 1 / (2 ** 0.5), 0],[-1 / (2 ** 0.5), -1 / (2 ** 0.5), 0],[-1 / (2 ** 0.5), 0, -1 / (2 ** 0.5)],[0, -1 / (2 ** 0.5), 1 / (2 ** 0.5)],[-1 / (2 ** 0.5), -1 / (2 ** 0.5), 0],[0, -1 / (2 ** 0.5), -1 / (2 ** 0.5)],[-1 / (2 ** 0.5), 0, 1 / (2 ** 0.5)],[-1 / (2 ** 0.5), 0, -1 / (2 ** 0.5)],[-1 / (2 ** 0.5), 1 / (2 ** 0.5), 0],[0, -1 / (2 ** 0.5), -1 / (2 ** 0.5)]])
Nvector = np.array([[1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[-1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[-1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[-1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), -1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), -1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), -1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), -1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), -1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), -1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[-1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[-1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[-1 / (3 ** 0.5), 1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), -1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), -1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), -1 / (3 ** 0.5), 1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), -1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), -1 / (3 ** 0.5)],[1 / (3 ** 0.5), 1 / (3 ** 0.5), -1 / (3 ** 0.5)]])
tc = np.zeros(k)
for r in range(0,k):
    tc[r] = 16*10**6
pogr = 0.0001
h0 = 180*10**6
a = 2.25
tsat = 148*10**6
def h(l,h0,tc,tsat,a):
    return h0*abs(1-tc[l]/tsat)**a


def delta(k,l):
    if k==l:
        return 1
    else:
        return 0

def qlat(k,l):
    if np.tensordot(Bvector[k],Bvector[l],axes=1) >= 1 - pogr:
        return 1.0
    else:
        return 1.4


Epsi = np.zeros((3,3))
SigmaP = np.zeros((3, 3))
Sigm = np.zeros((3,3))

# Nach
GradSkorosti = np.zeros(k)
T = np.zeros(k + 1)
Tkr = np.zeros(k)
Tkrit = np.zeros(k)
for g in range(0,k):
    Tkrit[g] = 17.5 * 10 ** 6
YskorostSdviga0 = 0.001
deltT = 1
m = 86
E11 = 0.001
E21 = -0.0005
E = np.array([[E11, 0, 0], [0, E21, 0], [0, 0, E21]])

P = np.zeros((3, 3, 3, 3))
P[0, 0, 0, 0] = P[1, 1, 1, 1] = P[2, 2, 2, 2] = 168.4*10**9
P[0, 0, 1, 1] = P[1, 1, 0, 0] = P[2, 2, 0, 0] = P[0, 0, 2, 2] = P[1, 1, 2, 2] = P[2, 2, 1, 1] = 121.4*10**9
P[0, 1, 0, 1] = P[1, 0, 0, 1] = P[1, 0, 1, 0] = P[0, 1, 1, 0] = P[0, 2, 0, 2] = P[2, 0, 0, 2] = P[2, 0, 2, 0] = P[0, 2, 2, 0] = P[2, 1, 2, 1] = P[2, 1, 1, 2] = P[1, 2, 1, 2] = P[1, 2, 2, 1] = 75.4*10**9
EP = 0
deltE = E
IntSigm = [0]
IntE = [0]
i = 0
while IntE[i] <= 0.02:
    SigmaP = np.tensordot(P, deltE, axes=2)
    Sigm = Sigm + SigmaP*0.001
    IntSigm.append(((2 / 3) * (np.tensordot(Sigm, Sigm, axes=2))) ** (1 / 2))
    EP = 0
    for p in range(1, k):
        T[p] = np.tensordot(np.tensordot(Bvector[p],Nvector[p],axes=0),Sigm)
        if Tkrit[p] >= T[p]:
            GradSkorosti[p] = 0
        if Tkrit[p] < T[p]:
            GradSkorosti[p] = YskorostSdviga0 * ((T[p] / Tkrit[p]) ** (1/m))
        EP += GradSkorosti[p]*np.tensordot(Bvector[p],Nvector[p],axes=0)
    for p in range(0,k):
        for l in range(0,k):
            hkl = h0 * abs(1 - tc[l] / tsat) ** a * (qlat(p, l) + (1 - qlat(p, l)) * delta(p, l))
            Tkr[p]+=hkl*GradSkorosti[l]
        Tkrit[p] = Tkrit[p] + Tkr[p]*0.001
        Tkr[p] = 0
    deltE = E-EP
    Epsi = Epsi + E * 0.001
    IntE.append(((2 / 3) * (np.tensordot(Epsi, Epsi, axes=2))) ** (1 / 2))
    i+=1
with open("IntSigm.txt", "a") as file:
    file.write(f"\n {IntSigm} ")
with open("IntE.txt", "a") as file:
    file.write(f"\n {IntE} ")
print(Sigm)

fig, ax = plt.subplots()
ax.set_title('График')
ax.plot(IntE,IntSigm )
plt.show()