DLL.AioInit.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_short)]
DLL.AioExit.argtypes = [ctypes.c_short]
DLL.AioResetDevice.argtypes = [ctypes.c_short]
DLL.AioGetErrorString.argtypes = [ctypes.c_long, ctypes.POINTER(ctypes.c_char)]
DLL.AioQueryDeviceName.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char)]
DLL.AioGetDeviceType.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_short)]
DLL.AioSetControlFilter.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float]
DLL.AioGetControlFilter.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]
DLL.AioResetProcess.argtypes = [ctypes.c_short]
DLL.AioSingleAi.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioSingleAiEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]
DLL.AioMultiAi.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioMultiAiEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]
DLL.AioGetAiResolution.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiInputMethod.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAiInputMethod.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioGetAiMaxChannels.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiChannel.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]
DLL.AioGetAiChannel.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiChannels.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAiChannels.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiChannelSequence.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]
DLL.AioGetAiChannelSequence.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]
DLL.AioSetAiRangeAll.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAiRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiTransferMode.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAiTransferMode.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiDeviceBufferMode.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAiDeviceBufferMode.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiMemorySize.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioGetAiMemorySize.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAiTransferData.argtypes = [ctypes.c_short, ctypes.c_long, ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAiAttachedData.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioGetAiSamplingDataSize.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiMemoryType.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAiMemoryType.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiRepeatTimes.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioGetAiRepeatTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAiClockType.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAiClockType.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiSamplingClock.argtypes = [ctypes.c_short, ctypes.c_float]
DLL.AioGetAiSamplingClock.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_float)]
DLL.AioSetAiScanClock.argtypes = [ctypes.c_short, ctypes.c_float]
DLL.AioGetAiScanClock.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_float)]
DLL.AioSetAiClockEdge.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAiClockEdge.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiStartTrigger.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAiStartTrigger.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiStartLevel.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_short]
DLL.AioSetAiStartLevelEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float, ctypes.c_short]
DLL.AioGetAiStartLevel.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_short)]
DLL.AioGetAiStartLevelEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiStartInRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_long, ctypes.c_long]
DLL.AioSetAiStartInRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float, ctypes.c_float, ctypes.c_long]
DLL.AioGetAiStartInRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAiStartInRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAiStartOutRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_long, ctypes.c_long]
DLL.AioSetAiStartOutRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float, ctypes.c_float, ctypes.c_long]
DLL.AioGetAiStartOutRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAiStartOutRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAiStopTrigger.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAiStopTrigger.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiStopTimes.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioGetAiStopTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAiStopLevel.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_short]
DLL.AioSetAiStopLevelEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float, ctypes.c_short]
DLL.AioGetAiStopLevel.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_short)]
DLL.AioGetAiStopLevelEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAiStopInRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_long, ctypes.c_long]
DLL.AioSetAiStopInRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float, ctypes.c_float, ctypes.c_long]
DLL.AioGetAiStopInRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAiStopInRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAiStopOutRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_long, ctypes.c_long]
DLL.AioSetAiStopOutRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float, ctypes.c_float, ctypes.c_long]
DLL.AioGetAiStopOutRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAiStopOutRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAiStopDelayTimes.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioGetAiStopDelayTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAiEvent.argtypes = [ctypes.c_short, ctypes.c_int, ctypes.c_long]
DLL.AioGetAiEvent.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAiEventSamplingTimes.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioGetAiEventSamplingTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAiEventTransferTimes.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioGetAiEventTransferTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioStartAi.argtypes = [ctypes.c_short]
DLL.AioStartAiSync.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioStopAi.argtypes = [ctypes.c_short]
DLL.AioGetAiStatus.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAiSamplingCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAiStopTriggerCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAiTransferCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAiTransferLap.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAiStopTriggerTransferCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAiRepeatCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAiSamplingData.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAiSamplingDataEx.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_float)]
DLL.AioResetAiStatus.argtypes = [ctypes.c_short]
DLL.AioResetAiMemory.argtypes = [ctypes.c_short]
DLL.AioSingleAo.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long]
DLL.AioSingleAoEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float]
DLL.AioMultiAo.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioMultiAoEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]
DLL.AioGetAoResolution.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAoChannels.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAoChannels.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioGetAoMaxChannels.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAoRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]
DLL.AioSetAoRangeAll.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAoRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAoTransferMode.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAoTransferMode.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAoDeviceBufferMode.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAoDeviceBufferMode.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAoMemorySize.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioGetAoMemorySize.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAoTransferData.argtypes = [ctypes.c_short, ctypes.c_long, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAoSamplingDataSize.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAoMemoryType.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAoMemoryType.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAoRepeatTimes.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioGetAoRepeatTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAoClockType.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAoClockType.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAoSamplingClock.argtypes = [ctypes.c_short, ctypes.c_float]
DLL.AioGetAoSamplingClock.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_float)]
DLL.AioSetAoClockEdge.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAoClockEdge.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAoSamplingData.argtypes = [ctypes.c_short, ctypes.c_long, ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAoSamplingDataEx.argtypes = [ctypes.c_short, ctypes.c_long, ctypes.POINTER(ctypes.c_float)]
DLL.AioGetAoSamplingTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAoStartTrigger.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAoStartTrigger.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAoStopTrigger.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAoStopTrigger.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetAoEvent.argtypes = [ctypes.c_short, ctypes.c_int, ctypes.c_long]
DLL.AioGetAoEvent.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAoEventSamplingTimes.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioGetAoEventSamplingTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioSetAoEventTransferTimes.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioGetAoEventTransferTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioStartAo.argtypes = [ctypes.c_short]
DLL.AioStopAo.argtypes = [ctypes.c_short]
DLL.AioEnableAo.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioDisableAo.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioGetAoStatus.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAoSamplingCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAoTransferCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAoTransferLap.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetAoRepeatCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioResetAoStatus.argtypes = [ctypes.c_short]
DLL.AioResetAoMemory.argtypes = [ctypes.c_short]
DLL.AioSetDiFilter.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float]
DLL.AioGetDiFilter.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]
DLL.AioInputDiBit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioOutputDoBit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]
DLL.AioInputDiByte.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioOutputDoByte.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]
DLL.AioSetDioDirection.argtypes = [ctypes.c_short, ctypes.c_long]
DLL.AioGetDioDirectio.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetCntMaxChannels.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetCntComparisonMode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]
DLL.AioGetCntComparisonMode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetCntPresetReg.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.c_short]
DLL.AioSetCntComparisonReg.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.c_short]
DLL.AioSetCntInputSignal.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]
DLL.AioGetCntInputSignal.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSetCntEvent.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_int, ctypes.c_long]
DLL.AioGetCntEvent.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_long)]
DLL.AioSetCntFilter.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_float]
DLL.AioGetCntFilter.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]
DLL.AioStartCnt.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioStopCnt.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioPresetCnt.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long]
DLL.AioGetCntStatus.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioGetCntCount.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioResetCntStatus.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long]
DLL.AioSetTmEvent.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_int, ctypes.c_long]
DLL.AioGetTmEvent.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_long)]
DLL.AioStartTmTimer.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float]
DLL.AioStopTmTimer.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioStartTmCount.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioStopTmCount.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioLapTmCount.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]
DLL.AioResetTmCount.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.AioTmWait.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long]
DLL.AioSetEcuSignal.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]
DLL.AioGetEcuSignal.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.AioSelectCntmChannelSignal.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]
