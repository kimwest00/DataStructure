#1.def Dijkstra pseudo 코드 수정하기
#2. main문에서 가중치(pseduo코드에서는 cost(u,v)로 형태로 사용함)저장
#3. AdaptedHeap 클래스에서 decreasekey 함수만들기

class AdaptedHeap: # min_heap으로 정의함!
	def __init__(self):
		self.A = []
		self.D = {}  # dictionary D[key] = index 
	def __str__(self):
		return str(self.A)
	def __len__(self):
		return len(self.A)

	def heapify_up(self, k):	# 올라가면서 A[k]를 재베치
		while k > 0 and self.A[(k-1)//2] > self.A[k] :
			self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
			self.D[self.A[k]],self.D[self.A[(k-1)//2]] = self.D[self.A[(k-1)//2]],self.D[self.A[k]]
			k = (k-1)//2
			
	def insert(self, key):
		self.A.append(key)
		self.D[key] = len(self.A)-1
		self.heapify_up(len(self.A)-1)
		return self.D[key]
		
	
	def heapify_down(self, k, n):
		while 2*k+1<n:
			L,R = 2*k+1, 2*k+2
			if L<n and self.A[L] < self.A[k]:
				m = L
			else:
				m = k
			if R<n and self.A[R]<self.A[m]:
				m=R
				
			if m !=k:
				self.D[self.A[m]]=k
				self.D[self.A[k]]=m
				self.A[k],self.A[m] = self.A[m],self.A[k]
			
				k= m
			else: 
				break
				
			

	def find_min(self):
		# 빈 heap이면 None 리턴, 아니면 min 값 리턴
		# code here
		if len(self.A) == 0: return None
		#self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
		#self.heapify_down(0, len(self.A)) # len(self.A) = n-1
		key = self.A[0]
		return key

	def delete_min(self):
		# 빈 heap이면 None 리턴, 아니면 min 값 지운 후 리턴

		if len(self.A) == 0: 
			return None
		
		self.D[self.A[0]] = len(self.A)-1
		self.D[self.A[len(self.A)-1]] = 0
		
		self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
		
		key = self.A[-1]
		self.D.pop(self.A[-1])
		self.A.pop()	# 실제로 리스트에서 delete!
		
		self.heapify_down(0, len(self.A)) # len(self.A) = n-1
		
		return key
	def decreaseKey(v,dist[v]):
		pass
def Dijkstra(G):
	#numbers of nodes and edges of G
	s = source node, simply 0
	dist = [0, inf, ..., inf]
	parent = [0, NULL, ..., NULL]
	H = AdaptedHeap()#괄호안에 H에 들어갈 리스트 넣어야함
	H.make_heap(nodes v of G with key dist[v])
	while len(H): # n iterations
		u = H.delete_min()
		for each v adjacent to u: # m edges are scanned in total
			if (u, v) is an edge of G:
				if dist[u] + cost(u, v) < dist[v]:
					dist[v] = dist[u] + cost(u, v)
					parent[v] = u
					H.decreaseKey(v, dist[v])
	return dist, parent

n = int(input())#노드 개수
m = int((input()))#에지 개수
G = [[] for _ in range(n)]
# G 입력 받아 처리
for _ in range(m):
	u, v, w = [int(x) for x in input().split()]#w는 가중치
	G[u].append(u)
	G[v].append(v)
   
for v in range(n):
   G[v].sort()
dist,parent = Dijkstra(G)
for i in dist:
	print(i ,end =' ')

'''
참고 DFS 코드
def DFS(G, v):
	global curr_time
	# 그래프 G의 노드 v를 DFS 방문한다
	visited[v] = True
	pre[v] = curr_time
	curr_time += 1
	for w in G[v]:
		if visited[w] == False:
			 DFS(G, w)
	post[v] = curr_time
	curr_time += 1
# 입력 처리
n = int(input())#노드 개수
m = int((input()))#에지 개수
G = [[] for _ in range(n)]
# G 입력 받아 처리
for _ in range(m):
	a, b = [int(x) for x in input().split()]
	G[a].append(b)
	G[b].append(a)
   
for v in range(n):
   G[v].sort()
# visited, pre, post 리스트 정의와 초기화
visited = [False for _ in range(n)]
pre, post = [0] * n, [0] * n
# curr_time = 1로 초기화
curr_time = 1

DFSAll(G)
# 출력
pair = list(zip([i for i in range(n)], pre))
pair.sort(key=lambda x: x[1])
for v, _ in pair:
   print(v, end=' ')
print()
for x, y in zip(pre, post):
   print(f"[{x}, {y}]", end=' ')
print()'''