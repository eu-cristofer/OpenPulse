import vtk
import random
from pulse.preprocessing.node import Node

class Point:
    def __init__(self, node, tag = -1):

        self.x = node.x
        self.y = node.y
        self.z = node.z
        self.color = [0,0,1]
        self.special = True
        if node.haveBoundaryCondition() and node.haveForce():
            self.color = [0,1,0]
        elif node.haveBoundaryCondition():
            self.color = [0,1,1]
        elif node.haveForce():
            self.color = [1,1,0]
        else:
            self.special = False
        self.tag = tag

        self.sphere = vtk.vtkSphereSource()
        self.cube = vtk.vtkCubeSource ()

        self._object = vtk.vtkPolyData()

        self._colorFilter = vtk.vtkUnsignedCharArray()
        self._colorFilter.SetNumberOfComponents(3)

        self._mapper = vtk.vtkPolyDataMapper()

        self._line_actor = vtk.vtkActor()

    def assembly(self):
        self._source()
        self._filter()
        self._map()
        self._actor()

    def _source(self):
        self.sphere.SetRadius(0.03)
        self.sphere.SetCenter(self.x, self.y, self.z)
        self.sphere.SetPhiResolution(11)
        self.sphere.SetThetaResolution(21)

        self.cube.SetXLength(0.01)
        self.cube.SetYLength(0.01)
        self.cube.SetZLength(0.01)
        self.cube.SetCenter(self.x, self.y, self.z)

    def _filter(self):
        pass
        # color = [0,255,0]
        # for _ in range(self._nodes.GetNumberOfPoints()):
        #     self._colorFilter.InsertNextTypedTuple(color)

        # self._object.GetPointData().SetScalars(self._colorFilter)

    def _map(self):
        if self.special:
            self._mapper.SetInputConnection(self.sphere.GetOutputPort())
        else:
            self._mapper.SetInputConnection(self.cube.GetOutputPort())
        self._mapper.ScalarVisibilityOff()

    def _actor(self):
        self._line_actor.SetMapper(self._mapper)
        #self._line_actor.GetProperty().SetDiffuseColor(1,0,.5)
        self._line_actor.GetProperty().SetColor(self.color)
        self._line_actor.GetProperty().SetDiffuse(.8)
        self._line_actor.GetProperty().SetSpecular(.5)
        self._line_actor.GetProperty().SetSpecularColor(1.0, 1.0, 1.0)
        self._line_actor.GetProperty().SetSpecularPower(30.0)

    def get_actor(self):
        return self._line_actor