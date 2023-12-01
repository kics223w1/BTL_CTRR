import numpy as np
import networkx as nx
def StrArrayRead(filename):
    with open(filename, 'r') as file:
        data = [tuple(map(int, line.strip().split())) for line in file]
    return data

def set_zero_rows(sparray, rowNum):
    for row in rowNum:
        sparray.data[sparray.indptr[row]:sparray.indptr[row + 1]] = 0

def set_diag_val(sparray, val):
    r, c = sparray.shape
    for row in range(r):
        sparray[row, row] = val

def StrArrayWrite(nparray, filename):
    with open(filename, "wt", buffering=20*(1024**2)) as f:
        data = [str(float(row[0])) + '\t' + str(float(row[1])) + '\n' for row in nparray]
        f.write(''.join(data))

def ktruss(inc_mat_file, k):
    ii = StrArrayRead(inc_mat_file)
# Create the graph
    G = nx.Graph()
    G.add_edges_from(ii)
# Lấy ma trận cạnh kề
    E = nx.incidence_matrix(G).todense()
  
   # tmp = np.dot(np.transpose(E), E)
    d = np.sum(E, axis=0)
    A = np.dot(np.transpose(E), E) - np.diag(d)
    R = np.dot(E, A)
    s = (R == 2).astype(int)
    x = np.where(s.sum(axis=1) < k - 2)[0]
    while len(x) > 0:
        Ex = E[x, :]
        E = E[np.where(s.sum(axis=1) >= k - 2)[0], :]
        dx =np.sum(Ex, axis=0)
        R = R[np.where(s.sum(axis=1) >= k - 2)[0], :]
        R = R - np.dot(E,np.dot(np.transpose(Ex),Ex))
        ##print(R)
        s = (R == 2).astype(int)
        x = np.where(s.sum(axis=1) < k - 2)[0]

    return E



