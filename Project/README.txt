####################################################################################################
####################################################################################################

                                       COMPUTER SIMULATION PROJECT 
                                                 "SOLAR"
                                                APRIL 2019
                                          YEAR 2 SEMESTER 2 2019  
                                           
                                           BENJAMIN CARPENTER
                                                S1731178

####################################################################################################
####################################################################################################

This project folder is broken into 4 sections:

Main running of files that show tasks being completed are in Testing and Experimentation

#####################################      SOURCE FILES (SRC)      #################################

--->SRC providing a class which implements the main required features and can be used by other code 
    to produce a valid outputs of body path traces, body data and animated paths alongside many 
    other smaller features.
    
    This main implementation was made up of three classes:
    --->A space object would contain within it many Body objects which would each represent a 
        planet or other type of body (such as a probe). 
    --->An AnimateSpace class could then be used to either animate this space before or 
        after data for it had been processed.
    
    Two other minor classes were included in the program however these provide minimal 
    functionality: 
    --->Probe adds some features that would be expected only of a manmade object and would not 
        be appropriate to place within the more general Body class and hence is a child of this 
        class to allow it to develop on these general features (i.e. for experiment 3 
        [Solar 1.4.3] the probe should not launch until 2 years have passed this is something 
        that is specific to a probe and could be implemented here). 
        
    --->Path acts as a data storage structure to standardise and hide the storage of data about
        a bodies path as it travels through space and is used by animate space to display a
        bodies path.


    --->The source of planet files is also stored here, all planet data is adapted from:
            https://nssdc.gsfc.nasa.gov/planetary/factsheet/

    --->Running is a simple class used to show that a terminal is running the simulation 


#######################################     TESTING     ############################################

--->Testing provides scripts that perform basic functionality in order to quickly determine if the 
    program works as expected and were important in development and improvment e.g. during 
    refactoring. As well as displaying tha basic functionality was achived by the class

    --->EarthMoon acted as a method for testing that an animation would be displayed to the screen
        immediately after generation of a data set containing a planets data was produced
        Also verified that reading from file worked correctly 
        
        It will show to the screen an animation of the Moon orbiting the Earth for a simulated 
        period of 1 month.

    --->innerPlanets is a script that will generate and then save an animation of the motion of the 
        inner planets over a period of a year. Outputting this animation to the OUTPUT folder.

        This has the effect of allowing testing of the orbital ratios as well as the programs 
        saving an animation output

    --->OrbitalPeriodTest is used to test that the year determination is correct, it is currently 
        set to determine an Earth year and will output to terminal the produced value in seconds


    --->LaunchTest provides an ability to see the position on the surface that a body is placed 
        using Mars as a launch surface, allowing the various parameters to be changed to see the 
        effect it has whilst no object are initially moving so the positions can be easily and 
        quickly seen.


    --->MarsPhobos is used to determine whether 'on the fly' animation is working correctly. Its 
        output is that expected for Checkpoint 5 of the Computer simulation course.


    --->All scripts in this directory can be run by the following process
            1.  Change directory to the Experimentation folder 
                $ cd Experimentation
            2.  Running the script
                $ ./<ScriptName>.py


####################################       EXPERIMENTATION      ####################################

--->Experimentation providing scripts that are used to produce numeric (and visual) data which can 
    be interpret and compared to 'real life' data to test how well this simulation simulates.
         
    --->MarsProbeExperiment is a script that can be called to determine the closest position to Mars
        that a probe gets for a range of experimental parameters most (notably the launch parameters
        of the probe) that are specified at the top of the file. 

        Each determined value will be output in csv format to a file specified at the top of the
        script. These are in the format Latitude,initial X velocity, initial Y velocity, Closest 
        distance to Mars 
        
        NOTE: Experimental paramters must be changed in file. 
                   
    --->DeterminedBodiesOrbitalPeriod is a script that will determine the orbital periods of the 
        various bodies in a file (setup for the inner planets hence the correction to ignore the 
        non-orbiting sun) and output them to a file again where any parameters are defined at the 
        top of the script page due to the large number.

        The output data will be in csv format PlanetName, orbitalPeriod
    
    --->ConstantTotalEnergy is a script that shows the conservation of energy throughout a 
        simulation (currently setup of the innerPlanets of the solar system).
        
        It outputs a graph to the screen showing the various energies involved in the system.

    --->All the above scripts in this directory can be run by the following process
            1.  Change directory to the Experimentation folder 
                $ cd Experimentation
            2.  Running the script
                $ ./<ScriptName>.py


    --->probeAnimator was a script that was used to produce a visual representation of a path that 
        had been based on launch parameters of a probe. 
        
        It was run by the following process:
            1.  Change directory to the Experimentation folder
                $ cd Experimentation
            2.  Run the script giving the following parameters:
                    
                    Latitude InitialXVelocity InitialYVelocity TimePeriod EnergyOutput
                
                    $ ./probeAnimator.py -50 10030 2525 5000 ../OUTPUT/EnergyOutput.txt




#########################################       OUTPUT      ########################################

--->OUTPUT acts a space where all produced data is placed, this includes many data sets and 
    animations.

    --->PATHS DATA contains within it the data produced through the MarsProbeExperiment script 
        Much of the data produced by is invalid or old due to this folder being used throught 
        development and acceleration, for example there are many path testing files that were 
        generatingthe furthest distance rather than closest due to having a '<' the wrong way around
    
    --->ANIMATION contains many visulisations that were generated throughout development and 
        experimentation. 
        --->Paths contains 'Promising' probe paths where the file names are 
            latitude, initial x velocity, initial y velocity and time interval used to sim

    --->CONST ENERGY contains files related to the determination of the programs ability to simulate
    conservation of energy

    --->ANALYSIS provides a space to place data that has been interpret from an output
    








    
