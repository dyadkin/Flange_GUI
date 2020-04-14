# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def FlangeWithComplexHub():
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
    s.Line(point1=(0.0, 1.0335), point2=(0.0, 1.8125))
    s.VerticalConstraint(entity=g[3], addUndoState=False)
    s.Line(point1=(0.0, 1.8125), point2=(0.0625, 1.8125))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(0.0625, 1.8125), point2=(0.0625, 3.25))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.Line(point1=(0.0625, 3.25), point2=(0.8725, 3.25))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.Line(point1=(0.8725, 3.25), point2=(0.8725, 1.655))
    s.VerticalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=186.208, 
        farPlane=190.915, width=12.3632, height=6.26736, cameraPosition=(
        0.807396, 1.73441, 188.562), cameraTarget=(0.807396, 1.73441, 0))
    s.ArcByCenterEnds(center=(0.9925, 1.655), point1=(0.8725, 1.655), point2=(
        0.953431821465141, 1.54153777092808), direction=COUNTERCLOCKWISE)
    s.Line(point1=(0.953431821465141, 1.54153777092808), point2=(1.97437163970839, 
        1.19))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=187.92, 
        farPlane=189.204, width=3.81556, height=1.93426, cameraPosition=(
        1.00583, 1.71983, 188.562), cameraTarget=(1.00583, 1.71983, 0))
    s.Line(point1=(1.97437163970839, 1.19), point2=(2.64635389665607, 1.19))
    s.HorizontalConstraint(entity=g[10], addUndoState=False)
    s.Line(point1=(2.64635389665607, 1.19), point2=(2.7525, 1.0635))
    s.Line(point1=(2.7525, 1.0635), point2=(2.7525, 1.0335))
    s.VerticalConstraint(entity=g[12], addUndoState=False)
    s.Line(point1=(2.7525, 1.0335), point2=(0.0, 1.0335))
    s.HorizontalConstraint(entity=g[13], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=187.127, 
        farPlane=189.996, width=8.52897, height=4.32366, cameraPosition=(
        1.44564, 2.6527, 188.562), cameraTarget=(1.44564, 2.6527, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(1.61125, 
        1.40425, 188.562), cameraTarget=(1.61125, 1.40425, 0))
    s.ConstructionLine(point1=(-100.0, 0.0), point2=(0.0, 100.0))
    s.undo()
    s.ConstructionLine(point1=(-100.0, 0.0), point2=(100.0, 0.0))
    s.HorizontalConstraint(entity=g[14], addUndoState=False)
    s.sketchOptions.setValues(constructionGeometry=ON)
    s.assignCenterline(line=g[14])
    p = mdb.models['Model-1'].Part(name='RFWN', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['RFWN']
    p.BaseSolidRevolve(sketch=s, angle=180.0, flipRevolveDirection=OFF)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['RFWN']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.74776, 
        farPlane=22.2085, width=11.4479, height=5.11336, viewOffsetX=-0.592769, 
        viewOffsetY=-0.0123213)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=12.4509, 
        farPlane=21.1284, width=14.6225, height=6.53136, cameraPosition=(
        -14.6768, -0.808201, 6.69836), cameraUpVector=(0.181674, 0.892345, 
        -0.413176), cameraTarget=(0.867366, 0.372887, 3.19349), 
        viewOffsetX=-0.757148, viewOffsetY=-0.0157381)
    p = mdb.models['Model-1'].parts['RFWN']
    f, e = p.faces, p.edges
    t = p.MakeSketchTransform(sketchPlane=f[2], sketchUpEdge=e[7], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0625, 0.0, 
        0.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=14.52, gridSpacing=0.36, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['RFWN']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    s1.CircleByCenterPerimeter(center=(0.0, 2.5), point1=(0.0, 2.8125))
    s1.radialPattern(geomList=(g[6], ), vertexList=(), number=8, totalAngle=360.0, 
        centerPoint=(0.0, 0.0))
    p = mdb.models['Model-1'].parts['RFWN']
    f1, e1 = p.faces, p.edges
    p.CutExtrude(sketchPlane=f1[2], sketchUpEdge=e1[7], sketchPlaneSide=SIDE1, 
        sketchOrientation=RIGHT, sketch=s1, flipExtrudeDirection=OFF)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']


