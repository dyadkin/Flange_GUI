# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def FlangeWithBoltHoles(raisedFace, raisedFaceOD, flangeOD, boltCircleD, boltHoles, boltD, flangeThickness, 
    hubD, pipeOD, hubLength, pipeID):
    # import section
    # import regionToolset
    # import displayGroupMdbToolset as dgm
    # import part
    # import material
    # import assembly
    # import step
    # import interaction
    # import load
    # import mesh
    # import optimization
    # import job
    # import sketch
    # import visualization
    # import xyPlot
    # import displayGroupOdbToolset as dgo
    # import connectorBehavior
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s.FixedConstraint(entity=g[2])
    s.Line(point1=(0.0, pipeID/2), point2=(0.0, raisedFaceOD/2))
    s.VerticalConstraint(entity=g[3], addUndoState=False)
    s.Line(point1=(0.0, raisedFaceOD/2), point2=(raisedFace, raisedFaceOD/2))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(raisedFace, raisedFaceOD/2), point2=(raisedFace, flangeOD/2))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.Line(point1=(raisedFace, flangeOD/2), point2=(raisedFace + flangeThickness, flangeOD/2))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.Line(point1=(raisedFace + flangeThickness, flangeOD/2), point2=(raisedFace + flangeThickness, hubD/2))
    s.VerticalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s.Line(point1=(raisedFace + flangeThickness, hubD/2), point2=(hubLength + raisedFace, pipeOD/2))
    s.Line(point1=(hubLength + raisedFace, pipeOD/2), point2=(hubLength + raisedFace, pipeID/2))
    s.VerticalConstraint(entity=g[9], addUndoState=False)
    s.Line(point1=(hubLength + raisedFace, pipeID/2), point2=(0.0, pipeID/2))
    s.HorizontalConstraint(entity=g[10], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
    s.ConstructionLine(point1=(-100.0, 0.0), point2=(100.0, 0.0))
    s.HorizontalConstraint(entity=g[11], addUndoState=False)
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=31.6709, 
        farPlane=51.3197, width=33.941, height=16.1832, cameraPosition=(
        -38.8936, -4.88734, 3.9747), cameraUpVector=(0.218028, 0.969938, 
        -0.108093), cameraTarget=(2.15681, 0.144696, 4.38473))
    p = mdb.models['Model-1'].parts['RFWN']
    f, e = p.faces, p.edges
    t = p.MakeSketchTransform(sketchPlane=f[2], sketchUpEdge=e[7], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(raisedFace, 0.0, 
        0.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=39.09, gridSpacing=0.97, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['RFWN']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    s1.CircleByCenterPerimeter(center=(0.0, boltCircleD/2), point1=(0.0, boltCircleD/2 + boltD/2))
    s1.radialPattern(geomList=(g[6], ), vertexList=(), number=boltHoles, totalAngle=360.0, 
        centerPoint=(0.0, 0.0))
    p = mdb.models['Model-1'].parts['RFWN']
    f1, e1 = p.faces, p.edges
    p.CutExtrude(sketchPlane=f1[2], sketchUpEdge=e1[7], sketchPlaneSide=SIDE1, 
        sketchOrientation=RIGHT, sketch=s1, flipExtrudeDirection=OFF)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']


