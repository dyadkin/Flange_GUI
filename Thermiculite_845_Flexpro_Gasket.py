#  Thermiculite_845_Flexpro_Gasket
#
#  22 April 2020   JCH
#  Flexitallic Thermiculite 845 Flexpro gasket, .156 inch thick
#  Data taken from ROTT report 10 Feb 2002
#  ROTT report obtained from Brian Hasha at Flexitallic
#
from part import *
from material import *
from section import *
from sketch import *
#
#	Get active model name for use later
#
ThisModels = mdb.models
items = list(ThisModels.keys())
thisName = items[0]
#
mdb.models[thisName].Material(description=
    'Flexitallic Thermiculite 845 Flexpro gasket (.156 inch thick).  Data from ROTT test 10 Feb 2002 obtained from Brian Hasha at Flexitallic.   '
    , name='Thermiculite_845_Gasket')
mdb.models[thisName].materials['Thermiculite_845_Gasket'].GasketThicknessBehavior(
    table=((0.0, 0.0), (1118.0, 0.0179), (2835.0, 0.0213), (4324.0, 0.0232), (
    7203.0, 0.024), (10071.0, 0.0246), (12934.0, 0.025), (17234.0, 0.0255), (
    20124.0, 0.0258), (23012.0, 0.026)), type=DAMAGE, unloadingTable=((0.0, 
    0.0, 0.0237), (1100.0, 0.0233, 0.0237), (5777.0, 0.0237, 0.0237), (0.0, 
    0.0, 0.0243), (1118.0, 0.0239, 0.0243), (8633.0, 0.0243, 0.0243), (0.0, 
    0.0, 0.0248), (1102.0, 0.0244, 0.0248), (11535.0, 0.0248, 0.0248), (0.0, 
    0.0, 0.0252), (1149.0, 0.0246, 0.0252), (15125.0, 0.0252, 0.0252), (0.0, 
    0.0, 0.026), (1124.0, 0.0253, 0.026), (23012.0, 0.026, 0.026)))
mdb.models[thisName].materials['Thermiculite_845_Gasket'].GasketTransverseShearElastic(
    table=((1770000.0, ), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Gasket-Section', 
            material='Thermiculite_845_Gasket', thickness=None)
#
print "Completed Thermiculite_845_Flexpro_Gasket properties"
#