#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.75.01), Tue Mar 12 12:16:55 2013
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui, sound
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'None'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/rowanaahmed/Desktop/TimingTask/timingtask.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='In this experiment, you will hear two tones.\n\nBefore the first tone you will see a fixation cross to warn you that the first tone is about to play.\n\nYour task is to compare the duration of time the tones each played and determine which tone was played for the shortest amount of time.\n\nIf you believe the first tone was shorter, press 1.  If you believe the second tone was shorter, press 2.\n\nPress the spacebar when you are ready to begin.\n',
    font='Arial',
    pos=[0, 0], height=0.09, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(win=win, name='image',
    image=u'media/cross.png', mask=None,
    ori=0, pos=[0, 0], size=[2,2],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
sound_1 = sound.Sound('A', secs=2.3)
sound_1.setVolume(1)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine"instruction"-------
t = 0
instructionClock.reset()  # clock 
frameN = -1
routineTimer.add(15.000000)
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instructionComponents = []
instructionComponents.append(text)
instructionComponents.append(key_resp_2)
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instruction"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    elif text.status == STARTED and t >= (0.0 + 15):
        text.setAutoDraw(False)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents()
    elif key_resp_2.status == STARTED and t >= (0.0 + 15):
        key_resp_2.status = STOPPED
    if key_resp_2.status == STARTED:  # only update if being drawn
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # abort routine on response
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath='/Users/rowanaahmed/Desktop/TimingTask/timingtask.psyexp',
    trialList=data.importConditions(u'condition.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine"trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(5.300000)
    # update component parameters for each repeat
    key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp.status = NOT_STARTED
    sound_1.setSound(stim)
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(image)
    trialComponents.append(key_resp)
    trialComponents.append(sound_1)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.0 + .4):
            image.setAutoDraw(False)
        
        # *key_resp* updates
        if t >= 1.8 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp.tStart = t  # underestimates by a little under one frame
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            event.clearEvents()
        elif key_resp.status == STARTED and t >= (1.8 + 3.5):
            key_resp.status = STOPPED
        if key_resp.status == STARTED:  # only update if being drawn
            theseKeys = event.getKeys(keyList=['1', '2'])
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp.keys = theseKeys[-1]  # just the last key pressed
                key_resp.rt = key_resp.clock.getTime()
                # was this 'correct'?
                if (key_resp.keys == str(correct)): key_resp.corr = 1
                else: key_resp.corr=0
                # abort routine on response
                continueRoutine = False
        # start/stop sound_1
        if t >= 0.0 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        elif sound_1.status == STARTED and t >= (0.0 + 2.3):
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(key_resp.keys) == 0:  # No response was made
       key_resp.keys=None
       # was no response the correct answer?!
       if str(correct).lower() == 'none': key_resp.corr = 1  # correct non-response
       else: key_resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# Shutting down:
win.close()
core.quit()
