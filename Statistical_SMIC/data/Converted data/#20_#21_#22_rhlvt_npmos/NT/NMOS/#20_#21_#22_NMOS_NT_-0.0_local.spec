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
.START_DATA|NMOS|W=4.5|L=4.5|T=25
idlin                    idsat                    vtlin                    vtsat
7.970983e-03             1.107126e-02             6.174254e-03             8.073607e-03             
.END_DATA|NMOS|W=4.5|L=4.5|T=25
.START_DATA|NMOS|W=4.5|L=4.5|T=25
idlin                    idsat                    vtlin                    vtsat
7.970003e-03             1.107587e-02             6.175443e-03             8.071174e-03             
.END_DATA|NMOS|W=4.5|L=4.5|T=25
.START_DATA|NMOS|W=4.5|L=4.5|T=25
idlin                    idsat                    vtlin                    vtsat
7.971168e-03             1.107626e-02             6.171042e-03             8.073780e-03             
.END_DATA|NMOS|W=4.5|L=4.5|T=25
.START_DATA|NMOS|W=1.8|L=4.5|T=25
idlin                    idsat                    vtlin                    vtsat
3.997290e-03             9.891169e-03             1.071557e-02             1.426379e-02             
.END_DATA|NMOS|W=1.8|L=4.5|T=25
.START_DATA|NMOS|W=1.8|L=4.5|T=25
idlin                    idsat                    vtlin                    vtsat
4.002978e-03             9.894916e-03             1.067818e-02             1.402744e-02             
.END_DATA|NMOS|W=1.8|L=4.5|T=25
.START_DATA|NMOS|W=1.8|L=4.5|T=25
idlin                    idsat                    vtlin                    vtsat
3.999224e-03             9.888802e-03             1.068949e-02             1.427918e-02             
.END_DATA|NMOS|W=1.8|L=4.5|T=25
.START_DATA|NMOS|W=1.8|L=1.08|T=25
idlin                    idsat                    vtlin                    vtsat
4.584151e-03             1.046650e-02             1.048585e-02             1.319401e-02             
.END_DATA|NMOS|W=1.8|L=1.08|T=25
.START_DATA|NMOS|W=1.8|L=1.08|T=25
idlin                    idsat                    vtlin                    vtsat
4.589389e-03             1.047173e-02             1.048933e-02             1.321532e-02             
.END_DATA|NMOS|W=1.8|L=1.08|T=25
.START_DATA|NMOS|W=1.8|L=1.08|T=25
idlin                    idsat                    vtlin                    vtsat
4.587320e-03             1.046898e-02             1.049983e-02             1.321031e-02             
.END_DATA|NMOS|W=1.8|L=1.08|T=25
.START_DATA|NMOS|W=0.36|L=1.08|T=25
idlin                    idsat                    vtlin                    vtsat
2.132762e-02             2.782959e-02             2.156270e-02             3.068783e-02             
.END_DATA|NMOS|W=0.36|L=1.08|T=25
.START_DATA|NMOS|W=0.36|L=1.08|T=25
idlin                    idsat                    vtlin                    vtsat
2.132056e-02             2.784368e-02             2.156795e-02             3.068339e-02             
.END_DATA|NMOS|W=0.36|L=1.08|T=25
.START_DATA|NMOS|W=0.36|L=1.08|T=25
idlin                    idsat                    vtlin                    vtsat
2.132510e-02             2.783067e-02             2.157961e-02             3.070189e-02             
.END_DATA|NMOS|W=0.36|L=1.08|T=25
.START_DATA|NMOS|W=1.8|L=0.63|T=25
idlin                    idsat                    vtlin                    vtsat
5.940382e-03             1.056303e-02             9.695925e-03             1.394754e-02             
.END_DATA|NMOS|W=1.8|L=0.63|T=25
.START_DATA|NMOS|W=1.8|L=0.63|T=25
idlin                    idsat                    vtlin                    vtsat
5.937848e-03             1.056520e-02             9.699497e-03             1.395117e-02             
.END_DATA|NMOS|W=1.8|L=0.63|T=25
.START_DATA|NMOS|W=1.8|L=0.63|T=25
idlin                    idsat                    vtlin                    vtsat
5.932370e-03             1.059253e-02             9.709724e-03             1.390967e-02             
.END_DATA|NMOS|W=1.8|L=0.63|T=25
.START_DATA|NMOS|W=1.8|L=0.45|T=25
idlin                    idsat                    vtlin                    vtsat
1.027811e-02             1.282797e-02             9.312584e-03             1.365056e-02             
.END_DATA|NMOS|W=1.8|L=0.45|T=25
.START_DATA|NMOS|W=1.8|L=0.45|T=25
idlin                    idsat                    vtlin                    vtsat
1.027691e-02             1.283231e-02             9.306401e-03             1.366066e-02             
.END_DATA|NMOS|W=1.8|L=0.45|T=25
.START_DATA|NMOS|W=1.8|L=0.45|T=25
idlin                    idsat                    vtlin                    vtsat
1.028749e-02             1.281601e-02             9.314727e-03             1.364406e-02             
.END_DATA|NMOS|W=1.8|L=0.45|T=25
.START_DATA|NMOS|W=9.0|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
8.184062e-03             1.009439e-02             4.450774e-03             5.805646e-03             
.END_DATA|NMOS|W=9.0|L=0.36|T=25
.START_DATA|NMOS|W=9.0|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
8.186414e-03             1.009720e-02             4.451862e-03             5.808984e-03             
.END_DATA|NMOS|W=9.0|L=0.36|T=25
.START_DATA|NMOS|W=9.0|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
8.180431e-03             1.009202e-02             4.444066e-03             5.808499e-03             
.END_DATA|NMOS|W=9.0|L=0.36|T=25
.START_DATA|NMOS|W=0.9|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
1.456491e-02             1.892565e-02             1.353201e-02             2.000299e-02             
.END_DATA|NMOS|W=0.9|L=0.36|T=25
.START_DATA|NMOS|W=0.9|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
1.455745e-02             1.892908e-02             1.353856e-02             1.999065e-02             
.END_DATA|NMOS|W=0.9|L=0.36|T=25
.START_DATA|NMOS|W=0.9|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
1.456700e-02             1.892400e-02             1.353456e-02             1.999774e-02             
.END_DATA|NMOS|W=0.9|L=0.36|T=25
.START_DATA|NMOS|W=0.45|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
1.780643e-02             2.329801e-02             1.865662e-02             2.438379e-02             
.END_DATA|NMOS|W=0.45|L=0.36|T=25
.START_DATA|NMOS|W=0.45|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
1.781208e-02             2.331612e-02             1.864694e-02             2.436854e-02             
.END_DATA|NMOS|W=0.45|L=0.36|T=25
.START_DATA|NMOS|W=0.45|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
1.779946e-02             2.333599e-02             1.865016e-02             2.437892e-02             
.END_DATA|NMOS|W=0.45|L=0.36|T=25
.START_DATA|NMOS|W=0.36|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
1.768533e-02             2.339586e-02             2.114766e-02             2.627226e-02             
.END_DATA|NMOS|W=0.36|L=0.36|T=25
.START_DATA|NMOS|W=0.36|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
1.769867e-02             2.341630e-02             2.115757e-02             2.629289e-02             
.END_DATA|NMOS|W=0.36|L=0.36|T=25
.START_DATA|NMOS|W=0.36|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
1.770524e-02             2.340322e-02             2.113750e-02             2.636631e-02             
.END_DATA|NMOS|W=0.36|L=0.36|T=25
.START_DATA|NMOS|W=1.8|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.073732e-02             1.396341e-02             9.771037e-03             1.303573e-02             
.END_DATA|NMOS|W=1.8|L=0.27|T=25
.START_DATA|NMOS|W=1.8|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.072370e-02             1.395955e-02             9.781614e-03             1.303922e-02             
.END_DATA|NMOS|W=1.8|L=0.27|T=25
.START_DATA|NMOS|W=1.8|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.072657e-02             1.395949e-02             9.774871e-03             1.305670e-02             
.END_DATA|NMOS|W=1.8|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.454645e-02             1.804147e-02             1.361567e-02             1.965770e-02             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.455023e-02             1.805437e-02             1.360032e-02             1.969934e-02             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.456151e-02             1.806021e-02             1.359905e-02             1.971229e-02             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.36|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
2.555763e-02             2.847744e-02             2.228810e-02             3.005364e-02             
.END_DATA|NMOS|W=0.36|L=0.27|T=25
.START_DATA|NMOS|W=0.36|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
2.556608e-02             2.848775e-02             2.227046e-02             3.004649e-02             
.END_DATA|NMOS|W=0.36|L=0.27|T=25
.START_DATA|NMOS|W=0.36|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
2.558594e-02             2.847231e-02             2.227190e-02             3.006609e-02             
.END_DATA|NMOS|W=0.36|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.496648e-02             1.615613e-02             1.324546e-02             1.706228e-02             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.497903e-02             1.616022e-02             1.324892e-02             1.705910e-02             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.495998e-02             1.614134e-02             1.325721e-02             1.707280e-02             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.514719e-02             1.797597e-02             1.369299e-02             1.837945e-02             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.513481e-02             1.798491e-02             1.364682e-02             1.838290e-02             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.513647e-02             1.795135e-02             1.365214e-02             1.839633e-02             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.625853e-02             1.914521e-02             1.341228e-02             1.758583e-02             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.630532e-02             1.913515e-02             1.346003e-02             1.750416e-02             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.629690e-02             1.917660e-02             1.344958e-02             1.749052e-02             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
