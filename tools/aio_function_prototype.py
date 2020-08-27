# coding:utf-8

import codecs

lookup = {
    'HWND':'ctypes.c_int',
    'HWND *':'ctypes.POINTER(ctypes.c_int)',
    'char *':'ctypes.POINTER(ctypes.c_char)',
    'long':'ctypes.c_long',
    'long *':'ctypes.POINTER(ctypes.c_long)',
    'float':'ctypes.c_float',
    'float *':'ctypes.POINTER(ctypes.c_float)',
    'short':'ctypes.c_short',
    'short *':'ctypes.POINTER(ctypes.c_short)'
}

all_argtypes= []
all_rettypes = []
callbackfunc = []

gen_list = False

if not gen_list:
    out_fp = codecs.open('aio_funcs.py','w','utf8')

in_fp = codecs.open('Caio.h','r','cp932')
for line in in_fp:
    if 'WINAPI' in line:
        split = line.split(' ')
        rettype = split[0]
        if gen_list:
            all_rettypes.append(rettype)
        funcname = split[2][:split[2].find('(')]
        if 'CallBackProc' in funcname:
            callbackfunc.append(line)
            continue
        elif 'AioCntm' in funcname:
            continue
        elif 'AioGetCntm' in funcname:
            continue
        elif 'AioSetCntm' in funcname:
            continue
        tmp = ' '.join(split[2:])
        arglist = tmp[tmp.find('(')+1:-2].split(',')
        c_arg = []
        for arg in arglist:
            tmparg = arg.strip().rsplit(' ', 1)
            if tmparg[1][0] == '*':
                tmparg[0] += ' *'
            if gen_list:
                all_argtypes.append(tmparg[0])
            c_arg.append(lookup[tmparg[0]])
        
        code = 'DLL.'+funcname+'.argtypes = [' + ', '.join(c_arg) + ']'
        print(code)
        if not gen_list:
            out_fp.write(code)
            out_fp.write('\n')

in_fp.close()
if not gen_list:
    out_fp.close()
