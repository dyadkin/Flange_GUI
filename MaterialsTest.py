# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def LoadMaterials(flangeFile, gasketFile, boltFile):
    if flangeFile
        execfile(flangeFile, __main__.__dict__)
        p = mdb.models['Model-1'].parts['RFWN']
        c = p.cells
        cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
        region = p.Set(cells=cells, name='Set-1')
        p = mdb.models['Model-1'].parts['RFWN']
        p.SectionAssignment(region=region, sectionName='Flange-Section', offset=0.0, 
            offsetType=MIDDLE_SURFACE, offsetField='', 
            thicknessAssignment=FROM_SECTION)

    if gasketFile
        execfile(gasketFile, __main__.__dict__)
        p = mdb.models['Model-1'].parts['Gasket']
        c = p.cells
        cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
        region = p.Set(cells=cells, name='Set-1')
        p = mdb.models['Model-1'].parts['Gasket']
        p.SectionAssignment(region=region, sectionName='Gasket-Section', offset=0.0, 
            offsetType=MIDDLE_SURFACE, offsetField='', 
            thicknessAssignment=FROM_SECTION)

    if boltFile
        execfile(gasketFile, __main__.__dict__)
        p = mdb.models['Model-1'].parts['Bolt']
        c = p.cells
        cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
        region = p.Set(cells=cells, name='Set-1')
        p = mdb.models['Model-1'].parts['Bolt']
        p.SectionAssignment(region=region, sectionName='Bolt-Section', offset=0.0, 
            offsetType=MIDDLE_SURFACE, offsetField='', 
            thicknessAssignment=FROM_SECTION)