import networkx as nx
import matplotlib.pyplot as plt
from random import randint
from random import random as rand
import cyaron
from cyaron import *

class Map():
	def __init__(self,n,m):
		self.G=nx.MultiGraph()
		self.n=n
		self.m=m
		self.edges_dic={}
		self.f=[i for i in range(n+1)]
		self.cols=[]
		self.node_col='red'
		self.edge_col='blue'
		self.path_col='red'

	def CreateNolmalMap(self):
		graph=Graph.graph(self.n,self.m,weight_limit=10,self_loop=False,repeated_edges=False)
		File=open('graph.in','w')
		print(graph,file=File)
		File.close()
		File=open('graph.in','r')
		for i in range(self.m):
			x,y,l=map(int,File.readline().split())
			x-=1
			y-=1
			self.G.add_edge(x,y,color=self.edge_col)
			self.edges_dic[(x,y)]=l
			self.edges_dic[(y,x)]=l
		
		for i in range(self.n):
			self.G.add_edge(i,i,color=self.edge_col)

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
		self.cols=[]
		for i in self.G.edges(data=True):
			if (v[i[0]] and v[i[1]] and (fr[i[1]]==i[0] or fr[i[0]]==i[1])):
				self.cols.append(self.path_col)
			else:
				self.cols.append(i[2]['color'])

	def CreateTree(self):
		self.f=[i for i in range(self.n+1)]
		lit=sorted(self.edges_dic.items(), key=lambda d:d[1])
		cse={}
		tot=0
		for i in lit:
			x=self.Find(i[0][0])
			y=self.Find(i[0][1])
			if (x==y):
				continue
			cse[(i[0][0],i[0][1])]=1
			self.f[x]=y
			tot+=i[1]
		print(tot)
		self.cols=[]
		for i in self.G.edges(data=True):
			if ((i[0],i[1]) in cse or (i[1],i[0]) in  cse):
				self.cols.append(self.path_col)
			else:
				self.cols.append(i[2]['color'])

	def Draw(self):
		plt.cla()
		pos=nx.spring_layout(self.G)
		nx.draw_networkx_nodes(self.G,pos,node_color=self.node_col,node_size=500)
		if (self.cols == []):
			for i in self.G.edges(data=True):
				self.cols.append(self.edge_col)

		nx.draw_networkx_edges(self.G,pos,width=3,edge_color=self.cols)
		# TODO alpha-setting
		# TODO beautify
		nx.draw_networkx_labels(self.G,pos)
		nx.draw_networkx_edge_labels(self.G, pos,self.edges_dic,font_size=10)
		plt.savefig("b.png",format="PNG")