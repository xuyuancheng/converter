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

# Output Spec values (Sigma) for PMOS device
.START_DATA|PMOS|W=4.5|L=7.2|T=25
idlin                    idsat                    vtlin                    vtsat
1.528192e-08             1.294306e-07             3.840656e-03             3.846166e-03             
.END_DATA|PMOS|W=4.5|L=7.2|T=25
.START_DATA|PMOS|W=4.5|L=7.2|T=25
idlin                    idsat                    vtlin                    vtsat
1.529242e-08             1.294047e-07             3.839192e-03             3.847061e-03             
.END_DATA|PMOS|W=4.5|L=7.2|T=25
.START_DATA|PMOS|W=4.5|L=7.2|T=25
idlin                    idsat                    vtlin                    vtsat
1.529242e-08             1.294208e-07             3.839692e-03             3.848135e-03             
.END_DATA|PMOS|W=4.5|L=7.2|T=25
.START_DATA|PMOS|W=1.8|L=1.8|T=25
idlin                    idsat                    vtlin                    vtsat
2.376361e-08             1.991043e-07             3.558413e-03             3.562352e-03             
.END_DATA|PMOS|W=1.8|L=1.8|T=25
.START_DATA|PMOS|W=1.8|L=1.8|T=25
idlin                    idsat                    vtlin                    vtsat
2.374209e-08             1.992982e-07             3.557413e-03             3.559900e-03             
.END_DATA|PMOS|W=1.8|L=1.8|T=25
.START_DATA|PMOS|W=1.8|L=1.8|T=25
idlin                    idsat                    vtlin                    vtsat
2.372387e-08             1.992659e-07             3.558327e-03             3.561829e-03             
.END_DATA|PMOS|W=1.8|L=1.8|T=25
.START_DATA|PMOS|W=0.9|L=0.9|T=25
idlin                    idsat                    vtlin                    vtsat
3.427958e-08             2.109344e-07             3.430287e-03             3.553781e-03             
.END_DATA|PMOS|W=0.9|L=0.9|T=25
.START_DATA|PMOS|W=0.9|L=0.9|T=25
idlin                    idsat                    vtlin                    vtsat
3.421606e-08             2.097158e-07             3.444399e-03             3.549542e-03             
.END_DATA|PMOS|W=0.9|L=0.9|T=25
.START_DATA|PMOS|W=0.9|L=0.9|T=25
idlin                    idsat                    vtlin                    vtsat
3.404511e-08             2.098886e-07             3.436471e-03             3.555896e-03             
.END_DATA|PMOS|W=0.9|L=0.9|T=25
.START_DATA|PMOS|W=0.9|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
1.051413e-06             4.003634e-06             2.688201e-03             2.701922e-03             
.END_DATA|PMOS|W=0.9|L=0.054|T=25
.START_DATA|PMOS|W=0.9|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
1.052309e-06             3.985814e-06             2.756875e-03             2.763630e-03             
.END_DATA|PMOS|W=0.9|L=0.054|T=25
.START_DATA|PMOS|W=0.9|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
1.049060e-06             4.010462e-06             2.701050e-03             2.723070e-03             
.END_DATA|PMOS|W=0.9|L=0.054|T=25
.START_DATA|PMOS|W=0.45|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
5.934943e-07             2.180627e-06             3.052977e-03             4.065239e-03             
.END_DATA|PMOS|W=0.45|L=0.054|T=25
.START_DATA|PMOS|W=0.45|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
5.904896e-07             2.173962e-06             3.044086e-03             4.079956e-03             
.END_DATA|PMOS|W=0.45|L=0.054|T=25
.START_DATA|PMOS|W=0.45|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
5.911961e-07             2.176800e-06             3.058773e-03             4.071740e-03             
.END_DATA|PMOS|W=0.45|L=0.054|T=25
.START_DATA|PMOS|W=0.27|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
3.820694e-07             1.586263e-06             5.233036e-03             6.476672e-03             
.END_DATA|PMOS|W=0.27|L=0.054|T=25
.START_DATA|PMOS|W=0.27|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
3.815546e-07             1.584274e-06             5.275437e-03             6.433514e-03             
.END_DATA|PMOS|W=0.27|L=0.054|T=25
.START_DATA|PMOS|W=0.27|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
3.821235e-07             1.591980e-06             5.315741e-03             6.443849e-03             
.END_DATA|PMOS|W=0.27|L=0.054|T=25
.START_DATA|PMOS|W=0.135|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
1.277010e-07             2.879723e-07             2.730498e-03             0.000000e+00             
.END_DATA|PMOS|W=0.135|L=0.054|T=25
.START_DATA|PMOS|W=0.135|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
1.219652e-07             2.730354e-07             2.220925e-03             0.000000e+00             
.END_DATA|PMOS|W=0.135|L=0.054|T=25
.START_DATA|PMOS|W=0.135|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
1.185730e-07             3.183252e-07             2.358071e-03             0.000000e+00             
.END_DATA|PMOS|W=0.135|L=0.054|T=25
.START_DATA|PMOS|W=0.108|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
1.436127e-07             5.884193e-07             1.788838e-03             5.331739e-03             
.END_DATA|PMOS|W=0.108|L=0.054|T=25
.START_DATA|PMOS|W=0.108|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
1.492550e-07             5.933234e-07             1.258345e-03             5.155446e-03             
.END_DATA|PMOS|W=0.108|L=0.054|T=25
.START_DATA|PMOS|W=0.108|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
1.409802e-07             5.608246e-07             1.917288e-03             5.461814e-03             
.END_DATA|PMOS|W=0.108|L=0.054|T=25
.START_DATA|PMOS|W=1.8|L=0.0405|T=25
idlin                    idsat                    vtlin                    vtsat
2.301875e-06             1.059447e-05             2.324275e-03             5.018670e-03             
.END_DATA|PMOS|W=1.8|L=0.0405|T=25
.START_DATA|PMOS|W=1.8|L=0.0405|T=25
idlin                    idsat                    vtlin                    vtsat
2.305268e-06             1.061461e-05             2.306970e-03             5.052857e-03             
.END_DATA|PMOS|W=1.8|L=0.0405|T=25
.START_DATA|PMOS|W=1.8|L=0.0405|T=25
idlin                    idsat                    vtlin                    vtsat
2.311376e-06             1.060345e-05             2.366953e-03             5.008623e-03             
.END_DATA|PMOS|W=1.8|L=0.0405|T=25
.START_DATA|PMOS|W=0.108|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.901958e-07             8.883907e-07             0.000000e+00             7.877750e-03             
.END_DATA|PMOS|W=0.108|L=0.036|T=25
.START_DATA|PMOS|W=0.108|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.850992e-07             9.147612e-07             0.000000e+00             7.800599e-03             
.END_DATA|PMOS|W=0.108|L=0.036|T=25
.START_DATA|PMOS|W=0.108|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.915336e-07             8.997172e-07             0.000000e+00             8.248550e-03             
.END_DATA|PMOS|W=0.108|L=0.036|T=25
.START_DATA|PMOS|W=9.0|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.216944e-05             8.032760e-05             4.648963e-03             7.553740e-03             
.END_DATA|PMOS|W=9.0|L=0.036|T=25
.START_DATA|PMOS|W=9.0|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.213744e-05             8.031494e-05             4.666670e-03             7.560290e-03             
.END_DATA|PMOS|W=9.0|L=0.036|T=25
.START_DATA|PMOS|W=9.0|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.214323e-05             8.026556e-05             4.672297e-03             7.557915e-03             
.END_DATA|PMOS|W=9.0|L=0.036|T=25
.START_DATA|PMOS|W=4.5|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.292480e-06             3.226489e-05             4.211209e-03             7.039973e-03             
.END_DATA|PMOS|W=4.5|L=0.036|T=25
.START_DATA|PMOS|W=4.5|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.268734e-06             3.223226e-05             4.205810e-03             7.038635e-03             
.END_DATA|PMOS|W=4.5|L=0.036|T=25
.START_DATA|PMOS|W=4.5|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.277542e-06             3.223275e-05             4.194408e-03             7.044641e-03             
.END_DATA|PMOS|W=4.5|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.022384e-06             4.985427e-06             3.181981e-04             5.214512e-03             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.017341e-06             4.928805e-06             8.746394e-04             4.908448e-03             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.005530e-06             4.924985e-06             9.223970e-04             4.901762e-03             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
9.962463e-07             4.388468e-06             7.167272e-03             9.712374e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.000056e-06             4.369768e-06             7.196065e-03             9.672060e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
9.935122e-07             4.350571e-06             7.122517e-03             9.701302e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.499820e-07             1.547966e-06             0.000000e+00             0.000000e+00             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.474844e-07             1.467570e-06             0.000000e+00             0.000000e+00             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.534692e-07             1.517538e-06             0.000000e+00             0.000000e+00             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.135|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.972979e-07             1.227254e-06             8.430843e-03             7.255010e-03             
.END_DATA|PMOS|W=0.135|L=0.036|T=25
.START_DATA|PMOS|W=0.135|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.966348e-07             1.224764e-06             8.239369e-03             7.191515e-03             
.END_DATA|PMOS|W=0.135|L=0.036|T=25
.START_DATA|PMOS|W=0.135|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.976568e-07             1.236653e-06             8.398535e-03             7.250835e-03             
.END_DATA|PMOS|W=0.135|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.697040e-06             7.572147e-06             7.308673e-03             1.019840e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.694753e-06             7.593490e-06             7.284439e-03             1.022692e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.698819e-06             7.601746e-06             7.302717e-03             1.019646e-02             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.474455e-06             6.768193e-06             4.382571e-03             8.342600e-03             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.485356e-06             6.747266e-06             4.338771e-03             8.356866e-03             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.483325e-06             6.749233e-06             4.278815e-03             8.358598e-03             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.055667e-06             4.893752e-06             9.666715e-04             5.589177e-03             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.042467e-06             4.923459e-06             1.243395e-03             5.368722e-03             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.036748e-06             4.936626e-06             1.276160e-03             5.348628e-03             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.118922e-06             5.365859e-06             3.751689e-03             5.329775e-03             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.145277e-06             5.455223e-06             3.363058e-03             5.279883e-03             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.131202e-06             5.381664e-06             3.653108e-03             5.340622e-03             
.END_DATA|PMOS|W=0.9|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
9.802135e-07             4.148568e-06             6.553129e-03             6.995006e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
9.771442e-07             4.159882e-06             6.731234e-03             7.136239e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
9.766294e-07             4.160354e-06             6.757291e-03             7.140111e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.002157e-06             4.079941e-06             2.364637e-03             5.592131e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.005732e-06             4.071866e-06             2.079253e-03             5.672513e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
9.975704e-07             4.081187e-06             2.282433e-03             5.681661e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
9.538277e-07             4.566381e-06             5.771071e-03             9.294419e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
9.669813e-07             4.601511e-06             5.796415e-03             9.241907e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
9.703918e-07             4.590380e-06             5.747570e-03             9.242289e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.075075e-06             4.496672e-06             2.144153e-03             5.841625e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.067452e-06             4.458328e-06             1.416992e-03             5.820184e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.073574e-06             4.496736e-06             2.159075e-03             5.902647e-03             
.END_DATA|PMOS|W=0.54|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.353321e-07             1.547273e-06             5.888245e-03             7.099442e-03             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.482740e-07             1.471384e-06             4.953854e-03             6.300150e-03             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.399847e-07             1.454098e-06             5.083270e-03             6.289591e-03             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.977820e-07             1.390115e-06             0.000000e+00             0.000000e+00             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.099833e-07             1.426393e-06             0.000000e+00             0.000000e+00             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.032172e-07             1.404880e-06             0.000000e+00             0.000000e+00             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.313339e-07             2.302698e-06             5.794925e-03             9.381498e-03             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.370001e-07             2.310189e-06             5.989920e-03             9.708351e-03             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.862082e-07             2.148518e-06             5.002147e-03             8.971032e-03             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.707531e-07             1.989746e-06             4.901779e-03             8.349242e-03             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.681627e-07             2.015063e-06             4.976712e-03             8.060800e-03             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
.START_DATA|PMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.569229e-07             1.990376e-06             4.882076e-03             8.316669e-03             
.END_DATA|PMOS|W=0.27|L=0.036|T=25
