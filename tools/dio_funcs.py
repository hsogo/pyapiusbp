DLL.DioInit.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_short)]
DLL.DioExit.argtypes = [ctypes.c_short]
DLL.DioResetDevice.argtypes = [ctypes.c_short]
DLL.DioGetErrorString.argtypes = [ctypes.c_long, ctypes.POINTER(ctypes.c_char)]
DLL.DioSetDigitalFilter.argtypes = [ctypes.c_short, ctypes.c_short]
DLL.DioGetDigitalFilter.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.DioSetIoDirection.argtypes = [ctypes.c_short, ctypes.c_uint]
DLL.DioGetIoDirection.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_uint)]
DLL.DioSetIoDirectionEx.argtypes = [ctypes.c_short, ctypes.c_uint]
DLL.DioGetIoDirectionEx.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_uint)]
DLL.DioSet8255Mode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]
DLL.DioGet8255Mode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]
DLL.DioInpByte.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_uchar)]
DLL.DioInpBit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_uchar)]
DLL.DioOutByte.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_uchar]
DLL.DioOutBit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_uchar]
DLL.DioEchoBackByte.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_uchar)]
DLL.DioEchoBackBit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_uchar)]
DLL.DioInpMultiByte.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.c_short, ctypes.POINTER(ctypes.c_uchar)]
DLL.DioInpMultiBit.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.c_short, ctypes.POINTER(ctypes.c_uchar)]
DLL.DioOutMultiByte.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.c_short, ctypes.POINTER(ctypes.c_uchar)]
DLL.DioOutMultiBit.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.c_short, ctypes.POINTER(ctypes.c_uchar)]
DLL.DioEchoBackMultiByte.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.c_short, ctypes.POINTER(ctypes.c_uchar)]
DLL.DioEchoBackMultiBit.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.c_short, ctypes.POINTER(ctypes.c_uchar)]
DLL.DioQueryDeviceName.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char)]
DLL.DioGetDeviceType.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_short)]
DLL.DioGetMaxPorts.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]
DLL.DioSetDemoByte.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_uchar]
DLL.DioSetDemoBit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_uchar]
