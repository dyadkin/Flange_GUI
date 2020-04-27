# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def assembly(gasketThickness, dimensions):

    boltCircleD = dimensions[3]
    boltHoles = dimensions[4]

    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Gasket']
    a1.Instance(name='Gasket-1', part=p, dependent=ON)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Gasket-1', ), vector=(-gasketThickness/2, 0.0, 0.0))
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['RFWN']
    a1.Instance(name='RFWN-1', part=p, dependent=ON)
    p1 = a1.instances['RFWN-1']
    # p1.translate(vector=(1.1282, 0.0, 0.0))
    # session.viewports['Viewport: 1'].view.fitView()
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=20.7195, 
    #     farPlane=41.4778, width=24.2567, height=10.8346, cameraPosition=(
    #     -6.30775, 8.84385, 31.564), cameraUpVector=(-0.349953, 0.647561, 
    #     -0.676903), cameraTarget=(2.66779, -0.0204859, 3.1218))
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=19.9293, 
    #     farPlane=42.2789, width=23.3316, height=10.4214, cameraPosition=(
    #     11.0323, 16.5814, 28.0681), cameraUpVector=(-0.220329, 0.618973, 
    #     -0.753875), cameraTarget=(2.6591, -0.0243648, 3.12355))
    a1 = mdb.models['Model-1'].rootAssembly
    f1 = a1.instances['RFWN-1'].faces
    f2 = a1.instances['Gasket-1'].faces
    a1.FaceToFace(movablePlane=f1[boltHoles/2 + 1 + 4], fixedPlane=f2[2], flip=ON, clearance=0.0)
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['RFWN']
    a1.Instance(name='RFWN-2', part=p, dependent=ON)
    p1 = a1.instances['RFWN-2']
    # p1.translate(vector=(5.8692, 0.0, 0.0))
    # session.viewports['Viewport: 1'].view.fitView()
    a1 = mdb.models['Model-1'].rootAssembly
    a1.rotate(instanceList=('RFWN-2', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(
        0.0, 0.0, 10.0), angle=180.0)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=20.9144, 
    #     farPlane=50.9078, width=19.7635, height=8.82769, cameraPosition=(
    #     -13.2653, 24.5853, 27.7695), cameraUpVector=(-0.247364, 0.255176, 
    #     -0.934717), cameraTarget=(3.26892, 0.104513, 2.95155))
    a1 = mdb.models['Model-1'].rootAssembly
    f1 = a1.instances['RFWN-2'].faces
    f2 = a1.instances['Gasket-1'].faces
    a1.FaceToFace(movablePlane=f1[boltHoles/2 + 1 + 4], fixedPlane=f2[0], flip=ON, clearance=0.0)
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['Bolt']
    a1.Instance(name='Bolt-1', part=p, dependent=ON)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=27.8285, 
    #     farPlane=48.8253, width=27.3489, height=12.2158, cameraPosition=(
    #     -38.3082, 0.791403, 3.9071), cameraUpVector=(0.29536, 0.251276, 
    #     -0.92175), cameraTarget=(-0.139735, 0.450655, 2.22787))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Bolt-1', ), vector=(0.0, boltCircleD/2, 0.0))
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=25.6708, 
    #     farPlane=60.0821, width=25.2284, height=11.2687, cameraPosition=(
    #     -31.7575, -8.4503, -19.1644), cameraUpVector=(0.615524, 0.512374, 
    #     -0.598834), cameraTarget=(0.621554, -0.623375, -0.453397))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.RadialInstancePattern(instanceList=('Bolt-1', ), point=(0.0, 0.0, 0.0), 
        axis=(1.0, 0.0, 0.0), number=boltHoles/2 + 1, totalAngle=180.0)


