import makeAssembly as Assembly
import createBolt as Bolt
import createGasket as Gasket
import FlangeWithThickComplexHub as Flange
import csv_reader as Mapper
import assignMaterials as Materials


def mainScript(flangeClass, flangeSize, pipeSchedule, gasketThickness, flangeFileName, gasketFileName, boltFileName):

	dimensions = Mapper.mapper(flangeClass, flangeSize)
	print(dimensions)
	print('a')
	Flange.flange(dimensions.get("flangeDimensions"), pipeSchedule)
	Bolt.makeBolt(dimensions, gasketThickness)
	Gasket.makeGasket(dimensions.get("gasketDimensions"), gasketThickness)
	Assembly.assembly(gasketThickness, dimensions.get("flangeDimensions"))
	Materials.materials(flangeFileName, gasketFileName, boltFileName)