import os
import imp

# cwd = os.getcwd()
# print(cwd)

HOME = os.environ.get("HOMEDRIVE")
USER = os.environ.get("USERNAME")

Flange = imp.load_source('FlangeWithThickComplexHub', HOME+"\\Users\\"+USER+"\\abaqus_plugins\\FlangeMainGUI\\FlangeWithThickComplexHub.py")
Bolt = imp.load_source('createBolt', HOME+"\\Users\\"+USER+"\\abaqus_plugins\\FlangeMainGUI\\createBolt.py")
Gasket = imp.load_source('createGasket', HOME+"\\Users\\"+USER+"\\abaqus_plugins\\FlangeMainGUI\\createGasket.py")
Mapper = imp.load_source('csv_reader', HOME+"\\Users\\"+USER+"\\abaqus_plugins\\FlangeMainGUI\\csv_reader.py")
Assembly = imp.load_source('assembly', HOME+"\\Users\\"+USER+"\\abaqus_plugins\\FlangeMainGUI\\assembly.py")


# Flange = imp.load_source('FlangeWithThickComplexHub', "C:\\Users\\yakov\\abaqus_plugins\\FlangeMainGUI\\FlangeWithThickComplexHub.py")
# Mapper = imp.load_source('FlangeWithThickComplexHub', "C:\\Users\\yakov\\abaqus_plugins\\FlangeMainGUI\\csv_reader.py")

def mainScript(flangeClass, flangeSize, pipeSchedule, gasketThickness):

	dimensions = Mapper.mapper(flangeClass, flangeSize)
	Flange.flange(dimensions.get("flangeDimensions"), pipeSchedule)
	Bolt.makeBolt(dimensions, gasketThickness)
	Gasket.makeGasket(dimensions.get("gasketDimensions"), gasketThickness)
	Assembly.assembly(gasketThickness, dimensions.get("flangeDimensions"))