import numpy, sys, os, pyopencl, random
platform = pyopencl.get_platforms()[0]
mygpu = platform.get_devices(pyopencl.device_type.GPU)[0]
context = pyopencl.Context(devices=[mygpu])
queue = pyopencl.CommandQueue(context)
prog = pyopencl.Program(context, open("func.cl").read()).build(devices=[mygpu])
