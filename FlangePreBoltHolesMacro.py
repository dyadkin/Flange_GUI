# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Flange():
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
    s.Line(point1=(0.0, 5.01), point2=(0.0, 6.375))
    s.VerticalConstraint(entity=g[3], addUndoState=False)
    s.Line(point1=(0.0, 6.375), point2=(0.0625, 6.375))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=186.724, 
        farPlane=190.399, width=9.65252, height=4.89324, cameraPosition=(
        0.221212, 5.99248, 188.562), cameraTarget=(0.221212, 5.99248, 0))
    s.Line(point1=(0.0625, 6.375), point2=(0.0625, 8.75))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=186.35, 
        farPlane=190.774, width=13.1523, height=6.66741, cameraPosition=(
        0.180609, 5.73291, 188.562), cameraTarget=(0.180609, 5.73291, 0))
    s.Line(point1=(0.0625, 8.75), point2=(1.875, 8.75))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.Line(point1=(1.875, 8.75), point2=(1.8725, 6.32))
    s.Line(point1=(1.8725, 6.32), point2=(4.6225, 5.375))
    s.Line(point1=(4.6225, 5.375), point2=(4.6225, 5.01))
    s.VerticalConstraint(entity=g[9], addUndoState=False)
    s.Line(point1=(4.6225, 5.01), point2=(0.0, 5.01))
    s.HorizontalConstraint(entity=g[10], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=185.547, 
        farPlane=191.576, width=17.921, height=9.08485, cameraPosition=(
        -0.197493, 6.2282, 188.562), cameraTarget=(-0.197493, 6.2282, 0))
    s.ConstructionLine(point1=(0.0, 0.0), point2=(10.0, 0.0))
    s.HorizontalConstraint(entity=g[11], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=172.539, 
        farPlane=204.585, width=84.1717, height=42.6699, cameraPosition=(
        -4.32974, 21.1259, 188.562), cameraTarget=(-4.32974, 21.1259, 0))
    s.sketchOptions.setValues(constructionGeometry=ON)
    s.assignCenterline(line=g[11])
    p = mdb.models['Model-1'].Part(name='RFWN', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['RFWN']
    p.BaseSolidRevolve(sketch=s, angle=180.0, flipRevolveDirection=OFF)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['RFWN']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


