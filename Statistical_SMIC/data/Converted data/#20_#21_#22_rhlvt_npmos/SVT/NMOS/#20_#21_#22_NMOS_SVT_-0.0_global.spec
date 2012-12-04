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
.START_DATA|NMOS|W=4.5|L=7.2|T=25
idlin                    idsat                    vtlin                    vtsat
7.353947e-08             5.428956e-07             3.471439e-03             3.432000e-03             
.END_DATA|NMOS|W=4.5|L=7.2|T=25
.START_DATA|NMOS|W=4.5|L=7.2|T=25
idlin                    idsat                    vtlin                    vtsat
7.355528e-08             5.429759e-07             3.474955e-03             3.429886e-03             
.END_DATA|NMOS|W=4.5|L=7.2|T=25
.START_DATA|NMOS|W=4.5|L=7.2|T=25
idlin                    idsat                    vtlin                    vtsat
7.360074e-08             5.432217e-07             3.474380e-03             3.431108e-03             
.END_DATA|NMOS|W=4.5|L=7.2|T=25
.START_DATA|NMOS|W=1.8|L=1.8|T=25
idlin                    idsat                    vtlin                    vtsat
1.265284e-07             8.694485e-07             3.361661e-03             2.668943e-03             
.END_DATA|NMOS|W=1.8|L=1.8|T=25
.START_DATA|NMOS|W=1.8|L=1.8|T=25
idlin                    idsat                    vtlin                    vtsat
1.266402e-07             8.693826e-07             3.356067e-03             2.664536e-03             
.END_DATA|NMOS|W=1.8|L=1.8|T=25
.START_DATA|NMOS|W=1.8|L=1.8|T=25
idlin                    idsat                    vtlin                    vtsat
1.266794e-07             8.697455e-07             3.357260e-03             2.665415e-03             
.END_DATA|NMOS|W=1.8|L=1.8|T=25
.START_DATA|NMOS|W=0.9|L=0.9|T=25
idlin                    idsat                    vtlin                    vtsat
1.239172e-07             8.698164e-07             4.756418e-03             6.060892e-03             
.END_DATA|NMOS|W=0.9|L=0.9|T=25
.START_DATA|NMOS|W=0.9|L=0.9|T=25
idlin                    idsat                    vtlin                    vtsat
1.237802e-07             8.707562e-07             4.765437e-03             6.092629e-03             
.END_DATA|NMOS|W=0.9|L=0.9|T=25
.START_DATA|NMOS|W=0.9|L=0.9|T=25
idlin                    idsat                    vtlin                    vtsat
1.239165e-07             8.694452e-07             4.768341e-03             6.055647e-03             
.END_DATA|NMOS|W=0.9|L=0.9|T=25
.START_DATA|NMOS|W=0.9|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
2.219669e-06             7.523143e-06             6.298823e-03             4.494547e-03             
.END_DATA|NMOS|W=0.9|L=0.054|T=25
.START_DATA|NMOS|W=0.9|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
2.226682e-06             7.523190e-06             6.315039e-03             4.530977e-03             
.END_DATA|NMOS|W=0.9|L=0.054|T=25
.START_DATA|NMOS|W=0.9|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
2.217317e-06             7.511149e-06             6.316376e-03             4.494171e-03             
.END_DATA|NMOS|W=0.9|L=0.054|T=25
.START_DATA|NMOS|W=0.45|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
9.775779e-07             3.226465e-06             1.286223e-03             5.043922e-03             
.END_DATA|NMOS|W=0.45|L=0.054|T=25
.START_DATA|NMOS|W=0.45|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
9.684416e-07             3.227524e-06             1.514903e-03             5.092760e-03             
.END_DATA|NMOS|W=0.45|L=0.054|T=25
.START_DATA|NMOS|W=0.45|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
9.683494e-07             3.233754e-06             1.451860e-03             5.054456e-03             
.END_DATA|NMOS|W=0.45|L=0.054|T=25
.START_DATA|NMOS|W=0.27|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
8.864339e-07             3.382442e-06             6.662396e-03             7.348416e-03             
.END_DATA|NMOS|W=0.27|L=0.054|T=25
.START_DATA|NMOS|W=0.27|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
8.879078e-07             3.389187e-06             6.682583e-03             7.363415e-03             
.END_DATA|NMOS|W=0.27|L=0.054|T=25
.START_DATA|NMOS|W=0.27|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
8.893788e-07             3.391059e-06             6.743808e-03             7.377982e-03             
.END_DATA|NMOS|W=0.27|L=0.054|T=25
.START_DATA|NMOS|W=0.135|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
6.096418e-07             2.299812e-06             5.584883e-03             8.050049e-03             
.END_DATA|NMOS|W=0.135|L=0.054|T=25
.START_DATA|NMOS|W=0.135|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
6.151288e-07             2.266144e-06             5.761334e-03             8.021307e-03             
.END_DATA|NMOS|W=0.135|L=0.054|T=25
.START_DATA|NMOS|W=0.135|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
6.086575e-07             2.267401e-06             5.436656e-03             8.036207e-03             
.END_DATA|NMOS|W=0.135|L=0.054|T=25
.START_DATA|NMOS|W=0.108|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
2.514928e-07             1.246143e-06             1.503974e-02             1.545831e-02             
.END_DATA|NMOS|W=0.108|L=0.054|T=25
.START_DATA|NMOS|W=0.108|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
2.723007e-07             1.188827e-06             1.506120e-02             1.564314e-02             
.END_DATA|NMOS|W=0.108|L=0.054|T=25
.START_DATA|NMOS|W=0.108|L=0.054|T=25
idlin                    idsat                    vtlin                    vtsat
2.679048e-07             1.180934e-06             1.505822e-02             1.569347e-02             
.END_DATA|NMOS|W=0.108|L=0.054|T=25
.START_DATA|NMOS|W=1.8|L=0.0405|T=25
idlin                    idsat                    vtlin                    vtsat
3.139067e-06             1.791120e-05             0.000000e+00             3.285080e-03             
.END_DATA|NMOS|W=1.8|L=0.0405|T=25
.START_DATA|NMOS|W=1.8|L=0.0405|T=25
idlin                    idsat                    vtlin                    vtsat
3.127844e-06             1.792222e-05             0.000000e+00             3.346887e-03             
.END_DATA|NMOS|W=1.8|L=0.0405|T=25
.START_DATA|NMOS|W=1.8|L=0.0405|T=25
idlin                    idsat                    vtlin                    vtsat
3.192036e-06             1.794207e-05             0.000000e+00             3.296998e-03             
.END_DATA|NMOS|W=1.8|L=0.0405|T=25
.START_DATA|NMOS|W=0.108|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.614673e-07             1.850896e-06             1.194650e-02             1.298955e-02             
.END_DATA|NMOS|W=0.108|L=0.036|T=25
.START_DATA|NMOS|W=0.108|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.852486e-07             1.874315e-06             1.164629e-02             1.280073e-02             
.END_DATA|NMOS|W=0.108|L=0.036|T=25
.START_DATA|NMOS|W=0.108|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
4.778324e-07             1.875809e-06             1.140027e-02             1.272890e-02             
.END_DATA|NMOS|W=0.108|L=0.036|T=25
.START_DATA|NMOS|W=9.0|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.500557e-05             2.553742e-04             3.912888e-03             6.177525e-03             
.END_DATA|NMOS|W=9.0|L=0.036|T=25
.START_DATA|NMOS|W=9.0|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.501407e-05             2.553865e-04             3.907411e-03             6.174258e-03             
.END_DATA|NMOS|W=9.0|L=0.036|T=25
.START_DATA|NMOS|W=9.0|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.500046e-05             2.553766e-04             3.909698e-03             6.186562e-03             
.END_DATA|NMOS|W=9.0|L=0.036|T=25
.START_DATA|NMOS|W=4.5|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.125380e-05             7.977905e-05             3.622314e-03             5.947620e-03             
.END_DATA|NMOS|W=4.5|L=0.036|T=25
.START_DATA|NMOS|W=4.5|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.124407e-05             7.976381e-05             3.615879e-03             5.967393e-03             
.END_DATA|NMOS|W=4.5|L=0.036|T=25
.START_DATA|NMOS|W=4.5|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.123698e-05             7.976559e-05             3.611749e-03             5.972670e-03             
.END_DATA|NMOS|W=4.5|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.949159e-06             1.371052e-05             4.116555e-03             7.050227e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.942545e-06             1.371222e-05             4.083859e-03             7.070188e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.953731e-06             1.373234e-05             4.121616e-03             7.075502e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.911888e-07             4.061305e-06             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
7.051936e-07             4.024695e-06             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.919646e-07             4.037967e-06             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.923698e-07             3.725475e-06             0.000000e+00             2.613575e-03             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.987741e-07             3.736492e-06             0.000000e+00             2.060891e-03             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
6.999807e-07             3.729908e-06             0.000000e+00             1.905192e-03             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.135|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
0.000000e+00             0.000000e+00             0.000000e+00             1.076404e-03             
.END_DATA|NMOS|W=0.135|L=0.036|T=25
.START_DATA|NMOS|W=0.135|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
0.000000e+00             0.000000e+00             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.135|L=0.036|T=25
.START_DATA|NMOS|W=0.135|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
0.000000e+00             0.000000e+00             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.135|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.280327e-06             1.286200e-05             6.055053e-03             6.424961e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.279890e-06             1.284948e-05             6.056331e-03             6.467723e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.295327e-06             1.285472e-05             6.094440e-03             6.459294e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.267818e-06             1.413986e-05             6.511360e-03             9.294810e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.249555e-06             1.414632e-05             6.504024e-03             9.307255e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
3.241356e-06             1.416739e-05             6.541465e-03             9.268481e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.135577e-06             8.040311e-06             8.937870e-03             9.814835e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.120990e-06             8.021752e-06             8.860925e-03             1.022439e-02             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.178735e-06             8.146637e-06             8.772509e-03             9.712856e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.467543e-06             9.416434e-06             8.523002e-03             9.515417e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.478296e-06             9.391717e-06             8.480337e-03             9.478622e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.9|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.475304e-06             9.400820e-06             8.518014e-03             9.495810e-03             
.END_DATA|NMOS|W=0.9|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.874088e-06             1.307596e-05             0.000000e+00             2.322005e-03             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.848088e-06             1.305214e-05             0.000000e+00             2.485020e-03             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.858664e-06             1.302208e-05             0.000000e+00             2.418534e-03             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.754026e-06             1.211999e-05             6.066636e-03             7.684894e-03             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.752673e-06             1.211922e-05             6.115095e-03             7.697158e-03             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.740686e-06             1.211504e-05             6.095142e-03             7.676707e-03             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.124482e-06             8.016275e-06             8.796137e-03             1.007237e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.177450e-06             8.115547e-06             8.690900e-03             9.959084e-03             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.166854e-06             8.132171e-06             8.642728e-03             1.001192e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.478978e-06             9.405914e-06             8.428386e-03             9.500045e-03             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.483050e-06             9.413160e-06             8.394155e-03             9.510297e-03             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.54|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
2.453330e-06             9.484925e-06             8.648069e-03             1.025273e-02             
.END_DATA|NMOS|W=0.54|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.678194e-07             2.456207e-06             6.984909e-03             1.130136e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.653188e-07             2.466314e-06             6.978114e-03             1.124433e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.978994e-07             2.501025e-06             6.818130e-03             1.142741e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.550365e-07             2.101401e-06             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.789105e-07             2.117528e-06             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
5.572792e-07             2.084221e-06             0.000000e+00             0.000000e+00             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.606952e-06             5.770259e-06             1.416485e-02             1.159320e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.560674e-06             5.804452e-06             1.405977e-02             1.308438e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.576642e-06             5.806235e-06             1.409215e-02             1.310108e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.190099e-06             4.302118e-06             8.574730e-03             1.074232e-02             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.205000e-06             4.342134e-06             8.777001e-03             9.880318e-03             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
.START_DATA|NMOS|W=0.27|L=0.036|T=25
idlin                    idsat                    vtlin                    vtsat
1.115330e-06             3.929685e-06             8.376958e-03             9.399169e-03             
.END_DATA|NMOS|W=0.27|L=0.036|T=25
