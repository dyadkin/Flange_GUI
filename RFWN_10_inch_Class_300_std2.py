# -*- coding: mbcs -*-
#  RFWN 10 inch Class 300 std pipe schedule
#
from part import *
from material import *
from section import *
from sketch import *
from visualization import *
from connectorBehavior import *
RF_OD = 12.75
FO_D = 17.5
BC_D = 15.25
No_BH = 16
B_D = 1
F_T = 1.81
H_D = 12.62
PO_D = 10.75
L_TH = 4.56
H_L = 2.75

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
    0.0, RF_OD/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, H_D/2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    H_D/2), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, RF_OD/2), point2=
    (0.0625, RF_OD/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.03125, RF_OD/2))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.03125, 
    RF_OD/2), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, H_D/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.03125, RF_OD/2))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    H_D/2), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.03125, 
    RF_OD/2), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0625, RF_OD/2), 
    point2=(0.0625, FO_D/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0625, 7.5625))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0625, 
    7.5625), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.03125, RF_OD/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0625, 7.5625))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.03125, 
    RF_OD/2), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0625, 
    7.5625), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0625, FO_D/2), 
    point2=(1.8725, FO_D/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((F_T/2, FO_D/2))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((F_T/2, 
    FO_D/2), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0625, 7.5625))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((F_T/2, FO_D/2))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0625, 
    7.5625), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((F_T/2, 
    FO_D/2), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.8725, FO_D/2), 
    point2=(1.8725, 6.4063))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.8725, 
    7.57815))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.8725, 
    7.57815), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((F_T/2, FO_D/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.8725, 
    7.57815))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((F_T/2, 
    FO_D/2), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.8725, 
    7.57815), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.94726, 6.2962), 
    point2=(4.029, PO_D/2))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(4.029, PO_D/2), 
    point2=(L_TH, PO_D/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.2945, PO_D/2))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.2945, 
    PO_D/2), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(L_TH, PO_D/2), 
    point2=(L_TH, 5.01))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((L_TH, 5.1925))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((L_TH, 
    5.1925), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.2945, PO_D/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((L_TH, 5.1925))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((4.2945, 
    PO_D/2), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((L_TH, 
    5.1925), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(L_TH, 5.01), point2=
    (0.0, 5.01))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((L_TH/2, 5.01))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((L_TH/2, 5.01), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((L_TH, 5.1925))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((L_TH/2, 5.01))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((L_TH, 
    5.1925), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((L_TH/2, 5.01), 
    ))
mdb.models['Model-1'].sketches['__profile__'].ArcByCenterEnds(center=(1.995, 
    6.4063), direction=CLOCKWISE, point1=(1.94726, 6.2962), point2=(1.8725, 
    6.4063))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((1.874995, 
    6.4063))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.8725, 
    7.57815))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    1.87499534342368, 6.4063), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.8725, 
    7.57815), ))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    constructionGeometry=ON)
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].assignCenterline(line=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.5, 0.0), 
    ))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='RFWN_10_in_CL_300_std'
    , type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].BaseSolidRevolve(angle=
    180.0, flipRevolveDirection=OFF, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].setValues(
    geometryRefinement=EXTRA_FINE)
mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].DatumPlaneByPrincipalPlane(
    offset=0.0, principalPlane=XYPLANE)
mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].DatumPlaneByPrincipalPlane(
    offset=0.0, principalPlane=YZPLANE)
mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].DatumPlaneByPrincipalPlane(
    offset=0.0, principalPlane=XZPLANE)
mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].PartitionCellByExtendFace(
    cells=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].cells.findAt(((
    0.041667, -6.357241, 0.475514), )), extendFace=
    mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].faces.findAt((0.0625, 
    -7.908672, 0.535936), ))
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.97, name='__profile__', 
    sheetSize=39.13, transform=
    mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].faces.findAt(
    (0.0625, -7.164107, 0.104269), ), sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].edges.findAt(
    (0.0625, 6.96875, 0.0), ), sketchOrientation=RIGHT, origin=(0.0625, 0.0, 
    0.0)))
mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].ConstructionCircleByCenterPerimeter(
    center=(0.0, 0.0), point1=(0.0, BC_D/2))
mdb.models['Model-1'].sketches['__profile__'].ConstructionCircleByCenterPerimeter(
    center=(0.0, BC_D/2), point1=(0.0, 8.25))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, BC_D/2), point1=(0.0, 8.25))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    2.91796, 7.04458), point1=(3.15714, 7.62201))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    5.39169, 5.39169), point1=(5.83363, 5.83363))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    7.04458, 2.91796), point1=(7.62201, 3.15714))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    BC_D/2, 0.0), point1=(8.25, 0.0))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    7.04458, -2.91796), point1=(7.62201, -3.15714))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    5.39169, -5.39169), point1=(5.83363, -5.83363))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    2.91896, -7.04458), point1=(3.15714, -7.62201))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, -BC_D/2), point1=(0.0, -8.25))
mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].CutExtrude(
    flipExtrudeDirection=OFF, sketch=
    mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, 
    sketchPlane=
    mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].faces.findAt((0.0625, 
    -7.164107, 0.104269), ), sketchPlaneSide=SIDE1, sketchUpEdge=
    mdb.models['Model-1'].parts['RFWN_10_in_CL_300_std'].edges.findAt((0.0625, 
    6.96875, 0.0), ))
del mdb.models['Model-1'].sketches['__profile__']