#!/usr/bin/python
from glob import glob

class ClassDiagramGenerator:
	"""A class that generates a graph of files given a root directory"""
	def __init__(self, rootDirectory, fileExtension):
		self.rootDirectory = rootDirectory
		self.fileExtension = fileExtension
		files = self.getFiles(self.rootDirectory, self.fileExtension)

	# Return a list of all files in root directory and sub directories ending in fileExtension
	def getFiles(self, rootDirectory, fileExtension):
		files = glob(rootDirectory + '/**/*.'+ fileExtension, recursive=True)
		return files;

	# Returns a directed graph of files
	def buildGraph(self, files):
		graph = Graph()
		#map of filename to Vertex
		createdVertexes = dict()
		#for each file in files
		for fileName in files:
			print(fileName)
			#get or create vertex with file path as value
			currentVertex = None
			if filename in createdVertexes:
				currentVertex = createdVertexes[fileName]
			else:
				currentVertex = Vertex(fileName)
				createdVertexes[fileName] = currentVertex
				graph.add_vertex(currentVertex)
			#get referenced files
			referencedFiles = self.getReferencedFiles(files, fileName)
			#for each referenced file
			for referencedFile in referencedFiles:
				#if file was added to graph, get node
				referencedNode = None
				if referencedFile in createdVertexes:
					referencedNode = createdVertexes[referencedFile]
				#else create new node
				else:
					referencedNode = Vertex(referencedFile)
					createdVertexes[referencedFile] = referencedNode
					graph.add_vertex(referencedNode)
				#add node as neighbor
				currentVertex.add_neighbor(referencedNode)
		return graph

	# Returns a list of all files in 'files' referenced by 'currentFile'
	def getReferencedFiles(self, files, currentFile):
		referencedFiles = ['universalFile.py']
		#open currentFile
		#parse import statements
		#for each file in files
		for file in files:
			#if file is mentioned in import statements
			if True:
				#add to referencedFiles
				getReferencedFiles.append(referencedFile)
				
		return referencedFiles

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()