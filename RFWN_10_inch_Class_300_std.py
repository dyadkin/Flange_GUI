# -*- coding: mbcs -*-
#  RFWN 10 inch Class 300 std pipe schedule
#
from part import *
from material import *
from section import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(angle=0.0, 
    point1=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.5, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 5.01), point2=(
    0.0, 6.375))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 6.30675))
# mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
#     False, entity=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
#     6.30675), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 6.375), point2=
#     (0.0625, 6.375))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.03125, 6.375))
# mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
#     addUndoState=False, entity=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.03125, 
#     6.375), ))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 6.30675))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.03125, 6.375))
# mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
#     6.30675), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.03125, 
#     6.375), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0625, 6.375), 
#     point2=(0.0625, 8.75))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0625, 7.5625))
# mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
#     False, entity=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0625, 
#     7.5625), ))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.03125, 6.375))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0625, 7.5625))
# mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.03125, 
#     6.375), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0625, 
#     7.5625), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0625, 8.75), 
#     point2=(1.8725, 8.75))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.9675, 8.75))
# mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
#     addUndoState=False, entity=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.9675, 
#     8.75), ))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0625, 7.5625))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.9675, 8.75))
# mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0625, 
#     7.5625), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.9675, 
#     8.75), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.8725, 8.75), 
#     point2=(1.8725, 6.4063))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.8725, 
#     7.57815))
# mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
#     False, entity=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.8725, 
#     7.57815), ))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.9675, 8.75))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.8725, 
#     7.57815))
# mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.9675, 
#     8.75), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.8725, 
#     7.57815), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.94726, 6.2962), 
#     point2=(4.029, 5.375))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(4.029, 5.375), 
#     point2=(4.56, 5.375))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.2945, 5.375))
# mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
#     addUndoState=False, entity=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.2945, 
#     5.375), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(4.56, 5.375), 
#     point2=(4.56, 5.01))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.56, 5.1925))
# mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
#     False, entity=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.56, 
#     5.1925), ))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.2945, 5.375))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.56, 5.1925))
# mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.2945, 
#     5.375), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.56, 
#     5.1925), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(4.56, 5.01), point2=
#     (0.0, 5.01))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.28, 5.01))
# mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
#     addUndoState=False, entity=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.28, 5.01), 
#     ))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.56, 5.1925))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.28, 5.01))
# mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.56, 
#     5.1925), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.28, 5.01), 
#     ))
# mdb.models['Model-1'].sketches['__profile__'].ArcByCenterEnds(center=(1.995, 
#     6.4063), direction=CLOCKWISE, point1=(1.94726, 6.2962), point2=(1.8725, 
#     6.4063))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((1.874995, 
#     6.4063))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.8725, 
#     7.57815))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     1.87499534342368, 6.4063), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.8725, 
#     7.57815), ))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    constructionGeometry=ON)
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.5, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].assignCenterline(line=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.5, 0.0), 
#     ))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='RFWN_10_in_CL_300_std'
    , type=DEFORMABLE_BODY)
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].BaseSolidRevolve(angle=
#     180.0, flipRevolveDirection=OFF, sketch=
#     mdb.models['Model-1'].sketches['__profile__'])
# del mdb.models['Model-1'].sketches['__profile__']
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].setValues(
#     geometryRefinement=EXTRA_FINE)
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].DatumPlaneByPrincipalPlane(
#     offset=0.0, principalPlane=XYPLANE)
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].DatumPlaneByPrincipalPlane(
#     offset=0.0, principalPlane=YZPLANE)
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].DatumPlaneByPrincipalPlane(
#     offset=0.0, principalPlane=XZPLANE)
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].PartitionCellByExtendFace(
#     cells=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].cells.findAt(((
#     0.041667, -6.357241, 0.475514), )), extendFace=
#     mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].faces.findAt((0.0625, 
#     -7.908672, 0.535936), ))
# mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.97, name='__profile__', 
#     sheetSize=39.13, transform=
#     mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].MakeSketchTransform(
#     sketchPlane=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].faces.findAt(
#     (0.0625, -7.164107, 0.104269), ), sketchPlaneSide=SIDE1, 
#     sketchUpEdge=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].edges.findAt(
#     (0.0625, 6.96875, 0.0), ), sketchOrientation=RIGHT, origin=(0.0625, 0.0, 
#     0.0)))
mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
myViewport = session.Viewport(name='Viewport for Model A',
    origin=(10, 10), width=150, height=100)

myViewport.setValues(displayedObject= mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'])

myViewport.partDisplay.setValues(renderStyle=SHADED)
# mdb.models['Model-1'].sketches['__profile__'].ConstructionCircleByCenterPerimeter(
#     center=(0.0, 0.0), point1=(0.0, 7.625))
# mdb.models['Model-1'].sketches['__profile__'].ConstructionCircleByCenterPerimeter(
#     center=(0.0, 7.625), point1=(0.0, 8.25))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     0.0, 7.625), point1=(0.0, 8.25))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     2.91796, 7.04458), point1=(3.15714, 7.62201))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     5.39169, 5.39169), point1=(5.83363, 5.83363))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     7.04458, 2.91796), point1=(7.62201, 3.15714))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     7.625, 0.0), point1=(8.25, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     7.04458, -2.91796), point1=(7.62201, -3.15714))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     5.39169, -5.39169), point1=(5.83363, -5.83363))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     2.91896, -7.04458), point1=(3.15714, -7.62201))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     0.0, -7.625), point1=(0.0, -8.25))
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].CutExtrude(
#     flipExtrudeDirection=OFF, sketch=
#     mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, 
#     sketchPlane=
#     mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].faces.findAt((0.0625, 
#     -7.164107, 0.104269), ), sketchPlaneSide=SIDE1, sketchUpEdge=
#     mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].edges.findAt((0.0625, 
#     6.96875, 0.0), ))
# del mdb.models['Model-1'].sketches['__profile__']
# End
##### mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.98, name='__profile__', 
#     sheetSize=39.29, transform=
#     mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].MakeSketchTransform(
#     sketchPlane=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].faces.findAt(
#     (1.874995, -8.416416, 0.010222), ), sketchPlaneSide=SIDE1, 
#     sketchUpEdge=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].edges.findAt(
#     (1.874995, 6.851575, 0.0), ), sketchOrientation=RIGHT, origin=(1.874995, 
#     0.0, 0.0)))
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].projectReferencesOntoSketch(
#     filter=COPLANAR_EDGES, sketch=
#     mdb.models['Model-1'].sketches['__profile__'])
# mdb.models['Model-1'].sketches['__profile__'].ConstructionCircleByCenterPerimeter(
#     center=(0.0, 0.0), point1=(0.0, 7.625))
# mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
#     0.0), point2=(2.91896, 7.04458))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.45948, 
#     3.52229))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 0.0), )
#     , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
#     1.45948, 3.52229), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((2.91896, 
#     7.04458))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.45948, 
#     3.52229))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((2.91896, 
#     7.04458), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.45948, 
#     3.52229), ))
# mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
#     0.0), point2=(5.39169, 5.39169))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.695845, 
#     2.695845))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 0.0), )
#     , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
#     2.695845, 2.695845), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((5.39169, 
#     5.39169))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.695845, 
#     2.695845))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((5.39169, 
#     5.39169), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.695845, 
#     2.695845), ))
# mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
#     0.0), point2=(7.04458, 2.91796))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.52229, 
#     1.45898))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 0.0), )
#     , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
#     3.52229, 1.45898), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((7.04458, 
#     2.91796))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.52229, 
#     1.45898))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((7.04458, 
#     2.91796), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.52229, 
#     1.45898), ))
# mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
#     0.0), point2=(7.04458, -2.91796))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.52229, 
#     -1.45898))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 0.0), )
#     , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
#     3.52229, -1.45898), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((7.04458, 
#     -2.91796))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.52229, 
#     -1.45898))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((7.04458, 
#     -2.91796), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.52229, 
#     -1.45898), ))
# mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
#     0.0), point2=(5.39169, -5.39169))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.695845, 
#     -2.695845))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 0.0), )
#     , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
#     2.695845, -2.695845), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((5.39169, 
#     -5.39169))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.695845, 
#     -2.695845))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((5.39169, 
#     -5.39169), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.695845, 
#     -2.695845), ))
# mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
#     0.0), point2=(2.91796, -7.04458))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.45898, 
#     -3.52229))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 0.0), )
#     , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
#     1.45898, -3.52229), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((2.91796, 
#     -7.04458))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.45898, 
#     -3.52229))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((2.91796, 
#     -7.04458), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.45898, 
#     -3.52229), ))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     0.0, 7.625), point1=(0.0, 8.4375))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     2.91896, 7.04458), point1=(3.22889, 7.79523))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     5.39169, 5.39169), point1=(5.96621, 5.96621))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     7.04458, 2.91796), point1=(7.79523, 3.22889))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     7.625, 0.0), point1=(8.4375, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     7.04458, -2.91796), point1=(7.79523, -3.22889))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     5.39169, -5.39169), point1=(5.96621, -5.96621))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     2.91796, -7.04458), point1=(3.22889, -7.79523))
# mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#     0.0, -7.625), point1=(0.0, -8.4375))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 8.25), point2=(
#     0.0, 8.4375))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 8.428125))
# mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
#     False, entity=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
#     8.428125), ))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.625, 7.625))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 8.428125))
# mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.625, 
#     7.625), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
#     8.428125), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(3.15714, 7.62201), 
#     point2=(3.22889, 7.79523))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(5.83363, 5.83363), 
#     point2=(5.96621, 5.96621))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.675433, 
#     5.948567))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.959581, 
#     5.959581))
# mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.675433, 
#     5.948567), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.959581, 
#     5.959581), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(7.62201, 3.15714), 
#     point2=(7.79523, 3.22889))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(8.4375, 0.0), 
#     point2=(6.8125, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.35625, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
#     addUndoState=False, entity=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.35625, 
#     0.0), ))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.397733, 
#     0.251076))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.35625, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.397733, 
#     0.251076), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.35625, 
#     0.0), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((6.8125, 0.0))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.397733, 
#     0.251076))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((6.8125, 
#     0.0), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.397733, 
#     0.251076), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(6.29392976977397, 
#     -2.60703055554768), point2=(7.79523, -3.22889))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((6.29393, 
#     -2.607031))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.52229, 
#     -1.45898))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     6.29392976977397, -2.60703055554768), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.52229, 
#     -1.45898), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(5.96621, -5.96621), 
#     point2=(4.81716999970376, -4.81716999970376))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((6.115627, 
#     -5.760555))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.874622, 
#     -4.874622))
# mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((6.115627, 
#     -5.760555), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.874622, 
#     -4.874622), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((4.81717, 
#     -4.81717))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.695845, 
#     -2.695845))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     4.81716999970376, -4.81716999970376), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.695845, 
#     -2.695845), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(3.22889, -7.79523), 
#     point2=(2.60703055554768, -6.29392976977397))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((2.607031, 
#     -6.29393))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.45898, 
#     -3.52229))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     2.60703055554768, -6.29392976977397), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.45898, 
#     -3.52229), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, -8.4375), 
#     point2=(0.0, -6.8125))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -8.19375))
# mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
#     False, entity=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
#     -8.19375), ))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.251076, 
#     -8.397733))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -8.19375))
# mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.251076, 
#     -8.397733), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
#     -8.19375), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, -6.8125))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -6.70315))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 
#     -6.8125), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
#     -6.70315), ))
# mdb.models['Model-1'].sketches['__profile__'].ArcByCenterEnds(center=(0.0, 0.0)
#     , direction=COUNTERCLOCKWISE, point1=(-0.811345991643665, 
#     -7.58171106557377), point2=(0.811345991643665, -7.58171106557377))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-0.811346, 
#     -7.581711))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     -0.811345991643665, -7.58171106557377), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.811346, 
#     -7.581711))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     0.811345991643665, -7.58171106557377), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.795179, 
#     -7.583424))
# mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.795179, 
#     -7.583424), ), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.811345991643665, 
#     -7.58171106557377), point2=(0.624474886902973, -7.59938524590164))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.811346, 
#     -7.581711))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     0.811345991643665, -7.58171106557377), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.624475, 
#     -7.599385))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.625, -7.625))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     0.624474886902973, -7.59938524590164), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.625, 
#     -7.625), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(2.15181064388163, 
#     -7.31507593623455), point2=(2.33121298596386, -7.25989469717526))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((2.151811, 
#     -7.315076))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     2.15181064388163, -7.31507593623455), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((2.331213, 
#     -7.259895))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.323869, 
#     -7.519838))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     2.33121298596386, -7.25989469717526), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.323869, 
#     -7.519838), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(3.6509789649322, 
#     -6.69410020821489), point2=(3.48510331166548, -6.78193776932657))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((3.650979, 
#     -6.6941))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     3.6509789649322, -6.69410020821489), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((3.485103, 
#     -6.781938))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.323869, 
#     -7.519838))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     3.48510331166548, -6.78193776932657), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.323869, 
#     -7.519838), ))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ), radius=7.625, textPoint=(-5.61193752288818, 
#     -8.0294132232666))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.811346, 
#     -7.581711))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     0.811345991643665, -7.58171106557377), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.624475, 
#     -7.599385))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     0.624474886902973, -7.59938524590164), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.624475, 
#     -7.599385))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.625, -7.625))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     0.624474886902973, -7.59938524590164), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.625, 
#     -7.625), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.811346, 
#     -7.581711))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.251076, 
#     -8.397733))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     0.811345991643665, -7.58171106557377), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.251076, 
#     -8.397733), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((3.650979, 
#     -6.6941))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     3.6509789649322, -6.69410020821489), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(4.78737579694071, 
#     -5.93478373480166), point2=(4.93200832445649, -5.81514564628366))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((4.787376, 
#     -5.934784))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     4.78737579694071, -5.93478373480166), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((4.932008, 
#     -5.815146))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.948567, 
#     -5.675433))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     4.93200832445649, -5.81514564628366), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.948567, 
#     -5.675433), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(5.81514564628366, 
#     -4.93200832445649), point2=(5.93478373480166, -4.78737579694071))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((5.815146, 
#     -4.932008))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.948567, 
#     -5.675433))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     5.81514564628366, -4.93200832445649), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.948567, 
#     -5.675433), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((5.934784, 
#     -4.787376))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     5.93478373480166, -4.78737579694071), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(6.69410020821489, 
#     -3.6509789649322), point2=(6.78193776932657, -3.48510331166548))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((6.6941, 
#     -3.650979))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     6.69410020821489, -3.6509789649322), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((6.781938, 
#     -3.485103))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.667659, 
#     -2.966998))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     6.78193776932657, -3.48510331166548), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.667659, 
#     -2.966998), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(7.25989469717526, 
#     -2.33121298596386), point2=(7.31507593623455, -2.15181064388163))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((7.259895, 
#     -2.331213))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.667659, 
#     -2.966998))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     7.25989469717526, -2.33121298596386), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.667659, 
#     -2.966998), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((7.315076, 
#     -2.151811))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     7.31507593623455, -2.15181064388163), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(7.58171106557377, 
#     -0.811345991643665), point2=(7.59938524590164, -0.624474886902973))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((7.581711, 
#     -0.811346))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     7.58171106557377, -0.811345991643665), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((7.599385, 
#     -0.624475))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.21941, 
#     0.193136))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     7.59938524590164, -0.624474886902973), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.21941, 
#     0.193136), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(7.59938524590164, 
#     0.624474886902973), point2=(7.58171106557377, 0.811345991643665))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((7.599385, 
#     0.624475))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.21941, 
#     0.193136))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     7.59938524590164, 0.624474886902973), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.21941, 
#     0.193136), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((7.581711, 
#     0.811346))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     7.58171106557377, 0.811345991643665), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(7.31507593623455, 
#     2.15181064388163), point2=(7.25989469717526, 2.33121298596386))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((7.315076, 
#     2.151811))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     7.31507593623455, 2.15181064388163), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((7.259895, 
#     2.331213))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.519838, 
#     3.323869))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     7.25989469717526, 2.33121298596386), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.519838, 
#     3.323869), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(6.78193776932657, 
#     3.48510331166548), point2=(6.69410020821489, 3.6509789649322))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((6.781938, 
#     3.485103))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.519838, 
#     3.323869))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     6.78193776932657, 3.48510331166548), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.519838, 
#     3.323869), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((6.6941, 
#     3.650979))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     6.69410020821489, 3.6509789649322), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(5.93478373480166, 
#     4.78737579694071), point2=(5.81514564628366, 4.93200832445649))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((5.934784, 
#     4.787376))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     5.93478373480166, 4.78737579694071), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((5.815146, 
#     4.932008))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.675433, 
#     5.948567))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     5.81514564628366, 4.93200832445649), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.675433, 
#     5.948567), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(4.78737579694071, 
#     5.93478373480166), point2=(4.93200832445649, 5.81514564628366))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((4.787376, 
#     5.934784))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     4.78737579694071, 5.93478373480166), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((4.932008, 
#     5.815146))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.675433, 
#     5.948567))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     4.93200832445649, 5.81514564628366), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.675433, 
#     5.948567), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(2.15308370808317, 
#     7.31470132992365), point2=(2.33247161292238, 7.25949042115982))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((2.153084, 
#     7.314701))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     2.15308370808317, 7.31470132992365), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((2.332472, 
#     7.25949))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.68078, 
#     6.46715))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     2.33247161292238, 7.25949042115982), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.68078, 
#     6.46715), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(3.48557088423287, 
#     6.78169747268249), point2=(3.65143602662886, 6.69385090537852))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((3.485571, 
#     6.781697))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.68078, 
#     6.46715))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     3.48557088423287, 6.78169747268249), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((2.68078, 
#     6.46715), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((3.651436, 
#     6.693851))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     3.65143602662886, 6.69385090537852), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.624474886902973, 
#     7.59938524590164), point2=(0.811345991643665, 7.58171106557377))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.624475, 
#     7.599385))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.625, 7.625))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     0.624474886902973, 7.59938524590164), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.625, 
#     7.625), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.811346, 
#     7.581711))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
#     0.811345991643665, 7.58171106557377), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-2.356255, 
#     7.251806), ))
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 7.0), point2=(
#     0.0, 6.8125))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 6.821875))
# mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
#     False, entity=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
#     6.821875), ))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.625, 7.625))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 6.821875))
# mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.625, 
#     7.625), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
#     6.821875), ))
# mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 6.8125))
# mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 6.70315))
# mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
#     addUndoState=False, entity1=
#     mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((0.0, 
#     6.8125), ), entity2=
#     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
#     6.70315), ))
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].PartitionFaceBySketch(
#     faces=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].faces.findAt(((
#     1.874995, -8.416416, 0.010222), )), sketch=
#     mdb.models['Model-1'].sketches['__profile__'], sketchUpEdge=
#     mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].edges.findAt((
#     1.874995, 6.851575, 0.0), ))
# del mdb.models['Model-1'].sketches['__profile__']
# mdb.models['Model-1'].ConstrainedSketch(gridSpacing=1.0, name='__profile__', 
#     sheetSize=40.17, transform=
#     mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].MakeSketchTransform(
#     sketchPlane=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].faces.findAt(
#     (1.27083, 6.8021, 0.0), ), sketchPlaneSide=SIDE1, 
#     sketchUpEdge=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].edges.findAt(
#     (0.0625, 6.53125, 0.0), ), sketchOrientation=RIGHT, origin=(0.0, 0.0, 
#     0.0)))
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].projectReferencesOntoSketch(
#     filter=COPLANAR_EDGES, sketch=
#     mdb.models['Model-1'].sketches['__profile__'])
# mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.87499534342368, 
#     -6.4063), point2=(0.0625, -6.375))
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].PartitionFaceBySketch(
#     faces=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].faces.findAt(((
#     1.27083, 6.8021, 0.0), )), sketch=
#     mdb.models['Model-1'].sketches['__profile__'], sketchUpEdge=
#     mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].edges.findAt((0.0625, 
#     6.53125, 0.0), ))
# del mdb.models['Model-1'].sketches['__profile__']
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].PartitionCellBySweepEdge(
#     cells=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].cells.findAt(((
#     1.270857, 6.394415, 0.0), )), edges=(
#     mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].edges.findAt((
#     1.421872, 6.398475, 0.0), ), ), sweepPath=
#     mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].edges.findAt((0.0625, 
#     4.507806, 4.507806), ))
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].PartitionCellByDatumPlane(
#     cells=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].cells.findAt(((
#     0.666665, 7.000084, 0.010225), ), ((1.270857, 6.394415, 0.0), ), ((
#     0.041667, -6.357241, 0.475514), ), ), datumPlane=
#     mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].datums[4])
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].Mirror(keepOriginal=ON, 
#     mirrorPlane=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].datums[2])
# mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].DatumPlaneByPrincipalPlane(
#     offset=4.029, principalPlane=YZPLANE)
# #  End of script
