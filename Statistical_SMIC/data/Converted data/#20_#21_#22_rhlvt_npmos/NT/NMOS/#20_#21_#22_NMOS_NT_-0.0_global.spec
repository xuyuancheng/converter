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

# Output Spec values (Sigma) for NMOS device
.START_DATA|NMOS|W=4.5|L=4.5|T=25
idlin                    idsat                    vtlin                    vtsat
2.564182e-07             2.368913e-06             3.960569e-03             4.178829e-03             
.END_DATA|NMOS|W=4.5|L=4.5|T=25
.START_DATA|NMOS|W=4.5|L=4.5|T=25
idlin                    idsat                    vtlin                    vtsat
2.565904e-07             2.371057e-06             3.963427e-03             4.197172e-03             
.END_DATA|NMOS|W=4.5|L=4.5|T=25
.START_DATA|NMOS|W=4.5|L=4.5|T=25
idlin                    idsat                    vtlin                    vtsat
2.566573e-07             2.371454e-06             3.957692e-03             4.181965e-03             
.END_DATA|NMOS|W=4.5|L=4.5|T=25
.START_DATA|NMOS|W=1.8|L=4.5|T=25
idlin                    idsat                    vtlin                    vtsat
9.763424e-08             9.476401e-07             3.436501e-03             3.747876e-03             
.END_DATA|NMOS|W=1.8|L=4.5|T=25
.START_DATA|NMOS|W=1.8|L=4.5|T=25
idlin                    idsat                    vtlin                    vtsat
9.730393e-08             9.444139e-07             3.466826e-03             3.884557e-03             
.END_DATA|NMOS|W=1.8|L=4.5|T=25
.START_DATA|NMOS|W=1.8|L=4.5|T=25
idlin                    idsat                    vtlin                    vtsat
9.769350e-08             9.484764e-07             3.458762e-03             3.708129e-03             
.END_DATA|NMOS|W=1.8|L=4.5|T=25
.START_DATA|NMOS|W=1.8|L=1.08|T=25
idlin                    idsat                    vtlin                    vtsat
4.976064e-07             3.739137e-06             3.867281e-03             4.000208e-03             
.END_DATA|NMOS|W=1.8|L=1.08|T=25
.START_DATA|NMOS|W=1.8|L=1.08|T=25
idlin                    idsat                    vtlin                    vtsat
4.976875e-07             3.740306e-06             3.873621e-03             3.969376e-03             
.END_DATA|NMOS|W=1.8|L=1.08|T=25
.START_DATA|NMOS|W=1.8|L=1.08|T=25
idlin                    idsat                    vtlin                    vtsat
4.977895e-07             3.741216e-06             3.848586e-03             3.969538e-03             
.END_DATA|NMOS|W=1.8|L=1.08|T=25
.START_DATA|NMOS|W=0.36|L=1.08|T=25
idlin                    idsat                    vtlin                    vtsat
0.000000e+00             3.466846e-07             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.36|L=1.08|T=25
.START_DATA|NMOS|W=0.36|L=1.08|T=25
idlin                    idsat                    vtlin                    vtsat
0.000000e+00             3.461699e-07             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.36|L=1.08|T=25
.START_DATA|NMOS|W=0.36|L=1.08|T=25
idlin                    idsat                    vtlin                    vtsat
0.000000e+00             3.458180e-07             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.36|L=1.08|T=25
.START_DATA|NMOS|W=1.8|L=0.63|T=25
idlin                    idsat                    vtlin                    vtsat
8.440679e-07             4.904085e-06             4.902214e-03             4.809222e-03             
.END_DATA|NMOS|W=1.8|L=0.63|T=25
.START_DATA|NMOS|W=1.8|L=0.63|T=25
idlin                    idsat                    vtlin                    vtsat
8.444849e-07             4.908353e-06             4.901282e-03             4.822449e-03             
.END_DATA|NMOS|W=1.8|L=0.63|T=25
.START_DATA|NMOS|W=1.8|L=0.63|T=25
idlin                    idsat                    vtlin                    vtsat
8.401031e-07             4.843952e-06             4.706021e-03             4.628912e-03             
.END_DATA|NMOS|W=1.8|L=0.63|T=25
.START_DATA|NMOS|W=1.8|L=0.45|T=25
idlin                    idsat                    vtlin                    vtsat
1.077969e-06             5.836836e-06             4.070571e-03             3.441726e-03             
.END_DATA|NMOS|W=1.8|L=0.45|T=25
.START_DATA|NMOS|W=1.8|L=0.45|T=25
idlin                    idsat                    vtlin                    vtsat
1.077520e-06             5.837860e-06             4.090052e-03             3.452264e-03             
.END_DATA|NMOS|W=1.8|L=0.45|T=25
.START_DATA|NMOS|W=1.8|L=0.45|T=25
idlin                    idsat                    vtlin                    vtsat
1.077087e-06             5.847290e-06             4.084535e-03             3.460157e-03             
.END_DATA|NMOS|W=1.8|L=0.45|T=25
.START_DATA|NMOS|W=9.0|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
6.410189e-06             6.499866e-05             3.827801e-03             3.837662e-03             
.END_DATA|NMOS|W=9.0|L=0.36|T=25
.START_DATA|NMOS|W=9.0|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
6.407040e-06             6.499635e-05             3.822424e-03             3.830221e-03             
.END_DATA|NMOS|W=9.0|L=0.36|T=25
.START_DATA|NMOS|W=9.0|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
6.405102e-06             6.499065e-05             3.826801e-03             3.832271e-03             
.END_DATA|NMOS|W=9.0|L=0.36|T=25
.START_DATA|NMOS|W=0.9|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
5.601695e-07             2.911926e-06             4.915774e-03             4.038612e-03             
.END_DATA|NMOS|W=0.9|L=0.36|T=25
.START_DATA|NMOS|W=0.9|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
5.606548e-07             2.903902e-06             4.917104e-03             4.057598e-03             
.END_DATA|NMOS|W=0.9|L=0.36|T=25
.START_DATA|NMOS|W=0.9|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
5.598095e-07             2.907381e-06             4.906637e-03             4.010306e-03             
.END_DATA|NMOS|W=0.9|L=0.36|T=25
.START_DATA|NMOS|W=0.45|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
3.673026e-07             1.910017e-06             5.452837e-03             7.345077e-03             
.END_DATA|NMOS|W=0.45|L=0.36|T=25
.START_DATA|NMOS|W=0.45|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
3.673472e-07             1.912334e-06             5.437525e-03             7.363299e-03             
.END_DATA|NMOS|W=0.45|L=0.36|T=25
.START_DATA|NMOS|W=0.45|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
3.677112e-07             1.908946e-06             5.454096e-03             7.370209e-03             
.END_DATA|NMOS|W=0.45|L=0.36|T=25
.START_DATA|NMOS|W=0.36|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
2.729320e-07             1.377941e-06             4.839890e-03             7.589826e-03             
.END_DATA|NMOS|W=0.36|L=0.36|T=25
.START_DATA|NMOS|W=0.36|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
2.725945e-07             1.376057e-06             4.826601e-03             7.624005e-03             
.END_DATA|NMOS|W=0.36|L=0.36|T=25
.START_DATA|NMOS|W=0.36|L=0.36|T=25
idlin                    idsat                    vtlin                    vtsat
2.724721e-07             1.377787e-06             4.834669e-03             7.581537e-03             
.END_DATA|NMOS|W=0.36|L=0.36|T=25
.START_DATA|NMOS|W=1.8|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.912108e-06             8.026279e-06             2.931056e-03             3.174787e-03             
.END_DATA|NMOS|W=1.8|L=0.27|T=25
.START_DATA|NMOS|W=1.8|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.915397e-06             8.022208e-06             2.923718e-03             3.177279e-03             
.END_DATA|NMOS|W=1.8|L=0.27|T=25
.START_DATA|NMOS|W=1.8|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.914254e-06             8.022108e-06             2.927369e-03             3.164864e-03             
.END_DATA|NMOS|W=1.8|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
8.800082e-07             4.084300e-06             3.868246e-03             3.672143e-03             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
8.795869e-07             4.080325e-06             3.854921e-03             3.574257e-03             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
8.783906e-07             4.075608e-06             3.860932e-03             3.553926e-03             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.36|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
2.458766e-07             1.562638e-06             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.36|L=0.27|T=25
.START_DATA|NMOS|W=0.36|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
2.464076e-07             1.566266e-06             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.36|L=0.27|T=25
.START_DATA|NMOS|W=0.36|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
2.456207e-07             1.562764e-06             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.36|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.201798e-06             5.128379e-06             4.452061e-03             5.500452e-03             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.201139e-06             5.128770e-06             4.440433e-03             5.509897e-03             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.202610e-06             5.127339e-06             4.431704e-03             5.479187e-03             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
9.205953e-07             3.708740e-06             3.242136e-03             4.758640e-03             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
9.211087e-07             3.714844e-06             3.295074e-03             4.751083e-03             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
9.209986e-07             3.716596e-06             3.305590e-03             4.718380e-03             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.202699e-06             5.169157e-06             4.566238e-03             4.822345e-03             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.207497e-06             5.185585e-06             4.558945e-03             4.810459e-03             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
.START_DATA|NMOS|W=0.9|L=0.27|T=25
idlin                    idsat                    vtlin                    vtsat
1.206999e-06             5.183125e-06             4.577341e-03             4.811873e-03             
.END_DATA|NMOS|W=0.9|L=0.27|T=25
