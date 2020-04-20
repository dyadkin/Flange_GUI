# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def makeGasket(dimensions, gasketThickness):
    gasketOD = dimensions[0]
    gasketID = dimensions[1]
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s.FixedConstraint(entity=g[2])
    s.ConstructionLine(point1=(-100.0, 0.0), point2=(100.0, 0.0))
    s.HorizontalConstraint(entity=g[3], addUndoState=False)
    s.Line(point1=(0.0, gasketID/2), point2=(0.0, gasketOD/2))
    s.VerticalConstraint(entity=g[4], addUndoState=False)
    s.ParallelConstraint(entity1=g[2], entity2=g[4], addUndoState=False)
    # s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
    # s.CoincidentConstraint(entity1=v[1], entity2=g[2], addUndoState=False)
    s.Line(point1=(0.0, gasketOD/2), point2=(gasketThickness, gasketOD/2))
    s.HorizontalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.Line(point1=(gasketThickness, gasketOD/2), point2=(gasketThickness, gasketID/2))
    s.VerticalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.Line(point1=(gasketThickness, gasketID/2), point2=(0.0, gasketID/2))
    s.HorizontalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s.sketchOptions.setValues(constructionGeometry=ON)
    s.assignCenterline(line=g[3])
    p = mdb.models['Model-1'].Part(name='Gasket', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Gasket']
    p.BaseSolidRevolve(sketch=s, angle=180.0, flipRevolveDirection=OFF)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Gasket']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


def Gasket2():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s.FixedConstraint(entity=g[2])
    s.Line(point1=(0.0, 6.25), point2=(0.0, 15.5643310546875))
    s.VerticalConstraint(entity=g[3], addUndoState=False)
    s.ParallelConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
    s.CoincidentConstraint(entity1=v[1], entity2=g[2], addUndoState=False)
    s.Line(point1=(0.0, 15.5643310546875), point2=(6.25, 15.5643310546875))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(6.25, 15.5643310546875), point2=(6.25, 6.25))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.Line(point1=(6.25, 6.25), point2=(0.0, 6.25))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.ConstructionLine(point1=(-100.0, 0.0), point2=(100.0, 0.0))
    s.HorizontalConstraint(entity=g[7], addUndoState=False)
    s.sketchOptions.setValues(constructionGeometry=ON)
    s.assignCenterline(line=g[7])
    p = mdb.models['Model-1'].Part(name='Gasket', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Gasket']
    p.BaseSolidRevolve(sketch=s, angle=180.0, flipRevolveDirection=OFF)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Gasket']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


