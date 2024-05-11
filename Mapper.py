import numpy as np
import open3d as o3d
import math

from scipy.spatial import Delaunay



def triangles_to_mesh(triangles):
    vertices = np.array(triangles)  # Convert list of triangles to numpy array
    triangles = [[i, i + 1, i + 2] for i in range(0, len(vertices), 3)]  # Define triangle indices
    mesh = o3d.geometry.TriangleMesh()  # Create an empty mesh
    mesh.vertices = o3d.utility.Vector3dVector(vertices)  # Set vertices of the mesh
    mesh.triangles = o3d.utility.Vector3iVector(triangles)  # Set triangles of the mesh
    return mesh

def save_mesh_to_obj(mesh, filename):
    o3d.io.write_triangle_mesh(filename, mesh)  # Write mesh to OBJ file

def triangles_to_obj(triangles, filename):
    with open(filename, 'w') as f:
        # Write vertices
        for vertex in triangles:
            f.write("v " + " ".join(map(str, vertex)) + "\n")
        
        # Write faces
        for i in range(len(triangles)//3):
            f.write("f {} {} {}\n".format(3*i + 1, 3*i + 2, 3*i + 3))
            
            
def VisualizeTriangles(self, xlim = (-100, 2000), ylim = (-100, 1500)):


        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
        fig, ax = plt.subplots()

        ax.set_xlim(xlim[0], xlim[1])
        ax.set_ylim(ylim[0], ylim[1])
        for triangle in self.triangles:
            ax.add_patch(patches.Polygon(triangle[:, :2], True, edgecolor='red', facecolor='none'))

        plt.show()

# Example usage
if __name__ == "__main__":
    # Example list of triangles (each triangle defined by three vertices)
    data = []
    values = None 
    
    with open('datalog.txt', 'r') as f:
        data = f.readlines()
        values = np.zeros((len(data)))
        vertex = np.zeros(shape = (len(data), 3))
        for i in range(len(data)):
            line = data[i].split()
            line[0] = math.radians(int(line[0]))
            line[1] = math.radians(int(line[1]))
            line[2] = float(line[2])

            y = line[2] * math.sin(line[0])
            z = line[2] * math.sin(line[1]) *math.cos(line[0])
            x = line[2] * math.cos(line[1]) *math.cos(line[0])

            values[i] = z
            data[i] = [z, x]
            vertex[i] = np.array([x, z, y])
        
    tri = Delaunay(data)
         
    #Convert the triangles to a usable format
    triangles = tri.simplices
    
    print(triangles)
    # Convert triangles to mesh
    #triangles_to_obj(triangles, 'gay.obj')
      # Convert list of triangles to numpy array

    mesh = o3d.geometry.TriangleMesh()  # Create an empty mesh
    mesh.vertices = o3d.utility.Vector3dVector(vertex)  # Set vertices of the mesh
    mesh.triangles = o3d.utility.Vector3iVector(triangles)  # Set triangles of the mesh
    
    ## Save mesh to OBJ file
    save_mesh_to_obj(mesh, "gay.obj")