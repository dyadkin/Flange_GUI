import imp

Flange = imp.load_source('FlangeWithThickComplexHub', "C:\\Users\\jcoll\\abaqus_plugins\\FlangeMainGUI\\FlangeWithThickComplexHub.py")
Mapper = imp.load_source('FlangeWithThickComplexHub', "C:\\Users\\jcoll\\abaqus_plugins\\FlangeMainGUI\\csv_reader.py")
# from FlangeWithThickComplexHub import flange
# from csv_reader import mapper
def mainScript(flangeClass, flangeSize, pipeSchedule):

	dimensions = Mapper.mapper(flangeClass, flangeSize)
	Flange.flange(dimensions, pipeSchedule)