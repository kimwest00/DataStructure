class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)


class Tree:
		def __init__(self):
				self.root = None
				self.size = 0

		def __len__(self):
				return self.size
		#1.가장 왼쪽트리로 이동(v.left == None)<= v.left !=None일때까지 계속 속으로 이동(재귀호출)
		#2.v.left -> v.key -> v.right (<->preorder의 경우 v.key가 바로 )
		def isLeft(self,v):
			if v.left == None:
				return v
			else:
				return self.isLeft(v.left)
		def inorder (self, v):
			p = self.isLeft(v)
			if p != None:
				print(p.key,end=' ')
				self.inorder(p.parent)
				self.inorder(p.left)
		
# Tree class의 method로 선언
		def preorder(self, v): # 노드 v와 자손 노드를 preorder로 방문하면서 출력
			if v != None:
				print(v.key, end =' ')
				self.preorder(v.left)
				self.preorder(v.right)
				
		def postorder(self,v):
    		
			if v != None:
				self.inorder(v.left)
				#self.inorder(v.parent)#해당코드는 처음 inorder함수가 실행될때,v.parent가 없으므로 에러남
				print(v.key)
				self.inorder(v.right)

		def find_loc(self, key): # if key is in T, return its Node
			# if not in T, return the parent node under where it is inserted
			if self.size == 0:
				return None
			p = None    # p = parent node of v
			v = self.root
			while v:    # while v != None
				if v.key == key:
					return v
				else:
					if v.key < key:
						p = v
						v = v.right
					else:
						p = v
						v = v.left
			return p

		def search(self, key):
			p = self.find_loc(key)
			if p and p.key == key:
				return p
			else:
				return None
		def insert(self, key):
			v = Node(key)
			if self.size == 0: 
				self.root = v
			else:
				p = self.find_loc(key)
				if p and p.key != key: # p is parent of v
					if p.key < key: 
						p.right = v
					else: 
						p.left = v
					v.parent = p
			self.size += 1
			return v
T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        if v != None:
            print("+ {0} is set into H".format(v.key))
        else:
            print(v.key, "is already in the tree!")
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
