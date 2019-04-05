#!/bin/bash

echo "Shows basic program working in an accelerated setup for testing"

echo "Testing Files"
cd Testing
echo "Running Inner planets"
./innerPlanets.py
echo "Running Orbital period test"
./OrbitalPeriodTest.py

echo "Experimentation files"
cd ../Experimentation
echo "Running Mars Probe Experiment"
./MarsProbeExperiment.py
echo "Running Constant Total Energy Experiment"
./ConstantTotalEnergy.py
echo "Running Determine Bodies Orbital Period Experiment"
./DetermineBodiesOrbitalPeriod.py
echo "Running Probe animator"
./probeAnimator.py -50 10030 2525 10000 /dev/null

