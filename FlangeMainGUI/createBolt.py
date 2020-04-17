# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def makeBolt(dimensions, gasketThickness):
    raisedFace=dimensions.get("flangeDimensions")[0]
    flangeThickness=dimensions.get("flangeDimensions")[6]
    boltStressD=dimensions.get("boltDimensions")[0]
    hexWidth=dimensions.get("boltDimensions")[1]
    hexThickness=dimensions.get("boltDimensions")[2]


    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s.FixedConstraint(entity=g[2])
    s.ConstructionLine(point1=(-100.0, 0.0), point2=(100.0, 0.0))
    s.HorizontalConstraint(entity=g[3], addUndoState=False)
    s.Line(point1=(-(raisedFace+flangeThickness+gasketThickness/2+hexThickness), 0.0), point2=(-(raisedFace+flangeThickness+gasketThickness/2+hexThickness), hexWidth/2))
    s.VerticalConstraint(entity=g[4], addUndoState=False)
    s.ParallelConstraint(entity1=g[2], entity2=g[4], addUndoState=False)
    # s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
    # s.CoincidentConstraint(entity1=v[1], entity2=g[2], addUndoState=False)
    s.Line(point1=(-(raisedFace+flangeThickness+gasketThickness/2+hexThickness), hexWidth/2), point2=(-(raisedFace+flangeThickness+gasketThickness/2), hexWidth/2))
    s.HorizontalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.Line(point1=(-(raisedFace+flangeThickness+gasketThickness/2), hexWidth/2), point2=(-(raisedFace+flangeThickness+gasketThickness/2), boltStressD/2))
    s.VerticalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.Line(point1=(-(raisedFace+flangeThickness+gasketThickness/2), boltStressD/2), point2=(raisedFace+flangeThickness+gasketThickness/2, boltStressD/2))
    s.HorizontalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s.Line(point1=(raisedFace+flangeThickness+gasketThickness/2, boltStressD/2), point2=(raisedFace+flangeThickness+gasketThickness/2, hexWidth/2))
    s.VerticalConstraint(entity=g[8], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
    s.Line(point1=(raisedFace+flangeThickness+gasketThickness/2, hexWidth/2), point2=(raisedFace+flangeThickness+gasketThickness/2+hexThickness, hexWidth/2))
    s.HorizontalConstraint(entity=g[9], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
    s.Line(point1=(raisedFace+flangeThickness+gasketThickness/2+hexThickness, hexWidth/2), point2=(raisedFace+flangeThickness+gasketThickness/2+hexThickness, 0.0))
    s.VerticalConstraint(entity=g[10], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
    s.CoincidentConstraint(entity1=v[7], entity2=g[3], addUndoState=False)
    s.Line(point1=(raisedFace+flangeThickness+gasketThickness/2+hexThickness, 0.0), point2=(-(raisedFace+flangeThickness+gasketThickness/2+hexThickness), 0.0))
    s.HorizontalConstraint(entity=g[11], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
    s.sketchOptions.setValues(constructionGeometry=ON)
    s.assignCenterline(line=g[3])
    p = mdb.models['Model-1'].Part(name='Bolt', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Bolt']
    p.BaseSolidRevolve(sketch=s, angle=360.0, flipRevolveDirection=OFF)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Bolt']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']