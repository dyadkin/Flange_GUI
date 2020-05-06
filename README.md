## Flange Assembly GUI User Guide

### About
Senior Design Project (Spring 2020) with the goal of creating an Abaqus GUI plugin for a RFWN flange assmebly model.

### Installation
Once a distribution of Abaqus CAE is installed on your machine, simply pull this respository and copy over the *FlangeMainGUI* folder into your *abaqus_plugins* directory. The plugin should appear in the *Plug-ins* drop down menu in Abaqus with the name *Flange Main GUI*. <br> <br>
A restart of the Abaqus kernel may be needed if the plugin does not show up immediately after install.

### Using the Plugin
**_Assembly Parameters_** 
<br>
Includes user selected flange class and NPS and user specified pipe schedule and gasket thickness. <br>
The user is expected to provide reasonable pipe schedules, i.e if a pipe schedule exceeds the pipe outer diameter the geometry will fail.

**_Materials_**
<br>
The Plugin takes in optional material loading scripts for each part in the assemby (flange, gasket, bolt). The material scripts must be python files. In each material script the user can define any material properties desired. At the end of the script ensure the following line is included:

```python
mdb.models['Model-1'].HomogeneousSolidSection(name='<section name>', material='<material name>', thickness=None)
```
Note, \<section name\> must correspond to one of the following: <br>
  - **Flange-Section** for flange materials
  - **Gasket-Section** for gasket materials
  - **Bolt-Section** for bolt materials <br>
  
and \<material name\> must correspond to name of the material specified at the beginning of the material script.<br>
Material assignment is not required for assembly creation, so the material fields can be left blank.<br>

Sample material scripts are available in the github repository.

**_Squared Off Hub Geometry_**
<br>
The hub defualts to being squared off at the end. If the user desires to create a model with a complex hub the _squareOffHub_ flag in _flange.py_ needs to be set to **False**.

```python
squareOffHub = True
```



