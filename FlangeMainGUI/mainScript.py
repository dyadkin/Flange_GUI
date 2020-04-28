import makeAssembly as Assembly
import createBolt as Bolt
import createGasket as Gasket
import FlangeWithThickComplexHub as Flange
import csv_reader as Mapper

def mainScript(flangeClass, flangeSize, pipeSchedule, gasketThickness):

	dimensions = Mapper.mapper(flangeClass, flangeSize)
	Flange.flange(dimensions.get("flangeDimensions"), pipeSchedule)
	Bolt.makeBolt(dimensions, gasketThickness)
	Gasket.makeGasket(dimensions.get("gasketDimensions"), gasketThickness)
	Assembly.assembly(gasketThickness, dimensions.get("flangeDimensions"))