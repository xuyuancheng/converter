#
# GLOBAL section -- global variables
#
.START_GLOBAL
#Name	#Value
INSTANCE_COL	3
VDD	5	NMOS
VDTHX	0.1	NMOS
CC_VAL	1.00E-07	NMOS
VDD	-5	PMOS
VDTHX	-0.1	PMOS
CC_VAL	-1.00E-07	PMOS
.END_GLOBAL

.START_OUTPUT
#Output_Name	#Key_Output_Name	# ERROR expression	# the criteria of on-target	#Bias
vtsat	Vth_CC	Error=(Model-Target)*1000	Error<10	Vds=Vdd	Vbs=0	CC=CC_VAL	L_Offset=0	W_Offset=0	Current=Id
vtlin	Vth_CC	Error=(Model-Target)*1000	Error<10	Vds=Vdthx	Vbs=0	CC=CC_VAL	L_Offset=0	W_Offset=0	Current=Id
idsat	Idsat	Error=(Model/Target-1)*100	Error<10	Vgs=Vdd	Vds=Vdd	Vbs=0
idlin	Idlin	Error=(Model/Target-1)*100	Error<10	Vgs=Vdd	Vds=Vdthx	Vbs=0
.END_OUTPUT

# Output Spec values (Local Variation) for NMOS device
.START_DATA|NMOS|W=4.5|L=7.2|T=25
idlin                    idsat                    vtlin                    vtsat
5.369409e-03             6.961777e-03             3.394758e-03             3.114413e-03             
.END_DATA|NMOS|W=4.5|L=7.2|T=25
.START_DATA|NMOS|W=4.5|L=7.2|T=25
idlin                    idsat                    vtlin                    vtsat
5.369504e-03             6.964065e-03             3.388537e-03             3.123059e-03             
.END_DATA|NMOS|W=4.5|L=7.2|T=25
.START_DATA|NMOS|W=4.5|L=7.2|T=25
idlin                    idsat                    vtlin                    vtsat
5.367409e-03             6.962760e-03             3.389258e-03             3.115227e-03             
.END_DATA|NMOS|W=4.5|L=7.2|T=25
.START_DATA|NMOS|W=1.8|L=1.8|T=25
idlin                    idsat                    vtlin                    vtsat
8.352693e-03             1.216605e-02             8.121442e-03             9.778912e-03             
.END_DATA|NMOS|W=1.8|L=1.8|T=25
.START_DATA|NMOS|W=1.8|L=1.8|T=25
idlin                    idsat                    vtlin                    vtsat
8.357792e-03             1.216560e-02             8.129435e-03             9.784148e-03             
.END_DATA|NMOS|W=1.8|L=1.8|T=25
.START_DATA|NMOS|W=1.8|L=1.8|T=25
idlin                    idsat                    vtlin                    vtsat
8.352751e-03             1.217057e-02             8.124936e-03             9.788376e-03             
.END_DATA|NMOS|W=1.8|L=1.8|T=25
.START_DATA|NMOS|W=0.9|L=0.9|T=25
idlin                    idsat                    vtlin                    vtsat
1.093173e-02             1.742361e-02             1.210609e-02             1.553094e-02             
.END_DATA|NMOS|W=0.9|L=0.9|T=25
.START_DATA|NMOS|W=0.9|L=0.9|T=25
idlin                    idsat                    vtlin                    vtsat
1.092487e-02             1.740690e-02             1.209960e-02             1.547600e-02             
.END_DATA|NMOS|W=0.9|L=0.9|T=25
.START_DATA|NMOS|W=0.9|L=0.9|T=25
idlin                    idsat                    vtlin                    vtsat
1.092442e-02             1.743609e-02             1.209596e-02             1.552093e-02             
.END_DATA|NMOS|W=0.9|L=0.9|T=25
.START_DATA|NMOS|W=0.9|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
3.801848e-02             4.555727e-02             1.810525e-02             2.090213e-02             
.END_DATA|NMOS|W=0.9|L=0.054|T=25
.START_DATA|NMOS|W=0.9|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
3.802836e-02             4.555937e-02             1.809169e-02             2.090434e-02             
.END_DATA|NMOS|W=0.9|L=0.054|T=25
.START_DATA|NMOS|W=0.9|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
3.804767e-02             4.555256e-02             1.809703e-02             2.091383e-02             
.END_DATA|NMOS|W=0.9|L=0.054|T=25
.START_DATA|NMOS|W=0.45|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
5.102652e-02             5.984308e-02             2.869232e-02             3.021031e-02             
.END_DATA|NMOS|W=0.45|L=0.054|T=25
.START_DATA|NMOS|W=0.45|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
5.096697e-02             5.978830e-02             2.867828e-02             3.018513e-02             
.END_DATA|NMOS|W=0.45|L=0.054|T=25
.START_DATA|NMOS|W=0.45|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
5.095244e-02             5.981135e-02             2.869686e-02             3.021252e-02             
.END_DATA|NMOS|W=0.45|L=0.054|T=25
.START_DATA|NMOS|W=0.27|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
6.783972e-02             7.636540e-02             3.556191e-02             3.748093e-02             
.END_DATA|NMOS|W=0.27|L=0.054|T=25
.START_DATA|NMOS|W=0.27|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
6.783881e-02             7.633443e-02             3.556237e-02             3.748431e-02             
.END_DATA|NMOS|W=0.27|L=0.054|T=25
.START_DATA|NMOS|W=0.27|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
6.786927e-02             7.635712e-02             3.554583e-02             3.750353e-02             
.END_DATA|NMOS|W=0.27|L=0.054|T=25
.START_DATA|NMOS|W=0.135|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
8.013145e-02             8.853141e-02             4.161214e-02             4.470076e-02             
.END_DATA|NMOS|W=0.135|L=0.054|T=25
.START_DATA|NMOS|W=0.135|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
7.990235e-02             8.896404e-02             4.153662e-02             4.469585e-02             
.END_DATA|NMOS|W=0.135|L=0.054|T=25
.START_DATA|NMOS|W=0.135|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
8.015579e-02             8.899563e-02             4.167398e-02             4.468404e-02             
.END_DATA|NMOS|W=0.135|L=0.054|T=25
.START_DATA|NMOS|W=0.108|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
9.775670e-02             1.110426e-01             4.264811e-02             4.864316e-02             
.END_DATA|NMOS|W=0.108|L=0.054|T=25
.START_DATA|NMOS|W=0.108|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
9.844695e-02             1.122239e-01             4.257895e-02             4.855943e-02             
.END_DATA|NMOS|W=0.108|L=0.054|T=25
.START_DATA|NMOS|W=0.108|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
9.855942e-02             1.122888e-01             4.260414e-02             4.854364e-02             
.END_DATA|NMOS|W=0.108|L=0.054|T=25
.START_DATA|NMOS|W=1.8|L=0.0405|T=25
idlin                    idsat                    vtlin                    vtsat
3.388961e-02             3.829683e-02             1.650411e-02             1.876887e-02             
.END_DATA|NMOS|W=1.8|L=0.0405|T=25
.START_DATA|NMOS|W=1.8|L=0.0405|T=25
idlin                    idsat                    vtlin                    vtsat
3.388059e-02             3.832460e-02             1.646394e-02             1.876612e-02             
.END_DATA|NMOS|W=1.8|L=0.0405|T=25
.START_DATA|NMOS|W=1.8|L=0.0405|T=25
idlin                    idsat                    vtlin                    vtsat
3.379960e-02             3.833647e-02             1.647398e-02             1.876358e-02             
.END_DATA|NMOS|W=1.8|L=0.0405|T=25
.START_DATA|NMOS|W=0.108|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.110312e-01             1.165926e-01             5.296022e-02             5.422571e-02             
.END_DATA|NMOS|W=0.108|L=0.036|T=25
.START_DATA|NMOS|W=0.108|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.108988e-01             1.166856e-01             5.299680e-02             5.447174e-02             
.END_DATA|NMOS|W=0.108|L=0.036|T=25
.START_DATA|NMOS|W=0.108|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.108274e-01             1.167772e-01             5.320351e-02             5.464866e-02             
.END_DATA|NMOS|W=0.108|L=0.036|T=25
.START_DATA|NMOS|W=9.0|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.287621e-02             1.707234e-02             8.417034e-03             9.819024e-03             
.END_DATA|NMOS|W=9.0|L=0.036|T=25
.START_DATA|NMOS|W=9.0|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.287823e-02             1.708490e-02             8.418085e-03             9.833662e-03             
.END_DATA|NMOS|W=9.0|L=0.036|T=25
.START_DATA|NMOS|W=9.0|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.289650e-02             1.709315e-02             8.414078e-03             9.810483e-03             
.END_DATA|NMOS|W=9.0|L=0.036|T=25
.START_DATA|NMOS|W=4.5|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.031108e-02             2.359238e-02             1.092909e-02             1.232714e-02             
.END_DATA|NMOS|W=4.5|L=0.036|T=25
.START_DATA|NMOS|W=4.5|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.029309e-02             2.359890e-02             1.094105e-02             1.230293e-02             
.END_DATA|NMOS|W=4.5|L=0.036|T=25
.START_DATA|NMOS|W=4.5|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.028091e-02             2.358769e-02             1.090724e-02             1.232148e-02             
.END_DATA|NMOS|W=4.5|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.602915e-02             4.739422e-02             2.395648e-02             2.522458e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.612304e-02             4.735758e-02             2.396095e-02             2.525158e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.611342e-02             4.738224e-02             2.395440e-02             2.529773e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.111118e-02             6.583600e-02             2.909683e-02             3.251852e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.092146e-02             6.588309e-02             2.906320e-02             3.258816e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.103060e-02             6.590273e-02             2.907741e-02             3.256132e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
8.800110e-02             8.971513e-02             4.385072e-02             4.483627e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
8.796513e-02             8.969636e-02             4.384953e-02             4.490982e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
8.794520e-02             8.970830e-02             4.387645e-02             4.489481e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.135|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.126078e-01             1.210817e-01             5.177059e-02             5.277851e-02             
.END_DATA|NMOS|W=0.135|L=0.036|T=25
.START_DATA|NMOS|W=0.135|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.125922e-01             1.211984e-01             5.184288e-02             5.279353e-02             
.END_DATA|NMOS|W=0.135|L=0.036|T=25
.START_DATA|NMOS|W=0.135|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.125850e-01             1.210548e-01             5.182993e-02             5.280266e-02             
.END_DATA|NMOS|W=0.135|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.743407e-02             4.871239e-02             2.220263e-02             2.481592e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.741350e-02             4.872808e-02             2.220636e-02             2.478432e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.735078e-02             4.865389e-02             2.219471e-02             2.476468e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.514515e-02             4.995934e-02             2.355772e-02             2.599798e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.522159e-02             4.991339e-02             2.355554e-02             2.601225e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.521203e-02             4.993581e-02             2.359942e-02             2.602061e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.939748e-02             6.527370e-02             2.796844e-02             3.124274e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.956469e-02             6.539492e-02             2.805839e-02             3.117201e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.877019e-02             6.480969e-02             2.793017e-02             3.122699e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.541881e-02             5.875217e-02             2.685409e-02             2.877597e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.532804e-02             5.881794e-02             2.688596e-02             2.878534e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.533656e-02             5.878231e-02             2.686628e-02             2.875769e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.583257e-02             4.926417e-02             2.601449e-02             2.815246e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.575967e-02             4.925453e-02             2.602075e-02             2.812344e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.584392e-02             4.932258e-02             2.599934e-02             2.814558e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.761649e-02             4.913521e-02             2.334698e-02             2.509685e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.755798e-02             4.911672e-02             2.334130e-02             2.509415e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.758253e-02             4.915174e-02             2.337057e-02             2.510829e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.948810e-02             6.530575e-02             2.902234e-02             3.200550e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.873188e-02             6.487353e-02             2.896476e-02             3.197414e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.874765e-02             6.487474e-02             2.903144e-02             3.201374e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.541852e-02             5.876718e-02             2.747986e-02             2.965905e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.529654e-02             5.877404e-02             2.751816e-02             2.994506e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.585330e-02             5.918811e-02             2.769248e-02             2.956217e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.927464e-02             8.644163e-02             3.971106e-02             4.260874e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.922913e-02             8.649842e-02             3.972164e-02             4.265817e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.922392e-02             8.640226e-02             3.974176e-02             4.256859e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.924523e-02             8.571309e-02             4.188279e-02             4.665891e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.918125e-02             8.564331e-02             4.188280e-02             4.663549e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.921143e-02             8.571537e-02             4.191083e-02             4.666637e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.600275e-02             7.774861e-02             3.793964e-02             4.363490e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.666672e-02             7.797773e-02             3.809302e-02             4.197901e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.651724e-02             7.797759e-02             3.807505e-02             4.196775e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.793784e-02             8.054692e-02             3.899467e-02             4.046901e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.780759e-02             8.047766e-02             3.898095e-02             4.179444e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.771599e-02             8.042064e-02             3.912775e-02             4.224067e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
