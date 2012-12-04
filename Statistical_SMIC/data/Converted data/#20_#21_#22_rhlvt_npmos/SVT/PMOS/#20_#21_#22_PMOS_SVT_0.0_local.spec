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

# Output Spec values (Local Variation) for PMOS device
.START_DATA|PMOS|W=4.5|L=7.2|T=25
idlin                    idsat                    vtlin                    vtsat
3.359341e-03             3.895688e-03             5.335847e-04             4.799105e-04             
.END_DATA|PMOS|W=4.5|L=7.2|T=25
.START_DATA|PMOS|W=4.5|L=7.2|T=25
idlin                    idsat                    vtlin                    vtsat
3.357711e-03             3.901698e-03             5.384836e-04             4.804713e-04             
.END_DATA|PMOS|W=4.5|L=7.2|T=25
.START_DATA|PMOS|W=4.5|L=7.2|T=25
idlin                    idsat                    vtlin                    vtsat
3.359358e-03             3.909856e-03             5.376700e-04             4.823828e-04             
.END_DATA|PMOS|W=4.5|L=7.2|T=25
.START_DATA|PMOS|W=1.8|L=1.8|T=25
idlin                    idsat                    vtlin                    vtsat
5.650561e-03             7.892529e-03             2.095455e-03             1.751214e-03             
.END_DATA|PMOS|W=1.8|L=1.8|T=25
.START_DATA|PMOS|W=1.8|L=1.8|T=25
idlin                    idsat                    vtlin                    vtsat
5.639881e-03             7.873106e-03             2.097454e-03             1.750932e-03             
.END_DATA|PMOS|W=1.8|L=1.8|T=25
.START_DATA|PMOS|W=1.8|L=1.8|T=25
idlin                    idsat                    vtlin                    vtsat
5.649046e-03             7.881300e-03             2.093764e-03             1.746968e-03             
.END_DATA|PMOS|W=1.8|L=1.8|T=25
.START_DATA|PMOS|W=0.9|L=0.9|T=25
idlin                    idsat                    vtlin                    vtsat
7.603882e-03             1.227952e-02             4.176754e-03             4.039610e-03             
.END_DATA|PMOS|W=0.9|L=0.9|T=25
.START_DATA|PMOS|W=0.9|L=0.9|T=25
idlin                    idsat                    vtlin                    vtsat
7.619177e-03             1.231000e-02             4.161666e-03             4.044356e-03             
.END_DATA|PMOS|W=0.9|L=0.9|T=25
.START_DATA|PMOS|W=0.9|L=0.9|T=25
idlin                    idsat                    vtlin                    vtsat
7.633501e-03             1.233450e-02             4.153014e-03             4.046476e-03             
.END_DATA|PMOS|W=0.9|L=0.9|T=25
.START_DATA|PMOS|W=0.9|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
2.753158e-02             3.630929e-02             1.259307e-02             1.629148e-02             
.END_DATA|PMOS|W=0.9|L=0.054|T=25
.START_DATA|PMOS|W=0.9|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
2.743121e-02             3.629827e-02             1.257879e-02             1.628307e-02             
.END_DATA|PMOS|W=0.9|L=0.054|T=25
.START_DATA|PMOS|W=0.9|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
2.742066e-02             3.621399e-02             1.262835e-02             1.629236e-02             
.END_DATA|PMOS|W=0.9|L=0.054|T=25
.START_DATA|PMOS|W=0.45|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
3.941383e-02             4.962135e-02             1.767586e-02             2.028067e-02             
.END_DATA|PMOS|W=0.45|L=0.054|T=25
.START_DATA|PMOS|W=0.45|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
3.943720e-02             4.983908e-02             1.765931e-02             2.025322e-02             
.END_DATA|PMOS|W=0.45|L=0.054|T=25
.START_DATA|PMOS|W=0.45|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
3.946685e-02             4.965262e-02             1.766720e-02             2.026709e-02             
.END_DATA|PMOS|W=0.45|L=0.054|T=25
.START_DATA|PMOS|W=0.27|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
4.621736e-02             5.612038e-02             1.851514e-02             2.261562e-02             
.END_DATA|PMOS|W=0.27|L=0.054|T=25
.START_DATA|PMOS|W=0.27|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
4.618396e-02             5.619229e-02             1.840701e-02             2.263740e-02             
.END_DATA|PMOS|W=0.27|L=0.054|T=25
.START_DATA|PMOS|W=0.27|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
4.619269e-02             5.611923e-02             1.842845e-02             2.264496e-02             
.END_DATA|PMOS|W=0.27|L=0.054|T=25
.START_DATA|PMOS|W=0.135|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
6.716913e-02             8.516620e-02             2.864259e-02             3.271362e-02             
.END_DATA|PMOS|W=0.135|L=0.054|T=25
.START_DATA|PMOS|W=0.135|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
6.681112e-02             8.513701e-02             2.866769e-02             3.275834e-02             
.END_DATA|PMOS|W=0.135|L=0.054|T=25
.START_DATA|PMOS|W=0.135|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
6.733439e-02             8.488579e-02             2.871350e-02             3.279320e-02             
.END_DATA|PMOS|W=0.135|L=0.054|T=25
.START_DATA|PMOS|W=0.108|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
6.737662e-02             8.209749e-02             2.805214e-02             3.200047e-02             
.END_DATA|PMOS|W=0.108|L=0.054|T=25
.START_DATA|PMOS|W=0.108|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
6.648270e-02             8.220171e-02             2.808406e-02             3.206663e-02             
.END_DATA|PMOS|W=0.108|L=0.054|T=25
.START_DATA|PMOS|W=0.108|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
6.737774e-02             8.296829e-02             2.807446e-02             3.199454e-02             
.END_DATA|PMOS|W=0.108|L=0.054|T=25
.START_DATA|PMOS|W=1.8|L=0.0405|T=25
idlin                    idsat                    vtlin                    vtsat
2.578041e-02             3.068328e-02             1.230218e-02             1.436134e-02             
.END_DATA|PMOS|W=1.8|L=0.0405|T=25
.START_DATA|PMOS|W=1.8|L=0.0405|T=25
idlin                    idsat                    vtlin                    vtsat
2.580196e-02             3.073331e-02             1.232022e-02             1.435089e-02             
.END_DATA|PMOS|W=1.8|L=0.0405|T=25
.START_DATA|PMOS|W=1.8|L=0.0405|T=25
idlin                    idsat                    vtlin                    vtsat
2.580560e-02             3.078707e-02             1.228481e-02             1.434168e-02             
.END_DATA|PMOS|W=1.8|L=0.0405|T=25
.START_DATA|PMOS|W=0.108|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
8.943034e-02             1.031525e-01             3.805309e-02             4.085405e-02             
.END_DATA|PMOS|W=0.108|L=0.036|T=25
.START_DATA|PMOS|W=0.108|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
9.036658e-02             1.024174e-01             3.813685e-02             4.104637e-02             
.END_DATA|PMOS|W=0.108|L=0.036|T=25
.START_DATA|PMOS|W=0.108|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
9.029803e-02             1.028685e-01             3.806665e-02             4.068636e-02             
.END_DATA|PMOS|W=0.108|L=0.036|T=25
.START_DATA|PMOS|W=9.0|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.052780e-02             1.292935e-02             5.369027e-03             6.218965e-03             
.END_DATA|PMOS|W=9.0|L=0.036|T=25
.START_DATA|PMOS|W=9.0|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.053314e-02             1.293118e-02             5.332272e-03             6.202965e-03             
.END_DATA|PMOS|W=9.0|L=0.036|T=25
.START_DATA|PMOS|W=9.0|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.056165e-02             1.290488e-02             5.352308e-03             6.225010e-03             
.END_DATA|PMOS|W=9.0|L=0.036|T=25
.START_DATA|PMOS|W=4.5|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.671935e-02             2.007019e-02             7.255616e-03             8.555031e-03             
.END_DATA|PMOS|W=4.5|L=0.036|T=25
.START_DATA|PMOS|W=4.5|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.680726e-02             2.009010e-02             7.247332e-03             8.547785e-03             
.END_DATA|PMOS|W=4.5|L=0.036|T=25
.START_DATA|PMOS|W=4.5|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.681148e-02             2.011958e-02             7.264681e-03             8.548622e-03             
.END_DATA|PMOS|W=4.5|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.154662e-02             3.823103e-02             1.649012e-02             1.868997e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.159535e-02             3.805615e-02             1.641477e-02             1.876826e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.122220e-02             3.769071e-02             1.642154e-02             1.875053e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.078240e-02             4.952655e-02             1.920504e-02             2.228858e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.047458e-02             4.976487e-02             1.925695e-02             2.231502e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.082423e-02             4.979257e-02             1.928852e-02             2.229624e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.208873e-02             7.265766e-02             2.947650e-02             3.366397e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.219637e-02             7.288949e-02             2.945967e-02             3.353712e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.206390e-02             7.299210e-02             2.944062e-02             3.351283e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.135|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.635352e-02             8.918264e-02             3.401882e-02             3.921955e-02             
.END_DATA|PMOS|W=0.135|L=0.036|T=25
.START_DATA|PMOS|W=0.135|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.697846e-02             8.934725e-02             3.430226e-02             3.918199e-02             
.END_DATA|PMOS|W=0.135|L=0.036|T=25
.START_DATA|PMOS|W=0.135|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.709454e-02             8.922589e-02             3.401550e-02             3.923917e-02             
.END_DATA|PMOS|W=0.135|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.529879e-02             4.303938e-02             1.457164e-02             1.790770e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.519928e-02             4.302940e-02             1.457879e-02             1.785470e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.509521e-02             4.292314e-02             1.458523e-02             1.788904e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.723856e-02             4.383531e-02             1.653668e-02             1.895956e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.700034e-02             4.399339e-02             1.654238e-02             1.896046e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.716580e-02             4.406929e-02             1.658486e-02             1.893810e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.621148e-02             4.354010e-02             1.767079e-02             2.026670e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.667561e-02             4.406467e-02             1.757924e-02             2.049629e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.693990e-02             4.406321e-02             1.760253e-02             2.050735e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.973475e-02             4.605871e-02             1.720185e-02             2.059827e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.984390e-02             4.617787e-02             1.751878e-02             2.073799e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.957345e-02             4.592380e-02             1.723426e-02             2.055498e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.458325e-02             5.334529e-02             1.862733e-02             2.357390e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.400070e-02             5.281764e-02             1.827832e-02             2.333299e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.388276e-02             5.276969e-02             1.831734e-02             2.337903e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.542243e-02             5.587844e-02             2.193979e-02             2.631596e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.543556e-02             5.593274e-02             2.198162e-02             2.623459e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.572679e-02             5.594871e-02             2.193933e-02             2.621991e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.598635e-02             5.437339e-02             1.993882e-02             2.338273e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.571117e-02             5.423459e-02             1.990983e-02             2.339833e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.543911e-02             5.434539e-02             1.994078e-02             2.339876e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.465383e-02             5.443725e-02             2.240982e-02             2.656597e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.535325e-02             5.560147e-02             2.276126e-02             2.675429e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.465805e-02             5.457621e-02             2.243677e-02             2.655112e-02             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.453354e-02             7.602031e-02             2.725377e-02             3.242939e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.429002e-02             7.569672e-02             2.774644e-02             3.283747e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.465317e-02             7.578204e-02             2.773159e-02             3.282476e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.217892e-02             7.066218e-02             2.636890e-02             3.063744e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.203497e-02             7.051150e-02             2.643013e-02             3.064527e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.221774e-02             7.080082e-02             2.639450e-02             3.065451e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.824794e-02             7.082423e-02             2.671119e-02             3.101567e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.752620e-02             6.953636e-02             2.655007e-02             3.078384e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.853880e-02             7.052524e-02             2.665362e-02             3.095060e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.432694e-02             7.411917e-02             2.809123e-02             3.222673e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.435203e-02             7.370496e-02             2.776751e-02             3.194632e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.504141e-02             7.384046e-02             2.805018e-02             3.226172e-02             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
