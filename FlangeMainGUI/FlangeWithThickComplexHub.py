# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__
import math

def flange(dimensions, pipeSchedule):
    raisedFace = dimensions[0]
    raisedFaceOD = dimensions[1]
    flangeOD = dimensions[2]
    boltCircleD = dimensions[3]
    boltHoles = dimensions[4]
    boltD = dimensions[5]
    flangeThickness = dimensions[6]
    hubD = dimensions[7]
    pipeOD = dimensions[8]
    hubLength = dimensions[9]
    pipeID = pipeOD - 2*pipeSchedule
    r = 0.12
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
    s.Line(point1=(raisedFace, flangeOD/2), point2=(flangeThickness + raisedFace, flangeOD/2))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.Line(point1=(flangeThickness + raisedFace, flangeOD/2), point2=(flangeThickness + raisedFace, hubD/2))
    s.VerticalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)

    #Hub Geometry
    if pipeSchedule <= 0.88:
        model2 = False
        x_right = hubLength+raisedFace-(pipeOD/2-pipeID/2-0.03)*math.tan(math.radians(40))
    else:
        model2 = True
        x_right = hubLength+raisedFace-((3.0/4.0)-0.03)*math.tan(math.radians(40))-(pipeSchedule-(3.0/4.0))*math.tan(math.radians(12.5))

    for alpha in range(19, 45):
        theta = 90-alpha
        x = flangeThickness+raisedFace
        y = hubD/2

        A = x+r*(1-math.cos(math.radians(theta)))
        B = y-r*math.sin(math.radians(theta))

        m = - (A-x-r)/(B-y) 
        b =  B-m*A 

        y2 = pipeOD/2
        x2 = (y2-b)/m

        if x_right-x2 >= 0.25:
            break

    s.ArcByCenterEnds(center=(flangeThickness + raisedFace + r, hubD/2), point1=(flangeThickness + raisedFace, hubD/2), point2=(
        A, B), direction=COUNTERCLOCKWISE)
    s.Line(point1=(A, B), point2=(x2, y2))
    s.Line(point1=(x2, y2), point2=(x_right, y2)) #point2=(hubLength + raisedFace, y2)
    s.HorizontalConstraint(entity=g[10], addUndoState=False)
    if model2:
        print("model2")
        s.Line(point1=(x_right, y2), point2=(x_right + (pipeSchedule - 3.0/4.0)*math.tan(math.radians(12.5)),
            pipeOD/2 - (pipeSchedule - 3.0/4.0)))
        s.Line(point1=(x_right + (pipeSchedule - 3.0/4.0)*math.tan(math.radians(12.5)), pipeOD/2 - (pipeSchedule - 3.0/4.0)),
            point2=(hubLength + raisedFace, pipeID/2 + .03))
        s.Line(point1=(hubLength + raisedFace, pipeID/2 + .03), point2=(hubLength + raisedFace, pipeID/2))
        s.VerticalConstraint(entity=g[13], addUndoState=False)
        s.Line(point1=(hubLength + raisedFace, pipeID/2), point2=(0.0, pipeID/2))
        s.HorizontalConstraint(entity=g[14], addUndoState=False)
        s.PerpendicularConstraint(entity1=g[13], entity2=g[14], addUndoState=False)
        s.ConstructionLine(point1=(-100.0, 0.0), point2=(100.0, 0.0))
        s.HorizontalConstraint(entity=g[15], addUndoState=False)
        s.sketchOptions.setValues(constructionGeometry=ON)
        s.assignCenterline(line=g[15])
    else:
        s.Line(point1=(x_right, y2), point2=(hubLength + raisedFace, pipeID/2 + .03)) #Diagoanl line to be removed
        s.Line(point1=(hubLength + raisedFace, pipeID/2 + .03), point2=(hubLength + raisedFace, pipeID/2)) #point1=(hubLength+raisedFace, y2)
        s.VerticalConstraint(entity=g[12], addUndoState=False)
        s.Line(point1=(hubLength + raisedFace, pipeID/2), point2=(0.0, pipeID/2))
        s.HorizontalConstraint(entity=g[13], addUndoState=False)
        s.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
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
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['RFWN']
    f, e = p.faces, p.edges
    t = p.MakeSketchTransform(sketchPlane=f[2], sketchUpEdge=e[7], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(raisedFace, 0.0, 
        0.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=14.52, gridSpacing=0.36, transform=t)
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