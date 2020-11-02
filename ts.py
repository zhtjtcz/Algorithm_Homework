import networkx as nx
import matplotlib.pyplot as plt
from random import randint
from random import random as rand

class Map():
	def __init__(self,n,pho):
		self.G=nx.MultiGraph()
		self.n=n
		self.p=1-pho
		self.edges_dic={}
		self.f=[i for i in range(n+1)]
		self.cols=[]
		self.alpha=[]

	def CreateNolmalMap(self):
		for i in range(self.n):
			for j in range(i+1,self.n):
				x=rand()
				if (x>=self.p):
					l=randint(1,10)
					self.G.add_edge(i,j,color='b')
					self.edges_dic[(i,j)]=l
					self.edges_dic[(j,i)]=l
		
		for i in range(self.n):
			self.G.add_edge(i,i,color='b')

	def Find(self,x):
		if (x==self.f[x]):
			return x
		else:
			return self.Find(self.f[x])

	def IsConneted(self):
		for i in range(self.n):
			self.f[i]=i
		for i in self.G.edges:
			x=self.Find(i[0])
			y=self.Find(i[1])
			if (x==y):
					continue
			self.f[x]=y
		for i in range(self.n):
			if (self.Find(i)!=self.Find(0)):
				return False
		return True

	def ShortestPath(self):
		while (self.IsConneted()==False):
			self.CreateNolmalMap()
		v=[0 for i in range(self.n+1)]
		z=[0 for i in range(self.n+1)]
		fr=[0 for i in range(self.n+1)]
		dis=[0x3f3f3f3f for i in range(self.n+1)]
		t=0
		v[0]=1
		w=1
		z[1]=0
		dis[0]=0
		while (t!=w):
			t=(t+1)%self.n
			x=z[t]
			v[x]=0
			for i in range(self.n):
				if (i!=x and self.G.has_edge(x,i)):
					if (dis[i]>dis[x]+self.edges_dic[(x,i)]):
						dis[i]=dis[x]+self.edges_dic[(x,i)]
						fr[i]=x
						if (v[i]):
							continue
						v[i]=1
						w=(w+1)%self.n
						z[w]=i
		print(dis[self.n-1])
		x=self.n-1
		v=[0 for i in range(self.n+1)]
		while (x):
			v[x]=1
			x=fr[x]
		v[0]=1
		for i in self.G.edges(data=True):
			if (v[i[0]] and v[i[1]] and (fr[i[1]]==i[0] or fr[i[0]]==i[1])):
				self.cols.append('r')
			else:
				self.cols.append(i[2]['color'])

	def CreateTree(self):
		self.f=[i for i in range(self.n+1)]
		lit=sorted(self.edges_dic.items(), key=lambda d:d[1])
		cse={}
		tot=0
		#print(lit)
		for i in lit:
			x=self.Find(i[0][0])
			y=self.Find(i[0][1])
			if (x==y):
				continue
			cse[(i[0][0],i[0][1])]=1
			self.f[x]=y
			tot+=i[1]
		print(tot)
		for i in self.G.edges(data=True):
			if ((i[0],i[1]) in cse or (i[1],i[0]) in  cse):
				self.cols.append('r')
				self.alpha.append(1)
			else:
				self.cols.append(i[2]['color'])
				self.alpha.append(0.5)

	def Draw(self):
		pos=nx.spring_layout(self.G)
		nx.draw_networkx_nodes(self.G,pos,node_size=500)
		nx.draw_networkx_edges(self.G,pos,width=3,edge_color=self.cols)
		# TODO alpha-setting
		nx.draw_networkx_labels(self.G,pos)
		nx.draw_networkx_edge_labels(self.G, pos,self.edges_dic,font_size=10)
		plt.show()

a=Map(10,0.4)
a.CreateNolmalMap()
#a.ShortestPath()
a.CreateTree()
a.Draw()

'''
G=nx.Graph()
G.add_edge(1,2,color='r')
G.add_edge(2,3,color='g')
G.add_edge(3,4,color='b')
cols=[]
for i in G.edges(data=True):
	cols.append(i[2]['color'])
print(cols)
nx.draw(G,with_lables=True,edge_color=cols)
plt.show()
'''
